---
title: 零成本！普通手机跑最强 Gemma 4 模型 (原生多模态)，安卓+iPhone 部署实测体验！
url: https://mp.weixin.qq.com/s/L5gaAuGJ2yaYbeGDB96dBw
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:25:55.888646
---

# 零成本！普通手机跑最强 Gemma 4 模型 (原生多模态)，安卓+iPhone 部署实测体验！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVu6HibZwr9tjicY9mIPgtWMTG8TexS3msuZQvFtaXHEpXoLV8y2mOMX5et4aUWBnCJxvFee6PzRawu6tSFGAyXRLIVU8fCO4ChbQ/0?wx_fmt=jpeg)

# 零成本！普通手机跑最强 Gemma 4 模型 (原生多模态)，安卓+iPhone 部署实测体验！

原创

SzHackingClub
SzHackingClub

灰帽安全

![]()

在小说阅读器中沉浸阅读

如果我告诉你，一台普通手机就能跑通谷歌刚刚发布的最强Gemma 4模型，你信吗？更惊喜的是，它支持原生多模态，能看图、能对话、能写代码，还能完全离线使用，全程不用花一分钱。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVtd94fxIiaI1DpNMSoRqribicr3qicAnWTicWibQxwHm6aqZYDWbkO9SJRQGTeicazEECF55icAIOw3CZVDSQ0Z5p5Guwx97aFhibJgUGZY/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVs57Kxsic5XvcqDuMJ31Izu1QAUD85txxV9cT13UxYcgNqzZ42CF8NmWvaS9l2p4SK8NtEsLTYq6t4jfgZ3pRYgnEBMnQ5DykU8/640?wx_fmt=webp&from=appmsg)

最近很多朋友问我，手机能不能跑通最新的大模型，毕竟不是人人都有高性能电脑。今天，我就带大家从零开始，一步步在安卓和iPhone手机上跑通Gemma 4模型，每一步都有详细操作，新手也能轻松跟上，所有需要的资料，我都会放在文末和博客置顶，大家直接获取即可。

先跟大家简单科普下，Gemma 4是谷歌DeepMind最新发布的开源旗舰模型，也是目前谷歌最强的开放模型系列，采用Apache 2.0许可证开源，支持免费商用和二次开发，共分为4个版本，其中E2B、E4B两个版本专门针对手机、嵌入式设备优化，内存占用最低可压至1.5GB以下，这也是普通手机能跑通它的关键原因。话不多说，直接上实操！

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVs1EmhblGXeVxicM0Cj2oiaxhs67jELaFE00UkmP13FqYGUWx342iaQB9dXcvmMlibv6o83DDwU895k2Fk0kQ4QBgY3wCUYKwj2yQ8/640?wx_fmt=webp&from=appmsg)

这期教程，我将带你从零开始，分别在 Android 和 iPhone 手机上跑通最新的 Gemma 4 模型。在开始动手之前，请确保你已经在本页下方找到了我们所需的全部下载资料和链接。

第一部分：Android 安卓端部署

我们先拿安卓手机来做测试。由于我的测试机配置比较旧，正好可以验证一下低配手机的运行效果。

1. 下载与安装环境

在下方资料区获取安装包，你可以选择直接从谷歌应用商店（Google Play）下载，或者直接下载 APK 安装包。

（1）、Google应用商店下载：

```
https://play.google.com/store/apps/details?id=com.ishanvohra2.localai
```

（2）、下载安卓APK安装包：

