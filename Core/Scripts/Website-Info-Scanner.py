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
    import concurrent.futures
    import requests
    from urllib.parse import urlparse
    import ssl
    import urllib3
    from requests.exceptions import RequestException
    import time
    import re
    import dns.resolver
    from bs4 import BeautifulSoup
    import whois
except Exception as e:
    ErrorModule(e)

Title("Website Scanner")

try:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    def WebsiteFoundUrl(url):
        website_url = f"https://{url}" if not urlparse(url).scheme else url
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Website: {white}{website_url}{cyan}")
        return website_url

    def WebsiteDomain(website_url):
        domain = urlparse(website_url).netloc
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Domain: {white}{domain}{cyan}")
        return domain

    def WebsiteIp(domain):
        try:
            ip = socket.gethostbyname(domain)
        except socket.gaierror:
            ip = "None"
        if ip != "None":
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} IP: {white}{ip}{cyan}")
        return ip

    def IpType(ip):
        if ':' in ip:
            type = "ipv6" 
        elif '.' in ip:
            type = "ipv4"
        else:
            return
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} IP Type: {white}{type}{cyan}")

    def WebsiteSecure(website_url):
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Secure: {white}{website_url.startswith('https://')}{cyan}")

    def WebsiteStatus(website_url):
        try:
            status_code = requests.get(website_url, timeout=5).status_code
        except RequestException:
            status_code = 404
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Status Code: {white}{status_code}{cyan}")

    def IpInfo(ip):
        try:
            api = requests.get(f"https://ipinfo.io/{ip}/json").json()
        except RequestException:
            api = {}
        for key in ['country', 'hostname', 'isp', 'org', 'asn']:
            if key in api:
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Host {key.capitalize()}: {white}{api[key]}{cyan}")

    def IpDns(ip):
        try:
            dns = socket.gethostbyaddr(ip)[0]
        except:
            dns = "None"
        if dns != "None":
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Host DNS: {white}{dns}{cyan}")

    def WebsitePort(ip):
        ports = [21, 22, 23, 25, 53, 69, 80, 110, 123, 143, 194, 389, 443, 161, 3306, 5432, 6379, 1521, 3389]
        port_protocol_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
            80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
            443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
            1521: "Oracle DB", 3389: "RDP"
        }

        def ScanPort(ip, port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(1)
                    if sock.connect_ex((ip, port)) == 0:
                        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Port: {white}{port}{cyan} Status: {white}Open{cyan} Protocol: {white}{port_protocol_map.get(port, 'Unknown')}{cyan}")
            except:
                pass

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda p: ScanPort(ip, p), ports)

    def HttpHeaders(website_url):
        try:
            headers = requests.get(website_url, timeout=5).headers
            for header, value in headers.items():
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} HTTP Header: {white}{header}{cyan} Value: {white}{value}{cyan}")
        except RequestException:
            pass

    def CheckSslCertificate(website_url):
        try:
            with ssl.create_default_context().wrap_socket(socket.socket(), server_hostname=urlparse(website_url).hostname) as sock:
                sock.settimeout(5)
                sock.connect((urlparse(website_url).hostname, 443))
                cert = sock.getpeercert()
            for key, value in cert.items():
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} SSL Certificate Key: {white}{key}{cyan} Value: {white}{value}{cyan}")
        except:
            pass

    def CheckSecurityHeaders(website_url):
        headers = ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection']
        try:
            response_headers = requests.get(website_url, timeout=5).headers
            for header in headers:
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} {'Missing' if header not in response_headers else 'Security'} Header: {white}{header}{cyan}")
        except RequestException:
            pass

    def AnalyzeCookies(website_url):
        try:
            cookies = requests.get(website_url, timeout=5).cookies
            for cookie in cookies:
                secure = 'Secure' if cookie.secure else 'Not Secure'
                httponly = 'HttpOnly' if cookie.has_nonstandard_attr('HttpOnly') else 'Not HttpOnly'
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Cookie: {white}{cookie.name}{cyan} Secure: {white}{secure}{cyan} HttpOnly: {white}{httponly}{cyan}")
        except RequestException:
            pass

    def DetectTechnologies(website_url):
        try:
            response = requests.get(website_url, timeout=5)
            headers = response.headers
            soup = BeautifulSoup(response.content, 'html.parser')
            techs = []
            if 'x-powered-by' in headers:
                techs.append(f"X-Powered-By: {headers['x-powered-by']}")
            if 'server' in headers:
                techs.append(f"Server: {headers['server']}")
            for script in soup.find_all('script', src=True):
                if 'jquery' in script['src']:
                    techs.append("jQuery")
                if 'bootstrap' in script['src']:
                    techs.append("Bootstrap")
            for tech in techs:
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Detected Technology: {white}{tech}{cyan}")
        except:
            pass

    Slow(scan_banner)
    url = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Website URL -> {reset}")
    Censored(url)
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Scanning..{reset}")

    website_url = WebsiteFoundUrl(url)
    domain = WebsiteDomain(website_url)
    ip = WebsiteIp(domain)
    IpType(ip)
    WebsiteSecure(website_url)
    WebsiteStatus(website_url)
    IpInfo(ip)
    IpDns(ip)
    WebsitePort(ip)
    HttpHeaders(website_url)
    CheckSslCertificate(website_url)
    CheckSecurityHeaders(website_url)
    AnalyzeCookies(website_url)
    DetectTechnologies(website_url)
    Continue()
    Reset()

except Exception as e:
    Error(e)
