# Copyright (c) Kulix  
# See the file 'LICENSE' for copying permission  
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|  
# EN:  
#     - Copyright (c) Kulix  
#     - See the file 'LICENSE' for copying permission  
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code  
#     - In the case you wish to analyze this code under any circumstance; note that touching this code should not be altered under any circumstance  
#            - If this code is altered, the owner holds no obligation for damages or errors caused by the altered code  
#     - Do not resell this tool, do not credit it to yours  
#
# FR (Français) :  
#     - Droits d’auteur (c) Kulix  
#     - Voir le fichier 'LICENSE' pour les permissions de copie  
#     - Ne touchez pas ou ne modifiez pas le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez modifier le code  
#     - Si vous souhaitez analyser ce code pour une raison quelconque, sachez que ce code ne doit en aucun cas être modifié  
#            - Si ce code est modifié, le propriétaire ne pourra être tenu responsable des dommages ou erreurs causés par le code modifié  
#     - Ne revendez pas cet outil, ne vous l’attribuez pas  
#
# ES (Español) :  
#     - Derechos de autor (c) Kulix  
#     - Consulte el archivo 'LICENSE' para obtener permisos de copia  
#     - No toque ni modifique el código a continuación. Si hay un error, comuníquese con el propietario, pero bajo ninguna circunstancia debe modificar el código  
#     - Si desea analizar este código por cualquier motivo, tenga en cuenta que no debe modificarse bajo ninguna circunstancia  
#            - Si este código se modifica, el propietario no se hace responsable de los daños o errores causados por el código modificado  
#     - No revenda esta herramienta, no se la atribuya  
#
# DE (Deutsch) :  
#     - Urheberrecht (c) Kulix  
#     - Siehe die Datei 'LICENSE' für Kopiergenehmigungen  
#     - Berühren oder ändern Sie den Code unten nicht. Wenn ein Fehler auftritt, wenden Sie sich bitte an den Eigentümer, aber unter keinen Umständen sollten Sie den Code ändern  
#     - Falls Sie diesen Code analysieren möchten, beachten Sie, dass der Code unter keinen Umständen geändert werden darf  
#            - Wenn dieser Code geändert wird, übernimmt der Eigentümer keine Haftung für Schäden oder Fehler, die durch den geänderten Code verursacht wurden  
#     - Verkaufen Sie dieses Tool nicht weiter, schreiben Sie es sich nicht selbst zu  
#
# PT (Português) :  
#     - Direitos autorais (c) Kulix  
#     - Consulte o arquivo 'LICENSE' para obter permissão de cópia  
#     - Não toque nem modifique o código abaixo. Se houver um erro, entre em contato com o proprietário, mas sob nenhuma circunstância deve modificar o código  
#     - Caso deseje analisar este código por qualquer motivo, observe que ele não deve ser alterado sob nenhuma circunstância  
#            - Se este código for alterado, o proprietário não se responsabiliza por danos ou erros causados pelo código modificado  
#     - Não revenda esta ferramenta, não a credite como sua  
#
# IT (Italiano) :  
#     - Copyright (c) Kulix  
#     - Vedere il file 'LICENSE' per i permessi di copia  
#     - Non toccare o modificare il codice sottostante. Se c'è un errore, contatta il proprietario, ma in nessun caso devi modificare il codice  
#     - Se desideri analizzare questo codice per qualsiasi motivo, tieni presente che non deve essere modificato in nessuna circostanza  
#            - Se questo codice viene modificato, il proprietario non è responsabile per eventuali danni o errori causati dal codice modificato  
#     - Non rivendere questo strumento, non attribuirlo a te stesso  
#
# ZH (中文) :  
#     - 版权所有 (c) Kulix  
#     - 复制许可请参阅 'LICENSE' 文件  
#     - 请勿触碰或修改以下代码。如果出现错误，请联系所有者，但在任何情况下都不得修改代码  
#     - 如果您出于任何原因想要分析此代码，请注意不得以任何方式修改它  
#            - 如果此代码被修改，所有者不对由修改后的代码引起的损害或错误承担任何责任  
#     - 请勿转售此工具，也不得将其归为您的作品  
#
# RU (Русский) :  
#     - Авторские права (c) Kulix  
#     - См. файл 'LICENSE' для разрешения на копирование  
#     - Не трогайте и не изменяйте код ниже. Если возникла ошибка, свяжитесь с владельцем, но ни при каких обстоятельствах не изменяйте код  
#     - Если вы хотите проанализировать этот код по какой-либо причине, обратите внимание, что он не должен изменяться ни при каких обстоятельствах  
#            - Если этот код изменен, владелец не несет ответственности за ущерб или ошибки, вызванные измененным кодом  
#     - Не перепродавайте этот инструмент, не присваивайте его себе  
#
# JA (日本語) :  
#     - 著作権 (c) Kulix  
#     - コピー許可については 'LICENSE' ファイルを参照してください  
#     - 以下のコードを触ったり変更したりしないでください。エラーが発生した場合は所有者に連絡してください。ただし、いかなる状況でもコードを変更しないでください  
#     - 何らかの理由でこのコードを分析したい場合、このコードをいかなる状況でも変更してはいけないことに注意してください  
#            - もしこのコードが変更された場合、所有者は変更されたコードによって生じた損害やエラーに対して責任を負いません  
#     - このツールを再販したり、自分のものとしてクレジットしたりしないでください  
#
# AR (العربية) :  
#     - حقوق النشر (c) Kulix  
#     - راجع ملف 'LICENSE' للحصول على إذن النسخ  
#     - لا تلمس أو تعدل الكود أدناه. إذا كان هناك خطأ، يرجى الاتصال بالمالك، ولكن لا يجوز لك تعديل الكود تحت أي ظرف  
#     - في حال كنت ترغب في تحليل هذا الكود لأي سبب، لاحظ أنه لا ينبغي تعديله تحت أي ظرف من الظروف  
#            - إذا تم تعديل هذا الكود، فإن المالك لا يتحمل أي مسؤولية عن الأضرار أو الأخطاء الناتجة عن الكود المعدل  
#     - لا تقم بإعادة بيع هذه الأداة، ولا تنسبها إلى نفسك  

