---
title: Artemis - APK Infrastructure Investigator
url: https://buaq.net/go-173201.html
source: unSafe.sh - 不安全
date: 2023-07-30
fetch_date: 2025-10-04T11:51:02.464300
---

# Artemis - APK Infrastructure Investigator

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

Artemis - APK Infrastructure Investigator

Overview A tools for Find APK Infrastructure . HADESS performs offensive cybersecurity ser
*2023-7-29 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-173201.htm)
阅读量:49
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiEdNzcQYMJMbBm4obxOh2FiZMblR_TqC039tHdgdovO3v-7yHVbe0F37pOtbrzo4qkIfsr1tfxEZDPRxqwrBnaYqztmAUnRAQrUgCfJee8C50poShIJhCAo_GELZfjWbdSoYUfJj_Se033XS0xpqHQE2MugYDGpBFwEAUYU1FCNjX0nMFE7DyFFgjNNNTK=w640-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEiEdNzcQYMJMbBm4obxOh2FiZMblR_TqC039tHdgdovO3v-7yHVbe0F37pOtbrzo4qkIfsr1tfxEZDPRxqwrBnaYqztmAUnRAQrUgCfJee8C50poShIJhCAo_GELZfjWbdSoYUfJj_Se033XS0xpqHQE2MugYDGpBFwEAUYU1FCNjX0nMFE7DyFFgjNNNTK)

## Overview

A tools for Find APK [Infrastructure](https://www.kitploit.com/search/label/Infrastructure "Infrastructure") .

[HADESS](https://hadess.io "HADESS") performs offensive [cybersecurity](https://www.kitploit.com/search/label/Cybersecurity "cybersecurity") services through infrastructures and software that include [vulnerability](https://www.kitploit.com/search/label/Vulnerability "vulnerability") analysis, scenario attack planning, and implementation of custom integrated preventive projects. We organized our activities around the prevention of corporate, industrial, and laboratory [cyber](https://www.kitploit.com/search/label/Cyber "cyber") threats.

## Installation

```
pip install -r requirements.txt
```

## Command Line Options

```
	  --help                       Display help
	  --path  					   Required path of apk file
	  --manifest  				   Display manifest informations
	  --infra  					   Find all infra addresses included ip,domain ex. --infra ip,domain
	  --whoise  				   Whoise all infra included ip,domain ex. --whoise ip,domain
	  --output  				   Set output files ex. --output out.txt
```

## Usage

### Display Manifest

[![APK Infrastructure Investigator (3)](https://camo.githubusercontent.com/bcd003353815351fa409c135e088112c859333b28d585362a698476463ae0755/68747470733a2f2f61736369696e656d612e6f72672f612f3539323333322e737667)](https://asciinema.org/a/592332 "APK Infrastructure Investigator (9)")

### IP Whois

[![APK Infrastructure Investigator (4)](https://camo.githubusercontent.com/d03b875cbbbe31f1750214fdcd0beb8b1653e4e95b0e096c275b940d53ae5a3d/68747470733a2f2f61736369696e656d612e6f72672f612f3539323333352e737667)](https://asciinema.org/a/592335 "APK Infrastructure Investigator (10)")

Example Usage:

1.Find infra(domain and ip) in sample4.apk and set output result into out.txt

```
python3 main.py --path sample4.apk --infra domain,ip --output out.txt
```

2. Investigate the Domain and IP on the APK

```
python3 main.py --path sample.apk --whois ip
```

Artemis - APK Infrastructure Investigator
![Artemis - APK Infrastructure Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEiEdNzcQYMJMbBm4obxOh2FiZMblR_TqC039tHdgdovO3v-7yHVbe0F37pOtbrzo4qkIfsr1tfxEZDPRxqwrBnaYqztmAUnRAQrUgCfJee8C50poShIJhCAo_GELZfjWbdSoYUfJj_Se033XS0xpqHQE2MugYDGpBFwEAUYU1FCNjX0nMFE7DyFFgjNNNTK=s72-w640-c-h640)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/07/artemis-apk-infrastructure-investigator.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)