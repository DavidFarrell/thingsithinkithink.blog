#!/bin/bash

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