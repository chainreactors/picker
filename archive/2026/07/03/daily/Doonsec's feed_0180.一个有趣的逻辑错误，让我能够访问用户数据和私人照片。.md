---
title: 0180.一个有趣的逻辑错误，让我能够访问用户数据和私人照片。
url: https://mp.weixin.qq.com/s/KV-TE4aO6W_HoqGozt92xQ
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:38:28.389666
---

# 0180.一个有趣的逻辑错误，让我能够访问用户数据和私人照片。

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MW9pCm89But0at5ECdhJ0YeWsNVr9A39jlpLkyoAicMS4KZS1r9JcBonFjf7umLm33y0mEIib1gmcQaMdBPuHdRskoVzL48icP8dN6LIX7JExI/0?wx_fmt=jpeg)

# 0180.一个有趣的逻辑错误，让我能够访问用户数据和私人照片。

原创

Hamzadzworm
Hamzadzworm

Rsec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：IDOR

您好，又见面了。

这是 Abdelkader Mouaz，又名 Hamzadzworm。

距离我上次写文章已经有一段时间了。

今天，我将分享我在一个私人项目中发现的一个有趣的 IDOR。

我当时在开发一个允许用户上传私密照片的私人程序。每个用户都有一个由 12 位数字组成的名为“OwnerId”的 ID，这使得暴力破解非常困难。

我首先注意到的是缺少电子邮件验证，所以你可以使用任何电子邮件地址创建帐户。

我使用不同的临时电子邮件地址创建了多个帐户，我注意到每个帐户都以特定的 9 位数字模式开头，而最后 3 位数字保持不变。

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/mmbiz_jpg/MW9pCm89BushicagcCibnwjQicINDyiaXW2D5DyIzVLcicyIgu4WRLcBIiccHpmZO4uviaiccrm8FFQcT8DecYicMeskGxic0G2qNoRRl7oakKywhLRPg/640?wx_fmt=jpeg)

在测试过程中，我试图确定是否存在 IDOR。我将照片上传到两个不同的账户，并开始分析用于共享照片的请求。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuvJPmUrib2OVUps4RicTveMLz0zalZcSxL2RoJia3dbUpJsTTNZGC5ha8sUaT99kKaiaFkWNBVjicBD3ibsVQ9LIdZDUps0K8KDS5M6c/640?wx_fmt=png&from=appmsg)

在此过程中，我注意到其中一个 API 端点在共享照片时接受 OwnerId和电子邮件地址作为参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89ButffSQL92hrwd4ZGgQXCLR394NP69gmaKSObxaudXza3YQdyzOJyXBNGxK19wplb2fADNQtFDbiauLd8kI0wrn39WUXWOoJicsVE/640?wx_fmt=png&from=appmsg)

为了测试 IDOR，我在从帐户 1（攻击者）执行操作时提供了帐户 2（受害者）的 OwnerId。
该应用程序成功共享了属于帐户 2 的照片，证实存在 IDOR 漏洞。

正如你所看到的，这是受害者的照片，但分享这张照片的人是攻击者。

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuuYS2dsbhO5CxYjdZtx0LBTlKXEsKlzW0h43NFgo1hACTGYAc3E0aQBmQLT0z7bXnpMREGric3DRwicrFFJ0IOcaZFuF1aJicG3Ks/640?wx_fmt=png&from=appmsg)

然而，主要挑战在于获取其他用户的 12 位 OwnerId。由于该应用程序依赖 OwnerId作为访问和共享照片的标识符，我开始研究这些值是如何生成的，以及它们是否可以预测。

我跳过了这部分，继续测试，方法是创建使用电子邮件别名的帐户，也就是使用以相同电子邮件地址开头的帐户。我注意到，使用电子邮件别名时，前 7 位数字都变成了相同的样子。

发现前三位数字来自电子邮件地址的第一部分，而后三位数字保持不变。

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BusF1zrvHyCEKnrco64lQTpvxTQlOZecicXQ9sGjC1ftnfJjw5AW4gcClG3t9HsPwW5ggmdlSuUibicPicaNbRC9OIP1pzwae7hofN8/640?wx_fmt=png&from=appmsg)

这意味着只剩下两个数字需要暴力破解了。

让我进一步解释一下：

john = 1234567(00)890

john+1 = 1234567(12)890

john+2 = 1234567(14)890

这表明 OwnerId 的第一部分来自电子邮件用户名，最后 3 位数字保持不变，只剩下中间的 2 位数字需要暴力破解。

为了利用这个漏洞，假设受害者的电子邮件地址是 user@company.com 。我只需要创建一个使用 user+1@company.com 的帐户 ，由于没有电子邮件验证，我可以直接登录。

因此，我将得到与受害者 OwnerId 相同的前 7 位数字。

区别只在于中间两位数字，我只能用穷举法计算出来。

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuvcMPtwD9h0EgdqyA2vzQCUQpvdsK5mSV8ibYR6qibvXU3QJxqfdcNyQDWZR627MMCxeiao1QUibymocO7OsIzSN5Qt3ria9w0oDlI4/640?wx_fmt=png&from=appmsg)

该漏洞实际上将原本无法猜测的 12 位标识符变成了一个可预测的值，只需极少的努力即可枚举出来，从而导致 IDOR 和未经授权访问用户的私人照片。

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89ButLOAsKTebA7cyCHACbpwnFmwgze6ibibjudGMe1lbffYYh6uNF3v81cMdJAVUeDvY9B0G8wPKvLq7voJE9SoqcBoVQGVQPiar19Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuuiaO29vWyz5LlnM3ewpJGW0CNZViaVnnTrUm1TJsicM21snwuJGEt78UF6JfUTDUJ8Nj0XO5Nd196MhMHlK9UaByERJrl0Xp5h7o/640?wx_fmt=png&from=appmsg)

我已经有一段时间没有分享文章了，希望你们喜欢这篇文章。

祝你今天过得愉快，我们下篇文章再见！:)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

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