---
title: HttpOnly 保护不了你，这点老猎人都懂
url: https://mp.weixin.qq.com/s/xtHnz0ohG0gZ5-vq8CxRmg
source: Doonsec's feed
date: 2026-09-13
fetch_date: 2026-09-14T07:20:33.052166
---

# HttpOnly 保护不了你，这点老猎人都懂

# HttpOnly 保护不了你，这点老猎人都懂

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

导读：Web Storage（sessionStorage / localStorage）存会话令牌，到底安不安全？网上搜一圈，前排答案几乎清一色唱衰，说它比 Cookie 危险得多。但一位干了多年渗透测试的老哥不这么看——他把三大"铁证"逐个拆开揉碎，得出的结论恰恰相反。这篇文章，就是他的完整推理过程，建议赏金猎人朋友们收藏细读。

---

## 一、从一个吵翻了的问题说起

前几天有个同行私下问我："会话令牌放 Web Storage 里，是不是作死？"

我没急着回答，先去谷歌搜了一圈。结果有点意思——排名靠前的文章，几乎都板上钉钉地告诉你：Web Storage 不安全，别拿来存令牌，老老实实用 Cookie。

讲道理，这话说得太满了。🤔

作为一个常年跟漏洞打交道的人，我习惯不轻信结论，只信推理过程。所以今天这篇文章，我把自己的完整思路摊开来讲：为什么我认为，Web Storage 恰恰是会话令牌的靠谱选择之一。

反对者的核心论据其实就三条：Web Storage 没有 Cookie 的Secure 标志、HttpOnly 标志，还有Path 属性。听起来挺唬人，那咱们就一个一个掰扯。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGEQcA0FYz0VcGqY1BSTseruzTyRPKpKjK3TnhDXdJxIUpiaayTlYgC1Up7hFMelcjLtDke5Kiaj8oKhHemIicdDHRXKrgnd0ia8jb0/640?wx_fmt=png&from=appmsg)

---

## 二、Secure 标志：不是 Cookie 的优点，是 Cookie 的补丁 🩹

先说个扎心的事实：Secure 标志对 Web Storage 来说，压根是个不相关的东西。

为什么？因为两者的底层逻辑完全不同。

Web Storage 从出生那天起就死守同源策略——数据按"源"隔离，也就是协议加域名的组合。https://example.com 存进 localStorage 的东西，http://example.com 一个字节都摸不着，因为协议不同，源就不同，隔着一堵墙。

Cookie 呢？不好意思，它天生就没把同源策略当回事。默认情况下，你在 https 上种下的 Cookie，转头就被送到 http 版本的同域名站点上，明晃晃地传输。

看到区别了吗？打个比方：

* Cookie 是一栋门禁形同虚设的楼，Secure 标志就是后加的一道铁门——纯属亡羊补牢；
* Web Storage 是一栋从图纸阶段就装好门禁的楼，只要走 HTTPS，天生就有 Secure 级别的防护。

换句话说，Secure 标志的存在，恰恰证明了 Cookie 的底子有问题。它是补丁，不是亮点。

---

## 三、Path 属性：一张纸糊的隔断 🧻

Path 属性就更尴尬了——圈内公认它对安全性几乎零贡献。

道理很简单：同源策略认的是"源"，也就是协议加域名。路径根本不在"源"的定义范围里，所以路径之间不存在任何安全边界。你在 /admin 下种个 Cookie、在 /public 下种个 Cookie，然后指望它们互不干扰？想多了。

想在应用层真正隔离两个应用，唯一的正经做法是：把它们放到不同的源上。这是又一个"Cookie 和同源策略不同步"留下的历史包袱。

---

## 四、HttpOnly：二十年前的老招，今天还管用吗？⏳

这一条是最多人拿来当"铁证"的，也是最值得细品的。

HttpOnly 诞生于 2002 年，初衷是防 XSS 偷 Cookie。要知道，那还是"偷 Cookie"是最主流攻击手法的年代——而 CSRF 要到四年之后才被正式描述为"沉睡的巨人"。

但今天的战场早就变了。真有本事的攻击者拿到 XSS，早就不用"偷令牌"这种笨办法了——直接上自定义 CSRF 载荷，或者植入 BeEF hook，一步到位。相比之下，偷会话令牌这条老路会引入时间延迟和环境切换，费劲、易错，还没必要。

