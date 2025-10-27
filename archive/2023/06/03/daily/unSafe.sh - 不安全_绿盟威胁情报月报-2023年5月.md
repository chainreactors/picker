---
title: 绿盟威胁情报月报-2023年5月
url: https://buaq.net/go-166980.html
source: unSafe.sh - 不安全
date: 2023-06-03
fetch_date: 2025-10-04T11:44:58.194496
---

# 绿盟威胁情报月报-2023年5月

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

![](https://8aqnet.cdn.bcebos.com/f5470da3205b1ab2849f68bd67024d09.jpg)

绿盟威胁情报月报-2023年5月

阅读： 55月，绿盟科技威胁情报中心（NTI）发布了多个漏洞和威胁事件通告，其中，本月微软月度更新修复的漏洞中，严重程度为关键（Critical）的漏洞有 6 个，
*2023-6-2 18:23:23
Author: [blog.nsfocus.net(查看原文)](/jump-166980.htm)
阅读量:34
收藏*

---

阅读： 5

5月，绿盟科技威胁情报中心（NTI）发布了多个漏洞和威胁事件通告，其中，本月微软月度更新修复的漏洞中，严重程度为关键（Critical）的漏洞有 6 个，重要（Important）漏洞有 32 个，其中包括 3 个 0day 漏洞： Win32k 权限提升漏洞（CVE-2023-29336） 安全启动安全功能绕过漏洞（CVE-2023-24932） Windows OLE 远程执行代码漏洞（CVE-2023-29325） 请相关用户尽快更新补丁进行防护。

在本月的威胁事件中，RA Group组织修改泄露的Babuk勒索软件源码并对三个美国组织和一个韩国组织进行攻击。

以上所有漏洞情报和威胁事件情报、攻击组织情报，以及关联的IOC，均可在绿盟威胁情报中心获取，网址：<https://nti.nsfocus.com/>

## **一、******漏洞态势****

2023年05月绿盟科技安全漏洞库共收录52个漏洞, 其中高危漏洞8个，微软高危漏洞8个。

![](http://blog.nsfocus.net/wp-content/uploads/2023/06/WeChat4c97154d2658e0a2757400a9e01e7c2c-300x241.png)

\* 数据来源：绿盟科技威胁情报中心，本表数据截止到2023.06.02

注：绿盟科技漏洞库包含应用程序漏洞、安全产品漏洞、操作系统漏洞、数据库漏洞、网络设备漏洞等；

## **二、******威胁事件****

1. RA group使用泄露的 Babuk 源代码攻击美国和韩国

【标签】Babuk,RA

【时间】2023-05-31

【简介】

RA Group组织修改泄露的Babuk勒索软件源码并对三个美国组织和一个韩国组织进行攻击。

【参考链接】

<https://blog.talosintelligence.com/ra-group-ransomware/>

【防护措施】

绿盟威胁情报中心关于[该事件](https://nti.nsfocus.com/event?query=ce5f278ed8edde039c82ed2a77f851d8cbd90168&type=all)提取4条IOC；绿盟安全平台与设备已集成相应情报数据，为客户提供相关防御检测能力。

2. 眼鹰的子组？来自Hagga组织的近期攻击活动分析

【标签】Hagga

【时间】2023-05-19

【简介】

在对南美洲相关APT组织盲眼鹰进行追踪时发现自2022年至今，从哥伦比亚上传了上百个诱饵pdf文件，这些诱饵pdf大多通过电子邮件进行传播，这些诱饵常 伪装成哥伦比亚的相关机构，包括哥伦比亚司法部门、税务和海关总局、哥伦比亚银行Davivienda、财务部、交通部、律师事务所等。这些pdf文件在正文中 嵌入了压缩包密码，并诱导受害者点击短链接下载压缩包，解压后点击执行伪装为pdf的VBS脚本，从而开启一个复杂的多阶段无文件感染链，最终加载远控软件。

【防护措施】

绿盟威胁情报中心关于[该事件](https://nti.nsfocus.com/event?query=ce5f278ed8edde039c82ed2a77f851d8cbd90168&type=all)提取10条IOC；绿盟安全平台与设备已集成相应情报数据，为客户提供相关防御检测能力。

3. 疑似APT组织TA569近期针对俄罗斯与德国的钓鱼攻击活动

【标签】TA569

【时间】2023-05-11

【简介】

2023年4月18日，绿盟科技伏影实验室在日常威胁狩猎中，发现一组针对俄罗斯的鱼叉式钓鱼邮件攻击事件。伏影实验室对该事件进行关联分析后，确认该攻 击者也对德国发动了类似的钓鱼攻击。

该攻击者在活跃时间、攻击目标、工具类型、工具内特征方面与已知黑客组织TA569有较高相似性，本次活动很可能是该组织在2023年2月的系列活动的延续。

【防护措施】

绿盟威胁情报中心关于[该事件](https://nti.nsfocus.com/event?query=ce5f278ed8edde039c82ed2a77f851d8cbd90168&type=all)提取10条IOC；绿盟安全平台与设备已集成相应情报数据，为客户提供相关防御检测能力。

4. Linux恶意软件加强了拉撒路与3CX供应链攻击之间的联系

【标签】3CX

【时间】2023-05-11

【简介】

研究人员发现了一个新的Lazarus Operation DreamJob活动，目标是Linux用户。Operation DreamJob是一系列活动的名称，该组织使用社会工程技术来达到 其目标，并以虚假的工作机会为诱饵。攻击者提供一个假的汇丰银行工作机会作为诱饵，直到最后的有效载荷：SimplexTea Linux后门通过OpenDrive云存储 帐户分发。 【参考链接】

<https://www.welivesecurity.com/2023/04/20/linux-malware-strengthens-links-lazarus-3cx-supply-chain-attack/>

【防护措施】

绿盟威胁情报中心关于[该事件](https://nti.nsfocus.com/event?query=ce5f278ed8edde039c82ed2a77f851d8cbd90168&type=all)提取10条IOC；绿盟安全平台与设备已集成相应情报数据，为客户提供相关防御检测能力。

5. APT组织Donot近期以我国相关信息为诱饵的网络钓鱼活动

【标签】Donot

【时间】2023-05-16

【简介】

5月4日，绿盟科技伏影实验室观测到APT组织Donot（肚脑虫）的一次网络钓鱼活动。Donot攻击者在本次活动中使用了名为“Chinese Delegation.doc”（中国 代表团）的钓鱼文档，直接目标疑似为巴基斯坦方面负责中巴关系的外交人员。Donot在本次活动中使用的攻击手法与近期该组织常用手法一致，是一种由宏 代码、多重shellcode以及组件化的木马程序构成的特殊钓鱼流程。

【防护措施】

绿盟威胁情报中心关于[该事件](https://nti.nsfocus.com/event?query=ce5f278ed8edde039c82ed2a77f851d8cbd90168&type=all)提取10条IOC，；绿盟安全平台与设备已集成相应情报数据，为客户提供相关防御检测能力。

6. Turla使用全新工具集来攻击政府

【标签】Turla

【时间】2023-05-19

【简介】

Turla在过去18个月通过一系列活动攻击政府和国际组织并且快速迭代其工具集，同时在其中一次攻击中劫持了Crambus组织的基础设施。

【参考链接】

<https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/waterbug-espionage-governments>

【防护措施】

绿盟威胁情报中心关于[该事件](https://nti.nsfocus.com/event?query=ce5f278ed8edde039c82ed2a77f851d8cbd90168&type=all)提取10条IOC，；绿盟安全平台与设备已集成相应情报数据，为客户提供相关防御检测能力。

7. [伊朗Agrius黑客使用Moneybird勒索软件攻击以色列组织](https://ti.nsfocus.com/security-news/IlP2t)

【标签】Moneybird

【时间】2023-05-26

【简介】

名为阿格里乌斯的伊朗威胁行为者正在利用一种名为“钱鸟”的新型勒索软件攻击以色列组织。Agrius，也被称为Pink Sandstorm(以前的Americium)，曾在勒索软件感染的幌子下对以色列进行破坏性的数据清除攻击。微软认为，伊朗情报和安全部(MOIS)也是“浑水”的运营者。已知它至少从2020年12月开始活跃。

【参考链接】

<https://ti.nsfocus.com/security-news/IlP2t>

【防护措施】

绿盟安全平台与设备已集成相应情报数据，为客户提供相关防御检测能力。

8. [Rheinmetall遭到BlackBasta勒索软件攻击](https://ti.nsfocus.com/security-news/IlP2L)

【标签】BlackBasta

【时间】2023-05-26

【简介】

2023年5月19日星期五，德国武器制造商莱茵金属公司(Rheinmetall)承认其一家私营子公司发生了网络事件。BlackBasta勒索软件组织已经通过其泄密网站宣称对此次攻击负责。

【参考链接】

<https://ti.nsfocus.com/security-news/IlP2L>

【防护措施】

绿盟安全平台与设备已集成相应情报数据，为客户提供相关防御检测能力。

9. [Kimsuky组织再次使用高级侦察恶意软件](https://ti.nsfocus.com/security-news/IlP1X)

【标签】Kimsuky

【时间】2023-05-25

【简介】

据报道，朝鲜的APT组织Kimsuky最近被发现使用一款名为RandomQuery的定制恶意软件，作为一项侦察和信息窃取行动的一部分。“最近，Kimsuky一直在持续地分发定制恶意软件，作为侦察活动的一部分，以便进行后续攻击”。

【参考链接】

<https://ti.nsfocus.com/security-news/IlP1X>

【防护措施】

绿盟安全平台与设备已集成相应情报数据，为客户提供相关防御检测能力。

10. [MalasLocker勒索软件入侵Zimbra服务器窃取邮件和加密文件](https://ti.nsfocus.com/security-news/IlP0l)

【标签】MalasLocker

【时间】2023-05-19

【简介】

一种新的勒索软件操作是入侵Zimbra服务器以窃取电子邮件和加密文件。然而，威胁行为者并没有要求支付赎金，而是声称要求向慈善机构捐款以提供加密器并防止数据泄露。被BleepingComputer称为MalasLocker的勒索软件行动于2023年3月底开始对Zimbra服务器进行加密，受害者在BleepingComputer和Zimbra论坛上都报告说他们的电子邮件已加密。

【参考链接】

<https://ti.nsfocus.com/security-news/IlP0l>

【防护措施】

绿盟安全平台与设备已集成相应情报数据，为客户提供相关防御检测能力。

**版权声明**

文章来源: http://blog.nsfocus.net/monthlyreport202305/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)