---
title: 新思路！支付漏洞实战案例分享：低价薅高价商品
url: https://mp.weixin.qq.com/s/cWFZTGjWa1kNJ2ZJuT96SA
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:44:03.071413
---

# 新思路！支付漏洞实战案例分享：低价薅高价商品

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eDXiba58htLcAhMff5JU6pCSgVibJw4MpGWnOSsKU5QZR0zJK71wxxrcX29HFibDRRQfj0Ju77us3lEcVwUiaJFNFJxx2fGtqFdxkyHARHaHkrE/0?wx_fmt=jpeg)

# 新思路！支付漏洞实战案例分享：低价薅高价商品

原创

洞悉安全团队
洞悉安全团队

洞悉安全团队

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/qvpyaxz7jZ8QtdL3DtXhRwH7e4n3xgYwcAAticYZPN5icCauXalWRpD3yW93icibTnLDtqXCcN1M30X54JgYDJuSgw/640)

点击上方蓝字关注我们

前言

多数白帽在挖掘支付漏洞时，关注于修改商品价格、购买数量等直接计费参数，但易被忽视的展示类参数篡改同样存在重大风险。商家未将唯一商品 ID作为商品识别与费用核算的核心依据，后端未严格校验商品名称、图片等展示字段与计费参数的一致性，仅通过传入的商品名称、图片等信息展示订单内容，导致攻击者可篡改数据包：保留低价商品的计费核心参数（商品 ID、价格），仅替换为高价商品的展示类信息（名称、图片、描述），最终实现以低价购买高价商品的目的

案例分享

案例一

1. 访问目标系统

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfolDFcx9wORIjCibjZPZa2IJYCVQszvibD83ruuhVBQJAMfX6KBh6feQoicuqalpWkqO9vRAhYpeGBg6ciaBdTvoPhJiaA7tctp7Ow/640?wx_fmt=png&from=appmsg)
2. 进入预定会议室

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLcMo2mPWsohiaObBycO8v44rIaGwakWjy2NM25gEXAJUcn8ETXF9KjoBc6ts9rIYWEytib1yiaGECTGNicVVDmK0XN2mUX0KicfrwWs/640?wx_fmt=png&from=appmsg)
3. 预定该会议室需要购买附加服务，水：5元/人 ，投影3元/场，总计52元

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLfnfjKqISZgXbL0k1ABgbfBhJTbcHUVnFAfxFcnzhESNN8aLhkxOb8aWZ9opSWYhvKMwicVKuyEVmLhKYQHjphfISic8Xs3fSRn0/640?wx_fmt=png&from=appmsg)
4. 提交申请后拦截数据包，数据包中包含了购买产品的信息，包括产品名称，商品id，商品价格等信息

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLf0LwicfP9bP9Bg9j3MJ45RATS52zcjEt1MRreNwt1xZYpEj0Rk2ahN2ib4JArkVDqrWrxOGbLx83mTBTP41N06Q29MFE34zrbyo/640?wx_fmt=png&from=appmsg)
5. 思考：如果后端不是根据商品id去回显出商品信息，而是通过我们数据包中传入的商品信息去最终显示出商品信息，如果我们篡改商品信息，不修改商品id以及商品价格，是否可以做到低价购买高价商品
6. 保留商品id以及商品价格，修改商品名称以及feeDesc，修改为价格更高的水，删除掉原本水的参数吗，下单

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLen77z6Xh4aGyN3JkCyiaCXzEFquG0iaMb4O73DsOYn8lImBurBvsVyXSibW4pRu5lNficLds683P7JzLAeibZj6LFtl2bGaE5Hzous/640?wx_fmt=png&from=appmsg)
7. 下单成功，利用原本购买投影的价格成功购买了12人的水

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLfFgrNZLlqg1q9QVpPzc254NYoPerlwv3hpXoM7wW92SxLj3m9s6fiaMb3ZvTpCmcRFeDW1ewKHZX0CpjttoRmkd72eNsD2WghU/640?wx_fmt=png&from=appmsg)

案例二

1. 进入商城，选择一个低价商品

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfS6ze7WJrtibTVeXkgTInPkAXnLM2AqgXFJCk5YNrLElFXByK9bglZlTfzLXRiaGDsI4iatUSzYMHsibTMBzRsxJanbIzkMV1cy0c/640?wx_fmt=png&from=appmsg)
2. 购买商品，获取生成订单的数据包

   ![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLewjpr5MUPCj1ugumAhI2gQRjciaqZm0jkPeYjoxBnmsibiaAZk4NOZicsMaj7NfE28ujibvYJWpO5WMtbUkiabErhAyEklN3MukHRicg/640?wx_fmt=png&from=appmsg)
