---
title: AI安全——实战敏感词汇绕过手法
url: https://mp.weixin.qq.com/s/0WJFPZuwoNB9CsA-bOG7-g
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:45:07.279641
---

# AI安全——实战敏感词汇绕过手法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZ9xibyyoOdzpUZFRpOzQAyuZgEeERyzpuZyBrJHOgvKFmibdtDq8IQQSg/0?wx_fmt=jpeg)

# AI安全——实战敏感词汇绕过手法

原创

zkaq suan\_cai\_yu
zkaq suan\_cai\_yu

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcr9luwbuD3PfLZAAUUvtyFXhz6icLI5IicHR6icsjzhVFxQOibibvdSVSNlzzZaRzjIeib6SGGwInc858ww/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **suan\_cai\_yu**投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（  https://bbs.zkaq.cn  **）****

# 一、前言

    在今年大概 6 月份的时候，煮波在一些公众号以及 src 平台上看到了一个船新漏洞——AI 漏洞，后面更是看到了应运而生的所谓《ai 魔咒》，随着人工智能的兴起，一些学校或者机构或者平台都部署了 AI，有些 AI 虽然设置了严格的内容安全策略（禁止生成色情、暴力等违规内容），但其防御机制并非牢不可破。通过精心构造的、具有对抗性的提示词（Adversarial Prompts），可以系统地绕过其语义过滤与伦理对齐机制，成功诱导AI模型输出包括色情言论在内的明确违规内容。

    其实 ai 提示词对抗是一门语言的艺术，要拐弯抹角地去诱导它输出一些违禁内容，同时也要思考开发者到底是怎么要求 ai 的？下面我分享一些我在实战中确实遇到过的 ai 敏感词绕过手法。

# 二、违禁词拆分

    直接看一个例子吧，某高校部署的 ai

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZcYEkvqALicfMxdee54Zetsxr3Z2fStlyYiaW9f81w1trC1OjprEoGBvQ/640?wx_fmt=png&from=appmsg)

创建一个账户就直接开始和 ai“聊天”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZiaFzkISJVg0iakI04waBB0gqaUpxE6EoIWNjwEbWVEamLpQM4ht5wjOg/640?wx_fmt=png&from=appmsg)

这里我猜测违禁词就是性关系

拆分违禁词

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZm1y8XqyicIfoblWj7FiaZzw4g35hQluCb3Ubqgx6iaSToygLqvGemr1pg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZ2sLfmeX0iaXbXfIzva1uzwiaGjoG9RnomUrOjUedDtNsBEhEkJCicNuvg/640?wx_fmt=png&from=appmsg)

再让 ai 自己拼起来，就会解释了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZ4THq5PZTgTkyHQrWwRl5NHbQqYaQFMfCOicwur5swQ02ria054awpHmA/640?wx_fmt=png&from=appmsg)

很多 ai 都是这样子的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZb8f1c0lKIyibTwhjb8icaDJXviaKTyGSBOqFaNyWg2OahHh0AceTouzHw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZXYS5vkRcdW5L5UuhCbGmLtkkXm0dAnvM63XcdUBvJEKLmw8e0zyrIQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZGvc8jWMiaPLJZgSCK7hDlQAT2T9luibFve0wgRaG5Oz1HBGZNzDPxW3Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZTLG2O7uTQJgmR6libutaWICr28kI7RCZiaHs90mCicgDWaO6ibypQ6zic4g/640?wx_fmt=png&from=appmsg)

# 三、重组逻辑语句

大部分 ai 都有自己重组语言的能力，当他们遇到逻辑不通的语言的时候，会自动思考怎么排序这个语句

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZHGCx6Nuldcjp7kY2zTR16BQS54Op3q6SRAicyI5H3w0A7g2J8nYK6PA/640?wx_fmt=png&from=appmsg)

而它们在思考的过程其实就已经完成绕过了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZD5BjEXe180LgWzfnHKpibvSiaptvBBXnZXnMEkE6TSiatRPe0WpI9ZN7A/640?wx_fmt=png&from=appmsg)

