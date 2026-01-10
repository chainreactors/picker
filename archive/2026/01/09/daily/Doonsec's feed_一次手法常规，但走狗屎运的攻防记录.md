---
title: 一次手法常规，但走狗屎运的攻防记录
url: https://mp.weixin.qq.com/s/sK4N_PQ9wdgNMI-8S8W9PA
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:26:39.737618
---

# 一次手法常规，但走狗屎运的攻防记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PVHs7dHw162ibib4bV0icHjVVKTwdJSEY0m5lZbhEkQEzia97SePiaWBHia4xxepicJE9hb4Z4DnXzoXu5TRtiaibRwZEfQ/0?wx_fmt=jpeg)

# 一次手法常规，但走狗屎运的攻防记录

原创

犀利猪

犀利猪安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC6CankDUFDurKHNPv6c9ko5AqkwHqWpfosEJZolyMm7jQJgETLL5c3liagnTI6wSibQyRKJs5uBBgFw/640?wx_fmt=png)

**免责声明**

文章内容**仅限授权测试**或**学习使用**请**勿进行非法的测试**或攻击，利用本账号所发文章进行直接或间接的非法行为，均由**操作者本人负全责**，犀利猪安全及文章对应作者将不为此承担任何责任。

文章来自互联网或原创，如有侵权可联系我方进行删除，深感抱歉。

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC6CankDUFDurKHNPv6c9ko501vNgyKf1ImmVAia8gkDje5L6Q8CyuBwNuB2ic5r5ql7ZgBROPgD37Aw/640?wx_fmt=png)

**0****0**

**文章背景**

    一次攻防的记录，手法常规，但运气还算不错。由于种种原因，本文相关图片将采用厚码呈现，各位师傅主要参考思路即可。

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw162ibib4bV0icHjVVKTwdJSEY0mPd1txHttNJZMs761bZAo0aqhb05ewQtJoXINibar7SF6yZu5g7F6hibw/640?wx_fmt=png&from=appmsg)

**0****1**

**发现盲点**

    开局只给单位名，通过收集资产获取到域名，访问页面只跟我说了一句Hello World：

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw162ibib4bV0icHjVVKTwdJSEY0mBhcxTws43SIOP4H8h6bV3vCCKRRvHoETiaYoYT72sxKicxIFr0m6DJng/640?wx_fmt=png&from=appmsg)

    既然能访问那就是有服务，先扫路径：

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw162ibib4bV0icHjVVKTwdJSEY0mZ8nzibftGKibpLYibeRxSwYefe85JVlVWUz13woaibicpXB7bLibv0ibhz6lw/640?wx_fmt=png&from=appmsg)

    运气不错，真扫到一处路径，而且看起来还是后台的路径，疑似出现了未授权，因为单看这个路径它理应是需要鉴权：

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw162ibib4bV0icHjVVKTwdJSEY0mfS83ib56eO7ydLc7UP33TIz9M0a8N96IIjqrIJ2B8KBykZ9eZrqw01A/640?wx_fmt=png&from=appmsg)

    然后瞎几把点，插件探到一个注入：

这里插播广告，欢迎各位师傅

使用我们的二开瞎注插件

```
https://github.com/AnQuanPig/XiaSQL_Plus
```

![](https://mmbiz.qpic.cn/mmbiz_png/FIBZec7ucChhZqvOVoz3euT3icYwAAGMrYuUVJWVHicKOyPNmOGv71vVzBmPNQUq7Pc0NiafbACHTrPfDCxaCwMow/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw162ibib4bV0icHjVVKTwdJSEY0mOuRBnibl6t6kkFgE3w8icIjzvxw12ENFezHGRSUITMJOicBib0NWC8l1nw/640?wx_fmt=png&from=appmsg)

**0****2**

**几十万数据**

    接下来，直接掏出sqlmap梭哈：

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw162ibib4bV0icHjVVKTwdJSEY0mrPlBicH3hVJfblXlEEWvUolzoibPkZU7fzAXPNX7LYXYjJR0qhNf1uXA/640?wx_fmt=png&from=appmsg)

    嗯……DBA了，可惜是mysql数据库，条件不够满足，没有直接GetShell的条件。只好换思路了，转手先尝试获取数据：

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw162ibib4bV0icHjVVKTwdJSEY0mKsddfpCOcUJW55yLpia5LYiaV2o8s3ovn1J4WP8UmBFpcqFb1iaiaJjQMw/640?wx_fmt=png&from=appmsg)

    运气还行哈，有几十万，数据分打满了。

