---
title: Cortex-XDR-Config-Extractor - Cortex XDR Config Extractor
url: https://buaq.net/go-151884.html
source: unSafe.sh - 不安全
date: 2023-03-04
fetch_date: 2025-10-04T08:37:22.740894
---

# Cortex-XDR-Config-Extractor - Cortex XDR Config Extractor

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

![](https://8aqnet.cdn.bcebos.com/2ae1c6be98f8ede7bebfd716bb4db508.jpg)

Cortex-XDR-Config-Extractor - Cortex XDR Config Extractor

This tool is meant to be used during Red Team Assessments and to audit the XDR Settings. Wi
*2023-3-3 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-151884.htm)
阅读量:37
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiqbVu2S3Gt5mdhd4YXomgzgHyuzu2f0ioVmXqg6HZAKUIuEGU4CIinlxu3vFkNnLvAmaZ0IqJaNlD8sp5EZEidcbEHPmt1f66PRZreXj6v237JFYNktT_EmhejsX-lpJdYQKRbmz5k8anZ_b4SZ68rEvJ9eMdZ4oEXs7RlLiYetLL9LPh_qaVr0lZWYQ=w398-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEiqbVu2S3Gt5mdhd4YXomgzgHyuzu2f0ioVmXqg6HZAKUIuEGU4CIinlxu3vFkNnLvAmaZ0IqJaNlD8sp5EZEidcbEHPmt1f66PRZreXj6v237JFYNktT_EmhejsX-lpJdYQKRbmz5k8anZ_b4SZ68rEvJ9eMdZ4oEXs7RlLiYetLL9LPh_qaVr0lZWYQ)

This tool is meant to be used during [Red Team](https://www.kitploit.com/search/label/Red%20Team "Red Team") Assessments and to audit the XDR Settings.

With this tool its possible to parse the `Database Lock Files` of the `Cortex XDR Agent` by Palo Alto Networks and extract `Agent Settings`, the `Hash and Salt` of the `Uninstall Password`, as well as possible `Exclusions`.

## Supported Extractions

* Uninstall Password Hash & Salt
* Excluded Signer Names
* DLL Security Exclusions & Settings
* PE Security Exclusions & Settings
* Office Files Security Exclusions & Settings
* Credential [Gathering](https://www.kitploit.com/search/label/Gathering "Gathering") Module Exclusions
* Webshell [Protection](https://www.kitploit.com/search/label/Protection "Protection") Module Exclusions
* Childprocess Executionchain Exclusions
* Behavorial Threat Module Exclusions
* Local [Malware](https://www.kitploit.com/search/label/Malware "Malware") Scan Module Exclusions
* Memory Protection Module Status
* Global Hash Exclusions
* Ransomware Protection Module Modus & Settings

## Usage

```
Usage = ./XDRConfExtractor.py [Filename].ldb
```

## Getting Hold of Database Lock Files

### Agent Version <7.8

With Agent Versions prior to 7.8 any authenticated user can generate a Support File on Windows via Cortex XDR [Console](https://www.kitploit.com/search/label/Console "Console") in the System Tray. The databse lock files can be found within the zip:

```
logs_[ID].zip\Persistence\agent_settings.db\
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjnoAXoIPnxTxyopMK3fLyaNRV_stRBa8OMe5jRJprVL_z-xBKOUaxPIUjNsatd-gVr6_21ZAoOLRTQUHiQ4URpWC1oUDn1H1Vsb17sLUaBSsxyqtNnHrt7wVLg6wtrSN50sQ5ekGr2YAjaxKrUDB2r2lBPOYOkyJZ72KiErIG8pP019FFwUPnhAuTKtg=w640-h362)](https://blogger.googleusercontent.com/img/a/AVvXsEjnoAXoIPnxTxyopMK3fLyaNRV_stRBa8OMe5jRJprVL_z-xBKOUaxPIUjNsatd-gVr6_21ZAoOLRTQUHiQ4URpWC1oUDn1H1Vsb17sLUaBSsxyqtNnHrt7wVLg6wtrSN50sQ5ekGr2YAjaxKrUDB2r2lBPOYOkyJZ72KiErIG8pP019FFwUPnhAuTKtg)

### Agent Version ≥7.8

Support files from Agents running Version 7.8 or higher are encrypted, but if you have elevated privileges on the Windows Maschine the files can be directly copied from the following directory, without encryption.

#### Method I

```
C:\ProgramData\Cyvera\LocalSystem\Persistence\agent_settings.db\
```

#### Method II

Generated Support Files are not deleted regulary, so it might be possible to find old, unencrypted Support Files in the following folder:

```
C:\Users\[Username]\AppData\Roaming\PaloAltoNetworks\Traps\support\
```

### Agent Version >8.1

Supposedly, since Agent version 8.1, it should no longer be possible to pull the data from the lock files. This has not been tested yet.

## Credits

This tool relies on a technique originally released by [mr.d0x](https://twitter.com/mrd0x "mr.d0x") in April 2022 [https://mrd0x.com/cortex-xdr-analysis-and-bypass/](https://mrd0x.com/cortex-xdr-analysis-and-bypass/ "https://mrd0x.com/cortex-xdr-analysis-and-bypass/")

## Legal disclaimer

Usage of Cortex-XDR-Config-Extractor for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.

Cortex-XDR-Config-Extractor - Cortex XDR Config Extractor
![Cortex-XDR-Config-Extractor - Cortex XDR Config Extractor](https://blogger.googleusercontent.com/img/a/AVvXsEiqbVu2S3Gt5mdhd4YXomgzgHyuzu2f0ioVmXqg6HZAKUIuEGU4CIinlxu3vFkNnLvAmaZ0IqJaNlD8sp5EZEidcbEHPmt1f66PRZreXj6v237JFYNktT_EmhejsX-lpJdYQKRbmz5k8anZ_b4SZ68rEvJ9eMdZ4oEXs7RlLiYetLL9LPh_qaVr0lZWYQ=s72-w398-c-h640)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/03/cortex-xdr-config-extractor-cortex-xdr.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)