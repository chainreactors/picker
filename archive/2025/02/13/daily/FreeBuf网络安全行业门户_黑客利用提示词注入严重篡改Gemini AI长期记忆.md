---
title: 黑客利用提示词注入严重篡改Gemini AI长期记忆
url: https://www.freebuf.com/news/421630.html
source: FreeBuf网络安全行业门户
date: 2025-02-13
fetch_date: 2025-10-06T20:35:07.261960
---

# 黑客利用提示词注入严重篡改Gemini AI长期记忆

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

黑客利用提示词注入严重篡改Gemini AI长期记忆

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)
* [漏洞](https://www.freebuf.com/articles/vuls)

黑客利用提示词注入严重篡改Gemini AI长期记忆

2025-02-12 08:35:42

所属地 上海

![image](https://image.3001.net/images/20250212/1739368889145054_435fad7fd6e64d54ab5c072f80442699.webp!small)

近日，一场针对谷歌 Gemini Advanced 聊天机器人的复杂攻击被曝光。该攻击利用间接提示词注入和延迟工具调用这两种手段，成功破坏了 AI 的长期记忆，使攻击者能够在用户会话间植入虚假信息。

这一漏洞引发了人们对生成式AI系统安全性的严重担忧，尤其是那些旨在长期保留用户特定数据的系统。

## **提示词注入与延迟工具调用**

提示词注入是一种网络攻击方式，攻击者将恶意指令隐藏在看似无害的输入（如文档或电子邮件）中，交由AI处理。

间接提示词注入是一种更为隐蔽的变体，恶意指令被隐藏在外部内容中。AI将这些嵌入的指令误解为合法的用户提示，从而执行非预期的操作。

根据Johann Rehberger的研究，该攻击基于一种名为延迟工具调用的技术。恶意指令不会立即执行，而是等待特定用户行为触发，比如用户回复“是”或“否”等关键词。这种方式利用了AI的上下文感知能力及其优先考虑用户意图的倾向，避开了许多现有保护措施。

攻击的目标是Gemini Advanced，这是谷歌配备长期记忆功能的高级聊天机器人。

* **通过不可信内容注入：**攻击者上传恶意文档，并由Gemini进行摘要。文档中隐藏着操纵摘要过程的指令。
* **触发式激活：**摘要中包含一个隐性请求，将记忆更新与特定用户响应相关联。
* **记忆篡改：**如果用户在不知情的情况下用触发词回复，Gemini会执行隐藏指令，将虚假信息（如伪造的个人资料）保存到长期记忆中。

例如，Rehberger演示了这种策略如何让Gemini“记住”某位用户年龄102岁、相信地平说，并且生活在类似《黑客帝国》的模拟反乌托邦世界中。这些虚假记忆会跨越会话持续存在，并影响后续交互。

## **长期记忆操纵的潜在影响**

AI系统的长期记忆旨在通过跨会话调用相关细节来增强用户体验。然而，一旦被利用，这一功能就变成了双刃剑。被篡改的记忆可能导致：

* **误导信息：**AI可能基于虚假数据提供不准确的回应。
* **用户操纵：**攻击者可以诱导AI在特定情况下执行恶意指令。
* **数据泄露：**通过将敏感信息嵌入指向攻击者控制服务器的Markdown链接等创造性方式，可能导致数据外泄。

尽管谷歌已承认这一问题，但对其影响和危险性进行了淡化。该公司认为，攻击需要用户被钓鱼或诱导与恶意内容互动，这种场景在大规模范围内不太可能发生。此外，Gemini在存储新的长期记忆时会通知用户，为警惕的用户提供了检测和删除未经授权条目的机会。

然而，专家指出，仅解决表象而非根源问题，系统依然存在漏洞。Rehberger强调，尽管谷歌已限制Markdown渲染等特定功能以防止数据泄露，但生成式AI的基础问题仍未得到解决。

这一事件凸显了确保大型语言模型（LLMs）免受提示词注入攻击的持续挑战。

**参考来源：**

> [Hackers Exploit Prompt Injection to Tamper with Gemini AI’s Long-Term Memory](https://cybersecuritynews.com/hackers-exploit-gemini-prompt-injection/)

# 网络安全 # web安全

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

提示词注入与延迟工具调用

长期记忆操纵的潜在影响

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)