**0****3**

**寻找上传点**

    正如之前所说，没有直接通过注入获取shell的条件，那么只好找后台，登入后台查看是否有上传点：

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw162ibib4bV0icHjVVKTwdJSEY0mD4RbNmtjaQP46gEz0Q6JuRFku6auQ6zg4dWkKYI4u72dQCbbZqbFgA/640?wx_fmt=png&from=appmsg)

    找到后台了，通过注入获取用户，惊奇的发现管理员是被锁定状态。无妨，虽然没有直接GetShell的条件，但我们有DBA权限堆叠注入，直接通过sql语句解锁管理员：

```
python sqlmap.py -r sql.txt --level 3 --risk 3 -p id --force-ssl --technique S --sql-query="UPDATE user_admin SET type=0 WHERE userid=1"
```

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw162ibib4bV0icHjVVKTwdJSEY0mEfKicMTWk8XZF8ibpVZiaWhmMJCgJ8y6iaG0xicQ3khrJVUX8S8b6PnXO4w/640?wx_fmt=png&from=appmsg)

    好消息：后台进了

    坏消息：无上传点

![图片](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw161icjWTvicuWEWm8BoCfdcXbaSVgLmAK4bVOChNicU7Wxiap0rHTY1FJdCxz9a4yLXL8UHhjoqOz3JFdQ/640?wx_fmt=png&from=appmsg&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

**文库账号**

**血赚价格**

**HOT**

**55.8一年，短时间内价格不变**

**后续只会涨，不会往下跌**

**登入后在文库同步获取各类资源**

![图片](https://mmbiz.qpic.cn/mmbiz_png/FIBZec7ucChhZqvOVoz3euT3icYwAAGMrYuUVJWVHicKOyPNmOGv71vVzBmPNQUq7Pc0NiafbACHTrPfDCxaCwMow/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

**内含POC、各类学习报告、学习文档**

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw163ebibEH089ficwRu5qkbMHaj0Oylj2qnictdFukxKshjs5mSibZaq3Hy8QJmrfbOJicC32YVRVzpkB2jw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw163iasWb5aWRFaB5bravMj1JegScul3xTooMWHO2unK500A98mMygh28RKjm1wvNM8IKnJic84GEt2og/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw163iasWb5aWRFaB5bravMj1JesIFtN7nN5ibmP9KHnoQpTCpPiaiaoocYC6zNXsZDlYzYeQoh0Dicu8BJ7g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw163iasWb5aWRFaB5bravMj1JeJ1k7MYQTPiaGiaksibzlJZEdlJzwniahlpbjpGrBapnpZKGU4rdLGIwiaJA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw163M2MLMxLUI8kNiaiasC0YZ2wjGcmTkibicyse7cf9sxySqDkO9vgK4iaYafDDAynwENibcBlm30ENHTk3Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw163M2MLMxLUI8kNiaiasC0YZ2wazPqFiaYibRwa8PrFPMibzpyc9cINURA8DoWa828HRnc0KAOoDTu3OAmA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/PVHs7dHw163nH6MUINlAAdNibz6iaI4Izy4LuoZ7bquVOTMR71nU9KdboYQl4xoGMXguo4X7ojBz8EgZn7RuRYMw/640?wx_fmt=gif)

(

**END**

)

**！扫码添加哦！**

****联系进群即可，群内可交流技术****

![](https://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw160sKTllbdHibe6OmJCO6EfgvVzXWXWAZf1ZKDwutM7fHDXauJWzfGW6wOXwVQqCenGxSKOkYYGByuQ/640?wx_fmt=png&from=appmsg)

**没钱吃饭了，大哥给点吧**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw163MtQy3ZniaJBcOS8ufAic7YYn1MQQDfflq927KF9ymvUcbU1srEJMdwoGYKF4o1xbb3jzmx5ntINeA/0?wx_fmt=png)

犀利猪安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PVHs7dHw163MtQy3ZniaJBcOS8ufAic7YYn1MQQDfflq927KF9ymvUcbU1srEJMdwoGYKF4o1xbb3jzmx5ntINeA/0?wx_fmt=png)

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