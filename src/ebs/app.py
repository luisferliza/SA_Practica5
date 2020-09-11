from flask import Flask, jsonify, request
import requests


app = Flask(__name__)


print("#################################")
print("############## EBS ##############")
print("#################################\n")

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"}), 200 

@app.route('/orderfood', methods=['POST'])
def order_food():
    print("-------------------- Inicio de Peticion --------------------")        
    print("Datos recibidos: ", request)        
    r = requests.post(url = "http://localhost:3000/request_food", data = {'food': request.json["food"]})           
    print("Datos retornados: ", r.json())
    print("-------------------- Fin de Peticion --------------------")        
    return r.json()   
    
    
@app.route('/restaurantstate/<identifier>')
def food_state_restaurant(identifier):
    print("-------------------- Inicio de Peticion --------------------")        
    print("Se está solicitando al repartidor el estado del pedido", identifier)     
    r = requests.get(url = "http://localhost:3000/ask_state", params = {'id':identifier})      
    print("Datos retornados: ", r.json())
    print("-------------------- Fin de Peticion --------------------")  
    return r.json()


@app.route('/driverstate/<identifier>')
def food_state_driver(identifier):
    print("-------------------- Inicio de Peticion --------------------")        
    print("Se está solicitando al restaurante el estado del pedido", identifier)     
    r = requests.get(url = "http://localhost:3200/ask_state", params = {'id':identifier})  
    print("Datos retornados: ", r.json())
    print("-------------------- Fin de Peticion --------------------")        
    return r.json()


@app.route('/notify_driver', methods=['POST'])
def notify_driver():
    print("-------------------- Inicio de Peticion --------------------")        
    print("Datos recibidos: ", request.json)        
    r = requests.post(url = "http://localhost:3200/notify_order", json = {'id': request.json["id"]})           
    print("Datos retornados: ", r.json())
    print("-------------------- Fin de Peticion --------------------")        
    return r.json()   

if __name__ == '__main__':
    app.run(debug=True)
