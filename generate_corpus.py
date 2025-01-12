import os

# Define paths
base_dir = os.path.join(os.getcwd(), "content/posts")
output_file = os.path.abspath(os.path.join(os.getcwd(), "..", "blog_content.txt"))

# Folders to process
folders = ["2024", "2025"]

# Accumulator for the text
corpus = []

# Process each folder
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    print(f"Processing folder: {folder_path}")  # Debug
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".md"):
                file_path = os.path.join(folder_path, file_name)
                print(f"Reading file: {file_path}")  # Debug
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        corpus.append(content)
                        print(f"File content length: {len(content)}")  # Debug
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    else:
        print(f"Folder does not exist: {folder_path}")  # Debug

# Write the cumulative corpus to the output file
print(f"Writing to output file: {output_file}")  # Debug
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(corpus))

if corpus:
    print(f"Corpus written successfully. Total length: {len('\n\n'.join(corpus))}")
else:
    print("No content was added to the corpus.")