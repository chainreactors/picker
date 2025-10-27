---
title: 开源工具 rsync 曝重大漏洞，黑客可越界写入缓冲区远程执行代码
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588763&idx=2&sn=987fea6e7bc8cce2c77f2e2035072ac4&chksm=b18c26d186fbafc74e6a05aa86e92183c63d2d9a959a88738a9e938d04954b0f5f417afec628&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-21
fetch_date: 2025-10-06T20:11:15.016728
---

# 开源工具 rsync 曝重大漏洞，黑客可越界写入缓冲区远程执行代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FBzrJVibngmNZ3zSxib8v9pHqyj8FIJXMWDMg8gFMruDGSjWwWmfribydibkNwJIScG3Ry0CxZSa1Mgw/0?wx_fmt=jpeg)

# 开源工具 rsync 曝重大漏洞，黑客可越界写入缓冲区远程执行代码

看雪学苑

看雪学苑

近日，开源文件同步工具 rsync 被曝存在多个严重安全漏洞，其中最严重的漏洞允许黑客通过越界写入缓冲区的方式远程执行代码。这一消息引发了广泛的关注，尤其是对于使用 rsync 的企业和个人用户来说，安全风险迫在眉睫。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FBzrJVibngmNZ3zSxib8v9pHReGYIeuAicbgwx2CpXBzWHD4UKKWk3Kxq5WEWRAdK4d4Hq5x2mdlskw/640?wx_fmt=png&from=appmsg)

据 Red Hat 产品安全工程师 Nick Tait 介绍，rsync 存在的 6 项漏洞中，最严重的是 CVE-2024-12084，CVSS 风险评分为 9.8 分（满分 10 分）。该漏洞存在于 3.2.7 版本及以上的 rsync 中，主要原因是程序对校验和（checksum）长度验证不当，导致攻击者可以通过越界写入 sum2 缓冲区，从而实现远程代码执行。

此外，Nick Tait 还披露了 CVE-2024-12085 漏洞，该漏洞 CVSS 风险评分为 7.5 分。该漏洞发生在 rsync 处理程序比对文件校验和的过程中，攻击者通过操控校验和的长度，可以使程序比对校验和与未初始化的内存，进而泄露部分未初始化的堆栈数据。

根据外媒 Bleeping Computer 的调查，全球超过 66 万台服务器可能因此受到安全威胁，其中大多数位于中国大陆和美国。rsync 是一款广泛使用的开源文件同步和数据传输工具，因其高效的增量传输能力而备受青睐，常用于备份系统、公共文件分发仓库以及云和服务器管理操作。

这些漏洞的发现引发了安全专家的高度重视。CERT 协调中心（CERT/CC）警告称，前两个漏洞（CVE-2024-12084 和 CVE-2024-12085）组合起来，攻击者可以在运行 rsync 服务器的设备上执行任意代码。此外，攻击者还可以通过控制恶意服务器，读取或写入连接客户端的任意文件，甚至提取敏感数据（如 SSH 密钥），并通过覆盖文件（如 ~/.bashrc 或 ~/.popt）来执行恶意代码。

目前，rsync 已发布 3.4.0 版本，修复了相关漏洞。Red Hat 也建议所有用户尽快升级至 3.4.0 版本，以消除安全风险。对于无法立即升级的用户，建议采取临时缓解措施，例如在编译时使用特定标志禁用 SHA256 和 SHA512 摘要支持，或者通过防火墙屏蔽 rsync 服务端口（默认为 873/TCP），仅允许可信来源访问。

开源同步工具 rsync 被曝存在多个高危漏洞，攻击者可利用漏洞远程执行代码，全球超 66 万台服务器受影响。

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

修改于

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