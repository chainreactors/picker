---
title: 杀软EDR都没检出？一文秒懂“银狐”四大绕过手法
url: https://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650176323&idx=1&sn=6c01c5d7ed068056c3664cbbd30903e5&chksm=f44880ffc33f09e9fa3a737c4947b046ee65b00040fc2765c6e96ebc3e9a6f7baa62c9b015d8&scene=58&subscene=0#rd
source: 微步在线
date: 2023-03-30
fetch_date: 2025-10-04T11:08:09.538639
---

# 杀软EDR都没检出？一文秒懂“银狐”四大绕过手法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hSMm4eMj41exEhBALCaaVQra7lHasGVrlGx0qsZw1lzaxBdx6YmibVhwcogOT7WnuGdia9dTbLhrmOg/0?wx_fmt=jpeg)

# 杀软EDR都没检出？一文秒懂“银狐”四大绕过手法

原创

ThreatBook

微步在线

![](https://mmbiz.qpic.cn/mmbiz_gif/Yv6ic9zgr5hRYwmkFFVSsK0fQGJBGqwl6iaBoFgqTpPricWCuX7uIb4Rj7eibLo3ibOiaOtqo7vXEnibKhxuInrceOoibg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

3月27日，微步发布了对[攻击金融、证券、教育等行业的黑产团伙 “银狐”的研究报告](http://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650176252&idx=1&sn=aa08ba2f668e5e393e91f52f0cc125be&chksm=f4488140c33f0856464e2ff3877309c851bdfb39f38f9db72aed248d04c25fad03e0f74b8d3e&scene=21#wechat_redirect)。“银狐”利用伪造工具网站、微信等即时通讯工具发送木马文件，诱骗员工点击，由此入侵企业办公网。

微步终端安全管理平台OneSEC在更早时候就发现了“银狐”的攻击行为，经微步安全实验室进一步分析，发现其母体样本存在至少4种利用方式，可以有效对抗或绕过现有终端安全产品（杀毒和EDR）。本文将详细分析、总结这些绕过手法各自的特点，以帮助大家有效应对办公网的新威胁。（也可直接查看【手法总结】，快速了解每种攻击手法的特点）

#**“银狐”四大绕过手法揭秘**#

微步总结出“银狐”团伙攻击技术过程中的四大绕过手法：浑水摸鱼、李代桃僵、瞒天过海、包藏祸心。

**01**

**浑水摸鱼****：模拟鼠标点击，构造合法执行链路加载恶意代码**

伪装成“xx聊天记录”的母体样本被用户双击后，会释放三个文件：

* vbn.exe是一个模拟鼠标点击程序，非恶意；
* adta.exe是一款带有合法签名的某股票软件；
* libcef.dll是一个恶意dll文件；

目前部分终端安全产品在行为检测上的信任逻辑依靠有效的文件签名，而在这一攻击手法中，“银狐”正是利用了白程序（有合法签名的某股票软件）特性，伪装成一个合法的进程链路。具体执行如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSMm4eMj41exEhBALCaaVQrnzyaP5ZIhUQkHFygG3DRHV5X1eXj80rl7X8tyFeepq8XnK3lJmAuDw/640?wx_fmt=png)

1. 名为“xx聊天记录.exe”的母体样本首先执行vbn.exe；
2. vbn.exe模拟鼠标点击动作，让Explorer程序启动adta.exe；
3. adta.exe程序加载有恶意代码的libcef.dll文件；
4. adta.exe将恶意代码注入svchost执行。

**手法总结** …

“银狐” 成功构造了一整条“白利用链路”，从而可以轻松绕过杀毒主防和EDR的检测。而且利用模拟鼠标点击，让Explorer执行的方式更不容易追溯到原始恶意进程。

**02**

**李代桃僵****：****利用微软官方程序启动程序加载恶意代码**

与手法1有些类似，伪装的母体样本同样会释放三个文件：

* helpPane.exe是微软官方提供的帮助程序；
* adta.exe是一款带有合法签名的某股票软件；
* libcef.dll是一个恶意dll文件；

与手法1不同的是，利用微软官方程序替代了模拟鼠标点击程序。母体样本在释放文件后，会调用COM组件中的冷僻接口，通过操作系统自主启动HelpPane.exe程序，然后再执行类似手法一的进程，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSMm4eMj41exEhBALCaaVQrS1cBCWClolAy06L8dJh5EdZIz43TSqjSzibrIMCTHcoGUxNw1EsRVibQ/640?wx_fmt=png)

**手法总结** …

与手法1相比，手法2通过COM组件替代模拟鼠标点击，利用操作系统来启动HelpPane.exe程序，构造了一条“合法”链路，相较于Explorer这种常见进程更具迷惑性。而且利用com组件的方式更不容易追溯到原始恶意进程。

**03**

**瞒天过海：****图片暗藏恶意代码实现无文件攻击**

