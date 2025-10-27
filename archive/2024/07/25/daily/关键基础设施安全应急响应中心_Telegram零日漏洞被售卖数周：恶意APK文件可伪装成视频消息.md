---
title: Telegram零日漏洞被售卖数周：恶意APK文件可伪装成视频消息
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545063&idx=5&sn=174632fd15b0ca95c5d986caa6be8d69&chksm=c1e9bcb6f69e35a0004f5ce8482e45ff22f8590076ea898168b7a2eaa206098afb786f06dd09&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-25
fetch_date: 2025-10-06T17:43:54.856187
---

# Telegram零日漏洞被售卖数周：恶意APK文件可伪装成视频消息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs3gFteicP6rfs4zmic9RZeiaUstxlw1mpoNkFukw4B01kwdaTm8tITT8FNNiafQdg9wYgSuFKtnrIQPA/0?wx_fmt=jpeg)

# Telegram零日漏洞被售卖数周：恶意APK文件可伪装成视频消息

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs3gFteicP6rfs4zmic9RZeiaUzk61m9XgXDqtjJLmRxf9BvFzTZEAbyDibv65l1MH3VvtpMWIPybqFRQ/640?wx_fmt=jpeg&from=appmsg)

利用该漏洞需要多步交互和授权，这大大降低了攻击成功的风险；

相关零日漏洞在地下论坛长期售卖，也说明了攻击者的旺盛需求，用户需要尽可能保持安全使用习惯。

7月23日消息，一个名为“EvilVideo”的Telegram安卓版零日漏洞，允许攻击者将恶意的安卓APK有效负载伪装成视频文件发送。

6月6日，威胁行为者“Ancryno”在XSS俄语黑客论坛上发帖，首次销售Telegram零日漏洞利用工具，称此漏洞存在于Telegram v10.14.4及更早版本中。

欧洲安全厂商ESET的研究人员在一个公共Telegram频道上，分享概念验证（PoC）演示后发现了该漏洞，藉此获取了恶意有效负载。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s4SGvLHlLItNx2vrdHvWkkCBBGnvbWODmRGViaKVvys74nLJvvyibSB4XeYRMFXGxnL5j6mKZFFbXQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

图：威胁行为者在黑客论坛上出售漏洞利用工具

ESET确认该漏洞在Telegram v10.14.4及更早版本中有效，并将其命名为“EvilVideo”。ESET研究员Lukas Stefanko于6月26日和7月4日两次向Telegram负责任地披露了该漏洞。

Telegram于7月4日回应称，正在调查上报的漏洞，并在7月11日发布的10.14.5版本中修补了该漏洞。

这意味着威胁行为者至少有五周的时间，可以利用该零日漏洞进行攻击。

目前尚不清楚该漏洞是否在攻击中被积极利用，ESET分享了恶意有效负载使用的C2服务器地址“infinityhackscharan.ddns[.]net”。

外媒BleepingComputer在VirusTotal上发现了两个使用该C2的恶意APK文件，它们伪装成Avast Antivirus或“xHamster Premium Mod”。

# **Telegram零日漏洞利用情况**

EvilVideo零日漏洞仅在Telegram安卓版上有效。该漏洞允许攻击者创建特制的APK文件。当这些文件被发送给其他Telegram用户时，会显示为嵌入视频。

ESET认为，该漏洞利用了Telegram API以编程方式创建信息。信息看似一条30秒长的视频。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s4SGvLHlLItNx2vrdHvWkk4G0PErjzmANZ0kAWOiaice6kkgX9aeBTsSIy2NhIfJcnUAe6wGYFxIBg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

图：APK文件预览为30秒视频片段

在默认设置下，安卓上的Telegram应用会自动下载媒体文件。因此频道参与者一旦打开对话就会在设备上收到有效负载。

即便已禁用自动下载，用户只要轻触视频预览就会开始下载文件。

当用户尝试播放假视频时，Telegram会建议使用外部播放器。在这种情况下，接收者可能会点击“打开”按钮并执行有效负载。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s4SGvLHlLItNx2vrdHvWkkiajS5TeR5MRyIlb1mVVou05U4pB4QjzGNzJapQrtZqnMQZSt2ZMUM9g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

图：启动外部视频播放器的提示

接下来还需要额外一步：受害者必须在设备设置中启用安装未知应用程序，允许恶意APK文件在设备上安装。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s4SGvLHlLItNx2vrdHvWkkCLrhPK2PJ8HXtv53ASfh9wDOcSol2Dvj4IDk8ticQzib22MMxpQdWaWQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

图：需要批准APK安装的步骤

尽管威胁行为者声称漏洞可“一键式”利用。但是，由于需要多次点击、多个步骤，以及特定设置才能在受害者设备上执行恶意有效负载，这大大降低了攻击成功的风险。

ESET在Telegram的网页客户端和Telegram桌面版上测试了该漏洞，发现它在这些平台上不起作用，因为有效负载被视为MP4视频文件。

Telegram在10.14.5版中对漏洞进行了修复，现在能正确显示APK文件的预览，因此接收者不再会被伪装成视频的文件所欺骗。

如果您最近通过Telegram收到要求使用外部应用播放的视频文件，请使用移动安全套件扫描文件系统，以定位并移除设备上的有效负载。

通常，Telegram视频文件存储在“/storage/emulated/0/Telegram/Telegram Video/”（内部存储）或“/storage/<SD卡ID>/Telegram/Telegram Video/”（外部存储）中。

**参考资料：**

bleepingcomputer.com

原文来源：安全内参

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