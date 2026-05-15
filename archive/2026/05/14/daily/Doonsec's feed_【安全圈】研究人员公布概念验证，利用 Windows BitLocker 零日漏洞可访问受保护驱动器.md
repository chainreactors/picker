---
title: 【安全圈】研究人员公布概念验证，利用 Windows BitLocker 零日漏洞可访问受保护驱动器
url: https://mp.weixin.qq.com/s/OnXI-rDV3sgZPW2qgLvLIw
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:48:56.803030
---

# 【安全圈】研究人员公布概念验证，利用 Windows BitLocker 零日漏洞可访问受保护驱动器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyE9uk5fs8gu9yZcIB1IleqHRMZMn71773icbRC7OUFY7nrA8MgkMWNdqF3DGvynwRkHfZVfQiaPu5jcZxye0wGhF4gfCt1gRWPBc/0?wx_fmt=jpeg)

# 【安全圈】研究人员公布概念验证，利用 Windows BitLocker 零日漏洞可访问受保护驱动器

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

一名网络安全研究人员公布了针对两个未修复的微软 Windows 漏洞的概念验证（PoC）利用程序，**这两个漏洞分别名为 YellowKey 和 GreenPlasma，其中 YellowKey 可绕过 BitLocker 加密，GreenPlasma 是一个权限提升漏洞。**

这位名为 Chaotic Eclipse 或 Nightmare Eclipse 的研究人员称，BitLocker 绕过漏洞就像一个后门，因为存在漏洞的组件仅在 Windows 恢复环境（WinRE）中出现，该环境用于修复 Windows 系统的启动相关问题。

此次公布的漏洞利用紧随该研究人员之前披露的 BlueHammer（CVE - 2026 - 33825）和 RedSun（无编号）本地权限提升（LPE）零日漏洞，这两个漏洞在公开披露后不久便开始在实际中被利用。

与之前的情况一样，该研究人员表示，公开披露 YellowKey 和 GreenPlasma 漏洞以及如何利用它们，是因为对微软处理漏洞报告的方式不满。

Chaotic Eclipse（在 GitHub 上名为 Nightmare - Eclipse）表示，他们将继续泄露针对未记录的 Windows 漏洞的利用程序，甚至承诺在下一个 “补丁星期二” 给大家 “一个大惊喜”。

### YellowKey：绕过 BitLocker 加密

该研究人员称，YellowKey 可绕过 BitLocker 加密，影响 Windows 11 以及 Windows Server 2022/2025 系统。利用方法是在 USB 驱动器或 EFI 分区上放置特制的 “FsTx” 文件，重启进入 WinRE，然后按住 CTRL 键触发一个命令行窗口。

此外，无需外部存储设备，将文件复制到目标驱动器的 EFI 分区，也能实现对 BitLocker 的绕过。

据 Chaotic/Nightmare Eclipse 称，触发的命令行窗口可无限制访问受 BitLocker 保护的存储卷。

独立安全研究员凯文・博蒙特（Kevin Beaumont）证实 YellowKey 漏洞利用有效，并认同 BitLocker 存在后门。他建议使用 BitLocker PIN 码和 BIOS 密码作为缓解措施。

Chaotic Eclipse 在今日的更新中表示，“公众仍不清楚真正的根本原因”，并且即使在启用可信平台模块（TPM）和 PIN 码的环境中，该漏洞依然可被利用。不过，针对此版本的漏洞利用程序尚未发布。

该研究人员称：“我认为即使对微软安全响应中心（MSRC）来说，要找到问题的真正根本原因也需要一些时间。我一直不明白为什么这个漏洞隐藏得如此之深。”

“不，TPM + PIN 码并无帮助，无论如何该漏洞都可被利用。我问过自己，它在 TPM + PIN 码环境下还能起作用吗？答案是肯定的，我只是不发布这个概念验证，我觉得目前已公开的内容已经够糟糕了。”

