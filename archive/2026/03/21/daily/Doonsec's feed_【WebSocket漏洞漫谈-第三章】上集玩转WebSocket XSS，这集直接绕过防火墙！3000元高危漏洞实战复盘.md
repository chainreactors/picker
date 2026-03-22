---
title: 【WebSocket漏洞漫谈-第三章】上集玩转WebSocket XSS，这集直接绕过防火墙！3000元高危漏洞实战复盘
url: https://mp.weixin.qq.com/s/Io5H5vBbGTLCrtgw9QuBxA
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:18:02.352305
---

# 【WebSocket漏洞漫谈-第三章】上集玩转WebSocket XSS，这集直接绕过防火墙！3000元高危漏洞实战复盘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qg1MKHx3jGHHrICZBsnWAslDLesQzGwZYKBN67Q9qPgtyH9wicbZgqTf8klicMtUJkuibZhgg2DpTLfQcPtdmwLoqVTyib5Ev0qZaRDgnoecteI/0?wx_fmt=jpeg)

# 【WebSocket漏洞漫谈-第三章】上集玩转WebSocket XSS，这集直接绕过防火墙！3000元高危漏洞实战复盘

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

上一节[【WebSocket漏洞漫谈-第二章】连客服都不放过！这种通过WebSocket传播的XSS到底有多野？](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447798023&idx=1&sn=d4d1d6ec1624ef8f53c5ac4a28d4991e&scene=21#wechat_redirect)，我们在客服聊天窗口中，成功利用了websocket漏洞进行了xss注入。今天这边再给大家分享一个如何利用websocket的握手漏洞，来实现对服务器防火墙绕过。

有些WebSocket漏洞，只有在篡改握手过程时才能发现和利用。这类漏洞通常源于设计上的问题，例如：

* 盲目信任HTTP头部信息来做安全判断，比如X-Forwarded-For头部。
* 会话处理机制存在缺陷，因为WebSocket消息的处理上下文，通常由握手时的会话上下文决定。
* 应用使用了自定义的HTTP头部，从而引入了新的攻击点。

话不多说，这边结合之前在挖洞时发现的一个案例来给大家分享下，如何理解并使用以上内容。

【悄咪咪的说一句，这个漏洞，厂商给定了高危，奖励了3000块，又可以加鸡腿了】

这边找到了系统使用websocket的功能后，和之前一样，先尝试输入<test>，看看服务器是什么反应，返回内容如下，很明显，系统和之前遇到的一样，前端做的 HTML 编码，那会不会只做了前端限制？那可是太简单了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGEaMqzl2fiakHndTSN499z0mwmDcZ962jyVH1TF11HjCo5zxfa1wTe1P2QicLnXHcgydJeQDE1nBcl0W2UicoEOaxjNfvFr4plBBA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGGOxk9MfIYPKlHcHYMlfZnIHM0bJ9j8hEpZ0sJzibRiboKxGrAprtzxzd3uasGicKCB7Qicuw0zqHwjFHb75HR1eyyx0nGOz8mYH3g/640?wx_fmt=png&from=appmsg)

这边直接将 xss 恶意弹窗，直接录入并发送请求：<img src=1 onerror='alert(1)'> ，理想很美好，现实很打击，发现直接被服务器拦截了，无法继续通过websocket发送消息了，具体如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGHt4uTUr2NbS6DrCFqfxpcVrkWIQSwNheAaiaFEMfbJFBiaG4ZT617xx6zI2iaybStM7ib60AfiatgGx9e0LEDcVkichia2VHkEicYQOt4/640?wx_fmt=png&from=appmsg)

服务器拦截了请求：

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGHm8CWshkIxw5nb8icQkBh4IvvHCYWGVgiaeGVNo3qhibqCLOUorZGv4bovBz5gYRrtb7QFWrF0icsYSeluBIiaJrVCObiaaCYGdEbQs/640?wx_fmt=png&from=appmsg)

被服务器拦截了也不用怕，要怎么做下一步绕过服务器拦截？接下来的操作就是今天的主题内容了，执行以下步骤就可以：

* 将被拦截的websocket请求发送到repeater中
* 在repeater中发起重连，并在重连时的请求头中添加一个 X-Forwarded-For: 1.1.1.1 头
* 找到不会被服务器拦截的 xss 脚本进行注入提交

  （1）重连服务器失败【因为IP已被服务器拦截】

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGHHBAc6nCQgohGKjiaRdj6dDjaRXIR73hr43TwAUibGq1pzGbTgFicAPibD5MBZ9jbkybYaQcIj6KYaqLlHUJt3GqgDWCfsfObad0w/640?wx_fmt=png&from=appmsg)

（2）直接在请求头中添加 X-Forwarded-For: 1.1.1.1 发现可以实现服务器IP拦截绕过，又可以连上websocket服务了！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGHWZebchmuSC7zibSqU2nkhuSWPRb3Yq57wx6k9qlW3DELEibaAnpBZefYO92RnzIn77c3x2SunBuxWRwg3WIK4IOSA8Jalyy0l4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGFpa5ZkBamAYHpm3Etr4KfuiaiaeRqOq0n4ibC7mP56clk6Spjpza2bpaRcPJJVwIibGEtOCpemQbUJgVJnK4m8LUiaxb32LaVdX77Y/640?wx_fmt=png&from=appmsg)

（3）既然IP限制已经成功绕过了，那就可以随意尝试使用不同的 XSS 脚本进行测试了，看看哪个不会被拦截，不会被拦截的就我们想要的了。

如下，使用 <img src=1 oNeRrOr=alert`1`> 后，websocket直接返回了，XSS 注入成功生效！

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGGw8UGcF8eXj5a1kpbL0RdR86Ofhkiaiaoic1wFbmDq1QFTcZS2OwsgyMMYtichHxSc4fIULGr3Fhkb0XJhgzu1LubtBzCY120DZSw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGFiaWVoR6X79OibRbHicODYgTy0YFza0efCgll6tvaRdz2icCibHRzUwxyMDyxP9saI8pgG9Eclz53j4ZRsCdbnExgTdZPAJCiawIHdk/640?wx_fmt=png&from=appmsg)

好了，今天的分享就到这里了。如果你平时也在研究 WebSocket 相关的漏洞，或者遇到什么有趣的案例，欢迎留言交流。毕竟这玩意儿现在太普及了，多聊聊没坏处。

另外，如果觉得文章对你有一丝启发或作用的话，一键三连（点赞、分享、关注），就是对我最大的鼓励，谢谢![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png)

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