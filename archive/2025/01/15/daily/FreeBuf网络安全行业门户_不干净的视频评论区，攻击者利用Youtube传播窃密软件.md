---
title: 不干净的视频评论区，攻击者利用Youtube传播窃密软件
url: https://www.freebuf.com/news/419785.html
source: FreeBuf网络安全行业门户
date: 2025-01-15
fetch_date: 2025-10-06T20:10:34.593056
---

# 不干净的视频评论区，攻击者利用Youtube传播窃密软件

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

不干净的视频评论区，攻击者利用Youtube传播窃密软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

不干净的视频评论区，攻击者利用Youtube传播窃密软件

2025-01-14 11:13:27

所属地 上海

趋势科技的一项调查研究发现，为了尽可能传播恶意软件，攻击者正利用Youtube评论区、谷歌搜索等渠道提供其恶意下载链接。

![](https://image.3001.net/images/20250114/1736824742_6785d7a6530dd43748a1f.png!small)

研究人员称，为了增加其恶意内容的可信度，攻击者以一些热门Youtube频道为目标，其中一些频道拥有数十万订阅者。这些受感染的频道声称提供破解版的高级软件或游戏，并在视频描述或评论中提供带有安装指南的下载链接。

在谷歌上，攻击者正积极创建盗版和破解软件的搜索结果，并带有指向看似合法下载器的链接，其中暗藏信息窃取软件。

经检测，这些破解软件包含了以Lumma Stealer为主的信息窃取木马，一旦安装在受害者的系统上，就会搜集浏览器中保存的账户密码、密货币钱包信息、信用卡详细信息、受害者桌面截图等敏感数据。

攻击者使用 Mediafire 和 Mega.nz 等合法文件托管服务来托管恶意负载，通过利用这些信誉良好的平台，安全软件检测和阻止这些威胁变得更加困难。此外，许多恶意下载都受密码保护和编码，使得安全沙箱中的分析更加复杂，并允许恶意软件逃避早期检测。

除了 Lumma，研究人员观察到的其他信息窃取恶意软件包括 PrivateLoader、MarsStealer、Amadey、Penguish 和 Vidar。

## 与利用GitHub的恶意活动具有相似性

这一攻击活动手法与之前利用GitHub 的活动相似，攻击者利用开发人员对平台的信任将 Remcos RAT恶意软件隐藏在 GitHub 存储库评论中。

研究人员解释称，尽管攻击媒介不同，但评论在传播恶意软件方面发挥着重要作用。在他们观察到的一次攻击中，一个视频帖子声称提供破解的Adobe Lightroom ，并包含一条带有软件下载器链接的评论。访问该链接后，YouTube 上会打开一个单独的帖子，显示虚假安装程序的下载链接，该链接导致从 Mediafire 文件托管站点下载恶意文件，其中包括信息窃取恶意软件。

研究人员指出，眼下的趋势，攻击者会继续使用社会工程策略来瞄准受害者，并应用各种方法来避免安全防御，包括：使用大型安装程序文件、受密码保护的 zip 文件、连接到合法网站，以及创建看起来是合法软件的的恶意脚本。

**参考来源：**

> [Cyberattackers Hide Infostealers in YouTube Comments, Google Search Results](https://www.darkreading.com/threat-intelligence/cyberattackers-infostealers-youtube-comments-google-search)

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

与利用GitHub的恶意活动具有相似性

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