---
title: 【安全圈】Bootkitty——首个针对Linux的UEFI引导程序恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066267&idx=4&sn=2e12d00121b83ddf62b939eea70ced2a&chksm=f36e7d9bc419f48d99a96d109e23a285f494a30a04a14d018c34cce2f40f6c231e40cc100242&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-29
fetch_date: 2025-10-06T19:17:57.689708
---

# 【安全圈】Bootkitty——首个针对Linux的UEFI引导程序恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg4kbtk0IKFiboTvHdnHibVXNFasQSS6m5ia4iawSkniadfTRsTPwRDiaOdqEWoR7W6DnOEeMbaibK92xwjQ/0?wx_fmt=jpeg)

# 【安全圈】Bootkitty——首个针对Linux的UEFI引导程序恶意软件

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

研究人员发现了首个专门针对Linux系统UEFI引导程序恶意软件，这标志着以前专注于Windows的隐蔽且难以清除的引导程序威胁发生了转变。

这款名为“Bootkitty”的Linux恶意软件是一个概念验证，仅在某些Ubuntu版本和配置上有效，而不是实际攻击中部署的完全成熟的威胁。引导程序恶意软件旨在感染计算机的启动过程，在操作系统加载之前运行，从而允许其在非常低的级别上控制系统。

这种做法的优势在于，引导程序可以规避在操作系统级别运行的安全工具，并修改系统组件或注入恶意代码而不被检测到。发现Bootkitty的ESET研究人员警告说，尽管目前对现实世界的影响有限，但它的存在是UEFI引导程序威胁领域的一个重要演变。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg4kbtk0IKFiboTvHdnHibVXNbzEoMwQlBsibYd9yLicyiaYibCTRYOn7ZdAmkTNOFYEXKoPOFzYN75mLKw/640?wx_fmt=jpeg&from=appmsg)ESET在2024年11月检查VirusTotal上传的一个可疑文件（bootkit.efi）后发现了Bootkitty。经过分析，ESET确认这是第一个绕过内核签名验证并在系统启动过程中预加载恶意组件的Linux UEFI引导程序案例。

Bootkitty依赖于自签名证书，因此它不会在启用安全启动的系统上执行，只针对某些Ubuntu发行版。此外，硬编码的偏移量和简化的字节模式匹配使其仅适用于特定的GRUB和内核版本，因此不适合广泛部署。

ESET还指出，恶意软件包含许多未使用的功能，并且处理内核版本兼容性不佳，常常导致系统崩溃。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg4kbtk0IKFiboTvHdnHibVXNCI6FzUGBzo2KWjIT9icPM66JQxSgvBkk5zu5KRKt22ASrIQK36N4zSQ/640?wx_fmt=jpeg&from=appmsg)引导程序中包含的ASCII，来源：ESET

恶意软件的缺陷性质以及ESET的遥测数据显示Live系统上没有Bootkitty的迹象，使研究人员得出结论，它处于早期开发阶段。

## Bootkitty的能力

在启动过程中，Bootkitty挂钩UEFI安全认证协议（EFI\_SECURITY2\_ARCH\_PROTOCOL和EFI\_SECURITY\_ARCH\_PROTOCOL），以绕过安全启动的完整性验证检查，确保引导程序加载，无论安全策略如何。

接下来，它挂钩各种GRUB函数，如'start\_image'和'grub\_verifiers\_open'，以操纵引导加载程序对二进制文件的完整性检查，包括Linux内核，关闭签名验证。

然后，Bootkitty截获Linux内核的解压缩过程，并挂钩'module\_sig\_check'函数。这迫使它在内核模块检查期间始终返回成功，允许恶意软件加载恶意模块。

此外，它将第一个环境变量替换为'LD\_PRELOAD=/opt/injector.so'，以便在系统启动时将恶意库注入进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg4kbtk0IKFiboTvHdnHibVXNHGUYOhQaUTIkicyRgN7jqzhziaVVBicianiaGdzugB8XFNWlrI4nFAiacY3w/640?wx_fmt=jpeg&from=appmsg)Bootkitty执行流程的一部分，来源：ESET

整个过程留下了几个工件，有些是有意的，有些则不是，ESET解释说，这也是Bootkitty缺乏精细化的另一个佐证。研究人员还指出，上传Bootkitty到VT的同一用户还上传了一个名为'BCDropper'的未签名内核模块，但现有证据只能弱弱地将两者联系起来。

BCDropper会释放一个名为'BCObserver'的ELF文件，这是一个具有rootkit功能的内核模块，在受感染的系统上隐藏文件、进程并打开端口。这种类型恶意软件的发现说明了攻击者是如何开发之前仅限于Windows的Linux恶意软件的，因为企业越来越多地采用Linux。

与Bootkitty相关的入侵指标（IoCs）已在此GitHub存储库中共享。

参考来源：https://www.bleepingcomputer.com/news/security/researchers-discover-bootkitty-first-uefi-bootkit-malware-for-linux/

***END***

阅读推荐

[【安全圈】VPN正在成为企业入侵的关键路径](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066249&idx=1&sn=c8eb4e218d2e6d7fd61aac243bb505d9&scene=21#wechat_redirect)

[【安全圈】星巴克遭勒索攻击，回到纸质办公时代](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066249&idx=2&sn=a365288784024618dd0cceec41933f95&scene=21#wechat_redirect)

[【安全圈】Firefox和Tor浏览器遭遇神秘0Day漏洞攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066249&idx=3&sn=c16dd8113efa3f879e94a0128384f7be&scene=21#wechat_redirect)

[【安全圈】CVE-2024-8114：GitLab 漏洞允许权限升级](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066249&idx=4&sn=df7d811b5e62d6af63575344f1f21cad&scene=21#wechat_redirect)

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

阅读原文

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