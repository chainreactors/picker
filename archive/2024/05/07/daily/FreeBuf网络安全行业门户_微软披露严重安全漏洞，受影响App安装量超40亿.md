---
title: 微软披露严重安全漏洞，受影响App安装量超40亿
url: https://www.freebuf.com/news/400004.html
source: FreeBuf网络安全行业门户
date: 2024-05-07
fetch_date: 2025-10-06T17:17:47.061899
---

# 微软披露严重安全漏洞，受影响App安装量超40亿

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

微软披露严重安全漏洞，受影响App安装量超40亿

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

微软披露严重安全漏洞，受影响App安装量超40亿

2024-05-06 13:32:33

所属地 上海

近日，研究人员披露了一个名为“Dirty Stream”的严重安全漏洞，该漏洞可能影响几款下载总量数十亿的 Android 应用程序。![1714974720_66387000c55893833aa6a.png!small](https://image.3001.net/images/20240506/1714974720_66387000c55893833aa6a.png!small)

微软威胁情报团队成员 Dimitrios Valsamaras 在一份报告中声明，威胁攻击者可以利用该安全漏洞，执行任意代码以及盗取令牌。一旦成功利用漏洞，威胁攻击者就可以完全控制应用程序的“行为”，并利用窃取的令牌在未经授权的情况下访问受害者的在线账户和其他数据。

这一安全漏洞可能会给大量设备带来威胁风险， Google Play 商店中目前已经发现了几个易受攻击的应用程序，这些应用程序的总安装量超过了 40 亿，其中受该安全漏洞影响程度最大的两个应用程序如下：

> 小米文件管理器 (com.mi. Android.globalFileexplorer) -，安装量超过 10 亿次
> WPS Office (cn.wps.moffice\_eng) -，安装量超过 5 亿次

安卓系统通过为每个应用程序分配专用的数据和内存空间来实现隔离，并以安全的方式促进应用程序之间的数据和文件共享。但实施过程中的疏忽可能会导致绕过应用程序主目录内的读/写限制。

Valsamaras 表示，这种基于内容提供商的模式提供了一种定义明确的文件共享机制，使服务应用程序能够以安全的方式与其他应用程序共享文件，并进行细粒度控制。

然而，在执行的过程中，经常遇到消费应用程序并不验证其接收到的文件内容，而且最令人担忧的是，它使用服务应用程序提供的文件名将接收到的文件缓存在消费应用程序的内部数据目录中。当服务应用程序为了实现应用程序之间的文件共享而声明恶意版本的 FileProvider 类时，这一“陷阱”可能会造成严重后果，最终导致消费应用程序覆盖其私有数据空间中的关键文件。

换句话说，该机制利用了消费应用程序盲目信任输入这一事实，通过自定义、明确的意图，在用户不知情或未经用户同意的情况下发送带有特定文件名的任意有效载荷，从而导致代码执行。

这时候，威胁攻击者就可以覆盖目标应用程序的共享首选项文件，使其与受其控制的服务器通信，从而外泄敏感信息。另一种情况是应用程序从自己的数据目录（而不是"/data/app-lib"）加载本地库，在这种情况下，恶意应用程序可以利用上述漏洞，在加载本地库时用恶意代码覆盖该库并执行。

值得一提的是，在接到安全漏洞披露通知后，小米和 WPS Office 均已于 2024 年 2 月对该安全漏洞问题进行了整改。与此同时，谷歌也就此发布了详细的指导意见，敦促开发者正确处理服务器应用程序提供的文件名。

谷歌方面强调，当客户端应用程序将接收到的文件写入存储时，应该忽略服务器应用程序提供的文件名，而使用自己内部生成的唯一标识符作为文件名，如果生成唯一的文件名不能轻易实现，客户端应用程序就应该对提供的文件名进行核验、清查。

最后，微软方面指出，该安全漏洞问题非常普遍，相关开发者应当采取措施，仔细检查自身应用程序是否存在类似问题。

**参考文章：**

> https://thehackernews.com/2024/05/popular-android-apps-like-xiaomi-wps.html

# 安全漏洞

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