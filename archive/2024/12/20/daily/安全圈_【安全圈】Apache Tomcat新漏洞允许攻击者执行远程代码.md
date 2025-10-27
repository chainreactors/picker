---
title: 【安全圈】Apache Tomcat新漏洞允许攻击者执行远程代码
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066717&idx=4&sn=b641682a1ea1ea39882cd929b37a230e&chksm=f36e7fddc419f6cba24202816ce961aac15b183ff97a27fbb019b434f5d7e60a6fdfa32e0d2d&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-20
fetch_date: 2025-10-06T19:39:05.316078
---

# 【安全圈】Apache Tomcat新漏洞允许攻击者执行远程代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgHibQfohsTenqicl4ia6QlKiciculKLpCtWRrnH1f6K5mX0g6AjH02CUdtAJ8ChJ0G57wJT1OX4aBXIsw/0?wx_fmt=jpeg)

# 【安全圈】Apache Tomcat新漏洞允许攻击者执行远程代码

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

据Cyber Security News消息，安全研究人员在流行的开源 Web 服务器 Apache Tomcat和servlet 容器中发现了两个严重漏洞，可能允许攻击者执行远程代码并导致拒绝服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgHibQfohsTenqicl4ia6QlKicicLUeHVxLII2uHvYaLf8F8nR7Dw3RwdZ9qj5tfSwFUTUAFcV8TtwD9wQ/640?wx_fmt=jpeg)

第一个漏洞被追踪为 CVE-2024-50379， 影响 Apache Tomcat  11.0.0-M1 到 11.0.1、10.1.0-M1 到 10.1.33 和 9.0.0.M1 到 9.0.97版本 。如果默认 servlet 在不区分大小写的文件系统上配置了写入权限，攻击者可在并发读取和上传操作期间利用竞争条件。这种绕过 Tomcat 大小写敏感性检查的做法会导致上传的文件被视为 JSP，最终导致远程代码执行。

第二个漏洞被追踪为 CVE-2024-54677，虽然严重性较低，但仍可能构成重大威胁。它影响相同版本的 Apache Tomcat，可使攻击者触发拒绝服务攻击。该漏洞源于 Tomcat 提供的 Web 应用程序示例，其中许多示例无法限制上传的数据大小，可能会导致 OutOfMemoryError，从而导致拒绝服务。

值得注意的是，默认情况下，示例网络应用程序只能从 localhost 访问，这在一定程度上限制了潜在的攻击面。

目前Apache 已经发布了解决这些安全漏洞的补丁，敦促用户立即升级：

* Apache Tomcat 11.0.2 或更高版本
* Apache Tomcat 10.1.34 或更高版本
* Apache Tomcat 9.0.98 或更高版本

这些漏洞的发现突显了在网络服务器环境中定期进行安全审计和及时打补丁的重要性。由于 Apache Tomcat 在企业环境中的广泛使用，因此这些漏洞的潜在影响十分巨大。

最近，Apache还披露了一个CVSS 4.0 评分高达9.5的高危漏洞，影响Apache Struts 2.0.0 到 2.3.37、2.5.0 到 2.5.33 以及 6.0.0 到 6.3.0.2版本，攻击者可以操纵文件上传参数以启用路径遍历，在某些情况下，这可能导致上传可用于执行远程代码执行的恶意文件 。

参考来源：New Apache Tomcat Vulnerabilities Let Attackers Execute Remote Code

***END***

阅读推荐

[【安全圈】2024年11月国内数据泄露及勒索事件汇总](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066682&idx=1&sn=2eb63c63a1b65f13023240b667bf4930&scene=21#wechat_redirect)

[【安全圈】知名间谍软件公司 Paragon 被美国私募收购](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066682&idx=2&sn=70318b76606cc51314d90fe11428590f&scene=21#wechat_redirect)

[【安全圈】APT组织开始大量抄袭红队先进的战术和工具](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066682&idx=3&sn=05ca26f017e4cc04fbaee8e8adfb38d9&scene=21#wechat_redirect)

[【安全圈】Meta因6年前的数据泄露事件被罚款2.64亿美元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066682&idx=4&sn=3d0218c3c7069eebaad560f58a4eca10&scene=21#wechat_redirect)

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