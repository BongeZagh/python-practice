import webbrowser

def generate_mermaid_html(mermaid_code):
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mermaid Mind Map Editor</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <script>
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        <style>
            #container {{
                display: flex;
            }}
            #code-editor, #mind-map {{
                width: 50%;
                height: 100vh;
            }}
        </style>
    </head>
    <body>
        <div id="container">
            <textarea id="code-editor">{}</textarea>
            <div id="mind-map"></div>
        </div>
        <script>
            const codeEditor = document.getElementById('code-editor');
            const mindMap = document.getElementById('mind-map');

            function updateMindMap() {{
                const mermaidCode = codeEditor.value;
                
                mermaid.render('mind-map', mermaidCode, svg => {{
                    mindMap.innerHTML = svg;
                }});
            }}

            codeEditor.addEventListener('input', updateMindMap);
            window.addEventListener('DOMContentLoaded', updateMindMap);
        </script>
    </body>
    </html>
    """.format(mermaid_code)

    return html_template

def save_html_file(html_content):
    file_name = "mermaid_editor.html"
    with open(file_name, "w") as file:
        file.write(html_content)
    
    return file_name

def open_editor():
    mermaid_code = "graph LR\n    A-->B\n    B-->C\n    C-->D"

    html_content = generate_mermaid_html(mermaid_code)
    file_name = save_html_file(html_content)

    webbrowser.open(file_name)

open_editor()

import webbrowser

# ...

def open_html_file(file_name):
    webbrowser.open_new_tab(file_name)

# ...

def open_editor():
    # ...

    open_html_file(file_name)

open_editor()
