---
title: 【网络安全】鸿蒙6应用网络抓包的高阶技巧与实践
url: https://mp.weixin.qq.com/s/7K26y_AZ1Su4mrxMSgMJSA
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:32:03.766943
---

# 【网络安全】鸿蒙6应用网络抓包的高阶技巧与实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgptXyUsqKlUMUroXGsvdIURxS6KHdhAV2qb8iafKpQsAtHicSVkhvzRq9w/0?wx_fmt=jpeg)

# 【网络安全】鸿蒙6应用网络抓包的高阶技巧与实践

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器中沉浸阅读

鸿蒙6应用网络抓包的高阶技巧与实践

试想一下，你现在手机只有一部手机和一台电脑，手机通过数据上网，给电脑分享热点，如何使用电脑上的渗透测试工具测试手机app？

如果用手机数据分享个人热点，如何设置系统代理？

如果是有另外的无线，可以让手机和电脑在同一个无线下，那就可以在wifi连接处设置代理，没有无线的话如何设置代理？

为了解决这个问题，我们在鸿蒙系统上找到了一款非常不错的软件---Wing Relay。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpkdIJcCsNqSZmCyGJWdaibbVb0ydyq61JYZDsr9hbZIxAxfeibymMiaAng/640?wx_fmt=jpeg)

Wing Relay 是一款专为开发者和网络研究人员设计的轻量级网络调试工具应用，以"轻盈、精准、兼容"为核心设计理念。该应用旨在帮助用户快速连接和管理各类主流抓包调试工具，包括 Reqable、ProxyPin、Proxyman、Whistle、Burp Suite、Yakit、Charles 和 mitmproxy 等，无需繁琐的手动配置即可实现一键连接，大幅提升网络调试效率。

在功能设计上，Wing Relay 提供了 HTTP/SOCK5 代理服务，支持扫码连接功能（兼容 Reqable 和 ProxyPin），并集成了证书安装与管理模块，确保 HTTPS 流量能够正常抓取与分析。应用还配备了快速连接开关和智能连通性检测机制，可每 5 秒自动检测服务器连接状态，当连接异常时自动切换至本机物理网卡发出流量，保证设备网络访问的连续性。

Wing Relay 采用现代化深色主题界面设计，界面简洁直观，操作逻辑清晰。底部导航栏集成了主页、连接按钮和设置三大核心功能入口，用户可轻松在不同功能模块间切换。凭借其小巧的安装包体积（仅约 5.8MB）和流畅的操作体验，Wing Relay 能够稳定支撑各类复杂网络场景的调试需求，是移动端网络调试的得力助手。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpBE6RibHWWxrhgBSNIoQSJkqn7y7qznqZnU5icKQF23sVdlXBB13Y9WVg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpXqwjVPZWiboHHSfq9N0KibNLm6AWMibcxHQJvPuXYibrL0Ra4RyULWyWRA/640?wx_fmt=jpeg&from=appmsg)

1.手机端开启个人热点供电脑连接

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgptqvIdx4SyxrlicIlcUlxE3aQC5EH8UpkqxV9G7PSJdJXJAO7TMJ9Npw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpicicfe93JRanicU9cTx3WJvCF6MHzgWMO9ZnGAJp28ibR5pKy7kdwBQqng/640?wx_fmt=png&from=appmsg)

获取电脑目前的ip

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpI6m0dduFf8JcKhGCEqoAwTEhhHnaRyicNsGatoZqhQSnyXoibtBK4zzA/640?wx_fmt=png&from=appmsg)

2.分别在Yakit和Burp Suite中设置监听

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpXknqo2qNcN70fDCQwlMDcibPMpRB0d4UgAESnfJdU6P9wryBBXoE0YA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpxEPpNqo4VE6TP7nMluXdeL4Y8yVBTPfYQKM1w7roUJzty8W0IQFZBw/640?wx_fmt=png&from=appmsg)

3.手机端安装Yakit和Burp Suite的证书

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR13hYTz9I157fSSwWQbfiazgp1JT7tK7icxlHOOnshF3fmicIwNAqkn4gSoeficeRWlbN3D8oCJwlLRWtA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpcOLxSvM9VOAjFjt3xvZhUY8MLWcYPiciclOd1PkOgslUCQYDvcopP9GA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpC6RNu4eDQyLicHuRfG5VFRlXqL9xibemhpJXeEpUIkOwYJw9tongwQ5A/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpzHTcpOk5lavLNfbDoIv8XKn2YkMllicQiakPacrfKfZlE73YiaZfkhVibg/640?wx_fmt=jpeg&from=appmsg)

4.使用Wing Relay配置代理地址

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgp90VegI4qIywIH07Sp1uMLmCFvUX1QQzuXuA8SMoGWI9oJ1rbegYLKw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgp6Xic4dbcI5It60yejXtzzhfMbnKeN5q7w02G1IIlYpRemzEGDIsmm0A/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpyyxibo9O5FeSjX1AObjuDAJEtzbEHAd3P6tqQX1Wt7O85VbJSTfmZCA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgp2m5kl6P3WD00adibGBSP9BRq3cHWKZ0oicDzC2nNzesUbia8ictqicmFL0w/640?wx_fmt=jpeg&from=appmsg)

5.打开软件抓包即可，比如我们测试一下活着么这款软件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpLCHGG03bOiaicBQowV5omiaslagQSOOY5gD8gbgtcia8eXVUN9icR7ovzdw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XB8gUH3cR13hYTz9I157fSSwWQbfiazgp0gKE768NSw664CxdqahpT2sDSrdYIyKwMsn8NREbibJyko1wMUUVF7g/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpAsojLhS8YXv5CsLcbPic4L72H03bsFUWJZ7icM6yL2J2GfEFTbnqzLpA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XB8gUH3cR13hYTz9I157fSSwWQbfiazgpBFz21h7L6twS73eY1zbS0lficPIzSCWAs1zziaKnSQNedgoewbibCCTSQ/640?wx_fmt=png&from=appmsg)

6.重要提醒：务必在授权情况下进行测试，未授权测试均为违法犯罪，违法必行拘，犯罪必坐牢！

预览时标签不可点

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