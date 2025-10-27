---
title: 威胁升级！伊朗APT34组织针对阿联酋及海湾关键基础设施发动攻击
url: https://www.freebuf.com/news/412761.html
source: FreeBuf网络安全行业门户
date: 2024-10-15
fetch_date: 2025-10-06T18:51:28.279956
---

# 威胁升级！伊朗APT34组织针对阿联酋及海湾关键基础设施发动攻击

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

威胁升级！伊朗APT34组织针对阿联酋及海湾关键基础设施发动攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

威胁升级！伊朗APT34组织针对阿联酋及海湾关键基础设施发动攻击

2024-10-14 10:07:41

所属地 上海

![1728871484_670c7c3c8f46162e0a2bf.png!small](https://image.3001.net/images/20241014/1728871484_670c7c3c8f46162e0a2bf.png!small)

伊朗国家支持的黑客组织 APT34（又名 OilRig）最近升级了其活动，针对阿拉伯联合酋长国和海湾地区的政府和关键基础设施实体发起了新的攻击。

在趋势科技研究人员发现的这些攻击中，OilRig 部署了一个新的后门，以微软 Exchange 服务器为目标窃取凭证，还利用 Windows CVE-2024-30088 漏洞提升了他们在受攻击设备上的权限。

除了这些活动，趋势科技还发现 OilRig 与另一个参与勒索软件攻击的伊朗 APT 组织 FOX Kitten 之间存在联系。

## 最新的 OilRig 攻击链

趋势科技表示，这种攻击首先会利用有漏洞的 Web 服务器上传 Web shell，使攻击者能够执行远程代码和 PowerShell 命令。

一旦 Web shell 处于活动状态，OilRig 就会利用它部署其他工具，包括一个旨在利用 Windows CVE-2024-30088 漏洞的组件。

CVE-2024-30088 是微软在 2024 年 6 月修复的一个高严重性权限升级漏洞，它使攻击者能够将权限升级到 SYSTEM 级别，从而对被入侵设备拥有重大控制权。

微软已承认存在 CVE-2024-30088 的概念验证漏洞，但尚未在其安全门户网站上将该漏洞标记为主动漏洞。CISA 也没有在 ts Known Exploited Vulnerability 目录中报告该漏洞曾被利用。

随后，OilRig 注册了一个密码过滤 DLL，以在密码更改事件中拦截明文凭证，然后下载并安装远程监控和管理工具 “ngrok”，用于通过安全隧道进行隐蔽通信。

威胁行为者的另一种新策略是利用内部 Microsoft Exchange 服务器，通过难以察觉的合法电子邮件流量窃取凭证和外流敏感数据。

![1728871581_670c7c9df33a4c0566e90.png!small](https://image.3001.net/images/20241014/1728871581_670c7c9df33a4c0566e90.png!small)

从 Exchange 窃取密码的后门，来源：趋势科技

名为 “StealHook ”的新型后门为密码外泄提供了便利，而趋势科技称，政府基础设施通常被用作支点，使这一过程看起来合法。

对此，趋势科技在报告中解释称这一阶段的关键目标是捕获窃取的密码，并将其作为电子邮件附件传输给攻击者。

此外，我们还观察到，威胁行为者利用带有被盗密码的合法账户，通过政府 Exchange 服务器路由这些电子邮件"。

![attack-chain.jpg](https://image.3001.net/images/20241014/1728872246_670c7f363ae8ae801b040.jpg!small)

石油钻机的最新攻击链，来源：趋势科技

趋势科技称，StealHook与OilRig在过去的活动中使用的后门（如Karkoff）之间存在代码相似性，因此最新的恶意软件似乎是一种进化，而不是从头开始的新创造。

这也并非 OilRig 首次使用微软 Exchange 服务器作为其攻击的活动组件。将近一年前，赛门铁克曾报告称，APT34 在内部部署的 Exchange 服务器上安装了一个名为 “PowerExchange ”的 PowerShell 后门，能够通过电子邮件接收和执行命令。

该威胁行为体在中东地区仍然非常活跃，它与 FOX Kitten 的关系目前还不清楚，但令人担忧的是，它有可能将勒索软件添加到其攻击武器库中。

据趋势科技称，由于大多数目标实体都在能源领域，因此这些组织一旦运营中断那么将影响十分广泛。

> 参考来源：[Iranian hackers now exploit Windows flaw to elevate privileges (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/oilrig-hackers-now-exploit-windows-flaw-to-elevate-privileges/)

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

最新的 OilRig 攻击链

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