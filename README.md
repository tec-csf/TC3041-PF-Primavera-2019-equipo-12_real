# TC3041 Proyecto  Final Primavera 2019

AMAYA
---

##### Integrantes:
1. Luis Fernando Carrasco de la Parra
2. Daniel Pelagio Vázquez


---
## 1. Aspectos generales

### 1.1 Requerimientos técnicos

A continuación se mencionan los requerimientos técnicos mínimos del proyecto, favor de tenerlos presente para que cumpla con todos.

* El equipo tiene la libertad de elegir las tecnologías de desarrollo a utilizar en el proyecto, sin embargo, debe tener presente que la solución final se deberá ejecutar en una plataforma en la nube. Puede ser  [Google Cloud Platform](https://cloud.google.com/?hl=es), [Azure](https://azure.microsoft.com/en-us/) o AWS [AWS](https://aws.amazon.com/es/free/).
* El proyecto debe utilizar al menos dos modelos de bases de datos diferentes, de los estudiados en el curso.
* La solución debe utilizar una arquitectura de microservicios. Si no tiene conocimiento sobre este tema, le recomiendo la lectura [*Microservices*](https://martinfowler.com/articles/microservices.html) de [Martin Fowler](https://martinfowler.com).
* La arquitectura debe ser modular, escalable, con redundancia y alta disponibilidad.
* La arquitectura deberá estar separada claramente por capas (*frontend*, *backend*, *API RESTful*, datos y almacenamiento).
* Los diferentes componentes del proyecto (*frontend*, *backend*, *API RESTful*, bases de datos, entre otros) deberán ejecutarse sobre contenedores [Docker](https://www.docker.com/) y utilizar [Kubernetes](https://kubernetes.io/) como orquestador.
* Todo el código, *datasets* y la documentación del proyecto debe alojarse en un repositorio de GitHub siguiendo al estructura que aparece a continuación.

### 1.2 Estructura del repositorio
El proyecto debe seguir la siguiente estructura de carpetas:
```
- / 			        # Raíz de todo el proyecto
    - README.md			# Archivo con los datos del proyecto (este archivo)
    - frontend			# Carpeta con la solución del frontend (Web app)
    - backend			# Carpeta con la solución del backend (CMS)
    - api			# Carpeta con la solución de la API
    - datasets		        # Carpeta con los datasets y recursos utilizados (csv, json, audio, videos, entre otros)
    - dbs			# Carpeta con los modelos, catálogos y scripts necesarios para generar las bases de datos
    - models			# Carpeta donde se almacenarán los modelos de Machine Learning ya entrenados 
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

El proyecto propuesto es una página web, cuya finalidad es compartir imagenes de tipo artístico (fotografias, dibujos, pinturas, esculturas, etc). La finalidad es tener un solo dashboard principal lleno de imagenes diferentes, sin nada más de información en pantalla. Cuando el usuario hace click en la imagen, se mostrará la información de dicha imagen (el nombre, el autor, dónde fue realizada, una pequeña descripción y tags para identificar el tipo de imagen.  

## 3. Solución

La información correspondiente a las imagen será guardada utilizando mongoDB, y la información de las sesiones de usuario mediante Redis. 

### 3.1 Modelos de *bases de datos* utilizados

*[Incluya aquí una explicación del análisis realizado y la justificación de los modelos de *bases de datos* seleccionados. Incluya todo lo que considere necesario para que una persona sin conocimientos técnicos pueda entender de que trata su solución.]*

### 3.2 Arquitectura de la solución

*[Incluya aquí un diagrama donde se aprecie la arquitectura de la solución propuesta, así como la interacción entre los diferentes componentes de la misma.]*

### 3.3 Frontend

*[Incluya aquí una explicación de la solución utilizada para el frontend del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.3.1 Lenguaje de programación
#### 3.3.2 Framework
#### 3.3.3 Librerías de funciones o dependencias

### 3.4 Backend

*[Incluya aquí una explicación de la solución utilizada para el backend del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.4.1 Lenguaje de programación
#### 3.4.2 Framework
#### 3.4.3 Librerías de funciones o dependencias

### 3.5 API

*[Incluya aquí una explicación de la solución utilizada para implementar la API del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.5.1 Lenguaje de programación
#### 3.5.2 Framework
#### 3.5.3 Librerías de funciones o dependencias

*[Incluya aquí una explicación de cada uno de los endpoints que forman parte de la API. Cada endpoint debe estar correctamente documentado.]*

*[Por cada endpoint debe incluir lo siguiente:]*

* **Descripción**:
* **URL**:
* **Verbos HTTP**:
* **Headers**:
* **Formato JSON del cuerpo de la solicitud**: 
* **Formato JSON de la respuesta**:


## 3.6 Pasos a seguir para utilizar el proyecto

* Clonar el repositorio con git clone o descargarlo.
* Entrar a la carpeta app con el comando: 'cd app'
 - Para correrlo localmente:  
    - 2.1. Crear la imagen de docker con el comando: 'sudo docker build -t test-app:v1 .'  
    - 2.2. Ejecutar la imagen y crear un contenedor con el comando: 'sudo docker run --name amaya -p 5000:5000 test-app:v1'  
    - 2.3. Entrar al link: 'localhost:5000'  
    
 - Para correrlo en la nube con google cloud platform:  
    - 2.1 Cree un proyecto en la Consola de Google Cloud Platform. Póngale el nombre y ID que usted prefiera.  
    - 2.2 Dentro de la misma consola, en el menú de la izquierda seleccione la opción Kubernetes Engine / Clústeres de Kubernetes y cree un nuevo clúster dentro del proyecto creado en el paso anterior.
    - 2.3 Una vez creado el clúster, seleccione la opción "Ejecutar" y en la ventana que aparece, seleccione el primer comando relacionado con kubectl. El comando a copiar tiene una estructura similar a la siguiente: 
    
            gcloud container clusters get-credentials demo-webinar --zone us-central1-a --project <PROJECT-ID>
        
    - 2.4 Ejecute el comando en una terminal de su computadora.
    - 2.5 Compile la imagen del contenedor de la aplicación, sustituyendo <PROJECT ID> por el que le correponde. Este valor es el que aparece en el parámetro --project del comando ejecutado en el paso anterior:
    
            docker build -t gcr.io/<PROJECT ID>/flask-api .
        
    - 2.6 Suba la imagen del contendor al registro de su proyecto en Google Cloud Platform:
    
            gcloud docker -- push gcr.io/<PROJECT ID>/flask-api
        
    - 2.7 Despliegue la aplicación en Google Cloud Platform:
    
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

