---
title: 大白话 说密改——密码篇
url: https://mp.weixin.qq.com/s/o-e6OUM0ksVGhvNQscs1_w
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:35:54.564361
---

# 大白话 说密改——密码篇

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1Vd0DvJG7yQ8VmMgc6Kxsic71RrHw9qzDcAoUS2KNkj7R5MKUsdnyJ10wM2s3ibzyiakQmUWRyZGmHniaXcFuy0Uuv03hNGAZ4ticyeNPPCkVtYc/0?wx_fmt=jpeg)

# 大白话 说密改——密码篇

原创

自主研发技术驱动
自主研发技术驱动

珞安科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/eXicedYoc2qUBq2XkibuVB46Wic8VXSpNXhplqfNmFooI0CWrFiagkCiarAuyia5s4gO5t1IgibprGPGb0Mskt144vpNw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgucsvulEWzPK7aR3ibs2suCTRg220S7x433QqDHc7ksTVibKibZyl504ib4z0WfoDM19hY8gLjARZ2mQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgucsvulEWzPK7aR3ibs2suCG30YbNgstJIl9AZIPYk8lWzFaXzswJgTGqSOdNuIicI1qVy3R1QznMg/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUA9p2uNAAicV4UCGV7jvr1OU99hJfn0yiaZsAWHiauloZ5G3tOHb8oD96jTp2HPIbA3ppzuymxKxLxsA/640?wx_fmt=png&from=appmsg)

**你以为的密码**

**可能不是真正的“密码”**

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgucsvulEWzPK7aR3ibs2suCIq2CHVNBo0nIicSX1JhhLlIUAwHicPVc8954uicq0uPb6B0BibDibQGIEJA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgucsvulEWzPK7aR3ibs2suCRibicfguibibWU96H73peibdvWXZ9VXfdvMUO3sj9iaOyEPF8nyJl8zUlvng/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1Vd0DvJG7ySZOHLwPyficMsRQEicwoSIRJcicVdItu6X0urqkeXMfLricd6YYVbXvscexAzNfP8iakR0ICyjwG1ShyiamsWITmjQDrSyTM8F70blU/640?wx_fmt=jpeg&from=appmsg)

你有没有过这种经历：

打开手机，

**提示“请输入密码”——**

你输入了 123456。

**又提示“密码强度过低”……**

![](https://mmbiz.qpic.cn/mmbiz_png/1Vd0DvJG7ySx94iaoNH6vaLOicX2SVYGQDdJibqHBued1rRLAO3FXw2uN4NMQKBbd6R75JwlsjgpYbr6dkP50rialSicLy6zzhhlsuFAup3nIWlA/640?wx_fmt=png&from=appmsg)

你换成了 123456asdf！。

过了！！！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1Vd0DvJG7yTDr3ANyKALLC6YtQGha0o4iawGnK6YPzWEJDicsckOiaArLs5B21eLNUqiaQTtqEkLCqRr1D7BpWEQsfl6mCBRznDO28Tvaov5n5Q/640?wx_fmt=jpeg&from=appmsg)

然后你心里想：

**密码嘛，**

**就是用来登录的那个东西，**

**越简单越好记。**

![](https://mmbiz.qpic.cn/mmbiz_png/1Vd0DvJG7yS4HxTicEWpQdt16hAqmcRR73V71j5aAfHC2wylJMu2JY22FWEwGicj5Q5wKraibpCeic7Kk3hed7VbE2rOQVHrCHeS3h3RIj8Yeng/640?wx_fmt=png&from=appmsg)

**这个叫“口令”**

**（p****assword），**

**不叫“密码”**

**（cryptography）。**

我们今天要聊的“**密码”**，

是那个能让你的银行卡、

电网系统、高铁调度、政府网络

不被黑客一锅端的**硬核技术**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1Vd0DvJG7yRagialh7jPR3jfvj9pHzNZGs0OtaG5dVkfYG9Jb1bsQUJGA0gRq7X9xZZAobxg73OoAV9qNGwPst8nYliaUBwiaknE1mIKKVvFHs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUA9p2uNAAicV4UCGV7jvr1OUKicDFrzZHJc3yQ1DaOL52aao6ib1KcI3ZqfmpibY4ZGdDlWhI0419pcwg/640?wx_fmt=png&from=appmsg)

**01**

**密码是个啥？**

**一句话解释：**

