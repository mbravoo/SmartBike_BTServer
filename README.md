# SmartBike_BTServer

Codigo Python para iniciar un servidor Bluetooth que permita escuchar peticiones desde la aplicación Android "SmartBike".
Deacuerdo al código enviado desde la aplicación Android, el servidor lo interpreta y devuelve el resultado correspondiente (La lectura de un sensor, por ejemplo).
En este momento solo envía datos random simulando la lectura de un sensor de corriente que permitiria calcular la potencia instantanea de la bicicleta eléctrica.
Para realizar lecturas desde los sensores, es posible utilizar los puertos GPIO disponibles en la RPi.

## Instalación

Para que se ejecute correctamente el script, es necesario instalar unas dependencias.
### sudo apt-get install bluez
### sudo apt-get install python-bluez
Luego hay que dejar visible la raspberry-PI
### hciconfig hci0 piscan
Finalmente ejecutar el script
### sudo python rf-comm-server.py
Existe la opción de instalar una aplicación que gestione el arranque automatico del script, así como el reinicio y parada de este.
### sudo apt-get install supervisor
Una vez instalado, es necesario crear el archivo conf que inicia la aplicación (rfcomm-bt.conf) en la ruta "/etc/supervisor/conf.d/"
una vez creado, se debe leer la nueva aplicación para ser gestionada
### supervisorctl reread
### supervisorctl reload
Y listo. Ahora cada vez que se encienda la Rpi, se ejecutará el script con el servidor Bluetooth

## Creditos

##Matias Bravo
##Gian Bravo
