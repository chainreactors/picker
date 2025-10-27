---
title: 新的“DoubleClickjacking”漏洞可绕过网站的劫持保护
url: https://www.freebuf.com/news/418913.html
source: FreeBuf网络安全行业门户
date: 2025-01-03
fetch_date: 2025-10-06T20:09:27.511666
---

# 新的“DoubleClickjacking”漏洞可绕过网站的劫持保护

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

新的“DoubleClickjacking”漏洞可绕过网站的劫持保护

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新的“DoubleClickjacking”漏洞可绕过网站的劫持保护

2025-01-02 11:46:14

所属地 上海

安全专家揭示了一种新型的“普遍存在的基于时间的漏洞”，该漏洞通过利用双击操作来推动点击劫持攻击及账户接管，几乎波及所有大型网站。这一技术已被安全研究员Paulos Yibelo命名为“DoubleClickjacking”。

![](https://image.3001.net/images/20250102/1735789931_67760d6b5512ab30e8668.jpg!small)

Yibelo指出：“它并非依赖单一点击，而是利用双击的序列。这看似微小的变化，却为新的UI操控攻击敞开了大门，能够绕过所有现有的点击劫持防护措施，包括X-Frame-Options头部或SameSite: Lax/Strict cookie。”

点击劫持，亦称作UI重定向，是一种攻击手段，诱使用户点击看似无害的网页元素（如按钮），进而导致恶意软件的安装或敏感信息的泄露。DoubleClickjacking作为这一领域的变种，它利用点击开始与第二次点击结束之间的时间差来规避安全控制，以最小的用户交互实现账户接管。

具体步骤如下：

> 1. 用户访问一个由攻击者控制的网站，该网站要么在无需任何用户操作的情况下自动打开一个新的浏览器窗口（或标签页），要么在点击按钮时打开。
> 2. 新窗口可能模仿一些无害的内容，例如CAPTCHA验证，提示用户双击以完成操作。
> 3. 在双击过程中，原始网站利用JavaScript Window Location对象悄悄重定向至恶意页面（如，批准恶意的OAuth应用程序）。
> 4. 同时，顶层窗口被关闭，使用户在毫不知情的情况下通过批准权限确认对话框授予访问权限。

Yibelo表示：“大多数Web应用程序和框架都认为只有单次强制点击存在风险。DoubleClickjacking引入了一层许多防御措施从未考虑过的内容。像X-Frame-Options、SameSite cookie或CSP这样的方法无法抵御这种攻击。”

网站所有者可通过客户端手段消除这类漏洞，默认禁用关键按钮，仅在检测到鼠标手势或按键时激活。研究发现，诸如Dropbox等服务已经实施了此类预防措施。作为长远解决方案，建议浏览器供应商采纳类似X-Frame-Options的新标准来防御双击利用。

Yibelo强调：“DoubleClickjacking是一种众所周知的攻击类别的变种。通过利用点击之间的事件时间差，攻击者能够在瞬间无缝地将良性UI元素替换为敏感元素。”

此次披露距离研究人员展示另一种点击劫持变体（即跨窗口伪造，亦称作手势劫持）已近一年，该变体依赖于说服受害者在攻击者控制的网站上按下或按住Enter键或空格键以启动恶意操作。

在Coinbase和Yahoo!等网站上，如果已登录任一网站的受害者访问攻击者网站并按住Enter/空格键，则可能被利用来实现账户接管。

“这是因为这两个网站都允许潜在攻击者创建具有广泛权限范围的OAuth应用程序以访问其API，并且它们都为用于授权应用程序进入受害者账户的‘允许/授权’按钮设置了静态和/或可预测的‘ID’值。”

参考来源：<https://thehackernews.com/2025/01/new-doubleclickjacking-exploit-bypasses.html>

# 漏洞

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