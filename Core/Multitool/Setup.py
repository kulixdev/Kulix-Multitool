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

from Core.Config.Utilities import *

try:
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  
    requirements_file = os.path.join(base_path, "Config", "requirements.txt")

    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the Python modules required for the Kulix MultiTool:\n")
        os.system("python -m pip install --upgrade pip")
        os.system(f"python -m pip install -r {requirements_file}")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the Python modules required for the Kulix MultiTool:\n")
        os.system("python3 -m pip install --upgrade pip")
        os.system(f"python3 -m pip install -r {requirements_file}")

    Continue()

except Exception as e:
    input(f"An error occurred: {e}")