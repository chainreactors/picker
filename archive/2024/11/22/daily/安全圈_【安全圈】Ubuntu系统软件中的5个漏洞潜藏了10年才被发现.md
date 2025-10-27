---
title: 【安全圈】Ubuntu系统软件中的5个漏洞潜藏了10年才被发现
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066112&idx=1&sn=00fc32fb2126236a289beba3ec9b7b29&chksm=f36e7d00c419f41616a3b529fd231f5c9cb584fc1c962df2286ebe434d3081d23b39cd91ade2&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-22
fetch_date: 2025-10-06T19:17:02.090474
---

# 【安全圈】Ubuntu系统软件中的5个漏洞潜藏了10年才被发现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylggLicm6zgDUAd59I5kicYGLSjFjBgHfEvq9nOMRYPWib3WBYar46VvVq0yiaibpqe3SZNGjIMdXfycibbQ/0?wx_fmt=jpeg)

# 【安全圈】Ubuntu系统软件中的5个漏洞潜藏了10年才被发现

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

Ubuntu系统中的实用程序 needrestart 近日被曝出存在5个本地权限提升 （LPE） 漏洞，这些漏洞不是最近才产生，而是已经潜藏了10年未被发现。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylggLicm6zgDUAd59I5kicYGLSpjFKcLT8LWd1I4YMZzdzBhRHl9sNMavBkxKu7BA0XOZ6Dc1wh4GPyQ/640?wx_fmt=jpeg&from=appmsg)

这些漏洞由 Qualys 发现，并被跟踪为 CVE-2024-48990、CVE-2024-48991、CVE-2024-48992、CVE-2024-10224 和 CVE-2024-11003，由 2014 年 4 月发布的Needrestart  0.8 版本中引入，直到最近的11月19日才在3.8 版本中修复。

这5个漏洞允许攻击者在本地访问有漏洞的 Linux 系统，在没有用户交互的情况下将权限升级到 root：

* CVE-2024-48990：Needrestart 使用从运行进程中提取的 PYTHONPATH 环境变量执行 Python 解释器。如果本地攻击者控制了这个变量，就可以通过植入恶意共享库，在 Python 初始化过程中以 root 身份执行任意代码。
* CVE-2024-48992：Needrestart 使用的 Ruby 解释器在处理攻击者控制的 RUBYLIB 环境变量时存在漏洞。这允许本地攻击者通过向进程注入恶意库，以 root 身份执行任意 Ruby 代码。
* CVE -2024-48991：Needrestart 中的争用条件允许本地攻击者用恶意可执行文件替换正在验证的 Python 解释器二进制文件。通过仔细把握替换时机，可以诱使 Needrestart 以 root 身份运行他们的代码。
* CVE-2024-10224：Needrestart 使用的 Perl ScanDeps 模块未正确处理攻击者提供的文件名。攻击者可以制作类似于 shell 命令的文件名（例如 command|），以便在打开文件时以 root 身份执行任意命令。
* CVE-2024-11003：Needrestart 对 Perl 的 ScanDeps 模块的依赖使其暴露于 ScanDeps 本身的漏洞中，其中不安全地使用 eval（） 函数会导致在处理攻击者控制的输入时执行任意代码。

值得注意的是，为了利用这些漏洞，攻击者必须通过恶意软件或被盗帐户对操作系统进行本地访问，这在一定程度上降低了风险。但攻击者过去也利用过类似的 Linux 权限提升漏洞来获得 root 权限，包括 Loony Tunables 和利用 nf\_tables 漏洞，因此不能因为这些漏洞需要本地访问权限就疏于修补。

除了升级到版本 3.8 或更高版本（包括所有已识别漏洞的补丁）之外，建议用户修改Needrestart.conf 文件以禁用解释器扫描功能，从而防止漏洞被利用。

参考来源：Ubuntu Linux impacted by decade-old 'needrestart' flaw that gives root

***END***

阅读推荐

[【安全圈】苹果手机72小时不用会自动锁死？](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066097&idx=1&sn=6b2503a2e569d80705cada518019361e&chksm=f36e7d71c419f4675e3986754fc7b32cd6d7589cac2505e25c84a51ded871da048608e7fe980&scene=21#wechat_redirect)

[【安全圈】涉嫌强迫用户共享数据，印度对Meta处以2500万美元罚款](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066097&idx=2&sn=1a5dd1ca6f2eb61c32d863fb63f4c5f8&chksm=f36e7d71c419f4677edcbb49aa84592cb0b2db6ffdfe051b4cad624bd7567c52e9f0ba1802fd&scene=21#wechat_redirect)

[【安全圈】苹果发布紧急安全更新修复WebKit引擎中的漏洞 黑客已经利用漏洞展开攻击](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066097&idx=3&sn=0e0cc754f2cdc596b5f8419a8fa6f7a5&chksm=f36e7d71c419f467daf3ea8cddb360e80ba1bf2d4166d38a18b9e3f18237b4be22f6661fe72a&scene=21#wechat_redirect)

[【安全圈】越来越多的国家正在为“黑客”松绑？](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066097&idx=4&sn=4c89dea98b272ff7dffa7f78d293c288&chksm=f36e7d71c419f467dbcdf3ea7de6e01f01c01afb2d854b3a7651a5f21daec878f96818777f10&scene=21#wechat_redirect)

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