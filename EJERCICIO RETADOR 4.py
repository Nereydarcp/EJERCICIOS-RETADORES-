#El programa deberá solicitarle al responsable del almacén de distribución ingresar la siguiente
#información: cantidad de cajas a vender y el tipo de producto por ID (Ver tabla 1).
#Posterior a esto, el programa deberá mostrar como salida, el nombre del producto que se
#seleccionó, el precio unitario por caja para ese producto y el monto total de la venta, teniendo
#en cuenta un costo de envío de $1,500 pesos, siempre y cuando la cantidad de cajas a vender
#sea menor o igual a 100 unidades.

Productos = ["Maíz", "Grano", "Pepino", "Tomate verde"]
ID_productos = [1, 2, 3, 4]

Precio_maíz=float(285.55)
Precio_pepino=float(334.72)
Precio_tomate=float(129.00)

#Entradas 
Cantidad_cajas_para_vender = int(input('Ingrese la cantidad total de cajas a vender: '))

ID_producto = int(input('Ingresa el ID del producto: '))

Precio_cajas_maíz=int(Cantidad_cajas_para_vender)*(Precio_maíz)
Precio_cajas_pepino=int(Cantidad_cajas_para_vender)*(Precio_pepino)
Precio_cajas_tomate=int(Cantidad_cajas_para_vender)*(Precio_tomate)

if ID_producto ==1:
 print("El producto es: Grano de maíz")
 print("El precio por caja es de", (Precio_maíz))
 print("El importe total a pagar es de:", (Precio_cajas_tomate))
       

elif ID_producto ==2: 
 print("El producto es: Pepino")
 print("El precio por caja es de: ", (Precio_pepino))
 print("El importe a pagar es de:", (Precio_cajas_pepino))

elif ID_producto ==3:
 print("El producto es: Tomate verde")
 print("El precio por caja es de:", (Precio_tomate))
 print("El total a pagar es de:", (Precio_cajas_tomate))




