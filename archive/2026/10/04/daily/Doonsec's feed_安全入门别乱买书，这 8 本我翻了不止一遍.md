---
title: 安全入门别乱买书，这 8 本我翻了不止一遍
url: https://mp.weixin.qq.com/s/DKq5TQ08oUJnga-RJz37Gw
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:56:50.516646
---

# 安全入门别乱买书，这 8 本我翻了不止一遍

# 安全入门别乱买书，这 8 本我翻了不止一遍

原创

大白
大白

知白守黑1024

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

上周一个刚想转行的朋友发消息问我，想做网络安全，该从哪本书开始。

我想了挺久，没直接回。这个问题其实问浅了。

网上随手一搜，「七天入门」「三十天精通」的书单一抓一大把。可真读进去你会发现，多数书是在教你点哪个按钮，而不是告诉你漏洞为什么会存在。

这几年我陆陆续续读了几十本，最后留在桌上、会反复翻的，只剩下面这八本。

我按从思维到实战的顺序排了一遍。你可以顺着读，也可以挑自己缺的那块补。

① 黑客与画家  ② 白帽子讲Web安全  ③ 图解密码技术 ④ Web安全深度剖析  ⑤ 黑客之道  ⑥ Web之困 ⑦ 渗透测试实践指南  ⑧ 0day安全

这几本都不是轻松读物。它们要你动脑，有几本还要你动手。

01

黑客与画家

保罗·格雷厄姆（Paul Graham）著　人民邮电出版社 · 图灵

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1gs1BIsQib7JnBpZ00EDbJnSbZRHlBJnWzS3595jboOQljQbX1qQqCBXawdYq0FrvxXl55X1E3cTDheJEwSP6SoBXatJjzLrialg/640?wx_fmt=jpeg&from=appmsg)

这不是一本安全技术书，但没有它，后面七本你都读不透。

保罗·格雷厄姆讲的是黑客到底是一群什么人。他们不是搞破坏的，是把「做出好东西」当成乐趣的创造者。书里那篇《书呆子的复仇》我读了很多遍，它解释了为什么聪明人常常在主流之外找到机会。

先读它，是为了搞明白自己为什么要进这一行。

02

白帽子讲Web安全

吴翰清 著　电子工业出版社

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1hlrmFAQR5U9NVmnqcJPhtRhkTgfgWx3vOM1sqDyXvx7OYmNmvw6CEibAE6rlynIvbpaRMMKIibubL8IxRzXL8XLjKLYt3mzRzaU/640?wx_fmt=jpeg&from=appmsg)

国内 Web 安全最经典的一本，没有之一。

吴翰清从安全世界观讲起，再一层层落到浏览器安全、XSS、CSRF、注入、认证与会话、加密算法。它最难得的地方，是**把「为什么会有这个漏洞」讲明白，而不是丢一堆 payload 让你照着打**。

做 Web 安全，这本应该是你的第一块地基。

03

图解密码技术（第3版）

结城浩 著　周自恒 译　人民邮电出版社 · 图灵

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1gzdhQNoFygZOL153PkPbA5pyLc0utf4wqribmdGdyIhSo9VxicTeG4LicFgPxyk11phkNnDECNHxcmwdpyaVoB9bgDVHEYJrWgGY/640?wx_fmt=jpeg&from=appmsg)

密码学最容易劝退人，这本书偏偏把它讲成了故事。

结城浩用大量插图和日常例子，把对称加密、公钥、哈希、证书、TLS 一路讲下来，连椭圆曲线和比特币这些新内容都补齐了。你不需要多强的数学底子，也能读懂密钥交换到底安全在哪。

想真正搞懂 HTTPS 背后发生了什么，看它就够了。

04

Web安全深度剖析

张炳帅 著　电子工业出版社

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1jj3Xv6iaGibrpAk4YSAeXPwvvFpfuBOy8VRn6iabExMtEWiaX9j9FVkictVrlCorOVwPqS1yW2LfB9Luicr7M2ZFR3U7vlCutR3TpdM/640?wx_fmt=jpeg&from=appmsg)

