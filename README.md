# TC3041 Proyecto  Final Primavera 2019

AMAYA  
http://35.225.166.237/  
---

##### Integrantes:
1. Luis Fernando Carrasco de la Parra
2. Daniel Pelagio Vázquez


---
## 1. Aspectos generales

### 1.1 Requerimientos técnicos

A continuación, se mencionan los requerimientos técnicos mínimos del proyecto, favor de tenerlos presente para que cumpla con todos.

* El equipo tiene la libertad de elegir las tecnologías de desarrollo a utilizar en el proyecto, sin embargo, debe tener presente que la solución final se deberá ejecutar en una plataforma en la nube. Puede ser  [Google Cloud Platform](https://cloud.google.com/?hl=es), [Azure](https://azure.microsoft.com/en-us/) o AWS [AWS](https://aws.amazon.com/es/free/).
* El proyecto debe utilizar al menos dos modelos de bases de datos diferentes, de los estudiados en el curso.
* La solución debe utilizar una arquitectura de microservicios. Si no tiene conocimiento sobre este tema, le recomiendo la lectura [*Microservices*](https://martinfowler.com/articles/microservices.html) de [Martin Fowler](https://martinfowler.com).
* La arquitectura debe ser modular, escalable, con redundancia y alta disponibilidad.
* La arquitectura deberá estar separada claramente por capas (*frontend*, *backend*, *API RESTful*, datos y almacenamiento).
* Los diferentes componentes del proyecto (*frontend*, *backend*, *API RESTful*, bases de datos, entre otros) deberán ejecutarse sobre contenedores [Docker](https://www.docker.com/) y utilizar [Kubernetes](https://kubernetes.io/) como orquestador.
* Todo el código, *datasets* y la documentación del proyecto debe alojarse en un repositorio de GitHub siguiendo la estructura que aparece a continuación.

### 1.2 Estructura del repositorio
```
- / 			        # Raíz de todo el proyecto
    - README.md			# Archivo con los datos del proyecto (este archivo)
    - app                       # Carpeta con todo lo necesario para correr la aplicacion       
        - frontend			# Carpeta con la solución del frontend (Web app)
        - backend			# Carpeta con la solución del backend (CMS)
        - api			        # Carpeta con la solución de la API
    - datasets		        # Carpeta con los datasets y recursos utilizados (csv, json, audio, videos, entre otros)
    - dbs			# Carpeta con los modelos, catálogos y scripts necesarios para generar las bases de datos
    - docs			# Carpeta con la documentación del proyecto
        - stage_f               # Documentos de la entrega final
        - manuals               # Manuales y guías
```

### 1.3 Documentación  del proyecto

Como parte de la entrega final del proyecto, se debe incluir la siguiente información:

* Justificación de los modelo de *bases de datos* que seleccionaron.
* Descripción del o los *datasets* y las fuentes de información utilizadas.
* Guía de configuración, instalación y despliegue de la solución en la plataforma en la nube  seleccionada.
* Documentación de la API. Puede ver un ejemplo en [Swagger](https://swagger.io/). 
* El código debe estar documentado siguiendo los estándares definidos para el lenguaje de programación seleccionado.

## 2. Descripción del proyecto

El proyecto propuesto es una página web, cuya finalidad es compartir imágenes de tipo artístico (fotografías, dibujos, pinturas, esculturas, etc.). La finalidad es tener un solo dashboard principal lleno de imágenes diferentes, sin nada más de información en pantalla. Cuando el usuario hace click en la imagen, se mostrará la información de dicha imagen (el nombre, el autor, dónde fue realizada, una pequeña descripción y tags para identificar el tipo de imagen.  

## 3. Solución

La información correspondiente a la imagen será guardada utilizando mongoDB, y la información de las sesiones de usuario mediante Redis. 

### 3.1 Modelos de *bases de datos* utilizados

Los modelos de bases de datos seleccionados fueron base de datos llave-valor y base de datos basado en documentos. Utilizamos redis debido a que cuenta con un gran manejo de la sesión de usuarios, redis es la base de datos llave-valor, ya que es capaz de solamente almacenar una llave, la cual cuenta con un solo valor. Esto nos provee una manera sencilla, simple y eficaz de manejar a los usuarios, guardamos el correo de cada usuario y lo relacionamos con el valor de su password. En cuando a mongodb, la base de datos basada en documentos, la utilizamos para poder guardar de manera más simple las imágenes, ya que los documentos permiten cierta flexibilidad al ser almacenados y facilitan el manejo de estos mismos, permitiéndonos guardar fotos sin ciertos valores o filtrar las fotos guardadas en base a ciertas especificaciones.  

Si deseas saber más acerca de mongodb o de redis, visita cualquiera de las siguientes ligas:  
https://redis.io/documentation    
https://docs.mongodb.com/    

### 3.2 Arquitectura de la solución

![arquitectura_solucion](https://user-images.githubusercontent.com/21222798/57347825-45c26680-7119-11e9-8825-9d0115f7c274.JPG)

### 3.3 Frontend

La solución que utilizamos para el frontend fue utilizar html, css y javascript. Esto para poder crear templates sencillos y que se vieran muy bien. Lo que utilizamos para desplegar los templates que utilizamos fue el framework flask y el lenguaje de programacion python. Esto es debido a que ambos son muy sencillos de implementar.

#### 3.3.1 Lenguaje de programación
Python fue el lenguaje de programación que utilizamos ya que cuenta con la facilidad de conectarse a los modelos de bases de datos e importar librerías que permiten su manejo.
Javascript junto con CSS fueron los otros 2 lenguajes de programacion que utilizamos, Javascript fue para permitir el diseño de los templates, así como para poder agregarles funciones a estos mismos, mientras que CSS solamente lo utilizamos para detallar y dar color a nuestros html's.

#### 3.3.2 Framework
El framework con el que trabajamos fue Flask, ya que es sencillo para manejar, junto con python, además que permite el uso de templates html.

#### 3.3.3 Librerías de funciones o dependencias
Las principales librerías que utilizamos fueron Jijna2, que nos permitía agregar funciones a nuestro html's y que se vieran mejor, y librerias de python para realizar una serie de operaciones dentro de nuestro código.

### 3.4 Backend
La solución que escogimos fue implementar una librerías en python que nos permitieran acceder a las bases de datos y utilizar funciones sobre estas mismas, así como insertar, consultar, borrar y demás, sobre nuestros dos modelos de bases de datos.

#### 3.4.1 Lenguaje de programación
Python, utilizamos python para facilitar el uso de librerías y la creación de las mismas.

#### 3.4.2 Librerías de funciones o dependencias
Las librerías que se usaron fueron redis-py y pymongo para poder utilizar las bases de datos.

### 3.5 API
La solución que implementamos como api fue crear un programa utilizando el lenguaje python, que fuera capaz de conectar nuestro frontend con nuestro backend. Importaba las librerías que creamos como nuestro backend y permite que el usuario interactuar con el interfaz en html.

#### 3.5.1 Lenguaje de programación
Python, para facilitar la conexión.

#### 3.5.2 Framework
Flask

Para el servicio en cloud, se reemplaza localhost:5000 por 35.225.166.237

Descripción: Login para usuarios.  

URL: localhost:5000/  
Verbos HTTP: Get y Post  
Headers: Ninguno  
Formato JSON del cuerpo de la solicitud: {"username":"user_input", "password":"user_input"}   
Formato JSON de la respuesta: {}   

Descripción: Dashboard principal para usuarios.   
URL: localhost:5000/home    
Verbos HTTP: Get y Post  
Headers: Ninguno  
Formato JSON del cuerpo de la solicitud: {"titulo":"user_input", "lugar":"user_input", "descripcion":"user_input", "imagen":"user_input"}  
Formato JSON de la respuesta: {}  

Descripción: SignUp para usuarios.  

URL: localhost:5000/signUp  
Verbos HTTP: Get y Post  
Headers: Ninguno  
Formato JSON del cuerpo de la solicitud: {"nombre":"user_input", "apellido_materno":"user_input", "apellido_paterno":"user_input", "email":"user_input", "password":"user_input"}  
Formato JSON de la respuesta: {}  


## 3.6 Pasos a seguir para utilizar el proyecto

* Clonar el repositorio con git clone o descargarlo.
* Entrar a la carpeta app con el comando: 

        cd app
 - Para correrlo localmente:  
    - 2.1. Crear la imagen de docker con el comando: 
    
            sudo docker build -t test-app:v1 . 
    - 2.2. Ejecutar la imagen y crear un contenedor con el comando: 
    
            sudo docker run --name amaya -p 5000:5000 test-app:v1  
    - 2.3. Entrar al link: localhost:5000 
    
 - Para correrlo en la nube con google cloud platform:  
    - 2.1 Cree un proyecto en la Consola de Google Cloud Platform. Póngale el nombre y ID que usted prefiera.  
    - 2.2 Dentro de la misma consola, en el menú de la izquierda seleccione la opción Kubernetes Engine / Clústeres de Kubernetes y cree un nuevo clúster dentro del proyecto creado en el paso anterior.
    - 2.3 Una vez creado el clúster, seleccione la opción "Ejecutar" y en la ventana que aparece, seleccione el primer comando relacionado con kubectl. El comando a copiar tiene una estructura similar a la siguiente: 
    
            gcloud container clusters get-credentials demo-webinar --zone us-central1-a --project <PROJECT-ID>
        
    - 2.4 Ejecute el comando en una terminal de su computadora.
    - 2.5 Compile la imagen del contenedor de la aplicación, sustituyendo <PROJECT ID> por el que le corresponde. Este valor es el que aparece en el parámetro --project del comando ejecutado en el paso anterior:
    
            docker build -t gcr.io/<PROJECT ID>/flask-api .
        
    - 2.6 Suba la imagen del contendor al registro de su proyecto en Google Cloud Platform:
    
            gcloud docker -- push gcr.io/<PROJECT ID>/flask-api
        
    - 2.7 Salga de la carpeta app (cd ..) y despliegue la aplicación:
    
            kubectl create -f proxy-api.yaml
        
    - 2.8 Obtenga la URL del servicio. Ejecute varias veces este comando hasta que el valor EXTERNAL-IP se encuentre asignado:
    
            kubectl get service
        
    - 2.9 Acceder a la IP obtenida 
    
Para eliminar la aplicación y los servicios creados ejecute:

    kubectl delete -f proxy-api.yaml
    
Elimine el clúster desde la Consola de Google Cloud Platform.

## 4. Referencias

http://flask.pocoo.org/docs/dev/quickstart/  
https://api.mongodb.com/python/current/  
https://docs.redislabs.com/latest/rc/quick-setup-redis-cloud/  
https://docs.docker.com/engine/reference/builder/  
http://jinja.pocoo.org/docs/2.10/  
https://www.w3schools.com/html/  
