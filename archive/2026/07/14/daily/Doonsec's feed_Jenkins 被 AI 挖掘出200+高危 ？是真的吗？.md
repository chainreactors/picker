---
title: Jenkins 被 AI 挖掘出200+高危 ？是真的吗？
url: https://mp.weixin.qq.com/s/WBvUF-W2kH49zZDujG89fQ
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:44:06.943959
---

# Jenkins 被 AI 挖掘出200+高危 ？是真的吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IicMcDFtTOlNpXqbicyKMtlY3GacEEup3FibKNj7PVLX4QXibsa0KYqM1QicF7ObsZoDzt14iaR8glFoxqW3138TUup0KeXGUTDOQlJn9slwibPu5c/0?wx_fmt=jpeg)

# Jenkins 被 AI 挖掘出200+高危 ？是真的吗？

原创

棉花糖糖糖
棉花糖糖糖

棉花糖fans

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/1mtwZURvGTkCK3ZFyqYEyTwmaLo2YSMeibz3eeShkewiadS4oh0RBl1U7BTVeEscGQrEbjWKcQzGpJEFLwr4cFQw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)![]()![]()前言

大家好，这里是棉花糖，一个四年网安自由职业者，bdziyi.com的站长。

众所周知现在AI+安全的东西特别多，如雨后春笋，正好前段时间有个项目号称自己已挖掘N多高危0day，其中甚至包括Jenkins，被挖掘出200+的高危。

![](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMBux2JTSUqkqNfWeUQJMPr34wqEicyZMCmLJWxUibclsm16oAnMiaNoibMxe8xPEw30Ibt5HcTOcia1RCepz6dCvQwHAudmTPrAWls/640?wx_fmt=png&from=appmsg)

烂活下的恶臭

很多人看到数据吓昏过去，感觉世界药丸辣。

先别急，经过了解，该团队的人已经被AI替代大脑，幻觉代替思考。

该团队在这个项目之后，推出了一个新的平台，以saas方式提供测试，今天他们终于漏出了马脚，在该平台中，展示了他们审计maccms的成果。

![](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlOejfic8VaSFFvFhyYLjExnLKWEBtOu3n7LibH17ffRZV0GYblpTtfB4qAg7CpBz85vCVQpeic0geeic7DKTGP3lcXQDAialUvKSEE4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlO8uY3aCcMaDgmOhFic0uHHzjc9wQNicmxu11P9DibwaT9iby7Sk8fQ8kKfhzUP7WfyhJByKETrzuJFUZUVx3WFBgUfLgNm3LHs5Go/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IicMcDFtTOlPvNg1WBibOoicV2COdfEpYRF24h2F04UOmXXfTOzIdjYE9biatXbXMcyXlWNaMOWsU7FONyic6vc0xEqmIkfiay46nV2Piagh6SyiaYw/640?wx_fmt=png&from=appmsg)

这就是他们的垃圾产品判定严重/高危的标准，md5密文？严重！不可利用的链路？严重！先拿到数据库权限之后再sql注入？严重！

此类垃圾数据还有很多，不一一列举了，对这种垃圾数据，该团队的人解释为

![](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlM8k3xpVdjgwXGtNqFRtb2vLvlOC8DkiaFZ5ic2nhT6HLeUk1gLKsWdjZZaJicqGylWsYjvhPtQicepUyMiaSkaib9plo5Xgaq1icZ5bI/640?wx_fmt=png&from=appmsg)

哦不用在意他们说的是点星还是万破，因为这俩都一样是烂货。

可笑的是这个团队还分工明确，人数不少，据可靠消息，还在成都成立了公司

![](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlMCHialWFrr5HJ0T3AibB7B0xj0iawmtibfQEQlVMKZMIC5v6OELjePFQBfS5W3Wia8elufbQoKnToUUtZiaRia1gyISWJ87GneI7PoUw/640?wx_fmt=png&from=appmsg)

更恶心的是拿这种垃圾项目出来骗真rce：

![](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlNWo7lgNlViaIppSAgibH6micbGXqzNJkIg6rjIhk2Qw127tc0fZwiaDI71eiaoWjxaZAYlyicz87Pia8CPEhmu49eoc5HPKBmxMSF8eE/640?wx_fmt=png&from=appmsg)

还花钱找公众号打了广告（有的甚至没花钱，免费帮这种泔水打广告的）

![](https://mmbiz.qpic.cn/mmbiz_png/IicMcDFtTOlM0sR6gs3cmicZo43Ts5XmfxHPqdvkflhxT5pOQMFboEUgCj2e0yQ4jahyFus96U5xKFRNLnP2J2PPrVl3YGQO3SYJbCUMj6AnQ/640?wx_fmt=png&from=appmsg)

像这种AI一把梭扫个sink点就拿出来当亮点的东西，我想都不用想，后端肯定是扫到sink点后直接交由AI一把梭分析，不做验证不做判断，全信AI，我说白了，哪怕抄一抄呢？拿个真有点作用的开源项目AI二开抄一抄也不至于这么烂.....要骗甲方钱，要吸社区流量，好歹认真点啊？纯侮辱人智商是几个意思？

哦对了，希望之后做此类项目的可以先把他们的这些高危判断采集下来，作为AI欺骗、幻觉的案例，极其标准的反面教材。

最后

有时候真的不想浪费时间来发个文来喷这种东西，浪费我挖洞的时间，不过一想到好多垃圾项目正在让各位头昏脑胀，就觉得还是有必要喷一下。

本文这种傻缺只是非常明显的典型，像本文这个这么明显傻缺的项目不多，很多都伪装在专业的外皮下，大部分人不容易发现端倪，我只能说很多人做的AI渗透、审计工具，还不如模型厂商的原生agent一把梭来的效果好，擦亮眼睛吧兄弟们。

如果您对内网靶场、SRC靶场、WEB靶场、应急响应靶场、网安方案、资料文档、各种各样的网安工具、实用的在线功能、教程资源感兴趣，欢迎看看我的网站广告，包您心动：[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)

网络安全交流群请在公众号菜单栏点击找棉花糖，加棉花糖好友后发送“棉花糖fans”，邀请您进群，CISP全系列、国内外网安考证也可以在公众号菜单栏点击找棉花糖，微信联系哦，爱你😘，下篇文章再见

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lic4LrsB27nuZ7usswE4zOJmgMWo4EicjNNJ9wvlcs6icCnoMDcNOTMPC4JfLP4mEbgPgBnKHKkM7KKgh1cWQAqJA/0?wx_fmt=png)

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