密码，就是把“看得懂的东西”

变成“看不懂的东西”，

再变回来。

**举个栗子：**

你和同桌约定：所有消息里，

每个字母往后挪3位。

“HELLO” → “KHOOR”

**这就是最简单的密码。**

![jimeng-2026-05-11-4734-保持图片整体内容不变，将风格和色系修改为@图片2的蓝色简约扁平化设计风格.png](https://mmbiz.qpic.cn/mmbiz_png/1Vd0DvJG7yR0WGhBzvkfZPId4zFG9WHiaNtEHpJjQNdLYW7tLtyQDYGqMj8icXTZRwEzIl09B5kJZt6PAAfjwhKMqdBoOjcA8AYoHHhrDax5c/640?wx_fmt=png&from=appmsg)

当然，

现实中的密码远没有这么幼稚，

但道理是一样的。

![](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUA9p2uNAAicV4UCGV7jvr1OUKicDFrzZHJc3yQ1DaOL52aao6ib1KcI3ZqfmpibY4ZGdDlWhI0419pcwg/640?wx_fmt=png&from=appmsg)

**02**

**别搞混了：密码 ≠ 口令**

为了让你彻底记住，

我们做个对比：

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/1Vd0DvJG7yRU75zwrB1xTHKvnWd2fJBAiahJWXWEWjOSWqJLRa922Miba4un4aYiabLSyxMsmYicUa1XLg7HsU6bdsaa1qC5RsHmudmCOSswibRI/640?wx_fmt=png&from=appmsg)**

**你可以这么记：**

**口令是钥匙的形状，密码是锁芯的原理。**

你输错口令，进不了门。

但如果没有密码技术，

整个门都是纸糊的。

![](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUA9p2uNAAicV4UCGV7jvr1OUKicDFrzZHJc3yQ1DaOL52aao6ib1KcI3ZqfmpibY4ZGdDlWhI0419pcwg/640?wx_fmt=png&from=appmsg)

**03**

**关基设施为啥离不开密码？**

**关键信息基础设施**

![](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUA9p2uNAAicV4UCGV7jvr1OUjqzEUDCzXXPD0whVRYo7Wmbz9XI6C7v1FLX9j7SCSHob5rkkHibzic1g/640?wx_fmt=png&from=appmsg)

关键信息基础设施（简称“关基”）是指一旦遭到破坏、丧失功能或者数据泄露，可能严重危害国家安全、国计民生、公共利益的重大网络设施和信息系统。主要涉及八大行业，包括公共通信和信息服务、能源、交通、水利、金融、公共服务、电子政务、国防科技工业等领域。

**简单讲：**

**没了它，社会会乱，**

**甚至国家会瘫。**

这些系统里，

每天都在传输海量数据——

电表读数、交易指令、

调度命令、患者信息……

**如果这些数据被人截获、**

**篡改、伪造，****会怎样？**

-篡改电表读数 → 全国电费乱套

- 伪造银行交易 → 钱被转走

- 篡改高铁调度 → 发生追尾

- 篡改燃气压力 → 城市爆炸

- 伪造医院检验单 → 误诊夺命

- 篡改水利闸门 → 洪水泛滥

![](https://mmbiz.qpic.cn/mmbiz_png/1Vd0DvJG7yRFPI8vL4rZCBPYyenxt0bcx0WLfWbEJ2prJ6kOVzyaTicn1pATLcACDcFPCgCW9wvmUMbej78WwkR6ibLletyMRrrNeRkic5LicEI/640?wx_fmt=png&from=appmsg)

这不是电影情节，

是真真实实的网络战场景。

**而密码技术，**

**就是给这些数据穿上“防弹衣”**

它能让数据：

- 别人看不懂（加密）

- 别人改不了（完整性校验）

- 别人冒充不了（身份认证）

- 事后赖不掉（数字签名）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1Vd0DvJG7ySkAS9KpNy56xKY9nrwKyib6Ax4mFfxafUAYSFxlFC1tib5rIDeOwD0nULbgkVQT28BMeEoPPEup87QDw2f5podlJttf3RtGhhKs/640?wx_fmt=png&from=appmsg)

**没有密码，**

**关基系统就像没锁的大门，**

**谁都能进来乱翻乱改。**

**小结一下**

**今天我们学到了三件事：**