这是无文件攻击的一种常见实现，母体程序是一个Go语言编译的程序，诱导用户点击之后，恶意程序会首先访问C&C，并下载一张图片，然后将图片加载到内存中。用户看到的就是一张图片（不影响图片的正常显示），而实际上，攻击者使用一些算法将数据嵌入到了图像中。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSMm4eMj41exEhBALCaaVQr0ibHlrFd5Fkdrh85MR4cr7ibJunJwwWPXqnbK4PkQhvqmlROSNS8mDhQ/640?wx_fmt=png)

反连C&C后下载的图片，恶意代码就隐藏其中

之后Go语言程序会在内存中将此图片解密，释放出恶意代码，并创建计划任务实现开机启动。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSMm4eMj41exEhBALCaaVQrF90I0Cic3cLwYKuTxtXAXXPFU5FeGNOSvJ4w1K6ibHTkmAZ0Q5JkBbkg/640?wx_fmt=png)

被微步抓到的内存中解密恶意代码过程图

**手法总结** …

在整个过程中，Go语言程序并不存在恶意代码，所以杀软无检出；恶意代码实际从下载的图片中动态获取，整个过程无任何恶意文件落盘，所有操作均在内存中处理完成，成功绕过了绝大多数的杀毒引擎，并通过计划任务达到持久稳定运行的目的。

**04**

**包藏祸心****：加密文件内存中释放恶意代码**

母体程序利用签名伪造技术将自身伪装成正常程序，尽管这个程序的签名是无效的，但因为并不包含恶意代码或恶意特征，所以大多数杀软都不会告警。运行这个程序会释放三个文件：

* AvSHpPsh.exe是一个无恶意代码/特征的执行程序；
* Antikk.dll是一个无恶意代码/特征的dll文件；
* xm.xml是一个加密文件。

母体文件会首先执行AvSHpPsh.exe程序，并加载Antikk.dll文件，然后在内存中解密xm.xml文件，执行payload：

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSMm4eMj41exEhBALCaaVQrKyx4jjj7Zd8u2mRYKGDdSM19Y6AceCpRMp8tCS5W1dmkELZnEVozuA/640?wx_fmt=png)

未解密的内存代码

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSMm4eMj41exEhBALCaaVQrlkzFJSg5pOH2icniawDQia30zicUNFrlicme7rhicL1WXBQFBHDDPWcZZeUw/640?wx_fmt=png)

解密后的内存代码

**手法总结** …

在这一攻击手法中，尽管恶意代码在本地，但以加密形式存储，不存在任何可疑特征，杀软几乎无法检出。AvSHpPsh.exe程序在内存中加载并解密运行恶意代码，同样可以轻松绕过杀软与EDR。

可以看到，“银狐”团伙使用的四大绕过手法均各有高明之处，那么如何在终端上破解？

# **EDR如何应对“银狐”攻击**#

# **让终端安全止于终端**

在3月27日的分析报告中，微步公布了“银狐”攻击相关的IOC与TTPs，本文则从终端角度切入，借助微步终端安全平台OneSEC，为大家展现“银狐”的应对之法。

从防范角度，可以将“银狐”的4种攻击手法分为两类：

**手法一和手法二使用的规避手法都是通过伪装白利用等方式执行**，以此绕过了杀软和大多数EDR的行为检测。**OneSEC****使用单点+事件的两阶段检测方式****，不仅检测行为，还将行为串联，从事件角度整体检测**，虽然表面看起来是“合法”链路，但综合其特殊的执行链路和注入方式，就会被OneSEC识别检出，检出图如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSMm4eMj41exEhBALCaaVQrAE5zePiawHfxWCV8mBSwkSFpTnwfhsKUBjyKna3YOcrLbdGQZXCF99Q/640?wx_fmt=png)

银狐攻击团伙行为检出图

**手法三和手法四，从技术角度看，利用了图片暗藏恶意代码、加密恶意文件**等方式，但都会经历内存解密、反射加载两个阶段。对于这两种攻击手法，**OneSEC 利用 IOA 引擎和内存扫描的组合拳能实现有效检出**：

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSMm4eMj41exEhBALCaaVQrP3JqhKRQwe1QO1NerLnnEzxxW4nCLG8MbfpicTjM1eDSA2FcZNGNJVQ/640?wx_fmt=png)

实际上，除了OneSEC之外，微步旗下的威胁感知平台 TDP 、威胁情报管理平台 TIP 、威胁情报云 API 、互联网安全接入服务 OneDNS 、主机威胁检测与响应平台 OneEDR 等均已支持对此次攻击事件和团伙的检测。

· END ·

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRYwmkFFVSsK0fQGJBGqwl6gYoAG5F1cXgRMNjT0PLZibxZyLvJ2PdcOiczbIv7Vl7xQVgzibia4JiafzQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

微步在线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

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