clase sintactico
hara llamadas al analizador lexico
y construira el AST correspondiente a la linea
leida
el constructor de la clase sintactico cuyo constructor recibe un
analizador lexico que almacena en el atributo lexico.
Ademas, llama a siguiente del analizador
lexico y almacena el resultado en el atributo componente.

tendra conjunto de metodos: 
analizalinea, analiza expresion, analizatermino y analizafactor, ninguno
tendra parametros y su ejecucion supondra analizar la
entrada desde el punto donde se obtuvo el
 ultimo valor de componente hasta que se haya encontrado
una lnea, una expresion, un termino o un factor, 
respectivamente, y devolver el arbol
correspondiente.