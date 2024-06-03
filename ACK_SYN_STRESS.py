import socket
import time

def send_syn_ack(destination, port, syn_ack_count, syn_ack_speed):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(2)
        sock.connect((destination, port))
        for i in range(syn_ack_count):
            if (i + 1) % 50 == 0:  
                print("\033[1;34mSYN/ACK sent successfully\033[0m")
            else:
                print("\033[1;32mSYN/ACK => sent successfully\033[0m")
            time.sleep(syn_ack_speed)
    except Exception as e:
        print("\033[1;31mSYN/ACK sending failed: {}\033[0m".format(e))
    finally:
        sock.close()

print("\033[1;32m⣿⣿⢿⣿⢿⣿⢿⣿⢿⣿⢿⣿⢿⣿⢿⣿⢿⣿⠟⣿⣿⢿⣿⢿⣿⢿⣿⢿⣿⢿\033[0m")
print("\033[1;32m⣿⣯⣿⢯⣿⣯⣿⢯⣿⣯⣿⠫⡿⣯⣿⣯⣟⠁⠀⢿⣿⣻⣯⣿⢯⣿⣯⣿⢯⣿\033[0m")
print("\033[1;32m⣿⣟⣾⡿⣟⣾⣿⣻⣿⠾⠃⢀⠀⡀⠿⠯⠏⠀⠌⣼⣿⢿⣽⣾⡿⣟⣾⣿⣻⣿\033[0m")
print("\033[1;32m⣿⡿⣽⣿⡛⠛⠚⣿⣟⣷⠄⠂⢰⣤⠀⠄⠠⢈⠠⢹⣿⢿⣻⣾⢿⣟⣿⡾⣿⣽\033[0m")
print("\033[1;32m⣿⣿⣻⣷⣿⣄⡂⠈⠉⡀⠠⢈⠘⠟⠀⠠⠁⡄⠂⡁⡸⠻⣿⣽⡿⣯⣿⣽⡿⣽\033[0m")
print("\033[1;32m⣿⣷⢿⣳⣿⢿⣷⣧⠐⠀⡁⢀⠂⠈⡄⠑⠡⢀⠂⡐⠀⠀⠈⠳⣿⢿⣽⣾⢿⣿\033[0m")
print("\033[1;32m⣿⣯⣿⢿⣽⡿⣯⡿⠀⠒⠰⠀⡈⠌⠐⢈⠠⠀⠄⠀⠀⠀⠀⠀⣿⣿⣻⣾⢿⣻\033[0m")
print("\033[1;32m⣿⣟⣾⡿⣯⣿⣟⣇⠠⠈⡴⡇⠀⡐⠈⡀⠀⠉⣤⣶⣤⠀⠀⠀⣾⣿⣽⢿⣻⣿\033[0m")
print("\033[1;32m⣿⡿⣽⣿⣻⣷⠟⠛⠀⠄⢟⡇⠠⣸⠀⣠⠀⢸⣿⣭⣿⡗⠀⠸⢿⣳⣿⢿⣻⣽\033[0m")
print("\033[1;32m⣿⣿⣻⣷⢿⣻⣦⣤⢈⡄⠀⡁⠐⣀⠵⠟⠧⠀⠙⠛⠉⠀⢀⣀⣼⡿⣯⣿⣟⣿\033[0m")
print("\033[1;32m⣿⣷⢿⣯⣿⣟⣿⢿⡿⣇⠐⣦⡅⠀⢠⠀⠀⡀⢠⣶⠇⢰⣿⡿⣯⣿⣟⣷⣿⣻\033[0m")
print("\033[1;32m⣿⣯⣿⣟⣾⡿⣽⣿⣻⣿⡀⢻⣿⣤⣇⣼⣔⣷⣾⡟⠀⣿⡿⣽⣿⣳⣿⣻⣾⢿\033[0m")
print("\033[1;32m⣿⣟⣾⡿⣽⣿⣻⣷⢿⣻⡃⢈⡋⠿⠹⠛⡟⢻⠉⠁⠀⣿⢿⣟⣷⡿⣯⣿⣽⣿\033[0m")
print("\033[1;32m⣿⡿⣽⣿⣻⣷⢿⣯⣿⢿⣷⣤⡈⠉⠂⠋⠓⠩⢁⣴⣾⢿⣟⣯⣿⣟⣿⡷⣿⣾\033[0m")
print("\033[1;32m⣿⣿⣻⣷⢿⣯⣿⣟⣾⡿⣯⣿⢿⣦⣥⣦⣴⣷⡿⣿⣽⣿⣻⣯⣷⡿⣯⣿⢿⣽\033[0m")

if __name__ == "__main__":
    print("\033[1;31mDEVASTER DDoS SYN/ACK BRUTE\nby t.me/VikingTERMINAL\033[0m")
    destination = input("\033[1;35mEnter the IP address or domain to perform the test: \033[0m")
    port = int(input("\033[1;35mEnter the port number: \033[0m"))
    syn_ack_count = int(input("\033[1;35mEnter the number of packets: \033[0m"))
    syn_ack_speed = float(input("\033[1;35mEnter the sending speed (in milliseconds): \033[0m"))
    send_syn_ack(destination, port, syn_ack_count, syn_ack_speed)