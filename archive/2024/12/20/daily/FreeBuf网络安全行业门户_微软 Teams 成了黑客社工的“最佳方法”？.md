---
title: 微软 Teams 成了黑客社工的“最佳方法”？
url: https://www.freebuf.com/news/418092.html
source: FreeBuf网络安全行业门户
date: 2024-12-20
fetch_date: 2025-10-06T19:38:33.848065
---

# 微软 Teams 成了黑客社工的“最佳方法”？

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

微软 Teams 成了黑客社工的“最佳方法”？

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

微软 Teams 成了黑客社工的“最佳方法”？

2024-12-19 14:20:56

所属地 上海

一项新的社会工程活动显示，大量攻击者利用微软Teams作为部署已知恶意软件DarkGate的手段。Trend Micro研究人员Catherine Loveria、Jovit Samaniego和Gabriel Nicoleta表示，“攻击者通过微软Teams电话进行社会工程，冒充用户的客户并获得远程访问他们系统的权利。攻击者未能安装微软远程支持应用程序，但成功指示受害者下载AnyDesk，这是一种常用于远程访问的工具。”

![](https://image.3001.net/images/20241219/1734589848_6763bd9848ef08657264d.png!small)

据网络安全公司Rapid7最近的报告，攻击者向目标的电子邮箱发送数千封邮件，然后通过微软Teams假装成外部供应商的员工接触目标。随后攻击者指示受害者在其系统上安装AnyDesk，远程访问随后被用于传送多个负载，包括凭据窃取工具和DarkGate恶意软件。

自2018年以来一直活跃的DarkGate是一种远程访问木马（RAT），后来演变为一种恶意软件即服务（MaaS）产品，其多种功能包括凭据窃取、键盘记录、屏幕捕捉、音频录制和远程桌面。过去一年针对DarkGate活动的分析表明，该恶意软件已通过使用AutoIt和AutoHotKey两条不同的攻击链进行分发。在Trend Micro检查的事件中，恶意软件可通过一个名为AutoIt脚本进行部署。

虽然在任何数据外泄活动发生之前攻击已被阻止，但这些发现表明攻击者如何使用多种初始访问途径传播恶意软件。因此安全专家建议组织启用多因素身份验证（MFA）、将批准的远程访问工具列入白名单、阻止未验证的应用程序，并彻底审核第三方技术支持提供商以消除语音钓鱼风险。

该事态进展正值各类网络钓鱼活动激增之时，这些活动利用各种诱惑和技巧欺骗受害者对信息进行泄露：

1. 一个大规模的YouTube定向活动中，假装成知名品牌，通过电子邮件联系内容创作者，试图进行潜在的推广、合作提案和市场合作，并敦促他们点击链接签署协议，部署Lumma Stealer。
2. 一场利用附带PDF文件的网络钓鱼邮件的活动，该PDF内含有一个二维码，用户扫描后会被引导到一个假的Microsoft 365登录页面以窃取凭据。
3. 利用Cloudflare Pages和Workers的信任设置假网站，模仿Microsoft 365的登录页面和假的CAPTCHA验证，号称为查看或下载文档。
4. 使用HTML电子邮件附件伪装成合法文档如发票或人力资源政策但含有嵌入的JavaScript代码，以执行恶意操作如引导用户访问钓鱼网站、窃取凭据，以及在修复错误的名义下诱使用户运行任意命令。
5. 利用可靠平台如Docusign、Adobe InDesign和Google Accelerated Mobile Pages (AMP)的电子邮件网络钓鱼活动，诱骗用户点击旨在窃取其凭据的恶意链接。
6. 声称来自Okta支持团队的网络钓鱼企图，以获取用户凭据并入侵组织系统。

针对印度用户的网络钓鱼信息通过WhatsApp分发，指示接收者安装恶意银行或用于Android设备的实用程序应用程序，能够窃取财务信息。攻击者也往往迅速利用全球事件，将其纳入到他们的网络钓鱼活动中，通常抓住紧迫性和情感反应操作受害者，诱使他们执行意外操作。这些活动还伴随有域名注册，使用与事件相关的关键词。

“备受瞩目的全球事件，包括体育锦标赛和产品发布，会吸引网络罪犯试图利用公众的兴趣，”Palo Alto Networks Unit 42表示，“这些罪犯注册欺骗性域名模仿官方网站，以出售假冒商品和提供欺诈服务。”

参考来源：<https://thehackernews.com/2024/12/attackers-exploit-microsoft-teams-and.html>

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