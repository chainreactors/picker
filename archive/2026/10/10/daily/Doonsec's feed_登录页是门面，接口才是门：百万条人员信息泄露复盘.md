---
title: 登录页是门面，接口才是门：百万条人员信息泄露复盘
url: https://mp.weixin.qq.com/s/u4WyVoEIOLAYl_7xK7Wppg
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:57:45.615302
---

# 登录页是门面，接口才是门：百万条人员信息泄露复盘

# 登录页是门面，接口才是门：百万条人员信息泄露复盘

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

这篇想告诉你的就一件事：登录页是门面，接口才是门。门面做得再规范，门没锁，数据就是敞开的——而门开着这件事，从登录页上一点都看不出来。背后却挂着一个不需要登录就能访问的查询接口。没有账号、没有凭证，一个 POST 请求，就能把库里百万条人员记录的姓名、身份证号、手机号、真人照片和 xx 全查出来。

本次渗透测试总计发现漏洞1个，其中高危漏洞1个，漏洞情况如下表：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 序号 | 系统名称 | 漏洞名称 | 漏洞数量 | 漏洞影响 | 漏洞级别 |
| 1 | https://xx.xx.xx.xx/basic\_element\_control/outSeaPersonRegister/pageRegisterNew | 接口未授权 | 1 | 攻击者可通过接口未授权可以获取到所有日期的xx的身份证，手机号，姓名，真人照片和xx等敏感信息。 | 高危 |

# 接口未授权

漏洞描述：

      通过接口未授权可以获取到所有日期的xx的身份证，手机号，姓名，真人照片和xx等敏感信息。

https://xx.xx.xx.xx/citywide/#/login

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1goTqickA2BzzulC8YlufYhIyFqXU2V8lSnOqrbtyBE1tdO8aV1l20piaoKBPvhxCrNhJVA6RMiauqyjOrBrUjeQPzh1A8YPLWx01Q/640?wx_fmt=png)

系统对外的入口只有一个登录页，看起来中规中矩。但登录页只是门面——前端页面能看到的数据，背后必然有接口在供数，而这些接口未必和登录框一样严格。

漏洞路径：

https://xx.xx.xx.xx/basic\_element\_control/outSeaPersonRegister/pageRegisterNew

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqC8CLpduyWsjqdS9RHwuyicVCWNd0MHjG4D80erjD1B2eWIwuSeo4hvpSSh8vGA9EY5FrxRH1j2BLFDFoCUFQmKgkJdmx2aibI0/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gosEJQ9yB0ibFDbJ7rz8Bqo0B052Xz67I19IRzPZZ9LMnHDyrwzRFPmzMlwt38iaTk5FhI8YGTr7gMGc4Bb7gDYvs18Pmf9Jomvg/640?wx_fmt=png)

从前端抓一遍请求，重点看哪些接口在没带鉴权凭证的情况下依然返回 200。上面这条请求就是答案：没有 Cookie、没有 Token、没有任何身份字段，服务端直接返回了 200 和完整数据。

Payload：

POST请求的json格式

https://xx.xx.xx.xx/basic\_element\_control/outSeaPersonRegister/pageRegisterNew

application/json

Fuzz接口所需的参数：

{

"ncommitte":null,

"pageSize":100,

"pages":1,

"exist":0,

"startTime":"2026-xx 00:00:00",

"endTime":"2026-xx 23:59:59",

"userName":"",

"idCard":"",

"userPhone":"",

"marineType":0

}

参数含义一目了然：startTime / endTime 控制时间范围，pageSize / pages 控制分页，userName / idCard / userPhone 还能按姓名、身份证号、手机号做精确筛选。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqpX78sox4NStSPFVpnpSOOQ38Hu8bqAvuc0tCTygQ9lcqv3rFExVfKQRR9x402kGcjDQPvtdRZdak2fXfDUPia6f6HjEKNwaYQ/640?wx_fmt=png&from=appmsg)

响应 code 200、msg 显示“查询成功”，data.records 展开就是一条条人员明细。

