---
title: 【安全圈】Redis服务器曝2个严重的RCE漏洞，数百万系统面临风险
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067236&idx=4&sn=b0147296a18e71da729ab28bc5c2ff3d&chksm=f36e79e4c419f0f2a35ef7ccb2f9e02e1ff05a8932fae3aec068182b76b3971be1050410a85a&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-10
fetch_date: 2025-10-06T20:09:27.390417
---

# 【安全圈】Redis服务器曝2个严重的RCE漏洞，数百万系统面临风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia8PmccbLyj90MFENK4UQcJwDUEKbyFib0Y5XmWrPwic1zSuCo5hcEVUL4ZaVibGkFIf2p7l6LJEzJlA/0?wx_fmt=jpeg)

# 【安全圈】Redis服务器曝2个严重的RCE漏洞，数百万系统面临风险

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

在广泛使用的内存数据库Redis里，发现了两个严重漏洞，这可能使数百万系统面临拒绝服务（DoS）攻击和远程代码执行（RCE）的风险。这些漏洞被标记为CVE - 2024 - 51741和CVE - 2024 - 46981，这凸显了Redis用户面临着重大的安全风险，也强调了及时更新和采取缓解措施的重要性。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia8PmccbLyj90MFENK4UQcJ8LkUShIHHAkicT13OYC5ic1of3z3LdicRXUiaWT1mCic4GE8hk9IruUWe4w/640?wx_fmt=jpeg&from=appmsg)

### 一、CVE - 2024 - 51741：畸形ACL选择器引发的拒绝服务

CVE - 2024 - 51741这个漏洞影响Redis 7.0.0及以上版本。拥有足够权限的认证用户能够创建一个畸形的访问控制列表（ACL）选择器。

当访问这个畸形选择器时，服务器就会崩溃，从而进入拒绝服务状态。该问题已在Redis 7.2.7和7.4.2版本中得到修复。

Redis用户应马上升级到这些修复后的版本，从而保护自己的系统免受可能的利用。此漏洞是由Axel Mierczuk报告的，他为发现这个漏洞做出了贡献。

### 二、CVE - 2024 - 46981：Lua脚本执行远程代码

CVE - 2024 - 46981这个漏洞带来的威胁更大，因为它可能导致远程代码执行。这个问题是由于Redis中Lua脚本功能被滥用而产生的。认证过的攻击者能够编写恶意的Lua脚本来操纵垃圾收集器，进而可能在服务器上执行任意代码。

这个漏洞影响所有开启了Lua脚本功能的Redis版本。针对Redis 6.2.x、7.2.x和7.4.x版本已经发布了修补程序。对于那些不能马上更新的用户，建议通过修改ACL规则来限制“EVAL”和“EVALSHA”命令，从而禁用Lua脚本作为额外的防范措施。

### 三、建议措施

1. 升级Redis

用户应该把安装更新到已修复漏洞的版本，即针对CVE - 2024 - 51741的7.2.7或7.4.2版本，以及针对CVE - 2024 - 46981的最新版本。

2. 限制Lua脚本

作为针对CVE - 2024 - 46981的临时解决办法，通过修改ACL规则阻止“EVAL”和“EVALSHA”命令来禁用Lua脚本。

3. 监控访问控制

要确保只有受信任的用户才能在Redis服务器上执行特权命令。这些漏洞表明在管理数据库系统时实施强大安全策略是非常关键的。强烈建议Redis用户立即行动起来，减轻风险，保护自己的环境免受潜在的利用。

参考来源：https://cybersecuritynews.com/redis-server-vulnerabilities/

***END***

阅读推荐

[【安全圈】首席执行官被捕后，Telegram 用户数据共享激增](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067220&idx=1&sn=32e5ae1627ca403870bb45f7884bb2c0&scene=21#wechat_redirect)

[【安全圈】CISA 警告称，Oracle 和 Mitel 在攻击中被利用了关键漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067220&idx=2&sn=a053c599ab3224a55ad5beec4dc12341&scene=21#wechat_redirect)

[【安全圈】PhishWP 插件劫持 WordPress 电子商务结账功能](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067220&idx=3&sn=b3641123d0bc84854504b30b4a1e8f93&scene=21#wechat_redirect)

[【安全圈】BIOS 缺陷使 iSeq DNA 测序仪面临 bootkit 攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067220&idx=4&sn=02eb8fe14f312d38658f3ad26fcd4cb9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过