```
https://pan.tuio.cc/s/Y2dul
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVsm2zwQIzQSXIUN0ONMMmSFpxzbwapLlAG2Vg6NUiapNdYM83v2ibqjLYpFBibUlFQa2P9OBcdGk0UTnLqx4doUIxefUDBiaAWg9q0/640?wx_fmt=webp&from=appmsg)

打开应用并完成安装。首次进入点击 Get Started，并允许发送通知。

2. 性能模式与模型下载

进入应用后，我们需要进行基础设置并下载对应的 AI 模型：

选择运行模式： 顶部可以选择 AI 模型的运行模式（Fast 快速、平衡、高性能、自定义）。

进入模型库： 点击左上方三个横杠菜单，进入 Model Hub。

下载 Gemma 4： 向下滑动找到 Gemma 4 ECB 量化版模型。

注：系统会根据手机配置推荐合适的版本。由于我的手机配置不高，它推荐的是 1.2GB 大小的 Q2\_K\_S\_L 量化版。如果你的安卓机配置较高，可以选择最高 2.3GB 的版本以获得更好的体验。

勾选推荐版本，拉到底部点击 Download，耐心等待一分钟左右即可下载完成。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVvibaRdMS4dPx0JCkvd1of4bn3ya3SnjsgDqM4x0yyLWGAZeictsYmhiaVNEKTTfNXZEpg9bEsu8icNq6cDbpu2IibibeF0SaoEgjhick/640?wx_fmt=webp&from=appmsg)

3. 载入与测试模型

返回首页，进入 Fast 选项卡并拉到底部，打开 自定义模式。

创建模型： 名称可以随便填。

选择模型： 选中我们刚刚下载好的 Gemma 4 1.2G 模型。

参数设置： \* 上下文长度：根据手机硬件配置自定义（配置低切勿拉太高）。

最高 Token 输出量：设置为 512。

点击保存，自定义模型就配置完成了！

实测表现： 我让它在本地完全离线的状态下帮我编写了一个贪吃蛇小游戏，生成速度非常快，日常对话也完全没有问题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVsqEQzQg791BuJ7l1YwKHwdXPjjyNu2SDibmjTaMw12aiaEqYTlKvzRicN9Lt0W6vz2XJVUwuxvgsptJ9AM4nhdXKAibk57oibRp0MQ/640?wx_fmt=webp&from=appmsg)

第二部分：iOS 苹果端部署

看完安卓，我们再来看看 iPhone 上的表现。

1. 下载 Locally AI

```
https://apps.apple.com/us/app/locally-ai-local-ai-chat/id6741426692
```

通过下方链接前往 App Store 下载名为 Locally AI 的应用程序。这是一款完全免费、主打隐私与安全、支持加载本地离线模型的强大工具。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVvf0uPp3pLKz9Ba8x2SfvIngGqmS9aJnZSgeCHZzInibCLAZAuJFHYWY3O7DVu0LJ5D27FGSoRqYw8zLzBTrLa1S5aUCQb3jMJQ/640?wx_fmt=webp&from=appmsg)

2. 下载 iOS 版 Gemma 4

打开应用，跳过欢迎页的默认模型推荐。

点击上方的 选择模型，在列表中找到支持深入思考和多模态的最新的 Gemma 4。点击下载（文件大小约为 3.61GB，版本为 E2B 量化版）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVuk0o51WoMcC0gJQghZk84Vwr6trd6Tx1K2B34WmPHiarL5vblxJzG5Ze2sa6RGEnXxxgqZRwX5J294e34Jjiazib5W2robVTUBVQ/640?wx_fmt=webp&from=appmsg)

极客硬核测试：Gemma 4 到底有多强？

模型下载好后，我针对它的多模态、逻辑推理和代码能力进行了深度测试。

测试一：多模态视觉识别（拍照识物）

我随手在桌面上扔了一些杂物，打开 深入思考模式 拍照发给它，看看它能识别出什么。

我的提问： 你看到了什么？桌面上堆有哪些东西？ Gemma 4 回答： > \*  一部深色的智能手机

 一个带花卉图案的偏紫色/粉色手机保护壳

 一个亮蓝绿色的小瓶（护肤品/精油）

 一个带标签的大罐子（益生菌）

 一个黑色小电子配件（声卡录音设备）

![](https://mmbiz.qpic.cn/mmbiz_jpg/iaK3IA1hoFVtmG9fDf9bppdRDGAZA4BFaVOkPCjdJRXcYcEgxV2icc48OnAia5tNcCEIriadicTicCFL1tdljibTEOcLAvpEt5icRrQMr0msNcqpictI/640?wx_fmt=webp&from=appmsg)

翻车环节： 唯独桌上的西瓜子它没认出来。我再次特写拍照问它“黑色点点是什么，总共有多少个？” 它推测是干燥的种子（算答对），但数量数成了 9 个（实际是 16 个）。 吐槽：为了公平起见，我也问了 ChatGPT，虽然 ChatGPT 认出了西瓜子，但也数错了（数成了 17 个）。看来 AI 数数依然是个老大难问题！

测试二：逻辑推理（蒙提霍尔问题）

题目： 三扇门（一车两羊），你选定一扇后，主持人打开一扇羊门。问：换门是否有利？ Gemma 4 回答： 这是一个经典的蒙提霍尔问题变种。答案是换门更有利。坚持原门只有 1/3 的概率，而换门可以抓住主持人排除错误选项带来的机会，将概率提升到 2/3。 结论： 逻辑非常清晰，完全正确！

测试三：前端代码编程

要求： 编写一个 3D 鱼缸场景，水、水草和鱼要有真实感。 结果： 它不仅提供了 HTML，还一并写好了 CSS 样式和 JS 代码。将代码复制到电脑上运行后，视觉效果非常逼真。作为一个手机端本地运行的小模型，能达到这种渲染水准令人惊艳。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVvh9PWKwyovVuZXCt9I2iaZaHv4gdyt2M2eiaKCGwPqdYfyMwee7cVVg7Yv7BTeWZCR9MYVNeRdjyJClUyZD13NImld5WZB9WvmM/640?wx_fmt=webp&from=appmsg)

测试四：医疗物品识别安全机制

我拍了一盒“瑞巴派特片”给它。它准确识别出了药片名称，但立刻触发了安全机制，表示“由于涉及身体和健康产品，无法提供医疗建议，请务必咨询医生”。表现得非常严谨。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaK3IA1hoFVs4oUTIoW945uG2xFmboOvKyYVGiaUiav8EQcH6egVrYBUyJGHxwDP4lLZW2XB7b6aWUndsb7ia1f5F72eQuyXuOs4bwMQVQVkqxw/640?wx_fmt=webp&from=appmsg)

终极考验：断网飞行模式测试

为了验证它的纯离线真伪，我断开了所有网络并开启了飞行模式。

写长篇小说： 让它写一篇 5000 字左右的恐怖小说。它在完全离线的状态下，使用繁体字分章输出，仅用时 1 分钟左右就完成了创作。

微距视觉推理： 在离线状态下发给它一张包含大象和蚂蚁的画。它准确识别出了大象头部，并声明“由于细节非常小，对蚂蚁的识别是基于微小尺寸的推测”。离线多模态能力确实靠谱。

Gemma 4 模型在手机端的本地离线表现远远超出了我的预期，无论是生成速度、逻辑推理还是多模态视觉，都达到了相当高的可用级别。

![](https://mmbiz.qpic.cn/mmbiz_png/1bQDlhHMib4A7kJeibPd8yBbdrqxqicvEIVSJuv3HrCDNe3jgCv4KJiapeE643lNzxj85iaeMkYx3sF6suibt0lMvxtQ/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1bQDlhHMib4Du5uDacz69OWbdwAUlNfCrXUOicJH7wDmzV9CsHbsXjZ5lEDQcHMK6M33ZM0aApjXjcsBNjRqYx1g/0?wx_fmt=png)

灰帽安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1bQDlhHMib4Du5uDacz69OWbdwAUlNfCrXUOicJH7wDmzV9CsHbsXjZ5lEDQcHMK6M33ZM0aApjXjcsBNjRqYx1g/0?wx_fmt=png)

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