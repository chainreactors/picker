---
title: 【安全圈】关键的Windows UI自动化框架漏洞允许黑客绕过EDR
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066594&idx=3&sn=fb1485e3b4a0ed439c616f967bfc2543&chksm=f36e7f62c419f674925c4fd86653e81123e3e05d411e575edd5ffcf7b8c21e0c38337de1b810&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-14
fetch_date: 2025-10-06T19:41:23.938776
---

# 【安全圈】关键的Windows UI自动化框架漏洞允许黑客绕过EDR

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljGyHYwcz2gbXHesVAr8Ipf1QaDO2PSTAjJbbfy4pEWBlxh2j6n8bFTUs9SylAicMTVQNvwepL7ZxQ/0?wx_fmt=jpeg)

# 【安全圈】关键的Windows UI自动化框架漏洞允许黑客绕过EDR

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

一种新近开发的技术，利用了Windows的一个辅助功能框架——UI Automation（UIA），来执行多种恶意活动，同时巧妙地避开了端点检测和响应（EDR）解决方案的监控。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljGyHYwcz2gbXHesVAr8IpfpMj5I7OK4jA8ndAHDhoq6rQ3aWza49SyQb42NibRLNJsA3mMiaFFjDEQ/640?wx_fmt=jpeg&from=appmsg)

Akamai的安全研究员Tomer Peled在一份与The Hacker News分享的报告中指出：“要利用这项技术，必须说服用户运行一个利用UI Automation的程序。”这可能导致隐蔽的命令执行，进而窃取敏感数据、将浏览器重定向至网络钓鱼网站等。

更糟糕的是，本地攻击者可能会利用这一安全漏洞执行命令，从Slack和WhatsApp等消息应用中读取或发送消息。此外，这种技术还可能被用来通过网络操控用户界面元素。

UI Automation最初随Windows XP和Microsoft .NET Framework一同推出，旨在提供对各种用户界面（UI）元素的程序化访问，并帮助用户通过辅助技术产品（如屏幕阅读器）来操作这些元素，它也可用于自动化测试场景。

微软在一份支持文件中提到：“辅助技术应用通常需要访问受保护的系统UI元素，或者可能以更高权限运行的其他进程。因此，辅助技术应用必须获得系统的信任，并以特殊权限运行。”

“要访问更高权限级别的进程，辅助技术应用必须在应用的清单文件中设置UIAccess标志，并由具有管理员权限的用户启动。”

与其他应用中的元素进行UI交互，是通过组件对象模型（COM）作为进程间通信（IPC）机制来实现的。这使得创建UIA对象成为可能，通过设置事件处理程序，在检测到特定UI变化时触发，从而与焦点应用进行交互。

Akamai的研究发现，这种方法也可能被滥用，允许恶意行为者读取或发送消息、窃取在网站（如支付信息）中输入的数据，并在浏览器中当前显示的网页刷新或更改时执行命令，将受害者重定向至恶意网站。

Peled指出：“除了我们可以在屏幕上与之交互的UI元素外，还有更多的元素被预先加载并存储在缓存中。我们也可以与这些元素交互，比如阅读屏幕上未显示的消息，甚至在屏幕上不显示的情况下设置文本框并发送消息。”

需要指出的是，这些恶意场景都是UI Automation的预期功能，类似于Android的辅助服务API已经成为恶意软件从受感染设备中提取信息的常用手段。

Peled补充说：“这归根结底是应用程序的预期用途：这些权限级别必须存在才能使用它。这就是为什么UIA能够绕过Defender——应用程序没有发现任何异常。如果某功能被视为特性而非缺陷，机器的逻辑就会遵循这一特性。”

Deep Instinct披露，分布式COM（DCOM）远程协议允许软件组件通过网络通信，可能被利用来远程编写自定义有效载荷，创建嵌入式后门。

安全研究员Eliran Nissan表示：“这种攻击允许在目标机器上编写自定义DLL，将它们加载到服务中，并使用任意参数执行它们的功能。”这种后门式攻击滥用了IMsiServer COM接口。

Nissan说：“到目前为止，DCOM横向移动攻击的研究主要集中在基于IDispatch的COM对象上，因为它们可以被脚本化。”新的“DCOM上传和执行”方法“远程将自定义有效载荷写入受害者的[全局程序集缓存]，从服务上下文执行它们，并与它们通信，有效地充当嵌入式后门。这里的研究证明，许多意想不到的DCOM对象可能被用于横向移动，应该对齐适当的防御措施。”

参考来源：https://thehackernews.com/2024/12/new-malware-technique-could-exploit.html

***END***

阅读推荐

[【安全圈】大量用户吐槽，Microsoft 365 又大面积宕机](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066578&idx=1&sn=1294f1f07ab020666e22003bce0314b4&scene=21#wechat_redirect)

[【安全圈】OpenAI、Facebook、Instagram、WhatsApp 集体全球宕机](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066578&idx=2&sn=464a287f7dc747494c68e686a161ab77&scene=21#wechat_redirect)

[【安全圈】知名企业级文件传输产品存在漏洞，正在被黑客利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066578&idx=3&sn=55d3538cbf8999a9aa8be86d3ea965e6&scene=21#wechat_redirect)

[【安全圈】Windows 远程桌面服务漏洞允许攻击者执行远程代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066578&idx=4&sn=fb9fe492092fe4a3088d8bcf368835be&scene=21#wechat_redirect)

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