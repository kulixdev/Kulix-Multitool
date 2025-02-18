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