"""
Enrique S. Fernandez
Ejercicio Integrador 01
La división de higiene está trabajando en un control de stock para productos sanitarios. 
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe 
obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 
unidades)
4. La marca y el Fabricante.

Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.
"""
flag = True
barbijo_mas_caro = {"precio": 0, "cantidad": 0, "marca": ""}
item_con_mas_unidades = {"cantidad": 0, "marca": ""}
contador_de_jabones = 0
for i in range(5):
    tipo_de_producto = input("barbijo, jabón o alcohol:\n")
    #while tipo_de_producto != "barbijo" and tipo_de_producto != "jabón" and tipo_de_producto != "alcohol":
    while tipo_de_producto not in ["barbijo", "jabon", "alcohol"]:# el not in me sirve para verificar dentro de ese array que hice con las opciones
        tipo_de_producto = input("Debe ingresar uno de estos 3 (barbijo, jabón o alcohol):\n")
    
    precio_producto = int(input("Ingrese el precio del producto (entre 100 y 300):\n"))
    while precio_producto < 99 or precio_producto > 300:
        precio_producto = int(input("El precio debe estar entre 100 y 300:\n"))
    
    cantidad_de_productos = int(input("Ingrese la cantidad de unidades (no puede ser 0 ni negativo y no debe superar las 1000 unidades):\n"))
    while cantidad_de_productos < 0 or cantidad_de_productos > 1001:
        cantidad_de_productos = int(input("La cantidad de unidades no puede ser 0 y no debe ser mas de 1000:\n"))
    
    la_marca_o_fabricante = input("Ingrese la marca y el fabricante:\n")
    
    #A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
    if tipo_de_producto == "barbijo":
        if precio_producto > 0:
            barbijo_mas_caro["precio"] = precio_producto
            barbijo_mas_caro["cantidad"] = cantidad_de_productos
            barbijo_mas_caro["marca"] = la_marca_o_fabricante
        
        if precio_producto > int(barbijo_mas_caro["precio"]):
            barbijo_mas_caro["precio"] = precio_producto
            barbijo_mas_caro["cantidad"] = cantidad_de_productos
            barbijo_mas_caro["marca"] = la_marca_o_fabricante

    #B. Del ítem con más unidades, el fabricante.
    if cantidad_de_productos > 0 and flag == True:
        flag = False
        item_con_mas_unidades["cantidad"] = cantidad_de_productos
        item_con_mas_unidades["marca"] = la_marca_o_fabricante
    elif cantidad_de_productos > item_con_mas_unidades["cantidad"]:
            item_con_mas_unidades["cantidad"] = cantidad_de_productos
            item_con_mas_unidades["marca"] = la_marca_o_fabricante

    #C. Cuántas unidades de jabones hay en total.
    if tipo_de_producto == "jabon":
        contador_de_jabones += 1

print("El más caro de los barbijos es ",barbijo_mas_caro["marca"]," con ",barbijo_mas_caro["cantidad"]," unidades.")
print("El objeto con mas unidades es de la marca: ",item_con_mas_unidades["marca"]," con ",item_con_mas_unidades["cantidad"],".")
print("Esta es la cantidad de unidades de jabones que se compro: "+str(contador_de_jabones))