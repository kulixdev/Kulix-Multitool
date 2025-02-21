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

Title("Traceroute")

try:
    from scapy.all import traceroute
    import time
except Exception as e:
    ErrorModule(e)

try:
    def Traceroute(destination):
        try:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Running custom traceroute to {destination}...")
            ans, _ = traceroute(destination, verbose=0, timeout=2, maxttl=30)

            if ans:
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {GEN_VALID} Traceroute completed successfully")
                sorted_ans = sorted(ans, key=lambda x: x[0].ttl)

                hops = []
                last_hop = None
                repeat_count = 0

                for sent, received in sorted_ans:
                    hop = received.src
                    time_taken = received.time - sent.sent_time

                    if hop == last_hop:
                        repeat_count += 1
                    else:
                        if repeat_count >= 1:
                            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} Hop to destination {last_hop} repeated {repeat_count + 1} times.")
                        repeat_count = 0

                    if repeat_count == 0:
                        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} Hop {sent.ttl}: {hop} (Time: {round(time_taken * 1000, 2)} ms)")
                        hops.append((sent.ttl, hop, round(time_taken * 1000, 2)))

                    last_hop = hop

                if repeat_count >= 1:
                    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} Hop to destination {last_hop} repeated {repeat_count + 1} times.")
            else:
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {GEN_INVALID} No response received")
        except Exception as e:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ERROR} Error: {str(e)} during custom traceroute")

    Slow(scan_banner)
    destination = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Enter the destination IP/URL -> {reset}")
    Censored(destination)
    Traceroute(destination)
    
    Continue()
    Reset()

except Exception as e:
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ERROR} Error: {str(e)}")
