import argparse
from tokenizer import Tokenizer
from parser import Parser
from html_renderer import HTML_Renderer
from pdf_renderer import PDF_Renderer

def main():
    parser = argparse.ArgumentParser(description="Convert .techx file to HTML or PDF.")
    parser.add_argument("input", help="Input .techx file")
    parser.add_argument("--output-html", help="Output HTML file")
    parser.add_argument("--output-pdf", help="Output PDF file")
    args = parser.parse_args()

    with open(args.input, 'r') as file:
        if(args.input[-6:] == ".techx"):
            text = file.read()
        else:
            print("Invalid file format. Please provide a .techx file.")
            return

    tokenizer = Tokenizer(text)
    tokens = tokenizer.get_tokens()

    parser = Parser(tokens)
    document = parser.parse()

    if args.output_html:
        html_renderer = HTML_Renderer(document)
        html_content = html_renderer.render()
        with open(args.output_html, 'w') as html_file:
            html_file.write(html_content)

    if args.output_pdf:
        pdf_renderer = PDF_Renderer(document, args.output_pdf)
        pdf_renderer.render()

if __name__ == "__main__":
    main()
