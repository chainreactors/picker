---
title: 攻击者已利用ChatGPT编写恶意代码
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515233&idx=3&sn=acc0f7a96702e65796637a360acf5510&chksm=ea948d0bdde3041dc094027cc96639bf548ab737e3da4cbb80f6cb46f6c3bad46bb7c78a2dc5&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-11
fetch_date: 2025-10-04T03:32:29.305951
---

# 攻击者已利用ChatGPT编写恶意代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSQcYibaBOwKsFjjfjY4y4iakkLCic9aM25Z1frASYrskPsIV0O7LxG7F8iaL82HgkOgRF6odmYtDewYQ/0?wx_fmt=jpeg)

# 攻击者已利用ChatGPT编写恶意代码

Jai Vijayan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**自OpenAI 在2022年11月发布ChatGPT以来，安全研究人员就预测称，网络犯罪分子开始利用这个AI聊天机器人编写恶意软件和执行其它恶意活动就只是时间问题。就在几周后，貌似这个时间已到。**

Check Point Research (CPR) 的研究人员指出，至少在地下论坛发现三个黑帽黑客利用ChatGPT 实施恶意目的的实例。

ChatGPT 是一款AI驱动的原型聊天机器人，适用于大量用例，包括代码开发和调试。它的主要亮点之一是能够使用户以对话方式与之交互，并获得在所有领域的协助，如编写软件、理解复杂主题、编写论文和邮件、提升客户服务以及测试不同的商业或市场场景等。

但ChatGPT也可用于恶意场景。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSQcYibaBOwKsFjjfjY4y4iakMonRj3kEZicRVTvL3ehYicvqkGzq6J32S6JluYlHbT3fI6ooY0UafGbQ/640?wx_fmt=png)

**从编写恶意软件到创建暗网市场**

在一个场景中，恶意软件作者在其它网络犯罪分子使用的论坛中披露了自己如何和ChatGPT进行试验，查看自己能否重新创建已知恶意软件和技术。例如，他通过ChatGPT分享了自己开发的基于 Python的信息窃取器，可从受感染系统中搜索、复制并提取12种常见的文件类型如Office 文档、PDF和镜像等。这个恶意软件作者还展示了如何使用ChatGPT编写Java代码，下载PuTTY SSH 和远程登录客户端，并通过PowerShell 在系统上静默运行。

2022年12月21日，昵称为 “USDoD”的威胁行动者贴出一个通过ChatGPT生成的Python 脚本，通过Blowfish和Twofish 加密算法加密和解密数据。CPR研究人员发现虽然该代码可用于非恶意目的，但威胁行动者可轻松修改在无需用户交互的情况下在系统运行，将其修改为勒索软件。和信息窃取工具的作者不同，USDoD 的技术能力似乎非常有限，并且生成自己生成的 Python 脚本是自己生成的第一个脚本。

在第三个案例中，研究人员发现一名网络犯罪分子讨论自己如何使用ChatGPT创建了完全自动化的暗网市场，可用于交易被盗银行卡和支付卡数据、恶意软件工具、毒品、弹药和多种其它非法商品。

研究人员指出，“为了展示如何将ChatGPT用于这些恶意目的，该犯罪分子发布了一份代码，它通过第三方API 获得当前的加密密币价格作为暗网市场支付系统的一部分。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSQcYibaBOwKsFjjfjY4y4iakMonRj3kEZicRVTvL3ehYicvqkGzq6J32S6JluYlHbT3fI6ooY0UafGbQ/640?wx_fmt=png)

**无需任何经验**

自去年11月份推出ChatGPT以来，关于遭滥用的话题就一直不断。很多安全研究员认为ChatGPT 大大降低了编写恶意软件的难度门槛。

Check Point 公司的威胁情报团队经理 Sergey Shykevich 重申，恶意人员无需任何编程经验就能够通过ChatGPT编写恶意软件，“你应该只需知道恶意软件或任何程序应该具备的功能，ChatGPT就能够替你编写代码，执行所需功能。”因此，“短期担忧绝对和ChatGPT允许低技能网络犯罪分子开发恶意软件有关。长期来看，我认为更多高技能网络犯罪分子会通过ChatGPT 改进活动效率或者解决可能具有的不同差距。”

