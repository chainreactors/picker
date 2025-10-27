---
title: 微软运用欺骗性策略大规模打击网络钓鱼活动
url: https://www.freebuf.com/news/413252.html
source: FreeBuf网络安全行业门户
date: 2024-10-22
fetch_date: 2025-10-06T18:51:28.234202
---

# 微软运用欺骗性策略大规模打击网络钓鱼活动

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

微软运用欺骗性策略大规模打击网络钓鱼活动

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

微软运用欺骗性策略大规模打击网络钓鱼活动

2024-10-21 09:49:30

所属地 上海

![1729474900_6715b154c131aeda5a09f.png!small](https://image.3001.net/images/20241021/1729474900_6715b154c131aeda5a09f.png!small)

微软正在利用欺骗性策略来打击网络钓鱼行为者，方法是通过访问 Azure 生成外形逼真的蜜罐租户，引诱网络犯罪分子进入以收集有关他们的情报。

利用收集到的数据，微软可以绘制恶意基础设施地图，深入了解复杂的网络钓鱼操作，大规模破坏网络钓鱼活动，识别网络犯罪分子，并显著降低其活动速度。

在 BSides Exeter 会议上，Microsoft 首席安全软件工程师 Ross Bevington 描述了这种策略及其对网络钓鱼活动的破坏性影响，他称自己为 Microsoft 的“欺骗主管”。

Bevington 在现已退役的 code.microsoft.com 上创建了一个“混合高交互蜜罐”，以收集有关行为者的威胁情报，这些行为者既有技能较低的网络犯罪分子，也有针对Microsoft基础设施的民族国家团体。

## 网络钓鱼成功的假象

目前，Bevington 和他的团队通过利用欺骗技术来打击网络钓鱼，该技术使用整个 Microsoft 租户环境作为蜜罐，具有自定义域名、数千个用户帐户以及内部通信和文件共享等活动。

公司或研究人员通常会设置一个蜜罐，等待威胁者发现并采取行动。除了将攻击者从真实环境中转移出来，“巢穴 ”还可以收集入侵系统所用方法的情报，然后将其应用于合法网络。

虽然 Bevington 的概念大致相同，但其不同之处在于，它将游戏带到攻击者面前，而不是等待威胁者找到入侵的方法。

这位研究人员在 BSides Exeter 的演讲中说，主动方法包括访问 Defender 识别出的活动钓鱼网站，并输入蜜罐租户的凭据。

由于凭据不受双因素身份验证的保护，而且租户中充斥着逼真的信息，攻击者很容易进入，并开始浪费时间寻找陷阱的迹象。

微软表示，它每天监控大约 2.5 万个钓鱼网站，向其中约 20% 的网站提供蜜罐凭据；其余网站则被验证码或其他反僵尸机制拦截。

一旦攻击者登录到假冒的租户（5% 的情况下会发生），它就会打开详细的日志记录，跟踪他们的每一个动作，从而了解威胁行为者的战术、技术和程序。收集到的情报包括 IP 地址、浏览器、位置、行为模式、是否使用 VPN 或 VPS 以及他们依赖的网络钓鱼工具包。此外，当攻击者试图与环境中的虚假账户进行交互时，微软会尽可能减慢响应速度。

一直以来，微软都在收集可操作的数据，这些数据可供其他安全团队用来创建更复杂的配置文件和更好的防御措施。

Bevington 提到，他们以这种方式收集的 IP 地址中，只有不到 10% 可以与其他已知威胁数据库中的数据相关联。

这种方法有助于收集足够的情报，将攻击归因于有经济动机的团体，甚至是国家支持的行为者，如俄罗斯午夜暴雪（Nobelium）威胁组织。

尽管利用“欺骗”的方式来保护资产的这种原理并不新鲜，许多公司也依靠蜜罐来检测入侵，甚至追踪黑客，但微软找到了一种利用其资源来大规模追捕威胁行为者的方法。

> 参考来源：[Microsoft creates fake Azure tenants to pull phishers into honeypots (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/microsoft-creates-fake-azure-tenants-to-pull-phishers-into-honeypots/)

# 网络钓鱼 # 微软安全

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

网络钓鱼成功的假象

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