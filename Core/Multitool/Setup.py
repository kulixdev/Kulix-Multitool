# Copyright (c) Kulix  
# See the file 'LICENSE' for your permissions while using this content 
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|   
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code  
#     - In the case you wish to analyze this code under any circumstance; note that touching this code should not be altered under any circumstance  
#            - If this code is altered, the owner holds no obligation for damages or errors caused by the altered code  
#     - Do not resell this tool, do not credit it as your own

import sys
import os
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Core.Config.Utilities import *

try:
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  
    requirements_file = os.path.join(base_path, "Config", "requirements.txt")

    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the Python modules required for the Kulix MultiTool:\n")
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run(["python", "-m", "pip", "install", "-r", requirements_file], check=True)

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the Python modules required for the Kulix MultiTool:\n")
        subprocess.run(["python3", "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run(["python3", "-m", "pip", "install", "-r", requirements_file], check=True)

    Continue()

except subprocess.CalledProcessError as e:
    input(f"An error occurred: {e}")
except Exception as e:
    input(f"An unexpected error occurred: {e}")
