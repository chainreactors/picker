---
title: NDSS 2026杰出论文奖丨复旦大学计算与智能创新学院系统软件与安全实验室研究成果首次系统揭示邮箱别名机制的身份混淆安全漏洞
url: https://mp.weixin.qq.com/s/UoSfDePfvoxwpyoWkDz0hQ
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:16:32.510198
---

# NDSS 2026杰出论文奖丨复旦大学计算与智能创新学院系统软件与安全实验室研究成果首次系统揭示邮箱别名机制的身份混淆安全漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTOMLkOGeDkCNJzr4GRZ0heHUgEFLCObWQODHjDo4ic93pI9mEMkuQ8JlGibmdYanyc2swLK4rTok4bGsWnu6TMKNQj9tMzmxZOr0/0?wx_fmt=jpeg)

# NDSS 2026杰出论文奖丨复旦大学计算与智能创新学院系统软件与安全实验室研究成果首次系统揭示邮箱别名机制的身份混淆安全漏洞

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

**NDSS 2026杰出论文奖**

**首次系统揭示邮箱别名机制的身份混淆安全漏洞**

**导语**

复旦大学计算与智能创新学院系统软件与安全实验室的研究成果《One Email, Many Faces: A Deep Dive into Identity Confusion in Email Aliases》入选网络安全国际顶级会议NDSS 2026（CCF-A类），并荣获杰出论文奖（Distinguished Paper Award）。这是对由邮箱别名机制导致的身份混淆问题的首次系统性分析，深入研究了不同邮箱服务提供商的别名机制，不同平台处理邮箱别名的能力以及邮箱别名在现实场景的滥用攻击。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/bo7mFWCsPicYZSvb6SWvcRuahVTQtG1qT7nVJNOVibHTGxzdmBBhxcBicX9ia5K1icdC8vPFDSUy5bf4QfvXyiccqlWBge4BbsE5h3mQ6e9icxePps/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**01**

**研究背景**

邮箱别名本质上是一种地址转发或代理机制，用户可以根据不同的服务场景使用不同的别名而无需额外设置，所有发往这些别名的邮件最终都会转发到主邮箱。

但是，当邮箱服务提供商、邮箱用户与线上平台对于邮箱别名机制的认知不一致时，便利的邮箱别名机制可能带来相应的安全问题。

**02**

**邮箱别名机制带来的身份混淆**

**（a）邮箱别名多重滥用**

邮箱服务提供商将主邮箱与各种邮箱别名视为同一邮箱，而线上平台由于不了解别名机制，通常将不同的邮箱别名分别视为一个单独的用户。

因此，攻击者可以基于主邮箱alice@a.com衍生出多个别名邮箱地址，在同一平台中注册多个账号，以此实现利用一个邮箱来多次免费试用高级功能、绕过资源限制、或充当水军操纵社交媒体等目的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/bo7mFWCsPicaIfQwAeicib4o3pGDY4o67bmKbDoad9IiciaS1MYHTV46JcEFUy8fwhGkHtngcYILTDkSgHykX1mznU1nZMyykRfsbqdbsZAnKohw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**（b）邮箱别名误认攻击**

不同邮箱服务提供商的别名规则也无法通用，因此即使用户了解别名机制，对别名规则的错误假设会导致别名误认攻击。例如，当用户习惯了加号后缀是常见的别名规则时，攻击者可以在一个不支持加号别名的邮箱提供商处注册邮箱账号（如下图的alice+1@b.com），以此伪装成受害者熟人的别名邮箱，从而诱导受害者点击钓鱼邮件。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/bo7mFWCsPicaFRsh2vDPA60K7losVEc5wW2qGovKtcUzf6ZLh66uVfQjjdVlo1Xyr3gHMViaPMicBRFVdbanDwcJ4VQ5CnPScpwLFIvG5ZFSTQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**03**

**研究贡献**

**本研究取得了以下关键成果：**

1. 首次对邮箱别名机制开展了系统性分析，揭示了邮箱服务提供商、用户与在线平台对于别名机制认知不一致所带来的身份混淆问题。

2. 揭示了28家主流电子邮件服务提供商的别名实现方式差异，发现仅有个别提供商对其别名机制提供了完整的说明文档，而其他服务提供商则缺乏透明度和一致性。

3. 发现了18家顶级在线平台均不能够完全防御所有邮箱别名注册攻击，进一步导致单个邮箱地址即可批量生成用于恶意活动的账号。

4. 证实了缺乏标准化的别名规范会增加普通用户遭到网络钓鱼攻击的风险，且自认为了解邮箱别名机制的用户反倒最容易被骗。

5. 开源了可抵御别名机制身份混淆攻击的工具箱OriginMail。

**04**

**会议介绍**

NDSS是网络安全领域具有重要影响力的国际顶级学术会议，自1993年创办以来已成功举办33届，为中国计算机学会（CCF）推荐的A类会议。本届大会竞争尤为激烈，共收到1481篇有效投稿，最终录用265篇高水平论文，整体录用率仅为17.89%。

**05**

**研究团队**

论文由21级直博生邬梦莹（https://funeoka-yumee.github.io/）为第一作者，洪赓老师（https://security.fudan.edu.cn/members/faculty/hg/）和杨珉老师为通讯作者，并得到了国家自然科学基金和国家重点研发计划项目的支持。这项工作不仅首次系统性剖析了邮箱别名这一广泛存在却未被充分审视的“模糊地带”所潜藏的安全风险，其开源的防御工具箱OriginMail也为平台与服务商提供了切实可行的防护方案，对提升互联网基础服务的身份安全治理水平具有重要价值。

**论文链接**

https://www.ndss-symposium.org/wp-content/uploads/2026-s148-paper.pdf

来源：复旦大学计算与智能创新学院微信公众号

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

信息网络安全杂志

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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