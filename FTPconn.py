print("\033[91m" + "░▒▓██████████►╬◄██████████▓▒░")
print("\033[91m" + "░▒▓██►╔╦╦╦═╦╗╔═╦═╦══╦═╗◄██▓▒░")
print("\033[91m" + "░▒▓██►║║║║╩╣╚╣═╣║║║║║╩╣◄██▓▒░")
print("\033[91m" + "░▒▓██►╚══╩═╩═╩═╩═╩╩╩╩═╝◄██▓▒░")
print("\033[91m" + "░▒▓██████████►╬◄██████████▓▒░")

from ftplib import FTP
from colorama import init, Fore
import os

init(autoreset=True)

def main():
    try:
        print(Fore.YELLOW + "\n[*] FTP connection powered by \n>>> t.me/VikingTerminal\n")
        host = input(Fore.CYAN + "[*] Enter FTP host: ")
        username = input(Fore.CYAN + "[*] Enter username: ")
        password = input(Fore.CYAN + "[*] Enter password: ")
        
        try:
            ftp = FTP(host)
            ftp.login(username, password)
            print(Fore.GREEN + "[*] Connected to", host)
        except Exception as e:
            print(Fore.RED + "[*] Unable to connect to FTP server:", e)
            return
        
        try:
            files = ftp.nlst()
            print(Fore.YELLOW + "[*] Files present on the host:")
            for i, file in enumerate(files):
                print(Fore.CYAN + "[{}] {}".format(i + 1, file))
            
            option = input(Fore.MAGENTA + "[*] Do you want to rename, delete, create a file, or download all files? (r/d/c/n): ").lower()
            if option == 'r':
                try:
                    file_index = int(input(Fore.CYAN + "[*] Enter the number of the file to rename: ")) - 1
                    if file_index < 0 or file_index >= len(files):
                        raise ValueError("Invalid file index")
                    
                    new_name = input(Fore.CYAN + "[*] Enter the new name for the file: ")
                    old_name = files[file_index]
                    ftp.rename(old_name, new_name)
                    print(Fore.GREEN + "[*] File renamed successfully!")
                except ValueError as ve:
                    print(Fore.RED + "[*] Error: {}".format(ve))
                except Exception as e:
                    print(Fore.RED + "[*] Error renaming the file:", e)
            elif option == 'd':
                try:
                    local_directory = input(Fore.CYAN + "[*] Enter the local directory to save files: ")
                    os.makedirs(local_directory, exist_ok=True)
                    for file in files:
                        local_file_path = os.path.join(local_directory, file)
                        with open(local_file_path, 'wb') as f:
                            ftp.retrbinary('RETR {}'.format(file), f.write)
                        print(Fore.GREEN + "[*] File '{}' downloaded successfully!".format(file))
                except Exception as e:
                    print(Fore.RED + "[*] Error downloading files:", e)
            elif option == 'c':
                try:
                    file_name = input(Fore.CYAN + "[*] Enter the name of the file to create: ")
                    with open(file_name, 'w') as f:
                        # You can add content to the file if needed
                        pass
                    print(Fore.GREEN + "[*] File '{}' created successfully!".format(file_name))
                except Exception as e:
                    print(Fore.RED + "[*] Error creating the file:", e)
            else:
                print(Fore.YELLOW + "[*] Operation cancelled.")
                
        except Exception as e:
            print(Fore.RED + "[*] Error listing files:", e)
        
        try:
            ftp.quit()
            print(Fore.GREEN + "[*] FTP connection closed successfully.")
        except Exception as e:
            print(Fore.RED + "[*] Error closing FTP connection:", e)

    except KeyboardInterrupt:
        print(Fore.YELLOW + "[*] Operation interrupted.")

if __name__ == "__main__":
    main()
