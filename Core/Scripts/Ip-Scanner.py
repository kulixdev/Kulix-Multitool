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
    import socket
    import ssl
    import subprocess
    import sys
    import requests
    from requests.exceptions import RequestException
    import concurrent.futures
except Exception as e:
    ErrorModule(e)
    
Title("Ip Scanner")

try:
    def IpType(ip):
        ip_type = "Unknown"
        if ':' in ip:
            ip_type = "ipv6"
        elif '.' in ip:
            ip_type = "ipv4"
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} IP Type: {white}{ip_type}{cyan}")

    def IpPing(ip):
        try:
            ping_cmd = ['ping', '-n', '1', ip] if sys.platform.startswith("win") else ['ping', '-c', '1', '-W', '1', ip]
            result = subprocess.run(ping_cmd, capture_output=True, text=True, timeout=1)
            ping = "Succeed" if result.returncode == 0 else "Fail"
        except Exception:
            ping = "Fail"
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Ping: {white}{ping}{cyan}")

    def IpPort(ip):
        port_protocol_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
            80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
            443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
            1521: "Oracle DB", 3389: "RDP"
        }
        
        def scan_port(ip, port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(1)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        protocol = port_protocol_map.get(port, "Unknown")
                        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Port: {white}{port}{cyan} Status: {white}Open{cyan} Protocol: {white}{protocol}{cyan}")
            except Exception:
                pass
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda port: scan_port(ip, port), port_protocol_map.keys())

    def IpDns(ip):
        try:
            dns, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
        except Exception:
            dns = "None"
        if dns != "None":
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} DNS: {white}{dns}{cyan}")

    def IpHostInfo(ip):
        api_url = f"https://ipinfo.io/{ip}/json"
        try:
            response = requests.get(api_url)
            api = response.json()
        except RequestException:
            api = {}

        host_country = api.get('country', 'None')
        if host_country != "None":
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Host Country: {white}{host_country}{cyan}")

        host_name = api.get('hostname', 'None')
        if host_name != "None":
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Host Name: {white}{host_name}{cyan}")

        host_isp = api.get('org', 'None')
        if host_isp != "None":
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Host ISP: {white}{host_isp}{cyan}")

        host_as = api.get('asn', 'None')
        if host_as != "None":
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Host AS: {white}{host_as}{cyan}")

    def SslCertificateCheck(ip):
        port = 443
        try:
            with socket.create_connection((ip, port), timeout=1) as sock:
                context = ssl.create_default_context()
                with context.wrap_socket(sock, server_hostname=ip) as ssock:
                    cert = ssock.getpeercert()
                    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} SSL Certificate: {white}{cert}{cyan}")
        except Exception as e:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} SSL Certificate Check Failed: {white}{e}{cyan}")


    Slow(scan_banner)
    ip = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Ip -> {reset}")
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Information Recovery..{reset}")
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Ip: {white}{ip}{cyan}")
    IpType(ip)
    IpPing(ip)
    IpDns(ip)
    IpPort(ip)
    IpHostInfo(ip)
    SslCertificateCheck(ip)
    Continue()
    Reset()

except Exception as e:
    Error(e)
