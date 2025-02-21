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
    import os
except Exception as e:
    ErrorModule(e)

os.startfile(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Executables", "Portables", "VirtualBox", "VirtualBox.exe")))

print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {NOTE} VirtualBox has now been launched...")
Continue()
Reset()
