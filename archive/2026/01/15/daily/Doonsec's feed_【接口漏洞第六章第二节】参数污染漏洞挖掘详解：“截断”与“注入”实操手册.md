---
title: 【接口漏洞第六章第二节】参数污染漏洞挖掘详解：“截断”与“注入”实操手册
url: https://mp.weixin.qq.com/s/xWXN5qkbYcqzD1CiJw4ZRA
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:27:41.982085
---

# 【接口漏洞第六章第二节】参数污染漏洞挖掘详解：“截断”与“注入”实操手册

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q3hE7mttEQokia8WjfV50gJ15oRsbOyQgee3iaHE6HH73w1ICHsXtCSJ40JKvhJgIRj0rgar3XpSmFQ/0?wx_fmt=jpeg)

# 【接口漏洞第六章第二节】参数污染漏洞挖掘详解：“截断”与“注入”实操手册

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

我们在上一节[【接口漏洞第六章第一节】你以为前端参数可控就安全了？聊聊服务器端参数污染](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797725&idx=1&sn=ad6bbd7d4ce0a9582094bc989888abbc&scene=21#wechat_redirect)中有大概聊了下服务器参数污染漏洞技术原理，以及它和隐藏参数挖掘之间的相同和不同之处。今天我们就继续就参数污染漏洞的发现方法做进一步的深入。

挖掘此类漏洞的方法大概有“截断”和“注入”两种方式，我们来看具体的操作方法：

1. 截断后端（服务器）请求

在查询参数中插入URL编码的 #（即 %23），可以尝试截断发送到后端API的请求。

比如发送：GET /userSearch?name=peter%23foo&back=/home

前端可能转发为：GET /users/search?name=peter#foo&publicProfile=true

这里需要注意的是：# 必须编码，否则会被浏览器当作页面锚点触发直接解析跳转，不会发给服务器。

进行服务器请求截断后，如何判断成功？观察返回的数据。如果返回了用户“peter”的信息，说明 # 后面的内容（publicProfile=true）可能被截掉了。如果返回“用户名foo无效”，则说明 foo 被当作用户名的一部分，截断失败。

对服务器请求进行截断操作有什么用？如果成功截断，就可能绕过类似 publicProfile=true 的限制，从而访问到非公开的用户资料。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0T6rzKq5MrqYM2IUy56qd3jhe2yLjr5jHmHALv7kMdvIA9syA0sriaPuYyVArygyFfUm2MQyuQmfQ/640?wx_fmt=png&from=appmsg)

2. 注入额外参数

在查询参数中插入URL编码的 &（即 %26），可以尝试向后端请求“塞入”新的参数。进行这类操作，可以遵循以下步骤：

A. 先试无效参数

比如发送：GET /userSearch?name=peter%26foo=xyz&back=/home

后端收到：GET /users/search?name=peter&foo=xyz&publicProfile=true

这样做的目的：测试参数注入是否可行。如果页面没变化，说明 foo=xyz 被成功注入但被后端忽略了。

B. 再试有效参数

如果找到了隐藏的有效参数（例如 email），就可以尝试注入它。

比如发送：GET /userSearch?name=peter%26email=hacker@test.com&back=/home

后端收到：GET /users/search?name=peter&email=hacker@test.com&publicProfile=true

这样做的目的：观察注入有效参数后，应用程序的行为是否改变（例如，是否按邮箱搜索了）。

C. 尝试覆盖原参数（最关键）

通过注入一个同名参数，尝试覆盖掉原始参数值。这是测试“服务器端参数污染”漏洞的核心。

比如发送：GET /userSearch?name=peter%26name=carlos&back=/home

后端收到：GET /users/search?name=peter&name=carlos&publicProfile=true

后端如何处理？这通常取决于网站使用的技术栈：

* PHP：通常使用最后一个值 → 搜索 carlos
* ASP.NET：可能合并两个值 → 搜索 peter,carlos（可能报错）
* Node.js/Express：通常使用第一个值 → 搜索 peter（结果不变）

有什么用？ 如果能够覆盖参数，就可能实现越权访问。例如，将 name 参数覆盖为 administrator，可能让你以管理员身份登录。

我们一起来复盘一下以上的大致步骤、方法： 先测试用 %23 截断，再测试用 %26 注入和覆盖参数，观察响应变化，从而探测并利用后端API的解析漏洞。

这两天一直都是在讲API接口的参数污染漏洞原理及方法，没有结合实际例子。可能理解上面会有点枯燥难懂，这边接下来会结合实际的利用场景来进行这类漏洞的实际挖掘，关于api接口漏洞的相关内容，这边也会持续输出。感兴趣的你，别忘了加个关注。

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