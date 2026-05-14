---
title: GemStuffer滥用150 RubyGems来窃取英国议会门户网站的数据
url: https://mp.weixin.qq.com/s/uTU6QFFuwdnE78iSyrPCqg
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:43:52.609761
---

# GemStuffer滥用150 RubyGems来窃取英国议会门户网站的数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs9b1VZBmbibretgb8mtxvBiavtCINckibgYQJtbYwn1DwjlmRAmYiabQibCG8oeHrlxOia8ZIOUWNm2vCWo1sF06XFWIic3uRibNGib2KOY/0?wx_fmt=jpeg)

# GemStuffer滥用150 RubyGems来窃取英国议会门户网站的数据

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADsibwh2bbVKdrWdHOvF7RStGKB3vCFyLVjwlYELCkpmX4N3yq5ib7bHiacd5VFISysIDaU5jtroBwvl6dZdEAVObBg0sGXoK4jMib1I/640?wx_fmt=jpeg&from=appmsg)

网络安全研究人员呼吁关注一项名为GemStuffer的新活动，该活动针对RubyGems存储库，其中有150多个gems使用注册表作为数据泄露渠道，而不是用于恶意软件分发。

Socket说：“这些软件包似乎不是为大规模开发者妥协而设计的。”许多下载活动很少或根本没有，而且有效负载是重复的、嘈杂的，而且是非常独立的。

相反，脚本从英国地方政府民主服务门户网站获取页面，将收集到的响应打包为有效的。并使用硬编码的API密钥将这些gem发布回RubyGems。

在此之前，RubyGems暂时禁用了新账户注册，原因是受到了严重的恶意攻击。虽然目前还不清楚这两种行为是否有关联，但这家应用安全公司表示，GemStuffer符合“相同的滥用模式”，即使用新创建的带有垃圾名称的软件包来托管收集到的数据。

在较高的层面上，该活动滥用RubyGems作为展示被刮掉的理事会内容的地方。它通过获取硬编码的英国议会门户url，将HTTP响应打包为有效的来实现这一点。并使用嵌入的注册表凭证将这些存档发布到RubyGems。

在某些情况下，gem内嵌入的有效负载会在/tmp下创建一个临时的RubyGems凭据环境，覆盖HOME环境变量，在本地构建一个gem，并使用gem命令行界面（CLI）将其推送到RubyGems，而不是依赖于目标机器上已有的RubyGems凭据。

我们发现恶意gems的其他变种会避开CLI组件，通过HTTP POST请求直接将归档文件上传到RubyGems API。一旦发布了新的gem，攻击者所要做的就是使用gem名称和版本运行gem fetch"命令来访问抓取的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs91vMJK0Dxss1XEkLKlhDQPwunMhNolFibfPkyAbJop6NkglV1AVmc5a995hdlODLD1m60MDH6Jm9icNMDZYlia4nRS7hSgIR2Vgs/640?wx_fmt=jpeg&from=appmsg)

这种新颖的抓取活动被发现是针对Lambeth、Wandsworth和Southwark使用的面向公众的ModernGov门户网站，目的是收集委员会会议日历、议程项目列表、链接的PDF文档、官员联系信息和RSS提要内容。目前还不清楚最终目标是什么，因为这些信息似乎是可以公开获取的。

Socket已经评估，系统地大量收集和存档这些数据，增加了攻击者可能利用“议会门户访问”作为枢纽来展示攻击政府基础设施的能力的可能性。

Socket说：“它可能是注册表垃圾邮件，一个概念验证蠕虫，一个滥用RubyGems作为存储层的自动抓取器，或者一个故意滥用包注册表的测试。”但其机制是有意为之的：重复的gem生成、版本增量、硬编码的RubyGems凭证、直接的注册表推送，以及嵌入包存档中的抓取数据。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

HackSee安全生活

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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