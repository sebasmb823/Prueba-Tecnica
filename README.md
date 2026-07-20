
# Prueba técnica 

**COMO EJECUTAR EL CODIGO:**

**Requisitos:**
- Python
- Librería de pandas
- Archivo transacciones.csv
- Archivo clientes.json

**Ejecución:**
- Crear una carpeta donde estén almacenados los archivos de transacción, clientes y el archivo de Python
- Ejecutar el archivo de Python 
- Al finalizar la ejecución el programa va a generar en la carpeta un archivo llamado "baseDatosLimpia.csv" que contiene la información de transacciones y clientes después del proceso de limpieza y unión de ambas bases de datos. Este archivo será el insumo para el dashboard de power bi.

**Nota:** En el código de Python hay varias líneas comentadas su propósito fue comprobar que los procedimientos realizados funcionaran correctamente y validar el antes y después.

**Que encontré:**
**dataset de transacciones.csv**
- Hay fechas en diferentes formatos
- En la columna tipo_producto los nombres no están estandarizados y están escritos de diferentes formas
	  por ejemplo AHORROS, ahorros, CTA_AHORROS
- En la columna monto hay valores nulos, hay valores numéricos combinados con letras
- La columna moneda no hay un estándar para el tipo de moneda por ejemplo Dolares, USD
- La tasa_interes tiene valores vacíos y valores N/A
- El plazo_dias hay valores vacíos, N/A, hay números combinados con letras
- en la columna canal los canales están escritos de diferente forma no hay un estándar también aplica para las columnas estado y sucursal

**dataset de clientes.json**
- el tipo documento no tiene un formato estándar
- si el cliente esta activo aparece como true, Si, false, No
- el numero de documento no tiene formato y hay algunos con puntos
- hay números de teléfono con el indicativo de país
- el segmento también carece de estandarización ya que se encuentra personal y Personal, premium y Premium
- Los nombres de las ciudades tampoco están estandarizados incluso hay nombres abreviados
- Hay clientes repetidos como Santiago Vargas


**LIMPIEZA DATASET TRANSACCIONES:**

**Columna fechas:** Para la limpieza de la columna de fechas use ia para encontrar la mejor de estandarizar fechas con múltiples formatos

**Columna Tipo producto:** se estandarizo la columna

**Columna monto:** 	En la columna monto lo único que elimine fue el carácter $ y la palabra COP ahora con lo valores
	       	negativos no los elimine ya que posiblemente pueden ser devoluciones ya que el dataset es de 		       	transacciones. los montos vacíos y los que decían sin dato se imputaron por el valor 0.
	       	Al terminar la limpieza encontré un problema al tratar los valores de dólares ya que 		        		eliminar los decimales quedaron números 1000 veces mayor en este punto use ia para poder tener un   		panorama mas claro de como tratar los valores en dólares me di cuenta de que había un error ya que 		verifique la conversión que había hecho en la nueva columna y vi que los valores quedaron muy altos 		lo que me aporto la ia en este caso fue crear una mascara de falsos y verdaderos para limpiar 			primero los valores en pesos y luego los valores en dólares para llegar al ultimo paso de convertir los valores 		a tipo numérico aunque el código me estaba dando un error y era con el tipo de moneda que estaban 		sin categorizar revise cuales eran estos valores y vi que estaban en formato COP por lo que les 		aplique la misma limpieza que hice al formato COP.
            No tome la decisión de eliminar las filas que estaban sin categorizar ya que es información 			financiera y los formatos de los números eran validos y considere que puede ser información útil
	
**Columna moneda:** Luego de limpiar y estandarizar los datos para los datos faltantes tome la decisión de clasificarlos como "Sin categoría" para que al llevarlos al tablero de power bi no hayan datos nulos. 

**Columna tasa de interés:** Se elimino el % los datos que estaban vacíos se imputaron con el valor de 0 ya que este valor no afecta el valor de la tasa de interés para cálculos futuros

**Columna plazo días:** Se elimino la palabra días y los valores vacíos se imputaron como 0

**Columna canal:** se estandarizo la columna 

**Columna estado:** se estandarizo la columna

**Columna sucursal:** Se corrigieron los nombres de las ciudades y las transacciones que no tenían una sucursal asignada se colocaron sin sucursal



**LIMPIEZA DATASET CLIENTES**

Después de analizar el dataset encontré que el id_cliente 1004 y 1011 son los clientes duplicados antes de proceder a eliminar los duplicados compare la información de cada fila usando print(df_clientes[df_clientes["id_cliente"] == 1004].T) para ver la información en formato vertical y poder comparar la informacion de cada uno. Al revisarla encontré que es la misma información y ejecute la herramienta de eliminar duplicados.


**Columna tipo documento:** estandarice los tipos de documentos como C.C. y NIT con los valores vacíos los impute como 			"Sin tipo documento"

**Columna numero documento:** hay ciertos números de documento con puntos los cuales elimine y deje solo el numero. Hay algunos NIT que tienen el digito de verificación 
no los elimine ya que se debe revisar los estándares de limpieza de datos de la empresa     			  para tomar la decisión ya que hay la posibilidad que para la empresa sean necesarios.

**Columna segmento:** Estandarice los nombres de los segmentos y las filas vacías las deje como "Sin segmento"

**Columna ciudad:** Estandarice los nombres de las ciudades

**Columna activo:** se limpiaron los valores y se dejaron como tipo de dato booleano

**Columna fecha:** se eliminaron las abreviaturas del mes como ago, sep por el numero del mes luego se le aplico el mismo formato a todas las fechas






 


