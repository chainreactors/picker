---
title: 【接口漏洞第六章第三节】隐藏在“&”和“#”背后的秘密：我是如何通过参数污染接管管理员账户的
url: https://mp.weixin.qq.com/s/TCoaB2A1Dr59aT9ghWRpSA
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:21:05.055181
---

# 【接口漏洞第六章第三节】隐藏在“&”和“#”背后的秘密：我是如何通过参数污染接管管理员账户的

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q0rmz7SS4JWibdG6jgbQUhhvC5weo9nQtFfdxFU6p832S4H8aYIklozJG1ia98UL4UxZ3NFtMHb6jKw/0?wx_fmt=jpeg)

# 【接口漏洞第六章第三节】隐藏在“&”和“#”背后的秘密：我是如何通过参数污染接管管理员账户的

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

在关于“api接口参数污染漏洞”的前面两小节中，我们对参数污染的漏洞原理和利用方法都有较深的了解了，但并没有结合实际的真实场景来进行演练过。今天，我们就结合一个实际场景来对之前的一些理论知识做一次实战演练。

这次的实战场景是需要我们通过“参数污染”漏洞，来污染、发现系统中的脆弱点，并最终实现对超级管理员的接管，进行相关权限的操作。

同样的，访问系统功能，并审查访问系统后一些请求接口，看是否存在一些特殊接口。然后再进行下一步操作

我们发现一个有post请求的“忘记密码”的请求接口，且参数格式比较常见，我们就拿这个接口进行尝试突破：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rmz7SS4JWibdG6jgbQUhhv62mugTibOvTAdop6KtibNicrZ8mGKVBKz9icl7OjDKAE1edCWwhgDwzlAA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rmz7SS4JWibdG6jgbQUhhvY3iayUJGic1fXZsib2yU1XqpCK1rO9qxXn6y6VLac2xwsMk6W12I0icnzg/640?wx_fmt=png&from=appmsg)

如上面，在随意输入用户名后，服务器会返回用户名不存在的提示。当用户名存在时，会直接触发服务器给对应用户的邮箱发送找回密码的动作。

这就非常可疑，我们猜测这个接口就存在服务器接口参数污染的情况。我们结合之前章节说到的一些方法来对这个接口进行深入测试。

首先，我们使用 & 符号进行测试，注意使用url编码后的字符，即 %26 进行测试，直接拼接在用户名后，会发现服务器直接返回了“不支持该参数”的提示信息，这说明服务器很可能是将 & 符号后面的内容当做单独的一个参数，而不是用户名的一部分了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rmz7SS4JWibdG6jgbQUhhvrjanzjwEkI2bq80zRKf84gicn0MibMpPPMjzZic2suP6BVnodibV9tJnKA/640?wx_fmt=png&from=appmsg)

虽然可以判断通过这个符号进行参数污染后，得知这个接口还存在其他参数了，但要怎么样继续挖掘后续参数呢？这个时候就要使用到 # 符号了，用这个符号来进行截断，并看看服务器是否有一些信息返回，以辅助我们进一步挖掘。当然，也是要采用url编码后的字符 %23 来测试的，具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rmz7SS4JWibdG6jgbQUhhvibvibANCA1b1vMg13hckKZTEjyPiaplPgrjxarjCicu9sTEhhIiaW6GR01g/640?wx_fmt=png&from=appmsg)

比较幸运的是，通过这个截断字符，我们得到的系统服务器返回的，缺少参数 field ,这很重要！这说明我们已经做到了第一步，通过参数污染，找到了隐藏参数 field ，接下来，我们就继续挖掘这个参数的值。因为得到了有效的参数名，只是要爆破参数的具体值了，所以在之前已有的参数名和值“username=administrator”后面，就要用 & 来拼接后面要爆破的参数名和值。

同样的，在被爆破的参数值后继续使用截断符 # 来校验，一旦爆破成功，服务器就因为这个符号的参数污染，而不会继续往后面请求。使用burpsuite的intruder进行服务器常用参数值的爆破。具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rmz7SS4JWibdG6jgbQUhhvibcPnBMUSjMNkOzIqCaFu4WKgclJNSVoQiaRxSRr1pKQbQrjvMgvVKSw/640?wx_fmt=png&from=appmsg)

爆破后得到有效的服务器隐藏参数名和值，得知这个参数是有两个值的，分别是 email 和 username

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rmz7SS4JWibdG6jgbQUhhveSW4tWfmdwLhibhhl1T4SVHS8XtFNlWJZSDLXLMHo0ib9tbWIjQuZLUA/640?wx_fmt=png&from=appmsg)

通过以上方式，我们就挖掘得知系统的隐藏参数和值，但这还无法支撑我们进一步实现获取 administrator 权限。我们继续来看系统中有没有一些有用的信息。

在系统的一个js文件中，发现了这么一串内容：/forgot-password?reset\_token=${resetToken}

这串内容疑似是更新用户token的接口，我们前面通过参数污染已经发现了服务器的隐藏参数 filed ,而且是在拼接对应的参数名 email 或 username 后，就会返回对应的用户的邮箱和用户名。那么极有可能将这个js 中的 reset\_token 作为参数值，就能实现获取对应用户的token值。我们来试下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rmz7SS4JWibdG6jgbQUhhvzq5nY2nUeUD4WZQib9ToBXaJFP5RrShpofaIP01ia5qnhujQRfRcPcVg/640?wx_fmt=png&from=appmsg)

发现果真如此，能够直接获取到当前用户的token。通过前面js中返回的路径，还有通过参数污染获取到的 administrator 的token值，我们就可以直接构造修改 administrator 的请求 /forgot-password?reset\_token=获取到的token值 并实现修改 administrator 密码的操作。

以上就是通过参数污染以及结合在参数污染后服务器返回的内容，一步步挖掘并实现修改超级管理员密码并接管最高权限。

关于api接口漏洞的相关内容，这边会持续输出，感兴趣的你，别忘了点点关注。

觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

升斗安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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