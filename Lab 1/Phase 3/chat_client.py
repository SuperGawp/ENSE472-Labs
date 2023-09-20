import socket

PORT = 8000
PC_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(PC_NAME)
TCP_ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Q"
HEADER_SIZE_IN_BYTES = 8

def send(sock, message):
    message_encoded = message.encode(FORMAT)
    message_length = len(message_encoded)
    message_send_length = str(message_length).encode(FORMAT)
    padding_needed = HEADER_SIZE_IN_BYTES - len(message_send_length)
    padding = b' ' * padding_needed
    padded_message_send_length = message_send_length + padding
    sock.send(padded_message_send_length)
    sock.send(message_encoded)

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(TCP_ADDR)

    try:
        # Prompt the user for a username
        username = input("Enter your username: ")
        client.send(username.encode(FORMAT))
        
        message = input(f"Enter a message or '{DISCONNECT_MESSAGE}' to disconnect: ")
        
        while message != DISCONNECT_MESSAGE:
            send(client, message)
            message = input()
    except KeyboardInterrupt:
        pass
    
    send(client, DISCONNECT_MESSAGE)
    client.close()
