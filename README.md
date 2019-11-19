# Challenge 
Aquí se encuentran mis "respuestas" al reto. El archivo de python esta escrito en la forma más económica que pude, probablemente se pueda mejorar. 
Cuando este se ejecuta el usario debe introducir el path a la imagen sobre la cual se quiere aplicar la inversión, así como el nombre del archivo 
incluyendo la extensión (jpg, png, etcétera).

N.B. en caso de utilizar python3 el archivo debe modificarse
raw_input() -----> input()
Y en Dockerfile las lineas 
FROM python:2.7 

CMD ["python", "script.py" ]

también deben modificarse.

En la creación de la imagen de Docker fue donde encontré dificultades. En principio crear la imagen usando 

docker run build -t nombre-imagen .

es sencillo, pero para acceder a la imagen que uno quiere modificar desde el contenedor de Docker me parece que hay que crear un volumen y es donde tuve 
dificultades.
