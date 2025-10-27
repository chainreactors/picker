---
title: 【安全圈】苹果、特斯拉均受影响，新型漏洞迫使GPU无限循环，直至系统崩溃
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065447&idx=1&sn=af6b1e3779b7cc108da77693a2bd8568&chksm=f36e62e7c419ebf1cd9ee388d190e5348b4f3438c42df530721e3ada741af2723a0779c39ec6&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-25
fetch_date: 2025-10-06T18:52:07.110207
---

# 【安全圈】苹果、特斯拉均受影响，新型漏洞迫使GPU无限循环，直至系统崩溃

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljChO1pW8DeTrvJ4hzjZicC1cFRx9HMhuvaWXChucZeLqx5wk5catwNibsqiaCrqeDYlD6hwseXHOuLQ/0?wx_fmt=jpeg)

# 【安全圈】苹果、特斯拉均受影响，新型漏洞迫使GPU无限循环，直至系统崩溃

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljChO1pW8DeTrvJ4hzjZicC1pxUPXU4tfXic5pDzmTAp4rCVPPHCE6Gyassb2tC7b7wZvnJkyHs70rw/640?wx_fmt=jpeg&from=appmsg)

近日，Imperva 研究人员发现了一个名为 ShadyShader 的漏洞。该漏洞允许攻击者反复冻结苹果设备的 GPU，最终可能导致系统崩溃。

研究人员认为，主要问题在于现代 GPU 如何检测和停止无限循环，即如果不终止就会无休止运行的指令序列。虽然 GPU 能够熟练地检测并阻止明显的循环，但研究人员展示了一种方法，即制作一个嵌套循环，并在未被发现的情况下执行。

Imperva 公司的安全研究员罗恩-马萨斯（Ron Masas）尝试制作了一个简单的着色器代码，该代码只迭代大量循环，迫使 GPU 执行大量计算。这种代码可以添加到网站上，使用户系统崩溃。它还可以通过信息、电子邮件和带有恶意链接的 QR 码扫描器发送。如果用户点击链接，浏览器就会加载带有恶意着色器的 WebGL 内容，设备就会进入数字迷宫。这些操作往往都无需用户许可，因为在执行许多常见任务时，GPU 访问都是悄无声息地进行的。

马萨斯表示，驱动程序无法识别着色器不必要地垄断了资源。这使 GPU 不堪重负，无法再管理其他任务，最终导致系统崩溃。

苹果的显示管理服务（macOS 上的 WindowServer 或 iOS 上的 SpringBoard）会等待 GPU 完成任务。当受到 ShadyShader 的攻击时，这个负责管理屏幕的服务就无法获得任何更新，整个系统就会变得很迟钝。

苹果设备内置的计时器可以监控关键进程，确保它们不会耗时过长。120 秒后，该计时器会触发内核恐慌，迫使系统崩溃并重启。在 iPhone 和 iPad 上，计时器的反应速度更快，只需 30 秒。

研究人员指出：在我们的测试中，Macbook 会在 1-2 分钟内完全重启，而 iOS 设备则会在显示锁屏之前的 3-6 分钟内保持无响应状态，在大多数情况下都不会完全重启。

## 尽管打了补丁，问题依然存在

苹果公司早在 2023 年就更新了 GPU 驱动程序来解决这个漏洞，因此运行最新 iOS 和 macOS 版本的用户应该没有问题。但根本问题似乎具有更广泛的影响。

Imperva 警告说：在我们看来，GPU 资源耗尽问题依然存在，并可能在未来的攻击中被利用。我们在其他设备上也观察到了有趣的行为，尤其是在谷歌 Pixel 手机上。

一些机会主义测试显示，Pixel 手机上的浏览器应用会变得无法使用，直到用户重启手机，尽管设备并未崩溃。

甚至在特斯拉汽车上，Imperva 的研究人员也观察到主屏幕在遭遇 ShadyShader 漏洞攻击后暂时无法响应的情况，不过其关键的驾驶功能没有受到影响。

研究人员表示，虽然目前没有测试该漏洞可能带来的全部影响，但所有带有 GPU 和浏览器的系统都可能受到类似的影响。

如果用户发现自己的设备因这种攻击而陷入崩溃循环，可以尝试在打开浏览器之前在设置中禁用 JavaScript，然后关闭有问题的标签页。

参考来源：Flaw crashes Apple devices with a single click, Tesla also vulnerable | Cybernews

***END***

阅读推荐

[【安全圈】水军狂喜？Claude AI现在可以控制PC并自己移动鼠标完成任务操作](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=1&sn=b934e5d1eacd20db87c29744a60e9747&chksm=f36e62d8c419ebcee92754914fb085938a5fd00ef2e9c04cb09422f2cfe22a02973d1a40af0e&scene=21#wechat_redirect)

[【安全圈】高通64款芯片存在0Day漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=2&sn=c5c869e24ab938b185e97679ede50f75&chksm=f36e62d8c419ebced3dfe7c7c112dd6fa9c2cce62710befa6d8ed1a4619a93818b4963036f5a&scene=21#wechat_redirect)

[【安全圈】K8s曝9.8分漏洞，黑客可获得Root访问权限](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=3&sn=8dd024db6fb200b80ea9bd4b0ab86a5a&chksm=f36e62d8c419ebceefe101ff0bc1b587b6e99447dcd96e41f562f8cf9aa4303b7eec61418712&scene=21#wechat_redirect)

[【安全圈】三星设备曝出高危零日漏洞，已在野外被利用](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065432&idx=4&sn=e821667ba35126b55834a52a98cbf559&chksm=f36e62d8c419ebcee6861d148234c4240e97f32ff3ae4d2ecce99feef2c26006edc5b720092f&scene=21#wechat_redirect)

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