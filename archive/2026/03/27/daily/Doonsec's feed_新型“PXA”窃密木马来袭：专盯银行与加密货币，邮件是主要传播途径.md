---
title: 新型“PXA”窃密木马来袭：专盯银行与加密货币，邮件是主要传播途径
url: https://mp.weixin.qq.com/s/4y79248cKezOl8w9_EmksQ
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:15:28.449983
---

# 新型“PXA”窃密木马来袭：专盯银行与加密货币，邮件是主要传播途径

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K28iawDdGaa0NcX7Qib8QoQ4rWicRx574NZMGYJyOH6ibevd1bHb9yCFK6UmgwQtwZlPzrfLuWkgNib0k7MHZjD830kLlwiagKnvEjn8/0?wx_fmt=jpeg)

# 新型“PXA”窃密木马来袭：专盯银行与加密货币，邮件是主要传播途径

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

近期，一种名为“PXA”的新型恶意软件正悄然活跃，尤其针对金融行业用户和加密货币持有者发起攻击。网络安全公司CyberProof监测发现，2026年第一季度，与此木马相关的攻击事件激增了约10%。

为什么这种病毒突然变得如此猖獗？专家分析，这与此前几款知名信息窃取软件（如RedLine、Lumma）在2025年被警方捣毁有关。犯罪分子失去了趁手的工具，便开始迅速推广“PXA”木马来填补空白。

对于普通用户来说，感染过程往往毫无察觉。攻击者会发送大量看似正常的钓鱼邮件，它们伪装成报税单、法律文件，甚至Adobe Photoshop的安装包，极具欺骗性。

其中一种常见套路是附带一个名为“Pumaproject.zip”的压缩包。一旦好奇的用户解压并打开了里面的文件，电脑就会在不知不觉中被“埋下”病毒。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0aWs4xOicuOicRbzibviaVIAtS7kE3UzxYxjv6W26cfkQ5RlgiaYnSBjQL1lmdIRY9lCJh5Oamu8PO7iamkHKjYHyPOT4vXYHnHSanw/640?wx_fmt=png&from=appmsg)

这款木马非常狡猾，为了不被杀毒软件发现，它会使用多层手段来隐藏自己：

* “隐身”文件夹：它在电脑中创建一个名为“Dots”的文件夹（在系统中通常以“.”开头，具有隐藏属性），并用一个特定的密码“shodan2201”来保护核心文件。
* 借壳“换脸”：为了让用户放松警惕，它会将恶意文件的名字伪装成常见的系统程序名，如svchost.exe（这是Windows系统的一个正常进程），试图混入正常的系统文件中。
* 键盘记录：更可怕的是，它会伪装成我们常用的办公软件（如WINWORD.EXE）。一旦得手，它就会悄悄启动“键盘记录”功能，你在电脑上输入的每一个字，包括账号和密码，都会被它暗中记录下来。

一旦感染成功，PXA木马就会开始“搜刮”你的数字资产，主要包括：

* 浏览器密码：你在Chrome、Edge等浏览器中保存过的所有网站登录密码。
* 加密货币钱包：如果你的电脑里存放着加密货币钱包的私钥或文件，都会被它盗走。
* 金融网站数据：针对特定的银行或金融平台，窃取相关敏感信息。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1xYQwhiblPveeKlAbibNCamaUvSuV0WBgMdKibYOr8EIIYc2DRFImm2G5p0wQiaTsH2KOXfd27yqaiclx7bqiaj2kXGSAJZBQ1Btj5o/640?wx_fmt=png&from=appmsg)

为了便于管理偷来的数据，黑客还会为每台被感染的电脑分配一个名为“Verymuchxbot”的身份编号。最终，所有窃取到的信息都会通过Telegram（一款即时通讯软件）的频道悄悄发送给黑客。

最麻烦的是，木马还会在电脑的注册表中留下“后门”，确保每次电脑重启时，它都能自动再次运行，很难彻底清除。

面对这种威胁，普通用户也不必过度恐慌，只需要在日常使用中多留个心眼：

* 警惕邮件附件：对于来历不明的邮件，尤其是带有 .zip 或 .rar 压缩包附件的，即使内容看起来很紧急（比如“逾期账单”），也要先通过其他方式核实发件人身份，切勿随意打开。
* 注意可疑连接：如果发现电脑网络流量异常，或者看到浏览器试图连接一些以 .xyz 或 .shop 结尾的奇怪网站，应提高警惕。
* 关注异常文件：如果在电脑中突然看到以 .vbs 或 .js 结尾的陌生文件，不要双击运行。

资讯来源：综合自网络安全公司CyberProof研究报告及公开威胁情报。

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

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