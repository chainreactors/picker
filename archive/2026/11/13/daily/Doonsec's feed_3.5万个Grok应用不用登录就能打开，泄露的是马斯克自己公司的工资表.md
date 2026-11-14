---
title: 3.5万个Grok应用不用登录就能打开，泄露的是马斯克自己公司的工资表
url: https://mp.weixin.qq.com/s/BkPkGMGbCoFlGk--Xlt5wA
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:19:52.949385
---

# 3.5万个Grok应用不用登录就能打开，泄露的是马斯克自己公司的工资表

# 3.5万个Grok应用不用登录就能打开，泄露的是马斯克自己公司的工资表

原创

欢迎关注→
欢迎关注→

安全客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

11 月 12 日，安全公司 Claroc 公布了一批测试结果：他们扫了 43551 个用 Grok 构建的应用地址，其中还在线的有 37571 个，94.7% 不需要登录就能打开。

顺着这些能打开的地址往里看，他们找到了大约 650 到 800 个装着私密数据的应用。涉及 SpaceXSI、X，以及另外 30 家企业，其中 6 家是财富 500 强。

最扎眼的几个样本：一份 ICU 患者简报，含化验结果、影像检查和呼吸机使用状态；一家承包商的工时管理应用，把 18 个账户的明文密码写进了脚本，谁访问页面都能下载；特斯拉一份服务中心评分表，22 名技术人员的姓名、工作效率和奖金情况全在里面。

这件事的技术含量不高，但它戳中的东西很痛：AI 帮你写代码的速度，已经远远超过你理解这段代码的速度。

一、它不是被黑进去的，是本来就没锁

先把责任划清楚。这不是一次入侵。

这些应用没有漏洞被利用，没有账号被盗，没有任何攻击者做了越权的事。它们只是被发布成了"任何持有链接的人都能访问"，然后被人找到了地址。

找到地址的方法也不复杂。Grok 给每个发布的应用分配一个独立网址，形式类似随机名称.grok.me。名字由几个单词拼成，设计初衷是让人猜不中。

但网址难猜，跟访问控制是两回事。

Claroc 的路径是这样的：每当有人访问一个应用，计算机都要做一次 DNS 查询，把域名解析成服务器地址。部分 DNS 服务商会把这些查询记录收集起来，做成可搜索的数据库，业内叫被动 DNS。于是链路就成了：有人访问过 → DNS 留下记录 → 域名进了数据库 → 外部人员批量就能捞出来。

地址一旦被捞出来，剩下的事取决于权限设置。如果设的是"任何持有链接的人"，那么链接等于钥匙。

这是一种很典型的错觉：把"没人知道地址"当成了"没人能访问"。前者是隐蔽性，后者是访问控制，两件事。混淆它们的代价，在这几年里已经被反复演示过——从云存储桶到内部面板，从调试接口到这次的 AI 生成应用。

二、AI 写的权限代码，把顺序写反了

如果只是默认权限宽松，这件事还能解释成产品设计取舍。但 Claroc 做的第二个测试，暴露了更麻烦的问题。

他们用虚构数据，自己搭了一个供四人销售团队使用的客户管理应用，让 Grok 生成。Grok 确实自动加上了 Google 和 X 登录，看起来挺像回事。

然后研究人员读了一遍代码，发现权限校验的顺序是反的：应用先把登录者加进团队，再检查他是不是团队成员。

先拉你进群，再看是不是群友。那结果必然是群友。

研究人员用一个从未被邀请的 Google 账号登录，不仅看到了全部客户资料，还成功修改了一条记录，删除了另一条记录。

这段代码从功能角度看，是能跑通的。登录能用，数据能看，页面正常。如果只是点几下试用，你根本发现不了问题。用人眼快速扫一遍，也很容易漏掉——因为顺序错误不产生报错，它只产生权限。

这才是 AI 生成代码在安全上的真正难点。它很少写出让你一眼看出毛病的代码，它写的是看起来合理、跑起来正常、但在关键判断上颠倒了因果的代码。语法正确，逻辑错误，而且在测试环境里永远不会暴露。

