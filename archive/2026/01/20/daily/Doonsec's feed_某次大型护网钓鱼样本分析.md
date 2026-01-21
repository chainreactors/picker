---
title: 某次大型护网钓鱼样本分析
url: https://mp.weixin.qq.com/s/HT1llid84VHeMnW40A7WbA
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:30:35.888027
---

# 某次大型护网钓鱼样本分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwca197xacHT3vyAEVxaamRS9nwWVCB3lYoCqFvUtsFI2Z7Lm0OicnUvA/0?wx_fmt=jpeg)

# 某次大型护网钓鱼样本分析

原创

wdh
wdh

照夜清网络科技

![]()

在小说阅读器中沉浸阅读

首先打开文件夹，发现pdf文件类型是快捷方式，打开属性了解到该快捷文件运行的是attachments下的runtime.dat文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwcTUgZfZ4TZ1nZv8uiaKibibNWJNEMgGRKR2cHHn1BBjOuYiaicXBUZ0VbRA/640?wx_fmt=png&from=appmsg)

发现并没有相关文件，猜测做了隐藏：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpw0adSswLfBfR9tW3070VHLWgsV6htJUlKVoBeODNzAiavA53qiasEBL9w/640?wx_fmt=png&from=appmsg)

关闭“隐藏受保护的操作系统文件”后发现该执行文件，打开并分析：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwvtXzMSb6KojPzWbVt96Vt3t7tQN4micuxutWd9BhibmDUNgCVuOzcgFw/640?wx_fmt=png&from=appmsg)

分析发现解密了一串混淆代码，并执行了它，这段代码通过循环逐个字符处理长字符串，核心解密规则是Chr(Asc(Mid(原字符串, i, 1)) - 6) —— 即把原混淆字符串中每个字符的 ASCII 码减6，再转回字符，最终拼接成Jiam变量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwqCwPXl8Z6vQyITQfMvqnNc5bdX2H1jpWBAsuicIp0WaIzVRws2FQ3kg/640?wx_fmt=png&from=appmsg)

让AI根据相关分析，写一份仅仅针对该段混淆的字符串的解密代码，并保存到txt文档里面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwJdUfK5V3nu7ycTekkdq6StW4DGsvxxjjEcm2rnbNiaPtTMIk3bhM5LQ/640?wx_fmt=png&from=appmsg)

得到解密后的执行代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwRchaCZ9CZrPzS92kKGIKNNvE46XjKqtxI5XibnnHVe9keaSW2jk2ovw/640?wx_fmt=png&from=appmsg)

解析代码含义，首先将该\attachments\.files\plugin\_1 文件重命名为《北京建筑大学-李.pdf》并移动，短暂判断plugin\_1 本身就是pdf文件，添加pdf后缀：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwnfofsubCZxzBVAt2XbETz5LyQnxID5MtadHreuLrUiarNedeJM8RKQw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwt6iafWFibM705k3ictxDOPzTwJP066be9M4EXJI4qBuedUCoulOGOxsTw/640?wx_fmt=png&from=appmsg)

然后会删除相关的lnk快捷方式，避免留下痕迹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwkS44orImS27DnJUzIwTPjiatgEIl0fYYMGbqdcnvaIOz6cQWwEAW6IA/640?wx_fmt=png&from=appmsg)

之后会创建计划任务和定时执行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwnPrRu1NkNKPwZR7E798VibcdUyicuvPmD38gVKtgAGfVSbs8HZI1ibHkg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwLdEoX3hhvPh73dcaIBhKcpbWaetQdaZoZnsMjnN5d5FxZvdP8UWetw/640?wx_fmt=png&from=appmsg)

解密后：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwacjpLRLxxRS5XqdwNue1Mp8zZ1amzSViah6GTZFdtolHr5X5dCYPpFg/640?wx_fmt=png&from=appmsg)

上面保存的\1,\2,\0都在代码里面被拼接成了exe文件并静默执行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpw7bD1LHx7GS3d5qkpQ0mOdbYnbehtZLn5QFNibDtx1gbvIMkIBfug1dg/640?wx_fmt=png&from=appmsg)

经过base64解密后形成对应exe文件。

