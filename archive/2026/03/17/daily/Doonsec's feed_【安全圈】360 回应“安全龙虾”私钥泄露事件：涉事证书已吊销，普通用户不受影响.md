---
title: 【安全圈】360 回应“安全龙虾”私钥泄露事件：涉事证书已吊销，普通用户不受影响
url: https://mp.weixin.qq.com/s/VghXRU9zzNRTCoQ_eKXrDQ
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:19:10.237418
---

# 【安全圈】360 回应“安全龙虾”私钥泄露事件：涉事证书已吊销，普通用户不受影响

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHpWCBptbFqkl6LGcVcNlCSYibVkGiaKCfHDbG4bUia4VWSTwdnJnMVrLWS0D720SpiaiccLpQoOuJo62dJVGicmiaDURgewBWcRFRCdU/0?wx_fmt=jpeg)

# 【安全圈】360 回应“安全龙虾”私钥泄露事件：涉事证书已吊销，普通用户不受影响

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

数据泄露

昨日有网友发现“360 安全龙虾”安装包中包含了属于 360 公司内部的 SSL 私钥与证书。该私钥对应域名为 \*.myclaw.360.cn，为通配符证书，可作用于该域名下的全部子站点。

针对这一安全疏漏，360 公司回应第一财经称，已第一时间对涉事证书进行了吊销处理。

360 方面表示，此次问题源于发布环节的失误，导致内部域名的网站证书被意外打包进安装包。问题发现后，公司已立即采取应急措施，完成对涉事证书的吊销操作，从技术层面阻断了攻击者利用该私钥伪造服务器、劫持流量的可能。目前该证书已经失效，从技术层面阻断了被利用来伪造服务器或劫持流量的可能性，因此普通用户不会因此受到影响。

据官方介绍，“360 安全龙虾”的界面采用了定制版浏览器，其调用地址涉及对本地服务的 HTTPS 加密连接。

有技术分析指出，通常情况下，处理此类本地连接的正确方式应是使用自签名证书或采用 HTTP 明文访问，而直接将包含私钥的网站证书置于本地环境中，虽能实现连接目的，但直接导致了密钥的泄露。360 方面将此归因于发布环节的失误，并表示已完成应急处理。

***END***

阅读推荐

[【安全圈】央视曝光“AI伪造人脸”大案：5万多条动态人脸视频被批量合成，冒充本人注册账号](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074758&idx=1&sn=7af05da7b8d43824113f474c308dc11e&scene=21#wechat_redirect)

[【安全圈】FBI 寻找被用于传播恶意软件的 Steam 游戏受害者](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074758&idx=2&sn=380176f5ead90fa27dbb4b3ab3077460&scene=21#wechat_redirect)

[【安全圈】星巴克数据泄露事件波及员工](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074758&idx=3&sn=50918cdf1bcb925bc8994d666b16dbb7&scene=21#wechat_redirect)

[【安全圈】两会网络安全最强音：2026年政府工作报告重点解读](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074689&idx=1&sn=1a33c2a4ba65ccb09812490c10156d2d&scene=21#wechat_redirect)

[【安全圈】紧急预警！Chrome再曝两个高危漏洞已被在野利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074689&idx=2&sn=df039d7dd8bb90f3e37e7590c242a92e&scene=21#wechat_redirect)

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