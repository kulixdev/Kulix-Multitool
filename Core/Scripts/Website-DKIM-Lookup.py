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

Title("DKIM Lookup")

try:
    import dns.resolver
except Exception as e:
    ErrorModule(e)

def DkimLookup(domain, selectors=None):
    if selectors is None:
        selectors = ['default', 'dkim', 'mail', 's1']
    
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} DKIM Records for {domain}:")

    for selector in selectors:
        try:
            dkim_record = f"{selector}._domainkey.{domain}"
            dns_records = dns.resolver.resolve(dkim_record, 'TXT')

            if dns_records:
                for i, record in enumerate(dns_records, start=1):
                    if i == len(dns_records):
                        print(f"└───{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} DKIM Record for {selector}: {record.to_text()}")
                    else:
                        print(f"├───{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} DKIM Record for {selector}: {record.to_text()}")
                return
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.NXDOMAIN:
            pass
        except Exception as e:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Error checking DKIM for {selector}: {e}")
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} No DKIM records found for {domain} using common selectors.")

Slow(scan_banner)
domain = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Domain Name -> {reset}")
Censored(domain)

DkimLookup(domain)
Continue()
Reset()
