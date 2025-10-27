---
title: 黑客入侵超 6000 个WordPress网站，以推送信息窃取程序插件
url: https://www.freebuf.com/news/413365.html
source: FreeBuf网络安全行业门户
date: 2024-10-23
fetch_date: 2025-10-06T18:51:01.842149
---

# 黑客入侵超 6000 个WordPress网站，以推送信息窃取程序插件

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

黑客入侵超 6000 个WordPress网站，以推送信息窃取程序插件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客入侵超 6000 个WordPress网站，以推送信息窃取程序插件

2024-10-22 10:14:57

所属地 上海

![红色背景上的 WordPress 标志](https://image.3001.net/images/20241022/1729567534_67171b2e8cc279ec22dee.jpg!small)

WordPress 网站近日被黑客非法入侵并安装恶意插件，这些插件会推送虚假的软件更新和错误信息，从而推送窃取信息的恶意软件。
在过去几年时间里，信息窃取恶意软件已成为全球安全防御者的“心腹大患” ，因为被盗凭据通常会被用来入侵网络和窃取数据。
自 2023 年以来，一个名为 ClearFake 的恶意活动一直被用于分发虚假的 Web 浏览器更新横幅。2024 年，一种名为 ClickFix 的新活动问世，它与 ClearFake 有许多相似之处，但不同的是它会假装是软件错误信息，并附有修复程序。然而这些 “修复 ”都是 PowerShell 脚本，执行后会下载并安装信息窃取恶意软件。

![An example ClickFix overlay pretending to be a Chrome error](https://image.3001.net/images/20241022/1729567537_67171b3165a6f0ba05eb0.png!small)

假冒 Chrome 浏览器错误的 ClickFix 叠加示例，来源：BleepingComputer

今年，ClickFix 活动变得越来越常见，一旦威胁行为者成功入侵网站，就会显示 Google Chrome 浏览器、Google Meet conferences、Facebook 甚至验证码页面的虚假错误的推送信息。

## 恶意 WordPress 插件

上周，GoDaddy 报告称，ClearFake/ClickFix 威胁行为者已经入侵了 6000 多个 WordPress 网站，安装恶意插件来显示与这些活动相关的虚假警报。

GoDaddy 安全团队正在追踪一种新的 ClickFix（也称 ClearFake）虚假浏览器更新恶意软件变种，该恶意软件通过虚假 WordPress 插件传播，GoDaddy 安全研究员 Denis Sinegubko 解释说。

这些看似合法的插件被设计成对网站管理员无害，但却包含嵌入式恶意脚本，会向最终用户发送虚假的浏览器更新提示。

这些恶意插件使用了与合法插件类似的名称，如 Wordfense Security 和 LiteSpeed Cache，而其他恶意插件则使用了通用的编造名称。

2024 年 6 月至 9 月期间，在该活动中出现的恶意插件列表如下：

![1729563200_67170a40d373e304336ff.png!small](https://image.3001.net/images/20241022/1729563200_67170a40d373e304336ff.png!small)

网站安全公司 Sucuri 指出，名为 “Universal Popup Plugin ”的虚假插件也是该活动的一部分。安装后，该恶意插件会根据变种关联各种 WordPress 操作，向网站的 HTML 中注入恶意 JavaScript 脚本。

![Injected JavaScript script](https://image.3001.net/images/20241022/1729567540_67171b342c07e957f8e47.jpg!small)

注入 JavaScript 脚本，来源：GoDaddy

加载该脚本后，该脚本将尝试加载存储在 Binance 智能链 (BSC) 智能合约中的另一个恶意 JavaScript 文件，然后加载 ClearFake 或 ClickFix 脚本以显示虚假横幅。

![Fake Google update banner](https://image.3001.net/images/20241022/1729567542_67171b36f3fd47d2d7f88.png!small)

伪造的谷歌更新横幅，来源：Randy McEoin

从 Sinegubko 分析的网络服务器访问日志来看，威胁者似乎是利用窃取的管理员凭据登录 WordPress 网站，并以自动化方式安装插件。

从下图中可以看到，威胁者通过单个 POST HTTP 请求登录，而不是首先访问网站的登录页面。这表明这是在已经获得凭据后自动完成的。

威胁行为者登录后，就会上传并安装恶意插件。

![Access logs showing how WordPress site is compromised](https://image.3001.net/images/20241022/1729567546_67171b3a8a41b8b64f6ab.jpg!small)

显示 WordPress 网站如何被入侵的访问日志，来源：GoDaddy

虽然目前还不清楚威胁者是如何获得凭证的，但研究人员指出，这可能是通过以前的暴力攻击、网络钓鱼和信息窃取恶意软件获得的。

如果您正在使用 WordPress，并且收到了向访问者显示虚假警报的报告，您应立即检查已安装的插件列表，并删除任何非您自行安装的插件。

如果发现未知插件，也要立即将所有管理员用户的密码重置为仅在网站上使用的唯一密码。

> 参考来源：<https://www.bleepingcomputer.com/news/security/over-6-000-wordpress-hacked-to-install-plugins-pushing-infostealers/>

# WordPress漏洞 # Wordpress插件漏洞 # WordPress安全

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

恶意 WordPress 插件

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