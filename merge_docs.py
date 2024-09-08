import os

def merge_markdown_files():
    # Initialize merged content
    merged_content = ""

    # Define file paths in the order specified in SUMMARY.md
    files_to_merge = [
        "README.md", "README (1).md", "SUMMARY.md", "contribute-to-the-book.md",
        "basic-tutorials/a-shells-differences.md",
        "basic-tutorials/configure-fonts-colors-and-the-toolbar.md",
        "basic-tutorials/configure-the-shell.md",
        "basic-tutorials/configure-lg2-for-version-controlling.md",
        "basic-tutorials/configure-your-vim.md",
        "basic-tutorials/run-jupyter.md",
        "lets-do-more-for-it/before-the-hard-part.md",
        "lets-do-more-for-it/compile-a-shell-yourself.md",
        "lets-do-more-for-it/compile-a-simple-command-with-a-shell.md",
        "lets-do-more-for-it/submit-new-packages.md",
        "lets-do-more-for-it/webassembly-for-a-shell.md",
        "ended.md"
    ]

    # Read each file and append its content to merged_content
    for file_path in files_to_merge:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                merged_content += f"\n\n# {file_path}\n\n{content}"

    # Write the merged content to a new file
    with open("merged-docs.md", 'w') as f:
        f.write(merged_content)

if __name__ == "__main__":
    merge_markdown_files()