npm run build

hugo server -D --buildFuture --disableFastRender --poll 500ms

python generate_corpus.py

## Creating a New Post with `hugo-new.sh`

The `hugo-new.sh` helper script lets you generate a properly-named Markdown file with the correct front-matter in a single command.

Basic usage:

```bash
./hugo-new.sh "My Awesome Blog Post"
```

This will:

1. Put the new file under `content/posts/<current-year>/`.
2. Prepend the current date (MM-DD) to the filename in kebab-case → `MM-DD-my-awesome-blog-post.md`.
3. Fill the front-matter `title` and `date` fields automatically.

### Using a Custom Date

You can optionally pass a date with `-d` in either `YYMMDD` or `YYYYMMDD` format:

```bash
# Same day in 2025 – short form
./hugo-new.sh -d 250101 "New Year, New Me"

# 2024-12-05 – long form
./hugo-new.sh -d 20241205 "Throwback Thursday"
```

The script converts that into an ISO timestamp (`YYYY-MM-DDT12:00:00Z`) and places the post in the appropriate year folder.

Run `./hugo-new.sh -h` to see the built-in help text.

---

## Building & Deploying with `build.sh`

`build.sh` is a convenience wrapper around the typical build / commit / push workflow. It expects **one argument** – the commit message:

```bash
./build.sh "🚀 Ship new post about Hugo helpers"
```

What it does:

1. Runs `npm run build` to compile the site / assets.
2. `git add .` – stages all changes.
3. `git commit -m "<your message>"` – commits them.
4. `git push` – pushes to the current remote.

If any step fails, the script exits with an error so you can fix the problem before continuing.

Tip: Make the script executable once (if necessary) with `chmod +x build.sh` – same for `hugo-new.sh`.
