import re
from collections import Counter
import csv

logfile = "access_log"  # Path to the log file

# Regular expression pattern to match IPv4 addresses
logreg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# Open the log file for reading
with open(logfile) as f:
    log = f.read()  # Read the entire content of the log file
    
    # Find all IP addresses in the log content
    ip_list = re.findall(logreg, log)
    
    # Open a CSV file to write the IP counts
    with open("ipcount.csv", "w") as f:
        fwriter = csv.writer(f)
        fwriter.writerow(["IP_Address", "Count"])  # Write the header row
        
        # Count occurrences of each IP address
        for k, v in Counter(ip_list).items():
            fwriter.writerow([k, v])  # Write each IP address and its count
