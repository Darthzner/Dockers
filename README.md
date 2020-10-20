# Server y Cliente XMPP

## Proyecto:

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
con el comando (en otra terminal):

```sh
$ sudo docker exec -it [ID_CONTAINER] /bin/bash
```

Una vez dentro ejecutar el siguiente comando: 

```sh
$ awk 'END{print $1}' /etc/hosts

```

Con esto sabremos la IP del servidor para ingresarla en nuestro navegador, Copiamos esa IP (y con el servidor ejecutandose en la otra terminal) 
pegamos la IP en la URL del navegador de la siguiente forma:

```sh
[IP_SEVER]:9090
```

Con esto se abrirá el servidor y se debe configurar (poner en dominio localhost y openfire.localhost), luego usar la base de datos interna y generar las credenciales de administrador. 
Posteriormente crear usuarios y definirlos con localhost igualmente en el correo, ej: correo@localhost

### Iniciar Cliente:

Ejecutar el siguiente comando antes de correr el docker image

```sh
$ xhost +local:root
```

Luego ejecutamos la imagen con el siguiente comando

```sh
$ sudo docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY [Image-ID]
```

Una vez abierto Spark nos vamos a Adavanced en la parte de abajo:

    - Desactivar detección automática de host y puerto

    - Host: ip del servidor, la que obtuvimos con "awk 'END{print $1}' /etc/hosts"

    - PORT: 5222

Posteriormente nos vamos a la pestaña de Security que está dentro de Advance de igual modo y le damos a Disable como modo de encriptación, esto para que no genere certificados.


Con esto debería poder entrar al servidor desde el cliente con los users y contraseñas seteados en el servidor.

##Enjoy!!

Pd: se puede ejecutar el comando:
```sh
$ sudo docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY [Image-ID] 
```
En distintos terminales para poder crear varios clientes y poder agregar amigos.

## Funciones para interceptar Trafico con Polymorph

En la capeta funciones, se encuentran las funciones que fueron usadas en el siguiente [Video](https://www.youtube.com/watch?v=n-DCk9sUTwM&feature=youtu.be) el cual muestra como 
manipular el tráfico asociado al sw de cliente y servidor a través de la herramienta polymorph, todo esto alojado en contenedores dockers.

[![Video Servidor y Cliente XMPP](http://img.youtube.com/vi/8VsujzifV5o/0.jpg)](https://www.youtube.com/watch?v=8VsujzifV5o)


[//]: #

[Openfire]: <https://github.com/igniterealtime/Openfire>
[Spark]: <https://www.igniterealtime.org/projects/spark/>
[Polymorph]: <https://github.com/shramos/polymorph>



