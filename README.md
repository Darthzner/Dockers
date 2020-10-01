# Docker

Luego de ejecutar ambos Dockerfiles:

### Iniciar el Server:

Conociendo el id del container del server hacerlo correr y meterse dentro del container
con el comando (en otra terminal):

```sh
$ sudo docker exec -it [ID_CONTAINER] /bin/bash
```

Una vez dentro ejecutar el siguiente comando 

```sh
$ awk 'END{print $1}' /etc/hosts

```

Con esto sabremos la ip del sv para poder ponerla en nuestro browser, Copiamos esa ip (y con el sv ejecutandose en la otra consola) 
pegamos la ip en la url del browser de la siguiente forma:

```sh
ip:9090
```

Con esto se abrira el servidor y se debe configurar, (poner en dominio localhost y openfire.localhost), luego usar la base de datos interna y generar las credenciales de admin. 
Posteriormente ir a crear usuarios y definirlos con localhost igualmente en el correo ej: correo@localhost

### Iniciar CLIENTE:

Ejecutar el siguiente comando antes de correr el docker image

```sh
$ xhost +local:root
```

Luego ejecutamos la imagen con el siguiente comando

```sh
$ sudo docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY [Image-ID]
```

Una vez abierto Spark nos vamos a adavanced en la parte de abajo:

    - Desactivar deteccion automatica de host y puerto

    - Host: ip del servidor, la que obtuvimos con "awk 'END{print $1}' /etc/hosts"

    - PORT: 5222

Posteriormente nos vamos a la pestaña de security que esta dentro de advance de igual modo y le damos a disable como modo de encriptacion, esto para que no genere certificados.


Con esto deberia poder entrar al servidor desde el cliente con los users y contraseñas seteados en el sv.

Enjoy.

Pd: se puede ejeecutar el comando sudo docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY [Image-ID] en distintos terminales para poder crear varios clientes y poder agregar amigos.







