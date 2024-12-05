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

3. Start development server:
   ```bash
   npm run dev
   ```

4. Build for production:
   ```bash
   npm run build
   ```

## Development Workflow

- `npm run dev` starts both:
  - Hugo server (localhost:1313)
  - Tailwind CSS watcher
  - Changes to content/CSS auto-reload

## Production Build and Deployment

1. Local Build:
   ```bash
   npm run build
   ```
   This command:
   - Processes Tailwind CSS
   - Builds Hugo site
   - Output goes to /public

2. Commit the changes:
   ```bash
   git add .
   git commit -m "Update site content"
   git push origin main
   ```
   Important: The /public directory must be committed as it contains the built site.

3. Deployment:
   - The site automatically deploys to GitHub Pages when changes are pushed to main
   - The deployment uses the pre-built files from the /public directory
   - No build process runs on GitHub - only deployment
   - Site becomes available at thingsithinkithink.blog

## Site Configuration

Edit hugo.toml for site settings: