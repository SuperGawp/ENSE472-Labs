import socket
import threading

PORT = 8000
PC_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(PC_NAME)
TCP_ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Q"
HEADER_SIZE_IN_BYTES = 8

# one instance of this will run for each client in a thread
def handle_client(conn, addr, server_active):
    print (f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while server_active.is_set() and connected:
        try:
            message_length_encoded = conn.recv(HEADER_SIZE_IN_BYTES)
            message_length_string = message_length_encoded.decode(FORMAT)
            if message_length_string:
                message_length_int = int(message_length_string)
                message_encoded = conn.recv(message_length_int)
                message = message_encoded.decode(FORMAT)
                if message != DISCONNECT_MESSAGE:
                    print (f"[{addr}] {message}")
                else:
                    connected = False
        except socket.timeout:
            continue
    print (f"[END CONNECTION] {addr} disconnected.")
    print (f"[ACTIVE CONNECTIONS] {threading.activeCount() - 2}")
    conn.close()

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(TCP_ADDR)
    print ("[STARTING] Server is starting...")
    server.listen()
    print (f"[LISTENING] Server is listening on {SERVER_IP}")
    threads = []
    server_active = threading.Event()
    server_active.set()
    try:
        while True:
            # this is a blocking command, it will wait for a new connection to the server
            conn, addr = server.accept()
            conn.settimeout(1)
            thread = threading.Thread(target=handle_client, args=(conn, addr, server_active))
            thread.start()
            threads.append(thread)
            print (f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


    except KeyboardInterrupt:
        print ("[SHUTTING DOWN] Attempting to close threads.")
        server_active.clear()
        for thread in threads:
            thread.join()
        print (f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    server.close()
