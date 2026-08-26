---
title: 【古法渗透】aes rsa 自加密
url: https://mp.weixin.qq.com/s/Ustpw4OxritqdlOrHNe2bw
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:04:27.413163
---

# 【古法渗透】aes rsa 自加密

# 【古法渗透】aes rsa 自加密

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于moonsec
，作者暗月大徒弟

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM5HMB6NAStYthWA6zMuef4MVymkHPmm4oia1bibvmiafatiaQ/0)

**moonsec**
.

暗月博客

```
免责声明：本公众号所提供的文字和信息仅供学习和研究使用，不得用于任何非法用途。我们强烈谴责任何非法活动，并严格遵守法律法规。读者应该自觉遵守法律法规，不得利用本公众号所提供的信息从事任何违法活动。本公众号不对读者的任何违法行为承担任何责任。
```

访问  encrypt靶场靶场 随意输入账号和密码 选择 aes+rsa加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRtSEFqYHjRBpiaGHXiaX0L6PjWXgyaspcvRdTI8Db1coEDGAkcnu4zadsqRiaoHdWPYE4n1oLsYGPTmmDmBMqjUSJnsaWzJk2KnsA/640?wx_fmt=png&from=appmsg)

查看数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRsW5bHksCPicMfSR8kicojsnwqaT1EbjhHibTc0Qpm6NJfnicBfSYMYxFqLBLN5dMH1ic2YiaaeGA1PYZCx7SfrVtXe2NgpPDd5mRiasM/640?wx_fmt=png&from=appmsg)

分析js文件

在这里下一个断点调试看看

![](https://mmbiz.qpic.cn/mmbiz_png/0ic45F94NibRvt8zDhvd0RW76uTWnLGcNkgbicg4aOn1UJBtwVkbyWfwlvLL3Ce2CdnicDXNjNaQbqxrQFfiaMLDEqNWdb15QpxibztYXrliblvFfA/640?wx_fmt=png&from=appmsg)

输入的账号和密码 进行 aes加密

接着是rsa处理 对之前的key和iv进行rsa加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRvqlZicERsDyq76ib6qpEheYjtoIZEM9pA1j0Pia3P0VnR33RVU1TaCWTU4wcBd9ibCajUxh0IqiazSqNiaia96uvicnAtSH5TdEtdINY0/640?wx_fmt=png&from=appmsg)

接着提交到服务器进行处理

![](https://mmbiz.qpic.cn/mmbiz_png/0ic45F94NibRvImWZJnuziboKz1ZlFj6ybQOC76h3oRgplGARzJdptxHxw9BVTUT5y6D933k2Plj4ibhj3KgCGgRVFVWpKqvhzs3FNtcZiabbNwM/640?wx_fmt=png&from=appmsg)

从上面的分析中发现iv和key是不变的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRtGOMgCELZc6RMQgj4QKhJvicr1icFt7AGHfLYILUhvUWkgGicQmVR6ALSXeo1jPXc109KqGu0Pia021qNpVSmib51PnLOSicA3r3xpM/640?wx_fmt=png&from=appmsg)

这段是 账号和密码 进行aes加密的 只要对这段进行重新封包即可。

```
"encryptedData":"cIozz6BiJgijaeb0Z2musU85+yl7ZWKP7mV/IpzuzqTnEn+mQ5k7TxPP7Ap7Epfg"
```

使用 burpsuite插件 autodecoder

调试替换 key和iv的值

```
	const key = CryptoJS.enc.Utf8.parse("1234567890123456");
	const iv = CryptoJS.enc.Utf8.parse("1234567890123456");
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRvv2h3MgxUXbnAKcdey1aXic7emsggArOFnHlNjEWWM3OibuEylewbqf1v1Sagwbrfm6TsuU2JIpYM6vpfRRoQeucXSWiauhh8lIw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0ic45F94NibRuC9r4sTfX34ZV6wDiabKSNSqxx2X4AlD4XUibLkFcNvc0gGibG9n4hb1J1w1sujUdibqXFF7tLCN8fwleKk20uicvdkRK3aRicvMIibQ/640?wx_fmt=png&from=appmsg)

提交即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRth2Wok64KdYoyoocsuJLkJ6W8WYrLON7a43dyMX1KneZNYweFjz1CC8dJQt3WCppZHobOS4WibdOzVSKydFIc4liaibV5dialsOSk/640?wx_fmt=png&from=appmsg)

也可以使用他默认的key和iv

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRufvqlLfMYg7KDll4Zy7OyTEIia75c5th27icibt1wcRTmMsfV2lpticrAhPpmM7iaGwvltAceh0zUcU0j5eKjUupIuwiayhCPLFajys/640?wx_fmt=png&from=appmsg)

提交一样可以

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0ic45F94NibRuhPic5z6Pos2UdgWchWjMUXlib1G4Y301CicicleAQeweYbsUDs3Vcfj3sgSnzabcAL5phVHnwCONQFvvXgCdQFWjOs7sgD7355IE/640?wx_fmt=png&from=appmsg)

需要本文相关工具

关注公众号回复【20260824】

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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