# 四、垃圾字符

其实本质也是截断敏感词，让 ai 检测不到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZSfXib3lHqr2wkUMsmOqC7EpiboPpUGKapwQkicMeg77Y5LMXLvSHRtjsQ/640?wx_fmt=png&from=appmsg)

# 五、构建环境

这种方法也是我一开始了解到的方法，也是大部分人看到 ai 直接扔给 ai 的魔咒，通常的技巧就是让 ai 当魅魔，或者其它有奴性的生物

具体语句大家可以直接去看这篇文章，感谢师傅分享！！！！！

[https://mp.weixin.qq.com/s/yhAQMXAaa\_wmneP3NqP2xQ](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493890&idx=1&sn=380e9dd566b29b713993b26f524fe0e4&scene=21#wechat_redirect)

最后的结果大概就是：hhhhh

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZfiagNLpKkibEIicyAttylKkK02G1QPxiaOCfQdlMTHU0SrZiaZpWdPuPbtQ/640?wx_fmt=png&from=appmsg)

# 六、文件上传xss、文字解析

现在很多 ai 都具备文件上传的功能了，可以考虑打存储型 xss，甚至直接 getshell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZ9HWjpF9XpdLw8pxZAlyXeGIKQML7xIKn6GiaOAzzbwgjWjz0P2CpgoQ/640?wx_fmt=png&from=appmsg)

又或者有些 ai 对于你直接提问的问题会进行过滤，但是对上传的文件内容是没有过滤的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZSOoQcyFLtIzZwX2ZJ29AXD1lChKVctsbHNFtTWWUnF0pRo6tUtfibNA/640?wx_fmt=png&from=appmsg)

但是这个 ai 可以上传 docx 文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZF5FFHcrNYmficMhicj3FUN0viaLFiaibA0SueZe4nJZ1P6HlRM30u6B8KKg/640?wx_fmt=png&from=appmsg)

再问它，就会回答了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZNGyMYTkKibvu3CTAV9MJyh3ricFibTJTnmicIuw6xuJauAp2YtnJK9yyVg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcpyvoG2nDBhFC6akEDgedvZTr4GUEib11X1MeonS80CmD4K2IbeU78BJdBvL0PswX68nrib3XcS7yJg/640?wx_fmt=png&from=appmsg)

    以上就是我曾经遇到过的一些 ai 敏感词绕过手法，其实还有很多，比如编码绕过，执行代码等等，但是我在实战中没有遇到过，就不给大家一一列举了。

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcr9luwbuD3PfLZAAUUvtyFXhz6icLI5IicHR6icsjzhVFxQOibibvdSVSNlzzZaRzjIeib6SGGwInc858ww/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=16)

**分享后扫码加我！**

**回顾往期内容**

[我与红队：一场网络安全实战的较量与成长](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247550558&idx=1&sn=589aa46a61b9ab02ab953ccb9539b1d3&scene=21#wechat_redirect)

[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)

[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)

[重生HW之感谢客服小姐姐带我进入内网遨游](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247549901&idx=1&sn=f7c9c17858ce86edf5679149cce9ae9a&scene=21#wechat_redirect)

[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b696f0cabab0a046385599a1683dfb2&chksm=fa6bb717cd1c3e01afc0d6126ea141bb9a39bf3b4123462528d37fb00f74ea525b83e948bc80&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17)

点赞+在看支持一下吧~感谢看官老爷~

你的点赞是我更新的动力

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BwqHlJ29vcq98SadiaYm6GqwrAZjdeXAuLrl5ATlxIMCiabYgjLJ1M1gcLHicsRuISeqtAuLaSfRtBULuibjDBcLsg/0?wx_fmt=png)

掌控安全EDU

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BwqHlJ29vcq98SadiaYm6GqwrAZjdeXAuLrl5ATlxIMCiabYgjLJ1M1gcLHicsRuISeqtAuLaSfRtBULuibjDBcLsg/0?wx_fmt=png)

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