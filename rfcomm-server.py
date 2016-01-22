import os
import random
from bluetooth import *

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SmartBike",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )
while True:          
	print "Esperando por una conexion RFCOMM en canal %d" % port

	client_sock, client_info = server_sock.accept()
	print "Conexion aceptada desde:  ", client_info

	try:
	        data = client_sock.recv(1024)
        	if len(data) == 0: break
	        print "Recibido [%s]" % data

		if data == '1':
			data = str(random.randint(0, 500)) + '!'
		else:
			data = 'Comando invalido!' 
	        client_sock.send(data)
		print "Enviando [%s]" % data

	except IOError:
		pass

	except KeyboardInterrupt:

		print "Desconectado"

		client_sock.close()
		server_sock.close()
		print "Todo listo"

		break
