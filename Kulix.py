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

from Program.Config.Configuration import *
from Program.Config.Utilities import *

option_01 = "Website-Vulnerability-Scanner"
option_02 = "Website-Info-Scanner"
option_03 = "Website-Url-Scanner"
option_04 = "Ip-Scanner"
option_05 = "Ip-Port-Scanner"
option_06 = "Ip-Pinger"
option_07 = "Ip-Traceroute"
option_08 = "Netstat-Viewer"
option_09 = "Bandwidth-Test"
option_10 = "Subnet-Calculator"
option_11 = "Network-Vulnerability-Scanner"

option_12 = "Username-Lookup"
option_13 = "Email-Tracker"
option_14 = "Email-Lookup"
option_15 = "Phone-Number-Lookup"
option_16 = "Ip-Lookup"

option_17 = "Launch-Putty"
option_18 = "Launch-Wireshark"
option_19 = "Launch-Stratoshark"
option_20 = "Launch-SystemInformer"
option_21 = "Launch-VirtualBox"
option_22 = "Launch-AdvancedIPScanner"

option_23 = "Who-Is-Lookup"
option_24 = "Website-MX-Lookup"
option_25 = "Website-Blacklist-Check"
option_26 = "Website-Record-Lookup"
option_27 = "Website-Reverse-Lookup"
option_28 = "Website-DKIM-Lookup"
option_29 = "Website-DMARC-Lookup"
option_30 = "Test-Email-Server"
option_31 = "Website-SSL-Check"

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

option_back_txt = option_back + f" {cyan}[{white}B{cyan}]{white}"
option_next_txt = option_next + f" {cyan}[{white}N{cyan}]{white}"
option_info_txt =  f"{cyan}[{white}I{cyan}]{white} " + option_info

menu1 = f"""                                                                                                          {option_next_txt} ─┐
 ┌─ {option_info_txt} ┌───────────────┐                          ┌───────┐                           ┌──────────┐            │
 └─┬─────────┤ Network Tools ├───────────┬──────────────┤ OSINT ├──────────────┬────────────┤ Programs ├────────────┴─
   │         └───────────────┘           │              └───────┘              │            └──────────┘
   ├─ {option_01_txt                   }├─ {option_12_txt                    }├─ {option_17_txt                    }
   ├─ {option_02_txt                   }├─ {option_13_txt                    }├─ {option_18_txt                    }
   ├─ {option_03_txt                   }├─ {option_14_txt                    }├─ {option_19_txt                    }
   ├─ {option_04_txt                   }├─ {option_15_txt                    }├─ {option_20_txt                    }
   ├─ {option_05_txt                   }└─ {option_16_txt                    }├─ {option_21_txt                    }
   ├─ {option_06_txt                   }                                      └─ {option_22_txt                    }
   ├─ {option_07_txt                   }
   ├─ {option_08_txt                   }
   ├─ {option_09_txt                   }
   ├─ {option_10_txt                   }
   └─ {option_11_txt                   }
"""

menu2 = f"""                                                                             {option_next_txt} ─┐
 ┌─ {option_info_txt}  ┌───────────────┐              ┌───────┐          ┌───────┐    {option_back_txt} ─┤
─┴─┬──────────┤ Website Tools ├──────────┬───┤ Empty ├──────┬───┤ Empty ├──────────────┴─
   │          └───────────────┘          │   └───────┘      │   └───────┘
   ├─ {option_23_txt                           }├─ Lorem Ipsum     ├─ Lorem Ipsum
   ├─ {option_24_txt                           }├─ Lorem Ipsum     ├─ Lorem Ipsum
   ├─ {option_25_txt                           }└─ Lorem Ipsum     ├─ Lorem Ipsum
   ├─ {option_26_txt                           }                   └─ Lorem Ipsum
   ├─ {option_27_txt                           }
   ├─ {option_28_txt                           }
   ├─ {option_29_txt                           }
   ├─ {option_30_txt                           }
   └─ {option_31_txt                           }
"""

menu_path = os.path.join(tool_path, "Program", "Config", "Menu.txt")

def Menu():

   try:
      with open(menu_path, "r") as file:
         menu_number = file.read()
      menu_mapping = {"1": menu1, "2": menu2}
      menu = menu_mapping.get(menu_number, menu1)
   except:
      menu = menu1
      menu_number = "1"

   banner = f"""                                                                                     
                                ██║ ██╔╝██║   ██║██║     ██║╚██╗██╔╝    ██║   ██║███║
                                █████╔╝ ██║   ██║██║     ██║ ╚███╔╝     ██║   ██║╚██║
                                ██╔═██╗ ██║   ██║██║     ██║ ██╔██╗     ╚██╗ ██╔╝ ██║
                                ██║  ██╗╚██████╔╝███████╗██║██╔╝ ██╗     ╚████╔╝  ██║
                                ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝      ╚═══╝   ╚═╝
{menu}"""
   return banner, menu_number

while True:
   try:
      Clear()

      banner, menu_number = Menu()

      Title(f"Menu {menu_number}")
      Slow(MainColor(banner))

      choice = input(MainColor(f""" ┌──({white}{username_pc}@kulix)─{cyan}[{white}~/{os_name}/Menu-{menu_number}]
 └─{white}$ {reset}"""))

      if choice in ['N', 'n', 'NEXT', 'Next', 'next']:
            menu_number = {"1": "2", "2": "1"}.get(menu_number, "1")
            with open(menu_path, "w") as file:
               file.write(menu_number)
            continue

      elif choice in ['B', 'b', 'BACK', 'Back', 'back']:
            menu_number = {"2": "1"}.get(menu_number, "1")
            with open(menu_path, "w") as file:
               file.write(menu_number)
            continue

      elif choice in ['I', 'i', 'INFO', 'Info', 'info']:
            StartProgram(f"{option_info}.py")
            continue

      options = {
         '01': option_01, '02': option_02, '03': option_03, '04': option_04,
         '05': option_05, '06': option_06, '07': option_07, '08': option_08,
         '09': option_09, '10': option_10, '11': option_11, '12': option_12,
         '13': option_13, '14': option_14, '15': option_15, '16': option_16,
         '17': option_17, '18': option_18, '19': option_19, '20': option_20,
         '21': option_21, '22': option_22, '23': option_23, '24': option_24,
         '25': option_25, '26': option_26, '27': option_27, '28': option_28,
         '29': option_29, '30': option_30, '31': option_31
      }

      if choice in options:  
         StartProgram(f"{options[choice]}.py")
      elif '0' + choice in options:
         StartProgram(f"{options['0' + choice]}.py")
      else:
         ErrorChoiceStart()

   except KeyboardInterrupt:
      Clear()
      Title("Interruptted")
      print(f"{BEFORE_CYAN + current_time_hour() + AFTER_CYAN} {WAIT} You cannot KeyboardInterrupt this MultiTool, please close it if you wish to exit" + reset)
      Continue()
      Reset()

   except Exception as e:
      Error(e)
