# Static Site Generator

A simple static site generator written in Python. It converts Markdown content into HTML pages using a shared template, copies static assets, and outputs a complete site structure in the `docs/` directory.

## Features
- Converts Markdown files to HTML
- Supports common block and inline Markdown elements
- Generates pages recursively from the `content/` directory
- Preserves directory structure in the output
- Copies static files from `static/` to `docs/`

## Project Structure
- `content/`: Markdown source files
- `static/`: CSS, images, and other static assets
- `template.html`: Shared page template
- `src/`: Generator source code
- `docs/`: Generated site output

## Run Locally
1. Generate the site:

```bash
python3 src/main.py
```

2. Serve the generated site:

```bash
cd docs && python3 -m http.server 8888
```

## Tests

```bash
bash test.sh
```

## Acknowledgment
I built this project by following the Boot.dev course:
https://www.boot.dev/courses/build-static-site-generator-python
