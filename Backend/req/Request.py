import socket
import sys
s = socket.socket()
s.bind(("localhost",9999))
s.listen(10) # Acepta hasta 10 conexiones entrantes.
sc, address = s.accept()

print (address)
#i es el número de archivos que hay ya creados en pdf
i=1
f = open("file_"+ str(i)+".pdf","wb") # Open in binary
i=i+1
#while (True):
# Recibimos y escribimos en el fichero
l = sc.recv(1024)
while (l):
    f.write(l)
    l = sc.recv(1024)
    f.close()
sc.close()
s.close()