---
title: Google Home智能音箱漏洞可监听用户会话
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247533654&idx=3&sn=f799f0ef49a7ef1f3c0de5b3ed1bfe1d&chksm=c1e9c807f69e4111c33bcf480452885c9a7c5f1c524c78ce2a20e10f99651b9dc96dcc98b594&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-01-04
fetch_date: 2025-10-04T03:00:23.284316
---

# Google Home智能音箱漏洞可监听用户会话

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguxXZr3iceO5XIZtBiakBRMf5qNJvorun46CAn91tzNIJ69YHGgsHtqSW8JY98usxBX97vXUKlhpdqw/0?wx_fmt=jpeg)

# Google Home智能音箱漏洞可监听用户会话

关键基础设施安全应急响应中心

# **漏洞概述**

2016年，谷歌发布Google Home智能音箱产品。2021年，安全研究人员Matt在Google Home智能音箱设备中发现了一个安全漏洞，攻击者利用该漏洞可以在受害者设备中安装后门装好，并通过互联网远程发送命令给受害者设备、访问麦克风数据量、在受害者网络中发起任意HTTP请求，甚至可能暴露WiFi密码，使攻击者访问受害者的其他设备。

研究人员在Google Home mini智能音箱测试时发现，使用Google Home app添加的新账号可以通过云API远程发送命令。

研究人员通过Nmap扫描发现了Google Home的本地http API端口，然后设置代理进行加密的HTTPS流量抓包，以期获取用户认证token。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibibibicjt5iayRJiaNVZ44ibDZI3j0LwG0OYaOaYibkqZcf8DStk55XD2O5FdJEKj70Y3wqgJHfhtRjjgfg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 HTTPS流量抓包

在目标设备上添加新用户需要2个步骤，首先需要设备名、证书、本地API的cloud ID。有了这个信息，就可以发送链接请求到谷歌服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibibibicjt5iayRJiaNVZ44ibDZI3G1DWYp75BgPpA4hRV7E04rTN5UribSVwDX7Uuyu8ZWC0cUqNSGcly5w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 包含设备ID数据的链接请求

整个攻击的流程如下：

· 攻击者想要监听无线网络范围内的Google Home，但无需知道受害者的WiFi密码；

· 攻击者通过谷歌公司的Mac地址前缀来发现受害者的Google Home设备；

· 攻击者发送deauth包使设备从网络端口，并进入设置模式；

· 攻击者连接到设备的设置网络，并请求受害者设备信息，包括设备名、证书、cloud ID等；

· 攻击者连接到互联网，并使用获得的设备信息将其账号与受害者设备链接起来；

· 攻击者就可以通过互联网来监听受害者设备了。

研究人员在GitHub上发布了3个PoC，包括植入恶意用户、通过麦克风进行监听，在受害者网络中发起任意http请求，在受害者设备上读写任意文件。PoC代码参见：https://github.com/DownrightNifty/gh\_hack\_PoC

在受害者设备上植入恶意账户就可以通过Google Home speaker执行以下操作：

· 进行在线购物；

· 远程开锁或解锁车辆；

· 通过暴力破解PIN码的方式解锁用户智能门锁。

此外，攻击者还可以滥用"call [phone number]"命令来在特定时间激活麦克风，拨通攻击者号码，并发送麦克风数据流，实现对用户的监听。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibibibicjt5iayRJiaNVZ44ibDZI3Gic10owUSicDYAaLIPqG6V9eQWyhT2PC00EmXFDibxBHLZveWBaQUGIbQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 获取用户麦克风数据

在拨打电话过程中，设备的LED灯会变蓝。如果受害者注意到LED灯的变化，可能会认为设备在进行固件升级。

此外，攻击者还可以在受害者设备上播放音乐、重命名设备、重启设备、忘记设备保存的WiFi网络密码、进行蓝牙或WiFi配对等。

# **漏洞补丁**

Matt于2021年1月发现了该漏洞，并在3月将漏洞报告给了谷歌，谷歌已于2021年4月修复了该漏洞。Matt也获得了谷歌的10.75万美元漏洞奖励。

完整技术分析参见：https://downrightnifty.me/blog/2022/12/26/hacking-google-home.html

**参考及来源：**

https://www.bleepingcomputer.com/news/security/google-home-speakers-allowed-hackers-to-snoop-on-conversations/

原文来源：嘶吼专业版

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

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