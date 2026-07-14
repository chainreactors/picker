---
title: 5步带你从0开局拿下漏洞赏金！1700讲透白帽src的所有核心基础和赏金思路！
url: https://mp.weixin.qq.com/s/aNwu1NP1vkLYk7YTkwVs-Q
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:46:01.651265
---

# 5步带你从0开局拿下漏洞赏金！1700讲透白帽src的所有核心基础和赏金思路！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kzUNKm24hOq4K6XLpViaRuFtibEaffenQuYwYvGM8Vzoho39XRMDibTT2JiamdKAHVQKY2dDxSJ8XFgtTApOxtghxcDtxyoJOhFto6T8LNHhpTE/0?wx_fmt=jpeg)

# 5步带你从0开局拿下漏洞赏金！1700讲透白帽src的所有核心基础和赏金思路！

沧海讲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

你会选择送外卖跑滴滴一天赚200，还是选择坐在电脑前花两小时拿下一笔漏洞赏金？

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9T5U6vuibp9RiaY9Ow4mf2EnwVczNwBA6Y8QSWXxYJZVlFXYyEJaicDV3EwscLHWssEzPUoicM1cGyic1XPgq9txRaZYibdexntL01ZY/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

不是说你不行，这中间的差距其实就是信息差。

接下来，我把从0拿下白帽SRC的关键五步给你完整讲透，但凡你真能听进去，拿下第一个漏洞只是时间问题。

---

第一步：先治好你的代码焦虑和工具迷信

这是很多新手的误区，其实挖漏洞前期根本用不着写代码，也不需要你去死磕一堆复杂工具。SRC上大部分能换钱的漏洞，靠的是你找问题的思维逻辑。

* 前期你只需要花两天搞懂浏览器是怎么跟服务器交互的就行，只需要明白什么是URL、什么是参数和cookie，以及get和post有啥区别，这就够了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9SeBuCgAt7BVWia59NflGHxlE9WyHQOUNQKFDZtobjqqyps0PYZcrvcFAqpzgLFbAMzzhlw7OM7Z29CxJEcpTqLrGLHbTeEnG68/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

剩下的边做边学，别被那些专业术语吓跑，咱们是来技术变现的，不是来考研的。

---

第二步：死磕两样核心工具

学的多不如用的好。

* 一个是Chrome浏览器装上FindSomething插件，主要用来改改参数；
* 另一个是BurpSuit，前期的重点武器。等你配置好以后，可以尝试用BP截获一个请求，然后修改参数再发送，如果服务器返回了不同结果，你就成功了一半。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/CsKJlMFPH9RPxAV8uqiazOycIZLibVapxnFk1PdCU5Lfg9kw5rQr4te9DRn9ibBCM2hPPdJaoKHqqsYDBw9RKHoZI3vZYb2fpLoTWDAhQq0pu8/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

---

第三步：搭建本地靶场练实战手感

先玩DVWA，难度调到低和中，把里面的SQL注入、XSS、文件上传每个都手动复现三遍。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9SiawV3Y4WTrgetib1QsOZtOlKbxpMoWmrQGY27WIiaSMXc7Y3BCSGF8dicFSUDH52pxHVJMgmblCEdTF5ibQVOEY7jZOkhnozeD8eI/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

注意是手动，不是抄命令，你要搞清楚为什么这里能注入，每个payload的作用也要铭记在心。

搞懂了原理再去玩Vulhub，里面的环境更接近真实业务。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9QkGRmUesovDSK1rsWgKl3FDKkEia1NT8H76NlNBnlDpAMhoWGwmKXgG0w0RMfvymnJXicjlxCs3PibQmMQgmLuMZsGtBsHK9Fqrw/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

这时候你可能会很挫败，明明教程都能行，你就不行，多半是cookie没带对或者参数名拼错了，不用着急，调试的过程本身就是在长本事。

---

第四步：尝试挖真实的漏洞

平台推荐补天和漏洞盒子这类众测平台。

* 前期你就认准公益SRC，虽然没钱，但能攒积分、熟悉流程；

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9SY4pgdcPh7B7qpOnVibzmdXD2aBjzTpUp28kZX2bINPNLxm7z7YmjoUfawwRQ3P7cxv9zbj4ChZViamo7d8LTlibd6ZHakWtg6Ms/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

* 或者去找那些刚接入平台的小厂商和排名靠后的企业，他们的防护相对弱，审核也没那么严，别想着一上来就盯着阿里、腾讯这种大厂，那是神仙打架的地方。

哪怕被拒收也别灰心，大不了多改几次再提交，这也是漏洞提交的关键历练，新手普遍要7到10天才能整出第一个有效漏洞，别着急，这将是你赏金之路的开端。

---

第五步，专注能拿赏金的漏洞

