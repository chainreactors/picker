---
title: 【接口漏洞第三章第三节】API漏洞挖掘实录：从GET到PATCH，我是如何实现“0元购”的
url: https://mp.weixin.qq.com/s/M76PZ6lwInelr_bIiRJUBQ
source: Doonsec's feed
date: 2026-01-07
fetch_date: 2026-01-08T03:27:34.481315
---

# 【接口漏洞第三章第三节】API漏洞挖掘实录：从GET到PATCH，我是如何实现“0元购”的

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q1jq02WtWR51BHPvYiapklSTfLDhnEKMx68kwf9R6X8cbDu1VWtO9Uo5JFib6PJg01pr1XZVC7XgUdw/0?wx_fmt=jpeg)

# 【接口漏洞第三章第三节】API漏洞挖掘实录：从GET到PATCH，我是如何实现“0元购”的

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于升斗安全
，作者升斗安全XiuXiu

![](http://wx.qlogo.cn/mmhead/2kpMNDYsSfCCBCENh6LOmFVgC9ciaIhQ4RHwsulEqe0kfcia0rFxsfQH0PLichNS01WIvWvHRpfPM4/0)

**升斗安全**
.

升斗安全：聚焦网安技术、漏洞挖掘与职业成长。 不止于漏洞原理，更专注实战利用。这里是关于白帽技术、赏金猎人与职业破局的硬核分享地。想提升你的“挖洞”功力？关注我们就对了。

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

前面章节中，我们已经对api接口的请求方法（method）和请求内容（content-type）有较深入的理解，今天我们就结合前面说的一些理论知识，来对某个存在api接口漏洞的系统进行实际的漏洞挖掘。

一般情况下，我们都先对系统进行登录并访问，然后对请求接口进行审查，看是否存在明显的/api 路径，在这个被测系统中，添加商品到购物车后，就会请求带 /api 的路径，具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q1jq02WtWR51BHPvYiapklSTU3EMT00vnSgicibJEcCyFoPh3eVQoNpHd847JrZYibcmjO3a74nMBuyNg/640?wx_fmt=png&from=appmsg)

从请求了该api接口后响应的内容来看，该接口应该是获取商品价格的一个查询接口，而且采用的是GET请求方法，前面章节有说到，关于api接口，不同的请求方法，对服务器的资源获取方式也会不一样，GET方法为获取价格 那其它方法会不会存在一些意想不到的漏洞？这就是一个值得我们测试验证的地方了

如上一节[【接口漏洞第三章第二节】解锁API漏洞宝藏：从请求方法与内容类型切入](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797672&idx=1&sn=e1a6901c64d6c7c1864fec8e92e32f81&scene=21#wechat_redirect)所说，通过intruder直接对请求方法进行验证。

发现遍历后，该api接口只有GET方法和PATCH方法是可以用的，但PATCH方法返回的400状态码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q1jq02WtWR51BHPvYiapklSTTsOQ9iceYpyv1fEEbiczOdJuHoJelCdUvzmMH2JgsG6rqobvCwkvDo2A/640?wx_fmt=png&from=appmsg)

在找到了api存在其他可用方法后（即使该方法的响应内容为非200的成功状态码）就可以进一步对这个方法进行研究了。

将该方法的请求发送至repeater中，并重放，虽然是返回400错误，但明显告知是因为content-type不对导致的，具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q1jq02WtWR51BHPvYiapklST85XZ2Yekowo8DwQcppthcYM5f6WfhjAgiczicWFDlaJQVYYBzrvbPtYQ/640?wx_fmt=png&from=appmsg)

根据提示，我们就可以进一步修改content-type为JSON格式，并添加相关参数后，就可以直接越权成功修改当前商品的价格了（因为PATCH方法的作用就是提交修改数据的常用方法）具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q1jq02WtWR51BHPvYiapklSTic04dYX0ODYqybibDpDxnicFoFDrGT7pkeibdzvqYDp5txZd72n44pTB8w/640?wx_fmt=png&from=appmsg)

然后再次使用GET方法来查看相同商品的价格，发现已经成功被修改为0元了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q1jq02WtWR51BHPvYiapklSTsVKonNoNNav8xKP7b27jWyFAgWV8O5Txo1mXJUzPpBOoCePZksMyicA/640?wx_fmt=png&from=appmsg)

至此，完整的一次利用api接口的不同请求方法导致的漏洞就演示完了。主要还是要多关注不同的请求方法，还有不同的content-type可能导致的一些后果的验证，以及要细心关注响应内容中的一些提示信息，那么，你也可以很轻松就发现系统的api接口漏洞。

关于api接口漏洞，后续还有很多内容，这边会继续循序渐进深入给大家呈现。感兴趣的小伙伴们记得点下关注咯~

如果觉得内容对你有帮助或启发，千万不要吝啬你的赞哈~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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