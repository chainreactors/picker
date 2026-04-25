---
title: AI编程默认不安全：知名AI公司发生重大数据泄露
url: https://mp.weixin.qq.com/s/mYrHecDqNAdMdnsUWDnX9Q
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:30:59.142933
---

# AI编程默认不安全：知名AI公司发生重大数据泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88VJlrvTprspSRUy90wWuMgd3wJInM2b8QoXNRZXlegT1q1wrny3UtJeU8KCmFr7Yiccb8l5b2WSMVB2ArmicYjTutX06Nw7ticAC4/0?wx_fmt=jpeg)

# AI编程默认不安全：知名AI公司发生重大数据泄露

e安在线
e安在线

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88WBJohrQceicibeoUGoicm8PfiaXicDkvMnhUQ0Dg3uaibcJXWj9Tm0EibRTk4atcuobOyp64THK5PHD2mQpeOApo4ePuKefcxAiauCLIw/640?wx_fmt=gif&from=appmsg)

Lovable、Vercel、Anthropic等多家知名AI公司近期均发生重大影响的数据泄露事件，前两家涉及大规模暴露/泄露用户数据，后者则是将明星产品的源代码公开暴露；

上述几起事件的原因不一，有默认设计暴露所有用户数据，有员工权限遭供应链投毒劫持，还有员工操作不当等。

4月23日消息，国际知名AI编程工具Lovable近期发生的安全问题，为专业软件工程师提供了又一个对氛围编程保持警惕的理由。

周一，X用户Impulsive点名Lovable，称这家瑞典AI编程初创公司发生了大规模数据泄露，“影响了2025年11月之前创建的每一个项目”。

该用户表示，仅通过自己的免费Lovable账号，就能够访问另一名用户的代码、AI聊天记录以及客户数据。

该用户称：“英伟达、微软、优步和Spotify的员工都有账号。这个漏洞在48天前就已被报告，但至今仍未修复。他们将其标记为重复问题，并一直未予处理。”

01

Lovable承认权限设置不当，暴露所有用户聊天和构建内容

对此，Lovable否认发生了数据泄露，并表示用户可以查看公共项目代码，是其有意为之的设计决策。

然而，这一声明在X上引发了争议。由于表述不够清晰，以及用户不清楚未来应如何保护自身数据，Lovable随后发布了第二份声明。

公司解释称，允许他人查看“公共”项目，是“为了方便用户探索他人正在构建的内容”。同时补充，自去年12月起，所有订阅层级已默认关闭公共可见性。

在第二份声明中，Lovable也承认了最初X帖子所指出的安全问题。

Lovable写道：“不幸的是，在2月我们对后端权限进行统一时，意外重新启用了对公共项目聊天内容的访问权限。一经发现该问题，我们立即回滚更改，使所有公共项目的聊天再次恢复为私密。我们感谢发现这一问题的研究人员。”

02

AI编程产品没有在设计时就嵌入安全

部分用户对Lovable的透明度表示赞赏，但也有用户认为，公司最初的声明是在推卸责任。

安全公司Hacker Minded创始人Tom Van de Wiele表示，这一事件“再次说明，在缺乏安全默认设置的情况下，又未能针对自动化与AI时代进行威胁建模，问题终将暴露”。

他补充称，让用户自行判断哪些内容是公开的、哪些不是，“最终往往会失败”。

ESET全球网络安全顾问Jake Moore表示，围绕该事件是否构成数据泄露的争论，可能掩盖了更深层的问题。

他在接受采访时说：“这并不属于传统意义上的数据泄露，但也绝非无关紧要。从本质上看，这更像是设计缺陷，因为数据是被暴露出来的，而非通过黑客入侵获取。”

他进一步指出：“当一家公司纠结于语义而非实际影响时，往往意味着安全并未从一开始就被纳入设计之中，这正是导致此次事件的现实原因。”

03

易用和安全是一次权衡取舍

总体来看，专业开发人员并不鼓励过度依赖AI，因为其可能生成混乱且未经充分测试的代码。他们认为，氛围编程还会带来信息安全方面的隐患，包括公司数据被意外暴露。

