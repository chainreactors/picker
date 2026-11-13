---
title: AI 黑客15分钟拿下你的内网？“只给人看的”蜜罐不够用了
url: https://mp.weixin.qq.com/s/NCyBpcryIrXtc3fL-J4_2w
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:03:14.089195
---

# AI 黑客15分钟拿下你的内网？“只给人看的”蜜罐不够用了

# AI 黑客15分钟拿下你的内网？“只给人看的”蜜罐不够用了

安恒信息

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icVz8RbowK3zzWCaicK1LPbSTJDDcicxleNaqXXSxYPFppNTsB1z02AlkKRMHgtzdCselqbaOWGGfYJPqibodouxRQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)![]()

如果有一天，攻破你内网的不是一个黑客，而是一台不会累、不会失误、还能自己改代码的 AI，你要靠什么发现它？

据 Google 威胁情报组（GTIG）与 Mandiant 于 2026 年 10 月 30 日发布的研究，这一天已经来了——多个攻击者正把 ARTEX、PentAGI 等开源“多智能体渗透框架”投入真实入侵，由 AI 自主完成横向移动、数据库利用、窃密准备等攻击链条。

报告显示，最快的一起案例里，攻击者从首个失陷账号打到深层访问只用了 15 分钟；AI 代理更在 23 秒内完成了 27 次探测。GTIG 判断，3—6 个月内，攻击将走向“几乎无人、更隐蔽的全自主形态”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QsTClNuIiapHEicOHMzOCiaKPKBDKrhvMoohmqxSkuia5B8Vpicj8noysgAcjuiaI7tcpLyf97n5534AKs2FksL1trA05R9uja3hBz59YRjrH652Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HoN1dosqKaU94zl1OmXBRRCOOqtpJaIuneOcBOicDsMgXDvsI657OCrSLKZDCmR3rgibSz9DuptrZbumXn4zJgF2H5HIWBqhxsEpW8rdKPZcA/640?from=appmsg)

攻击者换了物种，你的防线没换

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/usCmVxYib64d1NVv4vqic3EJh4jGZvuKZXb0quI7gMSbkGj9MhALaHXN5AuD7TpnBmQ3oM6d3zJKr5Jnvso5d579rNd5On0TV8JxKXdOxgDsU/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/y9RyYEv6VBc2nS2HYibdAe9EL6fia4WOUiaNeADw0Y4c9gCKkVDnKNudgJjvB4EurRI4bBMnJFRSPJpLaWNB537Q50Vgl2vHl8e7nLqpuhRYwc/640?from=appmsg)

问题不在于技术有多新，而在于——攻击者已经从“人”变成了“机器”。

过去，蜜罐的设计前提是“对手是个人”：人会疲惫、会犹豫、会留下可辨认的行为痕迹。而 AI 驱动的攻击者，可以快速识别、绕过传统静态蜜罐：那套部署后固化不变的“一次性陷阱”，在它眼里几乎“一眼假”，防御效果持续衰减。

更现实的压迫来自速度。Google GTIG/Mandiant 的同一份报告里，AI 代理的执行以 2—25秒为一次“爆发式”周期推进：脚本过大报错，它能自己删改后约 10 秒内重启；一次攻击单靠 AI 就产生了 240 条日志事件。这不是“更快的人”，而是一种不再需要休息、且能把失误成本压到近乎为零的节奏。

![](https://mmbiz.qpic.cn/mmbiz_png/QsTClNuIiapH9wvDQMzk6X5xvtAEyicOrkLGsGvqBy0SbG9mfyACANa6x6o8nzZo7zoM6crBJPX96V5I6rKUo9uf3NIwhciaGedICD5g2fwuaQ/640?wx_fmt=png&from=appmsg)

而防守方的节奏，却被卡在流程里。高危漏洞公开后，攻击者可在短时间内完成扫描、验证、利用；但关键行业的核心系统，往往要经过资产核对、兼容性验证、变更审批、回滚准备，才能完成一次安全升级——攻击窗口被压缩到小时级，补丁却在“按天、按周”排队。漏洞公开与补丁落地之间的这段空白期，正是风险最容易扩大的窗口，也是绝大多数“事后防护”手段失效的地带。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HoN1dosqKaU94zl1OmXBRRCOOqtpJaIuneOcBOicDsMgXDvsI657OCrSLKZDCmR3rgibSz9DuptrZbumXn4zJgF2H5HIWBqhxsEpW8rdKPZcA/640?from=appmsg)

