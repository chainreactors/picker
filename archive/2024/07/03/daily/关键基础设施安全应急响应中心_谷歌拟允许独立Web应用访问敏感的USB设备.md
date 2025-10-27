---
title: 谷歌拟允许独立Web应用访问敏感的USB设备
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247544704&idx=2&sn=d740b5c9e393be021fb4a5c78c559732&chksm=c1e9a3d1f69e2ac7bcdff018828cda943bc4a4b3f1d3bca0e87805af099bc111e0099d4d63f7&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-03
fetch_date: 2025-10-06T17:43:33.584692
---

# 谷歌拟允许独立Web应用访问敏感的USB设备

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogt6dnKwtVIc9Fw9fGEAnkrQdQicsuytxP1ERqQKzGaJnbJAnXWwTmBfiaSgAPHNVEfpAFIkz5mCjR7Q/0?wx_fmt=jpeg)

# 谷歌拟允许独立Web应用访问敏感的USB设备

关键基础设施安全应急响应中心

BleepingComputer消息，谷歌正在开发一项不受限制的 WebUSB 新功能，可允许受信任的隔离网络应用程序绕过 WebUSB API 中的安全限制。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39LcdUTibWwO2fKdibMKDKm2AxBS9iavoa11RtTqdQEblTJNgUECJia0xuOaBuvGvtWKN883vPF50AHZA/640?wx_fmt=jpeg&from=appmsg&wxfrom=13&tp=wxpic)

WebUSB 是一种 JavaScript API，能够让网络应用程序访问计算机上的本地 USB 设备。作为 WebUSB 规范的一部分，某些接口，比如HID、大容量存储、智能卡、视频、音频/视频设备和无线控制器会受保护，不能通过网络应用程序访问，以防止恶意脚本访问潜在的敏感数据。

此外，WebUSB 规范还包括一个阻止列表，禁止通过 API 访问的特定 USB 设备，如用于多因素身份验证的 YubiKeys、Google Titan 密钥和 Feitian 安全密钥。

谷歌目前正在测试的「无限制 WebUSB」功能，允许隔离的网络应用程序访问这些受限制的设备和接口。谷歌在 Chrome 浏览器的状态更新中指出：「WebUSB 规范定义了一个易受攻击设备的屏蔽列表和一个受保护接口类的列表，这些设备和接口类被禁止通过 WebUSB 访问。有了这项功能，拥有访问 ‘usb-un-restricted’ 权限策略功能的隔离网络应用程序将被允许访问这些列表中的设备和受保护的接口。」

独立网络应用程序是指不托管在实时网络服务器上，而是打包成网络捆绑包（Web Bundles）、由开发人员签名并分发给最终用户的应用程序。这些应用程序通常供公司内部使用。为使其正常运行，这些网络应用必须拥有使用 「USB-unrestricted」功能的权限。

当具有该权限的应用程序试图访问 USB 设备时，系统会首先检查该设备是否在易受攻击设备的拦截列表中。如果是，该设备通常会从访问列表中移除。但使用「usb-unrestricted」权限的网络应用程序可以绕过这一限制。

这一功能无疑会让受信任的隔离网络应用程序能够访问更广泛的 USB 设备，从而在受信任的环境中实现更多功能。谷歌表示，它计划在 2024 年 8 月发布 Chome 128 版本中对其进行测试。

**参考资料：**

https://www.bleepingcomputer.com/news/google/google-chrome-to-let-isolated-web-app-access-sensitive-usb-devices/

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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