---
title: 只需10分钟即可被绕过，Chrome浏览器最新cookie安全功能纸糊的一样？
url: https://www.freebuf.com/news/411689.html
source: FreeBuf网络安全行业门户
date: 2024-09-26
fetch_date: 2025-10-06T18:29:25.821232
---

# 只需10分钟即可被绕过，Chrome浏览器最新cookie安全功能纸糊的一样？

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

只需10分钟即可被绕过，Chrome浏览器最新cookie安全功能纸糊的一样？

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

只需10分钟即可被绕过，Chrome浏览器最新cookie安全功能纸糊的一样？

2024-09-25 10:30:43

所属地 上海

![1727230806_66f37356073437d5d09c0.png!small](https://image.3001.net/images/20240925/1727230806_66f37356073437d5d09c0.png!small)

最近，Infostealer恶意软件开发者发布更新，声称可以绕过谷歌Chrome浏览器最近推出的保护cookie等敏感数据的App-Bound Encryption功能。

App-Bound Encryption 是在 Chrome 浏览器 127 中引入的，旨在使用一个以系统权限运行的 Windows 服务对 cookie 和存储的密码进行加密。

这种模式不允许以登录用户权限运行的信息窃取恶意软件窃取存储在 Chrome 浏览器中的机密。

Chrome 浏览器安全团队的Will Harris表示，要想绕过这种保护，恶意软件需要系统权限或向 Chrome 浏览器注入代码，这两种操作都可能触发安全工具的警告。

然而，安全研究人员 g0njxa 和 RussianPanda9xx 发现多个信息窃取程序开发者“吹嘘” 他们的工具（MeduzaStealer、Whitesnake、Lumma Stealer、Lumar (PovertyStealer)、Vidar Stealer 和 StealC）已经实现了有效的绕过。

![1727231007_66f3741f8230abd6eee20.png!small](https://image.3001.net/images/20240925/1727231007_66f3741f8230abd6eee20.png!small)

Whitesnake盗号软件从Chrome128中窃取Cookie，来源：@g0njxa

g0njxa 向 BleepingComputer 证实，Lumma Stealer 的最新变种可以绕过 Chrome 129（目前最新版本的浏览器）中的加密功能。

![1727231158_66f374b630955d196d73e.png!small](https://image.3001.net/images/20240925/1727231158_66f374b630955d196d73e.png!small)

使用最新版Lumma 从Chrome浏览器129中提取 cookie，来源：@g0njxa

研究人员在沙盒环境中的 Windows 10 Pro 系统上测试了该恶意软件。
从时间上看，Meduza 和 WhiteSnake 是在两周前实施绕过机制的，Lumma 是在上周，而 Vidar 和 StealC 则是在本周。

Lumar 最初是通过实施一种临时解决方案来应对 App-Bound Encryption 的，该方案要求以管理员权限启动恶意软件，但随后又推出了一种绕过机制，该机制可登录用户的权限工作。

Lumma Stealer 的开发人员向其客户保证，他们不需要以管理员权限执行恶意软件就能窃取 cookie。

Rhadamanthys恶意软件的作者表示，他们用了10分钟时间逆转了加密。

目前该公司暂未对此事件进行进一步表态。

> 参考来源：[Infostealer malware bypasses Chrome’s new cookie-theft defenses (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/infostealer-malware-bypasses-chromes-new-cookie-theft-defenses/)

# 恶意软件 # chrome # 浏览器安全

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