![](https://mmbiz.qpic.cn/mmbiz_jpg/1Vd0DvJG7yT5eHY8piaibg4mmBl9lf55Jg1ibCxDnW5fpoTu0vHEcwOtgEowNkLhc8W2iaibBOcrUUwPzImyXUdBVIMQnsnzYgywWjVOv5u9bRPI/640?wx_fmt=jpeg&from=appmsg)

下次再有人说“我的密码是123456”，

你可以微笑着，拍拍他肩膀：

**“那不叫密码，**

**那叫口令。**

**真正的密码，**

**连黑客看见都头疼。”**

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaWv4Iwa2Hv6fUVkibwwa0u2qsUib8DeeEFdC6cz99zDlVo8MKg5cYD5wtYPLmsiatgW6PP0ysYjrYXQ/640?wx_fmt=gif&from=appmsg)

**下期预告**

SM2、SM3、SM4到底在干啥？

为什么RSA要“下岗”？

不用数学公式，

照样让你听明白。

**敬请期待**

**《大白话说密码——算法篇》**

**珞安科技**

**北京珞安科技有限责任公司（简称：珞安科技）成立于2016年，是专注工业网络空间安全的创新型高科技企业和国家专精特新“小巨人”企业，并于2022年行业内率先通过CMMI5级认证。**

珞安科技拥有业内顶尖工控安全专家团队、工业网络空间安全研究实验室和四大研发中心，坚持自主研发和技术创新，以零信任理念和体系化思想为指导，打造“实战化、易部署、易维护”工控网络安全产品体系，覆盖工控安全、业务安全和工业互联网安全，构建了全方位的工业网络空间安全防护体系。

依托强大的技术原厂商实力，积极开展安全服务和安全运营，业务遍布20多个行业的2000余家工业企业。在全国设有20+分子公司及办事处，提供7\*24h安全应急服务响应，保障国家关键信息基础设施安全稳定运行。

![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn6YThhy11Smc2QOP8zOBxpqd8SpV8ic7Fc3BjiaKwDfBzpy76Lf5ianBDGL2BoXWicJm8U4ZnYI3CSQ3g/640?wx_fmt=gif)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1Vd0DvJG7yTFe9gJSmFibRXvdqkPyqM9pKibAmI4OQQ6lmCBqiaI0OdLlVjZuumJ9Wkx2UtQuTicQ1FK5HibgdkDBc5qCTY9Uicpnqz3nTnbVcqM8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2NjI5NzY1OA==&mid=2247514826&idx=1&sn=e52297b3867908978725912bde40663a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1Vd0DvJG7yTAgPNnN2wKjoWcyuh5EWjkOQGdc2VutD1M1up8NDb92rTxKA7poDHILoM7riaGoOwQTX7bI6NicgryCsUmT5nCA5o6Tibgfibib1U4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2NjI5NzY1OA==&mid=2247514778&idx=1&sn=d6c87898fdfe1ac6102b6f41c991674a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1Vd0DvJG7yS4sLbl3ichpQoEYTia93EyBZsqFuqX9FYYcCjNO0hrTX3gcZBflGfV80tiaYr7AcOJaiaVicp8mLtzADYuysiaok5Nm7luicUP5Uf1ibc/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2NjI5NzY1OA==&mid=2247514844&idx=1&sn=cc2342395de11364c2075e01fe4a33c0&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/1Vd0DvJG7yQc58a4MdAic3qH56BF8RC9pQ2ib1kZicP97KoZf7gCA1lOmz3v3aFHLjH5pLaDkJ105rqaeXic66VRiaicaNkiajIEb7UveslpsI8h7A/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2NjI5NzY1OA==&mid=2247514805&idx=1&sn=6a76b0f4bbbb03f41cdd5ae4e8971518&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/eXicedYoc2qU6L7OdM6LWJZ3NrSxRiasZrBX7nKAn9QxSI5xT77YSJXFoohNZeuyb1moicaxZe3vEw9jNGkogEJ6w/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/eXicedYoc2qVC3qT2LCRbwyVyLJibgFSxJDHwh311aUAdeibE2vWyZ7pAkpH4c2pyrLDvYOt48Lhd9D8NutFeMTCg/0?wx_fmt=png)

珞安科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/eXicedYoc2qVC3qT2LCRbwyVyLJibgFSxJDHwh311aUAdeibE2vWyZ7pAkpH4c2pyrLDvYOt48Lhd9D8NutFeMTCg/0?wx_fmt=png)

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