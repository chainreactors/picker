---
title: .NET 一款解密CryptoObfuscator混淆的工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247494191&idx=1&sn=0f0c5eb910bcc52933d5d8f36e6af679&chksm=fa5944c2cd2ecdd4a8f434b34cb71180a50407b3369fa8be7fc4e7d3eb510eec50f78b7e6cde&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-08-06
fetch_date: 2025-10-06T18:05:02.835626
---

# .NET 一款解密CryptoObfuscator混淆的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8ibzXywvcYz5icO6VdOC7fianoK32yymzNvJdM7qTSZ3miaefzicNr0DX5pSicrmHVthFQhJkbRaYsyFUg/0?wx_fmt=jpeg)

# .NET 一款解密CryptoObfuscator混淆的工具

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

基本介绍

**Sharp4CryptoDeobfuscator** 是一款强大的工具，专为反混淆和解密使用 Crypto Obfuscator 保护的 .NET 程序而设计。该工具提供了多种功能，包括浮点解密、字符串解密、垃圾代码删除和调试器控制移除。目前，它仅支持可执行文件（.exe），未来版本计划支持动态链接库文件（.dll）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8ibzXywvcYz5icO6VdOC7fianrFGT8QbNxCRibdtS1n8seE0No4N8nsJCmCCrHZ8wtPyhtX0ul5libwSQ/640?wx_fmt=jpeg&from=appmsg)

03

功能描述

在Web应用程序中，ViewState 是.NET框架用于在页面请求之间维护状态的一种机制，攻击者可能会利用其中的漏洞执行远程代码执行（RCE）攻击。这正是ysoserial工具发挥其作用的地方，特别是在针对ViewState序列化漏洞时，以下是一个通过ViewState 触发反序列化漏洞的示例负载。

## 3.1 浮点解密

此功能针对使用浮点数进行混淆的值。Sharp4CryptoDeobfuscator 可以识别并还原这些被混淆的值，使代码更易于分析和调试。

## 3.2 字符串解密

混淆字符串是保护敏感信息和代码逻辑的常见技术。该工具可以解密这些字符串，使代码更加可读和易于理解

## 3.3 垃圾代码删除

感垃圾代码或“死代码”被添加到混淆程序中，Sharp4CryptoDeobfuscator 可以识别并删除这些不必要的代码，简化反编译输出。

## 3.4 调试器移除

混淆器通常添加反调试措施以防止分析。该工具可以去除这些控制，使您可以在去混淆的程序上使用标准调试工具。

04

基本用法

要确定 .NET 程序是否使用 Crypto Obfuscator 保护，可以使用如 DIE (Detect It Easy) 之类的工具。如果 DIE 显示存在 Crypto Obfuscator (例如“Crypto Obfuscator For .Net(5.X)[-]”)，Sharp4CryptoDeobfuscator 是处理反混淆的合适工具。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ibzXywvcYz5icO6VdOC7fianaVVFRpSjib7W1cjpZdX2jU5Nx6W7b6ViaDUMicP5E3BWbibnHUjJibGHYLg/640?wx_fmt=png&from=appmsg)

反混淆前的代码包含了大量的垃圾代码和调试器控制等，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ibzXywvcYz5icO6VdOC7fianmP9BbsvQas49ibL0qoz1phAo1PM30RwlxModm2HHwKz6CXRcJDKb4XA/640?wx_fmt=png&from=appmsg)

自动化反混淆比手动逆向工程节省时间，解密的字符串和删除的垃圾代码使输出更加可读和易于理解，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ibzXywvcYz5icO6VdOC7fianqQNYyKib9yJtZHaptzTvyesvt4f1eU0btFNjiabOTgZEBS0cYR7FkN4w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8ibzXywvcYz5icO6VdOC7fiangtFd76fymBzDkMXOz8ax2BTGicWeh9SLyTFHxEibUKbfCoHFJe0emxVA/640?wx_fmt=png&from=appmsg)

综上，Sharp4CryptoDeobfuscator 对于处理混淆程序集的 .NET逆向人员来说是一款宝贵的工具。工具已经打包在星球，感兴趣的朋友可以加入自取。

05

推荐阅读

