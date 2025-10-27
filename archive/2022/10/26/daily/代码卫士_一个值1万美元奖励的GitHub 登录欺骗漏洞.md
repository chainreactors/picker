---
title: 一个值1万美元奖励的GitHub 登录欺骗漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514319&idx=3&sn=6dd16dc42aa628d2d112e9e0f6512428&chksm=ea9489a5dde300b3d2d064af27d6ad29e9592f0c42842c936f2cff8d04443759b19d1a8545b5&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-10-26
fetch_date: 2025-10-03T20:55:58.538697
---

# 一个值1万美元奖励的GitHub 登录欺骗漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTWdwrkSsm0ZibM3IpjiaSWHJ02ZkpfL9S5ONsCrZMdSIRbVs7kd2OTicLMf1m5ujyEyicM0HhLjJHI1Q/0?wx_fmt=jpeg)

# 一个值1万美元奖励的GitHub 登录欺骗漏洞

Jessica Haworth

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

安全研究员 Saajan Bhujel 发现了欺骗GitHub 登录接口的方法，并借此获得1万美元的漏洞奖励金。

Bhujel 发现可通过一个绕过更改该网站的CSS，从而诱骗用户登录至虚假页面。GitHub 使用开源JavaScript 显示引擎 MathJax 进行 LaTeX、MathML 和 AsciiMath进行标记。用户可通过MathJax 库在Markdown 中渲染或显示数学表达式。

Bhujel 发现，通过注入过滤且删除的恶意标记可绕过MathJax的HTML过滤，之后注入表单元素，欺骗GitHub 登录接口。他通过一种不同技术将问题告知GitHub，当GitHub 发现他的提交重复时，Bhujel 使用另外的技术使自己找到了该绕过。

Bhujel表示获得1万美元的奖励“非常高兴”，尽管最初将其定为低危级别而上报。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[GitHub 2019年漏洞奖励计划最值得回顾的2个精彩 bug](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492619&idx=1&sn=8e05654cbcedf82d4c60965f7abd9608&chksm=ea94d561dde35c7770317e837f86df946bfc715e27adcb9e338e715c02dabf8982341ec9f449&scene=21#wechat_redirect)

[GitHub 推出“安全实验室”和漏洞奖励计划，提升开源生态系统安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247491566&idx=2&sn=e782abb86e587bb48d8b102acd027fa7&chksm=ea972e84dde0a792dee0cd8513ef4520fd24971325023bdf9670abe5a695e8f90e2b3bad397b&scene=21#wechat_redirect)

[五周年庆：GitHub 漏洞奖励计划扩大范围提高赏金](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489240&idx=1&sn=ec285a82712076bf14c937a5c6ca2a2d&chksm=ea9727b2dde0aea4d3a80fd88bc7810b6fcf7393231e442c7d6b702fe665664f816dcb2937fd&scene=21#wechat_redirect)

**原文链接**

https://portswigger.net/daily-swig/login-spoofing-issue-in-github-nets-researcher-10k-bug-bounty-reward

题图：Pixabay License‍

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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