猎影 AI 蜜罐：以 AI 猎 AI

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/usCmVxYib64d1NVv4vqic3EJh4jGZvuKZXb0quI7gMSbkGj9MhALaHXN5AuD7TpnBmQ3oM6d3zJKr5Jnvso5d579rNd5On0TV8JxKXdOxgDsU/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/y9RyYEv6VBc2nS2HYibdAe9EL6fia4WOUiaNeADw0Y4c9gCKkVDnKNudgJjvB4EurRI4bBMnJFRSPJpLaWNB537Q50Vgl2vHl8e7nLqpuhRYwc/640?from=appmsg)

面对 AI 黑客，安恒信息的答案是：用 AI 造一个它们认不出来的“数字猎场”。

在 2026 全球数字贸易博览会·西湖论剑上，安恒信息正式发布「猎影·AI 威胁狩猎诱捕系统」（简称猎影 AI 蜜罐）——全球首个捕获 AI 黑客的 AI 原生蜜罐。

它不是“放一个假资产等攻击”，而是用 AI 驱动高仿真诱捕环境构建、智能交互与攻击行为分析，让 AI 黑客在动态博弈中，主动暴露自己的路径与意图。

猎影的四大核心能力，环环相扣：

* 让陷阱更像真的：AI 智能生成、动态更新仿真靶标、应用与流量，让攻击者面对的不是几个孤立“假目标”，而是接近真实业务的数字猎场；
* 识别谁在攻击：基于攻击行为特征，区分人类黑客与 AI 黑客，识别其使用的 Skills、攻击过程与行为特征——从“看见一次异常”，升级为“理解攻击主体”；

* 让攻击自己暴露：通过动态攻防博弈，引导攻击主体持续暴露技战术，形成“诱捕→迟滞→溯源→反制”的闭环；

* 全链路溯源：基于 ATT&CK 框架还原攻击路径，把攻击行为沉淀为可复用的威胁情报。

把这四大能力放到客户的真实处境里，价值就落在了三类场景：

* 主动防御：支撑关键信息基础设施落实主动防御合规要求，开展未知威胁发现、攻击诱捕与溯源；

* 攻防演练：高仿真复刻业务环境诱导红队，完整记录攻击路径，反哺日常防护；

* 威胁情报：持续捕获 APT 攻击资产、未知样本与手法，沉淀 TTP 情报，赋能全网联防联控。

AI 黑客已经下场，它不会给你留出“等补丁、等流程”的时间。而猎影 AI 蜜罐要做的，是把防守前移到攻击发生之前——让每一次 AI 攻击，都变成可看见、可理解、可反制的安全资产。

以 AI 猎 AI，以智能御智能。猎影已出，AI 黑客的每一步，都将有迹可循。

![图片](https://mmbiz.qpic.cn/mmbiz_png/QsTClNuIiapGh0EgEoyffVPtJHSJ2rR650pzvHI4E2Voib4B1iapqgoOI9dibZ3LibibEJrZo4IgDI7lMJVAvHfqogz07WGobhxkVKzpwa2vt2RicA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

扫码获取免费试用

\*参考链接：

https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6Ppczr1X4OOTmbg4rENrqwqbYqRtgl3icicic9an9TicNrOnKOT4t2icSyx7w/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

**点点赞**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6P0OFJt7aruYwYjIWic5WCu7iaE9ZYWmW6TKPcvrib6Itmpc0dnMqlANmow/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

**点分享**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PwKHSiaCHQrj4D3mJJZ7QGPX1zbt3rJEKjhdBkX12A8r5L47fI28upaA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

**点喜欢**

点击下方名片立即关注

不走丢哦！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PzUETDErlviazPRtpVtc98iasfL8RCCib8yzmeGJ9HrBlJASFn5qz95QwQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6Pb2aOfdTZnZZbozL1mvicIWsdWicdDcibz2SAuHblLHicWQc8CmX6WT6OMA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PBQVNtt5ynIG7UjUHbRJFvFXgKjZW6mzjjhlxfjwtXfrdJyPgroKWQA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

**往期****精彩****回顾**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/4ZCae4yl53klulj6O0b7N5ze7sPltptcv23a1eYD0799Y8awib665MZbVGTgeeAHQH3hFnibibXNL2OzSRmaoic5ww/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)

