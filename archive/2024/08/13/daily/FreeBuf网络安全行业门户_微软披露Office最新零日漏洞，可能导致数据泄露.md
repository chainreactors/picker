---
title: 微软披露Office最新零日漏洞，可能导致数据泄露
url: https://www.freebuf.com/news/408346.html
source: FreeBuf网络安全行业门户
date: 2024-08-13
fetch_date: 2025-10-06T18:06:26.798130
---

# 微软披露Office最新零日漏洞，可能导致数据泄露

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

微软披露Office最新零日漏洞，可能导致数据泄露

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

微软披露Office最新零日漏洞，可能导致数据泄露

2024-08-12 09:57:12

所属地 上海

![](https://image.3001.net/images/20240812/1723428069_66b96ce55c8e121cfbdbb.png!small)

近日，微软披露了 Office 中一个未修补的零日漏洞，如果被成功利用，可能导致敏感信息在未经授权的情况下泄露给恶意行为者。

该漏洞被追踪为 CVE-2024-38200（CVSS 得分：7.5），被描述为一个欺骗漏洞，影响以下版本的 Office

* 32 位版本和 64 位版本的 Microsoft Office 2016
* 32 位版本和 64 位版本的 Microsoft Office LTSC 2021
* 适用于 32 位和 64 位系统的 Microsoft 365 企业应用程序
* 适用于 32 位和 64 位系统的 Microsoft Office 2019

微软在一份公告中提到：在基于网络的攻击场景中，攻击者可以托管一个网站，或利用一个接受或托管用户提供内容的受攻击网站，该网站包含一个特制文件专门利用该漏洞。

但是，攻击者无法强迫用户访问该网站。相反，攻击者必须诱导用户点击一个链接，通常是通过电子邮件或即时通信信息中的诱导方式，然后说服用户打开特制文件。

CVE-2024-38200的正式补丁预计将于8月13日正式发布。不过微软公司表示，他们已经确定了一种替代修复的方法，并已从2024年7月30日起通过 "功能飞行"（Feature Flighting）启用了该修复方法。

该公司还指出，虽然客户已经在所有支持版本的微软Office和微软365上得到了保护，但为了最大程度的规避安全风险，用户应在最终版本的补丁发布后立即更新。

微软对该漏洞进行了 "不太可能被利用 "的评估，并进一步概述了三种缓解策略--配置 "网络安全 "和 "安全漏洞"：

* 配置 "网络安全： 配置 "限制 NTLM：向远程服务器发出 NTLM 流量 "策略设置，允许、阻止或审计从运行 Windows 7、Windows Server 2008 或更高版本的计算机向任何运行 Windows 操作系统的远程服务器发出的 NTLM 流量。
* 将用户添加到受保护用户安全组，防止将 NTLM 用作身份验证机制
* 使用外围防火墙、本地防火墙并通过 VPN 设置阻止 TCP 445/SMB 从网络向外发送，以防止向远程文件共享发送 NTLM 身份验证信息

在披露该漏洞的同时，微软还表示其正在努力解决CVE-2024-38202 和 CVE-2024-21302两个零日漏洞，这些漏洞可能被利用来 "解除 "最新 Windows 系统的补丁，并重新引入旧漏洞。

上周，Elastic 安全实验室披露Windows智能应用控制（Smart App Control）和智能屏幕（SmartScreen）存在一个设计漏洞，该缺陷允许攻击者在不触发安全警告的情况下启动程序，至少自2018年以来一直在被利用。

智能应用控制是一项基于信任的安全功能，它使用微软的应用智能服务进行安全预测，并利用Windows的代码完整性功能来识别和阻止不受信任的（未签名的）或潜在危险的二进制文件和应用程序。

Elastic安全实验室认为，这一漏洞多年来一直被滥用，因为他们在VirusTotal中发现了多个利用此漏洞的样本，其中最早的提交时间超过六年。

> 参考来源：[Microsoft Warns of Unpatched Office Vulnerability Leading to Data Exposure (thehackernews.com)](https://thehackernews.com/2024/08/microsoft-warns-of-unpatched-office.html)

# 微软漏洞 # 零日漏洞 # Office漏洞

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