"""BE CAREFUL AND SET THE CORRECT HTML_DIRECTORY PATH."""

import os
html_directory = os.getcwd()
print(html_directory)
css_link = '<link rel="stylesheet" type="text/css" href="styles.css">'

for filename in os.listdir(html_directory):
    if filename.endswith(".html"):
        file_path = os.path.join(html_directory, filename)
        
        # Read the content of the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Insert the CSS link before the closing </head> tag
        if '</head>' in content:
            content = content.replace('</head>', f'    {css_link}\n</head>')
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
