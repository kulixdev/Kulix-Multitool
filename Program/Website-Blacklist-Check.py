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

Title("Blacklist Check")

try:
    import dns.resolver
    import socket
except Exception as e:
    ErrorModule(e)

blacklist_services = {
    "zen.spamhaus.org": {"method": "reverse", "query": "{reversed_domain}.zen.spamhaus.org"},  # Spamhaus
    "bl.spamcop.net": {"method": "reverse", "query": "{reversed_domain}.bl.spamcop.net"},  # SpamCop
    "b.barracudacentral.org": {"method": "reverse", "query": "{reversed_domain}.b.barracudacentral.org"},  # Barracuda
    "dnsbl.sorbs.net": {"method": "reverse", "query": "{reversed_domain}.dnsbl.sorbs.net"},  # SORBS
    "multi.surbl.org": {"method": "reverse", "query": "{reversed_domain}.multi.surbl.org"},  # SURBL
    "ivmURI": {"method": "reverse", "query": "{reversed_domain}.ivmURI"},  # ivmURI
    "nordspam.dbl": {"method": "reverse", "query": "{reversed_domain}.nordspam.dbl"},  # Nordspam DBL
    "spamhaus.dbl": {"method": "reverse", "query": "{reversed_domain}.spamhaus.dbl"},  # Spamhaus DBL
    "0spam.dbl": {"method": "reverse", "query": "{reversed_domain}.0spam.dbl"},  # 0SPAM
    "backscatterer.org": {"method": "reverse", "query": "{reversed_domain}.backscatterer.org"},  # BACKSCATTERER
    "psbl.dnsbl": {"method": "reverse", "query": "{reversed_domain}.psbl.dnsbl"},  # PSBL
    "spamcop.dnsbl": {"method": "reverse", "query": "{reversed_domain}.spamcop.dnsbl"},  # SPAMCOP
    "uceprotect1.dnsbl": {"method": "reverse", "query": "{reversed_domain}.uceprotect1.dnsbl"},  # UCEPROTECTL1
    "uceprotect2.dnsbl": {"method": "reverse", "query": "{reversed_domain}.uceprotect2.dnsbl"},  # UCEPROTECTL2
    "uceprotect3.dnsbl": {"method": "reverse", "query": "{reversed_domain}.uceprotect3.dnsbl"},  # UCEPROTECTL3
    "zapbl.dnsbl": {"method": "reverse", "query": "{reversed_domain}.zapbl.dnsbl"},  # ZapBL
    "kisa.dnsbl": {"method": "reverse", "query": "{reversed_domain}.kisa.dnsbl"},  # KISA
    "list.dsbl.org": {"method": "reverse", "query": "{reversed_domain}.list.dsbl.org"},  # DSBL
    "bl.spamrbl.com": {"method": "reverse", "query": "{reversed_domain}.bl.spamrbl.com"},  # SpamRBL
    "dnsbl.inps.de": {"method": "reverse", "query": "{reversed_domain}.dnsbl.inps.de"},  # INPS
    "blackholes.five-ten-sg.com": {"method": "reverse", "query": "{reversed_domain}.blackholes.five-ten-sg.com"},  # FiveTenSG
    "ivmSIP": {"method": "reverse", "query": "{reversed_domain}.ivmSIP"},  # ivmSIP
    "ivmSIP24": {"method": "reverse", "query": "{reversed_domain}.ivmSIP24"},  # ivmSIP24
    "JIPPG": {"method": "reverse", "query": "{reversed_domain}.JIPPG"},  # JIPPG
    "KEMPTBL": {"method": "reverse", "query": "{reversed_domain}.KEMPTBL"},  # KEMPTBL
    "Konstant": {"method": "reverse", "query": "{reversed_domain}.Konstant"},  # Konstant
    "LASHBACK": {"method": "reverse", "query": "{reversed_domain}.LASHBACK"},  # LASHBACK
    "MAILSPIKE BL": {"method": "reverse", "query": "{reversed_domain}.MAILSPIKE BL"},  # MAILSPIKE BL
    "MAILSPIKE Z": {"method": "reverse", "query": "{reversed_domain}.MAILSPIKE Z"},  # MAILSPIKE Z
    "MSRBL Phishing": {"method": "reverse", "query": "{reversed_domain}.MSRBL Phishing"},  # MSRBL Phishing
    "MSRBL Spam": {"method": "reverse", "query": "{reversed_domain}.MSRBL Spam"},  # MSRBL Spam
    "NETHERRELAYS": {"method": "reverse", "query": "{reversed_domain}.NETHERRELAYS"},  # NETHERRELAYS
    "NETHERUNSURE": {"method": "reverse", "query": "{reversed_domain}.NETHERUNSURE"},  # NETHERUNSURE
    "NIXSPAM": {"method": "reverse", "query": "{reversed_domain}.NIXSPAM"},  # NIXSPAM
    "Nordspam BL": {"method": "reverse", "query": "{reversed_domain}.Nordspam BL"},  # Nordspam BL
    "RATS Dyna": {"method": "reverse", "query": "{reversed_domain}.RATS Dyna"},  # RATS Dyna
    "RATS NoPtr": {"method": "reverse", "query": "{reversed_domain}.RATS NoPtr"},  # RATS NoPtr
    "RATS Spam": {"method": "reverse", "query": "{reversed_domain}.RATS Spam"},  # RATS Spam
    "RBL JP": {"method": "reverse", "query": "{reversed_domain}.RBL JP"},  # RBL JP
    "s5h.net": {"method": "reverse", "query": "{reversed_domain}.s5h.net"},  # s5h.net
    "SCHULTE": {"method": "reverse", "query": "{reversed_domain}.SCHULTE"},  # SCHULTE
    "SEM BACKSCATTER": {"method": "reverse", "query": "{reversed_domain}.SEM BACKSCATTER"},  # SEM BACKSCATTER
    "SEM BLACK": {"method": "reverse", "query": "{reversed_domain}.SEM BLACK"},  # SEM BLACK
    "Sender Score Reputation Network": {"method": "reverse", "query": "{reversed_domain}.Sender Score Reputation Network"},  # Sender Score Reputation Network
    "SERVICESNET": {"method": "reverse", "query": "{reversed_domain}.SERVICESNET"},  # SERVICESNET
    "Spamhaus ZEN": {"method": "reverse", "query": "{reversed_domain}.Spamhaus ZEN"},  # Spamhaus ZEN
    "SPFBL DNSBL": {"method": "reverse", "query": "{reversed_domain}.SPFBL DNSBL"},  # SPFBL DNSBL
    "Suomispam Reputation": {"method": "reverse", "query": "{reversed_domain}.Suomispam Reputation"},  # Suomispam Reputation
    "SWINOG": {"method": "reverse", "query": "{reversed_domain}.SWINOG"},  # SWINOG
    "TRIUMF": {"method": "reverse", "query": "{reversed_domain}.TRIUMF"},  # TRIUMF
    "TRUNCATE": {"method": "reverse", "query": "{reversed_domain}.TRUNCATE"},  # TRUNCATE
    "UCEPROTECTL1": {"method": "reverse", "query": "{reversed_domain}.UCEPROTECTL1"},  # UCEPROTECTL1
    "UCEPROTECTL2": {"method": "reverse", "query": "{reversed_domain}.UCEPROTECTL2"},  # UCEPROTECTL2
    "UCEPROTECTL3": {"method": "reverse", "query": "{reversed_domain}.UCEPROTECTL3"},  # UCEPROTECTL3
    "Woodys SMTP Blacklist": {"method": "reverse", "query": "{reversed_domain}.Woodys SMTP Blacklist"},  # Woodys SMTP Blacklist
    "ZapBL": {"method": "reverse", "query": "{reversed_domain}.ZapBL"},  # ZapBL
    "KISA": {"method": "reverse", "query": "{reversed_domain}.KISA"},  # KISA
    "NoSolicitado": {"method": "reverse", "query": "{reversed_domain}.NoSolicitado"}  # NoSolicitado
}

def BlacklistLookup(mx_domain):
    blacklisted = []
    not_blacklisted = []
    reversed_domain = '.'.join(reversed(mx_domain.split('.')))
    
    for blacklist, details in blacklist_services.items():
        try:
            blacklist_query = details["query"].format(reversed_domain=reversed_domain)
            dns.resolver.resolve(blacklist_query, 'A')
            blacklisted.append(blacklist)
        except (dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.exception.DNSException) as e:
            not_blacklisted.append(blacklist)
    
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Blacklist Lookup for {mx_domain}:")
    
    if blacklisted:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ERROR} {mx_domain} is blacklisted in the following blacklists:")
        for i, blacklist in enumerate(blacklisted, start=1):
            if i == len(blacklisted):
                print(f"└─── {white}{blacklist}{cyan}")
            else:
                print(f"├─── {white}{blacklist}{cyan}")
    elif not blacklisted:
        print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {ADD} No blacklists detected for {mx_domain}")

Slow(scan_banner)
domain = input(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Domain Name -> {reset}")
Censored(domain)

BlacklistLookup(domain)
Continue()
Reset()
