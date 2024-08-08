
# TEchX

TEchX is a lightweight typesetting system designed for creating easy and smooth technical documentation. It supports a custom `.techx` file format, allowing you to easily define sections like titles, authors, API references, and changelogs. TEchX can render these files into both HTML and PDF formats which can be displayed for documentation.

## Features

- **Custom Typesetting Language**: Use `.techx` files with a simple syntax to define your documentation structure.
- **HTML Output**: Generate clean and responsive HTML documentation from your `.techx` files.
- **PDF Output**: Convert `.techx` files into polished PDF documents, suitable for printing and sharing.

## Installation

You can install TEchX via `pip`. 

### Using PIP : 

```bash
pip install techx
```
Also run `pip install requirements.txt` to install some dependencies.
### Manual Installation

Clone the repository and install it locally:

```bash
git clone https://github.com/yourusername/TEchX.git
cd TEchX
pip install .
```
## Usage

Once installed, you can use the `techx` command-line tool to generate HTML and PDF documentation.

### Basic Commands

#### Generate HTML

bash

Copy code

`TEchX input_file.techx --output-html output_file.html` 

This command converts `input_file.techx` into `output_file.html`.

#### Generate PDF

bash

Copy code

`TEchX input_file.techx --output-pdf output_file.pdf` 

This command converts `input_file.techx` into `output_file.pdf`.

### Example `.techx` File

Here’s an example of what a `.techx` file might look like:

techx

Copy code

`~title{Project Documentation}
~author{Jane Doe}
~date{2024-08-07}

~section{Introduction}
This project is designed to showcase the capabilities of TEchX, a simple and effective typesetting system.

~section{Installation}
To install the project, run the following command:` 

pip install TEchX

css

Copy code

 ``~section{Guide}
TEchX is easy to use. Just create a `.techx` file with the desired sections and render it into HTML or PDF.

~section{API Reference}
This section contains the API details.

~section{Changelog}
Version 0.1: Initial release.`` 

### Generating Documentation

To generate documentation from the example above:

1.  **Create the `.techx` file**: Save the example content to a file, say `example.techx`.
2.  **Generate HTML**: Run `TEchX example.techx --output-html example.html`.
3.  **Generate PDF**: Run `TEchX example.techx --output-pdf example.pdf`.

## Project Structure

The project is structured as follows:

bash

Copy code

`TEchX/
├── TEchX/
│   ├── __init__.py          # Initializes the package
│   ├── main.py              # CLI entry point
│   ├── tokenizer.py         # Tokenizes the .techx file
│   ├── parser.py            # Parses the tokens into an intermediate structure
│   ├── intermediate.py      # Defines the document and node structures
│   ├── html_renderer.py     # Renders the document to HTML
│   ├── pdf_renderer.py      # Renders the document to PDF
├── tests/
│   └── test_TEchX.py      # Unit tests for the project
├── README.md                # Project README
├── setup.py                 # Setup file for packaging
└── requirements.txt         # Python dependencies` 

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue on the [GitHub repository](https://github.com/yourusername/TEchX).

### Running Tests

To run the tests:

bash

Copy code

`python -m unittest discover tests` 

## License

This project is licensed under the MIT License. See the LICENSE file for details.

markdown

Copy code

 ``### Key Sections:

- **Features**: Highlights the main capabilities of TEchX.
- **Installation**: Provides instructions on how to install the tool.
- **Usage**: Explains how to use the command-line tool to generate HTML and PDF files.
- **Example `.techx` File**: Demonstrates the syntax and structure of a `.techx` file.
- **Project Structure**: Gives an overview of the files and directories in the project.
- **Contributing**: Encourages contributions and provides a link to the GitHub repository.
- **License**: Mentions the licensing information.

This `README.md` should provide users with all the necessary information to get star``
