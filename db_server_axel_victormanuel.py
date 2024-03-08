"""
Equipo:
Campos Espinosa de los Monteros Axel
Feregrino Zamorano Victor Manuel
"""

import socket
import threading
import pandas as pd

# Leer la documentación siguiendo este orden:
# 1. Leer if __name__ == "__main__":
# 2. Leer start_server()
# 3. Leer handle_client()
# 4. Leer broadcast()

# Handle Client: Recibe un socket de un cliente y una dirección IP.
def handle_client(client_socket, addr): 
    nickname = client_socket.recv(1024).decode()
    print(f"El nickname es: '{nickname}'") #Se comprueba que salga bien el nuevo nombre del usuario dentro del servidor
    #usuario = {} #Declare el diccionario del nuevo usuario
    #test = cuentas.get(nickname,False)#Forma de saber si el usuario existe del profe
    repetir = 'S'
    while repetir == 'S':
        try:
            opcion = client_socket.recv(1024).decode()
            if not opcion:
                print(f"Conexion con '{addr}' cerrada.")
                break
            if(opcion == 1): #CONSULTAS 
                Criterio = client_socket.recv(1024).decode()
                if not Criterio:
                    print(f"Conexion con '{addr}' cerrada.")
                    break
                if(Criterio == "1"): #NOMBRE
                    Nombre = client_socket.recv(1024).decode()
                elif(Criterio == "2"): #EMAIL
                    Email = client_socket.recv(1024).decode()
                elif(Criterio == "3"): #EMAIL
                    Edad = client_socket.recv(1024).decode()
                    Operador = client_socket.recv(1024).decode()
                elif(Criterio == "4"): #EMAIL
                    Genero = client_socket.recv(1024).decode()

            elif(opcion == 2): #REGISTROS
                Nombre = client_socket.recv(1024).decode()
                if not Nombre:
                    print(f"Conexion con '{addr}' cerrada.")
                    break
                Password = client_socket.recv(1024).decode()
                if not Password:
                    print(f"Conexion con '{addr}' cerrada.")
                    break
                Genero = client_socket.recv(1024).decode()
                if not Genero:
                    print(f"Conexion con '{addr}' cerrada.")
                    break
                Edad = client_socket.recv(1024).decode()
                if not Edad:
                    print(f"Conexion con '{addr}' cerrada.")
                    break
                Email = client_socket.recv(1024).decode()
                if not Email:
                    print(f"Conexion con '{addr}' cerrada.")
                    break
                Mensaje = insercion(Nombre,Password,Genero,Edad,Email)
                broadcastAlClienteActual(Mensaje, client_socket)


            #message = client_socket.recv(1024).decode()
            #if not message:
                #print(f"Conexion con '{addr}' cerrada.")
                #break
            #broadcastAlClienteActual(message, client_socket)
        except Exception as e:
            client_socket.close()
            print(f"Conexion con cliente '{addr}' perdida por: '{e}'")
            break

def broadcastAlClienteActual(message, sender_socket):
    print("Entra al metodo 'broadcastToCurrentClient'")
    for client in clients:
        print(f"El socket del cliente es: '{client}', y el del argumento es: '{sender_socket}'")
        if client == sender_socket:
            try:
                #print(message.encode())
                #print(f"{cuentas[nombreUsuario]}:{message.encode()}")
                #mensaje = "\n"+nombreUsuario+": "+message
                mensaje = "Tu consulta es: "+message
                print(f"El mensaje debería verse así: '{mensaje}'")
                client.send(mensaje.encode())
            except Exception as e:
                print(f"Error enviando mensaje: '{e}'")

def consultas(valor, criterio, operador): #CONSULTAS GENERALIZADAS
    data = pd.read_csv("DB.csv")
    if(operador==1):
        print("El operador es 'Igual a'")
        data[data[f"{criterio}"]==valor]
    elif(operador==2):
        print("El operador es 'Mayor que'")
        data[data[f"{criterio}"]>valor]
    elif(operador==3):
        print("El operador es 'Menor que'")
        data[data[f"{criterio}"]<valor]

def insercion(nombre, password, genero, edad, email): #INSERCION DE REGISTROS
    sentenciainsert = f"{nombre},{password},{genero},{edad},{email}\n"
    with open("DB.csv","a") as file:
        file.write(sentenciainsert)
    return sentenciainsert
    

# Start Server: Función que inicia el servidor, en esta función se levantan
# hilos en el servidor para manejar múltiples clientes.
def start_server():
    server_socket = socket.socket(
        socket.AF_INET,     # Especifica la familia direcciones, como la IPV4
        socket.SOCK_STREAM  # Este argumento especifica que se usará el 
                            # protocolo TCP (Transmission Control Protocol) 
                            # como medio de comunicación
    )
    # Se establece la comunicación por localhost o 127.0.0.1 en caso de ser 
    # local, o 0.0.0.0 en caso de escuchar a clientes externos. En el puerto
    # que se especifique, en este caso puede ser 5000.
    server_socket.bind(('127.0.0.1', 5000))
    # Se establecen el número de conexiones que puede procesar el servidor al
    # mismo tiempo antes de empezar a rechazar nuevas conexiones.
    server_socket.listen(4)
    
    #print("Server started. Waiting for connections...")
    print("Server iniciado. Esperando conexiones...")
    # Se ejecuta en un ciclo infinito el proceso de escuchar la red para
    # esperar nuevos clientes.
    while True:
        # Se acepta un nuevo socket con el método accept, el cual regresa
        # dos argumentos, el objeto socket del cliente y la dirección de
        # este
        client_socket, addr = server_socket.accept()
        #print(f"Connection established with {addr}")
        print(f"Conexion establecida con: '{addr}'")
        # Se agrega el nuevo cliente a la lista de clientes
        clients.append(client_socket)
        # Usando la paquetería de threading se crea un nuevo hilo para la
        # nueva conexión.
        # Un hilo recibe al menos dos argumentos:
        # - Un target (función destino): Este argumento es la función que va
        #   a ejecutar en el hilo
        # - args (Argumentos): Aquí se espera una tupla con todos los 
        #   argumentos de la función colocada en target, en este caso se 
        #   envían dos
        client_thread = threading.Thread(
            target = handle_client, 
            args   = (client_socket, addr)
            #args   = (client_socket, addr, clients)
        )
        # Se inicia la ejecución del hilo con el método start()
        client_thread.start()

# Lista para guardar los sockets de los clientes conectados
clients = []

# Directiva main para iniciar el servidor
if __name__ == "__main__":
    # Se ejecuta el método del servidor
    start_server()
