# creamos la lista de productos 


productos = {
    "M001": ["Alimento premiun", "comida", "DogPlus", 10, True , False],
    "M002": ["Arena Aglomerante", "higiene" , "CatClean", 8, False, False],
    "M003": ["Snack Dental", "snack", "biteJoy", 1, True,True],
    "M004": ["Shampoo Suave", "higiene","PetCare", 0.5, False, True],
    "M005": ["Correa Nylon", "accesorio", "WalkPro", 0.3,True, False],
    "M006": ["Cama Mediana", "accesorios", "CozyPet", 2, False, False],
    
#creamos el stock de los productos

}

stock = {
    "M001": [32990,12],
    "M002": [9990, 0],
    "M003": [5490, 25],
    "M004": [7990, 5],
    "M005": [11990, 7],
    "M006": [24990, 3],

}

# vamos a crear el menu para pdoer interactuar con el usuario
def menu():
    print("1) Unidades por categoria")
    print("2) Busqueda de productos por rango de precio")
    print("3) Actualizar precio de producto")
    print("4) Agregar producto")
    print("5) Elimiar producto")
    print("6) Salir")

#validamos el stock de nuestra tiend

def stock_market(market):
    total = 0

    for necesidad in productos:
        if productos [necesidad][0].lower == market.lower():
            total += stock[necesidad][1]
            print("stock disponible",total)



def busqueda_productos(p_min , p_max):
    lista = []
    for necesidad in stock:
        precio = stock[necesidad][0]
        if p_min <= precio <= p_max:
            market = productos[necesidad][0]
            lista.append(f"{market}{necesidad}")
            
    if len(lista) == 0:
        print("no hay productos disponibles")
    else:
        lista.sort()
        print("lista")


#ahora le diremos al usuario que busque el codigo que desee

def buscar_codigo(codigo,):
    
    codigo = input("ingreses un codigo")

    if codigo in productos:
        stock[codigo][0] = productos
        return True
    else:
        return False
    
# ahora haremos que el usuario pueda actualizar su precio

def actualizar_precio(codigo, precio):
    if codigo in stock:
        stock[codigo][0] = precio
        return True
    else:
        return False
    
#lo mismo pero agregando sus productos
def agregar_productos(codigo,necesidad):
    if codigo in necesidad:
        productos += stock[necesidad][0]
        productos.append(codigo,necesidad)


#ahora vamos a ingresar la opcion de poder eliminar productos que ya no desee

def elimiar_producto(codigo):
    print(buscar_codigo)


# vamos a validar las opciones de nuestro menu 
while True:

    menu()

    opcion = input("ingrese una opcion del menu")

    if opcion == "1":
        market = input("ingrese una categoria")
        stock_market(market)

    elif opcion == "2" :
        while True:
            try:
                minimo = int(input("ingrese un precio minimo"))
                maximo = int(input("ingrese un precio maximo"))
                if minimo > maximo:
                    print("ingrese un valor entero ")
                else:
                    busqueda_productos(minimo , maximo)
                    break

            except ValueError:
                print("ingrese un valor entero")

    elif opcion == "3":
        while True:
            necesidad = input ("ingrese su necesidad")

            try:
                precio = int(input("ingrese un nuevo precio"))
            except ValueError:
                print("debe ingresar un precio valido")
                continue

            if actualizar_precio(necesidad,precio):
                print("precio actualizado")
            else:
                print("la necesidad no se encontro")

            respuesta = input("desea actualizar su precio (si/no)").lower()

            if respuesta != "Si":
                break



    elif opcion == "4":
            print("agregue su producto nuevo")
            agregar_productos(necesidad)
            print("su producto se agrego correctamente")


    elif opcion == "5":
        print("ingrese el codigo a eliminar")
        
    

    elif opcion == "6":
        print("programa finalizado")
        break
    else:
        print("debe ingresar una opcion valida")




            
        















    
                   




    





