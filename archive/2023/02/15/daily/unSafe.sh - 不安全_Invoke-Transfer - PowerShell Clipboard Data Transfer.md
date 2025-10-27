---
title: Invoke-Transfer - PowerShell Clipboard Data Transfer
url: https://buaq.net/go-149369.html
source: unSafe.sh - 不安全
date: 2023-02-15
fetch_date: 2025-10-04T06:36:08.726317
---

# Invoke-Transfer - PowerShell Clipboard Data Transfer

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

![](https://8aqnet.cdn.bcebos.com/b35df1cd4cc350db0e5066ba07cc1daf.jpg)

Invoke-Transfer - PowerShell Clipboard Data Transfer

Invoke-Transfer is a PowerShell Clipboard Data Transfer. This tool helps you to send file
*2023-2-14 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-149369.htm)
阅读量:27
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgi0We65Ztkng-hSXWQGqAdfu9tu1Tv_YlVz5tr6C-8EfY7oR_wETvSyhWMnyQ1W79A0vbsRJMW4yuRhtfs0tqHfBpwCuxK7R7wYCXJH8cOWLnf5mYnsrpBXYUHJbSIcf2nXmdcFyFA31Z88ZKC7pAlpJqQ7hRlsIJh9pFaDpJgSS_GleZoJL_lFuORXQ=w640-h400)](https://blogger.googleusercontent.com/img/a/AVvXsEgi0We65Ztkng-hSXWQGqAdfu9tu1Tv_YlVz5tr6C-8EfY7oR_wETvSyhWMnyQ1W79A0vbsRJMW4yuRhtfs0tqHfBpwCuxK7R7wYCXJH8cOWLnf5mYnsrpBXYUHJbSIcf2nXmdcFyFA31Z88ZKC7pAlpJqQ7hRlsIJh9pFaDpJgSS_GleZoJL_lFuORXQ)

**Invoke-Transfer** is a [PowerShell](https://www.kitploit.com/search/label/PowerShell "PowerShell") Clipboard Data Transfer.

This tool helps you to send files in highly [restricted environments](https://www.kitploit.com/search/label/Restricted%20Environments "restricted environments") such as Citrix, RDP, VNC, Guacamole.. using the clipboard function.

As long as you can send text through the clipboard, you can send files in text format, in small Base64 encoded chunks. Additionally, you can transfer files from a screenshot, using the native OCR function of [Microsoft](https://www.kitploit.com/search/label/Microsoft "Microsoft") Windows.

* Powershell 5.1
* Windows 10 or greater

It is recommended to clone the complete repository or download the zip file. You can do this by running the following command:

```
git clone https://github.com/JoelGMSec/Invoke-Transfer
```

```
.\Invoke-Transfer.ps1 -h

___                 _           _____                     __
 |_ _|_ __ _   __ __ | | __ __   |_   _| __ __ _ _ __  ___ / _| ___ _ __
  | || '_ \ \ / / _ \| |/ / _ \____| || '__/ _' | '_ \/ __| |_ / _ \ '__|
  | || | | \ V / (_) |   <  __/____| || | | (_| | | | \__ \  _|  __/ |
 |___|_| |_|\_/ \___/|_|\_\___|    |_||_|  \__,_|_| |_|___/_|  \___|_|

----------------------- by @JoelGMSec & @3v4Si0N ---------------------

Info:  This tool helps you to send files in highly restricted environments
        such as Citrix, RDP, VNC, Guacamole... using the clipboard function

Usage: .\Invoke-Transfer.ps1 -split {FILE} -sec {SECONDS}
          Send 120KB chunks with a set time delay of seconds
          Add -guaca to send files through Apache Guacamole

.\Invoke-Transfer.ps1 -merge {B64FILE} -out {FILE}
          Merge Base64 file into original file in de   sired path

.\Invoke-Transfer.ps1 -read {IMGFILE} -out {FILE}
          Read screenshot with Windows OCR and save output to file

Warning: This tool only works on Windows 10 or greater
          OCR reading may not be entirely accurate
```

### The detailed guide of use can be found at the following link:

[https://darkbyte.net/transfiriendo-ficheros-en-entornos-restringidos-con-invoke-transfer](https://darkbyte.net/transfiriendo-ficheros-en-entornos-restringidos-con-invoke-transfer "https://darkbyte.net/transfiriendo-ficheros-en-entornos-restringidos-con-invoke-transfer")

This project is licensed under the GNU 3.0 license - see the LICENSE file for more details.

This tool has been created and designed from scratch by Joel Gámez Molina (@JoelGMSec) and Héctor de Armas Padrón (@3v4si0n).

This software does not offer any kind of guarantee. Its use is exclusive for educational environments and / or security audits with the corresponding consent of the client. I am not responsible for its misuse or for any possible damage caused by it.

For more information, you can find us on Twitter as [@JoelGMSec](https://twitter.com/JoelGMSec "@JoelGMSec"), [@3v4si0n](https://twitter.com/3v4si0n "@3v4si0n") and on my blog [darkbyte.net](https://darkbyte.net "darkbyte.net").

Invoke-Transfer - PowerShell Clipboard Data Transfer
![Invoke-Transfer - PowerShell Clipboard Data Transfer](https://blogger.googleusercontent.com/img/a/AVvXsEgi0We65Ztkng-hSXWQGqAdfu9tu1Tv_YlVz5tr6C-8EfY7oR_wETvSyhWMnyQ1W79A0vbsRJMW4yuRhtfs0tqHfBpwCuxK7R7wYCXJH8cOWLnf5mYnsrpBXYUHJbSIcf2nXmdcFyFA31Z88ZKC7pAlpJqQ7hRlsIJh9pFaDpJgSS_GleZoJL_lFuORXQ=s72-w640-c-h400)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/02/invoke-transfer-powershell-clipboard.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)