---
title: 微软GitHub Copilot 被诉违反开源许可条款和侵犯开发人员权益
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514414&idx=1&sn=a937561278e4afeadc5816a57d8be22c&chksm=ea948844dde301521c4b577e4e0e5e3292436a79499f9b3e00726bd0f3a03f3400c521010ded&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-11-08
fetch_date: 2025-10-03T21:56:52.751627
---

# 微软GitHub Copilot 被诉违反开源许可条款和侵犯开发人员权益

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRib1W60OwVsAUicpkzzfC9EIUBnmCnica6PE7V47M8hlaicx8HkCFP6gJaCMQe3SDoJXx6LE0ynqDhTg/0?wx_fmt=jpeg)

# 微软GitHub Copilot 被诉违反开源许可条款和侵犯开发人员权益

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRib1W60OwVsAUicpkzzfC9EIYfoIBPnb1PsdkP6hlC1bppKjfsEWwb9vN0EyNGZaBWEJ5MCC2ykIwg/640?wx_fmt=gif)

**程序员兼律师 Matthew Butterick 起诉微软、GitHub 和 OpenAI称，GitHub Copilot 违反了开源许可协议并侵犯了编程人员的权益。**

GitHub Copilot 发布于2022年6月，是一款基于AI的编程助手，使用 OpenAI Codex在Visual Studio中生成实时源代码和函数建议。研究人员使用公开仓库中的数十亿行代码，通过机器学习训练了该工具，该工具可将数十种编程语言的自然语言转换为代码片段。

**将作者踢出局**

虽然 Copilot 可提高代码编写速度，让软件开发变得更容易，但其使用开源代码的行为使专家担忧违反了许可归属和限制条件要求。

开源许可证如GPL、Apache 和 MIT 许可证等，要求进行作者姓名归属以及明确特定版权。然而，Copilot 正在删除这一组件，甚至当代码片段长度大于150个字符且直接从训练集中提取时，并不会给出作者归属。

一些编程人员甚至认为这种行为是“开源洗白”，这种方式带来的法律问题随着该AI工具的发布而得以证实。

代表Butterick 的律所 Joseph Saveri 评论称，“微软似乎通过忽视底层开源许可条件和其它法律要求，通过他人的成果牟利。”更糟糕的是，人们发现Copilot错误地将机密信息公开发布在公开仓库中，导致这些信息如API密钥被包含在训练集中。

除了违反许可条款外，Butterick 还表示开发特性违反了如下要求：

* GitHub 的服务和隐私策略条款
* DMCA 1202，该条款禁止删除版权管理信息
* 加利福尼亚消费者隐私法案
* 以及其它法律要求

该起诉提交至美国地方法院加利福尼亚北区，要求批准法定损害赔偿90亿美元。该起诉书指出，“Copilot 每次提供不合法的输出时，它就三次违反 Section 1202（在没有（1）归属（2）版权通知和（3）许可条款的情况下分发许可材料）。因此，如果每名用户在使用Copilot 期间仅收到违反 Section 1202的一份输出（最早的使用者最多使用期限是15个月），那么GitHub 和 OpenAI 违反DMCA的次数就达到360万次。每次违反的最低法定损害是2500美元，因此最终为90亿美元。”

**损害开源生态**

Butterick 还在今年10月初在文章中提到了另外一个主题，提到了Copilot 为开源社区造成的损害。

他表示，向人们提供代码片段但不告诉代码创造人是谁，使得开源贡献和协作的动力严重丧失了。微软正在制造一个新的围墙花园，它将阻止编程人员发现传统的开源社区。随着时间的流逝，这一流程将使开源社区荒废。用户注意力和参与度将远离原仓库本身——远离其源仓库、问题追踪工具、邮件列表和讨论版。”

Butterick 担心在足够长的时间内，Copilot 将导致开源社区减少，进而导致该训练集数据中的代码质量下降。

GitHub 评论称，“从一开始，Copilot就致力于负责任地创新，而且将继续改进产品，为全球开发人员提供最好的服务。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[GitHub账户重命名可引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514352&idx=1&sn=7105ffba7a58b1c73df803461e6ca7ef&chksm=ea94899adde3008cbc9d8ee004890757957a4b7b7c5ada48418a5c0efd8425cad376d4679fdd&scene=21#wechat_redirect)

[一个值1万美元奖励的GitHub 登录欺骗漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514319&idx=3&sn=6dd16dc42aa628d2d112e9e0f6512428&chksm=ea9489a5dde300b3d2d064af27d6ad29e9592f0c42842c936f2cff8d04443759b19d1a8545b5&scene=21#wechat_redirect)

[钱少事多，开源项目维护人员几乎集体出走](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505473&idx=1&sn=79d809ceb8dad379225bdc25bfacd0ea&chksm=ea94e72bdde36e3d1e6a3003252d209da211b88eb74193980a3e9d3f3d573070a8521cddc686&scene=21#wechat_redirect)

[Netflix 推出漏洞奖励计划并承诺不会起诉研究人员](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247486734&idx=3&sn=5795db4526f4785e450e40114d473139&chksm=ea973c64dde0b572b9405c6473cfdc9e510c251056901e4ef0130a29e0fdbe75fdce78b4de85&scene=21#wechat_redirect)

[新型NPM计时攻击可导致供应链攻击，GitHub 不打算修复](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514198&idx=1&sn=896500007d3b6e8878a313e75f4f0440&chksm=ea94893cdde3002ab918f2937fefc42dece54a931457ca7274fbea4258224d4cc93342f08b7d&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/microsoft-sued-for-open-source-piracy-through-github-copilot/

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