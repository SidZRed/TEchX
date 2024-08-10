# TEchX

TEchX is a lightweight typesetting system designed for creating easy and smooth technical documentation. It supports a custom `.techx` file format, allowing you to easily define sections like titles, authors, API references, and changelogs. TEchX can render these files into both HTML and PDF formats which can be displayed for documentation.

## Features

  

-  **Custom Typesetting Language**: Use `.techx` files with a simple syntax to define your documentation structure.

-  **HTML Output**: Generate clean and responsive HTML documentation from your `.techx` files.

-  **PDF Output**: Convert `.techx` files into polished PDF documents, suitable for printing and sharing.

  

## Installation

  

You can install TEchX via `pip`.

  

### Using PIP :
Visit the PyPI official release : [TEchX](https://pypi.org/project/techx/0.1/)  

```bash
pip install techx==0.1
```

Also run `pip install requirements.txt` after cloning the repository to install some dependencies.

### Manual Installation
Clone the repository and install it locally:
```bash
git  clone  https://github.com/yourusername/TEchX.git
cd  TEchX
pip  install  .
```

## Usage

  

Once installed, you can use the `techx` command-line tool to generate HTML and PDF documentation.

  

### Utilities

  

#### Generate HTML TechDoc
```bash
techx tech_doc.techx --output-html tech_doc.html
```
  

This command converts `tech_doc.techx` into `tech_doc.html`.

  


#### Generate PDF TechDoc
```bash
techx tech_doc.techx --output-pdf tech_doc.pdf
```
  

This command converts `tech_doc.techx` into `tech_doc.pdf`.
  
 ## TEchX syntax:
 TEchX provides a very easy and simple syntax to produce technical documentation for small scale projects and also individual files. 

Techdoc uses a simple and intuitive syntax to define sections, code snippets, API references, and changelogs within `.techx` files. All commands begin with a `~` symbol, and the escape character is also `~`. Below is a breakdown of the available commands and their usage.

### 1. **Document Metadata**

- **`~title{}`**: Specifies the title of the document.
	
  ```techx
  ~title{Project Documentation}
  ``` 

-   **`~author{}`**: Specifies the author’s name.
	```techx
	~author{John Doe}
	```
-   **`~date{}`**: Specifies the date of the document. 
	This is an optional parameter. If left empty, it automatically fetches the date from the system.
	```techx
	~date{15 Oct 2005}
	```
	
    

### 2. **Sections**

-   **`~section{}`**: Defines a new section in the document. The section title is provided within the curly braces.
    
    ```techx
    ~section{Introduction}
    This is the introduction section.
    ```

### 3. **Code Snippets**

-   **`~code{language : code}`**: Embeds a code snippet in the document. The `language` specifies the programming language for syntax highlighting, and the `code` is the actual code snippet.
    
    ```techx
    ~code{bash : npm install myproject}
    ```
    
    Multiline code snippets are also supported:
    
    ```techx
    ~code{javascript : 
    const myProject = require('myproject');
    myProject.doSomething();
    }
    ```
    

### 4. **API References**

-   **`~api{}`**: Defines an API reference entry. The command is followed by the API method or function name, and a description is provided in the text.
    
    ```techx
    ~api{API_Reference}
    Description: Executes the main function of the project.
    Parameters: none
    Returns: void
    ```
    

### 5. **Changelog**

-   **`~changelog{}`**: Defines a changelog section. The changes are listed within the curly braces, with each change prefixed by a hyphen.
    
    ```techx
    ~changelog{
    - v1.0.0: Initial release
    - v1.1.0: Added new feature
    }
    ```
    

### 6. **Text Content**

-   **Plain Text**: Any text outside of a command is treated as plain text and will be rendered directly.
    
    ```techx
    This is a regular paragraph of text.
    ```

### 7. **Escape Characters**

-   **Escape `~`**: If you need to use the `~` character literally in your text, escape it by doubling the `~`.
	`Escaped tilde: '~~'`

***
## Contributing

Currently, the project is in a nascent stage with more updates and development yet to come. Any new feature ideas and/or bugs can be reported in an issue or by opening a pull request in this repository!
Design and implementation of some of the features is an ongoing process, so inputs are welcome. (PDF rendering is still at a very basic phase).
All contributions are most welcome!

## License
This project is an open source tool licensed under the [MIT License](https://github.com/SidZRed/TEchX/blob/main/LICENSE). 

***
