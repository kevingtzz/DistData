## **LAB 1:** Protocolo de comunicación cliente - servidor mediante programación en sockets

**Descripción:**
Esta aplicación que utiliza la programación en sockets TCP para establecer una comunicación entre un cliente y un servidor funciona como un sistema de buckets en el cual desde el cliente se permiten realizar las acciones basicas para el almacenamiento de archivos por medio de comandos

**Lista de comandos**

 1. LIST_BUCKET: ver lista de buckets disponibles
 2. NEW_BUCKET: crear nuevo bucket
 3. DELETE_BUCKET: eliminar bucket
 4. UPLOAD_FILE: subir un nuevo archivo
 5. LIST_FILE: listar los archivos de un bucket especifico
 6. DOWNLOAD_FILE: descargar un archivo
 7. DELETE_FILE: eliminar un archivo

	**Nota:** En esta version, ninguno de los anteriores comando recibe ningun tipo de argumento, la información necesaria para realizar las acciones requeridas sera solicitada luego de ingresar el comando

**Requisitos de software:**

	 - Python 3.x


**Intrucciones de ejecución**

 1. Correr el servidor, para esto dentro de la consola de nuestra instancia de AWS por ejemplo vamos a ejecutar:

	    python3 server.py database_path
     
	En caso de que no exista aun la ruta que especifiques para tu base de datos, se creará automaticamente (En esta version, la ruta de tu base de datos puede ser cualquier carpeta ej. home/ubuntu/db_test; revisa en el archivo server.py que la direccion ip en la cual se inicializa el servidor sea la ip privada de tu instancia)


2. Puedes ejecutar uno o varios clientes desde donde desees, en el archivo constans.py se asigna la ip publica del sirvidor al cual deseas conectarte y su puerto

	    python3 client.py


**Nota:** En esta version, se asume que todas las rutas de archivos que ingreses para subir o descargar existen y son correctas
