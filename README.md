# Servidor y Cliente TCP en Python

Este repositorio contiene un servidor y un cliente TCP simples implementados en Python. El servidor recibe mensajes de los clientes y responde con un mensaje de confirmación, o cierra la conexión si recibe el mensaje `"DESCONEXION"`.

## Requisitos

- Python 3.6 o superior
- No se requieren librerías externas, solo la librería estándar de Python.

## Instalación de librerías

Este proyecto no requiere ninguna librería adicional, ya que utiliza solo librerías estándar de Python. Si deseas asegurarte de tener Python 3 instalado, puedes hacerlo con los siguientes pasos:

### 1. Verificar versión de Python
Verifica que tengas instalada una versión compatible de Python ejecutando el siguiente comando:
    
    ```bash
    python3 --version
    ```

### **Instrucciones de ejecución**:
1. **Servidor**:
    - Ejecutar el servidor en una terminal:
      ```bash
      python3 ECHOServer.py
      ```

2. **Cliente**:
    - Ejecutar el cliente en otra terminal:
      ```bash
      python3 TCPClient.py
      ```

Este archivo `README.md` debería ser suficiente para que otros puedan entender cómo ejecutar y probar el servidor y el cliente en su entorno. Si necesitas alguna modificación, ¡déjame saber!


