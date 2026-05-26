---
title: AI带来的影响初现：互联网漏洞赏金大幅下降
url: https://mp.weixin.qq.com/s/1w9d6GAhWw71VLoGsIxt1g
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:01:20.313356
---

# AI带来的影响初现：互联网漏洞赏金大幅下降

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2mxgkqP6Hx2fIUcG5ibTZluSb6pV3UN3DHNrNsL24HhFk0B2CI5ag2CWzKiaRyER677JOTcmlwHDKTU21UdQmUMJk4A5uA022eS78/0?wx_fmt=jpeg)

# AI带来的影响初现：互联网漏洞赏金大幅下降

数世咨询

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点亮上方「★星标 」更多干货内容，不再错过！

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2mymGPAIkMxIER0whgicBuSkUlN7libnk3jDzsiaDfniaK7K47OK83nFYfr4Y732GY3OAA4dGbpseK70tFuMjt34H2b0fxsdiaYaDiaU8/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247542077&idx=1&sn=c63f262d4bb66895352b76087521895e&scene=21#wechat_redirect)

**本文关键看点：**

![](https://mmbiz.qpic.cn/mmbiz_gif/15I7jtE1uriaTpqMbLz5A8YygCg8eaYBUk0tJibjWvQrJONna1vQMDpOOafQaMjkeicDqcD9A02T81IYoKrqzrnzA/640?wx_fmt=gif)

**#****01**

研究人员发现一个中等严重性漏洞，此前HackerOne为该类型漏洞付1843美元，现在则只有297美元。

**#****02**

互联网漏洞赏金（IBB）项目目前暂停，很有可能是出于重新评估漏洞价值的原因。

**#****03**

AI导致漏洞发现成本低了许多，生成报告也很容易扩展。但仍然需要人来验证影响、去重报告、判断某事是否真的越过安全边界、协调披露机制，并确保安全修复。

********▍********以下正文内容基于英文原文编译，可能存在语义偏差，请以原文为准。

✦

**以下为正文**

✦

至少有一名漏洞猎手发现了一个开源安全漏洞，并通过HackerOne积压的互联网漏洞赏金（IBB）项目在数月前提交了报告，最终获得了报酬——但奖励金额却大幅缩水。同样，一个关键漏洞的新IBB奖金仅为2257美元，而此前为9250美元。HackerOne发言人表示："IBB项目目前暂停，同时我们正在评估对该项目的调整，以最大化对研究人员、赞助商和开源生态系统的价值。"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lYWDmickZ2mzhicxy95WGibIHOiaFkVmTF9Dcv3w0q8yISLlNOxzr71sjhq2cPOletE0XXc2TrgHB2icAiaZmXa9LsEQfmiay6bbS0YzHckn0U6Om0/640?wx_fmt=png&from=appmsg)

今年1月，The Register与黑客Jakub Ciolek交谈，他表示自己去年秋天通过HackerOne的IBB项目报告了Argo CD（一款流行的Kubernetes控制器）中的两个拒绝服务漏洞。Ciolek原本预计会收到约8500美元——但HackerOne却让他等了数月，在The Register联系该漏洞赏金平台后，才终于收到了邮件。

这些事件的发生并非偶然。随着AI工具能够自动生成漏洞报告并大规模扩展，漏洞猎人们提交的报告数量激增——但质量却良莠不齐。这一变化正在重塑漏洞赏金经济的格局，同时也引发了关于开源安全的深刻反思。

**0****1**

**AI如何改变漏洞发现的经济学**

AI驱动工具的出现从根本上降低了发现漏洞的成本，也使得生成报告变得前所未有的简单。HackerOne自己的数据证实了这一点：研究人员现在提交的高质量漏洞报告比例正在大幅下降，而垃圾报告的数量却在飙升。

这种变化的原因是多方面的。首先，AI工具使任何人——无论技术背景如何——都能生成看似专业的漏洞报告，其中包含正确格式的PoC（概念验证）。其次，AI生成的报告往往看起来很专业，但实际上缺乏对实际安全影响的真正理解。最后，当研究人员的报酬与其报告数量挂钩时，AI生成的大量低质量报告就会涌入平台。

**02**

**开源项目的困境**

像curl这样的知名开源项目已经感受到了压力。curl的安全负责人Daniel Stenberg在博客中详细描述了AI"垃圾报告"如何摧毁了该项目的漏洞赏金计划：确认的漏洞比例从超过15%暴跌至不足5%。处理这些无意义的报告占用了维护者大量的时间和精力，严重影响了他们的工作积极性。

**03**

**仍然需要人类判断**

