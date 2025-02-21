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
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except Exception as e:
   ErrorModule(e)
   

Title("Phone Number Lookup")

try:
    phone_number = input(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Phone Number -> {color.RESET}")
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Information Recovery..{reset}")
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            status = "Valid"
        else:
            status = "Invalid"

        if phone_number.startswith("+"):
            country_code = "+" + phone_number[1:3] 
        else:
            country_code = "None"
        try: operator = carrier.name_for_number(parsed_number, "fr")
        except: operator = "None"
    
        try: type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
        except: type_number = "None"

        try: 
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else None
        except: timezone_info = "None"
            
        try: country = phonenumbers.region_code_for_number(parsed_number)
        except: country = "None"
            
        try: region = geocoder.description_for_number(parsed_number, "fr")
        except: region = "None"
            
        try: formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        except: formatted_number = "None"
            
        print(f"""
    {INFO_ADD} Phone        : {white}{phone_number}{cyan}
    {INFO_ADD} Formatted    : {white}{formatted_number}{cyan}
    {INFO_ADD} Status       : {white}{status}{cyan}
    {INFO_ADD} Country Code : {white}{country_code}{cyan}
    {INFO_ADD} Country      : {white}{country}{cyan}
    {INFO_ADD} Region       : {white}{region}{cyan}
    {INFO_ADD} Timezone     : {white}{timezone_info}{cyan}
    {INFO_ADD} Operator     : {white}{operator}{cyan}
    {INFO_ADD} Type Number  : {white}{type_number}{cyan}
    """)
        Continue()
        Reset()
    except:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INFO} Invalid Format !")
        Continue()
        Reset()
except Exception as e:
    Error(e)