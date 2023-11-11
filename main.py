import os

os.system("python --version")

# Proyecto Bucles: Carly's Clippers

#Se le han proporcionado tres listas:

#1 - peinados: los nombres de los cortes ofrecidos en Carly's Clippers.

#2 - precios: el precio de cada peinado de la lista de peinados.

#3 - última_semana: el número de compras de cada tipo de peinado en la última semana.

#Cada índice en peinados corresponde a un índice asociado en precios y última_semana.

#Por ejemplo, El peinado "bouffant" tiene un precio \
#asociado de 30 de la lista de precios, y fue comprado 2 veces en la última \ 
#semana como se muestra en la lista last_week. \
#Cada uno de estos elementos se encuentra en el primer índice de sus respectivas listas.

peinados = ["militar", "afro", "high fade", "caesar corto"]

precios = [1800, 1500, 2000, 2500]

ultima_semana = [2, 4, 8, 7]

# Step 1 Variable igual a 0
precio_total = 0

# Step 2 Bucle For
for precio in precios:
  precio_total += precio

# Step 3 Utiliza la funcion len para saber el numero \ 
#de cortes de pelo y aquel valor ubicarlo en una nueva \
#variable llamada = precio_medio

precio_medio = precio_total / len(precios)

# Step 4 Imprimo y concateno el valor del precio medio
print("El valor del precio medio: " + str(precio_medio))

# Step 5 Reduzco el precio con la utilizacion de Comprension de Listas
nuevos_precios = [precio - 5 for precio in precios]

# Step 6 imprimo el valor de nuevos precios
print("Los nuevos precios: " + str(nuevos_precios))

# ========================================================================
# Ingresos

# Step 7 Creo una nueva variable igual a 0
total_ingresos = 0

# Step 8 Usa un bucle for para crear una variable i \
# que vaya de 0 a len(peinados), utilizo range
for i in range(len(peinados)):
  total_ingresos += precios[i] * ultima_semana[i] 

# Step 9 Imprimo y concateno valores int
print("Total de Ingresos: " + str(total_ingresos))

# Step 10 Ingresos medios 
ingresos_medios_diarios = total_ingresos / 7
print(ingresos_medios_diarios)

# Step 11 otro descuento más Compresion de Listas (bucle for, range, len)
descuento_1080 = [peinados[i] for i in range(len(peinados)) if nuevos_precios[i] < 1800]

# Step 12 Imprimo descuento_30
print(descuento_1080)