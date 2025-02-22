# Copyright (c) Kulix  
# See the file 'LICENSE' for your permissions while using this content 
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|   
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code  
#     - In the case you wish to analyze this code under any circumstance; note that touching this code should not be altered under any circumstance  
#            - If this code is altered, the owner holds no obligation for damages or errors caused by the altered code  
#     - Do not resell this tool, do not credit it as your own

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Core.Config.Info import *
from Core.Config.Utilities import *

Title("DNS Lookup")

try:
    import dns.resolver
    import socket
except Exception as e:
    ErrorModule(e)

def DnsLookup(domain, record_type='A'):
    try:
        dns_records = dns.resolver.resolve(domain, record_type)
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} DNS Records for {domain} ({record_type}):")
        
        if dns_records:
            for i, record in enumerate(dns_records, start=1):
                if i == len(dns_records):
                    print(f"└───{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Record {i}: {record.to_text()}")
                else:
                    print(f"├───{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Record {i}: {record.to_text()}")
        else:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} No {record_type} records found for {domain}")
    except dns.resolver.NoAnswer:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} No {record_type} records found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Domain {domain} does not exist")
    except Exception as e:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Error fetching {record_type} records: {e}")

Slow(scan_banner)
domain = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Domain Name -> {reset}")
Censored(domain)

record_type = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Record Type (A, AAAA, CNAME, MX, NS, PTR, SOA, TXT, SRV, CAA, DNSKEY, NSEC, DS, LOC, SPF, NAPTR) -> {reset}")

DnsLookup(domain, record_type)
Continue()
Reset()
