import socket

HOST = '172.16.17.5'
PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print('─────────────────────────────────────────────────────────────────')
print('                           ESCENARIO 1                           ')
print('─────────────────────────────────────────────────────────────────')
print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
print(f"Servidor escuchando en {HOST}:{PORT}")
print("Esperando conexion...\n")

while True:
    conn, addr = server_socket.accept()
    with conn:
        print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
        print(f"Conexión establecida desde {addr}")
        print('────────────────────────────   CHAT   ───────────────────────────')
        print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n\n')
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if data.decode() == 'salir':
                print("Se ha perdido la conexión.")
                break
            else:
                print("\t\t\t\t────────────────────────────────")
                print(f"\t\t\t\t| Recibido: {data.decode()}")
                print("\t\t\t\t────────────────────────────────")
            print("──────────────────────────")
            mensaje_servidor = input("|Tú: ")
            print("──────────────────────────")
            conn.sendall(mensaje_servidor.encode())
        conn.close()
        break
