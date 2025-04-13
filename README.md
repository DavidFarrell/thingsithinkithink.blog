# thingsithinkithink.blog

A personal blog built with Hugo using the Pehtheme-Hugo theme.

## Quick Start

1. Install required software:

   - Hugo (v0.116.0 or higher)
   - NodeJS (for Tailwind CSS)

2. Install Node dependencies:
   ```bash
   npm install
   ```

## Local Development

There are two main ways to run the site locally, depending on what you're working on:

1. For content development and general testing:

   ```bash
   hugo server -D --disableFastRender --poll 500ms
   ```

   This command:

   - Starts the Hugo server (localhost:1313)
   - `-D`: Includes draft posts
   - `--disableFastRender`: Ensures full page rebuilds for accurate previews
   - `--poll 500ms`: Watches for file changes every 500ms (more reliable than default)

2. For Tailwind CSS development:
   ```bash
   npm run dev
   ```
   Only use this command when actively working on Tailwind CSS styles. It:
   - Starts the Hugo server
   - Watches for Tailwind CSS changes
   - Processes CSS changes in real-time

## Creating New Posts

Use the `hugo-new.sh` script to create new posts:

1. Basic usage (creates post with current date):

   ```bash
   ./hugo-new.sh "Your Post Title"
   ```

2. With custom date (supports both YYMMDD and YYYYMMDD formats):
   ```bash
   ./hugo-new.sh -d 241205 "Your Post Title"
   # or
   ./hugo-new.sh -d 20241205 "Your Post Title"
   ```

The script will:

- Create a new markdown file in `content/posts/YEAR/`
- Add the date prefix to the filename (MM-DD-title)
- Preserve original title capitalization in the frontmatter
- Set the post date (current or specified)

## Production Build and Deployment

1. Using the build script (recommended):

   ```bash
   ./build.sh "Your commit message"
   ```

   This script automates the entire build and deployment process:

   - Builds the site with npm run build
   - Stages all changes with git add .
   - Commits with your provided message
   - Pushes to the remote repository

2. Manual Build:

   ```bash
   npm run build
   ```

   This command:

   - Processes Tailwind CSS
   - Builds Hugo site
   - Output goes to /public

3. Manual Deployment:

   ```bash
   git add .
   git commit -m "Update site content"
   git push origin main
   ```

   Important: The /public directory must be committed as it contains the built site.

4. Deployment Result:
   - The site automatically deploys to GitHub Pages when changes are pushed to main
   - The deployment uses the pre-built files from the /public directory
   - No build process runs on GitHub - only deployment
   - Site becomes available at thingsithinkithink.blog

## Site Configuration

Edit hugo.toml for site settings:
