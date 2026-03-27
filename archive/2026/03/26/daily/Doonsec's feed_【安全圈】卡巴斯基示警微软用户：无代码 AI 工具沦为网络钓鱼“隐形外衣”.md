---
title: 【安全圈】卡巴斯基示警微软用户：无代码 AI 工具沦为网络钓鱼“隐形外衣”
url: https://mp.weixin.qq.com/s/E9vlGi5-MlyNIw-M5dSLgA
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:29:45.791980
---

# 【安全圈】卡巴斯基示警微软用户：无代码 AI 工具沦为网络钓鱼“隐形外衣”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEgKz3Rk7rCseGibdQzbiawDrXdzrIrEmPTtXbQrtO7xVuqCSXR4ZAl9GqyJiaYnpdXfrWUAVvzhUycqrcMUibFAw2ibf0zZUyxibicxs/0?wx_fmt=jpeg)

# 【安全圈】卡巴斯基示警微软用户：无代码 AI 工具沦为网络钓鱼“隐形外衣”

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意网页

卡巴斯基安全团队披露新型网络攻击手段，黑客正利用无代码 AI 建站平台 Bubble 生成并托管恶意网页应用，**专门用于盗取微软账户凭证。**

注：Bubble 是一种允许用户无需编写代码，仅通过可视化界面或自然语言描述即可快速构建网页应用程序的合法商业平台。

黑客通过这种方式将用户重定向至高度伪装的微软登录门户，这些假冒页面有时还会刻意隐藏在 Cloudflare 的安全验证背后。

一旦用户在这些页面输入账号密码，黑客便能轻易获取凭证，进而肆意访问受害者的电子邮件、日历及其他存储在 Microsoft 365 中的敏感数据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEE4BmaAW3zjfibfYDGSiangXsswjxf7PTSZgqoeC4AHC1GQEclgeQIIuo2lDF4E82LIIibslFqvQfKzc1ASo2uaH6xGWes4lpMug/640?wx_fmt=jpeg&from=appmsg)

这种新型钓鱼手段之所以能频频得手，主要归功于巧妙滥用合法平台。Bubble 作为一个由 AI 驱动的无代码开发平台，支持用户通过自然语言描述自动生成应用的前后端逻辑。

生成的应用会统一托管在 Bubble 的基础设施及受信任的域名（\*.bubble.io）下。电子邮件安全防护系统通常不会将此类高信誉域名标记为潜在威胁，因此包含这些链接的钓鱼邮件能够轻松穿透拦截网，直接送达目标用户的收件箱。

除了利用受信任的域名，这种攻击在底层代码层面也具备极强的反侦察能力。卡巴斯基研究人员指出，由 Bubble 平台自动生成的代码本质上是大量复杂 JavaScript 与孤立影子 DOM（文档对象模型）结构的混合体。

常规的静态扫描和自动化网页代码分析算法在处理这些庞杂的代码时往往会陷入逻辑混乱，最终错误地将其判定为功能正常的实用网站。**即便是经验丰富的安全专家，也需要耗费大量精力进行深度逆向分析，才能看透其真实的恶意目的。**

研究人员警告，该策略未来极有可能被 " 钓鱼即服务 "（PhaaS）黑产平台大规模采纳，并被无缝整合到低阶网络罪犯广泛使用的傻瓜式钓鱼工具包中。

鉴于这些黑产平台目前已经集成了会话 Cookie 盗取、绕过双重认证（2FA）等高级技术，滥用合法 AI 平台的加入无疑将使防御难度呈指数级上升。

***END***

阅读推荐

[【安全圈】上海警方深入推进“涉企网络谣言”打击整治：处置 270 余个违规账号，AI 洗稿编造车企销量下滑等行为被严惩](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075069&idx=1&sn=13b358d9c7991bf709ee2d720e484439&scene=21#wechat_redirect)

[【安全圈】AI 圈地震：月安装量约 9500 万次的 API 网关 LiteLLM 遭投毒](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075069&idx=2&sn=7ea915e24da062e25443aebe478f6c60&scene=21#wechat_redirect)

[【安全圈】HackerOne 披露员工数据泄露事件：第三方服务商 Navia 遭入侵](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075069&idx=3&sn=81030c6344d3eb99b31a0593ace75849&scene=21#wechat_redirect)

[【安全圈】马自达通报安全事件：员工和合作伙伴数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075041&idx=1&sn=ae9e793a53a8639e64c1a2ab362f1677&scene=21#wechat_redirect)

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