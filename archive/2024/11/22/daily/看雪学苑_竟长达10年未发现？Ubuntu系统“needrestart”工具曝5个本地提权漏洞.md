---
title: 竟长达10年未发现？Ubuntu系统“needrestart”工具曝5个本地提权漏洞
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458583634&idx=3&sn=53aa35b505b9bfdfb18d41e18d667703&chksm=b18c32d886fbbbcec2d582409e43ce8f26477a7d97ca397baab16e65b2b303e18496e0e72982&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-22
fetch_date: 2025-10-06T19:16:29.749868
---

# 竟长达10年未发现？Ubuntu系统“needrestart”工具曝5个本地提权漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HwdbmO6yqch99GQZNlSmtKIQeortd8Wsjd0HHH0hPc9PooZzR2dozftMgz7v7xGiciclRdrpg3Q5Nw/0?wx_fmt=jpeg)

# 竟长达10年未发现？Ubuntu系统“needrestart”工具曝5个本地提权漏洞

看雪学苑

看雪学苑

> 近日，Ubuntu系统中的“needrestart”实用程序被曝出存在5个本地权限提升（LPE）漏洞，这些安全缺陷已潜伏10年之久未被发现。这些漏洞由安全公司Qualys发现，并被分配了CVE编号，从2014年4月的Needrestart 0.8版本中引入，直至2024年11月19日才在3.8版本中得到修复。

Ubuntu系统中的“needrestart”实用程序近日被曝出存在5个本地权限提升（LPE）漏洞，这些漏洞已潜藏10年未被发现。这些安全缺陷由Qualys安全研究团队发现，并被跟踪为CVE-2024-48990、CVE-2024-48991、CVE-2024-48992、CVE-2024-10224和CVE-2024-11003。这些漏洞最早在2014年4月发布的Needrestart 0.8版本中引入，直到2024年11月19日才在3.8版本中得到修复。

这些漏洞允许攻击者在本地访问有漏洞的Linux系统时，在无需用户交互的情况下将权限提升至root。具体漏洞详情如下：

- CVE-2024-48990：Needrestart使用从运行进程中提取的PYTHONPATH环境变量执行Python解释器。如果攻击者能够控制该环境变量，他们可以通过植入恶意共享库，在Python初始化过程中以root身份执行任意代码。

- CVE-2024-48992：Needrestart使用的Ruby解释器在处理攻击者控制的RUBYLIB环境变量时存在漏洞。这使得攻击者能够通过向进程注入恶意库，以root身份执行任意Ruby代码。

- CVE-2024-48991：Needrestart中的争用条件允许攻击者用恶意可执行文件替换正在验证的Python解释器二进制文件。通过精确控制替换时机，攻击者可以诱使Needrestart以root身份运行他们的代码。

- CVE-2024-10224：Needrestart使用的Perl ScanDeps模块未能正确处理攻击者提供的文件名。攻击者可以创建类似于shell命令的文件名（例如command|），以便在打开文件时以root身份执行任意命令。

- CVE-2024-11003：Needrestart对Perl的ScanDeps模块的依赖使其暴露于ScanDeps本身的漏洞中，其中不安全地使用eval()函数会导致在处理攻击者控制的输入时执行任意代码。

值得注意的是，为了利用这些漏洞，攻击者必须通过恶意软件或被盗账户对操作系统进行本地访问，这在一定程度上降低了风险。然而，历史上攻击者也曾利用过类似的Linux权限提升漏洞来获得root权限，因此这些漏洞的修补不容忽视。

除了升级到Needrestart版本3.8或更高版本（包括所有已识别漏洞的补丁）之外，建议用户修改Needrestart.conf文件以禁用解释器扫描功能，从而防止漏洞被利用。

资讯来源：bleepingcomputer

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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