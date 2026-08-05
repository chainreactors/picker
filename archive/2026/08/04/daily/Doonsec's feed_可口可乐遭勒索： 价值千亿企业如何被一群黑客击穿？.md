---
title: 可口可乐遭勒索： 价值千亿企业如何被一群黑客击穿？
url: https://mp.weixin.qq.com/s/LMbQdZgOih2hoCj7R7wdMw
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:55:14.135954
---

# 可口可乐遭勒索： 价值千亿企业如何被一群黑客击穿？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AjSHgfLXVrrEjxs7wFSXDsHhJ6qOFqq6VrdVG5PgUQc8lYB2AN8tWUAJBwBfAFqo3hFziaSLYCvaiaS4sN1vFyFPg0VlXShTxQP1baRGJKALc/0?wx_fmt=jpeg)

# 可口可乐遭勒索： 价值千亿企业如何被一群黑客击穿？

红客攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年7月16日，全球饮料巨头可口可乐公司向美国证券交易委员会（SEC）提交了一份措辞谨慎的8-K重大事项报告。这份文件向资本市场传递了一个令人不安的消息：其旗下乳制品子公司Fairlife遭遇勒索软件攻击，美国境内所有生产线被迫停摆。

一个年营收超过40亿美元的乳业品牌，一家刚宣布投资6.5亿美元扩建工厂的明星子公司，在短短数天内，生产线全部熄火。

这仅仅是故事的开始。几天后，一个名为Anubis的勒索软件组织在暗网泄密网站上公开"认领"，声称已加密Fairlife全部Nutanix基础设施，并窃取了约1TB的机密数据，威胁若不支付赎金，将在一周内公开所有文件。

一家市值超过2500亿美元的百年企业，如何被一群黑客击穿防线？这场攻击背后，又暴露出全球食品饮料行业怎样的安全危机？

**01**

**72小时风暴：事件全时间线**

从发现入侵到生产线停摆，从数据被盗到公开勒索，这场攻击的每一帧都充满戏剧性。

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrpz913pq7C6ucbUkrPDqEF2rdibyGCIib0kaibgD17A6QHwibqNnuAKfUEKM86VYlxl6FYljGfjqcSTInzWN9QO6GTo8UvwLI63Sjs/640?wx_fmt=png)

**02**

**谁是Anubis？揭开"死神"的真面目**

Anubis——古埃及神话中掌管死亡与冥界的豺头神。这个勒索组织以死神之名行走暗网，确实配得上这个名字的冷酷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVro2dWUoYpwH8rgLPU9wsPsXXFrV0ticyicClUvZIevT5WS2iasZuq9cQwUbonbPNe2cf6wAuLkDibW3lhSfs3kBtLqBaVWEqs9AJpA/640?wx_fmt=png)

在短短18个月内，Anubis已在全球范围内"收割"约100家受害组织，横跨医疗、制造、建筑、金融、科技等多个行业。其受害者遍布美国、英国、澳大利亚、加拿大、法国、荷兰、新西兰等国。

Anubis的攻击手段有三个令人胆寒的"杀手锏"：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrpzWL9btOBfRKiaHxEiaydicXRQVA8xe53RNjFp3CTGDLUw4icXCSQ4e2ruAGhkYicpvzk4lQb8KxgCofEXr23kEiaickzr0s8wI0jp50/640?wx_fmt=png)

**03**

**技术解密：黑客究竟是如何做到的？**

根据安全公司Arctic Wolf对多起Anubis入侵事件的调查，攻击者的手法并非依赖某种零日漏洞的"降维打击"，而是一套"低调、专业、步步为营"的组合拳。

**攻击链六步还原**

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrrISLJUS8GgOyUCf37zl6dnibetiaHZGDgL6ndnUqpWo10eibLXj8Mia1ze6nx9L12pqfJgDpVgopic1bNJXJvW3xZib3rticEQ4dyeMw/640?wx_fmt=png)

**第一步：初始入侵——两条路径，殊途同归**

Anubis的加盟成员主要依赖两种初始入口：

路径一：CitrixBleed 2漏洞利用。CVE-2025-5777是Citrix NetScaler ADC和Gateway中的一个预认证漏洞，允许攻击者从内存中泄露会话令牌，从而绕过包括多因素认证在内的所有身份验证机制。任何未打补丁的NetScaler设备，都是Anubis案板上的一块肉。

