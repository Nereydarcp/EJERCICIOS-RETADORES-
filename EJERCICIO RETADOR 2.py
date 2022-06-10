
#Lista de municipios Guasave, Sinaloa de Leyva y El fuerte 
lista_municipios = ["guasave", "sinaloa de leyva", "el fuerte"]
#Lista de habitantes por cada municipio en el orden Guasave, Sinaloa de Leyva y El Fuerte 
lista_habitantes = [289370, 88659, 96593]

#Paso 1. (instrucción 1) Se solicita al usuario ingresar un punicipio  
municipio_usuario = input('ingresa nombre de un municipio: ')
lista_municipios.append(municipio_usuario)
print("el municipio que se agregó es: "+ municipio_usuario)
#print(lista_municipios)

#Paso 2. (Instrucción 2) Se solicita el numero de habitanes del municipio 1
numero_habitantes_por_municipio = input('ingresa el numero de habitantes:' )
lista_habitantes.append(numero_habitantes_por_municipio)
print("El numero de habitantes que se agregó es: "+ numero_habitantes_por_municipio)

#paso 3. (instrucción 1) Se repite por segunda vez el paso 1
municipio_usuario = input('ingresa nombre de un segundo municipio: ')
lista_municipios.append(municipio_usuario)
print("el municipio que se agregó es: "+ municipio_usuario)
#print(lista_municipios)

#paso 4. (instrucción 2) Se repite por segunda vez el paso 1
numero_habitantes_por_municipio = input('ingresa el numero de habitantes:' )
lista_habitantes.append(numero_habitantes_por_municipio)
print("El numero de habitantes que se agregó es: "+ numero_habitantes_por_municipio)

#paso 5. (instrucción 1) Se repite por tercera vez el paso 1
municipio_usuario = input('ingresa nombre de un tercer municipio: ')
lista_municipios.append(municipio_usuario)
print("el municipio que se agregó es: "+ municipio_usuario)
#print(lista_municipios)

#paso 6. (instrucción 2) Se repite por tercera vez el paso 1
numero_habitantes_por_municipio = input('ingresa el numero de habitantes:' )
lista_habitantes.append(numero_habitantes_por_municipio)
print("El numero de habitantes que se agregó es: "+ numero_habitantes_por_municipio)



#Total de habitantes 
#Carlos: Aquí estás creando una variable innecesaria; fíjate que no la vuelves a utilizar. Te recomiendo en su lugar para imprimir mensajes simplemente utilices la función: print('El total de habitantes por municipio es: ')
total_habitantes = (lista_habitantes[0] + lista_habitantes[1] + lista_habitantes[2])
print(total_habitantes)

#Promedio del total de habitantes de los tres municipios 
suma_promedio_total_habitantes = input('El promedio de los tres municipios es: ' )
#Carlos: mismo caso, esta variable no se utiliza para nada.
promedio_habitantes = (total_habitantes / len(lista_municipios))
#Carlos: En este caso es incorrecto, ya que en un principio diste de alta tres municipios, mas los 3 municipios que agrega el usuario, tienes un total de 6 municipios. Para que tu programa pueda sacar el promedio de cualquier cantidad de municipios prueba con la función len() que te da el total de municipios que hay en la lista : len(lista_municipios)
print(promedio_habitantes)


