Control de temperatura para la Raspberry Pi
===========================================

La intencion es hacer un cron job que corra un archivo en Python
para que active un peque~no ventilador de 3v3, el comando que usare es
el estandard para hacer para conocer la temparatura de la raspberry pi:

	/opt/vc/bin/vcgencmd measure_temp | egrep "[0-9.]{4,}" -o

Al ejecutarlo tomar la informacion de la temperatura compararlo con el 
limite de temperatura que fue previamente establecido, y activar o 
desactivar el pin deseado para que funcione el abanico.

Pretendo no tener que utilizar las librerias del GPIO, y mejor utilizar
commandos directos con el sistema de ficheros de linux para controlar 
los pines directamente, por que creo que hay una especie de bloqueo, y no
quiero tener que correr el archivo todo el tiempo, lo que espero es 
programar la ejecucion y al ejecutarlo que se active el abanico en caso 
de ser necesario, y que se mantenga encendido o apagado, hasta que vuelva
a correr el script de nuevo.