三、默认值这道题，两家公司给了两个答案

Claroc 顺手做了个对照：拿 ChatGPT 的应用做同样的测试。

ChatGPT 的应用地址同样会被被动 DNS 收录，地址一样能被捞出来。但它的分享面板默认设置为"仅限我"，别人就算拿到网址，也打不开。

同一道题，两个答案。差别不在技术能力，在一个默认值。

SpaceXSI 的回应是：应用在创建者主动分享之前都是私密的，发布需要经过多个步骤；员工账户默认是"仅限你"，要公开应用必须主动改权限。

Claroc 不认这个说法。他们表示，在自己用的付费账户里，发布面板预先选中的是"任何持有链接的人"。

这里的争论点很关键，值得掰开：发布前私密，和发布时默认给谁访问，是两道题。如果一路点完"发布"，最终预选的范围仍然是所有持有链接的人，那么前面确认多少次都没用，多一步确认不会自动补上一份团队成员名单。

而现实是，绝大多数人点发布的时候，脑子里想的是"我这个工具做好了"，不是"我这个工具该给谁看"。默认值是什么，最后就是什么。这不是用户懒惰，这是产品设计的基本规律。

值得一提的是，Grok 现有的权限控制本身是好用的。Claroc 验证过：切到"仅限你"之后，陌生人访问页面和数据接口都会被拒；取消发布，几秒钟内应用就下线。能力都在，问题在于默认没打开。

四、Vibe Coding 把开发门槛降下来，也把发布门槛降下来了

过去做内部工具，流程通常是：提需求、排期、开发、测试、安全评审、上线。慢，但每一步都有人问一句"这东西谁能访问"。

现在不一样了。一个人花一个下午，用自然语言描述需求，就能得到一个能用的内部应用。效率是真的提升了，而且提得很实在——很多过去排不上期的小工具，现在当天就能有。

但发布这件事，也一起变简单了。

发布变简单，意味着"内部工具"和"公开网站"之间的那道墙，从一道需要审批的门，变成了一次下拉选择。而人对下拉选择的理解，远不如对审批流程那么认真。

于是就有了这批样本：ICU 患者简报、员工奖金表、装明文密码的脚本。这些数据在原来的流程里，几乎不可能出现在公网上，因为它们根本出不了内网。现在它们出去了，不是因为谁决定要公开，而是因为没人注意到那个默认选项。

这件事对安全团队的含义很直接。资产清单要扩，从"我们有哪些系统"扩到"我们的人用 AI 生成了哪些页面"。前者有台账，后者没有。很多单位现在连自己员工在用哪些 AI 编程工具都不清楚，更不用说统计生成了多少可访问的应用。

五、如果你也在用 AI 生成内部工具，现在就查这几项

给几条能当天做完的。

第一，搜一遍你们域名下有没有非预期的可访问页面。被动 DNS 数据库不是攻击者专属，防御方一样能查。把自己公司相关的域名捞一遍，看有多少应用地址是你不知道的。

第二，凡是涉及真实数据的应用，权限先改成"仅限指定人"，再谈功能。别用"反正地址没人知道"来说服自己。

第三，让 AI 生成的权限代码必须人工读一遍。重点看三处：登录后先做了什么、团队校验在哪个位置、数据接口有没有独立鉴权。这三处是顺序性错误的高发区，而且它们不报错。

第四，写进规范：内部工具发布前，数据必须是假数据或者脱敏数据。测试时用虚构数据，上线前再切真实数据源，并重新核一遍权限。

第五，工具下线的机制要能用。Grok 这边取消发布几秒就生效，这是好事。你们自己的工具，从决定下架到真正不可访问要多久，这个问题最好现在就答得出来。

最后一个问题，留着给所有在用 AI 写代码的人：你能说清楚，你这周生成的每一个页面，现在谁能打开吗。

