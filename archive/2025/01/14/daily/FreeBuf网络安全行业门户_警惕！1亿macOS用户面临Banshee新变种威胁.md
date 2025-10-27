---
title: 警惕！1亿macOS用户面临Banshee新变种威胁
url: https://www.freebuf.com/news/419718.html
source: FreeBuf网络安全行业门户
date: 2025-01-14
fetch_date: 2025-10-06T20:10:36.145484
---

# 警惕！1亿macOS用户面临Banshee新变种威胁

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

警惕！1亿macOS用户面临Banshee新变种威胁

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

警惕！1亿macOS用户面临Banshee新变种威胁

2025-01-13 15:28:47

所属地 上海

![](https://image.3001.net/images/20250113/1736753383_6784c0e73455797d43351.jpg!small)

研究人员分析了 Banshee macOS Stealer样本的新版本，该样本最初避开了大多数反病毒引擎的检测。

分析显示，该恶意软件采用了一种独特的字符串加密技术，与Apple XProtect防病毒引擎用于加密二进制文件中YARA规则的加密方法相同。通过利用这种共享加密算法，Banshee可以混淆关键字符串，从而阻碍安全解决方案的即时检测。

Check Point 研究人员补充道：“随着macOS的持续普及，全球用户超过1亿，它正逐渐成为网络犯罪分子越来越青睐的目标。”

![](https://image.3001.net/images/20250113/1736753405_6784c0fd457532916107a.png!small)已解压Banshee MacOS Stealer检测。

Banshee是一种窃取恶意软件，通过使用反分析技术（例如分叉和进程创建）来避免检测，目标是用户凭证、浏览器数据和加密钱包。

从包括Chrome 、Brave 、Edge 、Vivaldi 、Yandex 和Opera在内的各种浏览器和浏览器扩展中窃取信息，同时也针对特定的加密钱包扩展程序。

被窃取的数据经过压缩后，使用活动ID进行XOR加密，然后进行base64编码，最后被传输到命令和控制服务器。

C&C服务器经历了多次迭代，从基于Django的服务器（具有单独的管理面板），到用于机器人通信的单一FastAPI端点。目前，托管管理面板的服务器隐藏在Relay服务器后面，以增加隐蔽性。

![](https://image.3001.net/images/20250113/1736753466_6784c13a1119f5734f006.png!small)C＆C解密。

Check Point Research发现了针对macOS用户的Banshee Stealer新版本，该版本通过多个假装提供破解软件的网络钓鱼存储库进行分发。

这些储存库在恶意软件推送前几周创建，恶意软件窃取数据并将其发送到C&C服务器。最新的活动使用钓鱼网站针对macOS用户，并伪装成Telegram下载传播恶意软件。

![](https://image.3001.net/images/20250113/1736753493_6784c15565a966f531c2c.png!small)存储库发布。

一名名为@kolosain的威胁行为者最初在Telegram上以2999美元的价格出售Banshee macOS 窃取程序。随后，他们在XSS和Exploit论坛上以每月1500美元的价格提供该服务。甚至还招募了有限数量的熟练会员，组成了私人团体，并提供利润分享模式。

在原始源代码泄露后，@kolosain试图在关闭服务前出售整个项目。泄密事件导致防病毒软件的检测率上升，但也增加了其他行为者开发分支和新变种的可能性。

![](https://image.3001.net/images/20250113/1736753523_6784c173a0905ddaa4996.png!small)Banshee特卖帖

Banshee macOS Stealer最新代码更新涉及字符串加密，成功避开防病毒软件的检测长达两个多月的时间。

以前专注于Windows的恶意行为者现在正积极针对macOS，利用GitHub等平台分发DMG文件和不受保护的档案。

这强调了需要能够适应不断演变的威胁的强大安全解决方案，包括主动威胁情报以及操作系统和应用程序的及时更新。

用户必须保持警惕，谨慎对待意外通信，并优先进行网络安全意识培训，以减轻与这些威胁相关的风险。

**参考链接：**

> <https://cybersecuritynews.com/banshee-malware-targets-macos/>

# 资讯 # 系统安全 # 木马

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