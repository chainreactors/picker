---
title: 【商密测评】密评工具箱避坑指南
url: https://mp.weixin.qq.com/s/kOAWnQI1HNMmfAPFeAKE1A
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:28:33.739837
---

# 【商密测评】密评工具箱避坑指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe07fmkwkzUsDMFfEMquRCc7icYDDPFAUaYE9v4KxviapsFl1gSnLY1a1PXEb9UzMkTz7Tk2sPHfOxgy0cQleCib55S1vg8eToIhRA/0?wx_fmt=jpeg)

# 【商密测评】密评工具箱避坑指南

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器中沉浸阅读

密评工具箱避坑指南

ToolsFx（开源，免费）

软件介绍：

跨平台密码学工具箱。包含编解码，编码转换，加解密， 哈希，MAC，签名，大数运算，压缩，二维码功能，CTF等功能。

软件地址：

```
https://github.com/Leon406/ToolsFx
```

下载地址：

```
https://github.com/Leon406/ToolsFx/releases
```

更新地址：

```
https://nightly.link/Leon406/ToolsFx/workflows/app-test/dev/artifact.zip
```

软件版本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0aeSL1tcyGlic3IDwq1k8j2KV2vRpNX1VibVPmKreTYP1clicLHSNF9HAqV1ObibDbiciaog90TFdLlumTNoBlrlM8icKxMn9ukesBFY/640?wx_fmt=png&from=appmsg)

坑：默认配置文件中没有开启大数运算

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe0la6ExjwtAaFmtO7ic2Yrwia9OB2yhyiaoezK4BwKWibOC3eKpqS8T4M0CVjyfzpo7dxVUUkuRoKgHTuIX4cAeI3y7QVxJVROCwe8/640?wx_fmt=png&from=appmsg)

配置文件：ToolsFx.properties

默认配置：

```
isEnableClassical=trueisEnablePBE=trueisEnableSignature=trueisEnableMac=trueisEnableSymmetricStream=trueisEnableQrcode=trueisEnableInternalWebview=trueextUrls=http://www.hiencode.com/,https://tool.lu/,https://www.sojson.com/encrypt_rabbit.html,https://www.qqxiuzi.cn/bianma/wenbenjiami.php,https://github.com/Leon406/ToolsFx
```

修改配置：

