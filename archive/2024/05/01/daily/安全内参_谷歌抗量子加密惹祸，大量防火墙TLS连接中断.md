---
title: 谷歌抗量子加密惹祸，大量防火墙TLS连接中断
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247511518&idx=2&sn=a6c8ea2f94a60b1dd64f81b3c26a8332&chksm=ebfaeafedc8d63e8fd968b02819a3d75a56994dc6ffd01ea092f876f0ad0967bb1977ff74103&scene=58&subscene=0#rd
source: 安全内参
date: 2024-05-01
fetch_date: 2025-10-06T17:19:08.593756
---

# 谷歌抗量子加密惹祸，大量防火墙TLS连接中断

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tzgaGIBBOibreEoUicy4zy5W65HQlXc7BKFncvu6IMpEZPWicIbqd4IaHPwhHV7ghqOe0EmptgEsa9g/0?wx_fmt=jpeg)

# 谷歌抗量子加密惹祸，大量防火墙TLS连接中断

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvaaiaN4XZskIm65Nic6k9hmK53olqUfBd5yEER8yTuOcs4MyLBY1wKcITpzk7yjic32LlajQApmUK9zg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

作为后量子时代的标志性产品，谷歌首个抗量子加密浏览器Chrome 124的发布意外引发了网络安全业界的骚乱。

该Chrome版本默认启用全新的抗量子安全传输层安全(TLS)密钥封装机制X25519Kyber768，用于保护用户免受即将到来的量子破解威胁。然而，这项新技术却由于兼容性问题导致TLS连接中断，很多用户无法正常连接访问网站、服务器和多家安全厂商的防火墙。

**“先存储，后解密”攻击**

早在去年8月，谷歌就开始测试代号“Kyber768”的抗量子密钥协商算法，并计划将其整合至最新的Chrome版本中。理论上，Kyber768可以保护基于TLS 1.3和QUIC连接的Chrome流量，使其免遭未来量子计算机的破解。

“经过数月的兼容性和性能影响测试，我们决定在Chrome 124桌面版本中启用混合式抗量子TLS密钥交换，”谷歌Chrome安全团队解释道：“这项技术可以保护用户流量免受‘先存储，后解密’（黑客大量收集囤积加密的网络流量数据，等未来量子计算机成熟后进行解密）攻击的威胁。”

“先存储，后解密”攻击是数据安全面临的一个巨大潜在威胁。为了防范此类攻击，许多企业已经开始在其网络架构中加入抗量子加密技术。苹果、Signal和谷歌等科技巨头均已率先采用了抗量子算法。

**大量防火墙、服务器、网络设备产生兼容问题**

然而，根据系统管理员们的反馈，自上周Google Chrome 124和微软Edge 124桌面版推出以来，一些网络应用、防火墙和服务器产品在执行Client Hello TLS握手时会断开连接。

“该问题似乎影响了服务器处理客户端问候消息中的额外数据的能力，”一位管理员表示：“同样的问题也出现在了新版Edge浏览器上，似乎与派拓网络（Palo Alto Networks）防火墙产品的的SSL解密功能存在冲突。”

据报道，该兼容性问题的影响面非常大，多个供应商（例如Fortinet、SonicWall、Palo Alto Networks、AWS）的安全设备、防火墙、网络中间件和各种网络设备都遭遇了类似的兼容性问题。

值得注意的是，这些错误并非源于Google Chrome本身的漏洞，而是由于部分网站服务器和网络设备未能正确实现传输层安全(TLS)协议，无法处理用于抗量子加密的更大ClientHello消息。

这些不支持X25519Kyber768算法的网络设备，不会尝试降级至经典加密方案，而是直接拒绝使用Kyber768算法建立的连接。

**TLS连接中断问题的解决方法**

一个名为tldr.fail的网站专门分享了有关抗量子ClientHello消息如何导致服务器连接错误的信息，并为开发者提供了修复漏洞的指南。

网站管理员也可以通过在Chrome浏览器中启用“chrome://flags/#enable-tls13-kyber”标记来手动测试服务器的兼容性。启用后，管理员可以尝试连接到自己的服务器，并查看是否会产生“ERR\_CONNECTION\_RESET”错误。

受影响的Google Chrome用户可以访问“chrome://flags/#enable-tls13-kyber”并禁用混合式Kyber支持来暂时规避该问题。

系统管理员还可以通过以下方式进行修复：在“软件>策略>Google>Chrome”路径下禁用“PostQuantumKeyAgreementEnabled”企业策略；或者联系网络设备供应商，获取适用于其服务器或中间件的更新补丁，以使其兼容抗量子加密标准。

微软也发布了相关信息，指导用户如何通过Edge浏览器组策略控制此功能。

需要注意的是，从长远来看，TLS协议终究需要采用抗量子安全密码。谷歌未来也将移除Chrome企业策略中禁用混合式Kyber支持的选项。

参考链接：

* https://groups.google.com/a/chromium.org/g/chromiumdev/c/K\_HO5LsPDKc?pli=1
* https://www.reddit.com/r/sysadmin/comments/1carvpd/chrome\_124\_breaks\_tls\_handshake/
* https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#enable-post-quantum-key-agreement-for-tls

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：GoUpSec

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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