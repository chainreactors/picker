---
title: 【安全圈】PostgreSQL漏洞与BeyondTrust零日漏洞被联合利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067846&idx=2&sn=cd94ea7cada0daf8d439805d2653a055&chksm=f36e7446c419fd50cde0d3757dc46b33e360ae50088fab68c8f1bf59a63968103fa017346904&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-17
fetch_date: 2025-10-06T20:34:56.370904
---

# 【安全圈】PostgreSQL漏洞与BeyondTrust零日漏洞被联合利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaV4SlG5QKQz2ErxKWKzRfDia2IxjX0Bt8hxq7fwyl1picVe7kU68JdibUiag3oTlUAiaIgsfwhyX0nysg/0?wx_fmt=jpeg)

# 【安全圈】PostgreSQL漏洞与BeyondTrust零日漏洞被联合利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

根据 Rapid7 的调查结果，利用 BeyondTrust 特权远程访问（PRA）和远程支持（RS）产品中的零日漏洞（CVE-2024-12356）的攻击者，可能还利用了 PostgreSQL 中一个此前未知的 SQL 注入漏洞。

该漏洞被追踪为 CVE-2025-1094，CVSS 评分为 8.1，影响 PostgreSQL 的交互式工具 psql。安全研究员 Stephen Fewer 表示：“攻击者可以通过 CVE-2025-1094 生成 SQL 注入，然后利用该工具运行元命令的能力，实现任意代码执行（ACE）。”

在对 BeyondTrust 软件中最近修复的安全漏洞 CVE-2024-12356 进行调查时，Rapid7 发现了这一漏洞。该漏洞允许未经身份验证的远程代码执行。具体来说，研究人员发现，成功利用 CVE-2024-12356 的攻击必须包含对 CVE-2025-1094 的利用，才能实现远程代码执行。

在协调披露后，PostgreSQL 的维护者发布了更新，修复了以下版本中的问题：

* PostgreSQL 17（修复于 17.3）
* PostgreSQL 16（修复于 16.7）
* PostgreSQL 15（修复于 15.11）
* PostgreSQL 14（修复于 14.16）
* PostgreSQL 13（修复于 13.19）

该漏洞源于 PostgreSQL 处理无效 UTF-8 字符的方式，从而为攻击者打开了利用快捷命令 `\!` 的途径，该命令允许执行 shell 命令，从而实现 SQL 注入。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaV4SlG5QKQz2ErxKWKzRfDDusyvnAbA5VtZw8ha8WR8tCK3fLAqFfgkiaiaOoosSas1mr8neUEYEXw/640?wx_fmt=jpeg&from=appmsg)

Fewer 表示：“攻击者可以利用 CVE-2025-1094 执行这一元命令，从而控制被执行的操作系统 shell 命令。或者，攻击者可以通过 CVE-2025-1094 生成 SQL 注入，执行任意攻击者控制的 SQL 语句。”

与此同时，美国网络安全和基础设施安全局（CISA）将影响 SimpleHelp 远程支持软件的安全漏洞（CVE-2024-57727，CVSS 评分：7.5）添加到已知被利用漏洞（KEV）目录中，要求联邦机构在 2025 年 3 月 6 日之前应用修复措施。

***END***

阅读推荐

[【安全圈】黄某被策反，春节拜年当间谍](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067835&idx=1&sn=aee79751fcbbef9476521602f8b69b71&scene=21#wechat_redirect)

[【安全圈】英国被曝要求苹果创建“后门” 以检索全球用户云端内容](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067835&idx=2&sn=fec629433dd28f5f6e460233a8642832&scene=21#wechat_redirect)

[【安全圈】OmniGPT 聚合类 AI 平台遭黑客入侵，3400 万条聊天记录遭泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067835&idx=3&sn=5b8555ebfe1ac1a1d356b15389c25486&scene=21#wechat_redirect)

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