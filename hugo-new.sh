#!/bin/bash

# Initialize variables
CUSTOM_DATE=""

# Parse command line arguments
while getopts "d:" opt; do
  case $opt in
    d)
      # Handle both YYYYMMDD and YYMMDD formats
      if [ ${#OPTARG} -eq 8 ]; then
        YEAR="${OPTARG:0:4}"
        MONTH="${OPTARG:4:2}"
        DAY="${OPTARG:6:2}"
      else
        YEAR="20${OPTARG:0:2}"
        MONTH="${OPTARG:2:2}"
        DAY="${OPTARG:4:2}"
      fi
      CUSTOM_DATE="${YEAR}-${MONTH}-${DAY}T12:00:00Z"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# Shift the arguments to get the title after the options
shift $((OPTIND-1))

# Check if a title was provided
if [ -z "$1" ]; then
  echo "Please provide a title for the post."
  echo "Usage: $0 [-d YYMMDD|YYYYMMDD] \"Post Title\""
  exit 1
fi

# Set the date and year
if [ -z "$CUSTOM_DATE" ]; then
  # Use current date if no custom date provided
  CUSTOM_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  YEAR=$(date +%Y)
  MONTH_DAY=$(date +%m-%d)
else
  # Use the year and month-day from custom date
  YEAR="${CUSTOM_DATE:0:4}"
  MONTH_DAY="${MONTH}-${DAY}"
fi

# Format the title for the filename only (lowercase with hyphens)
FILENAME=$(echo "$1" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]/-/g')

# Create the post using Hugo
hugo new "posts/$YEAR/$MONTH_DAY-$FILENAME.md"

# Update the title and date in the new post
POST_PATH="content/posts/$YEAR/$MONTH_DAY-$FILENAME.md"

# Replace the frontmatter with our custom version
sed -i "s/+++/---/g" "$POST_PATH"  # Convert +++ to ---
sed -i "s/title:.*$/title: \"$1\"/" "$POST_PATH"  # Preserve original title case
sed -i "s/date:.*$/date: $CUSTOM_DATE/" "$POST_PATH"

echo "Post created at $POST_PATH"