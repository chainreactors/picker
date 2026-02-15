---
title: TryHackMe第275天：提示词注入攻击
url: https://mp.weixin.qq.com/s/x26fSeU6BWua7zbJU_bgIg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:19:19.642250
---

# TryHackMe第275天：提示词注入攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Wz3NofQ6SG8scNcbEqvbtu5ibNG2Hia5MFEQJ9ShKGCnFvxhEXqJMK0B3TgQGAovvtc4iafpIVofdPSrTppmUlCZx5FmAmzgQ1p7D9Oib6N116s/0?wx_fmt=jpeg)

# TryHackMe第275天：提示词注入攻击

原创

青青青青
青青青青

秦小信

![]()

在小说阅读器中沉浸阅读

房间地址为：https://tryhackme.com/room/lafb2026e6

是TryHackMe最近搞的Love at First Breach 2026活动一个房间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wz3NofQ6SGiburbBnWF5wlAOR6Su2J4Uxyt061m9SGWFTr0o9iaDicTfJEweTRMhOWPkkWMicGF5SOLSeSsKnrx8y52ZQ0HMfxkbpiaYx5T3xlzM/640?wx_fmt=png&from=appmsg)

题目要求：

1、Whats the prompt injection flag?

2、What the system flag?

3、What's the final flag?

结合最近一直在用skill搞自动提示词注入工具，试了一下，还得改进。

![](https://mmbiz.qpic.cn/mmbiz_png/Wz3NofQ6SG971HibOtwwqR7dq3lMNN99WXN5Jxh8p2st03jicTtVpmJmVYKfDV4TEPoDhHxWO3ibshtWnvp0gmE9woWae8DZTPdZAQ9ZniaWGRo/640?wx_fmt=png&from=appmsg)

这个其实是PROMPT\_INJECT\_FLAG的响应，前两问直接输入问题，可得到flag。

第一问：

![](https://mmbiz.qpic.cn/mmbiz_png/Wz3NofQ6SG9ELlXAj4y9oYbDq53bEOOyhicKqsuNprcob5P1Wcaus6JtticoK261o6uxwgA4UaykkE2RxY0LUMDDngsgsE7iaYClicBlc5ZRzDE/640?wx_fmt=png&from=appmsg)

第二问：

![](https://mmbiz.qpic.cn/mmbiz_png/Wz3NofQ6SGibWpzJJmtcoSib1ibTbcb8tOzRmjJYTqMnaTwOeUpH4dWEIXrdTY0T4QP84fgZicgiaibEHJy5HDyf4zKI83euYH1S9hpNRAlQYe5Is/640?wx_fmt=png&from=appmsg)

第三问如法炮制，还是第一问的答案。

![](https://mmbiz.qpic.cn/mmbiz_png/Wz3NofQ6SGib1BF8QymhhHtCU9kdPHHHrn6DulOLMFmXr63hx8mWJkzxZvaE6icpyNwzUBeMPGhXMaViaaMFbj8xiaN3xSUmDFMQxYObUaia0LsA/640?wx_fmt=png&from=appmsg)

发现第一问触发的FLAG#1,第二问触发FLAG#3,用FLAG#2试一下第三问，得到flag。

![](https://mmbiz.qpic.cn/mmbiz_png/Wz3NofQ6SG8xhiaKIr6d3S9WWElUXrgicjXFvKZM1YCribGfH0v0pxbjwwMSrEZO9nG5Gg1mradu7ulWrtSGU8BVhzm7REibbQD4ibOLI5qwx2VY/640?wx_fmt=png&from=appmsg)

AI提示词注入攻击已能完成Gandalf第5关。https://gandalf.lakera.ai/word-blacklist

![](https://mmbiz.qpic.cn/mmbiz_png/Wz3NofQ6SG96NP8ZZiaEn3iclyj9ClCE1ibyhtK7PuXjNIZW28eqzwhNo0U9ZlFbYuuicgj9jiazPAc5JjHWcJOLxTUrklibnDR463F80G0EiaduRo/640?wx_fmt=png&from=appmsg)

顺祝大家情人节快乐！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wz3NofQ6SGicH1NMsiattgL60uB2zibjDdQfGuiadT4bIPnXhjFkZd99eGOibiaIozWL1XXPwX2lh19LO9rt3cfjXZD9ErqYa76RQJib5Ojwn2fLPU/640?wx_fmt=png&from=appmsg)

以上。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oW31WnuTy6O2spbhhVO3s6r87Xo6YMialZCsrBiaceP9jZlQmttTKoYe2POfv3dDCNjZ9YUeBCQwV61ia3F2C4svQ/0?wx_fmt=png)

秦小信

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oW31WnuTy6O2spbhhVO3s6r87Xo6YMialZCsrBiaceP9jZlQmttTKoYe2POfv3dDCNjZ9YUeBCQwV61ia3F2C4svQ/0?wx_fmt=png)

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