---
title: 震惊！靠“复制粘贴”躺赢CTF，解题率91.7%！
url: https://mp.weixin.qq.com/s/7Eb6Jxy1LCeGJFaq8-wE9w
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:25:43.558258
---

# 震惊！靠“复制粘贴”躺赢CTF，解题率91.7%！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jUhNzoiaRDZau96e8M0Qgy8PsIzP00K6h6jF0c9UvksLUw1ibiaOukHv4TVxCNYYzYxiannMtX9uyoJ4KxnKFrzwlmoajcJdEXupZ80rcPNNJ2A/0?wx_fmt=jpeg)

# 震惊！靠“复制粘贴”躺赢CTF，解题率91.7%！

原创

南风
南风

南风安全站

![]()

在小说阅读器中沉浸阅读

点击上方蓝字关注我们

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5dOB5NL4uribqB8wYibcz5ibt9hfcIKNIo76CO2l5iaYxa6oJ3gJxB5iadpOYuL8s6QNnXQe8k7cxQiaCI7XicUqkZ4zMFTaQtdFnnNY4kW7G2Z2mibA/640?from=appmsg)

> 新瓜保熟，最近一个CTF选手，不靠0day，不靠逆向，全程靠当AI的“搬运工”！仅靠复制粘贴，结果一个人加一个AI干翻了900多支队伍，解题率高达91.7%！细思极恐。

01

# 躺平CTF实验

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5Y7Eyy4bglGfaNvLRIrxfj40JNhmvytB9TerOFzzuO2bntp9Wys2IEKmEibB3Okkiantic6r7a6hH1onPkydXffvUkznEIOu0ascfesKJXTbyXg/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5tXhCWgvnKEkyLxknxRqz8R6UiaSYILgiaNfpDsutmeTtgK5N5hN93gMutib4yLicChOibR1HcGYNDry6NGM8dOz1Oq6K1ibJIxxokGOfWcIDZllfw/640?from=appmsg)

南邮NCTF 2026开赛，某技术宅正愁token套餐用不完。灵机一动：准备完全依赖AI单刷团队赛？ 说干就干！目标是：不写一行代码，不开任何逆向工具（IDA/JADX都省了），不给任何技术提示！纯做“题目搬运工+复读机”。

![](https://mmbiz.qpic.cn/mmbiz_png/jUhNzoiaRDZYdtPQJkq2zXQESLaqU1abvuibicicptNez6ibmiaiciamvZGtCiaAbkMqkUDBxMwCohQPq2Uh2A4vnYkY69nqOUuYjO0NA0PhcttA0mfM/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/jUhNzoiaRDZZ3JZtLx30zxjEAkJWNEz4YpOC62FmmALjs6M934GB1QcdD9ODBqRSSs1DergGWIG3rmIqj0IDKW0GwibPP3K0nxbojCQoKNCsY/640?from=appmsg)

02

# 关键解题工作流

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7eWG4Be33F0SQ5ZBzjj8P5PwuNYhC81sjcndrbHSnDMjOI1YicMGwUUDeDEacFc62YNm3akoKCHn3RMU0A5RWCuoa5icbDQqRmyPqs4bO50XEw/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6Az1Lop1EnMVdtBKQEAp1hLEwBOfoYeE3RNTNz1pibN8hhjl9Nbcbmic6DoFISrhK5RSRIzvuicD3EftcibXFdL0Obr8iaLcexBibpUaqiaH8y818Fg/640?from=appmsg)

01.

# 武器库

Codex + GPT-5.4

Trae + GPT-5.4

02.

# 工作流

搬运： 把题目描述、附件原封不动甩给AI。遇到容器超时换端口？再告诉AI一声。

装死重试加PUA：绝对不给提示！AI卡壳了？只回复三句：“重试”、“换个思路”、“这么简单都做不出？再想想！”。

全程自力更生：自己装baksmali、Androguard反编译APK；自己用objdump、gdb搞二进制；自己上网找webhook.site收XSS的Flag；自己搭环境、写脚本、调exp... 失败？自己反思迭代！

03.

# 结果震惊一整年

比赛结束：24题解出22道，解题率91.7%！

总排名：34名！ （总参赛队915支）

比赛期间带娃逛商场、打麻将！就靠ToDesk远程瞄一眼进度，给AI喂个新端口信息... AI在家默默打工，Flag就堆满了屏幕！

![](https://mmbiz.qpic.cn/mmbiz_png/jUhNzoiaRDZZHmuDqViaFf8jmibQV6lWlsiaibQrJj3COh1N9D0XwGYBRUrypnAlrvnpzFJLqBfICYHotDeFFia7reuJ7CR2BgLmia2eMuT1rxUc0I/640?from=appmsg)

急的出题人紧急喊话！

![](https://mmbiz.qpic.cn/mmbiz_png/jUhNzoiaRDZaYK812ppttib9OCqYzC05rgH5jA9sFl2E4xfWnYy9ul7V17S4ID2l5ibGTApH9miaSKa9cn55YaDBpH9Fmx1bMxrBRaCdD41LgF4/640?wx_fmt=png&from=appmsg)

03

# 深思

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5Y7Eyy4bglGfaNvLRIrxfj40JNhmvytB9TerOFzzuO2bntp9Wys2IEKmEibB3Okkiantic6r7a6hH1onPkydXffvUkznEIOu0ascfesKJXTbyXg/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5tXhCWgvnKEkyLxknxRqz8R6UiaSYILgiaNfpDsutmeTtgK5N5hN93gMutib4yLicChOibR1HcGYNDry6NGM8dOz1Oq6K1ibJIxxokGOfWcIDZllfw/640?from=appmsg)

对安全人：凛冬将至？ 一个只负责“复制粘贴题目”的人，靠AI刷出91.7%解题率。这意味着什么？大量初级渗透、安全研究员、甚至部分中级的“传统手艺”岗位，岌岌可危！ AI抢饭碗不是预言，是正在进行时！

AI是洪水猛兽，还是涅槃机遇？拥抱AI，升级自己，才是王道！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0TDzwbv8GFibiaqup1Sn9SWDPQGpr7KEAicOknBWP0soQJA2zV3B7vJLUyJe4y8mWJY5DiaKTDpeC8ZwQ/0?wx_fmt=png)

南风安全站

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0TDzwbv8GFibiaqup1Sn9SWDPQGpr7KEAicOknBWP0soQJA2zV3B7vJLUyJe4y8mWJY5DiaKTDpeC8ZwQ/0?wx_fmt=png)

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