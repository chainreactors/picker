---
title: AI Agent导致杀伤链失效
url: https://mp.weixin.qq.com/s/Wtt5vcNKiiQNJ0C4cFhJkA
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:30:15.553375
---

# AI Agent导致杀伤链失效

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2myh4heErIaLPEMEfT0rQstNPwcOyxrPfuTaupr2VhoeoiboEWibYiau2zmu4dpvmTC7kGuQEdRQPuZ0BCqGKKHF9pwvBunjhjH3RY/0?wx_fmt=jpeg)

# AI Agent导致杀伤链失效

数世咨询

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点亮上方「★星标 」更多干货内容，不再错过！

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lYWDmickZ2mymGPAIkMxIER0whgicBuSkUlN7libnk3jDzsiaDfniaK7K47OK83nFYfr4Y732GY3OAA4dGbpseK70tFuMjt34H2b0fxsdiaYaDiaU8/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247542077&idx=1&sn=c63f262d4bb66895352b76087521895e&scene=21#wechat_redirect)

**本文关键看点：**

![](https://mmbiz.qpic.cn/mmbiz_gif/15I7jtE1uriaTpqMbLz5A8YygCg8eaYBUk0tJibjWvQrJONna1vQMDpOOafQaMjkeicDqcD9A02T81IYoKrqzrnzA/640?wx_fmt=gif)

**#****01**

攻击者根本不需要kill chain，因为他们已经攻破了你的人工智能代理。一个已经拥有访问权限和正当理由，且每天在你系统间移动的服务。

**#****02**

人工智能代理跨系统工作，在应用间传输数据，并且持续运行。如果被攻破，攻击者会绕过整个杀伤链，因为代理本身就是杀伤链。

**#****03**

主要问题在于安全工具被设计用来检测异常行为的，当攻击者依赖AI代理现有的工作流程时，一切看起来都很正常。

********▍********以下正文内容基于英文原文编译，可能存在语义偏差，请以原文为准。

✦

**以下为正文**

✦

2025年9月，Anthropic披露了一起事件：一个国家支持的攻击者利用AI编码代理，对30个全球目标执行了一次自主网络间谍活动。AI独立完成了80%至90%的战术操作，以机器速度执行侦察、编写漏洞利用代码并尝试横向移动。这一事件令人担忧，但还有一种场景应当更让安全团队警觉：攻击者根本不需要完整执行杀伤链，因为他们已经攻破了运行在你环境内部的AI代理。这个代理本身就拥有访问权限、合法授权，以及每天在你各系统间移动的正当理由。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lYWDmickZ2mzYApze0w2WDPD8ic1ibknczrnicGLKUWhaCUwhhIgACC6ffibFCwmDvLuxMAbZibl5M4CzicVPWkykLmjGR2CwNJXSu0g6tGzh7DjPo/640?wx_fmt=png&from=appmsg)

**0****1**

**为应对人类威胁而构建的框架**

传统的网络杀伤链假设攻击者必须逐步争取每一寸访问权限。这是一个由洛克希德·马丁公司于2011年开发的模型，用于描述对手如何从初始渗透到最终目标，也是安全团队建立检测思维的起点。逻辑很简单：攻击者需要完成一系列步骤，而防御者可以在任意环节中断这条链条。攻击者必须经过的每一个阶段，都是一次额外的捕获机会。

### 一次典型的入侵会经历以下不同阶段：

1. 初始访问（利用漏洞等）
2. 在不触发警报的情况下建立持久化
3. 侦察以了解环境
4. 横向移动至有价值的数据
5. 当权限不足时进行权限提升
6. 在避免DLP控制的同时进行数据窃取每个阶段都会产生检测机会：端点安全可能捕获初始有效载荷，网络监控可能发现异常的横向移动，身份系统可能标记权限提升，而SIEM关联可能将跨系统的异常行为联系在一起。攻击者经历的步骤越多，触发警报的机会就越多。这就是为什么像LUCR-3和APT29这样的高级威胁行为者要大力投入隐匿，花费数周时间进行"靠地生存"并融入正常流量。即便如此，他们仍会留下痕迹：异常的登录位置、奇怪的访问模式、轻微偏离基线的行为。这些痕迹正是现代检测系统被设计用来发现的目标。然而，问题在于，AI代理并不真正遵循这一套路。

**02**

**AI代理已拥有的能力**

AI代理的运作方式与人类用户根本不同。它们跨系统工作，在应用程序间移动数据，并持续运行。一旦被攻破，攻击者就绕过了整个杀伤链——代理本身就成了杀伤链。试想一个AI代理通常拥有哪些访问权限。它的活动历史本身就是一幅完美的数据地图，揭示了哪些数据存在以及存放在哪里。它可能从Salesforce提取数据、向Slack推送信息、与Google Drive同步，并作为日常工作流程的一部分更新ServiceNow。它在部署时被授予了广泛权限，通常是跨多个应用程序的管理级访问权限，而且它本身就负责在系统间移动数据。攻陷该代理的攻击者会瞬间继承所有这些能力。他们获得了地图、访问权限、授权，以及移动数据的正当理由。安全团队花了数年时间学习检测的那些杀伤链的每个阶段，代理默认跳过了它们全部。

**03**

**威胁正在上演**

OpenClaw危机向我们展示了这种情况在实践中是什么样子：其公开市场中约12%的技能是恶意的。一个关键RCE漏洞允许一键攻陷。超过21,000个实例被公开暴露。但更可怕的是，一个被攻陷的代理一旦连接到Slack和Google Workspace后能访问什么：消息、文件、邮件和文档，以及跨会话的持久记忆。主要问题在于，安全工具被设计用来检测异常行为的。当攻击者搭乘AI代理的现有工作流程时，一切看起来都很正常。代理在访问它始终访问的系统、移动它始终移动的数据、在它始终运行的时间运行。这就是安全团队面临的检测盲区。

\* 本文为泽钧编译，原文地址：https://thehackernews.com/2026/03/the-kill-chain-is-obsolete-when-your-ai.html
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

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fg6GdM2ic2q54fZEIdWz3LqKpPODruTaeEzRMArzYJWZD4reLgYGgG6DQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247542139&idx=1&sn=9e1ab0f25bc9d4e0fa86c8632dacb722&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcs0NU7ZEWiaTufjAkmrhLqnxywvopoNWA60bErgfSXD17qZ57dkxvue6A/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247537068&idx=1&sn=3a3e7c08d93638c1a6018c7862b13bcd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrcZ08ewdTHjp9ia8rKAaxcsic2hQICquOt1dwrexbbJanpAMLl2UFGG14LgYTzDtOHHSouF067yP1w/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247538269&idx=1&sn=848c657fc234aff8840d16d3f06b34ea&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信...