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

option_01 = "Launch-Putty"
option_02 = "Launch-Wireshark"
option_03 = "Launch-Stratoshark"
option_04 = "Launch-SystemInformer"
option_05 = "Launch-VirtualBox"
option_06 = "Launch-AdvancedIPScanner"
option_07 = "Metadata-Extractor"
option_08 = "Hidden-Process-Finder"
option_09 = "Netstat-Viewer"
option_10 = "Bandwidth-Test"

option_11 = "Ip-Lookup"
option_12 = "Ip-Scanner"
option_13 = "Ip-Port-Scanner"
option_14 = "Ip-Pinger"
option_15 = "Ip-Traceroute"
option_16 = "Subnet-Calculator"
option_17 = "Network-Vulnerability-Scanner"

option_18 = "Username-Lookup"
option_19 = "Email-Tracker"
option_20 = "Email-Lookup"
option_21 = "Phone-Number-Lookup"

option_22 = "Website-Vulnerability-Scanner"
option_23 = "Website-Info-Scanner"
option_24 = "Website-Url-Scanner"
option_25 = "Website-MX-Lookup"
option_26 = "Website-Blacklist-Check"
option_27 = "Website-Record-Lookup"
option_28 = "Website-Reverse-Lookup"
option_29 = "Website-DKIM-Lookup"
option_30 = "Website-DMARC-Lookup"
option_31 = "Website-SSL-Check"
option_32 = "Test-Email-Server"
option_33 = "Who-Is-Lookup"

option_next = "Next"
option_back = "Back"
option_info = "Info"

option_01_txt = f"{cyan}[{white}01{cyan}]{white} " + option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = f"{cyan}[{white}02{cyan}]{white} " + option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = f"{cyan}[{white}03{cyan}]{white} " + option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = f"{cyan}[{white}04{cyan}]{white} " + option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = f"{cyan}[{white}05{cyan}]{white} " + option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = f"{cyan}[{white}06{cyan}]{white} " + option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = f"{cyan}[{white}07{cyan}]{white} " + option_07.ljust(30)[:30].replace("-", " ") 
option_08_txt = f"{cyan}[{white}08{cyan}]{white} " + option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = f"{cyan}[{white}09{cyan}]{white} " + option_09.ljust(30)[:30].replace("-", " ")
option_10_txt = f"{cyan}[{white}10{cyan}]{white} " + option_10.ljust(30)[:30].replace("-", " ")

option_11_txt = f"{cyan}[{white}11{cyan}]{white} " + option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = f"{cyan}[{white}12{cyan}]{white} " + option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = f"{cyan}[{white}13{cyan}]{white} " + option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = f"{cyan}[{white}14{cyan}]{white} " + option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = f"{cyan}[{white}15{cyan}]{white} " + option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = f"{cyan}[{white}16{cyan}]{white} " + option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = f"{cyan}[{white}17{cyan}]{white} " + option_17.ljust(30)[:30].replace("-", " ")

option_18_txt = f"{cyan}[{white}18{cyan}]{white} " + option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = f"{cyan}[{white}19{cyan}]{white} " + option_19.ljust(30)[:30].replace("-", " ")
option_20_txt = f"{cyan}[{white}20{cyan}]{white} " + option_20.ljust(30)[:30].replace("-", " ")
option_21_txt = f"{cyan}[{white}21{cyan}]{white} " + option_21.ljust(30)[:30].replace("-", " ")

option_22_txt = f"{cyan}[{white}22{cyan}]{white} " + option_22.ljust(30)[:30].replace("-", " ")
option_23_txt = f"{cyan}[{white}23{cyan}]{white} " + option_23.ljust(30)[:30].replace("-", " ")
option_24_txt = f"{cyan}[{white}24{cyan}]{white} " + option_24.ljust(30)[:30].replace("-", " ")
option_25_txt = f"{cyan}[{white}25{cyan}]{white} " + option_25.ljust(30)[:30].replace("-", " ")
option_26_txt = f"{cyan}[{white}26{cyan}]{white} " + option_26.ljust(30)[:30].replace("-", " ")
option_27_txt = f"{cyan}[{white}27{cyan}]{white} " + option_27.ljust(30)[:30].replace("-", " ")
option_28_txt = f"{cyan}[{white}28{cyan}]{white} " + option_28.ljust(30)[:30].replace("-", " ")
option_29_txt = f"{cyan}[{white}29{cyan}]{white} " + option_29.ljust(30)[:30].replace("-", " ")
option_30_txt = f"{cyan}[{white}30{cyan}]{white} " + option_30.ljust(30)[:30].replace("-", " ")
option_31_txt = f"{cyan}[{white}31{cyan}]{white} " + option_31.ljust(30)[:30].replace("-", " ")
option_32_txt = f"{cyan}[{white}32{cyan}]{white} " + option_32.ljust(30)[:30].replace("-", " ")
option_33_txt = f"{cyan}[{white}33{cyan}]{white} " + option_33.ljust(30)[:30].replace("-", " ")

