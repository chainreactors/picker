---
title: FreeBuf 周报 |  阿里云某机房着火超30个小时；甲骨文Weblogic服务器被黑客入侵
url: https://www.freebuf.com/news/411068.html
source: FreeBuf网络安全行业门户
date: 2024-09-15
fetch_date: 2025-10-06T18:26:01.023165
---

# FreeBuf 周报 |  阿里云某机房着火超30个小时；甲骨文Weblogic服务器被黑客入侵

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

FreeBuf 周报 | 阿里云某机房着火超30个小时；甲骨文Weblogic服务器被黑客入侵

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

FreeBuf 周报 | 阿里云某机房着火超30个小时；甲骨文Weblogic服务器被黑客入侵

2024-09-14 15:48:12

所属地 上海

各位 Buffer 周末好，以下是本周「FreeBuf周报」，我们总结推荐了本周的热点资讯、安全事件、一周好文和省心工具，保证大家不错过本周的每一个重点！![](https://image.3001.net/images/20220923/1663923572_632d7574ead5a97f52086.jpg!small)

## 热点资讯

### 1. 为推送定制化广告，福特汽车新专利拟广泛采集驾驶员数据

###

福特公司新申请的一项技术专利引发了人们对隐私问题的关注 ，该专利以推送定制化车载广告为目的，广泛收集驾驶员数据，包括车内对话。

### 2. AI大模型新型噪声攻击曝光，可绕过最先进的后门检测

罗德岛大学的研究人员在一篇论文中提出了一种新颖的后门攻击方法，利用白高斯噪声的功率谱密度作为触发器，不仅提高了攻击的可行性和普遍性，在模型中都取得了很高的平均攻击成功率，而且不会对非受害者造成显著干扰。

### 3. 利用屏幕截图窃取秘钥，这个恶意软件受黑客追捧

一款名为 SpyAgent 的新型安卓恶意软件近期被发现可利用光学字符识别（OCR）技术，从存储在移动设备上的截图中窃取加密货币钱包恢复短语。

### 4. WhatsApp“阅后即焚”功能曝漏洞，黑客可反复查看

全球拥有20亿用户的即时通讯工具 WhatsApp最近修复了一个十分重要的隐私漏洞，该漏洞能允许攻击者多次查看用户发送的“阅后即焚”（View once）内容。

### 5. 新型 PIXHELL 声音攻击能从 LCD 屏幕噪音中泄露信息

以色列内盖夫本古里安大学（Ben Gurion University of the Negev）的研究人员发现，一种被称为 “PIXHELL”的新型侧信道攻击可通过突破“音频间隙”攻击气隙系统（Air-gapped ）中的计算机，并利用屏幕上像素产生的噪声来窃取敏感信息。

## 安全事件

### 1. SonicWall SSL VPN曝出高危漏洞，可能导致防火墙崩溃

近日，有黑客利用 SonicWall SonicOS 防火墙设备中的一个关键安全漏洞入侵受害者的网络。这个不当访问控制漏洞被追踪为 CVE-2024-40766，影响到第 5 代、第 6 代和第 7 代防火墙。SonicWall于8月22日对其进行了修补，并警告称其只影响防火墙的管理访问界面。

### 2. 卡巴斯基发布的 EDR 防护杀手，被勒索组织广泛使用

近期，RansomHub 勒索组织一直通过利用卡巴斯基的合法工具 TDSSKiller 来禁用目标系统上的端点检测和响应 (EDR) 服务。在攻破防御系统后，RansomHub 又部署了 LaZagne 凭证采集工具，试图从各种应用程序数据库中提取有助于在网络上横向移动的登录信息。

### 3. 针对程序猿的新型骗局，黑客借招聘Python传播恶意软件

近期，有攻击者利用虚假的求职面试和编码测试诱骗开发人员下载运行恶意软件。该活动被称为 VMConnect， 疑似与朝鲜 Lazarus 集团有关 。

### 4. 阿里云机房着火超30个小时，云服务宕机，AWS趁火打劫？

9月10日，阿里云服务又宕机了。此次宕机的原因是，新加坡可用区 C 数据中心的机房发生了一场严重的火灾。火灾原因是锂电池爆炸，导致机房升温和燃烧。离谱的是，自10日早上8点到11日晚上8点，火灾持续了整整36小时，仍未完全扑灭。

### 5. 只针对Linux，甲骨文Weblogic服务器被黑客入侵

网络安全研究人员发现了一场针对Linux环境的新恶意软件活动，目的是进行非法加密货币挖矿和传播僵尸网络恶意软件。云安全公司Aqua指出，这项活动特别针对甲骨文Weblogic服务器，旨在传播一种名为Hadooken的恶意软件。

## 一周好文共读

### 1. 韩国N号房2.0事件大爆发，Deepfake究竟有多“邪恶”？

在这次事件中，韩国男性用自己熟人的kakaotalk头像（类似微信的聊天软件）或上传到instagram的照片（社交软件）制造“deepfake视频”并戏弄女性。导致以女性为主的近千人受到侵害，200多所学校牵涉其中，初高中生未成年人作案比例惊人，网友直呼是“韩国N号房2.0版本”案件再现。 【[阅读全文](https://www.freebuf.com/articles/neopoints/410664.html)】

![1719383456_667bb5a05000ee7693c04.png](https://image.3001.net/images/20240914/1726300112_66e53fd089a57b3ab7bd4.png!small)

### 2. 两个影响WPS Office的任意代码执行漏洞分析

ESET研究人员在WPS Office for Windows中发现了一个代码执行漏洞（CVE- 2024-7262），该漏洞正被韩国网络间谍组织APT-C-60滥用。在分析了根本原因后，另一种任意代码执行漏洞（CVE-2924-7263）浮出水面。目前，两个漏洞均已被修复。 【[阅读全文](https://www.freebuf.com/articles/paper/409990.html)】

![1](https://image.3001.net/images/20240914/1726300384_66e540e0a940f56441539.png!small)

### 3. 攻防利器 | openCTI开源威胁情报管理平台的思考与详细部署

###

最近公司刚做了安全成熟度评估，结果显示为缺乏安全工具的支撑，例如bas、hids、hips、sip、数据dlp、零信任等等，众所周知，企业对于安全方面的投入，一年花个四五百万的都算是少了，不想花钱，又害怕开源的软件集成后存在安全风险，那就只有部署一些对现有环境没有影响，且不会导致公司信息泄露的开源软件，于是所有矛头对准了开源的威胁情报平台。 【[阅读全文](https://www.freebuf.com/sectool/410121.html)】

![1719198198_6678e1f6016c872e387dd.png!small?1719198198682](https://image.3001.net/images/20240914/1726300493_66e5414d689f10f794a40.png!small)

## 省心工具

### Invoke-Maldaptive：一款针对LDAP SearchFilter的安全分析工具

MaLDAPtive 是一款针对LDAP SearchFilter的安全分析工具，旨在用于对LDAP SearchFilter 执行安全解析、混淆、反混淆和安全检测。 【[阅读全文](https://www.freebuf.com/sectool/410429.html)】

![1719564735_667e79bfbf809fcd7dcff.png!small](https://image.3001.net/images/20240914/1726300612_66e541c4bb6557fa573dd.png!small)

### 2. SSHamble：一款针对SSH技术安全的研究与分析工具

SSHamble是一款功能强大的SSH技术安全分析与研究工具，该工具基于Go语言开发，可以帮助广大研究人员更好地分析SSH相关的安全技术与缺陷问题。 【[阅读全文](https://www.freebuf.com/sectool/410398.html)】

![1719567578_667e84da15a4003f28931.jpg!small](https://image.3001.net/images/20240914/1726300663_66e541f7126d119ee1dd8.jpg!small)

### 3. 如何使用VeilTransfer评估和提升组织的数据安全态势

VeilTransfer是一款功能强大的企业数据安全检测与增强工具，该工具基于Go语言开发，旨在帮助广大研究人员完成企业环境下的数据安全测试并增强检测能力。 【[阅读全文](https://www.freebuf.com/sectool/410397.html)】

![](https://image.3001.net/images/20240914/1726300730_66e5423a419e0293491c9.png!small)

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

热点资讯

* 1. 为推送定制化广告，福特汽车新专利拟广泛采集驾驶员数据
* 2. AI大模型新型噪声攻击曝光，可绕过最先进的后门检测
* 3. 利用屏幕截图窃取秘钥，这个恶意软件受黑客追捧
* 4. WhatsApp“阅后即焚”功能曝漏洞，黑客可反复查看
* 5. 新型 PIXHELL 声音攻击能从 LCD 屏幕噪音中泄露信息

安全事件

* 1. SonicWall SSL VPN曝出高危漏洞，可能导致防火墙崩溃
* 2. 卡巴斯基发布的 EDR 防护杀手，被勒索组织广泛使用
* 3. 针对程序猿的新型骗局，黑客借招聘Python传播恶意软件
* 4. 阿里云机房着火超30个小时，云服务宕机，AWS趁火打劫？
* 5. 只针对Linux，甲骨文Weblogic服务器被黑客入侵

一周好文共读

* 1. 韩国N号房2.0事件大爆发，Deepfake究竟有多“邪恶”？
* 2. 两个影响WPS Office的任意代码执行漏洞分析
* 3. 攻防利器 | openCTI开源威胁情报管理平台的思考与详细部署

省心工具

* Invoke-Maldaptive：一款针对LDAP SearchFilter的安全分析工具
* 2. SSHamble：一款针对SSH技术安全的研究与分析工具
* 3. 如何使用VeilTransfer评估和提升组织的数据安全态势

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