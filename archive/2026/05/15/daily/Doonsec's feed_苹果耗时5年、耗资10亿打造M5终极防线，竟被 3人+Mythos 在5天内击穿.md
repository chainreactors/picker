---
title: 苹果耗时5年、耗资10亿打造M5终极防线，竟被 3人+Mythos 在5天内击穿
url: https://mp.weixin.qq.com/s/H0shMLBtaVthKC8km8h6Wg
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:10:54.200913
---

# 苹果耗时5年、耗资10亿打造M5终极防线，竟被 3人+Mythos 在5天内击穿

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3TNvq686LgYsplTpBv9ODvZy4BjvQPGUNg29sa04ia53XO9BEffD0y2SF2tiaHBL8WGwHiaqKaiclkG1AuSYZ55so0EkngicekFTBI/0?wx_fmt=jpeg)

# 苹果耗时5年、耗资10亿打造M5终极防线，竟被 3人+Mythos 在5天内击穿

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

上周，一场足以改写全球安全格局的“闪电战”在硅谷悄悄落幕。加州帕洛阿尔托的安全研究公司Calif，借助Anthropic的超强AI模型Mythos，**仅用5天就彻底绕过了苹果为M5芯片量身打造的硬件级内存防线。**

**苹果：5年10亿，打造硬件“金库”**

过去五年，苹果为了根治困扰iOS和macOS数十年的头号杀手——内存损坏漏洞，在M5和A19芯片中投入了**数十亿美元**，构建了一套名为**MIE（内存完整性强制执行）**的硬件级防护体系。

它的思路堪称“降维打击”：既然软件防不住黑客，就把防线推进到物理层面。MIE基于ARM的MTE技术，**在芯片内为每一块内存打上标签，任何非法访问都会在硬件层被直接拦截。**在苹果的评估模型里，**全世界有能力挑战这套系统的组织不超过20个**。在他们的构想中，搭载M5的MacBook已不仅是生产力工具，而是一座装载着全球最高价值机密的移动金库。

然而，他们唯一算漏的变量，是AI进化的速度。

**闪电攻防战：3人+1AI，5天击碎“苹果神话”**

此次攻破苹果防线的，是美国帕洛阿尔托的Calif安全公司团队——三名顶尖安全研究员，搭配Anthropic公司一款未公开的AI模型Mythos。这场攻防战的节奏快得令人咋舌：

- 4月25日：团队初步探测到M5芯片内核的疑似漏洞；

- 4月27日：传奇黑客加入，Mythos全力运转扫描底层代码；

- 5月1日：仅用5天，完成“MAD Bugs”漏洞链闭环，成功绕过MIE防御。

最终，一个普通用户权限的程序，瞬间**夺取了macOS内核的最高权限**——这是**史上第一个公开的、在M5硬件层面绕过MIE防御的内核漏洞。**

**人机合谋的精确打击：Mythos 战绩斐然**

这个颠覆性的成果，并非AI的一枝独秀，而是“人机合谋”的精确打击。

攻击链采用纯数据攻击方式，不注入代码，只操纵数据——这恰恰是MIE最难防御的攻击面。Mythos在其中展现出了令人胆寒的“泛化与重组”能力：它能把两个看似无关的微小漏洞像拼图一样精妙地拼接，将人类的攻击逻辑瞬间应用到任何未知领域。**人类需要数月才能啃完的底层代码，它数秒之内就能完成逻辑建模。**

而此前，Mythos的战绩早已展露：它揪出了**隐藏在OpenBSD系统中长达27年的漏洞，**找到了能够**劫持Linux设备的方法**，甚至在**Firefox测试中两周找出100个高危漏洞**——而人类专家达到同样数量需要两个月。

但AI并非万能。面对MIE这种全新的防御体系，自主突破仍超出了当前AI的能力边界。此时，安全研究员的经验补上了致命一击。

**库比蒂诺的“判决书”：苹果紧急回应，补丁或将快速上线**

Calif团队对此次发现极具信心，直接驱车前往苹果库比蒂诺总部，当面递交了一份**55页的详细技术报告。**

苹果官方回应称，“安全是我们的首要任务，我们严肃对待所有潜在漏洞报告。”而据Calif高层透露，他们相信苹果将很快完成补丁修复。在问题彻底解决前，完整技术细节不会对外公开。

Anthropic已将Mythos纳入“Project Glasswing”计划，仅向约40家精选机构开放防御性研究，并承诺投入高达1亿美元的使用额度。苹果、谷歌、微软均在其中。

这场**5天 VS 5年**的攻防战，不仅**宣告了苹果MIE神话的破灭，**更拉开了AI攻防新纪元的序幕。而我们，正亲眼见证这场足以改写数字安全格局的变革。

资讯来源：Calif安全公司报告、The Wall Street Journal、Anthropic Project Glasswing相关披露

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K17NkpNs0KZician2shicfibfjHycjx3KP7xmzXRVtBOep8Q4Liaq590IYn3jgibEiaXajTERK2uC8YeVnk4Vjtzvt9NTowGibs5ZYtsAQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K12KDqWLeWxJmzBgG47MzSKOscErIUYhuL0qf34ousicRVLXvticM0ZmT6iaCtotocw10MuuyV6ulMpc10upkZMibR3V2UIaW12yEI/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K1XyzshxCuvE2ywe1qrENFfX4bmB5bB94kPM1Qzu6icKq7QST6n7EEqDXa52Zh8IdBlsTwTnSEljKMF3gNcFVoXBCR283ZmoZBA/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K1orehOsmHN8h8av4JtqicibiaVx9zPBWv6fZDiazic6yib1icXe27wDQVdBOBUwsP0A8bpzhtDPEpfzByPxUjHpO4iabqmvnAQBEAU2SM/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K0OhPJQbIzQ1gx9rOzd3picrttwmx3GEQicby9tbF95MMz9icU2asl9XLVkDedScLM3pHaJqvvkcOWKaQ5X0QdhjsIiagOVgmPFYfY/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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