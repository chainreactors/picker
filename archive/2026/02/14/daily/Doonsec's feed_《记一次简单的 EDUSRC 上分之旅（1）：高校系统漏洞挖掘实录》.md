---
title: 《记一次简单的 EDUSRC 上分之旅（1）：高校系统漏洞挖掘实录》
url: https://mp.weixin.qq.com/s/INNMO2KV7dRZubeLGsSVJw
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:24:53.062522
---

# 《记一次简单的 EDUSRC 上分之旅（1）：高校系统漏洞挖掘实录》

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VwNll4FsBV53h4TsbhCTcsNELL5sPgWibDmCxy9OhA66XKdtSaPFf1lZXicA0PjNN5ha2H27Nib8W16kvbv3Aa99cYCSNhgSFYTAdiaaMGAHKibs/0?wx_fmt=jpeg)

# 《记一次简单的 EDUSRC 上分之旅（1）：高校系统漏洞挖掘实录》

原创

陌上ms
陌上ms

陌上ms

![]()

在小说阅读器中沉浸阅读

## 郑重说明

本公众号文章内容均为作者日常学习与经验积累所得，仅供学习交流使用。若需转载，请联系作者取得授权。文中涉及的网络安全相关内容，**仅限在合法授权范围内进行测试与研究**，严禁用于任何商业或非法用途。

任何未经授权的测试行为所导致的后果，均由行为人自行承担，与作者本人及本公众号无关。

正文Action

# 漏洞描述1：密码重置校验逻辑漏洞

前提：已获取登录凭证进入目标系统后台。

访问站点url，进入大学SSO统一认证系统。

进入后台功能模块，在子模块**质量工程系统**中发现密码重置校验逻辑漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV71Q7eceib2arziaKYeo5p6TD2cT8U9172TU0vjFicX7IUWiciasBoiazIytc3zUYjVEAGApsu85uDzPaibicxsHxro8hqpumW2yLVugfw/640?wx_fmt=png&from=appmsg)

进入里面的质量工程系统，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VwNll4FsBV7Lf0QfiblHrJ0PtREWLRB5lyIwZpHYibwiaiaCatxBN4hBagiawKltiaTnEiciaocrNb4IhRWtXCiaJKQjvmjjMTlEibA0d6EPolQLQkeCs/640?wx_fmt=png&from=appmsg)

在该系统密码重置页面，输入管理员账号**admin**，并在姓名、工号、身份证号校验栏均填写**admin**相关占位符，点击下一步，并进行抓包，

![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV5iaO9wW8vfjBa2qDC7iazZFgyGibhGRc0icDsLh8Q0IRepAGTh3BS5oqa3UomtKgl2N6Nezl4tv9mfNnFJq8lY6FiaXIHoEZrWFEiaM/640?wx_fmt=png&from=appmsg)

正常获取请求包及响应包如下：

![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV593VTgEKwRYKOkPvQ6rrEUkdjHaZGwSnlf9SlK8Y5aAZF3aGhPGjiaIAdWRPibPjibibR6x8OqqZTUIb49Kq82VWwTmL6QkJSCAoQ/640?wx_fmt=png&from=appmsg)

更改响应包false为true，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VwNll4FsBV5NhxL8cDnTey9HulENEKR1QM7Hib2UkJGYuE11JH1ibhByxXCRx5UvicmJIwr32f0DsnDicd8Nf12KEKjibmG3j0InVmEXQTw0ooss/640?wx_fmt=png&from=appmsg)

可直接跳过系统一级身份核验环节，进入密码重置页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VwNll4FsBV7ZIWbKcWNS5Wdrjic5tUDwDqnb3icRnapQ1xvjKMpRQA8SIVgKtRRe11l28ueHr5icBKF1DVMc8nLs1Ua66VqbImBb5GFYBibiaTp4/640?wx_fmt=png&from=appmsg)

在密码重置页面设置密码为**admin**，

![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV5dIaiajPoHkbX0v53kIeWoUE4MD3nIBPKNGgBOsE2t9yWwZuzXTDNNjhMLhoF6gHFskyOFIJGJTv2zDlPC60fByt1hS9cHVsHs/640?wx_fmt=png&from=appmsg)

