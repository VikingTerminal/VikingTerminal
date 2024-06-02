import socket
import ipaddress
import time
import sys
import requests
from concurrent.futures import ThreadPoolExecutor
import random

def print_ascii_art():
    ascii_art = """
    __        
\  / | |__/ | |\ | / _`       
 \/  | |  \ | | \| \__>
    """

    colors = [32, 31, 34]
    for char in ascii_art:
        print(f"\033[{random.choice(colors)}m{char}\033[0m", end='', flush=True)

def print_color_text(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m", end='', flush=True)
    time.sleep(0.05)

def typewriter_effect(text, color_code):
    for char in text:
        print_color_text(char, color_code)
    print()

def input_color_text(prompt, color_code):
    user_input = input(f"\033[{color_code}m{prompt}\033[0m")
    return user_input

def save_to_txt(ip_info, open_ports, admin_directories):
    with open("scan_results.txt", "w") as file:
        file.write("Hostname: {}\n".format(ip_info["hostname"]))
        file.write("IP Addresses:\n")
        for ip in ip_info["ip_addresses"]:
            file.write("  {}\n".format(ip))
        file.write("\nPort Scan Results:\n")
        for port in open_ports:
            file.write("  Port {}: Open\n".format(port))
        file.write("\nAdmin Directories Found:\n")
        for directory in admin_directories:
            file.write("  {}\n".format(directory))

def get_ip_info(hostname):
    try:
        ip_info = {"hostname": hostname, "ip_addresses": []}
        ip_addresses = socket.gethostbyname_ex(hostname)[2]

        for ip_address in ip_addresses:
            addr_info = socket.getaddrinfo(ip_address, None)
            family = addr_info[0][0]
            ip = ipaddress.ip_address(ip_address)
            network = ipaddress.ip_network(ip, strict=False)

            typewriter_effect(f"IP Address: {ip}", 33)
            typewriter_effect(f"Address Family: {family}", 32)
            typewriter_effect(f"Network: {network}", 36)
            print("-" * 30)

            ip_info["ip_addresses"].append(str(ip))

        return ip_info

    except (socket.gaierror, ValueError):
        typewriter_effect(f"Unable to get information for the hostname {hostname}", 31)
        return None

def scan_port(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print_color_text(f"Port {port} open\n", 32)
        sock.close()
    except (socket.error, socket.timeout):
        pass

def scan_ports(ip_address):
    try:
        print_color_text("Scanning open ports:\n", 32)

        open_ports = []
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(scan_port, ip_address, port) for port in range(1, 1025)]

        for future in futures:
            future.result()
            open_ports.append(future)

        return open_ports

    except Exception as e:
        print_color_text(f"Error scanning ports: {e}", 31)
        return []

def search_admin_directories(ip_address):
    try:
        print_color_text("\nSearching for admin directories...", 36)

        common_directories = ["admin", "login", "dashboard"]
        found_directories = []

        for directory in common_directories:
            url = f"http://{ip_address}/{directory}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    found_directories.append(url)
            except requests.RequestException as e:
                print_color_text(f"Error requesting {url}: {e}", 31)

        if found_directories:
            print_color_text("\nDirectories found\n", 31)
            for dir_url in found_directories:
                print_color_text(f"{dir_url}\n", 32)
        else:
            print_color_text("\nNo admin directories found", 33)

        return found_directories

    except Exception as e:
        print_color_text(f"Error searching admin directories: {e}", 31)
        return []

print_color_text("\nEnter the hostname to analyze (type 'exit' to quit): ", 36)  
while True:
    try:
        hostname_input = input()
        if hostname_input.lower() == 'exit':
            typewriter_effect("\nThanks for trying out this tool! Visit t.me/VikingTerminal to try out more utilities.", 36)
            time.sleep(1)
            break

        ip_info = get_ip_info(hostname_input)

        if ip_info is not None:
            open_ports = scan_ports(hostname_input)
            found_directories = search_admin_directories(hostname_input)

            save_result = input_color_text("\n\nDo you want to save the results to a txt file? (yes/no): ", 33)
            if save_result.lower() == 'yes':
                save_to_txt(ip_info, open_ports, found_directories)
                print_color_text("Results saved in the file scan_results.txt", 36)
            elif save_result.lower() == 'no':
                print_color_text("Results not saved.\n", 31) 
            else:
                print_color_text("Invalid input. You should type 'yes' or 'no'. File not saved\n", 31)

            print_color_text("\nEnter the hostname to analyze (type 'exit' to quit): ", 32)
        else:
            print_color_text("The specified domain does not exist. Please try with an existing domain: ", 31)

    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
        break