---
title: 记录一下如何批量进行ICP备案查询
url: https://mp.weixin.qq.com/s/MUEvwbcbCBc1Hl3MVSQ-Kw
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:05:51.916093
---

# 记录一下如何批量进行ICP备案查询

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/F4N4AId99XfhMIA3ibVFEYMfqr5Dw0hLba3kSjpesSmlXXiaJLpeTZ09fQj9kIHW9GSqNzQXDsewSch5BOjr02NhpGOwdN73zMLxicxgGiagz1U/0?wx_fmt=jpeg)

# 记录一下如何批量进行ICP备案查询

原创

小帅安全
小帅安全

小帅安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责申明**

```
本公众号“小帅安全”旨在分享网络安全领域的相关知识，仅限于学习和研究之用。本公众号并不鼓励或支持任何非法活动。本公众号中提供的所有内容都是基于作者的经验和知识，并仅代表作者个人的观点和意见。这些观点和意见仅供参考，不构成任何形式的承诺或保证。本公众号不对任何人因使用或依赖本公众号提供的信息、工具或技术所造成的任何损失或伤害负责。本公众号提供的技术和工具仅限于学习和研究之用，不得用于非法活动。任何非法活动均与本公众号的立场和政策相违背，并将依法承担法律责任。本公众号不对使用本公众号提供的工具和技术所造成的任何直接或间接损失负责。使用者必须自行承担使用风险，同时对自己的行为负全部责任。本公众号保留随时修改或补充免责声明的权利，而不需事先通知。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xf2wibr0HBDdCyUKwjT9Z3dibaDKmVFGBEIw2OsfyK5n9aSbwr2YicOEwSNaXziaBiat4pZVp9czEkqbvZrBZSgtG6Dd1froYPbhWmw/640?wx_fmt=png&from=appmsg)

**点击蓝字 关注我们**

**1**

事情开始是这样的，公司给我一张图片让我收集ICP备案信息，如果有域名还要解析后的IP信息。

我一看，这几十个，我如果手动一个个弄，那得弄到什么时候去了。

最后是找到了ICP备案批量查询的工具。https://github.com/fasnow/fine/releases

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xc1Kqich1A1vlulcTcZPPPkAksOicWlMfBuhMzIPibQdmrdlYrNia43feictyJwNzEuob1W41RHPDAC57KFx98ky6L0W8ib5YpibSskhY/640?wx_fmt=png&from=appmsg)

从头开始，记录一下每一步的配置。

先下载好这个fine工具

https://github.com/fasnow/fine/releases

我这里就配置了fofa和hunter的

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XfOVhgyFuOE4qVga6fVVudQv3YvkO7jxOfEekExZyNswN2yUibmx8aQoJIWBEq9ficpOhe3exHrTNfOa8icuqgBMrdPVqWZ44q1VA/640?wx_fmt=png&from=appmsg)

大家应该都会配置，不过还是放一张图片防止有些师傅可能不太清楚

https://hunter.qianxin.com/home/myInfo

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XdYJUbYdnibfPclEgicq8OibybwECdb6pgvqJfbNbABIPX0cE9R1QN2gcKHemzju2N9xNjL6rr42SzX5CAkjseMTPM607zalgsDXg/640?wx_fmt=png&from=appmsg)

https://fofa.info/userInfo

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XdPWFVxtlst4Ogglh5CPwUE27pibUf8UnF7YiaOCnoxKfpI1L6p8EC2CTAibv3KMy9FYVqpG7TchiciaiadRryrmWic94zJrvUia1mKPls/640?wx_fmt=png&from=appmsg)

然后配好爱企查和天眼查，还需要配置一个代理池

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XdW2mLKbSko8W3sVf0GVoibYibq24UXiapQty8Cf7tKSsMichbhugtCEFic2WQ1dcITC0NA91rIFyYxzqK5BrDPCpK6hBeYXo6jNVe0/640?wx_fmt=png&from=appmsg)

先看天眼查，不管你是直接在网络请求里面获取还是使用cookie editor插件获取都可以，需要的都是auth\_token这个参数的值

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XdzUVsIQMyO8hqMXjS0ks3WlFvDBybFK4t49w7iamZfQ9FU7Nvt9ZXCPDMEMicibwqtmzx29YeoO4EHwg7N5N8cjpKlXeNUwibUEEY/640?wx_fmt=png&from=appmsg)

再看爱企查

把全部的cookie复制下来

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XehkGISvE8D8NMD7nsAackuu81qzkEiaKojsoUFNtg6NhvohoEJQj9M680t7KHndQicgibPtcmnP0d4A8TwM2kFRljmHk395zicx6w/640?wx_fmt=png&from=appmsg)

再看代理池

使用这个工具

https://github.com/thinkoaa/Deadpool

下载下来以后，编辑配置

填好key，编辑switch参数的值为open,记得保存一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xe2b5tUfZ1r2uxQz0MIicrKgNA65oe12H7yEDTPCXkxF6soySnqia52GW3Apdib1WCDOO00n3vBFSuCGZTzicbywK3g1QPhgMQdVeg/640?wx_fmt=png&from=appmsg)

首先看到ICP里面的设置，点开以后，复制下面给出的python代码，在本地新建一个文件，然后运行这个脚本，将给出的地址放进OCR URL里面就行

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99Xdn5Kw5SR91VxHSO1JIibKZoqIwfL3wDiaqmpEJWpJJhDg8Hj5BWC4V8qPN8NTB75C8ibyTAuickiaD2unX5zf4Pd4UfFhIJ0OYEIvw/640?wx_fmt=png&from=appmsg)

缺少什么模块就pip install安装一下就好了

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XcrAv6OSU7WIIhJzibKvpwMLELOY2lwoWxrbP1bqywFhsM9G42Fs7g3hOXibvMN3JXVwl0zpB7Op7j1jqdq5JFyxA7JvDPUk6FBg/640?wx_fmt=png&from=appmsg)

先单个查询，检查一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XfpciaffmNXyibDTZ6sgrzPsDKM3GvBEpX9lSSSGREDhWpr31vrb5770mO0YceaKQZv9nEU2VFb7iaU680EiaOqgWsSZxDYbXWLib9E/640?wx_fmt=png&from=appmsg)

没问题

选择批量查询

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99Xdib9AQSnpv6Uun4bkmpaj8fia9Du8SPyibIWYxIdAsBn2bZGqhXArdvpib4ICLCKWunIqOaFcNgHaIuehiaJbMQEuZPwS4ywQbdrfE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XcPJicicUerHOH4qVibF8h5zGaVP30T4ItxzcnKwicvFsf63DB0TBtSqPpJoNoqj6NUUB3M7lVpQicTCtRWXFz6ibooXBiaGAlTSCD4NA/640?wx_fmt=png&from=appmsg)

基本就没有什么问题了。

获取更多工具和实战技巧

关注 小帅安全

**往期推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99XeqrffLgRnnnh9ImV3J4pZWGrKIIFXia91nm5ibNynsoJHBgxiaGlgPWk2uXDJRZQDicVH2icjHo2rCIQ2DN7raadjIEd1DIM2slicGM/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483962&idx=1&sn=ea2a00b7fa821b99422e4d893ff43cab&scene=21#wechat_redirect)

用户名/昵称内容注入漏洞

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99XcPAHeE5c9M5ZC1tUJ61B8W4HrbfCh3nRmfPJKNPicLbaABsbCbJKFI3n9GeDp89ap3a4wiamLnuSibzLXxU9aQcvYdC7NqOsVkQU/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483947&idx=1&sn=5968556dc7169ee862c3842981a3a198&scene=21#wechat_redirect)

最近捡漏的一个验证码相关的实战案例分享

[![](https://mmbiz.qpic.cn/mmbiz_png/F4N4AId99Xd7kwlLwpEbUGYjxibDp2xxTrOuEZQSnenPiaBSd4olCXOGlAxfFXCq1V2nnN7o3KX2akAQ4qqUhrpA5Jib4hwvzImf3gWS6WzPCI/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483882&idx=1&sn=c3203a266955b29770706abc96f5e816&scene=21#wechat_redirect)

微信小程序反编译工具推荐

[![](https://mmbiz.qpic.cn/mmbiz_jpg/F4N4AId99XecMMfVIIWvT0l3NndtwrpkQ2dXzEZct8PQ0gicgLoJKYhT8j25vm44QXibBZWgfzTb0bXAEyUmoLibYHbW7XebprUr19BRwwaIEs/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzY5MTE3ODE3Ng==&mid=2247483745&idx=1&sn=210b474b3666c4b90564400c388ad46a&scene=21#wechat_redirect)

EDU挖到的简单满分漏洞之Vue框架实战加资产收集语法

如果文章对你有帮助，欢迎一键三连，点赞，关注加转发，后续我会更新更多优质文章。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/F4N4AId99XdIraiaSOaLDHfOvSqX3xia3zqIlbzVgibKZ4kxLiaVhxE55qKo61MM0wfkpobTd6N6l0ibcbCOKic27I7ELabB8PsxPWsN14o7FsJPg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/F4N4AId99Xf09ZC9xkJsEquQCRDf4BG7z1mdACUO9r5CLbPDOkGFqUgetyB3BbTamwRpGicHXm0CibYhQOEq6R3GwGj0H0YR7cFCAiacXIJA9w/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/F4N4AId99XcQUYQ67ITwEyEnKeSgtiaia6JfdO6jZiaW6uK4Gj15xicyqlSQNh5ao93lSFknaaf4sAebJ9qoibuicEToq9YVj8eY28vKrtu3TObXQ/640?wx_fmt=gif&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/F4N4AId99Xd9Nbt3OIoHdW8397TLDEpw56RIGjuvl0yibyiaF509zluBKQnk8pFFa7WiaAEebAyEvyibicu7ddTIkcMWtvODFZJuAbo4HQrOticAw/0?wx_fmt=png)

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