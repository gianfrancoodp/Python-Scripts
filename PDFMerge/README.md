
# PDFMerge

PDFMerge is a small Python script that allows you to merge two or more PDF files into one, sometimes facilitating the reading of the information contained in them. Said Script was developed with the aim of having a tool that allows you to join several PDF files without the need to use web applications, keeping the information of each file safely inside the computer.


## Tech Stack

* Python
* PyPDF2


## How to run the Script (Executable)

* Copy the executable "PDFMerge.exe" into the folder where all the PDF files that you want to merge into a single file are located.
* Double click on the executable "PDFMerge.exe" (or you can also right click->Open)
* A new PDF file with the name "PDF Result.pdf" will be displayed inside the source folder (where all the PDF files and the executable are located together). This is the Output of the executable, which includes all the PDF files found in the Path within a single PDF.
## Installation

First of all, the PIP Package Management System (https://pip.pypa.io/en/stable/) must be used to install the PyPDF2 package. To do this, it is necessary to open the console (cmd) of the computer and write the following command:

```bash
pip install PyPDF2
```
## How to run the Script (Python File)

* Copy the "PDFMerge.py" Script into the folder where all the PDF files that you want to merge into a single file are located.
* Open the "PDFMerge.py" Script with the code editor of your choice.
* Run the Script with the code editor.
* A new PDF file with the name "PDF Result.pdf" will be displayed inside the source folder (where all the PDF files and the Script are located together). This is the Output of the Script, which includes all the PDF files found in the Path within a single PDF.
## Considerations

* If there is no PDF file inside the folder where the Script/Executable is located, a pop-up window will be displayed when executing it, which indicates exactly the absence of PDF files inside the Path.
* If the Script/Executable is executed within the same location and on more than one occasion (without previously removing the resulting file), a pop-up window will be displayed when executing it, indicating that there is already a resulting file called " PDF Result.pdf". In this case, it is recommended to extract the resulting file to another path, to prevent this conflict from occurring and thus be able to execute the Script/Executable again. This conflict occurs when trying to overwrite the resulting file that already exists within the same path, causing the previous resulting file to be merged with the new one.
* If you want to change the name of the resulting file (only applies if you run the Script in the code editor), you can do so through the "ResultFile" variable, located on line 14 of the code.

## Contribution

Contributions are always welcome! Any type of change, improvement or optimization of the code of this Script is fully accepted and appreciated.


## Author

Gian Franco Ortega Di Pascuales

https://www.linkedin.com/in/gianfrancortega/