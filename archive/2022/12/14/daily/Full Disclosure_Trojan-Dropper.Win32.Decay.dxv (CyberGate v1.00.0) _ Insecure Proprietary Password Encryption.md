---
title: Trojan-Dropper.Win32.Decay.dxv (CyberGate v1.00.0) / Insecure Proprietary Password Encryption
url: https://seclists.org/fulldisclosure/2022/Dec/14
source: Full Disclosure
date: 2022-12-14
fetch_date: 2025-10-04T01:28:42.551205
---

# Trojan-Dropper.Win32.Decay.dxv (CyberGate v1.00.0) / Insecure Proprietary Password Encryption

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# Trojan-Dropper.Win32.Decay.dxv (CyberGate v1.00.0) / Insecure Proprietary Password Encryption

---

*From*: malvuln <malvuln13 () gmail com>
*Date*: Sun, 11 Dec 2022 19:45:40 -0500

---

```
Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source:
https://malvuln.com/advisory/618f28253d1268132a9f10819a6947f2.txt
Contact: malvuln13 () gmail com
Media: twitter.com/malvuln
Backup media: infosec.exchange/@malvuln

Threat: Trojan-Dropper.Win32.Decay.dxv (CyberGate v1.00.0)
Vulnerability: Insecure Proprietary Password Encryption
Family: CyberGate
Type: PE32
MD5: 618f28253d1268132a9f10819a6947f2
Vuln ID: MVID-2022-0664
Disclosure: 12/11/2022
Description: This well known RAT malware stores credentials using a
proprietary insecure encryption routine in its "Settings.ini" file. The
recovery procedure is trivial to decrypt stored credentials. theres no key,
xor or combined encrypt mechanism and relies on basic SUB, ADD and bitwise
operations SHR and SHL. Analysis of the following single encrypted
character table reveal the pattern 0,G,W,m that repeats every few
alpha-numeric characters a-c, d-g, h-k etc...

E.g.

a=OG
b=OW
c=Om
d=P0
e=PG
f=PW
g=Pm
h=Q0
i=QG
j=QW
k=Qm
l=R0
m=RG
n=RW
o=Rm
p=S0
q=SG
r=SW
s=Sm
t=T0
u=TG
v=TW
w=Tm
x=U0
y=UG
z=UW

"Settings.ini"
senhaconexao=OM9Z

For example, the password "abc" is stored as "OM9Z", in order to recover
the first character we need only perform the following bitwise operations
SUB, ADD, SHR and SHL.

OM9Z = "abc"

To recover the first password character, use the first two stored values
"OM" which will return the ascii value "a".

key="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

get 'a'

 b="PQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
 eax = len(key) - len(b)
 eax
25
 ebx = eax -1
 ebx
24
 b="NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
 ecx = len(key) - len(b)
 ecx
23
 edx = ecx -1
 edx
22
 ebx << 6
1536
 hex(1536)
'0x600'
 hex(22)
'0x16'
 0x600 + 0x16
1558
 hex(1558)
'0x616'
 0x616 >> 4
97
 hex(97)
'0x61'

61 = 'a'

PoC Video:
https://www.youtube.com/watch?v=PAkKo2dLGwQ

Exploit/PoC:
"CyberGate_Trojan_Decryptor.py"

import argparse, sys, time, os, atexit
from operator import *

#CyberGate v1.00.0 - Insecure Proprietary Password Encryption
#=========================================================================
#Basic password decryptor for the following RAT malwares:
#
#Trojan-Dropper.Win32.Decay.dxv (CyberGate v1.00.0)
#MD5: 618f28253d1268132a9f10819a6947f2
#
#Spy-Net 2.7 Beta 02 - Backdoor.Win32.Shpinat.a
#MD5: eaf37e9506ef76f6d26838692d76aabd
#
#By John Page (aka hyp3rlinx) Copyright (C) circa 2022
#malvuln.com
#malvuln13 () gmail com
#twitter.com/malvuln
#=========================================================================
#
#PoC to decrypt credentials due to flawed proprietary encryption.
#RAT password save usage:
#Click 'START' / Options then choose 'Select listening ports' from menu.
#Enter a new password in the 'Connection Password' field and click save.
#Password gets stored in 'Settings.ini' file.
#
#Note: Should recover most numeric and or lowercase passwords. May return
#multiple password candidates depending on the password recovered.
#Some limitation with long and or complex passwords, did not put much time
on it!
#
#TODO: Better handle complex long mixed letters and or repeating characters.
#Author is NOT responsible for any misuse or incorrect password recovery,
#the user accepts ALL risk by using the software.
#
#MIT License - Copyright (c) 2022 malvuln
#Permission is hereby granted, free of charge, to any person obtaining a
copy
#of this software and associated documentation files (the "Software"), to
deal
#in the Software without restriction, including without limitation the
rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
all
#copies or substantial portions of the Software.
#
#DISCLAIMER:
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

#Permission is also explicitly given for insertion in vulnerability
databases and similar,
#provided that due credit is given to the author:
#John Page (aka malvuln/hyp3rlinx) Copyright (C)(TM) 2022
#=========================================================================
BANNER="""
      ____                           ______                __
     / __ \___  _________ ___  __   / ____/________ ______/ /_____  _____
    / / / / _ \/ ___/ __ `/ / / /  / /   / ___/ __ `/ ___/ //_/ _ \/ ___/
   / /_/ /  __/ /__/ /_/ / /_/ /  / /___/ /  / /_/ / /__/ ,< /  __/ /
  /_____/\___/\___/\__,_/\__, /   \____/_/   \__,_/\___/_/|_|\___/_/
                       /____/                                       v1

                                             By Malvuln (c) circa 2022
"""

#Console colors
RED="\033[1;31;40m"
GREY="\033[1;30;40m"
GREEN="\033[1;32;40m"
CYAN="\033[1;36;40m"
YELLOW="\033[1;33;40m"
BOLD = "\033[1m"
ENDC = "\033[m" #Default

key=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I",

 "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b",

 "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",
     "v","w","x","y","z","+","/"]

result=""
sz=0
key_error=False

#Change console back to default if script exited unclean
def exit_handler():
    print(ENDC)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--creds", help="Password to decrypt, see
--about")
    parser.add_argument("-a", "--about", nargs="?", const="1", help="About
Decay password decryptor")
    parser.add_argument("-e", "--example", nargs="?", const="1",
help="Password test samples")
    return parser.parse_args()

def usage():
     print(RED+"[+] "+CYAN+"Encrypted password samples:"+GREY)
     print("[+]----------------------------")
     print("[-] GM9ZCJ8p8G : Abc123!")
     print("[-] KsLZScLqNp4 : Secret_1")
     print("[-] U7bwDZOsNpC : xyz666_3")
     print("[-] PsXlStG : ghost")
     print("[-] CZKmDZSuCp8q : 250678324")
     print("[-] P6bXOcnlC34oCm : diablo0123")
     print("[-] INTbON91JM5dRdLj : IwearAMagnum")
     print("[-] ON1mON9fT6blRdDbOm : apparitionsec")

def info():
    print(RED+"[$] "+GREY+"Credits: John Page (aka hyp3rlinx)")
    print("[!] Recovers most simple lowercase or numeric passwords for:")
    print("[-] Trojan-Dropper.Win32.Decay.dxv (CyberGate v1.00.0)"+GREY)
    print("[-] "+RED+"MD5: "+GREY+"618f28253d1268132a9f10819a6947f2")
    print("[-] Backdoor.Win32.Shpinat.a (Spy-Net 2.7 Beta 02)"+GREY)
    print("[-] "+RED+"MD5: "+GREY+"eaf37e9506ef76f6d26838692d76aabd")

def main(args):
    if args.creds:
        ...