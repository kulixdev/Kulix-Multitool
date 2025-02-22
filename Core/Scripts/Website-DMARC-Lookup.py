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

Title("DMARC Lookup")

try:
    import dns.resolver
except Exception as e:
    ErrorModule(e)

def DmarcLookup(domain):
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} DMARC Records for {domain}:")

    try:
        dmarc_record = f"_dmarc.{domain}"
        dns_records = dns.resolver.resolve(dmarc_record, 'TXT')

        if dns_records:
            for i, record in enumerate(dns_records, start=1):
                if i == len(dns_records):
                    print(f"└───{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} DMARC Record: {record.to_text()}")
                else:
                    print(f"├───{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} DMARC Record: {record.to_text()}")
        else:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} No DMARC records found for {domain}")
    except dns.resolver.NoAnswer:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} No DMARC records found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Domain {domain} does not exist")
    except Exception as e:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Error fetching DMARC records: {e}")

Slow(scan_banner)
domain = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Domain Name -> {reset}")
Censored(domain)

DmarcLookup(domain)
Continue()
Reset()
