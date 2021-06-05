#!/usr/bin/python2

#coding=utf-8

#The Credit For This Code Goes To lovehacker

#If You Wanna Take Credits For This Code, Please Look Yourself Again...

#Reserved2020

import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib

from multiprocessing.pool import ThreadPool

####  RANDOM Clour ####

P  = '\033[1;97m'  #

M  = '\033[1;91m' #

H  = '\033[1;92m' #

K = '\033[1;93m' #

B  = '\033[1;94m' #

U  = '\033[1;95m' #

O = '\033[1;96m' #

my_color = [P, M, H, K, B, U, O]

warna = random.choice(my_color)

warni = random.choice(my_color)

def pkgs():

        love("\033[1;91m«-----------------\033[1;96mSHABIR BALOCH\033[1;91m-----------------»")

        love("\033[1;96m«-----------------Disclaimer---------------»")

        love("\033[1;91m     This Tool is for Educational Purpose")

        love("\033[1;93mThis presentation is for educational")

        love("\033[1;93mpurposes ONLY.How you use this information")

        love("\033[1;93mis your responsibility.I will not be")

        love("\033[1;93mheld accountable This Tool/Channel Doesn't")

        love("\033[1;93mSupport illegal activities.for any illegal")

        love("\033[1;93mActivitie This Tool is for Educational Purpose")

        love("\033[1;91m«------------------SHABIR BALOCH----------------»")

        love("\033[1;95mB4Baloch 2nd Tool Start ComingSoon New Update»")

        love("\033[1;96m «-----------------\033[1;92mSHABIR BALOCH\033[1;96m--------------»")

        time.sleep(0.3)

        os.system("pip install lolcat")

try:

        import mechanize

except ImportError:

        os.system("pip2 install mechanize")

try:

        import requests

except ImportError:

        os.system("pip2 install requests")

        os.system("python2 Cloning.py")

from requests.exceptions import ConnectionError

from mechanize import Browser

from datetime import datetime

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")

done = False

def animate():

    for c in itertools.cycle(['\033[1;96m|', '\033[1;92m/', '\033[1;95m-', '\033[1;91m\\']):

        if done:

            break

        sys.stdout.write('\r\033[1;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )

        sys.stdout.flush()

        time.sleep(0.001)

t = threading.Thread(target=animate)

t.start()

time.sleep(5)

done = True

def keluar():

        print "\033[1;97m{\033[1;91m!\033[1;97m} Keluar"

        os.sys.exit()

def acak(x):

    w = 'mhkbpcP'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(x):

    w = 'mhkbpcP'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'%s;'%str(31+j))

    x += ''

    x = x.replace('!0','')

    sys.stdout.write(x+'\n')

def jalan(z):

        for e in z + '\n':

                sys.stdout.write(e)

                sys.stdout.flush()

                time.sleep(0.00001)

##### LOGO #####

logo = """

\033[1;96mPAK HACKERS░░░\033[1;92m░░░SHABIRBALOCH╗░░WEBDEVELOPER╗░AND╗░░A\033[1;91mETICALHACKER╗

\033[1;96mYT╔══M4╗B4║░\033[1;92m░░░░WEBHACKER╔══PAK╗ANONAYMOUS╔══YOUTUBE╗CHANNEL║\033[1;91m░B4_BALOCH_M4_MASTER╔╝

\033[1;96mPAKISTANI╦╝HACKERS\033[1;92m║░░░░░███████║██║░░╚═╝\033[1;91m█████═╝░

\033[1;96mWEBHACKER╔══SHABIRBALOCH╗\033[1;92m██║░░░░░██╔══██║██║░░\033[1;91m██╗██╔═██╗░

\033[1;96mWHATSAPP\033[1;92m╦╝03232132362╗██║░░██║╚█\033[1;91m████╔╝██║░╚██╗

\033[1;96m╚═══\033[1;92m══╝░╚══════╝╚═╝░░╚═╝\033[1;91m░╚════╝░╚═╝░░╚═╝

\033[1;96mHACK\033[1;92mTHE╗░░░HACKERS╗░BALOCH╗░HACKERS\033[1;91m████╗██╗░█████╗░

\033[1;96mWE\033[1;92mARE╗░LEGION║WE╔══NEVER╗\033[1;91mFORGIVE╔════╝SPEED█║LIMIT█╔══INCREASED█╗

\033[1;92mVISIT╔█OUR█╔YT║█CHANNEL█\033[1;91mB4║█BALOCH█╗░░M4║██MASTER██║

\033[1;92m██║╚██╔╝██║██╔\033[1;91m══██║██╔══╝░░██║██╔══██║

\033[1;92m██║░╚═╝░██║█\033[1;91m█║░░██║██║░░░░░██║██║░░██║

\033[1;92m╚═╝░░░░░╚═\033[1;91m╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝

\033[1;47m\033[1;31m      PAKISTANI HACKER       \033[1;0m

\033[1;96m«-----------------\033[1;91mSHABIR BALOCH\033[1;96m-----------------»

\033[1;91m  ┈┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈┈┈  BALOCH

\033[1;91m  ┈┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈┈┈  HACKER

\033[1;91m  ┈┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈┈┈

\033[1;91m  ┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈┈   WhatsApp

\033[1;91m  ┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈ 03232132362

\033[1;96m«-----------------\033[1;91mSHABIR BALOCH\033[1;96m-----------------»"""

