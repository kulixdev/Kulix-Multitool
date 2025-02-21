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
    import ipaddress
    import time
    import struct
    import socket
except Exception as e:
    ErrorModule(e)

Title("Subnet Calculator")

def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if first_octet <= 127:
        return 'A'
    elif first_octet <= 191:
        return 'B'
    elif first_octet <= 223:
        return 'C'
    elif first_octet <= 239:
        return 'D'
    else:
        return 'E'

def get_wildcard_mask(subnet_mask):
    subnet_octets = subnet_mask.split('.')
    wildcard_octets = [str(255 - int(octet)) for octet in subnet_octets]
    return '.'.join(wildcard_octets)

def get_ip_type(ip):
    if ipaddress.ip_address(ip).is_private:
        return "Private"
    return "Public"

def subnet_calculator(ip, subnet_mask):
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Calculating subnet details for {ip}/{subnet_mask}...", end="")
    start_time = time.time()

    try:
        network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)
        binary_mask = '.'.join(f'{int(octet):08b}' for octet in subnet_mask.split('.'))
        ip_class = get_ip_class(ip)
        wildcard_mask = get_wildcard_mask(subnet_mask)
        ip_type = get_ip_type(ip)
        integer_id = struct.unpack("!I", socket.inet_aton(ip))[0]
        hex_id = hex(integer_id)
        binary_id = bin(integer_id)[2:].zfill(32)
        in_addr_arpa = '.'.join(reversed(ip.split('.'))) + ".in-addr.arpa"
        ipv4_mapped = f"::ffff:{ip}"
        six_to_four_prefix = f"2002:{ip.replace('.', '')}::/48"
        elapsed_time = time.time() - start_time

        print(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {GEN_VALID} Subnet Calculation Results: {green}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} IP Address: {white}{ip}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Network Address: {white}{network.network_address}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Usable Host IP Range: {white}{list(network.hosts())[0]} - {list(network.hosts())[-1]}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Broadcast Address: {white}{network.broadcast_address}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Total Number of Hosts: {white}{network.num_addresses}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Number of Usable Hosts: {white}{network.num_addresses - 2 if network.num_addresses > 2 else 0}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Subnet Mask: {white}{subnet_mask}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Wildcard Mask: {white}{wildcard_mask}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Binary Subnet Mask: {white}{binary_mask}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} IP Class: {white}{ip_class}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} CIDR Notation: {white}/{network.prefixlen}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} IP Type: {white}{ip_type}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Short: {white}{ip} /{network.prefixlen}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Binary ID: {white}{binary_id}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Integer ID: {white}{integer_id}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Hex ID: {white}{hex_id}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} in-addr.arpa: {white}{in_addr_arpa}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} IPv4 Mapped Address: {white}{ipv4_mapped}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} 6to4 Prefix: {white}{six_to_four_prefix}{cyan}")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Test Duration: {white}{elapsed_time:.2f}s{cyan}")
    
    except Exception as e:
        print(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ERROR} Subnet calculation failed: {red}{e}{reset}")

try:
    ip_version = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Select IP Type (IPv4/IPv6) -> {reset}").strip()
    if ip_version.lower() == "ipv6":
        ip = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Enter IPv6 Address -> {reset}")
        subnet = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Enter Subnet Mask OR Network Bits (e.g., 255.255.255.0 OR 8) -> {reset}")
    else:
        ip = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Enter IPv4 Address -> {reset}")
        subnet = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Enter Subnet Mask OR Network Bits (e.g., 255.255.255.0 OR 8) -> {reset}")
    
    Censored(ip)
    Censored(subnet)
    subnet_calculator(ip, subnet)
    Continue()
    Reset()

except Exception as e:
    ErrorModule(e)
