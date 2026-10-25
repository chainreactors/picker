---
title: 漫谈AOSP蓝牙漏洞挖掘技术
url: https://mp.weixin.qq.com/s/tBpoFfNle2AVhaT58Adk5Q
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:07:23.661138
---

# 漫谈AOSP蓝牙漏洞挖掘技术

# 漫谈AOSP蓝牙漏洞挖掘技术

GRCC
GRCC

IoVSecurity

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/CQb4KERYG3QA0ezCCjgRONQvXCf3wka7je04trwIyMqsDUWBubpwfiahXImiaoia7NnueGomOO28vicSZ5wEFFTa1Q/640?wx_fmt=gif)

点击上方蓝色字体，关注我们

**/******技术交流群******/**

添加微信13918880149\**15021948198(好友已满），申请会员下载ppt & 加入网络信息安全、测试评价、汽车电子、自动驾驶、智能机器人、智能船舶、超级高铁、飞行器、招聘求职、投融资合作群...**

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVyoplEC2gRcrB0Gg8RQAMsv0DPKtLHkKym7iaYxaJpp4b7lbQuXUXuOA/640?wx_fmt=jpeg&from=appmsg#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVdWoWBQW4B5thPcibDibhnicVgIPMBgeXP9L8QGSQmoFPYE9jbcY1rUPmg/640?wx_fmt=jpeg&from=appmsg#imgIndex=2)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVVZkgbiaAUSEr1UveQLwyxCPxm92X6VJ0RrQNrrh5wiaVzoCCVTmiaVBTA/640?wx_fmt=jpeg&from=appmsg#imgIndex=3)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVNcg1tKeLj5nESOlCS0Jmq06U7vguyiaVwfAeKs0KVHgLyrSrx7HGYkg/640?wx_fmt=jpeg&from=appmsg#imgIndex=4)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVViaHtSsibqyAibMXicHTeUCfCdhlWhKiced0lmGcAq7qdHmM6ChcVUzdQBrw/640?wx_fmt=jpeg&from=appmsg#imgIndex=5)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVIHGHR4txtugm782qnEVlMCRHlib3Y2zS2q869sYcCc7WOZ2eaSftHgw/640?wx_fmt=jpeg&from=appmsg#imgIndex=6)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVZscrxOSxS6bRiaJdxEQjOPgWYNUWx5X9rPDb3fcbUZuvkkibOfcajPFw/640?wx_fmt=jpeg&from=appmsg#imgIndex=7)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVuBUBhZibD0IxzUPB03YVJ3wmx9tia29TZcxLiayY11qPOOq3VNQwCHwqw/640?wx_fmt=jpeg&from=appmsg#imgIndex=8)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVI4ONpXD59fI353ROlt4CLliaek8KQiaBYfW5U54axTFxnfJCdXmKNMDQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=9)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVyjM0cYxgqt8ZQtAeMZsy0sv2hhbBicYqlb1fnCHThzSVTRLic1WDGugA/640?wx_fmt=jpeg&from=appmsg#imgIndex=10)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVG1yDzzwa0A5GyFL9BFkxoAfupECU0GBfibicT5UGz9tK0cbDh5B0OQicA/640?wx_fmt=jpeg&from=appmsg#imgIndex=11)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVV2N7OFvuzpEQj5u5vHCp7icwDYfa5wAL2lMIRFzoxh6HuBiadiaWBMYrDQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=12)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVxAHib9Xppf2UUxR0MKbaaRyNuicyocnrMAejKOHFdnte4uKxqyqZUHwA/640?wx_fmt=jpeg&from=appmsg#imgIndex=13)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVCLddUqlOgZ0bIcoqahKh277UypUbNdH31cApag9KvC4nMv5f8GK9icQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=14)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVGSN1VGHl80DGHtalE3p0S7Vic2BprRicUJm1pyneT5xSDGLyhItLc7BQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=15)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVV6bd0x7ZEsZEicueiaUvSQdcWql4wqvtQHSobnO7eXBqFj3tTyMXHpjtw/640?wx_fmt=jpeg&from=appmsg#imgIndex=16)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVbtYpmZYKADuEHA3srGtHEunLLhrGCz9lrGUspu7nmyT8je19z3pCpQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=17)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVz0uRU6iayIqrzH9MArEPA6iagBJFL4s8oUaTxA48icFbHoflyb8Nu7x2w/640?wx_fmt=jpeg&from=appmsg#imgIndex=18)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVeAB3XftpFMtL1pRSNtqlJgNCCibAZgticLddRSK3TYJ8DvgJpLQ1Iib0g/640?wx_fmt=jpeg&from=appmsg#imgIndex=19)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVsf7UB16jaG98fJ6ia5olYmW9weQiaGkUTmza0gMTpf8SckKibI5231Aag/640?wx_fmt=jpeg&from=appmsg#imgIndex=20)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVJDzoxw7bMIL9dOlgVVuabnpIibhpPmLnSjfw2ywgXnibOvlttR4VOB1g/640?wx_fmt=jpeg&from=appmsg#imgIndex=21)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVgxugTMqPmWzAz4m3AqtwAHWTibibTTwrr7mRQBGRqdmpfdmPml2ZB5rw/640?wx_fmt=jpeg&from=appmsg#imgIndex=22)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVV6XW8kbAicKlJ3y3yjOppQzticTDr1FejhlffDoflhQRXKFXt2PDuHlVw/640?wx_fmt=jpeg&from=appmsg#imgIndex=23)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVhxic0O5lmQWzQOUvOicQqyzfLCn0Ga9IKns7eUJ47gWFtjKETjm37vyg/640?wx_fmt=jpeg&from=appmsg#imgIndex=24)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVvVPUjAckSzdoc3A9om88hQfXP1dxjUVMDevNkfibpoujzr8mdib3pJibQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=25)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVo58DTYRY3O4wicwCgQowtHpEHIzQlFCARUk8AUKzUXo8e4oZ0n9LFew/640?wx_fmt=jpeg&from=appmsg#imgIndex=26)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVV7sXdqP1OCHyDsicST9QlU0pgutjb4qtAJcQ4mLXOfDs39nPBX35sRpA/640?wx_fmt=jpeg&from=appmsg#imgIndex=27)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVrTUfFxG9oLGmI85hxpRmWMDibFtesZC7J46FlRAW5ELzlJADuAyQhZA/640?wx_fmt=jpeg&from=appmsg#imgIndex=28)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVz3iaxs865O2caXibvUkAK5XZadmWib6OecFp5SBeWUa69oeUgU3K6gRzg/640?wx_fmt=jpeg&from=appmsg#imgIndex=29)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVtVO9ZGZsKl3NUwicRAl56XlKLp8Y4OZF7ZsCRJwiaiaD0dmVuDryZCKbQ/640?wx_fmt=jpeg&from=appmsg#imgIndex=30)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVPd2KYiaTNbw5meJUPPLxcKWY7rZP1iacMvmkT3lyzRf4lc9XFNr0ib0MA/640?wx_fmt=jpeg&from=appmsg#imgIndex=31)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVV2J8OKCSEicXeicb0VQibxmBuiakLEQAujxAIIFvLA4a0aicI7yg0G20HfnA/640?wx_fmt=jpeg&from=appmsg#imgIndex=32)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVVQzkyGCokKjwicNibq02l4RmekZEV8VpJPJJBQpvxcKsgOb1gcEW9ib9ibg/640?wx_fmt=jpeg&from=appmsg#imgIndex=33)

![](https://mmbiz.qpic.cn/mmbiz_jpg/uTSIm9RGwm2G18XqQ97TBThhorNTUmVV3IwXObBwtzplv6NYg1w7Y8feI35SLyEf7CNssgvEpRfCPJwV5uEqZg/640?wx_fmt=jpeg&from=appmsg#imgIndex=34)

![](https://mmbiz.qpic.cn/mmbiz_gif/b96CibCt70iabwjyojLhA03PtxUnkNPREnt2F48ywfXLpDdDAjicOTPI8Q94tVLbJ58tbRs12iaXDKhUOW9gd4NlFA/640?wx_fmt=gif#imgIndex=35)

相关文章

# [基于模拟仿真的蓝牙协议栈漏洞挖掘](http://mp.weixin.qq.com/s?__biz=MzU2MDk1Nzg2MQ==&mid=2247601425&idx=1&sn=75fa4c1bbb48eaf5666ccd22a6e7ba96&chksm=fc031ddbcb7494cd458db474491f389a36b76d91b9ea3d3ca40380b94ac8d52f6353a2013270&scene=21#wechat_redirect)[低功耗蓝牙黑客.从数字逃逸到现实](http://mp.weixin.qq.com/s?__biz=MzU2MDk1Nzg2MQ==&mid=2247598421&idx=1&sn=078f96d1ca4fbb7b2429b4cffc7bf8b5&chksm=fc03119fcb7498893641c2f9129d356cf0284678c493abe86946b49cc7dfcc057ecae5ca144b&scene=21#wechat_redirect)[蓝牙在智能终端的信息安全技术要求](http://mp.weixin.qq.com/s?__biz=MzU2MDk1Nzg2MQ==&mid=2247576336&idx=3&sn=69acd8592dc4be8a1e80057841829710&chksm=fc03fbdacb7472cc0894511fff3ffb7419256603301a2e288c1e7413728540b989645ee578d4&scene=21#wechat_redirect)[智能网联汽车信息安全技术&市场报告2024](http://mp.weixin.qq.com/s?__biz=MzU2MDk1Nzg2MQ==&mid=2247600746&idx=3&sn=7a79ea44937f8666e425f256e7a455b4&chksm=fc031aa0cb7493b6ae817fa4219d57b1cf65eefaedead97dca01cc1fe196b6d470bbe9eb7a38&scene=21#wechat_redirect)

#

![](https://mmbiz.qpic.cn/mmbiz_gif/MfTd6rd9CyvNRMW8I9cvI1CK5gKiaYqg2veTn9t9dAe1GxYic7pAvgvRIKNFickConFyX8AvW2reAq8GchJI6aBpA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNwzJ6g6cwDPWQPkMNSdxNzJNib6icvM2LNjWicc7Jdyzgduy5tKjYjt6ghKmiaHv6XEq28Et5pnOos5Y1icH8Wrx9SX03t7n1mmuE1g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNx3XibDCcEHR7XYayO6ROlXoNkpaTZRl06QHfX1ncLMWf2RAUXM28XIrZIovlhoadFvJvBnZBQWfGeGrKAgZ9X42f3wA999JBZ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WvsNkg6cHNwGy566FAz6qyctiblp3tMd0ECjDLU2WDiaI8BRricjYnobXF0KVMKf2W5aYoqYvcsCoZAyK4ibLWHL0W4KxgBsgGr0QvVHT8mUbPo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/WvsNkg6cHNw6GRHELmyd2YoMhpH3n5v6qnolI6zvBd4PSWZUPUmr44DRDwibgKUhKKg1WqGpcagazmWynTiaGYFnicViaPJN...