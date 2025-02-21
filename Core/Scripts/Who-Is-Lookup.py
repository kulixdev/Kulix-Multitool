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
    import whois
    import time
except Exception as e:
    ErrorModule(e)

Title("Whois Lookup")

def WhoIs(domain):
    try:
        w = whois.whois(domain)
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {GEN_VALID} Whois Lookup Results: {green}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Domain Name: {white}{w.domain_name}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Registrar: {white}{w.registrar}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Creation Date: {white}{w.creation_date}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Expiration Date: {white}{w.expiration_date}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Name Servers: {white}{w.name_servers}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Country: {white}{w.country}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Email: {white}{w.emails}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Whois Server: {white}{w.whois_server}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Updated Date: {white}{w.updated_date}{cyan}")
    except Exception as e:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ERROR} Error: {str(e)}")

try:
    domain = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Enter Domain Name -> {reset}")
    Censored(domain)
    WhoIs(domain)
    Continue()
    Reset()

except Exception as e:
    ErrorModule(e)
