---
title: Google Ads用户成恶意广告诈骗新目标，凭据及双因素认证码被盗
url: https://www.freebuf.com/articles/419985.html
source: FreeBuf网络安全行业门户
date: 2025-01-17
fetch_date: 2025-10-06T20:10:21.881659
---

# Google Ads用户成恶意广告诈骗新目标，凭据及双因素认证码被盗

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

Google Ads用户成恶意广告诈骗新目标，凭据及双因素认证码被盗

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Google Ads用户成恶意广告诈骗新目标，凭据及双因素认证码被盗

2025-01-16 10:28:50

所属地 上海

![](https://image.3001.net/images/20250116/1737005132_6788984cf252969eefb4e.png!small)

网络安全研究人员最近注意到一项新的恶意广告活动，该活动针对通过Google Ads进行推广的个人和企业，试图通过在Google上投放虚假广告来窃取他们的凭据。

Malwarebytes威胁情报高级总监Jérôme Segura在报告中表示：“该计划通过冒充Google Ads，并将受害者重定向到虚假登录页面，尽可能多地窃取广告商账户。”

据推测，该活动的最终目标是利用被盗凭据进一步传播活动，同时将凭据出售给地下论坛的其他犯罪分子。根据Reddit、Bluesky以及Google自身支持论坛上的帖子，该威胁自2024年11月中旬以来一直活跃。

该活动与利用窃取器恶意软件窃取Facebook广告和商业账户数据，劫持账户并进一步传播恶意广告的活动非常相似。

新发现的攻击活动专门针对在Google自己的搜索引擎上搜索Google Ads的用户，提供虚假广告，点击后将用户重定向到托管在Google Sites上的欺诈网站。这些网站随后作为着陆页，引导访客前往外部钓鱼网站，通过WebSocket捕获他们的凭据和双因素认证（2FA）码，并将其传输到攻击者控制的远程服务器。

Segura称：“这些虚假广告来自不同地点的个人和企业（包括一个地区机场），其中一些账户已经运行了数百个其他合法广告。”

![](https://image.3001.net/images/20250116/1737005241_678898b9bd975d927d4ae.png!small)

该活动的一个巧妙之处在于，它利用了这样一个事实：只要域名匹配，Google Ads并不要求最终URL（用户点击广告时到达的网页）与显示网址相同。这使得威胁行为者可以在sites.google[.]com上托管他们的中间着陆页，同时将显示URL保持为ads.google[.]com。此外，该活动还采用指纹识别、反机器人流量检测、类似验证码的诱饵、伪装和混淆等技术来隐藏钓鱼基础设施。

Malwarebytes表示，收集到的凭据随后被滥用以登录受害者的Google Ads账户，添加新管理员，并利用他们的消费预算投放虚假谷歌广告。也就是说，威胁行为者接管Google Ads账户，推送自己的广告，以便为不断增长的被黑帐户池添加新的受害者，并利用这些账户进一步传播诈骗。

Segura称：“这些活动背后似乎有多个个人或团体。值得注意的是，他们中的大多数人是葡萄牙语使用者，很可能在巴西运营。钓鱼基础设施依赖以.pt顶级域名（TLD）的中间域名，这表明与葡萄牙有关。这种恶意广告活动并不违反谷歌的广告规则。威胁行为者被允许在广告中显示欺诈性URL，使其与合法网站无法区分。谷歌尚未表明其会采取明确步骤冻结此类账户，直到其安全性得到恢复。”

与此同时，Trend Micro透露，攻击者正在使用 YouTube 和 SoundCloud 等平台分发流行软件盗版版本的虚假安装程序链接，最终导致部署各种恶意软件家族，例如Amadey、Lumma Stealer、Mars Stealer、Penguish、PrivateLoader和Vidar Stealer。

该公司表示：“威胁行为者经常使用Mediafire和Mega.nz等知名文件托管服务来隐藏恶意软件的来源，使检测和移除更加困难。许多恶意下载都受到密码保护和编码，这使得在沙箱等安全环境中的分析变得复杂，从而使恶意软件能够逃避早期检测。”

**参考链接：**

> <https://thehackernews.com/2025/01/google-ads-users-targeted-in.html>

# 资讯 # web安全

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