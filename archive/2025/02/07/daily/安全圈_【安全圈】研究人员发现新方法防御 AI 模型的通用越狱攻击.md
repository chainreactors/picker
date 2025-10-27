---
title: 【安全圈】研究人员发现新方法防御 AI 模型的通用越狱攻击
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067669&idx=4&sn=027c0126ec6f44288fe766c11d208124&chksm=f36e7b15c419f20345dae8c76fd939a1638e36abef0ed5208d33d6a1f2e08fface283528ac0b&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-07
fetch_date: 2025-10-06T20:37:44.591855
---

# 【安全圈】研究人员发现新方法防御 AI 模型的通用越狱攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IEeCWZhmichJyiclBV1anF4kts6mZxFrIRl987fLQ0HkuNxMGnjo615gww/0?wx_fmt=jpeg)

# 【安全圈】研究人员发现新方法防御 AI 模型的通用越狱攻击

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

人工智能

来自Anthropic保障研究团队的研究人员开发了一种新方法，用于保护人工智能模型免受通用越狱攻击。这种创新方法被称为“宪法分类器”，已在数千小时的人类红队测试和合成评估中表现出了显著的抗攻击能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IEP33icxXOWcQQxl0QQaayiaCvmOZDEOMCQgPgGAiaXIzua7qX3n9V6fqlA/640?wx_fmt=jpeg&from=appmsg)

通用越狱攻击是指攻击者通过精心设计的输入，绕过人工智能模型的安全防护，迫使模型产生违反其安全准则的有害回应。这些攻击可能涉及用长提示信息淹没模型，或者使用不寻常的大写方式改变输入风格，尽管经过广泛的安全训练，大型语言模型仍然容易受到此类漏洞利用的攻击。

## 宪法分类器的工作原理

宪法分类器是基于合成数据训练的输入和输出分类器。它们能够过滤掉大多数越狱尝试，同时将过度拒绝率降至最低，并保持适度的计算开销。该系统基于“宪法”——一份定义允许和禁止内容类别的原则清单。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IERia5N5lHSErUmL0YBiaMCAT1icjjrYZto46GA9sREiceamZ5r07qvtYhLg/640?wx_fmt=jpeg&from=appmsg)

宪法分类器的训练和实施（来源：Anthropic）

以下是其工作原理：

* 宪法制定：制定一部宪法，明确无害和有害的类别。
* 合成数据生成：根据宪法，生成大量涵盖所有内容类别的合成提示和模型完成内容。这些数据通过翻译成不同语言以及模仿已知越狱风格进行增强。
* 分类器训练：使用合成数据训练输入和输出分类器，以检测和阻止有害内容。
* 部署：将这些分类器作为保护 AI 模型的安全措施实施。

## 实际测试结果

在一个漏洞赏金计划中，183名活跃参与者花费超过3000小时，试图对保护Claude 3.5 Sonnet的原型系统进行越狱。尽管奖金丰厚，但并未发现任何通用越狱漏洞。不过，该原型系统的过度拒绝率和计算成本较高。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylh0OtQqnxj1IibMicodHicl4IEyxyV7ic3NzAae5QGcGehSJWeWXYpOhbPbTtmwicSpdAUV38piczRO3Ygg/640?wx_fmt=jpeg&from=appmsg)

自动化评估结果（来源：Anthropic）

宪法分类器的更新版本在Claude 3.5 Sonnet上进行了测试，使用了1万个合成越狱提示。越狱成功率从86%降至4.4%，拒绝率仅略有上升（0.38%），额外计算成本适度增加（23.7%）。

虽然宪法分类器为AI模型提供了显著的保护，但要注意的是，它们并非万无一失。研究人员建议使用补充防御措施，并根据新出现的越狱技术不断调整“宪法”。

不过这一突破确实为未来安全部署更强大的 AI 模型带来了希望，减轻了越狱相关的风险，并确保AI系统符合安全原则。

2025年2月3日至2月10日，宪法分类器系统的实时演示将开放供红队测试。此次演示专注于与化学武器相关的查询，并邀请用户尝试越狱，以提供对系统改进的宝贵反馈。

来源：https://cybersecuritynews.com/researchers-uncovers-new-methods-to-defend-ai-models/#google\_vignette﻿

***END***

阅读推荐

[【安全圈】DeepSeek遭遇大规模网络攻击，暂停新用户注册](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=1&sn=110423832f37fabbb95e2bc014e2efb1&scene=21#wechat_redirect)

[【安全圈】DeepSeek AI 数据库曝光：超过 100 万行日志、密钥泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=2&sn=c07d521bd863d5ef6b8232fd91c2d58e&scene=21#wechat_redirect)

[【安全圈】Pwn2Own Automotive 2025 黑客因破解 49 个零日漏洞获 886,250 美元奖励](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=3&sn=15fafdc5115ba7e7a871e108304d8284&scene=21#wechat_redirect)

[【安全圈】以色列间谍软件公司Paragon涉嫌利用WhatsApp零点击漏洞发动攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067643&idx=4&sn=cee4f0162f4215b03faa784f2a08ca29&scene=21#wechat_redirect)

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