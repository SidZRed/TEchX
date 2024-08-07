import sys
from tokenizer import Tokenizer
from parser import Parser
from intermediate import Document
from html_renderer import HTML_Renderer
from pdf_renderer import PDF_Renderer
import argparse 

def main():
    parser = argparse.ArgumentParser(description="Process a techx file to render it as a HTML and PDF file.")
    parser.add_argument('input_file', type=str, help="file path of a .techx file")
    args = parser.parse_args()

    input_file = args.input_file    
    with open(input_file, 'r') as f:
        text = f.read()

    tokenizer = Tokenizer(text)
    tokens = tokenizer.get_tokens()

    parser = Parser(tokens)
    parsed_doc = parser.parse()

    html_renderer = HTML_Renderer(parsed_doc)
    html_output = html_renderer.render()
    with open('tech_doc.html', 'w') as file:
        file.write(html_output)
    
    pdf_renderer = PDF_Renderer(parsed_doc, "tech_doc.pdf")
    pdf_renderer.render()


if __name__ == "__main__":
    main()