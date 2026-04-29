---
title: 【主流WAF沦陷】Java Ghost Bits新型WAF绕过
url: https://mp.weixin.qq.com/s/BiiCVSoVz6u-tCyIDbMZ-g
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:07:59.908674
---

# 【主流WAF沦陷】Java Ghost Bits新型WAF绕过

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/14zTrTiaCfEX6TFaWAuJooMvBBGSYodgCJcx41GicPk8yxQFEuV8tudUTO4DclLUia7rcVTtPGdibicEtGo1thg0VjsFGrRLUa8wQMu3oTFCMn9c/0?wx_fmt=jpeg)

# 【主流WAF沦陷】Java Ghost Bits新型WAF绕过

xiachuchunmo
xiachuchunmo

银遁安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

前情提要

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

    最近Black Hat Asia 2026 上，关于 Java 安全的新研究Ghost Bits引发了广泛关注，这里简单解释一下什么是Ghost Bits，核心原理其实很简单：

Java 中：char是16 位byte是8位

如果代码里把字符强制转换成字节：

```
(byte) ch
```

就会发生：

> 高 8 位被丢弃，只保留低 8 位

例如：

```
陪 = U+966A低8位 = 0x6A = j
```

也就是说：

```
"陪" → "j"
```

    这就产生了一个危险现象：上层系统看到的是中文字符，底层执行时却变成危险 ASCII 字符，这就是 Ghost Bits。

    棉花糖的文章已经有详细解释了，这里就不再赘述，链接如下：

```
https://mp.weixin.qq.com/s/Utx64ue7Phs44pCHrpJbrQ
```

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

复现截图

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

      注：Burp\_Suite无法重现此漏洞，因为它在发送请求之前也会将“阮严灵丰丰甲来”转换为“.%u002e”。可以使用 Yakit 或发送原始 socket 数据包来重现该漏洞。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EqS9GE77r0OicavkqgX2gZmdMdsH8ETT4JdibhW3ibzCnUqoh0pSKeCUZLfRppFexarQSAodrUegOM5LhswREV4TfSWfCA9KTb2XskxFJAASuk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

（注：复现截图取自长亭安全应急响应中心）

    以下组件已被确认受Ghost Bits 影响:

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/14zTrTiaCfEWOpndA31gNhyO9unkzEwjZfbL4ibnZxPHufA7ybjZkZ9P63oGsibsCAkXNtduY7MJicTYWpjabV2dnhMMfflYIQaxVgRaxeVdhuo/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

文章获取

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

    原文是56页的PPT，PPT 最后想表达的观点也很明确：现在看到的只是开始。只要 Java 生态中仍然存在“Unicode 字符串 -> 低 8 位协议字节”的错误路径，Ghost Bits 就可能继续出现在新的组件和新的漏洞链里。如需要PPT原文可后台发送“2026042802”获取文章。

![](https://mmbiz.qpic.cn/mmbiz_png/14zTrTiaCfEWwuR3UctOpvgviaMEz2dYDrn5BVQnqibyKhjpDIdQntNQeSzWm9E29on8YoI4DgE6rMjaCSqsjf28bWdn0SjLZPlcRsj3GI7JnA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/yeJvia5dNx5icXzsEiaLXHHFs0v3Zzo3ibYj9Y6SBu26OWQAsgiaLcrnyB0Po1euQDCO2f8vs3xwGVvHdOiavXbqgqOg/0?wx_fmt=png)

银遁安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/yeJvia5dNx5icXzsEiaLXHHFs0v3Zzo3ibYj9Y6SBu26OWQAsgiaLcrnyB0Po1euQDCO2f8vs3xwGVvHdOiavXbqgqOg/0?wx_fmt=png)

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