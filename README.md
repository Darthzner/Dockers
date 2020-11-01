# Dcker

Luego de ejecutar ambos Dockerfiles:
Primero configurar el Server de la siguiente manera:

<<<<<<< HEAD
Conociendo el id del container del server hacerlo correr y meterse dentro del container
=======
La idea principal de este proyecto es la conexión de cliente-servidor alojados en contenedores dockers, 
estos al poseer un protocolo ya escogido, en este caso XMPP, se realiza control de tráfico a las interacciones
entre estos 2 Softwares y se estiman posibles vulnerabilidades.

También se creó un [Video](https://www.youtube.com/watch?v=8VsujzifV5o) en donde se muestra el enlace entre ambos softwares
y la muestra de 10 traficos diferentes XMPP.

Cabe destacar que los Softwares usados son los siguientes:

* [Openfire] - Servidor XMPP
* [Spark] - Cliente XMPP
* [Polymorph] - Manipulacion de Tráfico

## Instalacion e Inicialización:

Luego de hacer un build a cada Dockerfile, debemos ejecutar el server y el cliente, en ese respectivo
orden de la siguiente forma:

### Iniciar el Server:

Conociendo el ID del container del server, lo hacemos correr y nos metemos dentro del container
>>>>>>> parent of b5db7c1... Update README.md
con el comando (en otra terminal):

sudo docker exec -it [ID_CONTAINER] /bin/bash

ejecutar el siguiente comando 

awk 'END{print $1}' /etc/hosts

Con esto sabremos la ip del sv para poder ponerla en nuestro browser

copiamos esa ip (y con el sv ejecutandose en la otra consola) pegamos la ip en la url
del browser de la siguiente forma:

ip:9090

Con esto se abrira el servidor y se debe configurar (poner en dominio localhost y openfire.localhost), luego usar la base de datos interna y generar las credenciales de admin, posteriormente ir a crear usuarios y definirlos con localhost igualmente en el correo ej: correo@localhost

Entrar con CLIENTE:

ejecutar el siguiente comando antes de correr el docker image

xhost +local:root

luego ejecutamos la imagen con el siguiente comando

sudo docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY [Image-ID]

una vez abierto Spark nos vamos a adavanced en la parte de abajo:

desactivar deteccion automatica de host y puerto

Host: ip del servidor, la que obtuvimos con "awk 'END{print $1}' /etc/hosts"

PORT: 5222

posteriormente nos vamos a la pestaña de security que esta dentro de advance de igual modo y le damos a disable como modo de encriptacion, esto para que no genere certificados.


Con esto deberia poder entrar al servidor desde el cliente con los users y contraseñas seteados en el sv y el domain: localhost.

Enjoy.

Pd: se puede ejeecutar el comando sudo docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY [Image-ID] en distintos terminales para poder crear varios clientes y poder agregar amigos.

<<<<<<< HEAD
=======
[![Video Servidor y Cliente XMPP](http://img.youtube.com/vi/8VsujzifV5o/0.jpg)](https://www.youtube.com/watch?v=8VsujzifV5o)
>>>>>>> parent of b5db7c1... Update README.md






