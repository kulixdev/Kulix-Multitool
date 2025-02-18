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
   import dns.resolver
   import requests
   import re
except Exception as e:
   ErrorModule(e)

Title("Email Lookup")

try:
    def get_email_info(email):
        info = {}
        try: domain_all = email.split('@')[-1]
        except: domain_all = None

        try: name = email.split('@')[0]
        except: name = None

        try: domain = re.search(r"@([^@.]+)\.", email).group(1)
        except: domain = None
        try: tld = f".{email.split('.')[-1]}"
        except: tld = None

        try: 
            mx_records = dns.resolver.resolve(domain_all, 'MX')
            mx_servers = [str(record.exchange) for record in mx_records]
            info["mx_servers"] = mx_servers
        except dns.resolver.NoAnswer:
            info["mx_servers"] = None
        except dns.resolver.NXDOMAIN:
            info["mx_servers"] = None


        try:
            spf_records = dns.resolver.resolve(domain_all, 'SPF')
            info["spf_records"] = [str(record) for record in spf_records]
        except dns.resolver.NoAnswer:
            info["spf_records"] = None
        except dns.resolver.NXDOMAIN:
            info["spf_records"] = None

        try:
            dmarc_records = dns.resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
            info["dmarc_records"] = [str(record) for record in dmarc_records]
        except dns.resolver.NoAnswer:
            info["dmarc_records"] = None
        except dns.resolver.NXDOMAIN:
            info["dmarc_records"] = None

        if mx_servers:
            for server in mx_servers:
                if "google.com" in server:
                    info["google_workspace"] = True
                elif "outlook.com" in server:
                    info["microsoft_365"] = True

        return info, domain_all, domain, tld, name

    email = input(f"\n{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {INPUT} Email -> {reset}")
    Censored(email)
        
    print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} Information Recovery..{reset}")
    info, domain_all, domain, tld, name = get_email_info(email)

    try:
        mx_servers = info["mx_servers"]
        mx_servers = ' / '.join(mx_servers)
    except Exception as e:
        mx_servers = None

    try:
        spf_records = info["spf_records"]
    except:
        spf_records = None

    try:
        dmarc_records = info["dmarc_records"]
        dmarc_records = ' / '.join(dmarc_records)
    except:
        dmarc_records = None

    try:
        google_workspace = info["google_workspace"]
    except:
        google_workspace = None

    try:
        mailgun_validation = info["mailgun_validation"]
        mailgun_validation = ' / '.join(mailgun_validation)
    except:
        mailgun_validation = None

    print(f"""
    {INFO_ADD} Email      : {white}{email}{cyan}
    {INFO_ADD} Name       : {white}{name}{cyan}
    {INFO_ADD} Domain     : {white}{domain}{cyan}
    {INFO_ADD} Tld        : {white}{tld}{cyan}
    {INFO_ADD} Domain All : {white}{domain_all}{cyan}
    {INFO_ADD} Servers    : {white}{mx_servers}{cyan}
    {INFO_ADD} Spf        : {white}{spf_records}{cyan}
    {INFO_ADD} Dmarc      : {white}{dmarc_records}{cyan}
    {INFO_ADD} Workspace  : {white}{google_workspace}{cyan}
    {INFO_ADD} Mailgun    : {white}{mailgun_validation}{cyan}
    {color.RESET}""")

    Continue()
    Reset()
except Exception as e:
    Error(e)