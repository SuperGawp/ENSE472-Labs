import socket
import threading 

PORT = 8000
PC_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(PC_NAME)
TCP_ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Q"
HEADER_SIZE_IN_BYTES = 8

def send (sock, message):
    message_encoded = message.encode(FORMAT)
    message_length = len(message_encoded)
    message_send_length = str(message_length).encode(FORMAT)
    padding_needed = HEADER_SIZE_IN_BYTES - len(message_send_length)
    # this repeats the space byte by padding needed times
    padding = b' ' * padding_needed
    padded_message_send_length = message_send_length + padding
    sock.send(padded_message_send_length)
    sock.send(message_encoded)
    
def receive_messages(sock):
    while True:
        try:
            message_length_encoded = sock.recv(HEADER_SIZE_IN_BYTES)
            message_length_string = message_length_encoded.decode(FORMAT)
            if message_length_string:
                message_length_int = int(message_length_string)
                message_encoded = sock.recv(message_length_int)
                message = message_encoded.decode(FORMAT)
                print(f"[{TCP_ADDR}] {message}")
        except socket.timeout:
            continue

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(TCP_ADDR)

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    try:
        message = input(f"Enter a message, or enter '{DISCONNECT_MESSAGE}' to disconnect: ")
        while message != DISCONNECT_MESSAGE:
            send(client, message)
            message = input()
    except KeyboardInterrupt:
        pass

    send(client, DISCONNECT_MESSAGE)
    client.close()
    receive_thread.join()
