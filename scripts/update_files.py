import json

def read_words():
    with open('words-and-phrases.txt', 'r') as f:
        return [line.strip() for line in f if line.strip()]

def update_markdown(words):
    with open('words-and-phrases.md', 'w') as f:
        f.write("# Cursed Words and Phrases\n\n")
        for word in words:
            f.write(f"- {word}\n")

def update_json(words):
    data = {"cursed_words": words}
    with open('words-and-phrases.json', 'w') as f:
        json.dump(data, f, indent=2)

def update_html(words):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cursed Words and Phrases</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
            h1 { color: #333; }
            ul { list-style-type: none; padding: 0; }
            li { margin-bottom: 10px; }
        </style>
    </head>
    <body>
        <h1>Cursed Words and Phrases</h1>
        <ul>
    """
    
    for word in words:
        html_content += f"        <li>{word}</li>\n"
    
    html_content += """
        </ul>
    </body>
    </html>
    """
    
    with open('index.html', 'w') as f:
        f.write(html_content)

def main():
    words = read_words()
    update_markdown(words)
    update_json(words)
    update_html(words)
    print("All formats updated successfully.")

if __name__ == "__main__":
    main()