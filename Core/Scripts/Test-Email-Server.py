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

Title("Email Server Test")

try:
    import smtplib
    import socket
    import time
except Exception as e:
    ErrorModule(e)

def SmtpTest(domain):
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Testing SMTP server for domain: {domain}")

    smtp_ports = [25, 465, 587]
    server_found = False

    for port in smtp_ports:
        try:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Trying to connect to {domain} on port {port}...")
            
            start_time = time.time()
            
            server = smtplib.SMTP(domain, port, timeout=15)
            server.set_debuglevel(0)

            server.ehlo()

            if port in [25, 587]:
                if server.has_extn('STARTTLS'):
                    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Server supports STARTTLS.")
                else:
                    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Warning - Does not support TLS.")
            
            transaction_time = time.time() - start_time
            if transaction_time > 15:
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Warning - SMTP Transaction Time: {transaction_time:.2f} seconds - Not good!")

            server.quit()
            server_found = True
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} SMTP server for {domain} is responding on port {port}.")
            break

        except socket.timeout:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Timeout waiting for response after 15 seconds.")
        except smtplib.SMTPConnectError:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Failed to connect to {domain} on port {port}.")
        except smtplib.SMTPException as e:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} SMTP error: {e}")
        except Exception as e:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Error testing SMTP server: {e}")
    
    if not server_found:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ERROR} No responsive SMTP server found for {domain} on common ports.")
    else:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} SMTP test for {domain} completed.")
    
    try:
        ip = socket.gethostbyname(domain)
        reverse_dns = socket.gethostbyaddr(ip)[0]
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Reverse DNS for {domain}: {reverse_dns}")
        if reverse_dns != domain:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Warning - Reverse DNS does not match SMTP Banner.")
    except socket.herror:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} No reverse DNS record found for {domain}")

Slow(scan_banner)
domain = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Domain Name -> {reset}")
Censored(domain)

SmtpTest(domain)
Continue()
Reset()
