---
title: 注意！一个新的恶意扩展可以远程控制你的谷歌浏览器
url: https://www.freebuf.com/news/349237.html
source: FreeBuf网络安全行业门户
date: 2022-11-10
fetch_date: 2025-10-03T22:15:09.208076
---

# 注意！一个新的恶意扩展可以远程控制你的谷歌浏览器

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

注意！一个新的恶意扩展可以远程控制你的谷歌浏览器

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

注意！一个新的恶意扩展可以远程控制你的谷歌浏览器

2022-11-09 11:30:50

所属地 上海

![](https://image.3001.net/images/20221109/1667964117_636b1cd5ccafb5b8a7e89.jpg!small)最近Zimperium 的研究人员发现了一个新的名为“Cloud9”的 Chrome 浏览器僵尸网络，它使用恶意扩展来窃取在线帐户、记录击键、注入广告和恶意 JS 代码，并让受害者的浏览器参与 DDoS 攻击。

Cloud9 浏览器实际上是 Chromium Web 浏览器（包括 Google Chrome 和 Microsoft Edge）的远程访问木马 (RAT)，其作用是允许攻击者远程执行命令。

恶意 Chrome 扩展程序在官方 Chrome 网上商店中不可用，而是通过其他渠道传播，例如推送虚假 Adob​​e Flash Player 更新的网站。![](https://image.3001.net/images/20221109/1667964137_636b1ce9acf13fdf55256.jpg!small)

这种方法似乎运作良好，因为根据Zimperium 的研究人员报告说，他们已经在全球系统上看到了 Cloud9 感染。

## 感染浏览器

Cloud9 是一个恶意浏览器扩展，它对 Chromium 浏览器进行感染，以执行大量的恶意功能。

该扩展工具由三个 JavaScript 文件组成，用于收集系统信息、使用主机资源挖掘加密货币、执行 DDoS 攻击以及注入运行浏览器漏洞的脚本。

Zimperium 注意到它还加载了针对 Firefox 中的 CVE-2019-11708 和 CVE-2019-9810 漏洞、Internet Explorer 的 CVE-2014-6332 和 CVE-2016-0189 以及 Edge 的 CVE-2016-7200 漏洞的利用。

这些漏洞用于在主机上自动安装和执行 Windows 恶意软件，使攻击者能够进行更深入的系统入侵。

然而，即使没有 Windows 恶意软件组件，Cloud9 扩展也可以从受感染的浏览器中窃取 cookie，攻击者可以使用这些 cookie 劫持有效的用户会话并接管帐户。![](https://image.3001.net/images/20221109/1667964160_636b1d00b8c50d218501f.jpg!small)

此外，该恶意软件具有一个键盘记录器，可以窥探按键以窃取密码和其他敏感信息。

扩展中还存在一个“剪辑器”模块，不断监视系统剪贴板中是否有复制的密码或信用卡。![](https://image.3001.net/images/20221109/1667964175_636b1d0fe37a1730ab475.jpg!small)

Cloud9 还可以通过静默加载网页来注入广告，从而产生广告展示，为其运营商带来收入。

最后，恶意软件可以利用主机通过对目标域的 HTTP POST 请求执行第 7 层 DDoS 攻击。

“第 7 层攻击通常很难检测，因为 TCP 连接看起来与正常请求非常相似” ，Zimperium 评论道。

开发人员很可能会使用这个僵尸网络来提供执行 DDOS 的服务。

## 运算符和目标

Cloud9 背后的黑客有可能与 Keksec 恶意软件组织有联系，因为在最近的活动中使用的 C2 域在 Keksec 过去的攻击中被发现。

Keksec 负责开发和运行多个僵尸网络项目，包括EnemyBot、Tsunamy、Gafgyt、DarkHTTP、DarkIRC 和 Necro。

Cloud9 的受害者遍布全球，攻击者在论坛上发布的屏幕截图表明他们针对各种浏览器。![](https://image.3001.net/images/20221109/1667964195_636b1d23310b4622b2b55.jpg!small)

此外，在网络犯罪论坛上公开宣传 Cloud9 导致 Zimperium 相信 Keksec 可能会将其出售/出租给其他运营商。

### 参考来源：

> https://www.bleepingcomputer.com/news/security/malicious-extension-lets-attackers-control-google-chrome-remotely/

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

感染浏览器

运算符和目标

* 参考来源：

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