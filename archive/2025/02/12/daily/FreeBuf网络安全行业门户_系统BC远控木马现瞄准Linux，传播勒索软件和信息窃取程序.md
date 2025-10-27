---
title: 系统BC远控木马现瞄准Linux，传播勒索软件和信息窃取程序
url: https://www.freebuf.com/articles/endpoint/421497.html
source: FreeBuf网络安全行业门户
date: 2025-02-12
fetch_date: 2025-10-06T20:36:22.863903
---

# 系统BC远控木马现瞄准Linux，传播勒索软件和信息窃取程序

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

系统BC远控木马现瞄准Linux，传播勒索软件和信息窃取程序

* ![]()
* 关注

* [终端安全](https://www.freebuf.com/articles/endpoint)

系统BC远控木马现瞄准Linux，传播勒索软件和信息窃取程序

2025-02-11 13:00:08

所属地 上海

威胁分析师发现了一种新出现的威胁：SystemBC RAT（远程访问木马）的一个变种，目前正积极针对基于Linux的平台。这一新进展将企业网络、云基础设施和物联网设备置于危险之中。

最新版本的SystemBC RAT更加隐蔽，更难检测，它使用加密通信来隐藏自身，同时让攻击者在被入侵的系统中自由活动。

![新SystemBC RAT版本正瞄准Linux](https://image.3001.net/images/20250211/1739282481180968_7016e504948b4ac691f66e9f2291ac8b.jpg!small)ANY.RUN的分析师比较了SystemBC在Windows和Linux上的流量

## **SystemBC RAT：从Windows扩展到Linux**

SystemBC是一种远程访问木马（RAT），通常用于网络攻击，为攻击者提供对被感染系统的远程控制。

最初它仅针对Windows系统，现在已扩展到Linux，这使其变得更加危险，因为Linux服务器在企业环境中被广泛使用。

## **Linux版SystemBC RAT的危险性**

让我们看看这种恶意软件是如何运行的，以及为什么它对基于Linux的系统构成严重威胁。

### **与C2服务器的加密通信**

Linux版的SystemBC RAT与其Windows版本一样，使用自定义协议与C2服务器保持加密通信。

这使得攻击者能够在统一的Windows和Linux植入基础设施中保持稳定连接，从而更容易地控制被感染的机器而不引起怀疑。

虽然SystemBC RAT旨在保持其C2通信的加密和隐藏，但在ANY.RUN的分析会话中，它会完全暴露。通过在沙箱中运行真实样本，安全团队可以实时查看恶意软件的网络连接、文件修改和进程活动。

**查看ANY.RUN分析会话**

![新SystemBC RAT版本正瞄准Linux](https://image.3001.net/images/20250211/1739282481924348_af38062d760b442d85633ff67c4af3e1.jpg!small)在ANY.RUN沙箱中分析的SystemBC RAT

在Linux虚拟机窗口下方，所有与此特定攻击相关的网络连接和系统修改都清晰显示。

![新SystemBC RAT版本正瞄准Linux](https://image.3001.net/images/20250211/1739282482313446_ccadad93daff46fdaa080f9eff99dcfe.jpg!small)SystemBC RAT触发的Suricata规则

在“威胁”部分，我们可以看到一条由Suricata规则触发的警报：“检测到恶意软件命令与控制活动 - BOTNET SystemBC.Proxy连接。”这种即时检测使分析师能够跟踪感染过程并了解恶意软件的运行方式。

为您的团队配备实时威胁分析工具，以更快地检测和应对恶意软件。立即开始ANY.RUN的14天免费试用！

### **用于横向移动的代理植入**

该恶意软件作为代理植入运行，意味着它可以在被入侵的网络内促进横向移动，而无需部署额外的、易于检测的工具。这使得它成为攻击者寻求在企业基础设施中持久存在和深入渗透的强大武器。

### **逃避传统检测**

最令人担忧的一个方面是，安全厂商很难检测出该版本属于SystemBC家族。这种隐蔽的方法使RAT能够在较长时间内保持不被发现，使其成为一种持续威胁。

### **沙箱和虚拟化逃避**

除了基于签名的逃避外，SystemBC还会检测虚拟化环境以抵抗动态分析。在上述ANY.RUN分析会话中，MITRE ATT&CK框架标志显示“虚拟化/沙箱逃避 - 系统检查”，表明该恶意软件正在积极执行系统检查以确定是否在安全沙箱或虚拟机中运行。

通过识别这些环境，SystemBC可以改变其行为或终止执行，帮助攻击者绕过自动恶意软件分析工具，同时在真实被感染的系统上保持完全运行。

![新SystemBC RAT版本正瞄准Linux](https://image.3001.net/images/20250211/1739282482608092_d2b0fb021fb84792af5d3905a2e80ef3.jpg!small)ANY.RUN沙箱检测到的防御规避技术和战术

### **与其他恶意软件株的集成**

SystemBC很少单独部署，它通常与其他恶意软件协同工作以扩大攻击的影响。在Windows攻击中，它已被观察到传播Ryuk和Conti等勒索软件，以及银行木马和信息窃取程序。

随着其新的Linux变种的出现，类似的威胁可能会随之而来，使企业服务器和云环境面临更大的数据窃取、勒索软件加密和持久后门访问风险。

## **在威胁爆发前揭露隐藏风险**

网络威胁正变得更加智能，企业不能再滞后于攻击者。随着SystemBC RAT现在瞄准Linux，攻击者有了一种隐藏C2流量、在网

**参考来源：**

> [SystemBC RAT Now Targets Linux, Spreading Ransomware and Infostealers](https://hackread.com/systembc-rat-targets-linux-ransomware-infostealers/)

# 终端安全 # 企业安全

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

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)