如果答不上来，那答案大概就是所有人。

Grok 这次泄露的，不是马斯克公司的工资表。它泄露的是整个行业的一个共识盲区——我们把 AI 当成了生产力工具，却还没把它当成一个会产生发布动作的系统。写代码变快了，但"这段代码谁都能看"这件事，不会因为写代码的人很聪明就自动消失。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/o0buL62hK7M8RnVz7mqRVDRkqm2sJeT2icM4WyR7kMkHpLVaicR3tJ4gr5kIb4zje9lXgd5PuOw42Z5KtathltcQ/640?from=appmsg)

**END**

推荐阅读

[2000元算力免费领 | 只招100名，用AI跑真实安全测试](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790713&idx=1&sn=068e3f936bd33cb35a3b72ba5586a616&scene=21#wechat_redirect)

2026-11-12

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH2GD5Z8mGq4BAKz5ibxIZGr9FkO5icx0k2kc7wWmEshlvOcaTMGgicFr6de9s8lwkL0TlPia59nibz60ZT4t9MZG3GWQjzCPVxJrEfU/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790713&idx=1&sn=068e3f936bd33cb35a3b72ba5586a616&scene=21#wechat_redirect)

[一个月内十几家AI平台被扒，黑客要的不是数据，是你的API密钥](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790708&idx=1&sn=7da1b66daf2243c89e4ca903b90e4a25&scene=21#wechat_redirect)

2026-11-10

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH23coVRWJ4gzKniaGBuVPmjjNp2f70GJvGFhhtNgR0jAicRoDYjcF8TRsq89gLP6rZ15bK2PL1G0qWL8CsiaaaoYVqJZy39VBu4Kg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790708&idx=1&sn=7da1b66daf2243c89e4ca903b90e4a25&scene=21#wechat_redirect)

[杀毒软件成了后门：cPGuard更新通道被投毒](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790700&idx=1&sn=dbe2f4e03b49c7edbc36dc198972d05c&scene=21#wechat_redirect)

2026-11-09

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH0Jkh5fJicourSkKeeBzmb9Q9gfwXAsdjibaPYlxeZgIeeKIib8HPYR9vvqkr1EW8LaibGa5rMUCCoSSaib2mMHkExXSaa1RbkMSVpM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790700&idx=1&sn=dbe2f4e03b49c7edbc36dc198972d05c&scene=21#wechat_redirect)

[有人把欧洲超市的冷柜调到了50℃，这是第二个月了](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790689&idx=1&sn=2f92763396458e742d06a05ac48f53ff&scene=21#wechat_redirect)

2026-11-05

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH3f0cdfKqribMTiaMa6v7NSRvegtic5TUyUyaYVDBvVNeV0iarYicslibmEghjS87Uw5dOic2ljZ80C7XnVXBq1jU6bS01qXJXWwwUZSM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790689&idx=1&sn=2f92763396458e742d06a05ac48f53ff&scene=21#wechat_redirect)

[币安丢了63亿美元，问题出在一台工程师的笔记本上](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790688&idx=1&sn=1136e5e6f4f7cefe1f1a9f8cc51977ef&scene=21#wechat_redirect)

2026-11-04

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH0oefxLe06SHgv8vIcvUBhmX88cTMedMqTeKbCnkq82ibfOjiafB3ZrXoFw7GYlbibowWPgCLZ4m0OWubtOuSicUTj6849xH4pF3vY/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790688&idx=1&sn=1136e5e6f4f7cefe1f1a9f8cc51977ef&scene=21#wechat_redirect)

更多AI知识，请关注Aiker World社区（社区网站：aikerworld.com）

欢迎关注Aiker World社区网站

![图片](https://mmbiz.qpic.cn/mmbiz_png/g5KiabmYVDH1JfBLEjY0lr1yvKicCOBOnDphKNhT9MX0eyWTdpjofRYiajXtJrJsUwEqRyQ6wBmWufibL4JK5X8r25htWykL1ibiclPOGss7RL2fI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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