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

Title("Blacklist Check")

try:
    import dns.resolver
    import socket
except Exception as e:
    ErrorModule(e)

blacklist_services = {
    "zen.spamhaus.org": {"method": "reverse", "query": "{reversed_domain}.zen.spamhaus.org"},  # Spamhaus
    "bl.spamcop.net": {"method": "reverse", "query": "{reversed_domain}.bl.spamcop.net"},  # SpamCop
    "b.barracudacentral.org": {"method": "reverse", "query": "{reversed_domain}.b.barracudacentral.org"},  # Barracuda
    "dnsbl.sorbs.net": {"method": "reverse", "query": "{reversed_domain}.dnsbl.sorbs.net"},  # SORBS
    "multi.surbl.org": {"method": "reverse", "query": "{reversed_domain}.multi.surbl.org"},  # SURBL
    "ivmURI": {"method": "reverse", "query": "{reversed_domain}.ivmURI"},  # ivmURI
    "nordspam.dbl": {"method": "reverse", "query": "{reversed_domain}.nordspam.dbl"},  # Nordspam DBL
    "spamhaus.dbl": {"method": "reverse", "query": "{reversed_domain}.spamhaus.dbl"},  # Spamhaus DBL
    "0spam.dbl": {"method": "reverse", "query": "{reversed_domain}.0spam.dbl"},  # 0SPAM
    "backscatterer.org": {"method": "reverse", "query": "{reversed_domain}.backscatterer.org"},  # BACKSCATTERER
    "psbl.dnsbl": {"method": "reverse", "query": "{reversed_domain}.psbl.dnsbl"},  # PSBL
    "spamcop.dnsbl": {"method": "reverse", "query": "{reversed_domain}.spamcop.dnsbl"},  # SPAMCOP
    "uceprotect1.dnsbl": {"method": "reverse", "query": "{reversed_domain}.uceprotect1.dnsbl"},  # UCEPROTECTL1
    "uceprotect2.dnsbl": {"method": "reverse", "query": "{reversed_domain}.uceprotect2.dnsbl"},  # UCEPROTECTL2
    "uceprotect3.dnsbl": {"method": "reverse", "query": "{reversed_domain}.uceprotect3.dnsbl"},  # UCEPROTECTL3
    "zapbl.dnsbl": {"method": "reverse", "query": "{reversed_domain}.zapbl.dnsbl"},  # ZapBL
    "kisa.dnsbl": {"method": "reverse", "query": "{reversed_domain}.kisa.dnsbl"},  # KISA
    "list.dsbl.org": {"method": "reverse", "query": "{reversed_domain}.list.dsbl.org"},  # DSBL
    "bl.spamrbl.com": {"method": "reverse", "query": "{reversed_domain}.bl.spamrbl.com"},  # SpamRBL
    "dnsbl.inps.de": {"method": "reverse", "query": "{reversed_domain}.dnsbl.inps.de"},  # INPS
    "blackholes.five-ten-sg.com": {"method": "reverse", "query": "{reversed_domain}.blackholes.five-ten-sg.com"},  # FiveTenSG
    "ivmSIP": {"method": "reverse", "query": "{reversed_domain}.ivmSIP"},  # ivmSIP
    "ivmSIP24": {"method": "reverse", "query": "{reversed_domain}.ivmSIP24"},  # ivmSIP24
    "JIPPG": {"method": "reverse", "query": "{reversed_domain}.JIPPG"},  # JIPPG
    "KEMPTBL": {"method": "reverse", "query": "{reversed_domain}.KEMPTBL"},  # KEMPTBL
    "Konstant": {"method": "reverse", "query": "{reversed_domain}.Konstant"},  # Konstant
    "LASHBACK": {"method": "reverse", "query": "{reversed_domain}.LASHBACK"},  # LASHBACK
    "MAILSPIKE BL": {"method": "reverse", "query": "{reversed_domain}.MAILSPIKE BL"},  # MAILSPIKE BL
    "MAILSPIKE Z": {"method": "reverse", "query": "{reversed_domain}.MAILSPIKE Z"},  # MAILSPIKE Z
    "MSRBL Phishing": {"method": "reverse", "query": "{reversed_domain}.MSRBL Phishing"},  # MSRBL Phishing
    "MSRBL Spam": {"method": "reverse", "query": "{reversed_domain}.MSRBL Spam"},  # MSRBL Spam
    "NETHERRELAYS": {"method": "reverse", "query": "{reversed_domain}.NETHERRELAYS"},  # NETHERRELAYS
    "NETHERUNSURE": {"method": "reverse", "query": "{reversed_domain}.NETHERUNSURE"},  # NETHERUNSURE
    "NIXSPAM": {"method": "reverse", "query": "{reversed_domain}.NIXSPAM"},  # NIXSPAM
    "Nordspam BL": {"method": "reverse", "query": "{reversed_domain}.Nordspam BL"},  # Nordspam BL
    "RATS Dyna": {"method": "reverse", "query": "{reversed_domain}.RATS Dyna"},  # RATS Dyna
    "RATS NoPtr": {"method": "reverse", "query": "{reversed_domain}.RATS NoPtr"},  # RATS NoPtr
    "RATS Spam": {"method": "reverse", "query": "{reversed_domain}.RATS Spam"},  # RATS Spam
    "RBL JP": {"method": "reverse", "query": "{reversed_domain}.RBL JP"},  # RBL JP
    "s5h.net": {"method": "reverse", "query": "{reversed_domain}.s5h.net"},  # s5h.net
    "SCHULTE": {"method": "reverse", "query": "{reversed_domain}.SCHULTE"},  # SCHULTE
    "SEM BACKSCATTER": {"method": "reverse", "query": "{reversed_domain}.SEM BACKSCATTER"},  # SEM BACKSCATTER
    "SEM BLACK": {"method": "reverse", "query": "{reversed_domain}.SEM BLACK"},  # SEM BLACK
    "Sender Score Reputation Network": {"method": "reverse", "query": "{reversed_domain}.Sender Score Reputation Network"},  # Sender Score Reputation Network
    "SERVICESNET": {"method": "reverse", "query": "{reversed_domain}.SERVICESNET"},  # SERVICESNET
    "Spamhaus ZEN": {"method": "reverse", "query": "{reversed_domain}.Spamhaus ZEN"},  # Spamhaus ZEN
    "SPFBL DNSBL": {"method": "reverse", "query": "{reversed_domain}.SPFBL DNSBL"},  # SPFBL DNSBL
    "Suomispam Reputation": {"method": "reverse", "query": "{reversed_domain}.Suomispam Reputation"},  # Suomispam Reputation
    "SWINOG": {"method": "reverse", "query": "{reversed_domain}.SWINOG"},  # SWINOG
    "TRIUMF": {"method": "reverse", "query": "{reversed_domain}.TRIUMF"},  # TRIUMF
    "TRUNCATE": {"method": "reverse", "query": "{reversed_domain}.TRUNCATE"},  # TRUNCATE
    "UCEPROTECTL1": {"method": "reverse", "query": "{reversed_domain}.UCEPROTECTL1"},  # UCEPROTECTL1
    "UCEPROTECTL2": {"method": "reverse", "query": "{reversed_domain}.UCEPROTECTL2"},  # UCEPROTECTL2
    "UCEPROTECTL3": {"method": "reverse", "query": "{reversed_domain}.UCEPROTECTL3"},  # UCEPROTECTL3
    "Woodys SMTP Blacklist": {"method": "reverse", "query": "{reversed_domain}.Woodys SMTP Blacklist"},  # Woodys SMTP Blacklist
    "ZapBL": {"method": "reverse", "query": "{reversed_domain}.ZapBL"},  # ZapBL
    "KISA": {"method": "reverse", "query": "{reversed_domain}.KISA"},  # KISA
    "NoSolicitado": {"method": "reverse", "query": "{reversed_domain}.NoSolicitado"}  # NoSolicitado
}

def BlacklistLookup(mx_domain):
    blacklisted = []
    not_blacklisted = []
    reversed_domain = '.'.join(reversed(mx_domain.split('.')))
    
    for blacklist, details in blacklist_services.items():
        try:
            blacklist_query = details["query"].format(reversed_domain=reversed_domain)
            dns.resolver.resolve(blacklist_query, 'A')
            blacklisted.append(blacklist)
        except (dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.exception.DNSException) as e:
            not_blacklisted.append(blacklist)
    
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Blacklist Lookup for {mx_domain}:")
    
    if blacklisted:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ERROR} {mx_domain} is blacklisted in the following blacklists:")
        for i, blacklist in enumerate(blacklisted, start=1):
            if i == len(blacklisted):
                print(f"└─── {white}{blacklist}{cyan}")
            else:
                print(f"├─── {white}{blacklist}{cyan}")
    elif not blacklisted:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} No blacklists detected for {mx_domain}")

Slow(scan_banner)
domain = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Domain Name -> {reset}")
Censored(domain)

BlacklistLookup(domain)
Continue()
Reset()