R = '\033[1;91m'

G = '\033[1;92m'

Y = '\033[1;93m'

B = '\033[1;94m'

P = '\033[1;95m'

S = '\033[1;96m'

W = '\033[1;97m'

######Clear######

def clear():

    os.system('clear')

#### time sleep ####

def t():

    time.sleep(1)                             

def t1():                                         

    time.sleep(0.01)

#### print std #love###

def love(z):

        for e in z + "\n":

                sys.stdout.write(e)

                sys.stdout.flush()

                t1()

def menu():

    os.system('clear')

    pkgs()

    os.system('clear')

    print(logo)

    os.system('clear')

    os.system('echo  SHABIR░░░░░░BALOCH░░PAKISTANI░ETICAL░░HACKER | lolcat -a -F 0.1')

    os.system('echo  SHABIR░░░░░BALOCH██WEB██DEVELOPER░██ | lolcat -a -F 0.1')

    os.system('echo  WHATSAPP░░░░░03232132362░░FOR THIS SCRIPT░ | lolcat -a -F 0.1')

    os.system('echo  CONTACT  ░░░░░ME ON WHATSAPP░░BALOCH CYBER HACKER░ | lolcat -a -F 0.1')

    os.system('echo  WE ARE ░░ANONAYMOUS░WE ARE LEGION WE NEVER GORFIVE | lolcat -a -F 0.1')

    os.system('echo  WE NEVER FORGET░ASPECT ░░ US ░KNOWLEDGE░IS░░FREE | lolcat -a -F 0.1')

    os.system('echo  HI, I AM SHABIR BALOCH A ETICAL HACKER | lolcat -a -F 0.1')

    os.system('echo  WE ARE ANONYMOUS WE ARE LEGION WE NEVER FORGIVE WE NEVER FORGET ASPECT US | lolcat -a -F 0.1')

    os.system('echo  SHABIR BALOCH WHATSAPP = 03232132362 | lolcat -a -F 0.1')

    os.system('echo  VISIT OUR YOUTUBE CHANNEL B4 BALOCH M4 MASTER | lolcat -a -F 0.1')

    os.system('echo  PAKISTANI ETICAL HACKER AND A PROGRAMMER | lolcat -a -F 0.1')

    os.system('echo  LETS░░░░░ENJOY░░OUR░░░░░TOOL░░THANKS | lolcat -a -F 0.1')

    os.system('echo  ------ Your Mind is Your Best Weapon------&&date  | lolcat -a -F 0.1')

    os.system('echo ----------------SHABIR BALOCH-----------------| lolcat')

    os.system('echo  ┈┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈┈┈  SHABIR BALOCH| lolcat --animate')

    os.system('echo  ┈┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈┈┈  BALOCHHACKER| lolcat --animate')

    os.system('echo  ┈┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈┈┈| lolcat')

    os.system('echo  ┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈┈   WhatsApp| lolcat --animate')

    os.system('echo  ┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈03232132362| lolcat --animate')

    os.system('echo -----------------SHABIR BALOCH----------------| lolcat --animate')

    os.system('echo    To return to this menu from any Tool| lolcat --animate')

    time.sleep(0.0005)

    os.system('echo        Stop Process Press. CTRL + z| lolcat --animate')

    time.sleep(0.0005)

    os.system('echo         Type python2 B4BALOCH.py| lolcat --animate')

    os.system('echo -----------------SHABIR BALOCH----------------| lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [A]  Install Random Mail Cloning--------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [B]  Install Email Cloning--------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [C]  Install Manual Password------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [D]  Install Group Cloning--------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [E]  Install With Out Fb Id-------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [F]  Install Facebook Target------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [G]  Install SpiderMan------------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [H]  Install Kalilinux------------------------- Tool ----●  | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [I]  Install BlackHat-------------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [J]  Install RedMoonNew------------------------ Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [K]  Install love3Hack3r----------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [L]  Install B4 BALOCH Clonnig----------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [M]  Install Web Admin Panel Finder------------ Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [N]  Install Attacker-------------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [O]  Install Payload--------------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [P]  Install CamHacker------------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [Q]  Install Compiler-------------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [R]  Install Instagram Brut-------------------- Tool ----● | lolcat --animate')

    time.sleep(0.0005)

    os.system('echo [S]  Install Marsh Base------------------------ Tool ----● | lolcat --animate')

    time.sleep(0.0005)

   
