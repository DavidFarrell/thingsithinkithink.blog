---
title: "Building an AI Sandbox with Docker"
date: 2025-11-11T12:00:00Z
slug: /11-11-building-an-ai-sandbox-with-docker/
description: "How to set up a persistent Docker environment for AI coding tools without losing your authentication every time you restart the container."
image: /images/2025/11-11-docker-sandbox.png
caption: "Claude can do whatever it likes inside the sandbox"
categories:
  - coding
  - tools
  - artificial-intelligence
tags:
  - docker
  - claude-code
  - development
  - tooling
draft: false
---

I love Claude Code. I enjoy using coding agents, especially for quick and dirty things that I just need to get working for myself. I use them for all sorts of things, from writing my blog to using Claude Code as a [personal stylist](https://www.linkedin.com/posts/davidfarrell81_huge-thanks-to-eddie-forson-wilfred-kasekende-activity-7393335244239634432-e2Cw?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAKU3ZoBTHvzXgiOPqYTeQuTbQUqniMdk48) to dress me for a wedding I was attending. But when I'm doing coding things, I'm always wary of the potential ways that coding agents could mess up my system.

There was one instance where I was using Claude Code and it didn't respect my desire to always use the virtual environment. It installed a whole bunch of pip packages into my default Python and broke some things. Since then I've always been wary of running Claude Code without some mechanisms in place to protect me. I know that Claude is quite respectful of the project working directory, but it's still possible for it to do things you don't really like with your machine. Especially when you accidentally hit 2 instead of 1 and give it all its permissions.

So I started thinking it would be good to run it inside a sandbox, and the easiest way I know to create a sandbox is inside a Docker container. I thought this was the kind of thing that everybody does, and in fact when I was at the [AI Engineer conference in Paris](https://www.ai.engineer/paris), I asked the folks at the Docker stand if they had a recommendation. They didn't have a recommendation for me and they didn't seem to have heard anybody asking for anything like it before. So maybe I'm doing something silly here actually. I'm not 100% sure that I haven't missed something important.

However, on Friday last week I was showing something off to people at the [Claude Code meetup in London](https://www.linkedin.com/feed/update/urn:li:activity:7393619147105923073/), and people seemed interested in my little Docker sandbox. So I thought I would write a blog post about it here.

## The Basic Idea

You basically need three things:

- A Docker container that sets up a development environment
- A docker-compose file that mounts various folders between my real PC (in my case a Mac) and the Docker image so that when I'm working on stuff inside the Docker container, it's mapped onto a specific folder on my hard drive
- A bash script that updates my tools so that every time I run the container, I've always got the latest version of Claude Code

I used Claude Code to create these files for me, and I'd recommend you do the same. This is well within Claude's comfortable capabilities - you don't need my actual files, just ask it to set up a Docker sandbox for AI coding tools.

There were a few wee snags I had along the way, mostly around getting Claude authenticated automatically each time I enter a new sandbox, saving me having to create auth for GitHub, and how to tear down the Docker image automatically every time I use it. I'm going to share those here.

## The docker-compose File

The docker-compose file handles the volume mounts between your host machine and the container. Here's what mine looks like:

```yaml
services:
  dev-sandbox:
    build: .
    volumes:
      # Your actual project code
      - ./projects:/workspace/projects:rw

      # Claude settings and auth (stays persistent!)
      - ./claude-settings:/home/dev/.claude:rw

      # Git config and SSH keys (read-only for safety)
      - ~/.gitconfig:/home/dev/.gitconfig:ro
      - ~/.ssh:/home/dev/.ssh:ro

    working_dir: /workspace/projects
    stdin_open: true
    tty: true
    ports:
      - "3000:3000"
```

The line `./claude-settings:/home/dev/.claude:rw` fixes the authentication problem. By mounting a local folder to where Claude Code stores its config, your authentication persists across container restarts. I use the same method to have OpenCode persist its authentication too.

The lines with `~/.gitconfig` and `~/.ssh` handle the GitHub authentication. By mounting your git config and SSH keys as read-only (`:ro`), you don't have to set up SSH keys inside the container. It just works.

The `working_dir: /workspace/projects` line sets your working directory so when the container starts, you're already in the right place.

The `ports` line maps port 3000 from inside the container to port 3000 on your host machine. This means if you run a server on port 3000 inside the container (like a FastHTML app or an MCP server you're testing), you can access it from your browser on your main machine. Sometimes I run multiple servers - FastHTML, a couple of MCP servers to test them out - and I have to map each port. It works, but it's just enough friction that sometimes I write code in Claude Code inside Docker but then actually run the server on my main Mac because I'm too lazy to think about port mappings.

## The Dockerfile

Nothing particularly clever here:

```dockerfile
FROM ubuntu:22.04

# Install basics
RUN apt-get update && apt-get install -y \
    git curl build-essential python3 nodejs npm \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user with sudo access
RUN useradd -m -s /bin/bash dev && \
    usermod -aG sudo dev && \
    echo 'dev ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER dev
WORKDIR /workspace

# Install Claude Code
RUN curl -fsSL https://claude.ai/install.sh | bash
RUN echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Copy entrypoint script
COPY --chown=dev:dev docker-entrypoint.sh /home/dev/docker-entrypoint.sh
RUN chmod +x /home/dev/docker-entrypoint.sh

ENTRYPOINT ["/home/dev/docker-entrypoint.sh"]
CMD ["/bin/bash"]
```

The lines with `useradd` and `usermod` create a non-root user with passwordless sudo. This means you can install packages inside the container if you need to, but you're not running everything as root by default.

The `curl -fsSL https://claude.ai/install.sh | bash` line installs Claude Code at build time. The entrypoint script (which we'll get to) keeps it updated at runtime.

## The Entrypoint Script

This runs every time the container starts:

```bash
#!/bin/bash
export PATH="$HOME/.local/bin:$PATH"

echo "========================================"
echo "Checking for updates..."
echo "========================================"

# Auto-update Claude Code if it exists, otherwise install it
if command -v claude &> /dev/null; then
    echo "Claude found at: $(which claude)"
    echo "Current version: $(claude --version 2>/dev/null || echo 'version check failed')"
    echo "Updating Claude Code..."
    claude update || {
        echo "Built-in update failed, reinstalling..."
        curl -fsSL https://claude.ai/install.sh | bash
    }
else
    echo "Installing Claude Code..."
    curl -fsSL https://claude.ai/install.sh | bash
fi

echo "========================================"
echo "Claude Code: $(claude --version)"
echo "========================================"

exec "$@"
```

The `if command -v claude` section handles the update logic. It tries Claude's built-in `claude update` command first (faster), and falls back to a fresh install if that fails. Your Dockerfile installs it at build time, but this keeps it current without rebuilding the entire image.

## Running It

You need to use `--rm` when you run the container. Without it, you'll end up collecting a bunch of Docker containers that aren't running and it's messy - you'll have all this cruft inside your system.

I created a little bash script called `dev.sh` that sets it up for me, so I just do `./dev`:

```bash
#!/bin/bash
# Quick script to start the AI development sandbox
docker-compose run --rm dev-sandbox bash
```

When you exit the container, it gets removed automatically. No accumulation of dead containers cluttering your Docker.

## A Few Things That Caught Me Out

**Create the mounted directories first.** Before you run the container for the first time, create `./claude-settings` on your host machine. If you don't, Docker will create it with root permissions and you'll have to fix the permissions manually.

**Mount sensitive files as read-only.** Your `.gitconfig` and `.ssh` keys get mounted with `:ro` so AI tools can't accidentally modify them. Your project files and AI tool configs get `:rw` because those need to change.

## thingsithinkithink

- I mentioned above that you should get Claude to do this for you - you don't need my files. What I'd actually recommend is that you just copy this entire blog post, paste it into Claude and say "Claude, hey, do this for me."

- I'm surprised there's not a better or more standard way of doing this that somebody else has already figured out. I'm assuming that there is and I've just missed it. If anybody knows of one, please email me or get in touch.
