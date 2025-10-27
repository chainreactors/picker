---
title: 【安全圈】新型恶意软件能利用LogoFAIL漏洞感染Linux系统
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066393&idx=4&sn=b1e7b15689fa221569f9a1cad7eff071&chksm=f36e7e19c419f70f532549488e0e8d0f8aae4d951c7530354d032c143effdb2584400674cfa0&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-04
fetch_date: 2025-10-06T19:39:08.289697
---

# 【安全圈】新型恶意软件能利用LogoFAIL漏洞感染Linux系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljNjbcFCaXKEbVibCkASomibXhYUPxILUJZE3OlzfMjPnCfUNqhrrmdsSQ9qDxic40ZtTdGX8rYzo4Hw/0?wx_fmt=jpeg)

# 【安全圈】新型恶意软件能利用LogoFAIL漏洞感染Linux系统

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

据BleepingComputer消息，韩国Best of the Best （BoB） 培训计划的网络安全学生利用 LogoFAIL 漏洞创建了新型恶意软件Bootkitty，能够攻击Linux系统设备。

固件安全公司Binarly 于2023 年 11 月发现了 LogoFAIL，并警告其可能被用于实际攻击。而安全公司ESET表示，Bootkitty 是第一个专门针对 Linux系统的恶意软件。

LogoFAIL 是图像解析代码中的一组缺陷，源自各种硬件供应商使用的 UEFI 固件映像，可被植入 EFI 系统分区 （ESP） 上的恶意图像或徽标利用。Binarly指出，当这些镜像在启动过程中被解析时，可以触发漏洞，并且可以任意执行攻击者控制的有效负载来劫持执行流程并绕过安全启动，包括基于硬件的验证启动机制。

根据 Binarly 的最新研究，Bootkitty 在 BMP 文件（"logofail.bmp "和 "logofail\_fake.bmp"）中嵌入了 shellcode，通过向 MokList 变体注入流氓认证来绕过安全启动保护。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljNjbcFCaXKEbVibCkASomibXEogQPRib02NRXELweJxhIDjcrs72ibyAYEZwnCCmFWic3nFOSJW8zQg4Q/640?wx_fmt=jpeg&from=appmsg)恶意图片文件

合法的 MokList 被替换为恶意证书，从而有效地授权了恶意引导程序（'bootkit.efi'）。在将执行转移到 shellcode 之后，Bootkitty 会用原始指令恢复漏洞函数 (RLE8ToBlt) 中被覆盖的内存位置，因此任何明显的篡改痕迹都会被清除。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljNjbcFCaXKEbVibCkASomibXm4pXFAcE0Hop5D8MsYMdVyse5hW0ibEZoenubxiaQVx65M7mvPcq8sow/640?wx_fmt=jpeg&from=appmsg)攻击链概述

## 对特定硬件的影响

Bootkitty 可能会影响任何未对 LogoFAIL 进行修补的设备，但其当前的shellcode限于宏碁、惠普、富士通和联想电脑上固件模块使用的特定代码。

研究人员对 bootkit.efi 文件的分析确定，基于 Insyde 的联想设备最容易受到影响，因为 Bootkitty 引用了该品牌使用的特定变量名称和路径。但是，这可能表明开发人员只是在自己的笔记本电脑上测试 bootkit，稍后将添加对更广泛设备的支持。

一些最新固件仍然容易受到 LogoFAIL 漏洞的影响，包括联想IdeaPad Pro 5-16IRH8、IdeaPad 1-15IRU7、Legion 7-16IAX7、Legion Pro 5-16IRX8 和Yoga 9-14IRP8。

虽然该恶意软件是出于安全目的而研发，但Binarly警告称，自从首次敲响 LogoFAIL 警报以来已经一年多，仍有许多厂商产品仍然会受到 LogoFAIL 漏洞的一种或多种变体的影响。对此，建议受影响的用户限制物理访问、启用安全启动、密码保护 UEFI/BIOS 设置、禁用从外部介质启动，并且只从官方网站下载固件更新。

参考来源：BootKitty UEFI malware exploits LogoFAIL to infect Linux systems

***END***

阅读推荐

[【安全圈】知名科技公司员工举报公司高管系美国间谍？公司回应，疑点重重](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066376&idx=1&sn=be6fcf97a8eeb2bc8145ab42b1be777c&scene=21#wechat_redirect)

[【安全圈】摄像头贴很有必要，黑客可不激活指示器而调用摄像头](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066376&idx=2&sn=7f9d672677e1dcb0f7e67405da112ae9&scene=21#wechat_redirect)

[【安全圈】新型钓鱼工具包能让“菜鸟”轻松发动攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066376&idx=3&sn=35d457660d9cc1755f262a4e5f6fe6b4&scene=21#wechat_redirect)

[【安全圈】损坏的Word钓鱼文件可以绕过微软安全防护？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066376&idx=4&sn=4a3ea073cc936b52c057d059b24874a6&scene=21#wechat_redirect)

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