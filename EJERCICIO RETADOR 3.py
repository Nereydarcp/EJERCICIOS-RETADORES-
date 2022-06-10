#Lista_materiales = ["cemento", "yeso"]
Lista_pesos = [40, 30]
Capacidad_carga_kg = 3254
#Entrada 
Numero_costales_cemento = int(input('Número de costales cemento en kg: '))
Peso_total_cemento = (Lista_pesos[0] * Numero_costales_cemento)

Numero_costales_yeso = int(input('Número de costales yeso en kg: '))
Peso_total_yeso = (Lista_pesos[1] * Numero_costales_yeso)

#Salida 
Peso_total = Peso_total_cemento + Peso_total_yeso
print('El peso total es: ', Peso_total)

Realiza_envio = Peso_total > Capacidad_carga_kg*0.5 or Peso_total <= Capacidad_carga_kg
print('¿Se puede realizar el envio?: ', Realiza_envio)


