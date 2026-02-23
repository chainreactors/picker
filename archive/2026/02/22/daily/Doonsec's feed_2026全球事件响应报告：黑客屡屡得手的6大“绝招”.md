---
title: 2026全球事件响应报告：黑客屡屡得手的6大“绝招”
url: https://mp.weixin.qq.com/s/5mO5QQ6hgnW1T86P5AgN8A
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:18:15.455485
---

# 2026全球事件响应报告：黑客屡屡得手的6大“绝招”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2mxV248zE916bzzR6jyE9nhMvEnPjJgCPG3Zez0VZvDPJeMkIFmCgkULn8jLCnEDxGvNyZeDSBvmDIdbRfrIib3IxMxdphPkO3fE/0?wx_fmt=jpeg)

# 2026全球事件响应报告：黑客屡屡得手的6大“绝招”

原创

数世咨询
数世咨询

数世咨询

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lYWDmickZ2mzv5ia7kJjvElpoQM6WiaIlklloAIvjz7jPADHpwEkskQF6gG2X1vZQUOSHA174sfflHWZ2Q31KrNjvOjZp8JSNpEKqfreksWLVg/640?wx_fmt=png&from=appmsg)

近日，Unit 42 发布了《2026全球事件响应报告》，该报告分析了全球50 多个国家、覆盖所有主要行业的750余起重大网络安全事件，以揭示新兴攻击模式与防御经验。本报告的目标，是将一线经验转化为决策依据，帮助组织弥补攻击者仍然依赖的漏洞与缺口，在事件演变为数据泄露之前将其阻断。

1、关键发现：攻击更快、更广、更难遏制

随着黑客不断调整其攻击手段，我们总结出了黑客屡屡得手的6大绝招：

**AI 正在压缩攻击时间线**

在我们调查的最快案例中，攻击者仅用 72 分钟便从初始访问推进至数据外泄，速度较去年提升 4 倍。我们已观察到 AI 被广泛用于侦察、钓鱼攻击、脚本编写与操作执行，使攻击能够以机器级速度规模化开展。

**身份成为主要攻击载体**

在近 90% 的调查中，身份薄弱环节发挥了实质性作用。多数情况下，攻击者并非“攻破”系统，而是使用窃取的凭证与令牌直接“登录”，随后利用分散且碎片化的身份环境进行权限提升与横向移动，而不会触发传统防御机制。

**供应链风险驱动运营中断**

在 23% 的事件中，攻击者利用第三方SaaS应用展开行动。通过滥用受信集成接口、供应商工具及应用依赖关系，他们绕过传统边界防护，使攻击影响范围远超单一系统。

**攻击复杂度持续上升**

我们发现87%的入侵涉及多个攻击面的活动。攻击几乎不会停留在单一环境中，而是跨终端、网络、云环境、SaaS与身份体系协同展开，迫使防御者必须同时监控所有环境。

**浏览器成为主要战场**

近48%的事件包含浏览器相关活动。这反映出现代攻击与日常工作流程高度交织——电子邮件、网页访问及日常SaaS使用等正常用户行为，正在被转化为攻击载体。

**勒索策略超越加密阶段**

基于加密的勒索活动较去年下降15%。越来越多攻击者跳过加密环节，直接转向数据窃取与业务干扰。从攻击者视角来看，这种方式更快、更隐蔽，并能在缺少传统勒索信号的情况下更快得手。

2、攻击成功的原因：暴露面胜过技术复杂度

**尽管攻击速度与自动化程度不断提升，但我们响应的大多数事件并非始于颠覆性的新技术，而是反复出现的防御缺口。在许多案例中，攻击者依赖的不是复杂漏洞利用，而是被忽视的暴露点。**

**1）环境复杂性削弱防御能力**

在超过90%的调查事件中，配置错误或安全覆盖缺口在实质上导致了攻击成功。一个重要原因是工具泛滥。许多组织部署了50种以上安全产品，使一致性部署控制措施和清晰理解数据含义变得极其困难。

**2）可视性缺口延误检测**

在许多响应过程中，攻击信号其实已经存在。事后取证回溯时，证据清晰地存在于日志中。但在攻击进行期间，团队需要从多个割裂的数据源拼接信息，导致在最关键的早期阶段延误检测。

**3）过度信任扩大影响范围**

一旦攻击者取得立足点，过于宽松的访问控制与未受管理的令牌往往使其移动范围远超预期。我们反复看到，身份信任关系将单一被攻破账户转化为广泛横向移动与权限升级。

攻击者在工具与战术上持续进化，但他们最常利用的仍是现代企业环境中的复杂性、可视性不足与过度信任。

3、给安全主管的防御建议

**在750余起一线调查中，有三项优先事项在与CISO及安全团队的对话中反复出现。**

**1）降低暴露面（Reduce Exposure）**

我们看到的许多攻击始于团队未意识到的暴露点——第三方集成接口、未受管理的SaaS连接，或日常浏览器活动。降低暴露面意味着对整个应用生态系统实施安全控制，并以与核心基础设施同等的审慎态度审视所有受信连接。

**2）缩小影响范围（Reduce Area of Impact）**

攻击者进入后，事件是否可控往往取决于身份管理。收紧身份与访问管理，消除不必要的信任关系，可限制攻击者移动范围与潜在破坏程度。

