---
title: 锐捷云管理平台曝严重漏洞：可从云端劫持WiFi热点
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513360&idx=2&sn=d8aff409483c58eb180c3a8fbbc1b6b6&chksm=ebfaf230dc8d7b26fc2469ed55f55821b6ed7155fdc777f069cc7cd1713d97964cf82208d5cd&scene=58&subscene=0#rd
source: 安全内参
date: 2024-12-27
fetch_date: 2025-10-06T19:37:39.371741
---

# 锐捷云管理平台曝严重漏洞：可从云端劫持WiFi热点

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tLf2okx08NZAFMBq4kXIVal8NRibqkuQeB8guL4uGQmXLkc6iaMSeIlXnRibMVBEtA0SbbQpsup2K4Q/0?wx_fmt=jpeg)

# 锐捷云管理平台曝严重漏洞：可从云端劫持WiFi热点

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvbQot4tey7QwvtPeflfnf1djQRccjq5yLZrjJU3OrD9pbfbKcdDN2wUpuNhK8AUrpdswD9w3YkibWw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

近日，网络安全研究人员在锐捷网络的云管理平台中发现多个严重漏洞，这些漏洞可能使攻击者全面控制网络设备，进而对企业和个人用户的网络安全构成重大威胁。

**从云端入侵WiFi接入点**

来自工控安全公司Claroty的研究人员NoamMoshe和Tomer Goldschmidt指出，这些漏洞不仅影响锐捷的睿易云管理平台（Reyee），还波及基于Reyee OS的网络设备。

研究团队不仅发现了多达10个漏洞，还设计了一种名为“Open Sesame”的攻击方式，可通过云端入侵物理附近的接入点，从而未经授权访问网络。

**在发现的10个漏洞中有三个高危漏洞，如下：**

CVE-2024-47547

* 评分：9.4（高危漏洞）
* 问题：弱密码恢复机制，使身份验证机制易受暴力破解攻击。

CVE-2024-48874

* 评分：9.8（高危漏洞）
* 问题：服务端请求伪造（SSRF）漏洞，攻击者可利用其访问AWS云元数据服务，渗透锐捷的内部云基础设施。

CVE-2024-52324

* 评分：9.8（高危漏洞）
* 问题：使用高风险功能，允许攻击者发送恶意MQTT消息，导致设备执行任意操作系统命令。

**攻击链条与破坏潜力**

Claroty研究人员指出，MQTT协议的身份验证机制存在明显弱点，只需设备序列号即可破解（CVE-2024-45722，评分：7.5）。通过这一漏洞，攻击者可以获取所有连接至云端的设备列表，并生成有效的认证凭据。这些凭据进一步被利用执行以下攻击：

* 拒绝服务攻击（DoS）：通过伪造认证中断设备连接。
* 发送虚假数据：在云端注入错误信息，误导设备用户。

此外，攻击者还可以拦截Wi-Fi信标，提取设备序列号，从而利用MQTT漏洞实现远程代码执行。这种“OpenSesame”攻击被分配为CVE-2024-47146（评分：7.5）。

**漏洞修复与影响评估**

在经过负责任披露后，锐捷网络已修复了上述漏洞，并更新了相关云服务。用户无需额外操作即可确保设备安全。据估计，约5万台云连接设备可能受到影响。

Claroty的研究人员警告，这一事件再次表明，物联网设备（IoT）中的安全弱点对网络安全构成深远威胁。尤其是无线接入点、路由器等用户门槛较低的设备，却能为攻击者提供深入网络的路径。

参考链接：

https://claroty.com/team82/research/the-insecure-iot-cloud-strikes-again-rce-on-ruijie-cloud-connected-devices

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