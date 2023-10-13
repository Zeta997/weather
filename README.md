# Weather

## Proyecto de consumo de APIs

Para este proyecto he empleado Flask y requests. De todos modos el fichero `requirements.txt` 

El proposito de este proyecto es poner en práctica lo aprendido accerda del consumo de APIs con Python, Flask, requests y Jinja2, para este caso he decidido crear una aplicación con el que consumir APIs de terceros y mostrarlo en la web. 

Se trata de una web del tiempo y para poder recoger los ficheros json de cada provincia me dirigí a su apartado: `https://www.el-tiempo.net/api` <-- de aquí obtengo todos lo ficheros json ya los quiera por provincias o por municipios, en mi caso me enfoqué en los municipios.

Una vez que supe cómo obtener la información me dediqué a estructurar el proyecto y tener un orden para trabajar.

    --weather
    |--static
        |--css
        |--img
        |--proCss
    |--templates
        |--index
        |--provincias
    |getInputLocation.py
    |main.py
    |list-mun-2012.json

Realicé un diseño simple de la web con una etiqueta *form* en la que recogiese el input del usuario.
![Primera imagen](/imagenes/1.png)

Para tratar la información que el usuario pasa, decidí crear 2 archivos `.py` el archivo `main.py` y `getInputLocation.py`. 

Con el archivo `main.py` recojo la información del usuario a través de un POST en este caso recojo el nombre del municipio que el usuario haya escrito. Y con el archivo `getInputLocation.py` busco el municipio que el usuario ha solicitado y devolverlo en diversas funciones. Para obtener el municipio en cuestion a través del nombre lo que hice fue descargar un fichero json con todos los municipios de España y que cada municipio tuviese su `codine` de tal manera que con un condicional recogia el municipio con el dígito especifico y se lo entregaba a la url.

`main.py`
![Segunda imagen](/imagenes/2.png)
`getInputLocation.py`
![Tercera imagen](/imagenes/3.png)

Una vez que tenia todos los datos del municipio que el usuario había solicitado lo que quedaba era plasmar esos datos en un archivo HTML y darle estilos, en este caso el archivo se llama `pro.html`.
![Cuarta imagen](/imagenes/4.png)

Y cómo resultado tenemos lo siguiente:

![Quinta imagen](/imagenes/5.png)

## Este proyecto ha sido realizado con los siguientes requisitos:

-(Recomendable)Creación de un entorno virtual

-Clonar repositorio

    git clone https://github.com/Zeta997/weather.git

-Instalación de requirements
    
    pip install -r requirements.txt

-Versión de python 

    python 3.11 

-Ejecución de la aplicación

    flask --app main run --debug