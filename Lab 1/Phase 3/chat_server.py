import socket
import threading

PORT = 8000
PC_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(PC_NAME)
TCP_ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Q"
HEADER_SIZE_IN_BYTES = 8

clients = []
client_usernames = {}

def send(client_socket, message):
    message_encoded = message.encode(FORMAT)
    message_length = len(message_encoded)
    message_send_length = str(message_length).encode(FORMAT)
    padding_needed = HEADER_SIZE_IN_BYTES - len(message_send_length)
    padding = b' ' * padding_needed
    padded_message_send_length = message_send_length + padding
    client_socket.send(padded_message_send_length)
    client_socket.send(message_encoded)

def broadcast_message(sender_sock, message):
    sender_username = client_usernames[sender_sock]
    for client_sock, _, _ in clients:
        if client_sock != sender_sock:
            try:
                send(client_sock, f"[{sender_username}] {message}")
            except:
                pass

def handle_client(conn, addr, server_active):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    # Send the username prompt message to the client
    #send(conn, "Enter your username: ")

    username = conn.recv(1024).decode(FORMAT)
    client_usernames[conn] = username

    # Notify that the username is entered
    print(f"[NAME ENTERED] {addr} is now {username}")

    clients.append((conn, addr, username))

    broadcast_message(conn, f"has entered the chat.")

    while server_active.is_set() and connected:
        try:
            message_length_encoded = conn.recv(HEADER_SIZE_IN_BYTES)
            message_length_string = message_length_encoded.decode(FORMAT)
            if message_length_string:
                message_length_int = int(message_length_string)
                message_encoded = conn.recv(message_length_int)
                message = message_encoded.decode(FORMAT)
                if message != DISCONNECT_MESSAGE:
                    print(f"[{username}] {message}")
                    broadcast_message(conn, message)
                else:
                    connected = False
        except socket.timeout:
            continue

    broadcast_message(conn, f"has left the chat.")
    del client_usernames[conn]
    clients.remove((conn, addr, username))

    print(f"[CLOSED CONNECTION] {username} left.")
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 2}")
    conn.close()

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(TCP_ADDR)
    print("[STARTING] Server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    threads = []
    server_active = threading.Event()
    server_active.set()
    try:
        while True:
            try:
                conn, addr = server.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr, server_active))
                thread.start()
                threads.append(thread)
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
            except socket.timeout:
                continue
    except KeyboardInterrupt:
        print("[SHUTTING DOWN] Attempting to close threads.")
        server_active.clear()
        for thread in threads:
            thread.join()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    server.close()
