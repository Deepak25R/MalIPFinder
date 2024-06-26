import os
import requests
from tqdm import tqdm
import time

# ASCII art banner
banner = """
   ▄▄▄▄███▄▄▄▄      ▄████████  ▄█             ▄█     ▄███████▄         ▄████████  ▄█  ███▄▄▄▄   ████████▄     ▄████████    ▄████████ 
 ▄██▀▀▀███▀▀▀██▄   ███    ███ ███            ███    ███    ███        ███    ███ ███  ███▀▀▀██▄ ███   ▀███   ███    ███   ███    ███ 
 ███   ███   ███   ███    ███ ███            ███▌   ███    ███        ███    █▀  ███▌ ███   ███ ███    ███   ███    █▀    ███    ███ 
 ███   ███   ███   ███    ███ ███            ███▌   ███    ███       ▄███▄▄▄     ███▌ ███   ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
 ███   ███   ███ ▀███████████ ███            ███▌ ▀█████████▀       ▀▀███▀▀▀     ███▌ ███   ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
 ███   ███   ███   ███    ███ ███            ███    ███               ███        ███  ███   ███ ███    ███   ███    █▄  ▀███████████ 
 ███   ███   ███   ███    ███ ███▌    ▄      ███    ███               ███        ███  ███   ███ ███   ▄███   ███    ███   ███    ███ 
  ▀█   ███   █▀    ███    █▀  █████▄▄██      █▀    ▄████▀             ███        █▀    ▀█   █▀  ████████▀    ██████████   ███    ███ 
                              ▀                                                                                           ███    ███ 
"""

print(banner)

def check_ip_malicious(ip_address, api_key):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}'
    headers = {'Key': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        abuse_confidence_score = data['data']['abuseConfidenceScore']
        if abuse_confidence_score > 20:
            result = f"The IP address {ip_address} is malicious.\n"
            result += "Abuse confidence score: " + str(abuse_confidence_score) + "\n"
            result += "Country: " + str(data['data']['countryCode']) + "\n"
            result += "Usage Type: " + str(data['data']['usageType']) + "\n"
            result += "ISP: " + str(data['data']['isp']) + "\n"
            return result  # Return the result only if the IP is malicious
        else:
            return None  # Return None if the IP is not malicious
    else:
        return f"Error occurred while checking IP status: {response.text}\n"

# Enter your AbuseIPDB API key here
API_KEY = 'd8de94dcaa9e8be45f54d2f1d56fc1c6c0d9ad574457c902fd64825365c9dc2e32c298b83d864d88'

# Read IP addresses from file
with open('ip_addresses.txt', 'r') as file:
    ip_addresses = file.readlines()

# Remove whitespace characters like `\n` at the end of each line
ip_addresses = [ip.strip() for ip in ip_addresses]

# Get the number of IP addresses
num_ips = len(ip_addresses)

# Ask user for output file name
output_file_name = input("Enter the name for the output file (with extension): ")

# Initialize tqdm progress bar
with tqdm(total=num_ips, desc="Checking IPs") as pbar:
    # Check each IP address for malicious activity and store the output
    with open(output_file_name, 'w') as output_file:
        for ip in ip_addresses:
            result = check_ip_malicious(ip, API_KEY)
            if result:  # Check if result is not None (i.e., if IP is malicious)
                output_file.write(result)
                output_file.write("-" * 50 + "\n")  # Add separation line
            pbar.update(1)
            time.sleep(0.1)  # Simulate processing time

# Print location of the file
print("Output has been saved to:", os.path.abspath(output_file_name))
print("Thanks for using the tool. Made with <3 in India")
