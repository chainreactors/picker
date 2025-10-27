---
title: 7-Zip高危漏洞曝光！攻击者可绕过安全机制远程执行代码，速升级
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589076&idx=2&sn=d0f764edebe291ce5b96f036fabe1a56&chksm=b18c271e86fbae08b860c61d822fe9c14f3216204f7890876285cf7d58d7086a9d18b2c2002e&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-23
fetch_date: 2025-10-06T20:10:57.873121
---

# 7-Zip高危漏洞曝光！攻击者可绕过安全机制远程执行代码，速升级

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GDKxUicIYay3UHVJ49UvwUEbzpFzibPMa5OVehyKB7Sg5r8cM4DF22IXVHclIgh7VJvvwsRKTk98XA/0?wx_fmt=jpeg)

# 7-Zip高危漏洞曝光！攻击者可绕过安全机制远程执行代码，速升级

看雪学苑

看雪学苑

近日，一款广泛使用的开源文件压缩软件7-Zip被曝出存在严重的安全漏洞，编号为CVE-2025-0411，该漏洞的CVSS评分为7.0，属于高危漏洞，引发了广泛的安全担忧。根据相关报道，该漏洞允许远程攻击者绕过Windows系统的一项关键安全功能——“网络标记”（Mark of the Web，简称MotW），从而在受影响的系统上执行任意代码。

MotW是微软Windows系统的一项安全功能，用于标识从不可信来源（如互联网）下载的文件。当用户尝试打开这些带有MotW标记的文件时，系统会弹出警告对话框，提醒用户该文件可能来自不安全的来源，从而降低用户误运行恶意文件的风险。然而，7-Zip在处理带有MotW标记的压缩文件时出现了问题。当用户使用存在漏洞的7-Zip版本解压此类文件时，解压后的文件不会保留MotW标记，这就使得攻击者能够绕过这一关键的安全检查，进而在当前用户权限下执行任意代码。

根据相关安全研究人员的分析，攻击者可以通过精心构造的恶意压缩包来触发该漏洞。当用户打开这些恶意文件或访问恶意网页时，攻击者就可以利用该漏洞在用户的计算机上执行任意代码。这一漏洞的存在使得用户在处理来自不可信来源的文件时面临巨大的安全风险，尤其是在用户具有管理员权限的情况下，攻击者可能会利用该漏洞获取系统的完全控制权，进而分发恶意软件或进行未经授权的操作。

值得注意的是，该漏洞影响了7-Zip的24.07及之前的所有版本。不过，好消息是，7-Zip的开发者Igor Pavlov已经在2024年11月30日发布的7-Zip 24.09版本中修复了这一漏洞。在24.09版本的更新说明中提到，7-Zip File Manager在处理嵌套压缩文件时未能正确传播Zone.Identifier流，导致解压后的文件丢失了MotW标记。而24.09版本修复了这一问题，确保解压后的文件能够正确保留MotW标记，从而恢复了Windows系统的安全防护功能。

鉴于该漏洞的严重性，安全专家强烈建议所有7-Zip用户尽快检查自己的软件版本，并升级到7-Zip 24.09或更高版本。此外，用户在日常使用中还应保持警惕，避免打开来自未知或不可信来源的压缩包。同时，建议用户启用额外的终端安全解决方案，以检测和阻止可疑文件活动，从而进一步降低安全风险。

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

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibExiboJzOiafqGLvlOkrmU6NIr3qSr7ibpkIo2N5mhCTNXoMl37s2oRSIDw/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

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