一句话总结：只要对手足够老练，HttpOnly 连拖慢他一秒都做不到。这就像一个形同虚设的 WAF——烂到攻击者甚至察觉不到它存在。

我职业生涯里见过的唯一一个 HttpOnly 真正构成安全边界的案例，是在 bugzilla.mozilla.org 上：不受信任的 HTML 附件从某个子域提供，而 Cookie 那套"不完全遵循同源策略"的特性，让这个子域能摸到父域的会话 Cookie——HttpOnly 在这里才算派上了真用场。

你品出来了吗？跟 Secure 标志一样，HttpOnly 说到底也只是把 Cookie 的安全性拉到 Web Storage 的出厂水平而已。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGG1JibibthJYwibAxgM2lcBf036YkSa08zvT8Els3q6ygyWQu3ibjdkJX4w4xxBLZFp682m2KTwujHtQfeqKRo5s1rGAnibhbCia14GA/640?wx_fmt=png&from=appmsg)

---

## 五、真正的分水岭：环境授权（ambient authority）🔑

前面拆了三个"伪差异"，那真正的区别在哪？这一节才是干货，赏金猎人重点看。

Cookie 是浏览器自动往请求里塞的，Web Storage 的令牌必须由你的 JavaScript 手动挂到请求头上。

差别看着不起眼，安全意义却巨大,因为它决定了令牌是否作为"环境授权"生效。

什么意思？打个比方：

* Cookie 就像你挂在门口的门禁卡，任何人路过、任何请求路过，都自动刷一下——不管这个请求是你本意发的，还是别人伪造的；
* Web Storage 的令牌像你揣在兜里的私人物品，只有你自己亲手拿出来出示，才起作用。

浏览器自动把 Cookie 附带到跨域请求上，正是CSRF 和跨源计时攻击这一整类漏洞得以成立的根基。而 Web Storage 天生没有这个"自动刷卡"的毛病，等于一口气废掉了一整类攻击面。目前社区确实在制定新的 Cookie 属性来补救这个问题——但至少当下，想要这个特性，最省事的方案就是 Web Storage。

再补一刀：Cookie 协议的糟糕现状还催生过不少离谱场面——同一个 Cookie 头里，可能混着受信任和不受信任的数据。设计粗糙的"双提交"CSRF 防御方案，就经常栽在这个坑里。官方给出的解药呢？又双叒叕是一个新的 Cookie 属性：Origin。

---

## 六、几个小坑，用之前心里得有数 ⚠️

当然，Web Storage 也不是完美无缺，这几处差异你得知道：

1. 没有自动过期。不过影响不大——会话令牌的过期本来就该在服务端控制，别指望客户端替你兜底。
2. sessionStorage 的过期粒度是标签页：关标签页就没了，而不是关浏览器才没。这对你来说是加分项还是麻烦事，取决于业务场景。
3. Safari 在隐私浏览模式下直接禁用 Web Storage，这个属实帮倒忙。
4. Internet Explorer 8 下不安全，而且把 Web Storage 塞进非单页应用里，可能带来明显的请求开销。

还有一句要叮嘱：如果你最终决定用 Cookie，那就Secure 和 HttpOnly 一起安排上，别裸奔。

---

## 七、写在最后 💡

乍一看，Cookie 的"安全功能"一箩筐，Web Storage 似乎光秃秃的。

但你把每一项拆开看就会发现：Secure、HttpOnly、Path……这些花里胡哨的功能，本质上都是在给 Cookie那个糟糕的核心设计打补丁。

而 Web Storage 不需要打补丁，因为它天生就站在正确的一边。

技术选型这件事，别看广告，看疗效。下次再有人张口就来"Web Storage 存令牌不安全"，你可以把这篇文章甩给他。

---

## 🙌 觉得有用的话，动动手指！

如果这篇文章帮你理清了思路，或者让你在挖洞路上少踩了一个坑。

👍点个赞，让我知道这类硬核干货你爱看；➕关注我，不定期拆解一个赏金猎人视角的安全话题；🔄转发给你挖洞搭子，好东西别藏着掖着；⭐点亮"在看"并推荐，让更多还在纠结令牌存储的朋友看到这篇！

---

# #Web安全 #赏金猎人 #BugBounty #会话令牌 #WebStorage #Cookie安全 #渗透测试 #CSRF #XSS #安全经验分享

预览时标签不可点

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