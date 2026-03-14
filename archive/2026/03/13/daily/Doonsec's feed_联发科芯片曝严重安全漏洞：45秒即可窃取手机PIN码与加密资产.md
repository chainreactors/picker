---
title: 联发科芯片曝严重安全漏洞：45秒即可窃取手机PIN码与加密资产
url: https://mp.weixin.qq.com/s/LiiV4KLNxekXgnht-FPrWg
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:08:47.892772
---

# 联发科芯片曝严重安全漏洞：45秒即可窃取手机PIN码与加密资产

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2ct8Q1JibOsrEbKniaLUR4Kh5GG8c19c1qrEAVtEuE3JD3VRqLNYtrPM2ynBwR5emVCrmdyeiaNK0LUoC7Xm1vwTZicPGUVicLHdcY/0?wx_fmt=jpeg)

# 联发科芯片曝严重安全漏洞：45秒即可窃取手机PIN码与加密资产

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

近日，一项针对联发科芯片的严重安全漏洞引发关注。研究团队发现，攻击者利用该漏洞，可在约45秒内物理接触手机的情况下，窃取设备PIN码、解密存储数据，并盗取加密货币钱包的助记词，直接威胁到约25%安卓用户的资产安全。

**硬件级漏洞：无法通过软件修复**

该漏洞由Ledger的安全研究团队Donjon发现，存在于联发科Dimensity 7300（又名MT6878）芯片的启动ROM（Boot ROM）中。这是手机开机时执行的第一段代码，运行在最高的硬件权限级别（EL3），远早于安卓系统的加载。

由于Boot ROM被永久固化在处理器硅片上，这一硬件层面的核心缺陷无法通过任何软件更新来彻底消除。

**攻击方式：电磁故障注入**

研究人员利用电磁故障注入（EMFI）技术成功利用了该漏洞。这种方法通过在芯片启动时施加精确时控的电磁脉冲，来扰乱其正常的执行流程。攻击者只需将手机通过USB连接到笔记本电脑，反复触发启动并注入故障，即可在安卓系统尚未启动的情况下，绕过所有安全层，在芯片的最高权限级别执行任意代码。

**实锤：Nothing CMF Phone 1演示**

Ledger团队在一款Nothing CMF Phone 1上演示了该攻击。通过USB线连接电脑后，团队在45秒内突破了手机的基础安全层，成功恢复了设备PIN码，解密了存储，并提取了多个软件加密货币钱包的助记词。经测试确认受影响的应用程序包括Trust Wallet、Kraken Wallet、Phantom、Base、Rabby和Tangem的移动钱包等。

尽管单次攻击的成功率不高，但由于整个过程可自动化并快速重复，直到注入成功，因此该攻击在实际中具有可行性。

**波及范围：哪些设备受影响？**

此漏洞影响使用联发科Dimensity 7300芯片并搭配Trustonic可信执行环境（TEE）的安卓手机。据估计，这大约覆盖了全球25%的安卓设备。已确认受影响的预算和中端手机品牌包括Realme、Motorola、Oppo、Vivo、Nothing和Tecno。此外，主打加密货币功能的Solana Seeker智能手机也使用了相同的芯片组。

**厂商回应与用户建议**

在Ledger负责任地披露漏洞后，联发科已于2026年1月发布了安全补丁，并通知了所有受影响的原始设备制造商（OEM）。但需要明确的是，由于根本原因是硬件级的Boot ROM缺陷，该补丁只能缓解利用途径，而无法从根本上消除硅片层面的漏洞。联发科此前曾表示，EMFI攻击被认为超出了MT6878芯片组预期消费用例的范围。

Ledger首席技术官Charles Guillemet警告称，智能手机并非设计用于安全存储敏感信息的“保险库”。他建议用户及时应用安全补丁，但同时强调了将私钥和助记词存储在普通设备上的风险。他强烈推荐将敏感加密货币资产转移到经过认证的专用硬件钱包中，并指出智能手机的安全性与数字资产托管需求之间仍存在显著差距。

资讯来源：Ledger Donjon安全研究团队披露信息

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