如果说白帽子讲的是「道」，这本讲的是「术」。

张炳帅把 SQL 注入、XSS、CSRF、文件上传、命令执行、提权挨个拆开，配着靶场和工具一步步带你走。它不厚，但足够实在，适合你已经知道原理、准备真正动手的时候翻开。

唯一的提醒是，书里的靶场要自己搭一遍。光看，是学不会的。

道和术，缺一个都走不远。

05

黑客之道：漏洞发掘的艺术（原书第2版）

Jon Erickson 著　中国水利水电出版社

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1iaFNNAAPvTMGsfJVa736q3DUbZarjStibNwFLib2zAmuAlgAWq7qgDdAwhIsFKgWjg0M21Jq647ibsCVCicqmS3I16GrMGLTeuaV0k/640?wx_fmt=jpeg&from=appmsg)

这本会把你从「会用工具」拽回「懂原理」。

Jon Erickson 用 C 语言带你重走一遍内存、栈、堆、缓冲区溢出、shellcode，直到你自己能写出一个可用的利用。前几章确实枯燥，但熬过去之后，你看漏洞的眼光会彻底不一样。

**它是很多人从脚本小子走向真正研究者的分水岭。**

06

Web之困：现代Web应用安全指南

Michal Zalewski 著

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1hyCScrnMsx6P47WLyfmNgcibwspuqFqDubAlibDVINLGTL8kmXTjcXTEyEQMqbO22s66BAoXu7xQTnPicy6QQ7WkNHHBcBuuEryU/640?wx_fmt=jpeg&from=appmsg)

浏览器安全领域绕不开的一本。

Michal Zalewski 不教你怎么打，而是解释浏览器内部那些「看起来理所当然、其实全是坑」的设计，同源策略、来源判断、页面导航、Cookie、HTML 解析的怪异行为。

读完你会明白，很多漏洞不是程序员不小心，是这套系统本身太复杂。它是给想往深里走的人准备的。

07

渗透测试实践指南：必知必会的工具与方法

Patrick Engebretson 著　机械工业出版社

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1hewOpEYfL98Sq2feDQmpZCERclhjcqibVkQvPDwtZWhwcjCzr4bphRpnx0KuN4UDySZB9hMK0QBicUeRmTpiaGAoo8rxicZ8hSJPQ/640?wx_fmt=jpeg&from=appmsg)

想入门渗透测试，这本是我最愿意推荐的第一步。

Patrick Engebretson 把一次完整测试拆成侦查、扫描、利用、维持访问、写报告五个阶段，每个阶段都配上 Kali 里最基本的工具和一个能跑通的例子。它不炫技，但流程完整、门槛低。

等你把这条流水线跑顺了，再去啃 Metasploit 和更深的东西也不迟。

08

0day安全：软件漏洞分析技术（第2版）

王清 主编　电子工业出版社

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1gG5ojfFgK7JD39Jgrh4ybQRW1iccRCvX19ichJx8icN0d6chPpAQkT676vxkERAySWj9lVxBEva4k4QE7VztY9hWeH3VUqox2ib2A/640?wx_fmt=jpeg&from=appmsg)

最后一本，留给真正的硬骨头。

王清这本是国内二进制漏洞分析的经典，从栈溢出讲到堆溢出，再讲到各种安全防护机制怎么被绕过。它需要你有 C、汇编和操作系统的底子，读起来绝不轻松。

但如果你有志做漏洞挖掘或者逆向，这本值得放在桌上慢慢啃。

八本读下来你会发现一件事。

技术会过时，工具会换代，书里的具体 payload 几年后可能全都失效。

真正留下来的，是那套**先问为什么、再动手**的习惯。

安全这行最不缺教程，最缺的是愿意把一个漏洞追到根上的人。

如果这份书单对你有用，转给那个刚想入门的朋友。

end

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zlD2iah6QpJjciciaI6Ylp5L7rn9Y2O6cTxzf9Suxyw0cwibRgVtpuBzNrqS1ibK3USX8IXHulcNen2rMApDXn352cg/0?wx_fmt=png)

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