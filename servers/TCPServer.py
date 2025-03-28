import socket
from config import get_config_value
from abc import ABC, abstractmethod


class TCPServer(ABC):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self._host, self._port))
        self.server_socket.listen(5)
        print(f"Servidor TCP escuchando en {self._host}:{self._port}")

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @abstractmethod
    def handle_client(self, client_socket, client_address):
        pass

    def start(self):
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                print(f"Conexión recibida de {client_address}")
                self.handle_client(client_socket, client_address)
                client_socket.close()
        except KeyboardInterrupt:
            print("\nServidor detenido manualmente.")
            self.server_socket.close()
