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
    import speedtest
    import time
except Exception as e:
    ErrorModule(e)

Title("Speed Test")

def BandwidthTest():
    st = speedtest.Speedtest()
    st.get_best_server()
    start_time = time.time()

    time.sleep(1)

    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping
    server = st.results.server

    elapsed_time = time.time() - start_time
    print(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {GEN_VALID} Bandwidth Test Results: {green}")
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Download Speed: {white}{download_speed:.2f} Mbps{cyan}")
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Upload Speed: {white}{upload_speed:.2f} Mbps{cyan}")
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Ping: {white}{ping} ms{cyan}")
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Server: {white}{server['host']} ({server['country']}){cyan}")
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Test Duration: {white}{elapsed_time:.2f}s{cyan}")

try:
    BandwidthTest()
    Continue()
    Reset()

except Exception as e:
    ErrorModule(e)
