---
title: 【漏洞案例】越权之修改HTML+CE绕过签名校验
url: https://mp.weixin.qq.com/s/xTs0_sXjxuEtQP-jh9xoBA
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:34:31.267195
---

# 【漏洞案例】越权之修改HTML+CE绕过签名校验

# 【漏洞案例】越权之修改HTML+CE绕过签名校验

GG安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于挖个洞先
，作者挖个洞先

![](https://wx.qlogo.cn/mmhead/hIz3ylFIYS8YBkpg7n6eLWFQW1pejAdBHHWYiaI9h1tduNTFrzSqCfZSQOdlZptkakZwgDdb2Z20/0)

**挖个洞先**
.

有缺点的战士终究是战士，完美的苍蝇也终究不过是苍蝇

**“**

“最近只有出发的单程电车了，即使这样还要去吗？”

“嗯。”——《千与千寻》

**”**

01

—

操作步骤

1、查看论文处存在签名校验无法修改参数

```
https://yaklang.com/
```

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLicuUibTq0du8UsK4wcRY3g31iavibtia9oibsQNWDnMm1aWA9icfq2WAxM1QRiaXuSna4EicR7vqXkBWxicpsIc8eNQicQD1YA9vMCgDOIbw/640?wx_fmt=png&from=appmsg)

2、右键查看元素HTML，发现调用downloadFile函数，第二个参数为论文id，Edit as HTML修改第二个参数

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLicmKMpJwSy0IGHzl7ACJnMEdL8icvxSicicJcP9BicRfZpicKZlRuNS5PHuopicqMP31YFwshyAZngC9yQIw4vA4gxH8IJMbGfGVPmiaM/640?wx_fmt=png&from=appmsg)

3、再次点击按钮触发查询接口，越权查看其他用户论文，可以下载

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLicdPV8jpZ0zH2NKxNibVRwaaMZ6YqGEkONX9LBTYlnibE7ZhqayZYHfYAEzg7DVWribmHaNiaibY4ib8Bbric8fC6MdKMa3RBfaWGtGSY/640?wx_fmt=png&from=appmsg)

4、更多工具-任务管理器

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL8LQw5gUFKFUWDXJDo1rZdMpm67jRuHUDpsflVGT9vmk5CaV6bLCdQnNlnd09SdnPtiaBEot7vHqYhibnH38GujnWoibYeyA1ia1Rs/640?wx_fmt=png&from=appmsg)

5、进程ID，47244

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcL90tr9KO2Y5bKGFp5Usp3EvdfqoNh0sFhFq0AUBOhQgjbyibntNqiboLYiaxJyslqkQxceWxM9cRic0F19oDF9iaUuOp2AP2kYbsgU0/640?wx_fmt=png&from=appmsg)

6、47244转十六进制为B88C

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcLicVoQibuHVicXmppjyccfKiat6iawv3SoE0NEicDhwiap5a08OCXdkiaTvlfCh2LZicMGk6KNdzJ8eGJ1VPCjOoFItqfCgNGRjtAKIyYnA/640?wx_fmt=png&from=appmsg)

7、CE选择B88C进程

```
https://www.cheatengine.org/downloads.php
```

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLibYr2JWVwaO85kKoMk9M9MhHeLW7pAxHUHmX6vRhhR5G6DxwKYSucJiacdaEySJSrToZBPJOk3Fl0icaWPc7nIgxnMviajWYBbyRg/640?wx_fmt=png&from=appmsg)

8、String类型，搜索2124450

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcLiczN7w3VVmhAfLpRJTucFYH5bTloUFCZiaMtzyfl4WlstbP9xTja1dJiaia2x212SPFz8JbORMtZ3ZERf1iakp4hw288WqUrUWpRJ8/640?wx_fmt=png&from=appmsg)

9、全选结果修改为2124460

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcL9Yc5s4P0o2WqMBEYhKA7wYP8UlyjDIFicYgJ3swq43wxs1sNvYgQ6m8XnU15Hc5Bib4uFRpxEVGouMRCvEiaRic8purlCF1zS9Qibo/640?wx_fmt=png&from=appmsg)

10、点击查询，成功越权查看论文

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLicRJiapnNAEpTZHCeiacgG5lGqaicWvpvuYykLzAuXVBEbSh3aXhmPrCfm1jpjfFzneaqMibmria1DEUNPNkKo6UMibpvOkSSTAc1SLc/640?wx_fmt=png&from=appmsg)

**1**►

**福利放送**

再次声明：本公众号及其发布的内容的使用者需自行承担由此产生的任何直接或间接的后果和损失，GG安全公众号和原文章作者不承担任何责任。

欢迎加入我们的安全技术交流群，后台回复进群加入交流群

![图片](https://mmbiz.qpic.cn/mmbiz_png/ONkxMdpEUyicwaOmcTfkOFz3ibqQY5U5kZe6ersWbDDzPicCposncbMXDZqgfBYPs28MxicAalDfRc1zKRtLTPdVoz15lZiazxgvxu2PymOmXoks/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

**edusrc邀请码 | 无问AI 积分兑换码**

    免费不限量提供edusrc邀请码及玄机邀请码，可在的菜单栏资源获取-edusrc邀请码 | 无问AI 积分兑换码中获取。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ONkxMdpEUy9ElDjzNUt3nkCdORCzDQDqd5W9jMB7TGDkhjMpPBPib1tdSCIG2cxfkOUIDAU0bwh7SsuneyYRhMOftykBTOZWibqln7YYT0jHQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

**无问AI 积分兑换**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ONkxMdpEUyibL5FcSJZLe0eEX4CEAulldGaw6MXqsoVeTMTT7GsiafcdeWwOAfuQ1h89tWLAKmgSGibT9agQXe62yTwCCDlyUTNkAsLt2d8qts/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)

广告：nisp1级2级低价报考

**2**►

**往期精彩**

```
![图片](https://mmbiz.qpic.cn/mmbiz_gif/AFgdiaw95AaNY572lpficoa3l1cVE17VfZ4WDWhcMYWJbibW3UvQP4H2Izrsic6ZSlqnw3DtMzjzJHvuhGJ2V6CF2A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&retryload=1&randomid=tfibc7o0&tp=webp#imgIndex=24)

edusrc高校证书测评

绝版乌云重现：在VM中复活的安全宝藏！

钓鱼佬永不空军！！看我如何社g搞定学姐继而接管站点全部权限

捡洞！有手就行的信息泄露

没手都行，小程序纯自动化捡洞工具

护网在即，自动化"一键"钓鱼工具

Wifi Pineapple（大菠萝）无线攻击
```

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ia30l0vOygMHwGeYQM3b05DgghRuLMrUGfMh444bY02KJYLXXaur6Qp3IicGOTJQ82Dbs5rrIicaNMxSMWFFF5yXQ/0?wx_fmt=png)

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