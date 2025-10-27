---
title: 【安全圈】热门npm包被植入加密挖矿软件，感染目标涉及中国
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066835&idx=1&sn=d18006424cd216fae3e961831bf98f2e&chksm=f36e7853c419f1457f7acc42f4289b6ce9e45c7a0bb50f42709a993edb0c8be127b56299c122&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-24
fetch_date: 2025-10-06T19:40:35.927127
---

# 【安全圈】热门npm包被植入加密挖矿软件，感染目标涉及中国

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhpKyb65ASfBKicFJGuklJN9PYzavQHYz1ouMb5Z5m6M1Lbz3HhqnDUCsHfhKowRNuU7dCVEYibwTww/0?wx_fmt=jpeg)

# 【安全圈】热门npm包被植入加密挖矿软件，感染目标涉及中国

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

近日，有研究人员发现，一些热门的npm包遭到入侵，攻击者利用窃取到的令牌将带有加密挖矿恶意软件的版本发布到了官方包注册表中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhpKyb65ASfBKicFJGuklJN9VImQNKjYQNO1gEvsRHT4aaZZIVJd7uADMsEwogqichwkj4m6VkGsjQA/640?wx_fmt=jpeg&from=appmsg)

Rspack 的开发人员透露，他们的两个npm 包@rspack/core 和 @rspack/cli均被入侵。Rspack 被宣传为 webpack 的替代品，是一款用 Rust 编写的“高性能 JavaScript 打包工具”。最初由字节跳动开发，现在已经被阿里巴巴、亚马逊、 Discord 和微软等几家公司采用。受影响的两个包每周的下载量分别超过 30万次和 14.5万次，表明它们颇受开发人员欢迎。

对这两个库的恶意版本进行的分析显示，它们包含了调用远程服务器（“80.78.28[.]72”）的代码，用于传输敏感的配置信息，例如云服务凭据。同时它们还通过向“ipinfo[.]io/json”发出 HTTP GET 请求来收集 IP 地址和位置信息。为了取得性能和隐秘性的平衡，恶意加密挖矿活动还将CPU使用率限制在了75%。

值得注意的是，这种攻击还把感染范围限制在了特定一些国家，如中国、俄罗斯、中国香港、白俄罗斯和伊朗。攻击的最终目标是在安装这些包时，在受影响的 Linux 主机上触发 XMRig 加密货币挖矿软件的下载和执行。这一操作需通过“package.json”文件中指定的一个 postinstall 脚本来实现。

目前含有恶意软件的版本已被撤下，新发布了安全的1.18版本。此外，项目维护人员还表示，他们已经作废了所有现有的 npm 令牌和 GitHub 令牌，检查了代码库和 npm 包的权限，并审核了源代码是否存在潜在的漏洞，对令牌被窃取的根本原因进行了调查。

据悉，针对 Rspack的npm包的攻击还包含另一个名为Vant的npm 包，该包每周下载量超过 4.1 万次。Sonatype的研究人员表示，攻击者成功地将几个被感染的版本发布到了 npm 注册表中，包括 2.13.3 、2.13.4 、2.13.5 、3.6.13 、3.6.14 、3.6.15 、4.9.11 、4.9.12 、4.9.13 和4.9.14版本。目前，最新的安全版本4.9.15已发布，建议受影响的用户及时升级。

参考来源：Rspack npm Packages Compromised with Crypto Mining Malware in Supply Chain Attack

***END***

阅读推荐

[【安全圈】谷歌测试在Chrome中启用人工智能检测诈骗 当发现钓鱼网站时弹出警告](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=1&sn=dddcab37c43e140a04d10fdf74ccf0e4&scene=21#wechat_redirect)

[【安全圈】FortiWLM 曝关键漏洞，攻击者可获得管理员权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=2&sn=d36a351bfabba8d719c29fa871c22b3c&scene=21#wechat_redirect)

[【安全圈】Mozilla再次发文称禁止谷歌搜索向浏览器分成将威胁火狐等独立浏览器的生存](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=3&sn=5e35754a7884cd8ec8ef21319f9245ca&scene=21#wechat_redirect)

[【安全圈】罗马尼亚国民因 NetWalker 勒索软件攻击被判处 20 年监禁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066819&idx=4&sn=86f5fdfe10bdcdd67c657f5b8141121d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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