从攻击者角度来看，AI代码生成系统可使恶意人员通过ChatGPT这一语言之间的翻译来缩短任何技能缺口。这类工具提供了创建与攻击者目标相关的代码模板的按需模式，并削减了通过开发者网站如 Stack Overflow 和 Git等搜索的需求。

甚至在发现ChatGPT 遭滥用之前，研究人员就说明了竞争对手可如何将其用于恶意活动中。2022年12月19日，Check Point 公司发布一篇博客文章，说明了研究人员如何仅通过要求ChatGPT 编写看似来自虚构的网络托管服务，就创建了一份非常具有说服力的钓鱼邮件。研究人员还展示了如何让ChatGPT 编写可复制到Excel 中的VBS代码，用于从远程URL中下载可执行文件。这一演练的目标是展示攻击者如何利用ChatGPT等人工智能模型，执行多种活动如鱼叉式钓鱼邮件创建完整的感染链、在受感染系统上运行反向shell等。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSQcYibaBOwKsFjjfjY4y4iakMonRj3kEZicRVTvL3ehYicvqkGzq6J32S6JluYlHbT3fI6ooY0UafGbQ/640?wx_fmt=png)

**让网络犯罪分子更难以利用**

OpenAI和其它类似工具的开发人员已通过过滤器和控制来尝试限制对技术的滥用。至少目前来看，这些AI工具仍然存在一些问题并易出现很多研究人员说的彻底错误，这样可阻止一些恶意行为。即便如此，很多人认为长期来看，这些技术遭滥用的可能性仍然很大。

为使犯罪分子更难以滥用这些技术，开发人员将需要训练和改进AI引擎，识别可遭恶意滥用的请求。其它选择是执行使用该引擎的认证和授权要求。即使是执行目前在线金融机构和支付系统在使用的要求也已足够。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[堪比“震网”：罗克韦尔PLC严重漏洞可导致攻击者在系统中植入恶意代码](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511227&idx=1&sn=d28db703c4a8b363e328e4d7bd31acb6&chksm=ea949dd1dde314c7695fa5ecca6c16c0f8905de7f968f34a026fb212d3db07b9891b7995210f&scene=21#wechat_redirect)

[恶意软件利用合法的代码签名证书横行Windows 系统](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509867&idx=3&sn=3e423e37340d1ec03ca3ebd8036549a7&chksm=ea949601dde31f176af33dcf46929b15917a82ab96d52cf936fe90b019129b5526ad391fc35a&scene=21#wechat_redirect)

[速修复！热门代码覆盖率测试工具 Codecov 的脚本遭恶意修改，敏感信息被暴露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247503503&idx=1&sn=b571f78d11b62e2b42d472f322394979&chksm=ea94ffe5dde376f3fd8a34d12aa8e6f6869b4e8ca5b6a5fb464d01fdfbb7bad802bb6546620b&scene=21#wechat_redirect)

[美国或将禁止出口人工智能等敏感技术](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488578&idx=3&sn=525e2e16db3a5e2142ef5595271e8b9b&chksm=ea972528dde0ac3eb9dd7b1cbc06159a547ccefd2648d1a1f119d6c4a592c92678ef766d51c9&scene=21#wechat_redirect)

[开源软件源代码安全缺陷分析报告——人工智能类开源软件专题](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247488221&idx=1&sn=3e2b466542346f22af1271dcefacb99c&chksm=ea9723b7dde0aaa1530c93251b5cbaa5a9b1129ac569d89276697aa83abeee10397db8131471&scene=21#wechat_redirect)

[微软为Win 10增加基于人工智能的高级杀毒软件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485503&idx=2&sn=6abfcb67076fa0b792f044225a240863&chksm=ea973955dde0b0437b2d085b1846c053a14a58f89f65740c6e2b3f56fcca0f5380d1312abe1c&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/attacks-breaches/attackers-are-already-exploiting-chatgpt-to-write-malicious-code

题图：Pixabay License‍

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