成功获取到2026年1月到2026年5月期间的xx万人左右的xx详细信息。包含身份证，姓名，手机号和真人相片等敏感信息。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpQwAAen8kRoGW4g9FyDQvS645y6NJFXuqunpECm87yd7JtiaSeB27c72o52rJNsFmJvoGu1n0eFbLZnPN06WyGA3NOerpWZxR4/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gozzUJWxRREec7zicZlw8avvfyMDcGKl8N3KQLv1oc4A7yWv6ic4eibG8atYHNsIHVYbM4Sur6FY2GdaQeGQTrzoYjpOngWN5kfhs/640?wx_fmt=png)

返回的 total 字段直接暴露了库里的数据总量。而且 pageSize 没有服务端上限——把它从 100 改成 1000，服务端照单全收，总页数直接缩到十分之一，搬走全量的成本又低了一个数量级。

前端接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gpP4KH9I4iacyibJTs7CqYzkib8hT3d39ibWcSeKMtckfNyn2es8cbMp44fLiaxXyykjmCyKxtRYBqY2EibQ6KBSr1ibqXxIFgnojtU0E/640?wx_fmt=png&from=appmsg)

https://xx.xx.xx.xx/citywide/#/vesselBoard

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1greKRBicZ2PxIqO5fISU2Xhnn8ndv283yictFh2vVaOTl2pdJiaW6Wyn2IRyyeagliaEK4yUz9AbAz8o5oeskiaRmyPODWoLcq9u9fU/640?wx_fmt=png)

前端看板上的人数统计，和接口返回的 total 完全一致——看板上的数字，就是这个未授权接口在喂。

xx人数查询页面。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gp10Z1iaUgiceuT9wWF10BZAWlvpwHooKuXFOcibHO9Oc7WpfhfYAG1HoCicXIT2Qon86ibicaSeDCkEMhbnHP4qU9iaTLnJpBcW1BdjA/640?wx_fmt=png)

人员明细列表里，头像、姓名、身份证号、手机号、xx、登记时间一应俱全，底部显示共 xx万条。这些数据本该登录之后才能看到。

修改日期为2020年到2026年至今为止最新的时间，可获取到xx万人左右的xx的所有身份证，手机号，姓名，真人照片和xx等敏感信息。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpGUNbzs708Ux5zlV4hoHktf5SiamPicQrwLaNJMhWdqic7bGOiaMhfucjsC7BZHVYT4vPBE0Ov2dA7eDTFmzvahNaUU0gLEsWgV4M/640?wx_fmt=png)

时间范围同样由客户端说了算：时间窗拉得越长，返回的 total 越大——想要多少数据，自己调参数就行。

xx人数查询页面。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gr1IoJbj4ejJRKjzobo2nVorukGib2azZGLpfC1wdgC0ic0jpsrfZBWXCklYUXVIy8XZ366ma0ZHdhYQNNeBAvzJLjN6LwPbtuIc/640?wx_fmt=png)

总结一下：这次测试里没有 SQL 注入、没有文件上传、没有复杂的攻击链，唯一的突破口就是这一个“忘了做鉴权”的查询接口。但恰恰是这种看起来技术含量最低的漏洞，代价最大——一个接口，就是 xx万条敏感个人信息。

对做安全测试的同学：接手一套系统，先把前端所有接口抓一遍，重点标出那些没带鉴权凭证却依然返回数据的接口——它们往往不在功能菜单里，但它们在数据层是敞开的。这类系统的数据越敏感，越不该把安全寄托在“没人知道接口地址”上——接口地址就写在前端代码里，谁都能看到。

如果这篇对你有用，欢迎点赞在看；你在实战里遇到过类似的“一个接口定胜负”的案例吗？评论区聊聊。

预览时标签不可点

修改于

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HezRQjNneVHy39103FjCvxFaZicO2OgEB05ZbBLwibDiaCTqDJNUHUCC9OXjVeiasG4ibOVR0dg284RCzVquVhvQ3xQ/0?wx_fmt=png)

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