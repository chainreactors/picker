---
title: Pyramid - A Tool To Help Operate In EDRs' Blind Spots
url: https://buaq.net/go-139546.html
source: unSafe.sh - 不安全
date: 2022-12-12
fetch_date: 2025-10-04T01:14:24.367675
---

# Pyramid - A Tool To Help Operate In EDRs' Blind Spots

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9b665b230689a0312cbdb9b3f4d08d2b.jpg)

Pyramid - A Tool To Help Operate In EDRs' Blind Spots

Pyramid is a set of Python scripts and module dependencies that can be used to evade EDR
*2022-12-11 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-139546.htm)
阅读量:33
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiwyJplSNlKPGXq-lzooGKlu739aJ6bDluB3JoCClmCbxw0Gnu0qRejcDEaf-5lYlEtSkU2R7XaOgMBZolVRMofVeSs63HnaG6hm8DaHceHtoUztTRHHUzPZ5b_P9lUT7hijxFYn96WNmEPD_BVehJWSpKQ8QvUTf0T39Yoh_nUIACODOarpCyFQjTR1A=s320)](https://blogger.googleusercontent.com/img/a/AVvXsEiwyJplSNlKPGXq-lzooGKlu739aJ6bDluB3JoCClmCbxw0Gnu0qRejcDEaf-5lYlEtSkU2R7XaOgMBZolVRMofVeSs63HnaG6hm8DaHceHtoUztTRHHUzPZ5b_P9lUT7hijxFYn96WNmEPD_BVehJWSpKQ8QvUTf0T39Yoh_nUIACODOarpCyFQjTR1A)

Pyramid is a set of Python scripts and module dependencies that can be used to evade EDRs. The main purpose of the tool is to perform offensive tasks by leveraging some Python evasion properties and looking as a legit Python application usage. This can be achieved because:

1. the [Python Embeddable package](https://www.python.org/ftp/python/3.10.4/python-3.10.4-embed-amd64.zip "Python Embeddable package") provides a signed Python interpreter with [good reputation](https://www.virustotal.com/gui/file/261f682238e2dc3296038c8bd78dd01e5874e1177ebe3da2afcba35ef82d73b7 "good reputation");
2. Python has many legit applications, so there is a lot of different telemetry coming from the python.exe binary since the interpreter natively runs the APIs. This can be abused by operating within the Python.exe process and trying to blend in the huge "telemetry fingerprint" of python.exe binary.
3. There is a lack of auditing for Python code execution - [PEP-578](https://peps.python.org/pep-0578/ "PEP-578") tried to solve that but the stock python.exe binary does not have auditing capabilities enabled by default.
4. Operations can be done natively from within python.exe natively using Python language to perform [post exploitation](https://www.kitploit.com/search/label/Post%20Exploitation "post exploitation") tasks such as dynamically importing Python modules to run offensive tools and executing Beacon Object Files (after some BOF modifications) directly within python.exe.

For more information please check the **[DEFCON30 - Adversary village talk "Python vs Modern Defenses" slide deck](https://github.com/naksyn/talks/blob/main/DEFCON30/Diego%20Capriotti%20-%20DEFCON30%20Adversary%20Village%20-%20%20Python%20vs%20Modern%20Defenses.pdf "DEFCON30 - Adversary village talk Python vs Modern Defenses slide deck")** and this **[post on my blog](https://www.naksyn.com/edr%20evasion/2022/09/01/operating-into-EDRs-blindspot.html "post on my blog")**.

## Disclaimer

This tool was created to demostrate a bypass strategy against EDRs based on some blind-spots assumptions. It is a combination of already existing techniques and tools in a (to the best of my knowledge) novel way that can help evade defenses. The sole intent of the tool is to help the community increasing awareness around this kind of usage and accelerate a resolution. It' not a 0day, it's not a full fledged shiny C2, Pyramid exploits what might be EDRs blind spots and the tool has been made public to shed some light on them. A defense paragraph has been included, hoping that experienced blue-teamers can help contribute and provide better possible resolution on the issue Pyramid aims to highlight. All information is provided for educational purposes only. Follow instructions at your own risk. Neither the author nor his employer are responsible for any direct or consequential damage or loss arising from any person or organization.

### Credits

Pyramid is using some awesome tools made by:

* [xorrior](https://twitter.com/xorrior "xorrior") for [Empyre - Finder Class](https://github.com/EmpireProject/EmPyre "Empyre - Finder Class")
* [TrustedSec](https://twitter.com/TrustedSec "TrustedSec") for [COFFLoader](https://github.com/trustedsec/COFFLoader "COFFLoader")
* [Falconforcenl](https://twitter.com/falconforcenl "Falconforcenl") for [bof2shellcode](https://github.com/FalconForceTeam/BOF2shellcode "bof2shellcode")
* [S4ntiagoP](https://twitter.com/s4ntiago_p "S4ntiagoP") for [nanodump](https://github.com/helpsystems/nanodump "nanodump")

### Contributors

[snovvcrash](https://twitter.com/snovvcrash "snovvcrash") - base-DonPAPI.py - base-LaZagne.py - base-clr.py

### Current features

Pyramid capabilities are executed directly from python.exe process and are currently:

1. Dynamic loading of BloodHound Python, impacket secretsdump, paramiko, DonPAPI, LaZagne, Pythonnet, pproxy.
2. BOFs execution using in-process shellcode injection.
3. In-process injection of a C2 agent and tunneling its traffic with local SSH port forwarding.

### Tool's description

Pyramid is meant to be used unpacking an official embeddable Python package and then running python.exe to execute a Python download cradle. This is a simple way to avoid creating uncommon Process tree pattern and looking like a normal Python application usage.

In Pyramid the download cradle is used to reach a Pyramid Server (simple HTTPS server with auth) to fetch base scripts and dependencies.

Base scripts are specific for the feature you want to use and contain:

1. Custom Finder class to in-memory import required dependencies (zip files).
2. Code to download the required dependencies.
3. Main logic for the module you want to execute (bloodhound, secretsdump, paramiko etc.).

BOFs are ran through a base script containing the shellcode resulted from bof2shellcode and the related in-process injection code.

The Python dependencies have been already fixed and modified to be imported in memory without conflicting.

There are currently 8 main base scripts available:

1. **base-bh.py** script will in-memory import and execute python-BloodHound.
2. **base-secretsdump.py** script will in-memory import and execute [Impacket](https://github.com/SecureAuthCorp/impacket "Impacket") secretsdump.
3. **base-BOF-lsass.py** script is using a stripped version of nanodump to dump lsass from python.exe. This is achieved in-memory injecting shellcode output obtained from bof2shellcode and COFFloader. To make complex BOFs work with this technique, they should first be adapted for Python execution.
4. **base-tunnel-inj.py** script import and executes paramiko on a new Thread to create an SSH local [port forward](https://www.kitploit.com/search/label/Port%20Forward "port forward") to a remote SSH server. Afterward a shellcode can be locally injected in python.exe.
5. **base-DonPAPI.py** script will in-memory import and execute [DonPAPI](https://github.com/login-securite/DonPAPI "DonPAPI"). Results and credentials extracted are saved on disk in the Python Embeddable Package Directory.
6. **base-LaZagne.py** script will in-memory import and execute [LaZagne](https://github.com/AlessandroZ/LaZagne "LaZagne")
7. **base-tunnel-socks5** script import and executes paramiko on a new Thread to create an SSH remote port forward to an SSH server, then a socks5 proxy server is executed locally on target and made accessible remotely through the SSH tunnel.
8. **base-clr** script imports Pythonnet to load and execute a .NET assembly in-memory.

### Usage

#### Starting the server

`git clone https://github.com/naksyn/Pyramid`

Generate SSL [certificates](https://www.kitploit.com/search/label/Certificates "certificates") for HTTP Server:

`openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365`

Example of running Pyramid HTTP Server using SSL certificate and ...