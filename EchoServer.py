from servers.TCPServer import TCPServer
from config import get_config_value
import argparse


class EchoServer(TCPServer):
    def handle_client(self, client_socket, client_address):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"Mensaje recibido: {message}")
            if message == "DESCONEXION":
                print(f"Cliente {client_address} solicitó desconexión.")
                break  # Terminar la conexión si recibe el mensaje "DESCONEXION"
            client_socket.sendall(data)  # Enviar eco del mensaje recibido

            # Responder al cliente con el mensaje recibido o cualquier otra respuesta
            response = f"\nServidor ha recibido: {message}".upper()
            client_socket.sendall(response.encode('utf-8'))  # Enviar respuesta

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor TCP configurable.")
    parser.add_argument("--host", type=str, default=get_config_value('SERVER', 'HOST', '127.0.0.1'),
                        help="Dirección IP del servidor")
    parser.add_argument("--port", type=int, default=int(get_config_value('SERVER', 'PORT', '5000')),
                        help="Puerto del servidor")
    args = parser.parse_args()

    server = EchoServer(args.host, args.port)
    server.start()
