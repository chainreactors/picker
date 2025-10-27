---
title: 快讯：使用21个漏洞传播的DDoS家族WSzero已经发展到第4个版本
url: https://buaq.net/go-139014.html
source: unSafe.sh - 不安全
date: 2022-12-08
fetch_date: 2025-10-04T00:52:08.558752
---

# 快讯：使用21个漏洞传播的DDoS家族WSzero已经发展到第4个版本

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

![](https://8aqnet.cdn.bcebos.com/96eb999e57b1ab6fb598f557f420bbdf.jpg)

快讯：使用21个漏洞传播的DDoS家族WSzero已经发展到第4个版本

概述近期，我们的BotMon系统连续捕获到一个由Go编写的
*2022-12-7 20:58:21
Author: [blog.netlab.360.com(查看原文)](/jump-139014.htm)
阅读量:48
收藏*

---

## 概述

近期，我们的BotMon系统连续捕获到一个由Go编写的DDoS类型的僵尸网络家族，它用于DDoS攻击，使用了包括SSH/Telnet弱口令在内的多达22种传播方式。短时间内出现了4个不同的版本，有鉴于此，我们觉得该家族未来很可能继续活跃，值得警惕。下面从传播、样本和跟踪角度分别介绍。

## 传播分析

除了Telnet/SSH弱口令，我们观察到wszero还使用了如下`21`个漏洞进行传播：

| VULNERABILITY | AFFECTED |
| --- | --- |
| [CVE\_2014\_08361](https://nvd.nist.gov/vuln/detail/CVE-2014-8361?ref=blog.netlab.360.com) | Realtek SDK |
| [CVE\_2017\_17106](https://nvd.nist.gov/vuln/detail/CVE-2017-17106?ref=blog.netlab.360.com) | Zivif Webcams |
| [CVE\_2017\_17215](https://nvd.nist.gov/vuln/detail/cve-2017-17215?ref=blog.netlab.360.com) | Huawei HG532 |
| [CVE\_2018\_12613](https://nvd.nist.gov/vuln/detail/CVE-2018-12613?ref=blog.netlab.360.com) | phpMyAdmin 4.8.x before 4.8.2 |
| [CVE\_2020\_10987](https://nvd.nist.gov/vuln/detail/CVE-2020-10987?ref=blog.netlab.360.com) | Tenda AC15 AC1900 |
| [CVE\_2020\_25506](https://nvd.nist.gov/vuln/detail/CVE-2020-25506?ref=blog.netlab.360.com) | D-Link DNS-320 FW v2.06B01 Revision Ax |
| [CVE\_2021\_35395](https://nvd.nist.gov/vuln/detail/CVE-2021-35395?ref=blog.netlab.360.com) | Realtek Jungle SDK |
| [CVE\_2021\_36260](https://packetstormsecurity.com/files/164603/hikvision210702-exec.txt?ref=blog.netlab.360.com) | Hikvision DVR |
| [CVE\_2021\_46422](https://packetstormsecurity.com/files/167201/SDT-CW3B1-1.1.0-Command-Injection.html?ref=blog.netlab.360.com) | Telesquare SDT CW3B1 |
| [CVE\_2022\_01388](https://www.itechpost.com/articles/110537/20220509/f5-big-ip-trouble-cve-2022-1388-vulnerability-%E2%80%94-patch.htm?ref=blog.netlab.360.com) | F5 BIG-IP |
| [CVE\_2022\_22965](https://nvd.nist.gov/vuln/detail/cve-2022-22965?ref=blog.netlab.360.com) | Spring |
| [CVE\_2022\_25075](https://nvd.nist.gov/vuln/detail/cve-2022-25075?ref=blog.netlab.360.com) | TOTOLINK A3000RU |
| [CVE\_2022\_26186](https://doudoudedi.github.io/2022/02/21/TOTOLINK-N600R-Command-Injection/?ref=blog.netlab.360.com) | TOTOLINK N600R |
| [CVE\_2022\_26210](https://nvd.nist.gov/vuln/detail/CVE-2022-26210?ref=blog.netlab.360.com) | TOTOLINK A830R |
| [CVE\_2022\_30525](https://www.rapid7.com/blog/post/2022/05/12/cve-2022-30525-fixed-zyxel-firewall-unauthenticated-remote-command-injection/?ref=blog.netlab.360.com) | Zyxel Firewall |
| [CVE\_2022\_34538](https://nvd.nist.gov/vuln/detail/CVE-2022-34538?ref=blog.netlab.360.com) | Digital Watchdog DW MEGApix IP cameras |
| [CVE\_2022\_37061](https://packetstormsecurity.com/files/cve/CVE-2022-37061?ref=blog.netlab.360.com) | FLIR AX8 thermal sensor cameras |
| [DLINK](https://www.exploit-db.com/exploits/44760?ref=blog.netlab.360.com) | D-Link DSL-2750B |
| [CVE-2018-10561](https://nvd.nist.gov/vuln/detail/cve-2018-10561?ref=blog.netlab.360.com) | Dasan GPON home router |
| [SAPIDO RB-1732 command line execution](https://www.exploit-db.com/exploits/47031?ref=blog.netlab.360.com) | SAPIDO RB-1732 |
| [PHP Backdoor](https://packetstormsecurity.com/files/162749/PHP-8.1.0-dev-Backdoor-Remote-Command-Injection.html?ref=blog.netlab.360.com) | PHP 8.1.0 dev Backdoor |

## 样本分析

简单来说，wszero是一个Go语言编写的DDoS类型的僵尸网络家族，它被命名为wszero的原因是它的下载链接中的文件名多为`zero.*`这种形式，并且最新版本C2协议基于`websocket`，所以将其缩写为`wszero`。基于样本的C2协议、主机行为和C2加密等方面特征，我们把已经捕获的wszero分为4个大的版本，其捕获的时间线如下：

* 2022年11月18日，首次捕获到wszero v1
* 2022年11月21日，捕获到V2样本
* 2022年11月24日，捕获到V3样本
* 2022年11月26日，捕获到V3.x样本
* 2022年11月29日，捕获到V4样本

下面是这4个版本一些具体特性的对比:

| Version | C2 | Decryption | Exploit | Tel/SSH Crack | Protocol | Platform | Persistence | Instruction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| v1 | 176.65.137.5:1401 | SUB1 | 0 | No | TCP | Linux | YES | print,attack,command |
| v2 | 176.65.137.5:80 | NO | 0 | No | WS | Linux | YES | print,attack,command |
| v3 | zero.sudolite.ml | SUB 1 | 0 | No | WSS | Linux | YES | print,attack,command |
| v3.x | zero.sudolite.ml | SUB1 | 21 | YES | WSS | Linux/Windows | YES | kill,attack,update,ping,stop,command,enable\_scan,disable\_scan |
| v4 | 176.65.137.5:80 | SUB1 | 21 | YES | WS | Linux/Windows | YES | kill,attack,update,ping,stop,command,enable\_scan,disable\_scan |

因为使用Go编写并且未作混淆，从wszero样本中能容易的恢复出函数符号和功能逻辑等，因此我们不做详细的样本分析，下面着重介绍下wszero的C2存储和通信。

### C2存储和解密

V1和V3都使用了加密的方式存储C2，其中V1的C2保存在样本的rodata段中，而V3则存放在局部变量中，如下图所示。

它们的解密方法相同，都为**SUB 1**算法，即逐字节减一。上图中将V3的局部变量拼接后，再进行解密就得到了C2以及URI。
[![](https://blog.netlab.360.com/content/images/2022/11/wszero_v3c2.png)](https://blog.netlab.360.com/content/images/2022/11/wszero_v3c2.png)

### C2协议

Wszero的C2消息使用了一个自定义的JSON串，不同版本间有几个JSON字段的微小差别。最初版本的底层传输协议使用TCP，后续版本换成了WEBSOCKET，以及TLS保护的WEBSOCKET，下面分别介绍。

#### 上线包格式

当C2连接建立后，C2会主动向BOT发送Banner信息提示输入用户名，BOT首先向C2发送硬编码的用户名，接着再发送JSON格式的BotInfo，形如 `{"platform": "%s", "gcc": "%s", "cpu": %d, "payload": "%s"}` ，其中payload指的是分组信息。

[![](https://blog.netlab.360.com/content/images/2022/11/wszero_v1pkg.png)](https://blog.netlab.360.com/content/images/2022/11/wszero_v1pkg.png)

#### 底层传输协议的变化

V1版本采用了TCP，V2和V4基于WEBSOCKET，V3同样基于WEBSOCKET，但强制使用TLS对WEBSOCKET进行保护。

以V2为例，BOT和C2首先进行建立ws连接，

[![](https://blog.netlab.360.com/content/images/2022/11/wszero_v2pkg.png)](https://blog.netlab.360.com/content/images/2022/11/wszero_v2pkg.png)

接着再发送BotInfo，内容格式依然为JSON串。

[![](https://blog.netlab.360.com/content/images/2022/11/wszero_v2payload.png)](https://blog.netlab.360.com/content/images/2022/11/wszero_v2payload.png)

#### 指令

当Bot注册成功后，就开始等待并执行C2下发的指令。指令消息同样是JSON格式，有**Type， Data，Command** 3 个key，其中**Type**用于指定DDoS或Command任务类别，**Data**/**Command**则分别用于存储DDoS选项，系统命令及参数。相关解析代码如下。

[![](https://blog.netlab.360.com/content/images/2022/11/wszero_cmdfmt.png)](https://blog.netlab.360.com/content/images/2022/11/wszero_cmdfmt.png)

下面是我们实际接收到的HTTP\_BYPASS攻击指令，当Bot接收到这个指令后就会使用该方法对目标进行攻击。

[![](https://blog.netlab.360.com/content/images/2022/11/wszero_ddos.png)](https://blog.netlab.360.com/content/images/2022/11/wszero_ddos.png)

除了HTTP\_BYPASS, wszero还支持TCP/UDP/ICMP等多种协议的攻击方法，完整列表详见下图。

[![](https://blog.netlab.360.com/content/images/2022/11/wszero_atkvec.png)](https://blog.netlab.360.com/content/images/2022/11/wszero_atkvec.png)

## 指令跟踪情况

分析出这个新家族后，我们迅速做了跟踪处理，在2022年11月23日首次接收到DDoS攻击指令，具体DDoS攻击趋势如下图所示：

[![](https://blog.netlab.360.com/content/images/2022/12/Snip20221202_33.min.png)](https://blog.netlab.360.com/content/images/2022/12/Snip20221202_33.png)

能看出来其攻击指令的下发并不是很频繁，这可能跟这个家族还处于早期发展阶段有关。目前其C2仍在活跃，并且频繁下发更新指令。

## 结尾

今年我们已经观察到多起使用Go开发的全新botnet家族，wszero只是其中之一。其作者在10多天的时间内做了4次大的升级，说明该家族还在发展之中，未来可能会继续推出新的版本。对此我们会持续关注，有新的发现将会及时公开。

## 联系我们

感兴趣的读者，可以在 [twitter](https://twitter.com/360Netlab?ref=blog.netlab.360.com) 或者通过邮件netlab[at]360.cn联系我们。

## 解决方案

基于Netlab多年研究工作孵化的360全系列[DNS安全产品](https://sdns.360.net/?ref=blog.netlab.360.com)均已支持文中远控服务器的拦截和检测，同时内置多种算法可有效发现和拦截各种未知威胁，建议企业客户接入360 DNS安全SaaS平台或部署本地360DNS安全产品，及时防范此类新型威胁，避免企业资产失陷。联系人: [[email protected]](https://blog.netlab.360.com/cdn-cgi/l/email-protection#7c0b1d121b170912511e183c4f4a4c521f12)

## IoC

### C2

```
176.65.137.5
zero.sudolite.ml
```

### Loader IP

```
176.65.137.6
176.65.137.5
```

### Sample

```
aabca688b31eb962a7a2849c57000bea
86827dc70c5001633b801b7b7fa8a9b9
0642bc041c2e4a74fbf58537a2305543
13e1966f13274c71d39e4aea7f62127e
271aebe152b793765a75e5e89d24cdbd
27f66ef808e5497528c653ba862822b7
2eca5324301a55dfa5b5d2c2b67ab9d0
342a5c7e1eb3ead0b6ddeeed4f1a811f
3627e6848eb9f6a28c7c83b347753f26
367b9095e93d27fc1a684a90a77e82f9
40b3bb4e7d00377cbd9d100b39d26ac0
45bc7cd7c7acdf679d1f3ceceb7d6602
4a5e9ffd3ce77d5269033b8032426e45
513a8036ca358b0acfce30903f95f12b
52d21fbad081d699ec6e041fcdd6133c
59d635c...