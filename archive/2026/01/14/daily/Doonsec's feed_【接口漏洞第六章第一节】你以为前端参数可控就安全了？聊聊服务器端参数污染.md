---
title: 【接口漏洞第六章第一节】你以为前端参数可控就安全了？聊聊服务器端参数污染
url: https://mp.weixin.qq.com/s/urblBuPWzhxefl75bq_Cpw
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:28:31.034960
---

# 【接口漏洞第六章第一节】你以为前端参数可控就安全了？聊聊服务器端参数污染

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q0T6rzKq5MrqYM2IUy56qd3fDhJQs3SHqMt0WXpg6ZPkflFPBqTw2a7FkygZYwlK4nUiaEFic5xnkmA/0?wx_fmt=jpeg)

# 【接口漏洞第六章第一节】你以为前端参数可控就安全了？聊聊服务器端参数污染

原创

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

今天，我们来讲讲“服务器参数污染”。

什么是“服务器端参数污染”？

简单来说，有些网站后台藏着一些“内部接口”，平时外面的人是访问不到的。但如果网站在向这些内部接口发送请求时，把你的输入“直接粘贴”进去，而没有做好安全处理，就可能出问题。这就像你把一张便条转交给别人时，没有检查便条上是不是被人偷偷加了几行字。

这时候，攻击者就可能钻空子，比如：

* 偷偷改掉原来的参数；
* 让网站做出不正常的行为；
* 甚至看到本来不该看到的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0T6rzKq5MrqYM2IUy56qd3jhe2yLjr5jHmHALv7kMdvIA9syA0sriaPuYyVArygyFfUm2MQyuQmfQ/640?wx_fmt=png&from=appmsg)

怎么测试这类漏洞？

你可以试试在各种能输入的地方——比如网址问号后面、表单、请求头、甚至网址路径里——塞入像 #、&、= 这类特殊符号，然后看看网站反应是否异常。

举个例子--假设有个网站能搜索用户，你在搜索框输入“peter”，浏览器就会发这样一个请求：

```
GET /userSearch?name=peter&back=/home
```

这时候，网站后台会自己再向它的内部接口发一个请求：

GET /users/search?name=peter&publicProfile=true

如果网站没对你的输入做安全检查，攻击者就可能通过构造特殊的输入，影响甚至控制那个内部请求，从而搞破坏。

这一类漏洞挖掘的难点在于我们要如何才能做到快速、高效的去挖掘、发现能够污染服务器请求的参数名和参数值。这跟前面讲到的api隐藏参数挖掘和利用有些许相同之处，为了更好的区分两者在技术原理和利用方法上的不同，以下就两者进行区别的描述：

（1）服务器端参数污染 (SSPP)

* 攻击位置：你攻击的是请求①，目标是污染请求②。
* 核心原理：网站将你提供的值（如name=peter）不做安全检查，直接嵌入到它生成的请求②的参数值部分。攻击者通过注入分隔符（&, #）来截断并增加新的参数。
* 类比：你点外卖（请求①：“我要一份鱼香肉丝”）。餐厅老板直接把你的话写进给后厨的订单（请求②），而你在外卖单上写：“鱼香肉丝 & 多加两份鲍鱼 & 免单”。如果后厨不核对，你就可能得逞。你污染的是“订单内容”。

在刚才的例子中：

你的输入 name=peter 被直接放到了内部请求的 name= 后面。SSPP攻击就是尝试在 peter 后面加上 &admin=true，让内部请求变成：

GET /users/search?name=peter&admin=true&publicProfile=true

(试图增加一个管理员参数)

（2）API隐藏参数的挖掘与利用

* 攻击位置：你尝试直接猜测或发现请求②的结构和参数。
* 核心原理：内部API本身可能有未公开的、用于控制功能的参数。攻击者通过各种手段（如分析前端JS代码、测试常见参数名、利用信息泄露）来发现这些隐藏的参数。
* 类比：你发现餐厅给后厨的订单（请求②）上可能有“隐藏选项”，比如加辣等级=5、使用贵价材料=true。你虽然没有直接改订单内容，但你通过各种方法猜到了这些选项的名字和用法，然后试图在你自己的外卖单（请求①）里加上这些命令，希望餐厅老板会原样抄过去。

在刚才的例子中：

攻击者发现，内部API /users/search 除了已知的 name 和 publicProfile 参数，可能还接受一个未公开的参数 includeSensitiveData=true。

那么他可能在请求①中尝试：

GET /userSearch?name=peter&back=/home&includeSensitiveData=true

他希望网站会把整个 includeSensitiveData=true 这个“键值对”原封不动地传递到内部请求②中。

今天内容就先到这，这边会持续输出有关api接口相关漏洞的原理及挖洞技巧，感兴趣的你，别忘了点下关注。

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