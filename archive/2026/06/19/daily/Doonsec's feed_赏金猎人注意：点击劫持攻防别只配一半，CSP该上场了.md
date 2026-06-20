---
title: 赏金猎人注意：点击劫持攻防别只配一半，CSP该上场了
url: https://mp.weixin.qq.com/s/jfMwPLmtTM618qrXyy2VHg
source: Doonsec's feed
date: 2026-06-19
fetch_date: 2026-06-20T06:13:13.441923
---

# 赏金猎人注意：点击劫持攻防别只配一半，CSP该上场了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qg1MKHx3jGFIlEH2AMiaicaG6WsoTzGLuHBjHaAXmRbTbZgK2fpqj1hWZdELHeT2MurPwfVIM8JozZHUdf6PAnCaq5icycMhpt1EVLCERuT6vo/0?wx_fmt=jpeg)

# 赏金猎人注意：点击劫持攻防别只配一半，CSP该上场了

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

干了这么多年渗透测试，我发现一个挺有意思的事：很多兄弟把前端防护写得花里胡哨，但该被套的页面还是被套得明明白白。今天咱们就聊聊点击劫持这个老伙计，以及怎么在服务器端就把这事儿给它摁死。

先快速过一下背景。我们都知道前端有个防御手段叫“框架破解脚本”，听着挺唬人，其实就是一段 JavaScript，检测到页面被 iframe 嵌入了就自动跳出来。这玩意儿早年挺流行，但说实话，在我见过的实战案例里，绕过的难度约等于跨门槛，稍微换个姿势就进去了。所以业界后来学聪明了，开始把防御重心从浏览器端的“自觉”转移到服务器端的“规矩”上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGGkx502qzY5qicZxlrGFTFB7cxEm8rNqJ4iap0lXMZ8icA7C3sMXWxdENHyTxWDYlkXzdCsSLruUhsgv1480wHtLlvZmhn1JOJ7qY/640?wx_fmt=png&from=appmsg)

这里有个关键认知需要先对齐：点击劫持本质上是个浏览器行为攻击，成不成功全看浏览器听不听话、按不按标准来。服务器端防御的逻辑很简单：你浏览器不是爱把页面装进 iframe 吗？好，我直接在你请求的时候就告诉你，这个页面能不能被装进去。规矩我先立好，遵不遵守那是你浏览器的事，但至少合规的浏览器会照办。

干活的主要是两个机制，咱们一个一个说。

X-Frame-Options，老前辈了

这位老哥最早是 IE8 搞出来的一个非官方响应头，后来其他浏览器觉得“哎这东西不错”，就纷纷跟进了。用法简单粗暴，三句话就能讲清楚。

* 你想完全禁止页面被任何 iframe 嵌套？直接上：

```
X-Frame-Options: deny
```

这就像在门口贴张条：“谢绝入内，谁都不好使。”

* 如果想让同源的页面还能互相嵌套，比如自己的业务系统内部要用 iframe，那就换成：

```
X-Frame-Options: sameorigin
```

意思是“自家人随便串门，外人免谈”。

* 还有一种白名单模式，指定某个站可以嵌你：

```
X-Frame-Options: allow-from https://normal-website.com
```

但这地方有个坑，我得提醒一下。allow-from 这个指令浏览器兼容性一言难尽，Chrome 76 往后就不搭理它了，Safari 也是长期装死。所以你如果只靠这一个头做防御，大概率会有漏网之鱼。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGEkqaMlX8CBf088cx03ibyAuxsUv4b0QCJLwJ4PL02FwQmkicsAkCdfYkuD5ATbuzzuAu7MoxDgibeFFJdXbibgjrbOFaV1kEwvibvA/640?wx_fmt=png&from=appmsg)

CSP，当代防御的扛把子

聊完老前辈，咱们说说现在更推荐的主流方案【内容安全策略】，简称 CSP。这玩意儿不光能治点击劫持，对 XSS 也是一把好手，属于一专多能的类型。

CSP 本质上是服务器通过响应头给浏览器下发一套“家规”，明确告诉它哪些资源从哪来是合法的。格式长这样：

```
Content-Security-Policy: policy
```

后面的 policy 是一串分号隔开的指令，浏览器拿到之后就会按章办事，不符合规矩的操作直接拦截。

针对点击劫持，CSP 专门有个 frame-ancestors 指令，比 X-Frame-Options 灵活得多。咱们看几个实战配置：

* 禁止一切嵌套，跟 deny 一个效果：

```
Content-Security-Policy: frame-ancestors 'none';
```

* 只允许同源嵌套：

```
Content-Security-Policy: frame-ancestors 'self';
```

* 指定某个域名可以嵌你，而且写法比 allow-from 更规范，兼容性也好得多：

```
Content-Security-Policy: frame-ancestors normal-website.com;
```

说实话，在实际渗透测试中，我见过太多只配了 X-Frame-Options 却忽略了 CSP 的案例，或者两个都没配的，那简直就是对着挖洞的兄弟们敞开了大门。

最佳实践很简单：把 frame-ancestors 指令老老实实写进 CSP，需要兼容老浏览器就顺手再补个 X-Frame-Options，双重保险，美滋滋。

当然，CSP 这东西想配好也不是随便写两行就完事的，策略开发、实施落地、效果测试，每个环节都得认真对待，而且要把它当成多层防御体系中的一环来用，别指望单靠它一个就能刀枪不入。

好了，今天这波防守姿势就聊到这。如果你觉得这篇文章对挖洞或者做防御有帮助，麻烦点赞、关注、转发、推荐走一波，让更多搞安全的兄弟看到。咱们下期继续聊实战技巧，坑还有很多，慢慢填。

❤️往期推荐❤️

* [免费打造你的渗透测试 AI助手：Burpsuite+Ollama+本地大模型 → AI辅助分析，赏金猎人高效挖洞（脚本已打包）](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447798575&idx=1&sn=0636ff98027e96c2dbbec867b59ba8ff&scene=21#wechat_redirect)
* [别只看书了！CTF免费资源+在线靶场福利，这才是赏金猎人的训练营](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447798624&idx=1&sn=1291eb2c49b2fa9f78bdd9b6d457eade&scene=21#wechat_redirect)

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