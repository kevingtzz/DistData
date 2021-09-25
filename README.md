## **Proyecto 1:** 

**Descripción:**
Esta aplicación se compone de tres partes, un cliente que se encarga de solicitar las peticiones, un servidor que las recibe, procesa y decide a que nodo almacenar el dato, y un conjunto de nodos que almancenan los datos.

La comunicación entre todos los procesos se hace medianto sockets TCP.

**Lista de comandos**

 Cuando se inicializa la aplicación lo primero en solicitar es el comando a usar, acontuación verás la lista de comandos disponible.

 1. PUT: Se usa para agregar un nuevo dato. (Al ingresar este comando se le solicitarán 2 parametros; key (palabra clave, ej: rojo), value (valor del dato, ej: manzana))
 2. GET: Se usa para recuperar un dato. (Al ingresar este comando se le solicitará el argumento key, este comando retornará todos los datos asociados al key ingresado)
 3. UPDATE: Se usa para modificar un dato. (Al ingresar este comando se le solicitarán 3 argumentos, el key, el valor que desea editar y el nuevo valor que desea que tenga)
 4. DELETE: Se usa para eliminar un dato. (Al ingresar este comando se le solicitará 1 argumento que será el key; tenga en cuenta que serán eliminados todos los datos asociados a la key ingresada)

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
