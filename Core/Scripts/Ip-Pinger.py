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
    import concurrent.futures
    import time
    import socket
except Exception as e:
    ErrorModule(e)

Title("Ip Pinger")

try:
    def PingIp(hostname, port, bytes):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(2)
                start_time = time.time()
                sock.connect((hostname, port))
                data = b'\x00' * bytes
                sock.sendall(data)
                end_time = time.time()
                elapsed_time = (end_time - start_time) * 1000
                print(f'{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Hostname: {white}{hostname}{cyan} time: {white}{elapsed_time:.2f}ms{cyan} port: {white}{port}{cyan} bytes: {white}{bytes}{cyan} status: {white}succeed{cyan}')
        except socket.error:
            print(f'{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ERROR} Hostname: {white}{hostname}{cyan} time: {white}N/A{cyan} port: {white}{port}{cyan} bytes: {white}{bytes}{cyan} status: {white}fail{cyan}')

    Slow(wifi_banner)

    hostname = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Ip -> " + color.RESET)

    try:
        port_input = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Port (enter for default) -> " + color.RESET)
        port = int(port_input) if port_input else 80
        
        bytes_input = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Bytes (enter for default) -> " + color.RESET)
        bytes = int(bytes_input) if bytes_input else 64
    except ValueError:
        ErrorNumber()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(4):  # Ensures exactly 4 attempts
            executor.submit(PingIp, hostname, port, bytes)
            time.sleep(1)  # Pause between pings

except Exception as e:
    Error(e)

Continue()
Reset()
