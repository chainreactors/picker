---
title: 0.0.0.0 Day漏洞曝光，谷歌、Safari、火狐等主流浏览器面临威胁
url: https://www.freebuf.com/news/408169.html
source: FreeBuf网络安全行业门户
date: 2024-08-10
fetch_date: 2025-10-06T18:05:10.922793
---

# 0.0.0.0 Day漏洞曝光，谷歌、Safari、火狐等主流浏览器面临威胁

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

0.0.0.0 Day漏洞曝光，谷歌、Safari、火狐等主流浏览器面临威胁

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

0.0.0.0 Day漏洞曝光，谷歌、Safari、火狐等主流浏览器面临威胁

2024-08-09 10:10:26

所属地 上海

![1723172357_66b586056c53f62fc6501.png!small?1723172357335](https://image.3001.net/images/20240809/1723172357_66b586056c53f62fc6501.png!small?1723172357335)

近日，一个名为 "0.0.0.0 Day "的重大安全漏洞在网络安全社区中引发了巨大反响，该漏洞导致数百万使用 Chrome、Firefox 和 Safari 等流行浏览器的用户受到潜在攻击。同时，该漏洞还允许恶意行为者访问私人网络（特别是 "本地主机"）中设备上存储的文件、信息、凭证和其他敏感数据。

## 什么是 0.0.0.0 Day漏洞？

0.0.0.0 Day漏洞是以色列网络安全初创公司 Oligo 新发现的漏洞，攻击者能够在补丁可用之前利用该漏洞。

这个漏洞是一个涉及 IP 地址 0.0.0.0 的零日漏洞。该漏洞被研究人员称为"0.0.0.0 Day"，它暴露了浏览器处理网络请求时的一个漏洞，可被滥用来访问敏感的本地服务。

这是一个存在多年的漏洞。研究人员发现，早在 2006 年就有报告称存在涉及 IP 地址的安全问题。

![1723169358_66b57a4ec83383af46bf6.png!small](https://image.3001.net/images/20240809/1723169358_66b57a4ec83383af46bf6.png!small)

图解公共网络如何使用 0.0.0.0 地址与专用网络和本地设备通信，来源：Oligo

正如报告中所提到的，该漏洞的技术细节涉及恶意网站欺骗浏览器，允许浏览器与运行在用户本地机器（localhost）上的 API（应用程序编程接口）进行交互。这些 API 通常是为应用程序内部通信而设计的，不应该从网站等外部来源访问。这些网站只需瞄准 0.0.0.0，而不是 localhost/127.0.0.1，就有可能在访问者的硬件上执行代码。通过利用 0.0.0.0 Day漏洞，攻击者有可能在未经授权的情况下访问存储在用户计算机上的敏感信息、窃取数据甚至启动恶意软件。

这项研究进一步凸显了浏览器安全漏洞十分令人担忧的现状。浏览器的设计目的是作为用户与潜在有害在线内容之间的屏障。然而，0.0.0.0 Day漏洞暴露了浏览器处理网络请求的弱点。不同浏览器在安全机制上的不一致性，可能会让恶意行为者访问用户的本地网络和在其上运行的服务。

![1723169395_66b57a737b30074d18891.png!small](https://image.3001.net/images/20240809/1723169395_66b57a737b30074d18891.png!small)

与 0.0.0.0 通信的网站数量，来源：Oligo

## 对市面上主流浏览器带来巨大影响

研究人员发现，几乎市面上的所有浏览器都可能受到该漏洞的影响，所以作为负责任披露的一部分，所有相关公司都已被告知，目前这些公司也都做出了相应的应对措施，具体如下：

* **Chrome 零日漏洞：** 谷歌 Chrome 浏览器是全球最流行的浏览器，无疑是攻击者的首要目标。如果成功利用0.0.0.0 Day漏洞，攻击者就可以绕过 Chrome 浏览器的安全机制，访问用户的本地网络。这可能会暴露存储在用户计算机上的敏感数据，如果用户是远程办公，还可能危及企业网络，甚至为安装恶意软件提供便利。
* **火狐零日漏洞：** 火狐浏览器虽然不像 Chrome 浏览器那样被广泛使用，但仍然是许多用户的首选。成功利用 0.0.0.0 Day漏洞可能会给 Firefox 用户带来类似的后果。攻击者有可能访问本地网络、窃取数据或发起恶意软件攻击。
* **Safari 零日漏洞：**苹果公司的 Safari 浏览器是苹果设备上的默认浏览器，也有可能受到 0.0.0.0 Day 漏洞的攻击。虽然苹果公司以强大的安全性著称，但这一漏洞凸显了时刻保持警惕的必要性。成功的漏洞利用可能会让攻击者访问用户 Mac 或 iOS 设备上的本地网络，从而可能泄露敏感数据或为进一步攻击提供便利。

针对这一安全漏洞，苹果和谷歌更新了正在努力解决这一问题的方法。报告显示，在即将发布的 macOS 15 Sequoia 测试版中，苹果 Safari 将阻止所有查询 0.0.0.0 IP 地址的尝试。同样，谷歌 Chrome 浏览器的安全团队也在努力修复漏洞。谷歌正在推出阻止访问 0.0.0.0 的更新，预计将在 Chrome 133 中完全实施。

微软已经在 Windows 操作系统中阻止了对 0.0.0.0 IP 地址的访问。然而，Mozilla 采取了不同的立场。Mozilla 发言人表示，担心实施更严格的限制可能会带来严重的兼容性问题。由于有关标准的讨论和对这些兼容性风险的评估仍在进行中，火狐尚未实施拟议的限制。相反，Mozilla 计划继续参与这一进程，以确保采取一种平衡的方法。

0.0.0.0 Day 漏洞的发现凸显了在日益复杂的威胁环境中维护浏览器安全所面临的持续挑战。浏览器开发商必须继续投资研发，时刻领先于网络犯罪分子。同时，用户也必须保持警惕，以保护自己免受新威胁的侵害。

> 参考来源：https://thecyberexpress.com/chrome-safari-mozilla-zero-day-vulnerability/

# 零日漏洞 # 火狐浏览器 # 谷歌 Chrome # Safari浏览器

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

什么是 0.0.0.0 Day漏洞？

对市面上主流浏览器带来巨大影响

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