3. 这里先获取其他高价商品的商品信息

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLf9N8JxMj4ZFedLXFQ60qnkFqICP3rCXLp9bjWQpJVntqJrBa6uYzYho6REI7lHyLN82ODfUs5aV0lcPIGmvtGIvSu2vJKdup4/640?wx_fmt=png&from=appmsg)
4. 修改掉生成订单中的商品名称以及商品图片，保留商品id以及商品价格

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLdqY8QKlTN4pq4GTYNFiagyM3dRnVyNFTrYIicUaeowU9HzIbfCmFsnALI0NLMpQFvH9JxJesrLMjfobQC3B5ErAUX52iaJuygPj4/640?wx_fmt=png&from=appmsg)
5. 成功利用低价购买了高价商品，并且商家会以该商品信息去发货

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLfEt54vqs1u32TBL5sGrlkUr8QCF0ILeF9o7Fibq733HywibdTCrf8pqibucMQoMBylvVWu56k0Nbd1icgqvXr9gH57lXZZdkGiacOQ/640?wx_fmt=png&from=appmsg)

最后也是狠狠拿下高危漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLdLjh2vibHg3OAl1oak8pojnBQ0f9pRTNaPK0iaDeyPuloicg0lRr9OSl2iaTRudf3EDl4xQHZ3mXQFM5r3Hic6p7Riapnet4nzsYRUE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLdUzlxQOu2zF4JgyTiabB1UPZtSsjOlun3TdohttVVVABGRicUSYJlGBBnKddc6R5SvqQop8RKqZibfpYIjMDyOnKMuV8FSBUpia8A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLexgjFPZNWhS2IJrOncKiaSxBPzCibGZJ1ATx1jia0OPhSE4LOSFOPIeM8u9J4OiaAkEXnA4x3x3pBiadNSDcrib4oheIAdw6ib5Y0jBI/640?wx_fmt=png&from=appmsg)

思路总结

该支付漏洞的核心成因在于后端未将唯一商品 ID作为商品识别的核心依据，而是依赖前端传入的商品名称、描述等易篡改的展示类字段来呈现商品信息，且未对展示字段与计费核心参数（商品 ID、价格）的一致性做严格校验，导致攻击者可通过篡改展示类字段、保留计费核心参数的方式，实现 “低价计费、高价商品获取” 的目的。

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eDXiba58htLekHKc7aQlwu3dr05zYdBibC5nicwX5jqzjHvtZWW5JQiciasgF7fLxXkVQyYEaVibytibUPamib1jy151gjqjBRPl5AHqnoXQEdz3Ehw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzY3MjkwNg==&mid=2247484378&idx=1&sn=cce951dcddbaa1d74efdf6452c081fb8&scene=21#wechat_redirect)

[深度剖析 Node.js 环境下的 SSRF 漏洞：从原理挖掘到防御体系构建](https://mp.weixin.qq.com/s?__biz=MzkwNzY3MjkwNg==&mid=2247484378&idx=1&sn=cce951dcddbaa1d74efdf6452c081fb8&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/eDXiba58htLcGaycvLZ1JM0rjUQIKaV5r052LTsoABrakSpHNVErX8Q3WEEVv5tkoicjiaFSyibSV0PkSvoePpZVfy5ydgCZc3CyrbxL3f3aHN8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzY3MjkwNg==&mid=2247484352&idx=1&sn=d2de41077343666343b4b611b4f49470&scene=21#wechat_redirect)

[实战复盘：严苛 WAF 防护下的 SQL 注入绕过思路与实现](https://mp.weixin.qq.com/s?__biz=MzkwNzY3MjkwNg==&mid=2247484352&idx=1&sn=d2de41077343666343b4b611b4f49470&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/cv7xkU9cPaX1dqtBQs6CcuBcVruKFIXQKHnK0iaQY1lRENrqAp2dD2piaqJcyPic3WYTicIjCXDNDCZvicxfvqEUSFQ/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/dOYiaqzHIghaFLYs31bUp453ZkiaRaIxEricFoJpkmMedQjr86DVO4RlxSBKcF1wljKE3YyacFpicMxFDE3eZZf2EQ/0?wx_fmt=png)

洞悉安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/dOYiaqzHIghaFLYs31bUp453ZkiaRaIxEricFoJpkmMedQjr86DVO4RlxSBKcF1wljKE3YyacFpicMxFDE3eZZf2EQ/0?wx_fmt=png)

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