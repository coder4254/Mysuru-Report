"""BE CAREFUL AND SET THE CORRECT HTML_DIRECTORY PATH."""

import os

css_link = '<link rel="stylesheet" type="text/css" href="styles.css">\n\n'

current_directory = os.getcwd()

# Loop through each HTML file in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith(".html"):
        file_path = os.path.join(current_directory, filename)
        
        # Read the content of the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if the CSS link is already present
        if css_link not in content:
            # Insert the CSS link at the first line
            content = css_link + content
        
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)

print("CSS link has been added to the first line of all HTML files in the current directory.")
