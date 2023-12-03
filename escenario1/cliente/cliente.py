import socket

import socket
HOST = '172.16.17.5'
PORT = 8080
print('─────────────────────────────────────────────────────────────────')
print('                           ESCENARIO 1                           ')
print('─────────────────────────────────────────────────────────────────')
print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
        print('────────────────────────────   CHAT   ───────────────────────────')
        print('              Para salir del chat escribe \'salir\'              ')
        print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n\n')
        
        while True:
            print("──────────────────────────")
            mensaje = input("| Tú: ")
            print("──────────────────────────")
                
            if mensaje.lower() == 'salir':
                client_socket.sendall(mensaje.encode())
                print("\nDesconectando....")
                break

            client_socket.sendall(mensaje.encode())
            # Recibir datos del servidor
            data = client_socket.recv(1024)
            print("\t\t\t\t────────────────────────────────")
            print(f"\t\t\t\t| Recibido: {data.decode()}")
            print("\t\t\t\t────────────────────────────────")
except socket.error as e:
    print(f"No se puede conectar a {HOST}")
