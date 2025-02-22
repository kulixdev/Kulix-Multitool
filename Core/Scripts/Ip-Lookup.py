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
    import requests
except Exception as e:
   ErrorModule(e)
   
Title("Ip Lookup")

try:
    Slow(map_banner)
    ip = input(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Ip -> {reset}")

    try:
        response = requests.get(f"https://{website}/api/ip/ip={ip}")
        api = response.json()

        ip = api.get('ip')
        status = api.get('status')
        country = api.get('country')
        country_code = api.get('country_code')
        region = api.get('region')
        region_code = api.get('region_code')
        zip = api.get('zip')
        city = api.get('city')
        latitude = api.get('latitude')
        longitude = api.get('longitude')
        timezone = api.get('timezone')
        isp = api.get('isp')
        org = api.get('org')
        as_host = api.get('as')

    except:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        api = response.json()

        status = "Valid" if api.get('status') == "success" else "Invalid"
        country = api.get('country', "None")
        country_code = api.get('countryCode', "None")
        region = api.get('regionName', "None")
        region_code = api.get('region', "None")
        zip = api.get('zip', "None")
        city = api.get('city', "None")
        latitude = api.get('lat', "None")
        longitude = api.get('lon', "None")
        timezone = api.get('timezone', "None")
        isp = api.get('isp', "None")
        org = api.get('org', "None")
        as_host = api.get('as', "None")

    Slow(f"""    
    {INFO_ADD} Status     : {white}{status}{cyan}
    {INFO_ADD} Country    : {white}{country} ({country_code}){cyan}
    {INFO_ADD} Region     : {white}{region} ({region_code}){cyan}
    {INFO_ADD} Zip        : {white}{zip}{cyan}
    {INFO_ADD} City       : {white}{city}{cyan}
    {INFO_ADD} Latitude   : {white}{latitude}{cyan}
    {INFO_ADD} Longitude  : {white}{longitude}{cyan}
    {INFO_ADD} Timezone   : {white}{timezone}{cyan}
    {INFO_ADD} Isp        : {white}{isp}{cyan}
    {INFO_ADD} Org        : {white}{org}{cyan}
    {INFO_ADD} As         : {white}{as_host}{cyan}{reset}
    """)

    Continue()
    Reset()
except Exception as e:
    Error(e)