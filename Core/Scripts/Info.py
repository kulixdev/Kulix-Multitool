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
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Info")

try:
    print(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Information Recovery..{reset}")

    Slow(f"""
    {INFO_ADD} Tool Name     :  {white}{name}
    {INFO_ADD} Version       :  {white}{version}
    {INFO_ADD} Copyright     :  {white}{copyright}
    {INFO_ADD} Coding        :  {white}{lang}
    {INFO_ADD} Language      :  {white}{language}
    {INFO_ADD} Github        :  {white}{github}
    {INFO_ADD} Creator       :  {white}{creator}
    {INFO_ADD} Platform      :  {white}{platform}
    {reset}""")

    license_read = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Open 'LICENSE' ? (y/n) -> {reset}")
    if license_read in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webbrowser.open_new_tab(license)
    else:
        pass
    Continue()
    Reset()
except Exception as e:
    Error(e)
