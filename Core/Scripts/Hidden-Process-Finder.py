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
    import psutil
    import subprocess
except Exception as e:
   ErrorModule(e)

try:
    Title("Hidden Processes")

    def GetProcesses():
        processes = {}
        for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline', 'ppid', 'cpu_percent', 'memory_info']):
            try:
                processes[proc.info['pid']] = proc.info
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return processes

    def GetTasklist():
        hidden_processes = []
        try:
            result = subprocess.run(["tasklist", "/fo", "csv", "/nh"], capture_output=True, text=True, check=True)
            tasklist_pids = {int(line.split(',')[1].strip('"')) for line in result.stdout.splitlines() if line}
            running_processes = GetProcesses()

            for pid in tasklist_pids:
                if pid not in running_processes:
                    hidden_processes.append({
                        'pid': pid,
                        'name': 'Unknown',
                        'exe': 'Unknown',
                        'cmdline': 'Unknown',
                        'ppid': 'Unknown',
                        'cpu': 'Unknown',
                        'memory': 'Unknown'
                    })
                else:
                    hidden_processes.append(running_processes[pid])

            for proc in running_processes.values():
                if not proc.get('exe') or (proc.get('cmdline') and "hidden" in ' '.join(proc['cmdline'])):
                    hidden_processes.append(proc)

                if proc.get('cpu_percent', 0) > 50 or proc.get('memory_info', None) and proc['memory_info'].rss > 500 * 1024 * 1024:
                    hidden_processes.append(proc)

                if proc.get('exe') and ("\\AppData\\" in proc['exe'] or "\\Temp\\" in proc['exe']):
                    hidden_processes.append(proc)

        except Exception as e:
            ErrorModule(e)

        return hidden_processes

    def HiddenProcesses():
        hidden_processes = GetTasklist()
        if not hidden_processes:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} No hidden processes found.{cyan}")
        else:
            print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Hidden Processes:{cyan}")
            for proc in hidden_processes:
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} PID: {white}{proc['pid']}{cyan}")
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Name: {white}{proc['name']}{cyan}")
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Executable: {white}{proc['exe']}{cyan}")
                cmdline = ' '.join(proc['cmdline']) if isinstance(proc['cmdline'], list) else proc.get('cmdline', 'Unknown')
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Command Line: {white}{cmdline}{cyan}")
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Parent PID: {white}{proc['ppid']}{cyan}")
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} CPU Usage: {white}{proc.get('cpu_percent', 'Unknown')}{cyan}%")
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} Memory Usage: {white}{proc.get('memory_info', 'Unknown')}{cyan} bytes")

    Slow(scan_banner)
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Scanning for hidden processes...{reset}")
    HiddenProcesses()
    Continue()
    Reset()

except Exception as e:
    Error(e)