萨罗斯实验室（Tharros Labs）的首席漏洞分析师威尔・多尔曼（Will Dormann）也证实，使用 USB 驱动器上的 FsTx 文件，YellowKey 漏洞利用确实有效，但使用 EFI 分区无法复现该漏洞。

他向 BleepingComputer 解释说：“YellowKey 结合 Windows 恢复镜像，利用了 NTFS 事务。PIN 码提示出现在进入 Windows 恢复环境之前。”

多尔曼详细说明了漏洞利用过程，为了启动 Windows 恢复环境，“Windows 会在连接的驱动器上查找 \System Volume Information\FsTx 目录，并会重放任何 NTFS 日志。”

默认情况下，仅使用 TPM 的 BitLocker 配置会自动解锁加密驱动器，无需用户干预。如果系统为了方便能透明解密磁盘，那么攻击者最终可能找到滥用该过程的方法，这并不意外。

多尔曼说：“YellowKey 就是利用此类弱点的一个例子。” 他解释说，由于该漏洞利用了启动时的自动解锁功能，当前的 YellowKey 漏洞利用在 TPM + PIN 码环境下不起作用。

值得注意的是，使用受 BitLocker 保护的驱动器测试 YellowKey，必须在 TPM 存储加密密钥的原始设备上进行。

因此，Chaotic Eclypse 目前的 YellowKey 漏洞利用对被盗驱动器无效，但可在无需凭证的情况下访问仅用 TPM 保护的 BitLocker 磁盘。

### GreenPlasma 漏洞利用

GreenPlasma 是一个权限提升安全漏洞，可被利用来获取具有 SYSTEM 权限的命令行窗口。Chaotic Eclipse 将其描述为 “Windows CTFMON 任意节创建权限提升漏洞”。

普通用户可在 SYSTEM 可写的目录对象内创建任意内存节对象，这可能导致对信任这些位置的特权服务或驱动程序进行操纵。

不过，泄露的概念验证并不完整，缺少实现完整 SYSTEM 权限命令行窗口所需的组件。尽管如此，Chaotic Eclipse 表示：“如果你足够聪明，就能将其转化为完全的权限提升。”

这位不满的研究人员补充说，新创建的节可被影响，从而操纵数据以及包括内核模式驱动在内的各种服务，使其信任标准用户无法访问的特定路径。

虽然尚不清楚是什么确切原因导致 Chaotic Eclipse 大量泄露漏洞利用程序，但该研究人员暗示在下个月的 “补丁星期二” 会给微软 “一个大惊喜”。

此外，他们还称 “微软悄悄修复了 RedSun 漏洞”，并批评微软这种悄无声息的做法，以及未像 BlueHammer 漏洞那样为该漏洞分配编号。

BleepingComputer 已联系微软，就 Chaotic Eclipse 最新泄露漏洞利用程序一事征求评论，微软发言人表示，公司致力于调查报告的安全问题，“并尽快更新受影响设备，以保护客户。”

微软发言人告诉 BleepingComputer：“我们也支持协调漏洞披露，这是一种被广泛采用的行业做法，有助于确保在公开披露前，对问题进行仔细调查和处理，既保护客户，也支持安全研究社区。”

***END***

阅读推荐

[【安全圈】苹果修复 macOS 和 iOS 系统数十个漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076415&idx=1&sn=28c320ab902f356686e31c217bcd9b65&scene=21#wechat_redirect)

[【安全圈】Windows 11遭新型BitUnlocker降级攻击：5分钟内可解密加密磁盘](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076415&idx=2&sn=8bef02564b19d5593d920a9e226b38ed&scene=21#wechat_redirect)

[【安全圈】Exim 新 BDAT 漏洞致 GnuTLS 构建面临代码执行风险](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076415&idx=3&sn=4a801e88018faba5f0fdb72a80373270&scene=21#wechat_redirect)

[【安全圈】警惕！你的蓝牙可能正被监听 改一个设置就能有效防护](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076374&idx=1&sn=80e79d8ca786f2b8a4f2a23fe7d5bad4&scene=21#wechat_redirect)

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