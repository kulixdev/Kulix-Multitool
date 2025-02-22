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

try:
   import dns.resolver
   import requests
   import re
except Exception as e:
   ErrorModule(e)

Title("Email Lookup")

try:
    def get_email_info(email):
        info = {}
        try: domain_all = email.split('@')[-1]
        except: domain_all = None

        try: name = email.split('@')[0]
        except: name = None

        try: domain = re.search(r"@([^@.]+)\.", email).group(1)
        except: domain = None
        try: tld = f".{email.split('.')[-1]}"
        except: tld = None

        try: 
            mx_records = dns.resolver.resolve(domain_all, 'MX')
            mx_servers = [str(record.exchange) for record in mx_records]
            info["mx_servers"] = mx_servers
        except dns.resolver.NoAnswer:
            info["mx_servers"] = None
        except dns.resolver.NXDOMAIN:
            info["mx_servers"] = None


        try:
            spf_records = dns.resolver.resolve(domain_all, 'SPF')
            info["spf_records"] = [str(record) for record in spf_records]
        except dns.resolver.NoAnswer:
            info["spf_records"] = None
        except dns.resolver.NXDOMAIN:
            info["spf_records"] = None

        try:
            dmarc_records = dns.resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
            info["dmarc_records"] = [str(record) for record in dmarc_records]
        except dns.resolver.NoAnswer:
            info["dmarc_records"] = None
        except dns.resolver.NXDOMAIN:
            info["dmarc_records"] = None

        if mx_servers:
            for server in mx_servers:
                if "google.com" in server:
                    info["google_workspace"] = True
                elif "outlook.com" in server:
                    info["microsoft_365"] = True

        return info, domain_all, domain, tld, name

    email = input(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Email -> {reset}")
    Censored(email)
        
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Information Recovery..{reset}")
    info, domain_all, domain, tld, name = get_email_info(email)

    try:
        mx_servers = info["mx_servers"]
        mx_servers = ' / '.join(mx_servers)
    except Exception as e:
        mx_servers = None

    try:
        spf_records = info["spf_records"]
    except:
        spf_records = None

    try:
        dmarc_records = info["dmarc_records"]
        dmarc_records = ' / '.join(dmarc_records)
    except:
        dmarc_records = None

    try:
        google_workspace = info["google_workspace"]
    except:
        google_workspace = None

    try:
        mailgun_validation = info["mailgun_validation"]
        mailgun_validation = ' / '.join(mailgun_validation)
    except:
        mailgun_validation = None

    print(f"""
    {INFO_ADD} Email      : {white}{email}{cyan}
    {INFO_ADD} Name       : {white}{name}{cyan}
    {INFO_ADD} Domain     : {white}{domain}{cyan}
    {INFO_ADD} Tld        : {white}{tld}{cyan}
    {INFO_ADD} Domain All : {white}{domain_all}{cyan}
    {INFO_ADD} Servers    : {white}{mx_servers}{cyan}
    {INFO_ADD} Spf        : {white}{spf_records}{cyan}
    {INFO_ADD} Dmarc      : {white}{dmarc_records}{cyan}
    {INFO_ADD} Workspace  : {white}{google_workspace}{cyan}
    {INFO_ADD} Mailgun    : {white}{mailgun_validation}{cyan}
    {color.RESET}""")

    Continue()
    Reset()
except Exception as e:
    Error(e)