```
isEnableClassical=trueisEnablePBE=trueisEnableSignature=trueisEnableMac=trueisEnableSymmetricStream=trueisEnableQrcode=trueisEnableInternalWebview=trueisEnableBigInt=trueofflineMode=falseuiScale=-1extUrls=https://tools.huijusa.cn/home#/home,https://pan.huijusa.cn/,https://asn1js.eu/,https://asn.vcsjones.dev/,https://www.haomitec.com/static/change-log/index.html,https://gchq.github.io/CyberChef/,http://www.hiencode.com/,https://tool.lu/tool/,https://www.sojson.com/encrypt/,https://github.com/Leon406/ToolsFx,https://www.revshells.com/,https://demo.sub.cmliussss.net/,https://sub.cmliussss.com/,https://flk.npc.gov.cn/index,https://acl4ssr-sub.github.io/,https://openstd.samr.gov.cn/bzgk/gb/index,https://forum.ywhack.com/reverse-shell/
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe2ZWlaAIOOjUL8j3ZvIZ2G7m45ZFQia5WLyxKS4EkvflduFUicIwI44EV8oH5oKEI6PcibgHjBL09V1ic3buIBQsln55p4YIhupdMU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe1n6zUNZZXd8sKgXFOQibfMrZGg5u718bNfIAib9AdUIZH5Wic7h5DwKytObv4egmU90icrY1krpyIkaX3voJGILk1HhF9llnS5LW8/640?wx_fmt=png&from=appmsg)

泥瓦匠密评工具箱（旧版本免费，新版本付费）

软件介绍：

泥瓦匠系列之密评工具箱，基于Tongsuo 8.4.0及BouncyCastle实现相关密码算法，为密码运算操作和证书验证操作提供可视化的界面，方便快捷地完成流密码算法、分组密码算法、杂凑密码算法、非对称算法、证书管理等操作。

软件地址：

公众号关注密评泥瓦匠

下载地址：

NWJ\_CBox\_v1.3.6.1：

百度网盘：

 https://pan.baidu.com/s/1t2o9055Lio-DP748Cwc72g?pwd=bkjw

提取码: bkjw

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0Vp4ts1csicPR1luibWGtLeZV7IYeKoeDKyeKVaj3SQLeKxWW59I3GTPLbiaKyib5fIqBuEZhfFf9aaglQibhiaNSK8pMNiciagOCh6JA/640?wx_fmt=png&from=appmsg)

🚫 严禁：

 商业倒卖或二次开发

最新版加VX获取！

![](https://mmbiz.qpic.cn/mmbiz_jpg/Nlss3fiaZwbSfMnW3ycricHwVCJbhtIClFmVFroichW52aIDpq3ViaoNfRFhJCyp19UmtFrJ5BOTTQswN8pZXpYLSA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=0)

更新地址：

```
【1-23泥瓦匠系列之密评工具箱-【新增】杂凑算法分析、文件哈希值校验、SM4_MAC校验】https://www.bilibili.com/video/BV1hfMwzFEu5?vd_source=ed7b1c961b1ef8e76187a6a09637d08a
```

购买方式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0VDplPB4F9wvQXyr4EjBXfj42xMzKX07AibOGMTBaS0bTYiaYBSDJJEsBI2rdygic29Rn6Z7kusUUfq6k8dPwOe0gwDlO9zGDK4s/640?wx_fmt=png&from=appmsg)

坑：部分功能异常导致数据分析出错

例如，十六进制转字符串

3030303030303300E588A9E58883E4BFA1E5AE89000000000000000000000000313736303032303034383800000000006C6972656E4071712E636F6D00000000

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe2uK4EQBy7FCkaLsC7qzKuW9BB14qciaMv0PTIgc5AyLTrnEpsECibdxBmqJmVZmSxcHZicPHtyC8LesJu3clquAhVeXib56SA0yxU/640?wx_fmt=png&from=appmsg)

正确结果应该是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2IsAYnuScVF5zAiaKWPMQdfHXvORdhb6nx7SV0l3pfnmTzoGPuDFBfeURSiaUwFjBFbbNotfRQic4x9JmV2biaLymbp2stv3osteA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2mbJ9T5E4X5yWiaNUxSbakH9GtmTicZ1960kicJdBoiaoIj3UZZZia8wmGGS9PN770tmp2dXHAlNJO5CsAlfcX3VIOGIxBlHZnj6Pk/640?wx_fmt=png&from=appmsg)

商用密码验证工具（网页版免费，离线版付费）

软件介绍：

密评工具百宝箱是参考《商用密码应用安全性评估测评工具指引》及《量化评估2023版》等标准，由多名多年密评实际工作经验者提供技术支持，基于Bouncy Castle、Pcap4j、SmartAdmin等开源库，开发的一款综合性密评验证平台。平台已基本实现工具指引中的大部分常用工具，旨在为用户提供高效、可靠的商用密码安全评估支持。

本平台面向互联网用户永久免费开放，所有工具永久免费使用。所有上传至平台的数据仅用于计算、分析和逻辑处理，平台不进行数据存储、备份、转发、销售等任何行为。用户可以放心使用，您的数据隐私将得到严格保护。

我们致力于成为互联网密码相关工具的首选平台，为广大用户提供更加正确、有效、便捷、高效的在线密码验证服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe06yNDoqhv2K85WOsXoSDftubJHFHDLuydLrGd7woW7S6icmStM7LHTcgibNe1Sf8ZqUdpob2YJVWxV2cBMq9mWRnjqVlA2JOJvA/640?wx_fmt=png&from=appmsg)

网页地址：

```
https://tools.huijusa.cn/home#/home
```

软件地址：

```
https://tools.huijusa.cn/home#/home
```

下载地址：

```
https://pan.huijusa.cn/
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe3vgt4ibicx0bOtWvYDp5SV2hYCr6rPzqu63B27UvNmBCxDEBrpoRQnXCxVhHf0AB32oBu9kPFEicLDCqCiadib48NsQg1Fl4kiaIj80/640?wx_fmt=png&from=appmsg)

更新地址：

```
所有功能已恢复正常使用，已购买离线版的用户，客户端下载地址为：https://pan.huijusa.cn
```

购买方式：

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1CX0UaNZIgbnrlbvkyy3oDULQlqk7FNl1c0u7CZP9OyUN4RY3VxYIM1P9ibeo91Dib53xwJEYONVPYtum8AerpP8lmFiaNzxasI0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe3n7vzB6YQia7Tyic8te6ZibxBrYkkSNeMZUfXdAI6t4GPUkMYBLpVaLDuxukEkR1Scto5mib2YnSBhniaQ2D5NosgAdiaHSPpC4iba3U/640?wx_fmt=png&from=appmsg)

坑：部分数据功能实现不是按照国标文件规定

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1rgjdUFBqbYlzyBqLLx0LLTP3vcGqafRZLdB1W7jibXICicicRJC5aOqk6FlmVPHdImGgfClaBibgTf3ZuqPibff0DibxFwa7ibM5ibnw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2xMErlAz7Jf3eVqxGu3tQIEzmjmywr9NpOR9qlSgqqfywyDICvfCC6ibk83viar6xuW2VD6U6loHMCs0PlWz4yyhGCibic6Wa2wYw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

作者提示: 内容由AI生成

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR10Jq56nSiafMPnQSnibHYF5nLj0lQmgOpIPGCVchYCar4R1WN50svCnBva2ia0FzfIx212iaABoed4fYA/0?wx_fmt=png)

利刃信安

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR10Jq56nSiafMPnQSnibHYF5nLj0lQmgOpIPGCVchYCar4R1WN50svCnBva2ia0FzfIx212iaABoed4fYA/0?wx_fmt=png)

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