从漏洞分析到安全攻防，我们涵盖了.NET安全各个关键方面，为您呈现最新、最全面的.NET安全知识，下面是公众号发布的精华文章集合，推荐大家阅读！

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5jtGD7iaMnQxKfLfibIwMQP6vlheBicOeYPibv4Nu5fxtEibLibdJSW8HPp7w/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=3&sn=88060c78ccd74089bfe67682e79497d8&chksm=fa5947adcd2ecebbe09ba231b44c9574b5cc88f6d8e934989e3953856301fa071ae39aa827d6&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8TQhCZMggf71ffibqISJ8f5naPJacnjn0roDyxxnAibmuwDJq2p1GTBpicZhnM9o9gTIu9S9ia8Uqwtw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247493952&idx=4&sn=db68011fb075c1d02268811163646b53&chksm=fa5947adcd2ecebbb1ca6659f289a5e344e37d1136fe0bd9272b5578e4c71bb19bb250e934d3&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOE2ogFoYIdqnYynqF6XyicI7XfRsWsn36wsCpKpAJcIQOicZUhbDJOe0w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488762&idx=1&sn=a5710927a6ba09b5c83adf616e2b12ae&chksm=fa5aba17cd2d330119d1ab2ce4b3a434274f0adf96729dbf8f04bef16c389565fc144f84d341&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOeP3ichLEiafhGiawd8mjkHYBalO37fN8QQkNdic1hjjY2Nvw2Bib6UvibDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490722&idx=2&sn=c9807daa5548e139a0c67303cb26882a&chksm=fa5ab24fcd2d3b59a85be03e69c655ffd644e8458bc2ec3f572da4b40b43e5003fda756f35b4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOjWgak8cI7Mic1wTt3YSKqsbLl9rPe0cF9WGtOEuiceLreTNtNVib6IKlw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490703&idx=2&sn=e7db1ff662e5b41d9a1806fbdf33e204&chksm=fa5ab262cd2d3b7470f029b9a07d1dd3611e63be910b01a601144efe7d84b5f016f488a354cf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxO8jJ97qqWlY6XR03DqSnutcHFYibDtVG5Y2wEaK4p2bzEicZblY4oQyGg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247490700&idx=2&sn=e8a865ada7c743e77fb9e953c5da74b1&chksm=fa5ab261cd2d3b7736387eddfc8524a378a1604552d0c9b55476646f9e8275f48818aab8acad&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOe1viaia4aoFceunsUdIna4DPbmemW1EqlBMrovOoE6bdAFF3iaApxz5qA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247488736&idx=2&sn=d24aaa297c51eb620ccdf67af513086d&chksm=fa5aba0dcd2d331bbb22f3f5657199d718c90efed42fcb9cb67ec23d342f887c117e4858f1cb&scene=21#wechat_redirect)

06

欢迎加入.NET安全星球

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。 星球门票后期价格随着内容和质量的不断沉淀会适当提高，因此越早加入越好！

    目前dot.Net安全矩阵星球已成为中国.NET安全领域最知名、最活跃的技术知识库之一，从.NET Framework到.NET Core，从Web应用到PC端软件应用，无论您是初学者还是经验丰富的开发人员，都能在这里找到对应的安全指南和最佳实践。

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布很多高质量的.NET安全资源，可以说市面上很少见，都是干货。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibzerwUbGOupPoJgYlZNMo1gg58eGoicPibjMBKkEo1zOia6zOyeupYasZZ9DTFvJVvzJQTEuhKrvTsA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibQ6VpnKYXPqfmHnyJHzHxOc2SogKzZ16SD7dpzF3v81kia4ZAx5QU5ibnNibEo8kZZSJgrficz4Ckxwg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

星球文化始终认为授人以鱼不如授人以渔！加入星球后可以跟星主和嘉宾们一对一提问交流，20+个专题栏目涵盖了点、线、面、体等知识面，助力师傅们快速成长！其中主题包括.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库等等。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YiccvW0LwqSx3grm4bgM0fz01qCxrYGBR94wibZ7sk1zIO9DzCgviab9vmUic8qmvynXhSM8LxFhGG97w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

    我们倾力打造专刊、视频等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9XgicSeCfnDO0KyvDNdCZhG3pTSWHRekG0Wrp0FXyHO1mz9ia5uiaICjCmg5jIzx4ERLU8MjXWVSkCw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

我们还有一个会员专属的内部星球陪伴群，加入的成员可以通过在群里提出问题或参与论的方式来与其他成员交流思想和经验。此外还可以通过星球或者微信群私聊向我们进行提问，以获取帮助迅速解决问题。

为了助力大家在2024国家级hvv演练中脱颖而出，我们特别整理出了一套涵盖dotNet安全矩阵星球的八大.NET相关方向工具集。

```
.NET 免杀WebShell
.NET 反序列化漏洞
.NET 安全防御绕过
.NET 内网信息收集
.NET 本地权限提升
.NET 内网横向移动
.NET 目标权限维持
.NET 数据外发传输
```

这些阶段所涉及的工具集不仅代表了当前.NET安全领域的最前沿技术，更是每一位网络安全爱好者不可或缺的实战利器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9ZQNibdZiazXl9zhxh3wB9n5LXcwJqbvQywJQLsckcGGV6NNWLITK1VkDV2CPeahvyUbPNPCRATEmA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

dotNet安全矩阵

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

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