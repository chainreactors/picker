---
title: 网络安全领域研究人员遭遇假PoC专项攻击
url: https://www.freebuf.com/news/420252.html
source: FreeBuf网络安全行业门户
date: 2025-01-21
fetch_date: 2025-10-06T20:10:19.323611
---

# 网络安全领域研究人员遭遇假PoC专项攻击

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

网络安全领域研究人员遭遇假PoC专项攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

网络安全领域研究人员遭遇假PoC专项攻击

2025-01-20 10:00:12

所属地 上海

## **一、事件概述**

近期，网络安全领域接连曝出针对研究人员的假PoC（概念验证）攻击事件，引发业界高度关注。2024年12月，微软在当月的补丁星期二更新中修复了两个关键的LDAP漏洞，分别是CVE-2024-49112和CVE-2024-49113。其中，CVE-2024-49113是一个拒绝服务（DoS）漏洞。然而，就在漏洞修复后不久，Trend Micro发现了一个名为“LDAPNightmare”的恶意利用，它伪装成CVE-2024-49113的PoC，通过一个恶意代码仓库，诱骗安全研究人员下载并执行信息窃取型恶意软件。该恶意软件会从受感染机器上收集敏感数据，包括计算机信息、运行进程、网络详情和已安装更新等，并将其传输到攻击者控制的远程服务器。

无独有偶，2023年，Palo Alto Networks的研究人员也发现了一个新的恶意软件活动，该活动针对WinRAR的CVE-2023-40477漏洞。攻击者使用一个基于GeoServer漏洞CVE-2023-25157公开PoC代码修改而来的假PoC脚本，诱骗研究人员下载并执行VenomRAT有效载荷。一旦执行，该恶意软件会在系统中创建计划任务，每隔三分钟运行一次，以持续运行恶意软件，进而控制受害者系统、执行命令并窃取数据。

![](https://image.3001.net/images/20250120/1737338392_678dae18b15581c7a60c8.png!small)包含 “poc.exe” 的存储库

## **二、技术分析过程**

### **（1）LDAPNightmare攻击技术分析**

攻击者精心构建了一个看似合法的恶意代码仓库，其中的Python文件被替换为恶意可执行文件。当研究人员下载并执行该文件后，会释放并执行一个PowerShell脚本。该脚本随后建立计划任务，从Pastebin下载并执行另一个恶意脚本，最终收集受害者的公网IP地址，并将窃取的数据传输到外部FTP服务器。

SafeBreach Labs对CVE-2024-49113进行了深入研究，并开发出了一个PoC利用工具（概念验证漏洞），这个工具能够致使任何未打补丁的Windows服务器（不仅仅是域控制器）崩溃，来证明此漏洞的严重危害程度。根据Microsoft的分析发现，还可以进一步利用此漏洞导致远程代码执行。其次，研究人员确实验证了Microsoft的补丁修复了越界漏洞，并且该漏洞无法使修补的服务器崩溃。具体其攻击流程如下：

* 攻击者向受害服务器发送DCE/RPC请求。
* 受害服务器被触发，向攻击者的DNS服务器发送关于SafeBreachLabs.pro的DNS SRV查询。
* 攻击者的DNS服务器回复攻击者的主机名和LDAP端口。
* 受害服务器发送NBNS请求，以查找收到的主机名（攻击者的）的IP地址。
* 攻击者发送带有其IP地址的NBNS响应。
* 受害服务器成为LDAP客户端，向攻击者的机器发送CLDAP请求。
* 攻击者发送带有特定值的CLDAP转介响应包，导致LSASS崩溃并强制重启受害服务器。

![](https://image.3001.net/images/20250120/1737338435_678dae433f4bdc726d41f.png!small)LDAPNightmare攻击流程

### **（2）VenomRAT恶意软件活动技术分析**

Palo Alto Networks的安全研究人员发现了一个针对WinRAR中 CVE-2023-40477 漏洞的新恶意软件活动。该活动使用虚假的概念验证（PoC） 脚本来诱骗研究人员下载并执行VenomRAT有效载荷。虚假的PoC脚本基于跟踪的GeoServer中漏洞CVE-2023-25157公开可用的PoC代码。该代码已经过修改，以删除有关CVE-2023-25157漏洞详细信息的注释，并添加了下载和执行带有“检查依赖关系”注释的批处理脚本的其他代码。该脚本在%TEMP%/bat.bat创建批处理文件，连接到特定URL并运行响应内容，进而下载可执行文件并保存到%APPDATA%\Drivers\Windows.Gaming.Preview.exe，同时创建计划任务，每三分钟运行一次该可执行文件，以实现持久化运行。Windows.Gaming.Preview.exe 可执行文件是VenomRAT的变体，VenomRAT是一种远程访问木马（RAT）。VenomRAT可用于窃取数据、在受害者系统上执行命令以及远程控制系统。

Palo Alto Networks研究人员认为，该攻击活动背后的攻击者是以网络安全研究人员为目标的，以便控制与访问他们的系统并窃取他们的数据。研究人员还认为，攻击者还可能正在使用受感染的系统对其他组织发起进一步的攻击活动。

## **三、结论与建议**

这些假PoC攻击事件凸显了网络安全领域面临的严峻挑战。攻击者利用研究人员对安全漏洞的关注和研究热情，通过伪装成PoC的恶意软件，成功渗透并窃取了研究人员的敏感信息，甚至可能进一步利用这些系统对其他组织发动攻击。因此，安全研究人员在下载和执行来自在线仓库的代码时必须保持高度警惕，优先选择官方来源，仔细审查仓库内容，验证仓库所有者或组织的真实性，并关注社区反馈，寻找可能的安全风险警示。同时，用户应确保及时更新软件至最新版本，避免点击不明链接，并使用有效的安全解决方案来检测和阻止恶意软件。

**参考链接：**<https://hackread.com/fake-poc-exploit-hit-cybersecurity-researchers-malware/><https://hackread.com/fake-poc-script-researchers-download-venomrat/><https://www.safebreach.com/blog/ldapnightmare-safebreach-labs-publishes-first-proof-of-concept-exploit-for-cve-2024-49113/>

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

一、事件概述

二、技术分析过程

* （1）LDAPNightmare攻击技术分析
* （2）VenomRAT恶意软件活动技术分析

三、结论与建议

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