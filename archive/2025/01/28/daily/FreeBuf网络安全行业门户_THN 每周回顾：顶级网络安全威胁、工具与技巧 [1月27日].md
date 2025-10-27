---
title: THN 每周回顾：顶级网络安全威胁、工具与技巧 [1月27日]
url: https://www.freebuf.com/vuls/420917.html
source: FreeBuf网络安全行业门户
date: 2025-01-28
fetch_date: 2025-10-06T20:09:31.742683
---

# THN 每周回顾：顶级网络安全威胁、工具与技巧 [1月27日]

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

THN 每周回顾：顶级网络安全威胁、工具与技巧 [1月27日]

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

THN 每周回顾：顶级网络安全威胁、工具与技巧 [1月27日]

2025-01-27 18:09:00

所属地 上海

![image](https://image.3001.net/images/20250127/1737986469461597_717c28b2026f47c289e94b705859561c.png!small)

欢迎来到本周的网络安全快讯！你是否想过，原本用于保护医院的AI技术，也可能成为攻击的突破口？本周，我们将深入探讨AI驱动的威胁、法规更新的关键内容，以及医疗技术中亟待解决的漏洞。

在解析这些复杂话题的同时，我们也会为你提供应对这些挑战的深刻见解。想了解解决方案吗？它们比你想象的更聪明、更出人意料。让我们开始吧。

---

## **本周威胁**

**Juniper Networks路由器遭J-magic攻击**
在2023年中期至2024年中期，一场新的攻击活动针对企业级Juniper Networks路由器，利用特定条件植入名为J-magic的后门程序。该恶意软件是已有近25年历史的公开后门cd00r的变种，旨在建立与攻击者控制的IP地址和端口的反向连接。半导体、能源、制造业和信息技术（IT）行业是主要攻击目标。

---

## **头条新闻**

### **Palo Alto防火墙存在固件漏洞**

对Palo Alto Networks的三款防火墙型号（PA-3260、PA-1410和PA-415）的分析发现，它们存在已知的安全漏洞，可能被利用绕过安全启动并修改设备固件。Palo Alto Networks回应称，攻击者需先通过其他方式入侵PAN-OS软件并获取提升权限才能利用这些漏洞。该公司表示将与第三方合作，为部分设备开发固件更新。

### **PlushDaemon与韩国VPN供应商供应链攻击有关**

一个名为PlushDaemon的中国背景黑客组织在2023年对韩国一家虚拟专用网络（VPN）供应商发起供应链攻击，投放名为SlowStepper的恶意软件。该后门程序功能齐全，具备广泛的信息收集能力。该组织还利用Apache HTTP服务器的未知漏洞，并通过中间人（AitM）攻击入侵其他目标。自2019年以来，该组织已针对中国、台湾、香港、韩国、美国和新西兰的个人与实体发起攻击。

### **Mirai僵尸网络发起5.6 Tbps的DDoS攻击**

Cloudflare披露，一个由超过13,000台物联网设备组成的Mirai僵尸网络对东亚一家未具名的互联网服务提供商（ISP）发起了破纪录的5.6 Tbps分布式拒绝服务（DDoS）攻击，持续约80秒。每秒平均有5,500个独立源IP地址参与攻击，每个IP地址每秒贡献约1 Gbps流量。

### **LTE和5G实现中存在100多个漏洞**

一组学者披露了影响LTE和5G实现的119个安全漏洞，涉及Open5GS、Magma、OpenAirInterface等平台。攻击者可利用这些漏洞中断服务访问，甚至渗透到蜂窝核心网络。部分漏洞可被武器化，用于监控城市范围内的用户位置和连接信息，或对特定用户发起定向攻击。

### **前CIA分析师承认泄露绝密文件**

前美国中央情报局（CIA）分析师Asif William Rahman承认向未经授权的人员传输绝密国防信息（NDI），并试图掩盖这一行为。2024年10月，Rahman分享了由美国国家地理空间情报局和国家安全局准备的文件，内容涉及以色列攻击伊朗的计划。这些文件随后被一个名为“中东观察者”的Telegram账号泄露。Rahman已承认两项与国防相关的故意保留和传输机密信息的指控，预计将于2025年5月15日被判刑，最高可面临10年监禁。

---

## **‎️‍ 热门CVE漏洞**

你的常用软件可能隐藏着危险的安全漏洞——不要等到为时已晚！立即更新，提前防范威胁。本周的热门CVE包括：CVE-2025-23006（SonicWall）、CVE-2025-20156（Cisco Meeting Management）、CVE-2025-21556（Oracle Agile产品生命周期管理框架）、CVE-2025-0411（7-Zip）、CVE-2025-21613（go-git）、CVE-2024-32444（WordPress的RealHomes主题）、CVE-2024-32555（Easy Real Estate插件）、CVE-2016-0287（IBM i Access Client Solutions）、CVE-2024-9042（Kubernetes）。

---

## **全球网络安全动态**

### **印度与美国签署网络犯罪合作备忘录**

印度与美国签署了一份谅解备忘录（MoU），以加强网络犯罪调查合作。印度外交部（MEA）表示，该备忘录允许两国相关机构在利用网络威胁情报和数字取证进行刑事调查方面加强合作与培训。

### **ABB ASPECT-Enterprise、NEXUS和MATRIX产品存在严重漏洞**

ABB ASPECT-Enterprise、NEXUS和MATRIX系列产品中披露了100多个安全漏洞，攻击者可利用这些漏洞中断操作或执行远程代码。Zero Science Lab的Gjoko Krstikj因发现并报告这些漏洞而受到赞誉。

### **91%暴露的Exchange Server实例仍易受ProxyLogon攻击**

中国背景的Salt Typhoon黑客组织利用CVE-2021-26855（即ProxyLogon）漏洞进行初始访问。网络安全公司Tenable的分析显示，近30,000个暴露在外的Exchange实例中，91%仍未修复该漏洞。Salt Typhoon以在受害者网络中长期潜伏而闻名。

### **IntelBroker辞去BreachForums职务**

威胁行为者IntelBroker宣布辞去非法网络犯罪论坛BreachForums的所有者职务，理由是时间不足。该论坛曾多次被执法部门调查，基础设施被关闭，前任管理员被捕。创始人Conor Brian Fitzpatrick（又名Pompompurin）一年前被判刑，但最新法庭文件显示其判决已被撤销。

### **Cloudflare CDN漏洞泄露用户位置**

一名15岁的安全研究员发现，广泛使用的Cloudflare内容分发网络（CDN）中存在一种新的“去匿名化攻击”，可通过发送图片暴露用户位置。该漏洞允许攻击者在目标手机或笔记本电脑上安装易受攻击的应用时，提取目标250英里范围内的位置信息。

### **Belsen Group泄露Fortinet FortiGate防火墙配置**

鲜为人知的黑客组织Belsen Group在暗网上免费泄露了超过15,000台Fortinet FortiGate防火墙的配置数据，包括VPN用户凭据、设备序列号等信息。安全研究员Kevin Beaumont分析发现，这些数据可能是通过利用2022年10月披露的CVE-2022-40684漏洞收集的。

---

## **专家网络研讨会**

### **不再妥协：全速编写安全代码**

厌倦了安全拖慢开发进度，或冒险的捷径让你陷入风险？加入Palo Alto Networks产品管理副总裁Sarit Tager的研讨会，了解如何打破开发与安全的僵局，将智能、无缝的安全防护融入DevOps流程。

### **身份韧性的清晰路线图**

为身份安全漏洞带来的风险和低效而苦恼？加入Okta专家Karl Henrik Smith和Adam Boucher的研讨会，了解如何通过安全身份评估（SIA）制定清晰的路线图，强化身份防护。

---

## **网络安全工具**

### **Extension Auditor**

随着网络威胁日益复杂，Extension Auditor等工具对维护在线安全至关重要。该工具评估浏览器扩展的安全性和隐私风险，提供权限和潜在漏洞的清晰分析。

### **AD威胁狩猎工具**

这是一款简单但功能强大的PowerShell工具，可帮助检测Active Directory中的可疑活动，如密码喷洒攻击或暴力破解尝试。它提供实时警报、攻击模式智能分析和详细报告。

---

## **本周安全小贴士**

**基本网络安全实践**
要有效保护网络，无需复杂解决方案。使用VPN（如NordVPN）保护数据隐私，确保防火墙开启，及时更新软件和设备，使用强密码并考虑使用密码管理器，学习识别钓鱼攻击。这些简单措施可显著提升网络安全。

---

**结语**
本周快讯结束时，让我们聚焦医疗技术中的漏洞问题。这些漏洞凸显了加强安全措施和动态监管框架的迫切需求。如何更好地保护关键基础设施？你的专业知识至关重要。让我们保持对话，推动网络安全领域的进步。保持关注，持续参与。

**参考来源：**

> [THN Weekly Recap: Top Cybersecurity Threats, Tools and Tips [27 January]](https://thehackernews.com/2025/01/thn-weekly-recap-top-cybersecurity_27.html)

# 网络安全 # 企业安全

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