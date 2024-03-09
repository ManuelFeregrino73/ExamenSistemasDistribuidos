"""
Equipo:
Campos Espinosa de los Monteros Axel
Feregrino Zamorano Victor Manuel
"""

import socket
import threading
import time

InformacionRecibida = []

#MiUsuario = "Absalon" #Ejemplo de un usuario

def receive_information():
    repetir = 'S'
    while repetir != 'N':
        try:
            message = server_socket.recv(1024).decode(encoding='utf-8')
            if(message=='N'):
                print("Terminando el programa")
                repetir = 'N'
                break
            InformacionRecibida.append(message)
           # print(f"El mensaje ha sido recibido y se ha agregado a la lista 'InformacionRecibida': '{InformacionRecibida}'")
            #data_queue.put(message)  # Agregar el mensaje a la cola
            #print(message)
        except Exception as e:
            print(f"Error recibiendo información: '{e}'")
            break
    

def send_data():
    #nombre_usuario = input("Ingresa tu nombre de usuario: ")
    #server_socket.send(nombre_usuario.encode())
    print("A continuación se te mostrará un menú de funciones donde se te pedira ingresar un caracter numerico para entrar a dicha funcion.")
    repetir = 'S'
    while repetir == 'S':
        #message = input(f"{nombre_usuario} (Tu): ")
        print("-------------------------")
        print("-----MENU DE FUNCIONES------")
        print("-------------------------")
        print("1. Buscar Informacion (Consultar)")
        print("2. Ingresar un registro")
        try:
            opcion = input("Ingresa una opción: ")
        except EOFError:
            print("\nPrograma interrumpido. Saliendo...")
            opcion = None  # o cualquier otra acción que desees tomar al interrumpir el programa
        #opcion = input(f"Ingresa una opcion: ")
        try:
            server_socket.send(opcion.encode())
        except Exception as e:
            print(f"Error recibiendo mensaje: '{e}'")
            break
        if(opcion == "1"): #CONSULTAS 
            repetirConsulta1 = 'S'
            while  repetirConsulta1 == 'S':
                print("Elige en base a que criterio quieres hacerlo: ")
                print("1. Nombre")
                print("2. Email")
                print("3. Edad")
                print("4. Genero")
                Criterio = input(f"Ingresa una opcion: ")
                try:
                    server_socket.send(Criterio.encode())
                except Exception as e:
                    print(f"Error recibiendo mensaje: '{e}'")
                    break
                if(Criterio == "1"): #NOMBRE
                    Nombre = input(f"Ahora escribe el nombre: ")
                    try:
                        server_socket.send(Nombre.encode())
                    except Exception as e:
                        print(f"Error recibiendo mensaje: '{e}'")
                        break
                    #infoConsulta = data_queue.get()
                    #print("El mensaje va a ser utilizado")
                    print("Esperando 5 segundos para recibir el mensaje")
                    time.sleep(5) #Creo que es necesario usar time para poder captar la informacion del servidor
                    infoConsulta = InformacionRecibida[0]
                    #print(f"El mensaje debería verse asi: '{InformacionRecibida[0]}'")
                    InformacionRecibida.pop(0)
                    #print(f"El mensaje ha sido borrado de informacionRecibida: '{InformacionRecibida}'")
                    print(f"El resultado de la consulta por el nombre '{Nombre}' es: '{infoConsulta}'")
                elif(Criterio == "2"): #EMAIL
                    Email = input(f"Ahora escribe el email: ")
                    try:
                        server_socket.send(Email.encode())
                    except Exception as e:
                        print(f"Error recibiendo mensaje: '{e}'")
                        break
                    print("Esperando 5 segundos para recibir el mensaje")
                    time.sleep(5) #Creo que es necesario usar time para poder captar la informacion del servidor
                    infoConsulta = InformacionRecibida[0]
                    InformacionRecibida.pop(0)
                    print(f"El resultado de la consulta por el email '{Email}' es: '{infoConsulta}'")
                elif(Criterio == "3"): #EDAD
                    repetirConsulta2 = 'S'
                    while repetirConsulta2 == 'S':
                        Edad = input(f"Ahora escribe la edad: ")
                        try:
                            server_socket.send(Edad.encode())
                        except Exception as e:
                            print(f"Error recibiendo mensaje: '{e}'")
                            break
                        print("Ahora tienes que escoger la opcion numericamente de si quieres buscar una edad igual, mayor o menor a la que escribiste.")
                        print("1. Igual que (Operador '=')")
                        print("2. Mayor que (Operador '>')")
                        print("3. Menor que (Operador '<')")
                        Operador = input(f"Ingresa el numero del operador que quieres usar: ")
                        oper = int(Operador)
                        if(oper>=1 or oper<=3): #VERIFICAMOS QUE HAYA SELECCIONADO UNA OPCION VALIDA DE LOS OPERADORES
                            try:
                                server_socket.send(Operador.encode())
                            except Exception as e:
                                print(f"Error recibiendo mensaje: '{e}'")
                                break
                            print("Esperando 5 segundos para recibir el mensaje")
                            time.sleep(5) #Creo que es necesario usar time para poder captar la informacion del servidor
                            infoConsulta = InformacionRecibida[0]
                            InformacionRecibida.pop(0)
                            print(f"El resultado de la consulta por la edad '{Edad}' con el operador numero '{oper}' es: '{infoConsulta}'")
                        else:
                            print("ERROR!!! no ingresaste el numero de un operador valido")
                        repetirConsulta2 = input("Desea volver a intentar una consulta por Edad? S/N " )
                        try:
                            server_socket.send(repetirConsulta2.encode())
                        except Exception as e:
                            print(f"Error recibiendo mensaje: '{e}'")
                            break
                elif(Criterio == "4"): #SEXO
                    repetirConsulta3 = 'S'
                    while repetirConsulta3 == 'S':
                        Genero = input(f"Ahora escribe el sexo (0 para Masculino, 1 para Femenino): ")
                        if(Genero=="0" or Genero == "1"): # TIENE QUE INGRESAR EL SEXO MASCULINO O FEMENINO DE ACUERDO A COMO SE GUARDO EN 'BOOLEANO'
                            try:
                                server_socket.send(Genero.encode())
                            except Exception as e:
                                print(f"Error recibiendo mensaje: '{e}'")
                                break
                            print("Esperando 5 segundos para recibir el mensaje")
                            time.sleep(5) #Creo que es necesario usar time para poder captar la informacion del servidor
                            infoConsulta = InformacionRecibida[0]
                            InformacionRecibida.pop(0)
                            print(f"El resultado de la consulta por el sexo '{Genero}' es: '{infoConsulta}'")
                        else:
                            print("Error... La opción que elegiste no es valida. Debe elegir entre 0 para Masculino o 1 para Femenino ")
                        repetirConsulta3 = input("Desea intentarlo nuevamente?(S/N):") #REPETIR CICLO?
                        try:
                            server_socket.send(repetirConsulta3.encode())
                        except Exception as e:
                            print(f"Error recibiendo mensaje: '{e}'")
                            break
                else:
                    print("Error... La opción que elegiste para las consultas no es valida")
                repetirConsulta1 = input("Desea intentar otra consulta?(S/N):") #REPETIR CICLO?
                try:
                    server_socket.send(repetirConsulta1.encode())
                except Exception as e:
                    print(f"Error recibiendo mensaje: '{e}'")
                    break
            repetir = input("Desea realizar otra opcion?(S/N):") #REPETIR CICLO?
        elif(opcion == "2"): #REGISTROS
            Nombre = input(f"Ingresa el nombre del nuevo registro: ") #INGRESAR NOMBRE
            try:
                server_socket.send(Nombre.encode())
            except Exception as e:
                print(f"Error recibiendo mensaje: '{e}'")
                break
            Password = input(f"Escribe la contraseña del nuevo registro: ") #INGRESAR CONTRASEÑA
            try:
                server_socket.send(Password.encode())
            except Exception as e:
                print(f"Error recibiendo mensaje: '{e}'")
                break
            Genero = input(f"Ingresa el sexo del nuevo registro('0' para Masculino o  '1' para Femenino): ") #INGRESAR GENERO (SEXO)
            if(Genero=="0" or Genero == "1"):
                try:
                    server_socket.send(Genero.encode())
                except Exception as e:
                    print(f"Error recibiendo mensaje: '{e}'")
                    break
            else:
                print("ERROR!!! no ingresaste un sexo valido")
            Edad = input(f"Ahora ingresa la edad del nuevo registro: ") #INGRESAR EDAD
            try:
                server_socket.send(Edad.encode())
            except Exception as e:
                print(f"Error recibiendo mensaje: '{e}'")
                break
            Email = input(f"Por ultimo ingresa el Email del nuevo registro: ") #INGRESAR EMAIL
            try:
                server_socket.send(Email.encode())
            except Exception as e:
                print(f"Error recibiendo mensaje: '{e}'")
                break
           # print("Se han enviado los datos al servidor")
            print("Esperando 5 segundos para recibir el mensaje")
            time.sleep(5) #Creo que es necesario usar time para poder captar la informacion del servidor
            infoinsercion = InformacionRecibida[0]
            InformacionRecibida.pop(0)
            print(f"Se obtuvo este resultado: '{infoinsercion}'") #Se imprime la informacion con el formato dado por el servidor
          #  print("Ya termino la parte de recibir informacion")
            repetir = input("Desea realizar otra opcion?(S/N):") #REPETIR CICLO?
        else: #NO ELEGISTE NI CONSULTAS NI REGISTROS
            print("Error la opción que elegiste no es valida")
            print("Terminando el programa")
            repetir == 'N' #TERMINAR CICLO
        try: #Envia al servidor la opcion que haya elegido el usuario sobre si repetir todo el programa
            server_socket.send(repetir.encode())
        except Exception as e:
            print(f"Error recibiendo mensaje: '{e}'")
            break


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('127.0.0.1', 5000)) #Local
#client_socket.connect(('192.168.137.1', 5000)) #Direccion del profe

receive_thread = threading.Thread(target=receive_information)
receive_thread.start()

send_thread = threading.Thread(target=send_data)
send_thread.start()

