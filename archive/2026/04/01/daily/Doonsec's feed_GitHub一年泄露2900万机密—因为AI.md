---
title: GitHub一年泄露2900万机密—因为AI
url: https://mp.weixin.qq.com/s/ac2zvGFWoLsR1TSgO9ikkg
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:26:49.072774
---

# GitHub一年泄露2900万机密—因为AI

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lYWDmickZ2mx2JBIaYVBCEn5nfmB6MM1ibv2MEn6iaZZWWMQt5x1WWZhkqy9dXrtHsGCPjvsBcIaljNpGDiaQU1oE0Eg94d8nU0kJaiapRlWWXKA/0?wx_fmt=jpeg)

# GitHub一年泄露2900万机密—因为AI

数世咨询

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2mytxBUsY9H5gFIUFFTIp92B3gnaAB58cNDxrdAI9FafGhoEJwtOxdYsJQqliacYqrylCOD27YMWYbjGTwoKcWe6TxcGTXFkUqzc/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247541849&idx=1&sn=9d3d83958fe3bad1ca644d8420ee7438&scene=21#wechat_redirect)

**本文关键看点：**

![](https://mmbiz.qpic.cn/mmbiz_gif/15I7jtE1uriaTpqMbLz5A8YygCg8eaYBUk0tJibjWvQrJONna1vQMDpOOafQaMjkeicDqcD9A02T81IYoKrqzrnzA/640?wx_fmt=gif)

**#****01**

2025年，人工智能的采用彻底改变了软件开发，GitHub总计检测到约2900万泄密，创下有史以来单年最大增幅；

**#****02**

人工智能辅助加快了软件开发速度，使得嵌入现代技术栈中的令牌、密钥和服务身份数量倍增，但治理方面却没有相应的改进；

**#****03**

下一代安全项目必须将非人类身份(NHI)视为一级资产，配备专门的治理、上下文和缓解自动化，涵盖代码和非代码环境。

********▍********以下正文内容由AI工具生成，可能存在语义偏差，请以原文为准。

✦

**以下为正文**

✦

2025年，开发者使用Claude Code的秘密泄露率为3.2%，高于1.5%的基准。人因因素依然至关重要。

GitGuardian，GitHub上安装量最大的安全应用背后的领导者，今天发布了第五版“**秘密扩散状态**”报告，记录了2025年主流人工智能的采用如何重塑软件交付，并加速了非人身份（NHI）及其秘密在公共和内部系统中的曝光。

![](https://mmbiz.qpic.cn/mmbiz_png/lYWDmickZ2mwNntGicxJSZ3doLJW8kWf0VZQ7Wc4tM9Vic88bkZdm9lMbNyBtVrxLRq1f2mvVwukPnl5afpEvKbpgdwZrBVPYU0J7icZUO8rdwY/640?wx_fmt=png&from=appmsg)

尽管软件生态系统快速增长，**泄露的秘密增长速度更快**，而**补救措施未能跟上**。

**0****1**

**软件改变的年份**

在2025年，人工智能的采用永久性地改变了软件工程：

* **公共提交同比增长43%**，增长速度至少是之前的2倍
* 自2021年以来，秘密的增长速度大约是活跃开发者人口的**1.6倍**
* 在AI辅助的代码中，秘密泄露率平均约为GitHub整体基准的两倍。

这些因素共同推动了GitHub上新泄露秘密同比增长34%，**总计检测到约2900万个秘密**，创下有史以来最大的单年增长幅度。

**02**

**CISO保护非人身份（NHI）的九个要点**

暴露的凭证仍然是一个主要且重复的被攻破路径。在2025年，AI的辅助提高了软件创建的速度，并使现代技术栈中嵌入的令牌、密钥和服务身份数量倍增，而治理方面的改善却没有相应增加。

**03**

**AI助手在新类别凭证中放大风险**

Claude Code辅助的提交泄露秘密的比例约为3.2%，是基准的2倍。AI辅助编码使软件开发民主化，使没有正式培训的开发者能够快速构建应用程序。然而，这种可及性伴随着安全漏洞：经验较少的开发者可能缺乏安全意识，忽视AI的警告，或明确提示工具包含敏感信息。这些泄露的秘密最终可能反映人类的错误，而不仅仅是AI的失败。

与AI服务相关的凭证泄露是增长最快的：与AI服务相关的泄露同比增长81%（达到1,275,105），并且更有可能绕过主要为传统开发工作流程构建的保护措施。

MCP配置风险正在显现：MCP服务器文档通常建议将凭证直接放入配置文件，而不是使用更安全的客户端身份验证模式。这导致在研究的MCP配置文件中暴露了24,008个独特的秘密。

**04**

**AI瞬间扩展攻击面**

内部仓库仍然是最大的暴露储存库。它们被硬编码秘密的可能性是公共仓库的约6倍。

秘密扩散超越代码：约28%的事件源于协作和生产力工具中的泄露（不仅仅是仓库），在这些工具中，凭证可能暴露给更广泛的受众、自动化和AI代理。

开发者机器正成为凭证边界的一部分。随着AI代理获得更深层的本地访问权限（编辑器、终端、文件、凭证存储），提示注入和供应链式攻击（例如Shai-Hulud）可能将本地秘密转化为组织风险。

“AI代理需要本地凭证以连接跨系统，使开发者的笔记本电脑成为一个巨大的攻击面。我们构建了我们的本地扫描和身份清单工具来保护它们。安全团队需要明确映射出哪些机器持有哪些秘密，揭示出诸如过度特权访问和暴露的生产密钥等关键弱点。” GitGuardian首席执行官Eric Fourrier说。

**05**

**行业面临日益增长的债务，需要NHI治理，而不仅仅是检测**

长期存在的秘密仍然占主导地位：约60%的政策违规是持续存在的凭证，突显出向短暂、最小特权访问转变的缓慢。

优先级排序比看起来更困难：约46%的关键秘密没有供应商提供的验证机制，需依赖上下文信号（位置、使用情况、下游消费者和秘密管理者）来评估现实世界的可利用性。

补救措施在规模上失败：2022年的64%有效秘密在2026年仍未被撤销，最常见的原因是安全团队缺乏实现任何泄露秘密可行、可重复补救路径所需的治理。

\* 本文为泽钧编译，原文地址：https://hackread.com/gitguardian-reports-an-81-surge-of-ai-service-leaks-as-29m-secrets-hit-public-github/
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁**多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgrBsUKCFUU3a6Tf9jsVWJcD2l6ic183HdhE2nqia7uMYO2NRQRylficZ5Q/640?wx_fmt=png&from=appmsg)

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

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg6GdM2ic2q54fZEIdWz3LqKpPODruTaeEzRMArzYJWZD4reLgYGgG6DQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247542139&idx=1&sn=9e1ab0f25bc9d4e0fa86c8632dacb722&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcs0NU7ZEWiaTufjAkmrhLqnxywvopoNWA60bErgfSXD17qZ57dkxvue6A/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247537068&idx=1&sn=3a3e7c08d93638c1a6018c7862b13bcd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcsic2hQICquOt1dwrexbbJanpAMLl2UFGG14LgYTzDtOHHSouF067yP1w/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=22475382...