from Clase_pregunta import Pregunta

p1 = Pregunta(2,"Expresion que utilizarias para hacer match con 'ABCDEFabcdef123450' ",'ABCDEFabcdef123450',"Considera letras y numeros")
p2 = Pregunta(1,"Haz match con '@ironhackmexico'","@ironhackmexico","No olvides el @")
p3 = Pregunta(1,"Considerando 02-11-2013, que usarias para regresar la fecha?" ,"02-11-2013","Recuerda usar '\' para especificar caracteres")
p4 = Pregunta(2,"Haz match con '#insta<3U'","#insta<3U","Considera todos los caracteres especiales")
p5 = Pregunta(1,"Expresion que utilizarias para obtener un string con los primeros 10 caracteres de la CURP","SDGH980427","Recuerda que se compone de 4 letras y 6 numeros!")
p6=Pregunta(0,"Haz match con 'parangaricutirimicuaro'","parangaricutirimicuaro","Revisa el tipo de caracter empleado")
p7=Pregunta(1,"Con que expresion guardarias el telefono  '55 3349 9000'?","55 3349 9000","Considera los espacios intermedios!")
p8=Pregunta(1,"Cómo guardarias los correos de dominio @gmail?","ironhacker@gmail.com","Toma como ejemplo ironhacker@gmail.com")
p9=Pregunta(1,"Expresion que utilizarias para obtener 'wazzzzzzzup'",'wazzzzzzzup',"Puedes usar + o * para repeticiones" )
p10=Pregunta(0,"Sabes cual es la expresión para devolver un digito?","9","Necesitas el back slash")
p11=Pregunta(2,"Haz match con '#happ33b1rthd4y'","#happ33b1rthd4y","Checa el orden #wwwdd...")
p12=Pregunta(1,"Cómo buscarias cualquier mayuscula? ","Q","Necesitas el back slash")

# Las juntamos en una lista para poder después hacer index
todas_las_preguntas = [p1, p2, p3, p4, p5,p6,p7,p8,p9,p10,p11,p12]