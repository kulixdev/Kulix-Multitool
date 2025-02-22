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
   import socket
   import concurrent.futures
except Exception as e:
   ErrorModule(e)
   
Title("Ip Port Scanner")

try:
    def PortScanner(ip):
        port_protocol_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
            80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
            443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
            1521: "Oracle DB", 3389: "RDP"
        }

        def ScanPort(ip, port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.1)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        protocol = IdentifyProtocol(ip, port)
                        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Port: {white}{port}{cyan} Status: {white}Open{cyan} Protocol: {white}{protocol}{cyan}")
            except Exception:
                pass

        def IdentifyProtocol(ip, port):
            if port in port_protocol_map:
                return port_protocol_map[port]
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.5)
                    sock.connect((ip, port))
                    sock.send(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode('utf-8'))
                    response = sock.recv(100).decode('utf-8')
                    if "HTTP" in response:
                        return "HTTP"
                    sock.send(b"\r\n")
                    response = sock.recv(100).decode('utf-8')
                    if "FTP" in response:
                        return "FTP"
                    sock.send(b"\r\n")
                    response = sock.recv(100).decode('utf-8')
                    if "SSH" in response:
                        return "SSH"
                    return "Unknown"
            except Exception:
                return "Unknown"

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda port: ScanPort(ip, port), range(1, 65536))

    Slow(scan_banner)
    ip = input(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Ip -> {reset}")
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Scanning..")
    PortScanner(ip)
    Continue()
    Reset()
except Exception as e:
    Error(e)
