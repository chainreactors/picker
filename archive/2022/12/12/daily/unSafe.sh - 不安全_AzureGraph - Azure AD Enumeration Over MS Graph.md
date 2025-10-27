---
title: AzureGraph - Azure AD Enumeration Over MS Graph
url: https://buaq.net/go-139489.html
source: unSafe.sh - 不安全
date: 2022-12-12
fetch_date: 2025-10-04T01:14:33.854723
---

# AzureGraph - Azure AD Enumeration Over MS Graph

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

![](https://8aqnet.cdn.bcebos.com/b713ea5218903beac86e8012b75cbe79.jpg)

AzureGraph - Azure AD Enumeration Over MS Graph

AzureGraph is an Azure AD information gathering tool over Microsoft Graph. Thanks to Micros
*2022-12-11 05:45:0
Author: [www.kitploit.com(查看原文)](/jump-139489.htm)
阅读量:37
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjFYE0zBN7rKaY14uhqieJjcZ2PwWwwyUn4JDbzJxw1DUSozjrVDJ3e9aRWDG1FkHyq9bCyOu0vEa6DEIfAMEosNmNlZ2i838MFa_wz5nujkSML2acydMRjSBK7sJte-V-d5VH27D_pmenQ073e0o7L7aLS7JZs5mFQe_j3b6Xc3h6DO88AT3fDclaBaQ=w640-h400)](https://blogger.googleusercontent.com/img/a/AVvXsEjFYE0zBN7rKaY14uhqieJjcZ2PwWwwyUn4JDbzJxw1DUSozjrVDJ3e9aRWDG1FkHyq9bCyOu0vEa6DEIfAMEosNmNlZ2i838MFa_wz5nujkSML2acydMRjSBK7sJte-V-d5VH27D_pmenQ073e0o7L7aLS7JZs5mFQe_j3b6Xc3h6DO88AT3fDclaBaQ)

**AzureGraph** is an Azure AD [information gathering](https://www.kitploit.com/search/label/Information%20Gathering "information gathering") tool over [Microsoft](https://www.kitploit.com/search/label/Microsoft "Microsoft") Graph.

Thanks to Microsoft Graph technology, it is possible to obtain all kinds of information from Azure AD, such as users, devices, applications, domains and much more.

This application, allows you to query this data through the API in an easy and simple way through a [PowerShell](https://www.kitploit.com/search/label/PowerShell "PowerShell") console. Additionally, you can download all the information from the cloud and use it completely offline.

* PowerShell 4.0 or higher

It's recommended to clone the complete repository or download the zip file.

```
git clone https://github.com/JoelGMSec/AzureGraph
```

```
.\AzureGraph.ps1 -h

_                         ____                 _
    / \    _____   _ _ __ ___ / ___|_ __ __ _ _ __ | |__
   / _ \  |_  / | | | '__/ _ \ |  _| '__/ _' | '_ \| '_ \
  / ___ \  / /| |_| | | |  __/ |_| | | | (_| | |_) | | | |
 /_/   \_\/___|\__,_|_|  \___|\____|_|  \__,_| .__/|_| |_|
                                             |_|
  -------------------- by @JoelGMSec --------------------

Info:  This tool helps you to obtain information from Azure AD
        like Users or Devices, using de Microsft Graph REST API

Usage: .\AzureGraph.ps1 -h
          Show this help, more info on my blog: darkbyte.net

.\AzureGraph.ps1
          Execute AzureGraph in fully interactive mode

Warning: You need previously generated MS Graph token to use it
          You can use a refresh token too, or generate a new one
```

### The detailed guide of use can be found at the following link:

[https://darkbyte.net/azuregraph-enumerando-azure-ad-desde-microsoft-graph](https://darkbyte.net/azuregraph-enumerando-azure-ad-desde-microsoft-graph "https://darkbyte.net/azuregraph-enumerando-azure-ad-desde-microsoft-graph")

This project is licensed under the GNU 3.0 license - see the LICENSE file for more details.

This tool has been created and designed from scratch by Joel Gámez Molina // @JoelGMSec

This software does not offer any kind of guarantee. Its use is exclusive for educational environments and / or security audits with the corresponding consent of the client. I am not responsible for its misuse or for any possible damage caused by it.

For more information, you can find me on [Twitter](https://www.kitploit.com/search/label/Twitter "Twitter") as [@JoelGMSec](https://twitter.com/JoelGMSec "@JoelGMSec") and on my blog [darkbyte.net](https://darkbyte.net "darkbyte.net").

AzureGraph - Azure AD Enumeration Over MS Graph
![AzureGraph - Azure AD Enumeration Over MS Graph](https://blogger.googleusercontent.com/img/a/AVvXsEjFYE0zBN7rKaY14uhqieJjcZ2PwWwwyUn4JDbzJxw1DUSozjrVDJ3e9aRWDG1FkHyq9bCyOu0vEa6DEIfAMEosNmNlZ2i838MFa_wz5nujkSML2acydMRjSBK7sJte-V-d5VH27D_pmenQ073e0o7L7aLS7JZs5mFQe_j3b6Xc3h6DO88AT3fDclaBaQ=s72-w640-c-h400)
Reviewed by Zion3R
on
6:45 PM
Rating: 5

文章来源: http://www.kitploit.com/2022/12/azuregraph-azure-ad-enumeration-over-ms.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)