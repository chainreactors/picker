---
title: 反华坐实！为了监控中国人使用 Claude，Anthropic塞了个“间谍软件”！马斯克：你的人工智尤其仇恨中国人
url: https://mp.weixin.qq.com/s/kutrfrhng13cgpTpk0hAKg
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:52:02.925361
---

# 反华坐实！为了监控中国人使用 Claude，Anthropic塞了个“间谍软件”！马斯克：你的人工智尤其仇恨中国人

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicL5b5GJQ7hsmicHva2RiaSuXiba9Fmh6zAyPpCITItZticR2fZicH6XW3jBpic5PxEpstcCiaCWm10ZFZER9ZvBLOOW6X6mbMNib3iczica0/0?wx_fmt=jpeg)

# 反华坐实！为了监控中国人使用 Claude，Anthropic塞了个“间谍软件”！马斯克：你的人工智尤其仇恨中国人

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

不少程序员日常用代理中转AI工具，最近发现新版Claude Code一识别代理就直接卡死。

有开发者一气之下逆向拆解程序，挖出一段藏了整整三个月的隐秘代码“间谍软件后门”，官方更新日志里对此只字不提。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKYrOrhGVemPIjiadx05PtQ2am3pYnlatpFal3eR6OL3ToUXhdsXcI5BIFkeFY2EqlzI3ribCKNKAETcBl4ibjq69LDDMtAeTb3qs/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIacPL00LA5bgTibRLg6RbxLGHm2c0WJbp8GFJWdlFwCzdzCTz712wn2iazYPr4eIBdP7icQ2jHUKkKWC7jR2icXy1kzDlmR9mOFMQ/640?wx_fmt=jpeg)

01、开发者逆向实锤，隐形后门潜伏三个月

这套代码手段堪比木马：

用病毒常用的XOR加密规避安全软件扫描，内置代理域名黑名单。

最隐蔽的是靠肉眼看不出的Unicode特殊字符、日期符号改动，悄悄向后台上传用户地区、代理信息，全程没有任何弹窗提示。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicI6nLmJPBhY6IJGnURkZlzgOS01yC3R621QAH75W8sgPsgjIhqEyENCxwzV2zSRDS3f1UJCqPuLaZ5W8j0YtmxE61Kiavx691hk/640?wx_fmt=jpeg)

涉及中国Shanghai等城市的源码

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJAEsOThGJvNvC6wha1cjZ0aOGDwhpQs3l0bHhHBC9AxjpAkL5gt6IqjS2x62JxLGwpeicunV3JvYefV6havtlyLg9vT8PBEHmk/640?wx_fmt=jpeg)

源码里针对中国的中文日期设置

02、

防模型蒸馏操作，却踩中隐私红线

面对外界质疑，Anthropic解释代码是3月上线的实验功能，初衷是防止账号倒卖、避免模型被蒸馏窃取。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLunBGy8tf10uv8p0zoenrFEJ5CRVP0XRP7bcxfEApFoBlWwgusfbyT1DOT44hVWnHtKDlZZrenNkHAEriaYRVHo2SR4tLyFFcw/640?wx_fmt=jpeg)

但这套操作争议拉满：

一边标榜AI安全透明，

一边在本地工具预埋静默上报逻辑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJwjKvcoNk15ktpLm1lt9iaiaPWdyy2ibgvuzgL6HJIiaAuIdqStSEjh45snSicicwEWiaRlAGJwSLs232ibZHJMOonYOJlqTmjFlRQXJU/640?wx_fmt=jpeg)

懂技术的人能轻松绕过限制，最后受风控、泄露使用痕迹的只有普通开发者。

另外消息透露，Anthropic下一代大模型Fable 5会上线实名分区额度管控，就算放开地域限制，也未必能正常使用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLNguDA8SxSQ381pIrPq35CJBjnibka1p6YLCYlE2reWYZhSJNwrdwy9EGhf3yVL3l0ltpDC6HwlDaMGf8E0GUnyVOa4BJST4Uo/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicK0EXFghARmgGKhAaULCTIaOo85jcz3tWBMveamGicXnTBUGSjcGSBTBfWPJHcf6v44pvRpOaSYbvzdDJdaqTmnM79V3OaNP9UY/640?wx_fmt=jpeg)

03、

官方火速补救，附上稳定使用小技巧

丑闻曝光后，Claude Code负责人立刻出面回应，已经提交修复代码，次日新版本会彻底删除整套监测程序。

不少网友吐槽，如果没被开发者扒出漏洞，这段后门会一直悄悄运行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJh4ZHv5Jtmj6eE3kfeD5wkIdm2fN89hweaVuYwv0dezaGdVCRLR9qo47reOhMF2EqIC0BAthZhsW4HvHUR1BZFQH6GF96JfsQ/640?wx_fmt=jpeg)

分享两个实用避坑方法：

统一本地时区、支付地区与IP归属；

预算充足可远程海外实体机开发，大幅降低触发风控、工具异常的概率。

04

马斯克评论

“你的人工智能仇恨白人和亚洲人，尤其是中国人、异性恋者和男性。这是厌世邪恶的行为。必须纠正。
坦白说，我觉得你根本无法避免“人本主义”最终演变成“厌世主义”这种不可避免的讽刺。你选择这个名字的时候，就已经注定了这种命运。
风之名。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicL7vq1OAev8rkibZME0BSfwlEVFz7JAXRibdIA1DbOFpptSpMibuwrYmsCcOW4N7ricLS7M3zdq8ml3v6boBQ3fSQfXCAZMGlicibwFE/640?wx_fmt=jpeg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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