路径二：盗取凭证 + VPN登录。通过钓鱼邮件获取员工VPN账号密码，或从暗网购买此前泄露的凭据信息，直接"刷脸"进入企业内网——看起来像一次正常的远程办公登录。

**第二步到第五步：隐身操作**

一旦进入内网，Anubis的操作者展现出高度的专业素养：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrr5ib0ibEV0ib6E9nXqeR6ibmg0qsTzmm1TZV7Mlc02Y0Evvyj9HicwkcaRKMbIQXGiblUrTPHo3d45ESbuxXNBBruLLJhxiaTZefT7Gc/640?wx_fmt=png)

"Anubis的运营哲学可以用一句话概括：永远不要使用你的IT团队不会使用的工具。"

——安全研究机构Infosec.ge

**第六步：致命一击**

当所有有价值数据已完成外传，攻击者部署加密载荷。Anubis的加密器基于Go语言编写，采用ECIES椭圆曲线集成加密方案，加密前先执行：删除卷影副本（vssadmin）、停止安全相关服务、终止数据库进程以确保文件可被锁定。加密后的文件被添加.anubis扩展名，并在每个目录下放置名为"RESTORE FILES.html"的赎金通知。

如果受害者拒绝支付，攻击者可以启动/WIPEMODE——将所有被加密文件的内容清零为0字节。此时，任何恢复希望都化为乌有。

**04**

**关键数字：一场攻击的破坏力**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrq8270t1SVJN2icRXib1sR4oC9lfWSmAPsXCRfNqSibA5hMLXjfpe72OoVrwbtaqdRFU6VBJ6dic2bebHsePjkuCe5nj0XkibiakfVyg/640?wx_fmt=png)

**05**

**为什么是食品饮料行业？**

如果你以为Fairlife是个案，那就大错特错了。食品饮料行业已经成为勒索软件攻击的重灾区。

**近期行业攻击一览**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrpZIgibF2z274dFXC0Zms0oog2WhGf3hQJBgT4vhA28qLBWG20FSDH00wY8QTAnSy05f1hH5GqVEjARibbk48Zo5OFOh0JT6l15I/640?wx_fmt=png)

**为什么攻击者盯上了食品饮料行业？**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrrNFfLg78uvm1GAF0icCuItMvkzUFKgTPlalUY3G2SviadNW6fgjMQ2LwUG0JCqthehPgZmP8ekTnWVPTKzJMWib2fr3QFbzXIRYA/640?wx_fmt=png)

根据Food and Ag-ISAC报告，2025年全球食品和农业领域共发生265起勒索软件攻击，全行业勒索攻击总数达6377起，同比增长82%。更令人警惕的是，72个活跃威胁组织正在持续瞄准这一行业。

**06**

**深度反思：千亿帝国为何不堪一击？**

可口可乐不是一家对安全漠不关心的公司。它拥有世界级的安全团队、完善的合规体系、充足的预算——这正是整件事最令人不安的地方：

**规模和安全投入≠安全免疫力。**

此次事件暴露了四个令人深思的防御盲区：

**01**

**盲区一：子公司是最薄弱的环节**

Fairlife是可口可乐2020年全资收购的品牌。大企业并购时，往往重点关注财务和业务的整合，而网络安全往往被排在优先级列表的末端。子公司的IT基础设施、安全策略可能与母公司存在巨大差距——攻击者深谙此道。值得庆幸的是，可口可乐的网络分段做得相对到位：加拿大业务全程未受影响，说明地理隔离发挥了一定作用。

**02**

**盲区二：补丁管理的"最后一公里"**

CitrixBleed 2（CVE-2025-5777）是一个已知漏洞，有补丁可用。然而Anubis依然能利用它入侵——这说明从"知道有漏洞"到"所有设备都打了补丁"之间存在巨大的执行鸿沟。在拥有成百上千台网络设备的跨国企业中，这个鸿沟往往比预想的大得多。

**03**

**盲区三：合法工具的"双刃剑"**

ScreenConnect、Cloudflared、PsExec、rclone——这些工具本身无害，是IT运维的日常利器。但当攻击者也使用它们时，安全团队的眼睛就"瞎了"。传统的基于签名的检测手段对这些"白工具"完全失效。