至少要把八成的精力放在逻辑漏洞上，这玩意儿不需要你懂多深的代码，只需要你像个刁钻用户一样思考业务流程里的问题。

* 比如越权访问，你登录A账号，不小心改了一下ID参数，要是能看到别人的信息，那就是存在水平越权漏洞。整个过程可能不用半小时，拿一个也能有300到800左右的赏金。

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9RNicyJ2meZe1gFtVDS3MS9LWxkamKpJtwPqZZusFXwMkPywcYzcwJL4ibXV1GS8L6pOxQPKia7YaFiaEnL0pibUDq7emymv44UWMo8/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

* 再比如密码重置，抓包看看能不能跳过验证码，或者验证码能不能爆破。如果能发现单个账户可被重置，赏金就是500到1000左右；要是给你碰上任意用户密码都可被重置，那甚至能到5000。
* 还有信息泄漏漏洞，试试在域名后面加些参数，说不定就能捡到漏。虽然普遍的信息泄漏都在50到200不等，但是剩在量大管饱。

这些漏洞扫描器扫不出来，全靠经验和积累。等你把主流的漏洞案例积累足够了，每个月出个四五千都是很普遍的水平。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9SwWiaM0wMlRuR25zKLlyo018jqqI6dBYMogVO6Z2h2PYZDGGApnWskiaL16UPYUDqeLsQPTqEcH1aMxtnWj6ytWyucOeNkAzvjc/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

说句实话，那些成天抱怨挖不到洞的人，不是光说不练，就是一些基本的漏洞复现都没有亲自去跑通过。

你要是真能跟着我这五步死磕下来，拿下漏洞赏金真不是件什么难事，干就完了！

---

---

「最后」

如果你真的想学好一门本事，首先就要考虑自己对这门技术的兴趣，没有天赋还能靠时间和努力去弥补，但如果没有兴趣加持，就很难坚持到最后。

你要是正打算尝试网安或者想努力一次，我把这些年用过的视频教程和学习笔记都梳理出来了，现在都无偿分享给大家，需要的找我拿就行（文末自取）。

现在哪个行业都不好走，如果没有学历也没有天赋，那就只有努力和坚持了，请相信相信的力量，共勉！

**沧海专属黑客/网络攻防技术资料**

@沧海讲安全：在安全圈待了十多年，已经积累了很多的技术教程，在计算机这个行业，如果不会主动学习，手里没点学习资料，注定是走不远的。我整理的这些资料包含了市场上主流的攻防技术，不说让你成为黑客大佬，帮助你从0到进阶网络安全技术问题不大。

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

**部分技术资料预览**

**01**

***视频教程***

从0到进阶主流攻防技术视频教程（包含红蓝对抗、CTF、HW等技术点）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcYaRKqWc1cxP8sBrX6KZasFTJEVibWmdyoGAuRO4AbzaVjUJ8guoWAzQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcCP8oaOCQm8Cp2qhpCxWiaOjzYrOoA1iac5eSafBicPxSQcpYtchyfVvxA/640?wx_fmt=jpeg&from=appmsg)

**0****2**

***书籍Pdf***

入门必看攻防技术书籍pdf（书面上的技术书籍确实太多了，这些是我精选出来的）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcUumOTUmUznuo7MzKl1JiaEQIeSh4ibkO6jxY68zVZz7iayrwGRtGu2bHw/640?wx_fmt=jpeg&from=appmsg)

**0****3**

*安装包/源码*

主要攻防会涉及到的工具安装包和项目源码（防止你看到这连基础的工具都还没有）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcvsT9h4B1hS9VEPengMcOtNL24949kb4cibKLS9HkIb1k2htW8GYqzMQ/640?wx_fmt=jpeg&from=appmsg)

**0****4**

***面试试题/经验***

网络安全岗位面试经验总结（谁学技术不是为了赚$呢，找个好的岗位很重要）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6Kqcm6J0eAql29R6DIM8bJW4rweVBicM8ibGMOmLNFTpdcQ0gFvefMTOg9dA/640?wx_fmt=jpeg&from=appmsg)

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

@沧海讲安全：只要你是真心想学黑客/网络安全技术，我这份资料就可以无偿共享给你学习，但是想学技术去乱搞的人别来找我，目前全球网络环境日益紧张，我国在这方面的相关人才比较紧缺，网络安全行业确实也需要更多的有志之士加入进来，我也真心希望帮助大家学好这门技术，如果日后有啥学习上的问题，欢迎找我交流。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kWXbooRKsCUic8In0GE4Hd6nTM7iclEUG0UewS479kicpBqGcfpOAaTibhgwsEsblvqe0EsP95XKBe2E90T9g02cQg/0?wx_fmt=png)

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