Van de Wiele表示，开发此类工具的公司通常面临取舍，需要在提升易用性与确保安全之间找到平衡，但这并不能成为防护不足的理由。

他说：“公司往往处于两难境地，一方面希望降低新用户的使用门槛，另一方面又要防范数据抓取者。”他补充称，对于可能被抓取并转售数据的用户来说，这确实会带来现实影响。

Moore表示，如果用户未能充分理解哪些内容会被暴露，氛围编程工具可能进一步放大这些风险。

他说：“氛围编程正在不断加速不良默认设置的传播，用户必须对此保持清醒认识，并建立必要的故障保护与备份机制。”

他认为，这种趋势可能使类似事件变得更加频繁。

Moore表示：“如果用户因AI编程工具的默认设置而意外暴露敏感数据，攻击者甚至无需发起任何黑客攻击。”

04

接连发生数据安全事件

在Lovable出错前的几周内，AI领域已接连发生两起重大数据泄露事件。

3月下旬，Anthropic错误泄露了一个包含近2000个文件和50万行代码的档案。当时Anthropic表示，“未涉及或暴露任何敏感客户数据或凭证”。

本周早些时候，网站托管平台Vercel表示，其发现一起安全事件，导致未授权用户能够访问部分内部系统。

Vercel称，该事件源于其员工使用的第三方工具Context.ai被攻破。攻击者借此接管了该员工的谷歌Workspace账号，从而进一步获得了对部分Vercel环境的访问权限。

Vercel在周一发布声明称：“我们正在积极调查此事，并已聘请事件响应专家协助调查与修复。我们已通知执法部门，并将在调查推进过程中持续更新相关信息。”

在2月的一期播客中，Andreessen Horowitz普通合伙人Anish Acharya表示，公司不应在业务的每个环节都使用AI辅助编程，因为相关风险并不值得承担。他同时指出，依赖AI编写代码本身就存在潜在风险。

参考资料：businessinsider.com

来源：安全内参

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88UR6icztiaMDcvGBs077WN4FIDNT7bJkZ4NKH5o7uRIGIzibFZa2mq1qXCzmtBEz8ICcicPia9n64FMynVib4bjvbnZCppHQ1Z5TpIkQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537006&idx=1&sn=47b4fd64c51fd886882eba9f2755bd0a&scene=21#wechat_redirect)

