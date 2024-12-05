#!/bin/bash

# Check if a title was provided
if [ -z "$1" ]; then
  echo "Please provide a title for the post."
  exit 1
fi

# Get the current date
DATE=$(date +%Y-%m-%d)
YEAR=$(date +%Y)
MONTH_DAY=$(date +%m-%d)

# Format the title for the filename
FILENAME=$(echo "$1" | tr '[:upper:]' '[:lower:]' | sed 's/ /_/g' | sed 's/[^a-z0-9_]/_/g')

# Create the post using Hugo
hugo new "posts/$YEAR/$MONTH_DAY_$FILENAME.md"

# Update the title in the new post
POST_PATH="content/posts/$YEAR/$MONTH_DAY_$FILENAME.md"
sed -i "s/title = ''/title = '$1'/g" "$POST_PATH"

echo "Post created at $POST_PATH"