点击钓鱼链接，查看是否是按照分析执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwJsiaGqpGrMGRsicKa6b2WXclzgBKdONWy1Xu3gb1kSH2neh0hIyERxAw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpw44PEC90pCV1K9qvXclX7UCMNAeQxe6UibZX7x0KTddpPBE7caqywzuQ/640?wx_fmt=png&from=appmsg)

这时候可以确定恶意软件，对恶意软件进行分析。

由go语言编写。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwBibSI9gHeGzOIVPDyiaraIbia15INnjEkEXANPOYRP4bsB0rlaYiccRbmA/640?wx_fmt=png&from=appmsg)

进入IDA

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwMFnHpE9sjahhOqXWCswr1Tpwq7Le2DUaNV0TUu5bsR8zC2hamGJvZQ/640?wx_fmt=png&from=appmsg)

1. 找到main函数的入口位置
2. 经过分析2处代码的含义，判定为混淆代码
3. 3处为AES解密函数，跟进去：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwIE8SYBWmvhqsny6Y6njXAetptjboNJc7ywhd9f6YxawuyEOercEKyw/640?wx_fmt=png&from=appmsg)

发现代码逻辑很长，我们采用动态调试获取解密字符串：

找到解密前的字符串：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwfaR28R3OzzcQkGwMsnkgNQELnjsE4LQAqH5RSvQzM4ftTlZeEVUweQ/640?wx_fmt=png&from=appmsg)

找到字符串所在的位置；判断222.5379E0函数为解密函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwr0iaibicOsKoX2kviaCfTQpcqGwV5jE405RnRCF41nqt7dngyicKIf6IftA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwia4oP49Sftiaua3AsXpko0AfKXmwibDTfMFftjS1UZFRoIHTQic6tJkRmw/640?wx_fmt=png&from=appmsg)

我们调试看字符串变化：

可以看到字符串变化为Global\\88d58e63-7fab-49cc-bc4d-6b4fd24f6e5d。，暂时没有相关关键信息发现。

接着分析，暂时认为" main\_mutex\_Acquire是进行互斥锁，确保当前只有一个进程连接服务器，降低了被发现的可能。

通过判断，我们将目标锁定在main\_\_ptr\_BeaconClient\_Run这个函数，通过翻查资料可以知道：main\_NewBeaconClient里面知识声明一个对象，后续实现在main\_\_ptr\_BeaconClient\_Run里面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpw4IDodEJMqDnkvFrfZydsc6A2vibAvYCh4WvuLcjNUpjnrjz0qLjHQxQ/640?wx_fmt=png&from=appmsg)

动态调试到该函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwVjzuMib0Jd6YCvpW008QTbfrQVDrTdDOsJG5ibI1TrsXc83PCzVhrobg/640?wx_fmt=png&from=appmsg)

找到一个建立连接的函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwtXuYbPIKa3ofH2VJicW8y6e43Pic9AIh6qnPT0SqAoedWxia87yrTZUiag/640?wx_fmt=png&from=appmsg)

在动态分析里面找到他的入口点，进入之后，很明显看到了发送http的请求，我们进入httpget函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwE8nfeRJjMrNtxjYz9QPz0JJjRyoezu8eUqBfCeMAC3Yga8ib8Z093bA/640?wx_fmt=png&from=appmsg)

发现了恶意外链的IP。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwdGenBLAdbhKF7JCzqJ3yuJvPicibHX3Kqib6R9j46Jic8MSIG0tgLSt6iaA/640?wx_fmt=png&from=appmsg)

通过进程监视：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LacLedJ7BicdYfsGCNTnfAYpwO8oFaA8GTL7u51I514AGmGlsU4pVBHRbxU9erkWicpJ5MhDUy42t3uA/640?wx_fmt=png&from=appmsg)

当然，我在实际测试中也发现了相关反调试，因为篇幅原因，这里就不多做介绍了。总之这是一次很不错的样本分析体验。希望对你有所帮助。如果哪里分析的不到位，也欢迎交流探讨

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LafVoHCH05Wd0EPtOu1AkoetmINp14nOcpFXqpaCLXGWAnBvCMXiaZrmmLk0dLjtJKmgAiczRUib03HgQ/0?wx_fmt=png)

照夜清网络科技

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LafVoHCH05Wd0EPtOu1AkoetmINp14nOcpFXqpaCLXGWAnBvCMXiaZrmmLk0dLjtJKmgAiczRUib03HgQ/0?wx_fmt=png)

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