尽管AI能够大规模生成报告，但验证影响、去重、判断某事是否真正跨越安全边界、协调披露机制，并确保安全修复——这些仍然需要人类来完成。AI可以加速发现，但最终的决策和协调仍然掌握在安全专业人员手中。

HackerOne的决定反映了一个更大的行业趋势：当AI降低了漏洞发现的门槛，传统的漏洞赏金模式正在被重新审视。IBB项目的暂停可能是暂时的，但它揭示了一个根本性的问题：在AI时代，我们如何评估和奖励安全研究工作？

\* 本文为泽钧编译，原文地址：https://www.theregister.com/security/2026/05/21/hackerone-takes-an-axe-to-its-bug-bounty-rewards/5244458
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁**多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgrBsUKCFUU3a6Tf9jsVWJcD2l6ic183HdhE2nqia7uMYO2NRQRylficZ5Q/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrGADwibHso9Bicpccu5Oe06s25Kz1rp9KUaUGaHbA3TG9R1iaqOxQbKlzz3q45urLLiaNm3r8x4LowhA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539099&idx=1&sn=8820d80fdc92ac1f321b5e0a3ff0653e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqodJDDGgZLvcLHLjonO6D6SWFh5QdgUTDZJI2uWWhL2pvdicCoic8jhlmXDDmqnUreFaQeJvEMF12dA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539436&idx=1&sn=676908ed11008cd016b253d1d8e6ba8a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqwJ5oWv2LTsaCqsARGoJpjT7Pxib7vCX6T9TTuWQLuAx3KSUpryl4ZvTnpJSBJCZ8SgoowVjD1BVg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540181&idx=1&sn=e0cd678638b098f969f257b408062b91&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrBJ7QP9nU3wQmMvolcOV1gCuk81sv95ev7tRqTxnh4ib8kqibgFJPFxaF0iaKtiaLicoF6B6iaggtVH8Ww/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540845&idx=1&sn=ec923893881e69010ad830ec852b0abb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrgBb4f5DIe21U8to7y1VMziaQ7ahiaKEkib894mtlFoxDBF62D1wGlQNm5vghS5XGSALN6YY4ZFJHJg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539573&idx=1&sn=a721e2933ad640a3a4b3c72f74d76685&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgzKcal7yWn6SZcgqEr0keAmz0xMbg93YD4my88Np43CkMAEdZHXtlxw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514185&idx=1&sn=8015c07a68a5e2b6074efd2c77f20085&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqwJ5oWv2LTsaCqsARGoJpjOQz7r8ibPUG4znENuDuosPYHByfLHsh7jPxvyiaFianIJgfEV9HX4icpbQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539380&idx=1&sn=da5e8afa28247b4212a544750ece924d&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgjAGO2xBRC4TjicDA4jPbLyeLJbhlLs26gV3dyHrBL6O7H33PPeibFoYw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514336&idx=1&sn=e69b1126e86ab2c59c8ca8e315637031&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgaGg7wIzbRTBJwle4uBxXUJcCG0AibMSAKnJ6qdE9l2HgeAWpxfVAfIw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247530968&idx=1&sn=3d712e23b322ad37cee46d27adb08ed0&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoUdBA8wdHsOh02x6PfOicR0fqdOTPLahE5Y2UPZqZ0Viat6BrAJYrzEyDA9CI3N1uP45zwLjHFTysw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247538943&idx=1&sn=7f95d33eb069aab1cba23c41d68c9759&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgqUkHibDR3uvnsb4JEozX3XJgFnPQSoMCqWYTZNrr0jvCy11yibml4Wgg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247515942&idx=1&sn=bc9ba104b8eb1c0e914d90c8c9a34542&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg1RBWLvLVSHPqQJ613ib6sKvgDPCfa8wYrog3uFFP8pc4pCycQQ3a0nA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247532302&idx=1&sn=2c6afc5d39c89c86f79020099ea44baa&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg0sUJC8RzqMWibMF0LfCLyEcesDzHTJOlIFyibtUyCZy2bJswaUK56ZdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247512372&idx=1&sn=5d06a830f00953a0ab75157fc023ae56&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg6GdM2ic2q54fZEIdWz3LqKpPODruTaeEzRMArzYJWZD4reLgYGgG6DQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247542912&idx=1&sn=1d8f517c8cafee1d4963665676835063&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcs0NU7ZEWiaTufjAkmrhLqnxywvopoNWA60bErgfSXD17qZ57dkxvue6A/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247537068&idx=1&sn=3a3e7c08d93638c1a6018c7862b13bcd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcsic2hQICquOt1dwrexbbJanpAMLl2UFGG14LgYTzDtOHHSouF067yP1w/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247538269&idx=1&sn=848c657fc234aff8840d16d3f06b34ea&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http:...