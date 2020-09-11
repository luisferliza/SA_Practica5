# importing the requests library 
import requests 

print("#################################")
print("############ CLIENTE ############")
print("#################################\n")

# Funciones de peticiones
def create_food_request(comida):
    print("\n------- Inicio de Peticion -------")    
    print("Enviando un pedido de", comida, "al restaurante")    
    r = requests.post(url = "http://localhost:5000/orderfood", json = {'food': comida})        
    print("El restaurante respondio", r.json())
    print("------- Peticion terminada -------\n")  


def ask_state_restaurant(identifier):    
    print("\n------- Inicio de Peticion -------")    
    print("Solicitando al restaurante el estado del pedido", identifier, "...")
    r = requests.get(url = "http://localhost:5000/restaurantstate/"+identifier)  
    print("El restaurante respondio", r.json())
    print("------- Peticion terminada -------\n")  


def ask_state_driver(identifier):    
    print("\n------- Inicio de Peticion -------")  
    print("Solicitando al repartidor el estado del pedido", identifier, "...")
    r = requests.get(url = "http://localhost:5000/driverstate/"+identifier)  
    print("El repartidor respondio", r.json())
    print("------- Peticion terminada -------\n")  

# Funciones de GUI
def show_menu():    
    print("1. Solicitar un pedido al restaurante")
    print("2. Verificar el estado del pedido al restaurante")
    print("3. Verificar el estado del pedido al repartidor")
    print("4. Salir")


def select_option():
    while True:
        show_menu()
        selection = input("Ingrese la opcion deseada:\n")
        if selection == "1":
            create_food_request("Sushi")
        elif selection == "2":
            ask_state_restaurant("123456")
        elif selection == "3":
            ask_state_driver("123456")
        elif selection == "4":
            break
        else:
            print("Ingrese una opcion válida")

select_option()