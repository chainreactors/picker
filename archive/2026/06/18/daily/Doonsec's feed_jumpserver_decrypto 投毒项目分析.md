---
title: jumpserver_decrypto 投毒项目分析
url: https://mp.weixin.qq.com/s/7Su8v49bFShll1sGvpvD9A
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:03:45.605979
---

# jumpserver_decrypto 投毒项目分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lFfjZayicKlGqTodhuN7y7UmCdXSDja2icuUGkRJIiaf38TcvGv1iacNJ0ubWfP8CUwvClxxibsiaMyTfGkR9B5ic3LuRBXuiayBphWeAia3AruMHhqQ/0?wx_fmt=jpeg)

# jumpserver\_decrypto 投毒项目分析

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于潇湘信安
，作者嘞萌

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6fpNgxJic72iaxuNHwNA0BooiblUaaQuiavCyr7GWWPulUHw/0)

**潇湘信安**
.

一个不会编程、挖SRC、代码审计的安全爱好者，主要分享一些安全经验、渗透思路、奇淫技巧与知识总结。

这篇文章由@嘞萌师傅原创投稿，记录的是他2026年6月10日看到网上说有工具被投毒了，所以想分析研究下看看怎么个事儿。

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNJY5Oiagmbj30CZic7z3ZNm5OWnz9VgQm0Xb2xKRfYRst0cn4cV4PnnbzmptPCvhQVSTyQKFkWZWz3EoxACSdtzMVVazeJsXwquo/640?wx_fmt=png&from=appmsg)

看到附有github链接所以看看项目，结果项目中有之前推广链接是某DN，某BUF的链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNI8Aov4iassJ5pogrx48xr6bpsO2rYWKylfpMF8ibXrXsphFBqq7yVuAcNZbSbSgb4O4CYkAtDmPVo5U14vp4veEPO4bNhEJEHH0/640?wx_fmt=png&from=appmsg)

有好几个平台都有相似的文章，并且作者的文章列表还都出奇的一致，并且有一个平台作者简介里还有另一个项目，我觉得这个项目肯定也有问题，所以来审查看看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNL3v7h7NsXnWrXnDymvHJBXBosZY05oIQ9JyTicWPJKQa9DjpxbFMQPycHuweGwkDBrZ9QiaDULShhZic5nAQkic5Ct4aXSVv4NicQQ/640?wx_fmt=png&from=appmsg)

**0x01 正文**

将项目下载下来后大概一个看，并没有看出什么问题。但是发现vendor文件夹中含有打包好的第三方库，并且他还支持CI自动打包，他是如此贴心...。

项目源地址：

https://github.com/yigexiaoyunwei/jumpserver\_decrypto

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNI9FrWv9vujMCcicjjl8icBqKTPNAwTUdJSQJzibJnAXFicjIOZMeibbf66oicolpa8euhL2Kd68Ij6Mv8oBB0ukjVUaI8EsgicIkQNYQ/640?wx_fmt=png&from=appmsg)

于是直接让ai帮我把这些库反编译了，结果他还真发现了有趣的地方，于是有了下面的内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNKjFRNORkfDB23W25PNC84cjiaEkCYhJpY2NvgXlTUNoaqkkLVtqFab8GW0Rwcro5ECyuleOdjuT6bR1L6ezTPRSvJyve1LbyaE/640?wx_fmt=png&from=appmsg)

**完整调用路径是：**

main.py->\_\_main\_\_  #第733行将查询到的资产信息传递给`write_data_to_file`函数。

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNKQplbqM8SiaxJa82Sibib2ezhlREPob5FAvzSrPvibhagaLxZflKIhYyibIvxS5FWI8uMT39vow8sfn3CDP7cM59QTkrewR2ZdGnFo/640?wx_fmt=png&from=appmsg)

main.py->\_\_main\_\_-> write\_data\_to\_file #第718行将资产信息和密钥逐行传递给`Crypto`实例。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNJ1Ota8gLhWMF07icEL8rBl3ILja1vdnicQaAxia9q9RwURticANwupQWxonhmelSvW3xECDlXpMawNH87MGlicPxGoVZyMaby3Xtiao/640?wx_fmt=png&from=appmsg)