[安恒信息加入世界旅游联盟，范渊分享AI重构文旅场景安全底座的路径](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653826&idx=1&sn=d15fcf5be5cfb58137e061ddeea5b48f&scene=21#wechat_redirect)

2026-11-12

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QsTClNuIiapHicHicsUfTIlKZl3WBHH7NIhKDtiagBw8ncXkWibPLnuSvWqcBaibATxoDaD7rz1x58uVg48O4NPnt2ibPrzic6Er2Xby1ibN5coqmibB8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653826&idx=1&sn=d15fcf5be5cfb58137e061ddeea5b48f&scene=21#wechat_redirect)

[涉密服务器还在逐台巡检？安恒涉密运维监控平台，打造“监-管-控-析”一体化方案](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653804&idx=1&sn=a30b811994bd07705bff60ffdf37e3d2&scene=21#wechat_redirect)

2026-11-11

[![](https://mmbiz.qpic.cn/mmbiz_jpg/QsTClNuIiapFyQp3HxtOcRVnvnqE0qIzuBbf6AVvPmXiaTXXNXiaSdDMfHqTke0hPsnbnKz7lD8hX2daf4JXKqWl2sQVicEia3hia5bGiclviaGuDrM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653804&idx=1&sn=a30b811994bd07705bff60ffdf37e3d2&scene=21#wechat_redirect)

[安恒信息MAF获公安部第三研究所大模型安全防护围栏（增强级）证书](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653795&idx=1&sn=073e1781e0a4501eecd4bacc352d576d&scene=21#wechat_redirect)

2026-11-10

[![](https://mmbiz.qpic.cn/mmbiz_jpg/QsTClNuIiapFiaUG25qWJSFSBw9lGTREOdM6A11alQezvlq6VLmQIzpTP61FcgYWnRhgTOx9GicegGQKk5icDzZ4ibNEhWU09Cic4G5gYkUodm2KU/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650653795&idx=1&sn=073e1781e0a4501eecd4bacc352d576d&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3wm5VicXg2ibVyMsjPZ3OJSzTwdeSU207GIcBicQDzkDVgFNvXD0npWKhFtBb2VtiaczibVqM8HE0vRoNw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/cbge2dLXia4bbQyBibIkuZz7hZVFlib5Oib5VZCiacheOLBHzKc88VEQYkXdC7BfdzLSVml0HWO6RjrP7FHL8oL0ONw/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=other&tp=webp#imgIndex=43)

法律声明

本文数据均来自内部统计、媒体报道、公开信息整理等，仅供信息分享，可能存在统计口径差异或误差，敬请理性看待，我们不对其准确性承担责任。股市有风险，投资需谨慎。阅读者在作出任何投资决定之前，应当咨询各自的顾问。本公众号发布内容仅代表内容创作视角，不构成任何投资建议或投资依据。在任何情况下，本公众号及运营主体不对任何人的投资结果承担法律责任。本公众号原创内容，欢迎合法合规复制、转载，转载时请务必注明出处，不得断章取义、以偏概全或进行有悖原意的引用。

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3yb7qoZWcKSwhTB3uxkfjDibSNP8lzqckKw2hXiarlP61qbUia2RUibZ15gV3hiabWypl17tkwrW7SaWOg/0?wx_fmt=png)

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