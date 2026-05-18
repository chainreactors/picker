---
title: 【安全圈】苹果最强安全防线，5天被AI攻破：网络安全进入新纪元？
url: https://mp.weixin.qq.com/s/U7stDX-D7jpe8FNwN6GzeA
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:07:36.169212
---

# 【安全圈】苹果最强安全防线，5天被AI攻破：网络安全进入新纪元？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFzSM3MsZUxxeleGImBcwHdF81R7SGQFHUxMlPKevsEOFq5dKeMUM7FQ0hiavMFv4KtNsWdyian3BsBVO0C9bQX47xf19kTYa23g/0?wx_fmt=jpeg)

# 【安全圈】苹果最强安全防线，5天被AI攻破：网络安全进入新纪元？

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

AI

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyE9RDOIVCLAQQNxZOiaL6uj31tWzQJ0ZMwezkLKLRkaqicFMTeLezovAZvMJgtcZV3BXd38zAubE7XXeUotPqCicBsjOtRW9pSKpE/640?wx_fmt=jpeg&from=appmsg)苹果最强安全防线，5天被AI攻破：网络安全进入新纪元？

如果有人告诉你：

苹果耗时5年、投入数十亿美元打造的芯片级安全系统，被3位工程师加一个AI模型，在5天内攻破。

你第一反应可能是：夸张标题党。

但这件事，正在成为安全圈热议的话题。

近日，一支由安全研究人员组成的小团队，联合Anthropic最新AI模型 Mythos，对苹果最新M5芯片的硬件安全机制发起挑战，并成功实现了全球首个公开案例：在开启最高级硬件防护的macOS系统中完成内核提权。

更令人震惊的不是漏洞本身，而是破解速度。

过去顶级漏洞团队可能需要半年，而这次只用了5天。

安全行业，可能正在进入一个全新的时代。

---

## 苹果押注5年的“终极防线”

长期以来，苹果系统最危险的问题之一，就是内存漏洞。

简单理解：

系统程序运行时会不断读写内存，而攻击者常通过“内存损坏”漏洞获得系统最高权限。

过去十多年，大量针对iPhone、Mac的高级攻击，最终都是从这里突破。

苹果决定换一种思路：

既然软件层挡不住，那就把防御做到芯片里面。

于是诞生了MIE（Memory Integrity Enforcement，内存完整性强制执行）。

这套机制基于ARM内存标记技术，在硬件层给内存加上“身份标签”，任何异常访问都会被芯片直接阻止。

苹果内部甚至认为：

它能阻断目前已知的大多数攻击链。

换句话说：

这不是修补漏洞，而是直接重新定义游戏规则。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFkt7ichpvtGpCyKibHzSiaQAhhVBWSdQJOOZUhaABgoOxs5MMBtnL1QxfDrTMjxCrY2kkbyicuxHB2so3WictKHWWRSFIUXOiajSsn4/640?wx_fmt=jpeg&from=appmsg)

---

## 结果：AI只用了5天

事情发生在今年4月。

几位安全研究人员开始分析M5系统底层结构。

随后，Anthropic的新AI模型 Mythos 加入。

接下来时间线非常离谱：

* 第1天：发现疑似突破口
* 第3天：更多安全专家加入
* 第5天：完整漏洞利用链形成

最终实现：

普通权限程序 → 获取内核权限 → 完整Root控制。

并且整个过程：

* 在真实M5硬件运行
* 全程开启MIE
* 未关闭任何安全机制

这成为首个公开绕过MIE机制的案例。

---

## 真正可怕的，不是漏洞

漏洞一直都有。

真正让行业不安的是：

AI开始改变漏洞发现速度。

过去安全研究很像“人工挖矿”。

工程师阅读海量代码：

发现异常 → 反复试验 → 拼接漏洞 → 构造攻击链

可能耗费数月。

但AI出现后，它开始扮演“超级助手”。

研究人员表示：

AI最擅长模式识别和逻辑重组。

看似无关的小问题，它可能迅速组合成攻击路径。

人类需要几个月完成的代码分析，AI可能几分钟就能完成第一轮筛查。

于是出现一种新组合：

人类提供经验与方向；

AI负责海量分析和高速试错。

效率直接进入另一个量级。

---

## 网络安全可能迎来“奥本海默时刻”

安全行业一直有个默认前提：

发现漏洞的人很少。

所以防御者还有时间：

发现漏洞 → 发布补丁 → 推送全球。

但如果AI让发现速度提高10倍甚至100倍：

事情就变了。

安全圈甚至出现一个新词：

**Bugmageddon（漏洞末日）**

意思是：

AI找漏洞的速度，开始超过人类修补漏洞的速度。

这意味着未来威胁者不再局限于国家级组织。

小团队甚至个人，也可能拥有过去只有顶级机构才有的能力。

门槛正在迅速下降。

---

## 苹果其实没有做错

有意思的是：

苹果在设计MIE时，Mythos还不存在。

站在当时看：

他们做的几乎全是正确决策：

* 芯片级安全
* 硬件防御
* 底层隔离
* 内存标签机制

问题在于：

AI的发展速度，超出了所有人的预期。

不是苹果落后。

而是整个行业面对的是一种新的变量。

---

## 写在最后

过去几十年：

网络安全像城墙与攻城锤的战争。

墙越来越厚。

锤子越来越重。

而AI出现后，规则突然变了。

它既能帮助防守，也能帮助攻击。

问题已经不再是：

“系统能不能绝对安全”。

而是：

“在人类和AI共同参与的时代，我们还能多快修补漏洞？”

苹果这次遭遇的，也许不是失败。

而可能只是AI安全时代的第一声枪响。

***END***

阅读推荐

[【安全圈】Linux内核漏洞"ssh-keysign-pwn"允许攻击者窃取SSH密钥与影子密码文件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076524&idx=1&sn=85724f6aa9c493a3823cc2988e73c7ec&scene=21#wechat_redirect)

[【安全圈】微软 Edge 148 浏览器将增强安全，密码不再明文进入内存](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076524&idx=2&sn=4bce93113ae71c271aa59e2f723b5d8f&scene=21#wechat_redirect)

[【安全圈】微软Exchange Server高危漏洞正遭攻击者积极利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076524&idx=3&sn=8adfa54adbe431abba673a75db6ad228&scene=21#wechat_redirect)

[【安全圈】新型远程控制木马被披露，黑客伪造苹果与雅虎 CDN 域名攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076488&idx=1&sn=ffae0916c178fdfdfc63e5f205db23f8&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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