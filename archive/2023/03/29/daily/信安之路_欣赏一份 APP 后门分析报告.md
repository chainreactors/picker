---
title: 欣赏一份 APP 后门分析报告
url: https://mp.weixin.qq.com/s?__biz=MzI5MDQ2NjExOQ==&mid=2247498593&idx=1&sn=b27bb097ee2f9dd1628bb47f09d11228&chksm=ec1dcb49db6a425f661071c738ab7f50d7f2760d1195ce54fd84a16d6d101b58b72a307be7ec&scene=58&subscene=0#rd
source: 信安之路
date: 2023-03-29
fetch_date: 2025-10-04T11:01:27.060544
---

# 欣赏一份 APP 后门分析报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjzU3xiaUGlpYElic8pR7iaibXI7DDYbOrRLmCiaJmBcZDSF9GwnfrF7MBnFw/0?wx_fmt=jpeg)

# 欣赏一份 APP 后门分析报告

信安之路

报告来源：https://github.com/davincifans101/pinduoduo\_backdoor\_detailed\_report/blob/main/report\_cn.pdf‍

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjchvA96uzftbJ1EIialbBECibicJTyXd4YMrWspmJujJtXoqU9Uotlsc8w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5Uj2Jqf3ibvFlLFccCt6GXN1hC61St185pEbvJnIBxUCtytLSapOic9iavhQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5Ujm24DiaBFibJaluuOFxMuJUVQQ4norBGhLlyvSCicADYGMtKfDicPBKzBSw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjtLOqGzbGYLvsKOx5ByJiabFuhFWYnwh8gI0WLgNKy9O3gCovUibFd2Xg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjUrLCoMC7Bibpmy9ibZVoXNrCDMB2CC5JGE1DIVThCZ7Z5hOp60neIQ5Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjOUcdQUluzh6kiaybKIeiaP6FPI7kcwDK8NRLPaChox4kufbKtblakbYg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjDLbobhEqQsMRRGm7iauKshYk8y9R408l2crfw2HTkVmtpCQGwHvft6Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjyjkxKhot8K0dyHwfgpLRlCE7A60JQdRnnhe9giaubXib8bib5CMoBMYcg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjrQibcpSJfTgA5riaFviaibzcjcZF6OBbcA91vqLmcyiaYYoMg2ysXOW1Nibg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjicGvTpTwWNVU4d7B96KR9N7PcRfT6bVeg6lo9IxqLLRUUtQaIEd5vIQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjMNAMxHmASTM9pHfWr9A0oILAmpEYItEOJedCWpBpOR6uQ9eCLdYukA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjYzVOXtDN4O4booBqmujR9icK6LYRBAtbibO8rmulefmlXn6XMiaSpFpjQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5Uj4YD3qS50WIZmm5AcXuuAPheTJRSiajT8NSibJvKjYIqNyKVUfVOCG7qg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjQAtWamXApE2r9sb6FVd7PwVb4w6yeMykZdFgX1GPvqCu3M0x2GhZ9g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5Ujm68PPCyS4a1eo1HeFibQl8NDsQJZfR4hZ6NL99iczPYw2rOAkW3xHT5Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5Ujib9ic0ru2418Wgbw7fPo1VEr2ITxPrGhzqZ9uxjDz53N8hMtUtOayhdQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjK3C0RtImZVDt9f2ohmyl8eOhUPibfOdiaKNAgNicfTYhNKAyuID0pfv0g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5Uj0eAPpxA5HvCWDJmwsaxepbQg4dVxAKPvqriakQBuXT3JkOu6R1wWzHQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjibjzblgmcZ5nHpP5IbVhzvbhJetpEsxRvmddGmktBzKIcaA4Sktpdpg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjU3Ys7UxDkmUZL685vWCzicWPAWY0Libgj4saGwgFDZw0NGic3A1UXnjUQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5Uj6iaUgHLhB3tsMAVgA1zp44lIrX4P8RmvuP9Cqs9eTrRnGnKWr7nDupA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjY8zTPg3s0713q0SNkiaYibNjEl4gegOKhoOWcnB03eGfoxbKaXj9lYTA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5Ujq6n4uoUl2TrKSZvjQ1fQvWVModVfwOTUKYyeRv2VDtsm4BwvtDxn0Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5Uj6RRKneYs1MJHwaYa9pR8tSfaVR6S0juiaOCfrabrtH9b3hZgmzQbJdQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjCHoJwzb1tsqia3ToRgWfuUkgskXmIqGoNk9lIB1VEFryxwRO8CT5qVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5Uj3ToMROvmyI6fDu7knmxdfzlMXczP65fnd9JC8xBLVhrsC5Y8Yn5dFw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfdB5yN7BKUXOe4qvibZiar5UjVh5PcVDIaG0fciaRvYT3DUM3n8MOejJFKP6OX8mDpf1SMZLicbNRMoVQ/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

信安之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

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