完成密码修改后，使用 **admin/admin**账号密码可成功重新登录系统。

此刻我可以通过修改返回包跳过身份验证，实现任意用户修改密码（知道账号或者知道账号的组成规律）

![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV49RxwXPDhRP4c5vl4ljcHlEqt1aL5X6Q500eS75CDqfTVhH95uCdrQVaVdvJcxfSP40cnSyQS04ickTFA3IZYicZ0DbwVwJFjxA/640?wx_fmt=png&from=appmsg)

进入系统用户管理模块后，发现可查看校内**2135 个**教职工账号信息，且具备账号密码初始化、账号删除等操作权限，在这一步其实也实现了真正的任意用户修改密码了。

![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV6urQdXcgF1U2SibtLYTicYMwC1bxMGKDk3yMF14Kpq1h10R7sAE1UiaGUB1GHnNkOFAuWpfHEb1Z5unEMpzNdicuHQVRibCicPnGMUg/640?wx_fmt=png&from=appmsg)

漏洞描述2：响应包中身份证号未脱敏

点击历史数据，并查看历史包，

![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV4SHBypGwqMbIPqSMLLX7EPEmTpCWtXbHUuIFKPOKs4J2R08l6IvODaoRUlvY9nWEA5pD3KwIX2v2ibyc6vvuhibqcbDYUExVvYs/640?wx_fmt=png&from=appmsg)

将此包发送到repeater，发现**HTTP 响应包**中明文包含**10 条**教职工身份证号码信息。

![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV5TZaFxeHTSnz8IxmH4XMQOKibKzN7WdMHGVW8icTJFaDc0bO25sHr2IyADibSdiajnEibiaetfLiaHatT9GTm7dFMns7ribP9R89EnFOY/640?wx_fmt=png&from=appmsg)

历史数据功能点，一页10条身份证，共50页，差不多500条身份证泄露（其实在响应包中的totalCount字段也有体现）。

在项目申请管理功能点泄露了354条；

在项目审核推荐泄露了340条；

在立项设置管理泄露了330条；

在项目过程材料泄露了500条；

......

......

总结：该系统共**8 处**功能模块存在身份证信息泄露漏洞，累计泄露教职工身份证信息**4370 余条**，所有敏感信息均在 HTTP 响应包中明文传输，未做加密、脱敏处理。

漏洞描述3：弱口令

弱口令永远的神！！！

进入多媒体平台，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VwNll4FsBV48UMKrua3OnPfXibibV5372iaCffrVG8Daia0esWjtfNZk3V7uDibZcZXO8FtLBLHFF0icN8RScXrtmGLFpLia7sTcfbcr5aKQkW6FdU/640?wx_fmt=png&from=appmsg)

选择教师，admin/admin直接进入，

![](https://mmbiz.qpic.cn/mmbiz_png/VwNll4FsBV6WsTJ1UkN6xfytgvEmou9Akd2X8WES6lqB4cCqIPpEiaNfo6pJ7av1h4p54pZRQUFnXsmxprQTevNRfxickLwJZuEmEu5Cr3VTg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VwNll4FsBV53gtiam0xZyYABUc30MNzTj3uO7dysmWxhc1ru8f6bWH50WuQz7fBibOsHALIocCKJ6zgtyGnCW3Odq8s2Sm5ffJKONXNAibiao4o/640?wx_fmt=png&from=appmsg)

发现后台包含试卷管理、试题管理等敏感功能，存在重大安全隐患。相关漏洞已报送 EDUSRC，完成合规处置并退场。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Vic8YTtzzHTC9pEGUNNzb0fyTKKLticVzN4DqO1g50Lzc4JibnwFic5pibcmrP4OaC23icxB2d2Ff16jKP2fR5C10ryw/0?wx_fmt=png)

陌上ms

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Vic8YTtzzHTC9pEGUNNzb0fyTKKLticVzN4DqO1g50Lzc4JibnwFic5pibcmrP4OaC23icxB2d2Ff16jKP2fR5C10ryw/0?wx_fmt=png)

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