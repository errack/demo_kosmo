import socket


class TCPClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self._host, self._port))
            print(f"Conectado al servidor {self._host}:{self._port}")
        except Exception as e:
            print(f"Error al conectar: {e}")

    def send_message(self, message):
        try:
            self.client_socket.sendall(message.encode('utf-8'))
            print(f"Mensaje enviado: {message}")
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")

    def receive_message(self):
        try:
            response = self.client_socket.recv(1024)
            print(f"Respuesta recibida: {response.decode('utf-8')}")
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")

    def close(self):
        self.client_socket.close()
        print("Conexión cerrada.")


if __name__ == "__main__":
    client = TCPClient("127.0.0.1", 5000)
    client.connect()

    while True:
        # Leer mensaje desde la consola
        message = input("Escribe un mensaje para enviar al servidor (o 'DESCONEXION' para salir): ")

        if message.lower() == "desconexion":
            print("Enviando mensaje de desconexión...")
            client.send_message(message)
            break

        client.send_message(message)
        client.receive_message()

    client.close()