**04**

**盲区四：备份不是万能药**

Anubis的Wiper模式宣告了一个残酷的事实：在双重勒索+数据销毁的威胁模型下，备份只能解决加密问题，解决不了数据泄露和永久销毁的问题。当你面对的不是"文件被锁了"而是"文件被永久抹除了"，传统的灾备策略便显得苍白无力。

**07**

**企业如何自保？五道防线**

从Fairlife事件中，每一家企业都能提炼出切实可行的防御策略：

**第一道防线：漏洞与暴露面管理**。立即修补Citrix NetScaler ADC/Gateway（CVE-2025-5777），对所有面向公网的资产进行持续性漏洞扫描。你的攻击面就是你的风险面。

**第二道防线：RMM工具白名单化**。建立企业内合法远程管理工具清单，对清单外任何新出现的RMM二进制文件设置告警。一个陌生的ScreenConnect进程应该立刻触发应急响应。

**第三道防线：IT/OT网络隔离**。生产控制系统（OT）与办公网络（IT）之间必须部署**单向隔离网关**。即便IT网络被完全攻陷，生产线也不应受到影响。这不是建议，而是底线。

**第四道防线：离线不可变备份。**关键数据必须有**离线、不可变**的备份副本——即攻击者无论如何也无法触及和修改的备份。同时做好数据泄露应急预演：如果你今天发现1TB数据被窃，你能否在1小时内确定泄露范围？

**第五道防线：事件响应预演。**不要等到攻击发生时才翻出尘封的应急预案。每个季度进行一次全场景演练：文件被加密、生产线停摆、勒索信出现、媒体开始打电话——在平静的日子里练好兵，风暴来临时才不会慌乱。

**08**

**结语：没有绝对安全，只有持续警惕**

这场攻击最终没有动摇可口可乐的根基。加拿大业务正常运转，美国工厂大部分产能已经恢复，公司向投资者保证不会产生重大财务影响。但这绝不意味着可以松一口气。

Anubis仍然活跃。更多的CitrixBleed 2漏洞等待被利用。更多的子公司IT系统存在防护缺口。更多的数据在暗网等待被交易。

在网络安全领域，没有"我已经够安全了"这种状态，只有"我今天比昨天更安全了吗"这一种追问。

可口可乐遭勒索的故事，不是一家企业的故事。它是这个时代所有企业的故事——**当你连接世界的那一刻，世界上的恶意也连接了你。**

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVroPVcBaJ95Q00CBD0ZGZQkd9ATcycFeuozRV5U2CVOpVJTQvBlmDGUvxkVc80WQgVcX2XrRWC3glInR9yibF2K4oGJrlhhvRUfs/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ZKURiabKFyfPEsfbBaPPzZrTNYRtjGEgexmWgWPDd8KteL8lDobPOhxsJWroZbUjpOj7sgzCW7ic60ZGuiaouzfukx9dEqexCkR4sezQ2Vkx1E/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ZKURiabKFyfMRPdVYQCSaEq89ic4icDfmJoy48rpLrsTIaX3BQL8xGn2tL4U7EicT613SWrZq9lWBkjYg2IicMEDtfs2BBFOkMzwgvicdvMb67rnU/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ZKURiabKFyfP0bgJewLVKePCRLZfrRLAXzOO53kPdVYy36fRDzjt4zEsSvCALgmdDibib7gae3zSwew7jHfd34cXgptFBesgrT1UfGiale5Ihuo/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKURiabKFyfMCHpzAXUPI7rOOKYGgqccialtTMjb9ENvqfsnyGHD27IA3hM47ceI08gibIxvTIkEniaXiaCzxPTQVP15SLUvqk2Z3MzHVfzn4Dics/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZKURiabKFyfOJgfH3Cf15Gziax8Q2Ssv7ITkwF2ane91DHQvSXGQJxBLPKelfUnaFJWnv8NSSVz3psC53gWvBhgXFCSB7oiaYKdKxp8sY2uc9g/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iaPh0yKxE5zleqvXBjCQSwl3YRSgLDiaCJs6thgE7HAEN9bHD2ph3Mg2c349icibwQIyTx6mIvbL2Liatz4PdfGiapVg/0?wx_fmt=png)

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