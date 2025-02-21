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

try:
    import ssl
    import socket
    import time
except Exception as e:
    ErrorModule(e)

Title("SSL/TLS Checker")

def get_ssl_certificate(hostname, port=443):
    context = ssl.create_default_context()
    
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            return ssock.getpeercert()

def ssl_checker(domain):
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Checking SSL/TLS for {domain}... ", end="")
    start_time = time.time()
    time.sleep(1)

    try:
        cert = get_ssl_certificate(domain)
        elapsed_time = time.time() - start_time

        issuer = dict(x[0] for x in cert['issuer'])
        subject = dict(x[0] for x in cert['subject'])
        expiry = cert['notAfter']

        print(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {GEN_VALID} SSL/TLS Certificate Details: {green}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Domain: {white}{domain}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Issuer: {white}{issuer.get('organizationName', 'Unknown')}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Subject: {white}{subject.get('commonName', 'Unknown')}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Expiration Date: {white}{expiry}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Test Duration: {white}{elapsed_time:.2f}s{cyan}")

    except Exception as e:
        print(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ERROR} SSL check failed: {red}{e}{reset}")

try:
    domain = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Enter Domain Name -> {reset}")
    Censored(domain)
    ssl_checker(domain)
    Continue()
    Reset()

except Exception as e:
    ErrorModule(e)