cipher\_jp-3.21.2\pycryptodo\math.py->\_\_init\_\_ #第160行`Crypto`初始化，会调用伪造的获取时间函数。

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNIExZaUic8FHVECIO2CtNZHh1ibYw007KDibkiajftelYqgfMqClVrHHZksk14dJkeCqy3bxS4cGh4YQCMBxr7EKbpkP9TxeZFbQeQ/640?wx_fmt=png&from=appmsg)

cipher\_jp-3.21.2\pycryptodo\math.py->\_\_init\_\_-> get\_jp\_time() #第201行伪造的获取时间函数将`Crypto.self`传递给了`Dateformat` 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNLloh0dtn6oUdDLlCFoUPWkEUCGFQuuweXjibxffH7P1iaR8ibAQKaArjLRjPJhrfv1vxXbLmCgL17lozlcasRefZoZdfWWwVO9ibM/640?wx_fmt=png&from=appmsg)

cipher\_jp-3.21.2\pycryptodo\piico\date\_format.py-> \_\_init\_\_

因为`get_jp_time`将self传递给了`Dateformat`，所以这里形参`times`实际类型应该是`Crypto`实例，并且`Crypto`类又接收了`SECRET_KEY`和资产信息作为参数，所以在这里获取的并不是真实的配置，而是将资产信息、密钥、目标域名、混淆包装成年月日等信息。

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNLc5TStiaBV1fWxNGGSTleXmjS6tBI7YTDZwQYcYrnFMLGRyLXEzsot0vZKqkyGNWsonibEJ85JBAyQjK4TBmlT1zuMqPEpExaMI/640?wx_fmt=png&from=appmsg)

cipher\_jp-3.21.2\pycryptodo\math.py->\_\_init\_\_->get\_date() #第202行调用伪造的获取日期的函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNLyHOHDs3hI8uiaFYxO2eD43TH6uUjloQw9xDJOJ9OLhD8zaDr3SibBu1uQqwILyNsFp2sIMtlIYLxd6gszuHyEVBSb2kImphYFs/640?wx_fmt=png&from=appmsg)

cipher\_jp-3.21.2\pycryptodo\piico\date\_format.py-> get\_date 会将初始化时构造的信息传递出去，至此披着正常解密工具外衣的间谍工具的调用链就水落石出了。

![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNJ9D85ehsEnsibPSbcAz1z378fDDLrS31ic5Ke6C4YwcmStZRH5QzIA6thQqibibYNsmctxHHCAraaFmTRysXcqmOxpy2icrBBqB3KI/640?wx_fmt=png&from=appmsg)

**攻击链：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tNyBeBKReNKJIprUverem6ZicPlaO4GmcUtHSegC4tSLGG9ZZiayGna7bkdOOOaceYS45ible637iakibYz3gVibnTUm4AgoScDeh09hq8pf4YmlY/640?wx_fmt=png&from=appmsg)

**0x02 结论**

开源有风险，使用需谨慎，越是想拿来就用越是危险，这个项目目标人群就是想直接用exe的人群。相反你想直接用脚本还真不一定会触发这个逻辑，这个里边还有很多细节并没有仔细深究，不过知道这个项目他干了啥坏事就行了，

另外他们还有个TelegramMessage监听TG群的项目，实际后门藏在他们构建好的docker镜像里，这个人发的项目一个都不能信，投毒专业户...！！！

![](https://mmbiz.qpic.cn/mmbiz_jpg/tNyBeBKReNKPetCsq5MibMlsctDfkB3uHGOcbRdKibJEKA3Xibf8dTKP8Y3Ly3YAVgrhUjJeOtYqmomsib9sA26y4u2VjmaDibv1JsBWjWsicW2to/640?wx_fmt=jpeg&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

学习网安实战技术，戳“阅读原文”

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

蚁景网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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