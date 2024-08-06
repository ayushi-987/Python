import re
from collections import Counter
import csv

logfile="access_log"

logreg=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' 

with open(logfile) as f:
    log = f.read()
    ip_list = re.findall(logreg,log)
    with open("ipcount.csv","w") as f:
        fwriter = csv.writer(f)
        fwriter.writerow(["IP_Address","Count"])
        for k,v in Counter(ip_list).items():
            fwriter.writerow([k,v])
