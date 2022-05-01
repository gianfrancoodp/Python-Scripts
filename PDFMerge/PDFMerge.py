## Author: Gian Franco Ortega Di Pascuales
## E-mail: gianfrancoodp@gmail.com

from PyPDF2 import PdfFileMerger
import os
from tkinter import messagebox
from tkinter import *

## Variables
Path = os.path.abspath(os.getcwd())
filesInPath = os.listdir(Path)
OriginalDocuments = []
ModifiedDocuments = []
ResultFile = 'PDF Result.pdf' ## This name can be changed according to the user requirements - Este nombre puede ser cambiado según sean los requerimientos del usuario
count = 0

if os.path.exists(ResultFile): 
    print('The merge failed because the file "' +ResultFile+ '" already exist!! Try to delete it and execute the Script again.')
    messagebox.showinfo(message='The merge failed because the file "' +ResultFile+ '" already exist!! Try to delete it and execute the Script again.', title='Script Error')

else:
    ## PDF files are renamed for better sheet handling
    ## Los archivos PDF son renombrados para un mejor manejo de las hojas
    for file in filesInPath:
        if os.path.isfile(os.path.join(Path, file)) and file.endswith('.pdf'):
            OriginalDocuments.append(file)
            pdf_oldname = os.path.join(Path, file)
            pdf_newname = os.path.join(Path, str(count)+'.pdf')
            ModifiedDocuments.append(str(count)+'.pdf')
            count=count+1
            os.rename(pdf_oldname, pdf_newname)

    ## We use the PdfFileMerger function to merge each PDF file into a single file
    ## Usamos la función PdfFileMerger para unir cada archivo PDF en un solo archivo
    FusionPDF = PdfFileMerger()

    if ModifiedDocuments:
        for pdf in ModifiedDocuments:
            FusionPDF.append(pdf, 'rb')

        with open(ResultFile, 'wb') as output:
            FusionPDF.write(output)
    else:
        print('There are no PDF files in this path!! Try to add some PDF files.')
        messagebox.showinfo(message='There are no PDF files in this path!! Try to add some PDF files.', title='Script Error')

    ## We will close the FusionPDF process because we are going to rename each file back to its original name
    ## Cerraremos el proceso de FusionPDF porque vamos a renombrar nuevamente cada archivo a su nombre original
    FusionPDF.close()

    filesInPath2 = os.listdir(Path)
    count2 = 0

    ## This FOR cicle raname each file back to its original name
    ## Este ciclo FOR renombra cada archivo nuevamente a su nombre original 
    for file in OriginalDocuments:
        pdf_oldname2 = os.path.join(Path, ModifiedDocuments[count2])
        pdf_newname2 = os.path.join(Path, OriginalDocuments[count2])
        os.rename(pdf_oldname2, pdf_newname2)
        count2=count2+1