from Config.Utilities import *
from Config.Configuration import *
try:
    import requests
    from bs4 import BeautifulSoup
    import re
    import time
except Exception as e:
   ErrorModule(e)

Title("Username Tracker")

try:
    sites = {
        "Roblox Trade": "https://rblx.trade/p/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Instagram": "https://www.instagram.com/{}",
        "Paypal": "https://www.paypal.com/paypalme/{}",
        "GitHub": "https://github.com/{}",
        "Giters": "https://giters.com/{}",
        "Pinterest": "https://www.pinterest.com/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "Telegram": "https://t.me/{}",
        "Steam": "https://steamcommunity.com/id/{}",
        "Blogger": "https://{}.blogspot.com",
        "Tumblr": "https://{}.tumblr.com",
        "SoundCloud": "https://soundcloud.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "About.me": "https://about.me/{}",
        "Flickr": "https://www.flickr.com/people/{}",
        "Keybase": "https://keybase.io/{}",
        "Last.fm": "https://www.last.fm/user/{}",
        "Behance": "https://www.behance.net/{}",
        "Quora": "https://www.quora.com/profile/{}",
        "Patreon": "https://www.patreon.com/{}",
        "Myspace": "https://myspace.com/{}",
        "Kaggle": "https://www.kaggle.com/{}",
        "Periscope": "https://www.pscp.tv/{}",
        "Disqus": "https://disqus.com/by/{}",
        "Mastodon": "https://mastodon.social/@{}",
        "GitLab": "https://gitlab.com/{}",
        "Giphy": "https://giphy.com/{}",
        "LiveJournal": "https://{}.livejournal.com",
        "CodeWars": "https://www.codewars.com/users/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Spotify": "https://open.spotify.com/user/{}",
        "Weebly": "https://{}.weebly.com",
        "YouTube": "https://www.youtube.com/{}",
        "ProductHunt": "https://www.producthunt.com/@{}",
        "Mix": "https://mix.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Strava": "https://www.strava.com/athletes/{}",

        "Internet Archive": "https://archive.org/search?query={}",
        "Twitter Archive": "https://web.archive.org/web/*/https://twitter.com/{}/status/*",
        "Linktree": "https://linktr.ee/{}",
        "Xbox": "https://www.xboxgamertag.com/search/{}",
        "Twitter": "https://twitter.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "Goodreads": "https://www.goodreads.com/{}",
        "VK": "https://vk.com/{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Dribbble": "https://dribbble.com/{}",
        "AngelList": "https://angel.co/{}",
        "500px": "https://500px.com/{}",
        "LinkedIn": "https://www.linkedin.com/in/{}",
        "WhatsApp": "https://wa.me/{}",
        "Discord": "https://discord.com/users/{}",
        "Weibo": "https://weibo.com/{}",
        "OKCupid": "https://www.okcupid.com/profile/{}",
        "Meetup": "https://www.meetup.com/members/{}",
        "CodePen": "https://codepen.io/{}",
        "StackOverflow": "https://stackoverflow.com/users/{}",
        "HackerRank": "https://www.hackerrank.com/{}",
        "Xing": "https://www.xing.com/profile/{}",
        "Deezer": "https://www.deezer.com/en/user/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "Tidal": "https://tidal.com/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Ravelry": "https://www.ravelry.com/people/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Vine": "https://vine.co/u/{}",
        "Foursquare": "https://foursquare.com/user/{}",  
        "Ello": "https://ello.co/{}",
        "Hootsuite": "https://hootsuite.com/{}",
        "Prezi": "https://prezi.com/{}",
        "Groupon": "https://www.groupon.com/profile/{}",
        "Liveleak": "https://www.liveleak.com/c/{}",
        "Joomla": "https://www.joomla.org/user/{}",
        "StackExchange": "https://stackexchange.com/users/{}",
        "Taringa": "https://www.taringa.net/{}",
        "Shopify": "https://{}.myshopify.com",
        "8tracks": "https://8tracks.com/{}",
        "Couchsurfing": "https://www.couchsurfing.com/people/{}",
        "OpenSea": "https://opensea.io/{}",
        "Trello": "https://trello.com/{}",
        "Fiverr": "https://www.fiverr.com/{}",
        "Badoo": "https://badoo.com/profile/{}",
        "Rumble": "https://rumble.com/user/{}",
        "Wix": "https://www.wix.com/website/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "ReverbNation": "https://www.reverbnation.com/{}",
        "Gumroad": "https://gumroad.com/{}",
        "Dailymotion": "https://www.dailymotion.com/{}",
        "Vimeo": "https://vimeo.com/{}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{}",
        "Snapfish": "https://www.snapfish.com/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
        "VK": "https://vk.com/{}",
    }

    def SiteException(username, site, page_content):
        if site == "Paypal":
            page_content = page_content.replace(f'slug_name={username}', '').replace(f'"slug":"{username}"', '').replace(f'2F{username}&amp', '')
        elif site == "TikTok":
            page_content = page_content.replace(f'\\u002f@{username}"', '')
        return page_content

    number_site = 0
    number_found = 0
    sites_and_urls_found = []

    Slow(osint_banner)
    username = input(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Username -> {reset}")
    Censored(username)

    username = username.lower()

    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Scanning..")

    session = requests.Session()

    for site, url_template in sites.items():
        try:
            number_site += 1
            url = url_template.format(username)
            try:
                response = session.get(url, timeout=3)
                if response.status_code == 200:
                    page_content = re.sub(r'<[^>]*>', '', response.text.lower().replace(url, "").replace(f"/{username}", ""))
                    page_content = SiteException(username, site, page_content)

                    soup = BeautifulSoup(response.text, 'html.parser')
                    page_text = soup.get_text().lower().replace(url, "")
                    page_title = soup.title.string.lower() if soup.title else ""

                    found = username in page_title or username in page_content or username in page_text

                    if found:
                        number_found += 1
                        sites_and_urls_found.append(f"{site}: {white + url}")
                        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {GEN_VALID} {site}: {white + url}")
                    else:
                        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {GEN_INVALID} {site}:{white} Not Found")

                else: 
                    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {GEN_INVALID} {site}:{white} Not Found")

            except Exception as e:
                print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ERROR} {site}: {white + e}")
        except:
            pass

    print(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INFO} Total Found:{reset}")
    for site_and_url_found in sites_and_urls_found:
        time.sleep(0.5)
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} {site_and_url_found}")

    print(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INFO} Total Website: {white}{number_site}{cyan} Total Found: {white}{number_found}{cyan}")
    Continue()
    Reset()

except Exception as e:
    Error(e)