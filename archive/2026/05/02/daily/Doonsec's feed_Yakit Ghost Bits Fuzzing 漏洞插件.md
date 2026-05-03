---
title: Yakit Ghost Bits Fuzzing 漏洞插件
url: https://mp.weixin.qq.com/s/Upi_9mWnFntdpZiIv_I7Qg
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:23:04.389327
---

# Yakit Ghost Bits Fuzzing 漏洞插件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVnIA6FibPMzI2q5owSViaPo76WjSYr5m3tFOyM2lluzBeT4ic48tM4WMvibNOruwWYto2emvPUjcSib9m1boT70icpoAG9zEt1f6mJ2c/0?wx_fmt=jpeg)

# Yakit Ghost Bits Fuzzing 漏洞插件

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 87，阅读大约需 1 分钟

## 前言

Yakit 有三个 Ghost Bits 官方插件
![b1383da422e9fc6a79b16ea171e346d2.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlzcWcK06sm1tYv1SkAbu1e7HEkobdm2nX0oyictlps8ttepeRMLpIHSIsbM1bQtYcg1uGRX3qic2xR7QBrxQEJKlrr8NOt5SnOc/640?from=appmsg "null")

b1383da422e9fc6a79b16ea171e346d2.png

* • Ghost Bits Fuzz
* • Ghost Bits 编码字符串验证
* • Ghost Bits 编码

## Ghost Bits Fuzz

列出了常见的 Fuzzing 使用场景
![2c22b5d0781d1032345e4c9aaa6e5a6f.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlO30NI7EKDSzORcMBdiaYNLrljylqpuZX49EVTrGibibQ2D9yBfP8oswaFKXh3VdC08XSLWvC1Kyt6tBEMntYI11Ql8tyxiculkHU/640?from=appmsg "null")

2c22b5d0781d1032345e4c9aaa6e5a6f.png

**搭建靶场**
https://github.com/vulhub/vulhub/blob/d277a8693e588684e951dddb0733809e53881a3c/spring/CVE-2025-41242/README.zh-cn.md

验证
![acee5f1cdb0e7be4274efdffa07a892c.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnAEF9msK7hrTF0v1ztcqwicGaFvJDw3JMjciaJjlyDVQ0RBDUvyBJGMhj2rZ4O1V6mGEJT1HdbDboAwgZXFrkIPFNsUjUjrJnnc/640?from=appmsg "null")

acee5f1cdb0e7be4274efdffa07a892c.png

结果
![3a6e70b9973c245d68608cd4493d46c7.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmP68Yphz6iblfcc5VZG0FUDEXhgZbVqpUBbEpd2wL0crsRJKsaibLESMDibxcHU5KNWWylQS6cb9mBtlGVZVfHwEEicnNiaxF0OIsw/640?from=appmsg "null")

3a6e70b9973c245d68608cd4493d46c7.png

## Ghost Bits 编码

![94fe23e3cb9d0d0e96bcc8225d357be8.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmo5qeV6z4vJg3Ky3OrXObV47l8pxibpeLdTtP6uaG0dGLCVELCkTxm3WShz2oDtxKVj3BAUyUiahv9pK4jmpdYQwd3bVzg3TCgc/640?from=appmsg "null")

94fe23e3cb9d0d0e96bcc8225d357be8.png

## Ghost Bits 编码字符串验证

```
/etc/passwd
/孥聴镣/蕰遡乳蕳穷聤
```

![4a8ddbf0719732a0afa758516ba2392a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl7F20eP9H7iaWhiadU3lAezF689Hf3cRsCl7L2xyfyrBh26KORtUxLgfF3qcNJbicpIict1Qnpdtt6yDn5h6KyEw5cXtbNS4PiaHgs/640?from=appmsg "null")

4a8ddbf0719732a0afa758516ba2392a.png

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png&wxfrom=13)

声明：文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

如有侵权烦请告知，我会立即删除并致歉。谢谢！

文章有疑问的，可以公众号发消息问我，或者留言。我每天都会看的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png&wxfrom=13)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a1BOUvqnbriaKQaulUawUmcqevsicgRXaDWWcgmsbG7iaTtKE89ZwJEkPHzibEzXwcibLn8PKu1hGoicqAEIW9uQjyBw/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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