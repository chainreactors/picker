---
title: 【安全圈】黑客利用 LLMjacking 牟利，以每月 30 美元的价格出售被盗的 AI 访问权限
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067721&idx=2&sn=6318faf5565268c7590c5ce1ffbb4f9d&chksm=f36e7bc9c419f2df79f0bff1044125b2ea3f5b89c4c66c5baf6ad9fb88dfab28073d13427fff&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-10
fetch_date: 2025-10-06T20:37:06.542269
---

# 【安全圈】黑客利用 LLMjacking 牟利，以每月 30 美元的价格出售被盗的 AI 访问权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1oOYoHUQm0a2cy9I03m1lAWs7N9R4tD8Xd2usgvObRReWDrYA0ZxGoBmcmfreurkTSFMPaJzsjg/0?wx_fmt=jpeg)

# 【安全圈】黑客利用 LLMjacking 牟利，以每月 30 美元的价格出售被盗的 AI 访问权限

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

人工智能

Sysdig 威胁研究团队 (TRT) 自2024 年 5 月首次发现 LLMjacking 攻击以来，就一直观察到其快速发展，包括扩展到 DeepSeek 等新的大型语言模型 (LLM)。据报道，DeepSeek-V3 发布几天后，它就被集成到 ORP 实例中，这表明攻击者的适应速度非常快。

### **利用 DeepSeek API 密钥和 LLMjacking 获利**

据研究人员称，DeepSeek-R1 在发布后不久就被纳入这些平台。研究人员发现多个 ORP 中都填充了 DeepSeek API 密钥，这表明该新模型正在被积极利用。

LLMjacking 的出现是由于使用基于云的 LLM 的成本过高，攻击者会入侵账户，免费使用这些昂贵的服务。根据 TRT 的最新发现，LLMjacking 已成为一种成熟的攻击媒介，在线社区积极分享工具和技术。

他们发现 LLMjacking 的货币化程度有所上升，LLM 访问权限通过 ORP（OpenAI 反向代理）出售，据报道，其中一个实例的访问权限售价为每月 30 美元。运营商通常低估了与 LLM 使用相关的成本，而研究人员注意到，在一个实例中，正常运行时间仅为 4.5 天，产生了近 50,000 美元的成本，其中 Claude 3 Opus 的成本最高。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1oOYoHUQm0a2cy9I03m1lswXUOkCdKlV8BGIqjzPBtjdUqvGFhMq6sdnLtGTwKgInrZC8X1eOLA/640?wx_fmt=jpeg&from=appmsg)

###

### **资源开发规模**

在观察到的 ORP 中，令牌（LLM 生成的单词、字符集或单词/标点符号组合）的总使用量超过 20 亿，凸显了资源利用的规模。受害者是合法帐户持有者，他们的凭据已被盗用。

ORP 使用仍然是 LLMjacking 的常用方法。ORP 服务器充当各种 LLM 的反向代理，可以通过 Nginx 或 TryCloudflare 等动态域公开，从而有效掩盖攻击者的来源。这些代理通常包含来自不同提供商（如 OpenAI、Google AI 和 Mistral AI）的大量被盗 API 密钥，使攻击者能够向其他人提供 LLM 访问权限。

“Sysdig TRT 发现十多个代理服务器在许多不同的服务中使用被盗凭证，包括 OpenAI、AWS 和 Azure。LLM 的高成本是网络犯罪分子（如下例所示）选择窃取凭证而不是支付 LLM 服务的原因，”研究人员在博客文章中指出。

### **在线社区利用 LLMjacking**

4chan 和 Discord 等在线社区通过 ORP 促进了 LLM 访问权限的共享。Rentry.co 用于共享工具和服务。研究人员在蜜罐环境中的 LLM 提示日志中发现了大量 ORP 代理，其中一些代理使用自定义域，另一些使用 TryCloudflare 隧道，可追溯到攻击者控制的服务器。

凭证窃取是 LLMjacking 的一个重要方面，攻击者以易受攻击的服务为目标，并使用验证脚本来识别访问 ML 服务的凭证。公共存储库也提供公开的凭证。定制的 ORP（通常经过修改以保护隐私和隐秘性）用于访问被盗帐户。

为了打击 LLMjacking，保护访问密钥和实施强大的身份管理至关重要。最佳做法包括避免硬编码凭证、使用临时凭证、定期轮换访问密钥以及监控暴露的凭证和可疑的帐户行为。

来源：https://hackread.com/hackers-monetize-llmjacking-selling-stolen-ai-access/

***END***

阅读推荐

[【安全圈】韩某某投敌叛变，48小时内被国安抓捕归案](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=1&sn=7f31eb8f0f2b9706fa2bb95c56de54b9&scene=21#wechat_redirect)

[【安全圈】慧与Office 365 邮件服务遭攻击，至少 16 名员工隐私数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=2&sn=3fed7e8c8d5ff870c7d74733e568e26f&scene=21#wechat_redirect)

[【安全圈】微软示警 ASP.NET 重大安全漏洞，超3000公开密钥恐致服务器沦陷](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=3&sn=42ec007bcefb5e73b814bbd77c03cb62&scene=21#wechat_redirect)

[【安全圈】曝英国要求苹果留“后门”：允许其检索全球任何用户上传到云端的所有内容](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067706&idx=4&sn=932d329534a041f36ccec808cef39b2e&scene=21#wechat_redirect)

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