**3）提升响应速度（Increase Response Speed）**

初始访问后的数分钟，往往决定事件是否升级为数据泄露。安全团队需要跨环境的可视性，并能够利用AI进行检测、识别与优先级排序，使SOC能够以机器速度遏制威胁，快于攻击者的行动节奏。

**结 语**

在数百起案例中，模式逐渐清晰，攻击方式正在发生显著转变。黑客攻击速度更快，愈发依赖身份与受信连接展开行动，并在多个攻击面之间扩展其入侵路径。随着入侵速度、规模与复杂度的加速提升，从初始访问到产生业务影响之间的时间窗口正在快速收缩。然而，大多数入侵仍然源于可预防的可视性缺口与安全控制薄弱环节。

![](https://mmbiz.qpic.cn/mmbiz_png/Lzy0Vukmvr4leIPQLfBYnbuoUUaZqoPSBLpJRsPxa49Xeeua2A0sgnQABL6BXvFFMoc0n9ZYgqDJ8v7YZ9pqSg/640?)

\* 本文为泽钧编译，原文地址：https://www.paloaltonetworks.com/blog/2026/02/unit-42-global-ir-report/
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁**多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgrBsUKCFUU3a6Tf9jsVWJcD2l6ic183HdhE2nqia7uMYO2NRQRylficZ5Q/640?wx_fmt=png&from=appmsg)![]()

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrGADwibHso9Bicpccu5Oe06s25Kz1rp9KUaUGaHbA3TG9R1iaqOxQbKlzz3q45urLLiaNm3r8x4LowhA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539099&idx=1&sn=8820d80fdc92ac1f321b5e0a3ff0653e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqodJDDGgZLvcLHLjonO6D6SWFh5QdgUTDZJI2uWWhL2pvdicCoic8jhlmXDDmqnUreFaQeJvEMF12dA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539436&idx=1&sn=676908ed11008cd016b253d1d8e6ba8a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqwJ5oWv2LTsaCqsARGoJpjT7Pxib7vCX6T9TTuWQLuAx3KSUpryl4ZvTnpJSBJCZ8SgoowVjD1BVg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540181&idx=1&sn=e0cd678638b098f969f257b408062b91&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrBJ7QP9nU3wQmMvolcOV1gCuk81sv95ev7tRqTxnh4ib8kqibgFJPFxaF0iaKtiaLicoF6B6iaggtVH8Ww/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540845&idx=1&sn=ec923893881e69010ad830ec852b0abb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrgBb4f5DIe21U8to7y1VMziaQ7ahiaKEkib894mtlFoxDBF62D1wGlQNm5vghS5XGSALN6YY4ZFJHJg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539573&idx=1&sn=a721e2933ad640a3a4b3c72f74d76685&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgzKcal7yWn6SZcgqEr0keAmz0xMbg93YD4my88Np43CkMAEdZHXtlxw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514185&idx=1&sn=8015c07a68a5e2b6074efd2c77f20085&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqwJ5oWv2LTsaCqsARGoJpjOQz7r8ibPUG4znENuDuosPYHByfLHsh7jPxvyiaFianIJgfEV9HX4icpbQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539380&idx=1&sn=da5e8afa28247b4212a544750ece924d&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgjAGO2xBRC4TjicDA4jPbLyeLJbhlLs26gV3dyHrBL6O7H33PPeibFoYw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514336&idx=1&sn=e69b1126e86ab2c59c8ca8e315637031&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgaGg7wIzbRTBJwle4uBxXUJcCG0AibMSAKnJ6qdE9l2HgeAWpxfVAfIw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247530968&idx=1&sn=3d712e23b322ad37cee46d27adb08ed0&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoUdBA8wdHsOh02x6PfOicR0fqdOTPLahE5Y2UPZqZ0Viat6BrAJYrzEyDA9CI3N1uP45zwLjHFTysw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247538943&idx=1&sn=7f95d33eb069aab1cba23c41d68c9759&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgqUkHibDR3uvnsb4JEozX3XJgFnPQSoMCqWYTZNrr0jvCy11yibml4Wgg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247515942&idx=1&sn=bc9ba104b8eb1c0e914d90c8c9a34542&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg1RBWLvLVSHPqQJ613ib6sKvgDPCfa8wYrog3uFFP8pc4pCycQQ3a0nA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247532302&idx=1&sn=2c6afc5d39c89c86f79020099ea44baa&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg0sUJC8RzqMWibMF0LfCLyEcesDzHTJOlIFyibtUyCZy2bJswaUK56ZdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247512372&idx=1&sn=5d06a830f00953a0ab75157fc023ae56&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg6GdM2ic2q54fZEIdWz3LqKpPODruTaeEzRMArzYJWZD4reLgYGgG6DQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540892&idx=1&sn=4c2c4b434d9731b3181760d45759d47b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcs0NU7ZEWiaTufjAkmrhLqnxywvopoNWA60bErgfSXD17qZ57dkxvue6A/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247537068&idx=1&sn=3a3e7c08d93638c1a6018c7862b13bcd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcsic2hQICquOt1dwrexbbJanpAMLl2UFGG14LgYTzDtOHHSouF067yP1w/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247538269&idx=1&sn=848c657fc234aff8840d16d3f06b34ea&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

向上滑动看下一个

知道了

![]()
微信扫...