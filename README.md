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

- `npm run build` creates production build:
  - Processes Tailwind CSS
  - Builds Hugo site
  - Output goes to /public

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the main branch. The deployment process:

1. Builds the Hugo site with Tailwind CSS
2. Deploys to GitHub Pages
3. Makes the site available at thingsithinkithink.blog

## Site Configuration

Edit hugo.toml for site settings: