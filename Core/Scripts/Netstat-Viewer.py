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

Title("Netstat")

try:
    import psutil
    from tabulate import tabulate
except Exception as e:
    ErrorModule(e)

def Netstat():
    try:
        connections = psutil.net_connections(kind='inet')
        netstat_data = []
        valid_statuses = ['ESTABLISHED', 'LISTEN', 'CLOSE_WAIT', 'TIME_WAIT', 'FIN_WAIT2', 'SYN_SENT', 'SYN_RECV', 'CLOSE', 'LAST_ACK', 'FIN_WAIT1']

        for conn in connections:
            status = conn.status
            local_address = f"{conn.laddr.ip}:{conn.laddr.port}"
            remote_address = f"{conn.raddr.ip if conn.raddr else 'None'}:{conn.raddr.port if conn.raddr else 'None'}"
            pid = conn.pid
            name = psutil.Process(pid).name() if pid else 'N/A'
            netstat_data.append([local_address, remote_address, status, pid, name])

        valid_connections = [item for item in netstat_data if item[1] != 'None:None' or item[2] == 'LISTEN']
        none_connections = [item for item in netstat_data if item[1] == 'None:None' and item[2] != 'LISTEN']
        valid_connections.sort(key=lambda x: (x[1], x[2] not in valid_statuses, x[2]))
        sorted_netstat_data = valid_connections + none_connections
        
        if sorted_netstat_data:
            formatted_table = tabulate(sorted_netstat_data, headers=["Local Address", "Remote Address", "Status", "PID", "Process Name"], tablefmt="fancy_grid")
            Quick(MainColor(formatted_table))
        else:
            Quick(MainColor("No active network connections found."))

        Continue()
        Reset()

    except Exception as e:
        print(f"Error: {str(e)}")

try:
    Netstat()
except Exception as e:
    print(f"Error: {str(e)}")