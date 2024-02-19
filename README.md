# MalIPFinder
Have a bulk of IP'S and you need Check if the multiple ip's are malicious

## Description:

This Python script checks a list of IP addresses against the AbuseIPDB API to determine whether they are associated with malicious activity. It fetches information such as abuse confidence score, country, usage type, and ISP for each IP address and provides the results in an output file. Additionally, it filters out non-malicious IP addresses and saves them to a separate file.

### Features:
- Utilizes the AbuseIPDB API to check IP addresses for malicious activity.
- Provides detailed information about each IP address, including abuse confidence score, country, usage type, and ISP.
- Filters non-malicious IP addresses and saves them to a separate file.
- Displays a progress bar to track the status of IP address checks.
- Includes an ASCII art banner for a visually appealing display.
- Offers a cute footnote "Thanks for using the tool. Made with <3 in India" as a finishing touch.

### Usage:
1. Create a text file named `ip_addresses.txt` containing a list of IP addresses, with each IP address on a separate line.
2. Run the script and provide the name for the output file when prompted.
3. Check the generated output file for the results of IP address checks.
