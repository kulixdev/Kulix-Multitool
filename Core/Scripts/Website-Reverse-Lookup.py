# Copyright (c) Kulix  
# See the file 'LICENSE' for copying permission  
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|   
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code  
#     - In the case you wish to analyze this code under any circumstance; note that touching this code should not be altered under any circumstance  
#            - If this code is altered, the owner holds no obligation for damages or errors caused by the altered code  
#     - Do not resell this tool, do not credit it to yours  

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Core.Config.Info import *
from Core.Config.Utilities import *

Title("Reverse Lookup")

try:
    import dns.resolver
    import socket
except Exception as e:
    ErrorModule(e)

def ReverseDnsLookup(ip_address):
    try:
        reversed_ip = '.'.join(reversed(ip_address.split('.'))) + '.in-addr.arpa'
        dns_records = dns.resolver.resolve(reversed_ip, 'PTR')
        
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Reverse DNS Records for {ip_address}:")
        
        if dns_records:
            for i, record in enumerate(dns_records, start=1):
                if i == len(dns_records):
                    print(f"└───{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Record {i}: {record.to_text()}")
                else:
                    print(f"├───{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Record {i}: {record.to_text()}")
        else:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} No PTR records found for {ip_address}")
    except dns.resolver.NoAnswer:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} No PTR records found for {ip_address}")
    except dns.resolver.NXDOMAIN:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} IP address {ip_address} does not have a reverse DNS record")
    except Exception as e:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Error fetching reverse DNS records: {e}")

Slow(scan_banner)
ip_address = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} IP Address -> {reset}")
Censored(ip_address)

ReverseDnsLookup(ip_address)
Continue()
Reset()
