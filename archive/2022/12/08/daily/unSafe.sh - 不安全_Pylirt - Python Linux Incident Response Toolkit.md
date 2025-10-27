---
title: Pylirt - Python Linux Incident Response Toolkit
url: https://buaq.net/go-139010.html
source: unSafe.sh - 不安全
date: 2022-12-08
fetch_date: 2025-10-04T00:52:11.006152
---

# Pylirt - Python Linux Incident Response Toolkit

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

![](https://8aqnet.cdn.bcebos.com/e50bb9598da6b2c1770ee6389e3efbc8.jpg)

Pylirt - Python Linux Incident Response Toolkit

With this application, it is aimed to accelerate the incident response processes by collecti
*2022-12-7 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-139010.htm)
阅读量:42
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEivhsbYo4aRh9oeOXlQWNUs7mOKcRjGNkKZFJ-0fxB_F1D_y7BCv3A_bTzitik8ciFCW4iVbxTBa-TTh3hUmkDSVVL3HjFConunqFXCvLiLWifoFNRO1W58XhhmrIDZPXTJUqbteRtvCtDscRWJppUNQHvwjtJFKPIgeHO9fGZxKZQqSfEF60OFc9BTHg=w590-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEivhsbYo4aRh9oeOXlQWNUs7mOKcRjGNkKZFJ-0fxB_F1D_y7BCv3A_bTzitik8ciFCW4iVbxTBa-TTh3hUmkDSVVL3HjFConunqFXCvLiLWifoFNRO1W58XhhmrIDZPXTJUqbteRtvCtDscRWJppUNQHvwjtJFKPIgeHO9fGZxKZQqSfEF60OFc9BTHg)

With this application, it is aimed to accelerate the incident response processes by collecting information in linux operating systems.

## Features

Information is collected in the following contents.

/etc/passwd

cat /etc/group

cat /etc/sudoers

lastlog

cat /var/log/auth.log

uptime/proc/meminfo

ps aux

/etc/resolv.conf

/etc/hosts

iptables -L -v -n

find / -type f -size +512k -exec ls -lh {}/;

find / -mtime -1 -ls

ip a

netstat -nap

arp -a

echo $PATH

## Installation

git clone [https://github.com/anil-yelken/pylirt](https://github.com/anil-yelken/pylirt "https://github.com/anil-yelken/pylirt")

cd pylirt

sudo pip3 install paramiko

## Usage

The following information should be specified in the cred\_list.txt file:

IP|Username|Password

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgzuYGC4pljUDpsX6Ez7l1DNBRw2g2k5ZVLhNFCh8_xP_lPkeD5hCrFiI-DOwNtOaneTuTYkvUUvxjQ7Ab9pMkKd5buHxG8K9ZN6fMhlxv6sABFQiImCndZjb8xaFllYCXmvpZucirdOIC7g0gt3NRXga2mzeLEP2flX04-NSCCUaxRM2zF9nMdgjxE9w=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEgzuYGC4pljUDpsX6Ez7l1DNBRw2g2k5ZVLhNFCh8_xP_lPkeD5hCrFiI-DOwNtOaneTuTYkvUUvxjQ7Ab9pMkKd5buHxG8K9ZN6fMhlxv6sABFQiImCndZjb8xaFllYCXmvpZucirdOIC7g0gt3NRXga2mzeLEP2flX04-NSCCUaxRM2zF9nMdgjxE9w)

sudo python3 plirt.py

[![](https://blogger.googleusercontent.com/img/a/AVvXsEivhsbYo4aRh9oeOXlQWNUs7mOKcRjGNkKZFJ-0fxB_F1D_y7BCv3A_bTzitik8ciFCW4iVbxTBa-TTh3hUmkDSVVL3HjFConunqFXCvLiLWifoFNRO1W58XhhmrIDZPXTJUqbteRtvCtDscRWJppUNQHvwjtJFKPIgeHO9fGZxKZQqSfEF60OFc9BTHg=w590-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEivhsbYo4aRh9oeOXlQWNUs7mOKcRjGNkKZFJ-0fxB_F1D_y7BCv3A_bTzitik8ciFCW4iVbxTBa-TTh3hUmkDSVVL3HjFConunqFXCvLiLWifoFNRO1W58XhhmrIDZPXTJUqbteRtvCtDscRWJppUNQHvwjtJFKPIgeHO9fGZxKZQqSfEF60OFc9BTHg)

## Contact

[https://twitter.com/anilyelken06](https://twitter.com/anilyelken06 "https://twitter.com/anilyelken06")

[https://medium.com/@anilyelken](https://medium.com/%40anilyelken "https://medium.com/@anilyelken")

Pylirt - Python Linux Incident Response Toolkit
![Pylirt - Python Linux Incident Response Toolkit](https://blogger.googleusercontent.com/img/a/AVvXsEivhsbYo4aRh9oeOXlQWNUs7mOKcRjGNkKZFJ-0fxB_F1D_y7BCv3A_bTzitik8ciFCW4iVbxTBa-TTh3hUmkDSVVL3HjFConunqFXCvLiLWifoFNRO1W58XhhmrIDZPXTJUqbteRtvCtDscRWJppUNQHvwjtJFKPIgeHO9fGZxKZQqSfEF60OFc9BTHg=s72-w590-c-h640)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/12/pylirt-python-linux-incident-response.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)