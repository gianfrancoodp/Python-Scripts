PDFMerge

PDFMerge es un pequeño Script en Python que permite unir dos o mas archivos PDF en uno solo, facilitando en ocasiones la lectura de la información contenida en ellos. Dicho Script fue desarrollado con el objetivo de disponer de una herramienta que permita unir varios archivos PDF sin la necesidad de utilizar aplicaciones webs, manteniendo la información de cada archivo de forma segura dentro del ordenador. 

Instalación

En primer lugar, se debe utilizar el Sistema de Gestión de Paquetes PIP (https://pip.pypa.io/en/stable/) para instalar el paquete PyPDF2. Para ello, es necesario abrir la consola (cmd) del ordenador y escribir el siguiente comando:

pip install PyPDF2


Uso

1. Copiar el Script "PDFMerge.py" dentro de la carpeta donde se encuentran todos los archivos PDF que se desean unificar en un solo archivo.
2. Abrir el Script "PDFMerge.py" con el editor de código de su preferencia.
3. Ejecutar el Script con el editor de código.
4. Se visualizará dentro de la carpeta fuente (en donde se encuentran todos los archivos PDF y el Script juntos) un nuevo archivo PDF con el nombre "PDF Result.pdf". Este es el Output del Script, el cual contempla todos los archivos PDF que se encuentran en el Path dentro de un solo PDF.


Consideraciones

1. Si no existe ningún archivo PDF dentro de la carpeta donde se encuentra el Script, se visualizará una ventana emergente al momento de ejecutarlo, la cual indica exactamente la ausencia de archivos PDF dentro del Path.
2. Si se ejecuta el Script dentro de la misma ubicación y en más de una ocasión (sin sacar previamente el archivo resultante), se visualizará una ventana emergente al momento de ejecutarlo, la cual indica que ya existe un archivo resultante llamado "PDF Result.pdf". En este caso, se recomienda extraer dicho archivo resultante hacia otra ruta, para evitar que se produzca dicho conflicto y así poder ejecutar nuevamente el Script. Este conflicto se produce al momento de intentar sobrescribir el archivo resultante que ya existe dentro de la misma ruta, generando que inclusive se fusione el archivo resultante anterior con el nuevo.
3. Si se desea cambiar el nombre del archivo resultante, puede hacerlo a través de la variable "ResultFile", ubicada en la línea 14 del código. 


Contribución

Cualquier tipo de cambio, mejora u optimización del código de este Script es totalmente aceptado y apreciado.