[安测促发展，积聚创未来——2026网络通信安全融合生态创新发展大会在宁举行](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537006&idx=1&sn=47b4fd64c51fd886882eba9f2755bd0a&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88WjwEF932bqbsMPq0DTA9D2YkakBfmTLKazcj1TV2FCpaSMerCv4bCfffibN5lN92u3woYmLXauY5iazscibMiaXvuVD6xxNSGszGM/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537051&idx=1&sn=cd6f6b480f3b1cafb714df95f3132ae1&scene=21#wechat_redirect)

[征集标准参编单位！关于征集《消费级无人机检验检测通用要求》认证认可行业标准参编单位的通知](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537051&idx=1&sn=cd6f6b480f3b1cafb714df95f3132ae1&scene=21#wechat_redirect)

****热点聚焦****

****HOT！！****

**[邬江兴院士：AI内生安全问题及可信应用系统研究](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247524079&idx=1&sn=f4e4c0da54b241108c7940047ee1be77&scene=21#wechat_redirect)**

**[征稿启事 | 16个热点问题，欢迎来稿！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247521812&idx=1&sn=df8ac4f4f7071445227e454703cf3eac&scene=21&token=891324421&lang=zh_CN#wechat_redirect)**

**[新书出版 | 邬江兴院士发布最新英文著作](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247525711&idx=1&sn=7c47de2a92853e19af33b0c0ff76063e&scene=21#wechat_redirect)**

**[可信内生安全、变结构拟态计算技术等入选“新一代信息工程科技新质生产力技术备选清单（2024）”](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247524134&idx=1&sn=e8f83445d7ea448a8ea38a06e228f77c&scene=21#wechat_redirect)**

**[持续赋能内生安全！第五届网络空间内生安全学术大会暨第八届“强网”拟态防御国际精英挑战赛完美收官](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534994&idx=1&sn=a35dc208810295861b94d6af88c2c7e8&scene=21#wechat_redirect)**

[蓝皮书下载 | 第五届网络空间内生安全学术大会，四本蓝皮书重磅发布](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535240&idx=2&sn=da33dc8d3ad64e3c161538e0d3a14494&scene=21#wechat_redirect)

**[正式发布！网络空间内生安全理论和标准体系入选信息通信领域十大科技进展（附手册）](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247527344&idx=1&sn=b9f70ff5f052f6866645a8bc506f43bd&scene=21#wechat_redirect)**

**[递交2025网信生态高质量发展“开年答卷”  网络通信安全融合生态创新发展大会在宁举行](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247528656&idx=1&sn=28c73aa522cb86038989efae1f2c8ee2&scene=21#wechat_redirect)**

**[邬江兴院士为五色石先导班学生授课](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247530005&idx=1&sn=ae066476dfc29be0b0d528a64e6b6679&scene=21&token=891324421&lang=zh_CN#wechat_redirect)**

**[邬江兴院士——AI时代内生安全自主知识体系建设的思考](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534787&idx=1&sn=3e2e3df01300637de00f028894fd6493&scene=21#wechat_redirect)**

**[出版啦！南京市网络空间内生安全协会5项团体标准在中国标准出版社正式出版](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534684&idx=1&sn=1814c0aed65128d0e345064e5b7b83d1&scene=21#wechat_redirect)**

**[邬江兴院士 | 破击美欧网络弹性铁幕——基于自主知识技术体系的数字生态系统底层驱动范式变革](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247533711&idx=1&sn=7a843b5f85bfce11554c51cb97c5e1f0&scene=21#wechat_redirect)**

**[喜报！南京市网络空间内生安全协会获评为AAAA等级社会组织！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535467&idx=1&sn=343185d42eca10a491337f0111035b24&scene=21#wechat_redirect)**

**[邬江兴院士提出“时空协同复杂度”理论——揭秘介观尺度智能涌现机理引领AI架构革新](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247535842&idx=1&sn=bf905ee97eb951d993e28c518e8adf67&scene=21#wechat_redirect)**

**[南京市网络空间内生安全协会第二届会员大会暨换届选举大会圆满举行](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247536554&idx=1&sn=e7d5d716f55a62c9f64360c2a527d45d&scene=21&token=891324421&lang=zh_CN#wechat_redirect)**

****| 往期回顾****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[邬江兴院士：人工智能内生安全质量检测中试平台](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247536446&idx=1&sn=0ede0c81fb0d67df45be75a62e84b87b&scene=21#wechat_redirect)**

[《科技日报》整版访谈邬江兴院士：将“安全基因”植入人工智能系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537206&idx=1&sn=2ce618202d759560ecee6aeca93b8c24&scene=21#wechat_redirect)

[一图看懂“十五五”规划10大核心方向（附产业全景图）](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537406&idx=1&sn=38bf0cf38e71042a6956fc39a1e59f38&scene=21#wechat_redirect)

[2026年第一季度全球网络攻击事件盘点](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537413&idx=1&sn=6c43d3a245aa489bbd59c117b3df4888&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/jRRfTC292pXGqHBACsK1cVtpyTB5F8VFsEY3paWnfS3dichupP4OknoSrNN3c6YviaDsLwKnfHwj1OibB7lWFvbibQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pX7QK5QfSb6k3uQJ3EsDmeCnsG6veyEXTXsbCcuuTJ7LWzo0tPv2ezibrAF07JXGxYs8zSXgXibLX2Q/0?wx_fmt=png)

内生安全联盟

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pX7QK5QfSb6k3uQJ3EsDmeCnsG6veyEXTXsbCcuuTJ7LWzo0tPv2ezibrAF07JXGxYs8zSXgXibLX2Q/0?wx_fmt=png)

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