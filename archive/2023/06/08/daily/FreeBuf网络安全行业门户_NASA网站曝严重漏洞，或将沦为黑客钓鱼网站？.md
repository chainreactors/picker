---
title: NASA网站曝严重漏洞，或将沦为黑客钓鱼网站？
url: https://www.freebuf.com/news/368750.html
source: FreeBuf网络安全行业门户
date: 2023-06-08
fetch_date: 2025-10-04T11:47:54.719411
---

# NASA网站曝严重漏洞，或将沦为黑客钓鱼网站？

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

NASA网站曝严重漏洞，或将沦为黑客钓鱼网站？

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

NASA网站曝严重漏洞，或将沦为黑客钓鱼网站？

2023-06-07 14:21:29

所属地 上海

![](https://image.3001.net/images/20230607/1686108856_647ffab814f0b446b72e9.png!small)

美国国家航空航天局（NASA）天体生物学专用网站存在一个严重的安全漏洞，可能通过伪装带有NASA名称的危险URL来诱骗用户访问恶意网站。

太空旅行无疑是危险的。然而，在访问NASA网站的时候也有可能如此。Cybernews研究团队发现了一个NASA天体生物学网站的开放式重定向漏洞。

经过研究人员的调查，早在几个月前（2023年1月14日）已经有研究人员通过漏洞赏金计划发现并报告该漏洞，但该机构没有处理和修复。

攻击者可以利用这个漏洞将任何人重定向到恶意网站，从而获取他们的登录凭证、信用卡号码或其他敏感数据。

自4月初以来，Cybernews研究团队已多次联系美国国家航空航天局，截止到今天尚未收到任何答复。

## 什么是开放式重定向漏洞？

开放式重定向漏洞简单来说就像是一个假冒的出租车司机。例如你叫了一辆出租车并告诉司机你想去哪里，但是他并没有把你送到目的地，而是把你带到另一个地方。

同样，试图访问 astrobiology.nasa.gov 的用户可能就被重定向进入了一个恶意的网站。通常情况下，网络应用程序会验证用户提供的输入，如URL或参数，以防止恶意重定向的发生。

网络新闻研究人员解释说：攻击者可以利用该漏洞，通过将恶意网址伪装成合法网址，诱使用户访问恶意网站或钓鱼网页。

## 为什么开放式重定向漏洞是危险的？

攻击者可以用额外的参数修改NASA的网站，将用户引导到他们选择的地方。重新跳转的网站甚至可能类似于NASA的页面，只是在其中加入要求输入信用卡数据的提示。

此外，攻击者可以利用开放的重定向漏洞，引导用户进入网站，在登陆后立即将恶意软件下载到他们的电脑或移动设备上。

另一种利用该漏洞的方式是通过将用户重定向到展示低质量内容或垃圾邮件的网站来控制搜索引擎的排名。

虽然我们没有确认是否有人真正利用了NASA网站的这个漏洞，但是事实上这个漏洞已经暴露了几个月。

## 如何减轻开放式重定向漏洞的影响？

利用开放式重定向漏洞可以使恶意行为者进行网络钓鱼攻击，窃取凭证并传播恶意软件。

为了避免此类事故，Cybernews研究团队强烈建议网站验证所有用户输入，包括URL。

研究人员解释说：这可能包括使用正则表达式来验证URL的正确格式，检查URL是否来自受信任的域，并验证URL不包含任何额外或恶意的字符。

为了防止恶意字符被注入URLs，网站管理员还可以使用URL编码。同时，网站所有者可以创建一个可信URL的白名单，只允许重定向到这些URL。防止攻击者将用户重定向到恶意的或未经授权的网站。

> 参考链接：https://cybernews.com/security/nasa-astrobiology-website-flaw/

# 资讯 # 漏洞

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

什么是开放式重定向漏洞？

为什么开放式重定向漏洞是危险的？

如何减轻开放式重定向漏洞的影响？

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