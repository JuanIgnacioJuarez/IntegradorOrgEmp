# IntegradorOrgEmp
## Grupo: CodeCrafters</>
### Integrantes:
- Sofia Raia (Product Owner)
- Martina Molina (Scrum Master)
- Ailen Carretero (Developer) 
- Ignacio Juarez (Developer) 
- Mariano Videla (Developer) 

Para el correcto funcionamiento de la App es necesario crear un archivo .env con una variable de entorno API_KEY.

Para correr la app necesitamos correr los comandos:
docker run -it my_python_app (por ahora este comando no anda hasta arreglar la variable de entorno con compost)

docker build -t my_python_app .   (esto se hace la primera ves que se corre)
docker run -it -e API_KEY='de3a10965f84f387c4dc5471da563d87' my_python_app  (Para que corra la app)
