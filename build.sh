#!/bin/bash
#
# Build + deploy thingsithinkithink.blog.   Usage:  ./build.sh "commit message"
#
# This is the ONE correct way to publish. It runs the production build
# (npm run build = tailwind CSS + `hugo --environment production`) into ./public,
# then commits everything (including public/) and pushes.
#
# WHY commit public/: the GitHub Action only UPLOADS ./public - it does NOT run
# Hugo. The built site must be generated locally and committed, which this does.
#
# NEVER `git commit` right after `hugo server` / `npm run dev`: the dev server
# rewrites public/ with localhost:1313 URLs. Always run THIS script (a clean
# production build) before committing so the live URLs are correct.
#
# Hero image missing? Hugo writes _hu_-suffixed image variants under
# resources/_gen/images/ during the local build; if a post's hero won't render,
# check resources/_gen has entries for it (they only exist after a local build).

# Check if a commit message was provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide a commit message"
    echo "Usage: ./build \"your commit message\""
    exit 1
fi

# Store the commit message
COMMIT_MESSAGE="$1"

# Echo what we're about to do
echo "Building project and deploying with message: \"$COMMIT_MESSAGE\""

# Run npm build
echo "Running npm build..."
npm run build
if [ $? -ne 0 ]; then
    echo "Error: npm build failed"
    exit 1
fi

# Add all files
echo "Adding files to git..."
git add .
if [ $? -ne 0 ]; then
    echo "Error: git add failed"
    exit 1
fi

# Commit with message
echo "Committing changes..."
git commit -m "$COMMIT_MESSAGE"
if [ $? -ne 0 ]; then
    echo "Error: git commit failed"
    exit 1
fi

# Push changes
echo "Pushing to remote..."
git push
if [ $? -ne 0 ]; then
    echo "Error: git push failed"
    exit 1
fi

echo "Build and deploy completed successfully!" 