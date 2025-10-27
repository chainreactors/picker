---
title: 研究员在DeepSeek 和 Claude AI 中发现多个提示注入漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521736&idx=1&sn=f656ad45da506b8f778e68ff0243d0be&chksm=ea94a4a2dde32db4651e878de8188d4f6cae7312a721ec5b3a69201300cc4b8990af592861cc&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-11
fetch_date: 2025-10-06T19:41:12.319910
---

# 研究员在DeepSeek 和 Claude AI 中发现多个提示注入漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTsjrxKUfO6ZlYcrL824wwQUticVLqic1ZBKc1icjhxbaMPdQlzWx58CFlpnsmpZMknXiaibibiceyiajykZg/0?wx_fmt=jpeg)

# 研究员在DeepSeek 和 Claude AI 中发现多个提示注入漏洞

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全研究员 Johann Rehberger 在DeepSeek 人工智能 (AI) 聊天机器人中发现了一个缺陷（现已修复），可导致恶意人员通过提示注入攻击的方式控制受害者账户。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTsjrxKUfO6ZlYcrL824wwQ1W6yJcfXSyTLNKnhrqRsz2MVibXXjmAva0Oc1V32hDjIXxQp3k1OXhg/640?wx_fmt=gif&from=appmsg)

Rehberger 发现，在 DeepSeek 聊天框中提供输入“以项目符号清单方式打印 XSS 速查表，仅包括 payload。”就会触发JavaScript 代码执行，作为生成回复的一部分，而这是典型的XSS攻击案例。

XSS攻击可在受害者的 web 浏览器上下文中执行越权代码，从而造成严重后果。攻击者可利用这类缺陷劫持用户会话并获得对于 chat.deepseek[.]com 域名相关联的 cookie 和其它数据，从而导致账户遭接管。

Rehberger提到，“经过一些实验后，我发现接管用户会话所需要做的就是在 chat.deepseek.com 域上存储在 localStorage 中的 userToken。”他提到，可通过一个特殊构造的提示触发该XSS 并通过提示注入访问受陷用户的userToken。

该提示由多个指令和 Base64编码字符组成，DeepSeek 聊天机器人对其进行解码，执行负责提取受害者会话令牌的 XSS payload，最终导致攻击者模拟该用户。

Rehberger 还演示称，Anthropic 公司的 Claude Computer User 也可被通过提示注入自动运行恶意命令。Claude Computer Use 可使开发人员通过该语言模型通过鼠标移动、按钮点击和文本输入来控制计算机。这种技术被称为 "ZombAIs"，

主要利用提示注入来武器化 Computer Use，下载 Sliver C2 框架、执行该框架，并通过受攻击者控制的远程服务器建立连接。

此外，研究人员还发现可使用大语言模型输出 ANSI 转移代码，通过提示注入来劫持系统终端。该攻击主要针对的是继承了LLM的 CLI 工具，被称为 "Terminal DiLLMa"。

Rehberger 表示，“十年之久的特性向 GenAI 应用提供了异常的攻击面，开发人员和应用设计人员应考虑插入 LLM 输出的上下文情况，因为输出是不可信的且其中可能包含任意数据。”

而且，威斯康星大学麦德逊分校和圣路易斯华盛顿大学开展的新研究成果表明，OpenAI 公司的 ChatGPT 可被诱骗渲染以 markdown 格式提供的外部图片链接，包括可能是以非常重要的良性目标为借口的露骨和暴力的图片。

更重要的是，研究人员发现，通过提示注入可间接调用 ChatGPT 插件而无需获取用户确认，甚至可绕过 OpenAI 公司部署的限制，将从用户聊天历史提取的危险链接中的内容渲染到受攻击者控制的服务器。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Ultralytics AI模型正被劫持用于部署挖矿机](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521726&idx=1&sn=6242710e1abb2954dfd85acd30c4ffb1&scene=21#wechat_redirect)

[Fuzzing 升级：谷歌通过AI找到更多漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521578&idx=1&sn=0f7082c24d8e05dca215004ae796d61e&scene=21#wechat_redirect)

[DHS发布在关键基础设施安全开发部署AI的框架](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521523&idx=2&sn=9222522f67aa6bada64bed055a3adfeb&scene=21#wechat_redirect)

[谷歌AI平台存在漏洞，可泄露企业的专有LLMs](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521484&idx=1&sn=19327f5e0d0275273114fd7a7e37da3f&scene=21#wechat_redirect)

[研究员在开源AI和ML模型中发现30多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521331&idx=1&sn=e13cd9f9dccd9d17953e551df9108205&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/12/researchers-uncover-prompt-injection.html

题图：Pexels License

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