option_back_txt = option_back + f"{cyan}[{white}B{cyan}]{white}"
option_next_txt = option_next + f"{cyan}[{white}N{cyan}]{white}"
option_info_txt =  f"{cyan}[{white}I{cyan}]{white} " + option_info

page1 = f"""                                                                                                 {option_next_txt} ─┐
 ┌─ {option_info_txt} ┌─────────────┐                 ┌───────────────┐                       ┌───────┐            │
 └─┬─────────┤ Local Tools ├─────────────┬───┤ Network Tools ├─────────────────┬─────┤ OSINT ├────────────┴─
   │         └─────────────┘             │   └───────────────┘                 │     └───────┘
   ├─ {option_01_txt                   }├─ {option_11_txt                    }├─ {option_18_txt}
   ├─ {option_02_txt                   }├─ {option_12_txt                    }├─ {option_19_txt}
   ├─ {option_03_txt                   }├─ {option_13_txt                    }├─ {option_20_txt}
   ├─ {option_04_txt                   }├─ {option_14_txt                    }└─ {option_21_txt}
   ├─ {option_05_txt                   }├─ {option_15_txt                    } 
   ├─ {option_06_txt                   }├─ {option_16_txt                    }
   ├─ {option_07_txt                   }└─ {option_17_txt                    }
   ├─ {option_08_txt                   }
   ├─ {option_09_txt                   }
   └─ {option_10_txt                   }                                  
                                      
"""

page2 = f"""                                                                              {option_next_txt} ─┐
 ┌─ {option_info_txt}  ┌───────────────┐              ┌───────┐          ┌───────┐     {option_back_txt} ─┤
─┴─┬──────────┤ Website Tools ├──────────┬───┤ Empty ├──────┬───┤ Empty ├──────────────┴─
   │          └───────────────┘          │   └───────┘      │   └───────┘
   ├─ {option_22_txt                   }├─ Lorem Ipsum     ├─ Lorem Ipsum
   ├─ {option_23_txt                   }├─ Lorem Ipsum     ├─ Lorem Ipsum
   ├─ {option_24_txt                   }└─ Lorem Ipsum     ├─ Lorem Ipsum
   ├─ {option_25_txt                   }                   └─ Lorem Ipsum
   ├─ {option_26_txt                   }
   ├─ {option_27_txt                   }
   ├─ {option_28_txt                   }
   ├─ {option_29_txt                   }
   ├─ {option_30_txt                   }
   ├─ {option_31_txt                   }
   ├─ {option_32_txt                   }
   └─ {option_33_txt                   }
"""

def Menu():
    try:
        PageNumber = SavedPage()
        menu_mapping = {"1": page1, "2": page2}
        menu = menu_mapping.get(PageNumber, page1)
    except:
        menu = page1
        PageNumber = "1"

    banner = f"""                                                                                     
                                ██║ ██╔╝██║   ██║██║     ██║╚██╗██╔╝    ██║   ██║███║
                                █████╔╝ ██║   ██║██║     ██║ ╚███╔╝     ██║   ██║╚██║
                                ██╔═██╗ ██║   ██║██║     ██║ ██╔██╗     ╚██╗ ██╔╝ ██║
                                ██║  ██╗╚██████╔╝███████╗██║██╔╝ ██╗     ╚████╔╝  ██║
                                ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝      ╚═══╝   ╚═╝
                                
                                     https://github.com/kulixdev/Kulix-Multitool
{menu}"""
    return banner, PageNumber

while True:
    try:
        Clear()
        banner, PageNumber = Menu()
        Title(f"Page {PageNumber}")
        Slow(MainColor(banner))

        choice = input(MainColor(f""" ┌──({white}{LocalUsername}@kulix)─{cyan}[{white}~/{os_name}/Page-{PageNumber}]
 └─{white}$ {reset}"""))

        if choice in ['N', 'n', 'NEXT', 'Next', 'next']:
            PageNumber = {"1": "2", "2": "1"}.get(PageNumber, "1")
            UpdateSavedPage(PageNumber)
            continue

        elif choice in ['B', 'b', 'BACK', 'Back', 'back']:
            PageNumber = {"2": "1"}.get(PageNumber, "1")
            UpdateSavedPage(PageNumber)
            continue

        elif choice in ['I', 'i', 'INFO', 'Info', 'info']:
            StartProgram(f"{option_info}.py")
            continue
        
        elif choice in ['Page1', 'page1', 'p1', 'P1', 'PAGE1']:
            UpdateSavedPage("1")
            continue
        
        elif choice in ['Page2', 'page2', 'p2', 'P2', 'PAGE2']:
            UpdateSavedPage("2")
            continue

        options = {str(i).zfill(2): globals()[f"option_{str(i).zfill(2)}"] for i in range(1, 34)}

        if choice in options:  
            StartProgram(f"{options[choice]}.py")
        elif '0' + choice in options:
            StartProgram(f"{options['0' + choice]}.py")
        else:
            ErrorChoiceStart()

    except KeyboardInterrupt:
        Clear()
        Title("Interrupted")
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} You cannot KeyboardInterrupt this MultiTool, please close it if you wish to exit" + reset)
        Continue()
        Reset()

    except Exception as e:
        Error(e)
