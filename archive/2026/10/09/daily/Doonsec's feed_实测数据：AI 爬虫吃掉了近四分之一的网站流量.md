---
title: 实测数据：AI 爬虫吃掉了近四分之一的网站流量
url: https://mp.weixin.qq.com/s/ZYY1VTQ013e3RnqhCypbsQ
source: Doonsec's feed
date: 2026-10-09
fetch_date: 2026-10-10T07:55:24.808828
---

# 实测数据：AI 爬虫吃掉了近四分之一的网站流量

# 实测数据：AI 爬虫吃掉了近四分之一的网站流量

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

你打开自己的网站后台，会发现大部分访问者不是人。Googlebot、Bingbot这些传统搜索引擎爬虫你早就认识，但现在多了一堆新面孔：GPTBot、ClaudeBot、PerplexityBot、FacebookBot。它们是谁，来做什么，有多少是真的，一份连续30天的实测数据把这些问题摆到了台面上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqna1ickjhbaricepa8iap5jibOpKrqk9Oy1GDIziau8JUvl1tmNf3eFEG2Hf6JpELlM0PGVXmeJT8UJSKb0KnTHjW0zTC3mGXB9zHQ/640?wx_fmt=png&from=appmsg)

这个数据来自一个叫Mojo Dojo的网站，它把服务器日志里所有长得像爬虫的请求都记录下来，按用途分类，还做了一件很多网站没做的事：用IP地址反向验证。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDr8WVY1Jl3ibNBibrkTqWEy7boSmztawic4QH0icgpbxlK4jAlicqiaP624DdsYcibSGRep3ia7g0Dwot4ViaG7E2LqsveXHWJLeiaVUE5ZE/640?wx_fmt=png&from=appmsg)

也就是说，凡是自报家门叫Googlebot或GPTBot的，它都去核对来源IP到底在不在对方公司公布的地址段里。核对不上的，直接剔除。

核心数字过去30天，AI爬虫贡献了23.7%的机器人流量（15,044次访问 / 总计63,500次机器人请求），已经逼近传统搜索引擎的24.9%。平均每来一次搜索引擎抓取，就有0.95次AI抓取。

不是所有爬虫都干同一件事。这个网站把所有访问分成了八类，其中跟AI直接相关的有三类：

AI training（训练数据抓取）：把你的页面搬走，喂给大模型做训练素材。代表是GPTBot、ClaudeBot、Amazonbot、Meta-ExternalAgent。

AI search（AI搜索索引）：为AI问答产品建立索引，比如用户问ChatGPT或Perplexity一个问题时，它们需要知道哪些网页能作为答案来源。代表是OAI-SearchBot、PerplexityBot、Claude-SearchBot。

AI user fetch（实时代读）：某个真人在跟AI助手对话，助手临时去读了你的页面。代表是ChatGPT-User、Claude-User、Perplexity-User。这一类30天里发生了1,060次。

剩下的是大家熟悉的传统角色：搜索引擎（Googlebot、Bingbot等）、SEO工具（AhrefsBot、SemrushBot这些帮你查排名的）、社交预览（FacebookBot、LinkedInBot，链接被分享时抓个缩略图）、网页存档（Internet Archive），以及其他杂项。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDol3Qtq5zmzx7JcNnLMM5xkcLQsDzW8hB4iaEK1CmxXsMNGA55vGLGKUm73JvFKgGxSa0EGZZlrz4iccZq4UqgkVevPcsvqY0JiaM/640?wx_fmt=png)

按用途分类的爬虫流量占比，冒充请求已全部剔除

把每天的爬虫访问量画成堆叠柱状图，能看出一个有意思的现象：大部分日子流量平稳，但在9月底出现了一个尖峰，当天总计9,633次访问。红色部分（AI training）在尖峰那天明显增厚，说明集中抓取训练数据是造成波动的主因。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqSlCF1f7D5fqkoSQcV4SrkxnFLKDibL0tZMuZnQNXxwFEibtQsPZON0RFeLvkFhLuxRItiaT4wRyG1jr8TIJCpXgfakrFmEDoqX8/640?wx_fmt=png)

每日爬虫访问量趋势（已剔除冒充请求），红色为AI训练类爬虫

另一个容易被忽略的数字是6.8%。这是在所有声称自己是爬虫的请求中，来源IP对不上的比例。30天里一共剔除了556个冒充请求。也就是说，你在日志里看到的那些GPTBot或Googlebot，有相当一部分根本不是它们自己来的。

把每个爬虫30天的访问次数排个序，几个关键角色的表现如下：

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDriafs7hQiayGLDicGZqU0dYG4viaYV8HlK60mjlx9PxyvkedcBylDecvovfI2WKIT5VLsUuTCp88ibTSibj2ic0BBtmI9r3EmCc8FtWk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDonYgthlDMV3ezhjnW13yyblUmS6RV7Pvs9R9tR8ClwLPLK7m8ibZqKqtVMuHPzApPzYiaxKkia2RibsOkjfyw6PlPvlyALLgD5tHU/640?wx_fmt=png&from=appmsg)

爬虫排行榜：访问次数、日均量、覆盖页数、验证率

最激进的访问者不是哪个AI公司，而是FacebookBot。30天里来了10,280次，平均每天343次，但它只访问了175个不同页面，平均每个页面被抓了58.7次。这其实是社交预览爬虫的典型行为，你在Facebook上分享一个链接，它就反复去抓预览图和摘要。

AI类里最勤快的是ClaudeBot（Anthropic），3,517次访问，日均117次，覆盖1,641个页面，验证率87%。紧随其后的是Amazonbot（2,878次，88%验证）和Meta-ExternalAgent（2,856次，1,898个页面，AI类里覆盖页面最广）。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqwD3ZR2MDgpQibqFeMwQ0b70F3dxBxv9UC6tXPCrQPz20odhiaP6IcC1G89jhtLPs7u7neLibjk1UDQmoX62kuMv3Ovd2uyJdwog/640?wx_fmt=png)

爬虫排行榜后半部分：GPTBot、ChatGPT-User等AI相关爬虫

最让人意外的是GPTBot。30天里它只来了1,376次（日均46次），但验证率只有8%。换句话说，1,376次自称GPTBot的访问中，只有约110次真正来自OpenAI公布的IP范围，其余46次被明确判定为冒充，剩下的大量请求无法通过验证。对比一下，Googlebot的验证率是97%，Bingbot和PetalBot是100%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDq2ETbUGmwpD5F5PVOuVW4twxJnnxn7cSCtH6ZibY67hLiaHlQjPwDnbZkibrVM91qNTibWZO8TcGuEOq49o8ujsa0SHcGM9u9Dx4Y/640?wx_fmt=png&from=appmsg)

被冒最多的是PerplexityBot，58个假请求被IP验证拦截。Claude-User（53个）、Claude-SearchBot（50个）、CCBot（44个）也都有大量冒充者。这个现象的原因不复杂：很多恶意爬虫、扫描器、竞品工具会在User-Agent里写上知名爬虫的名字来伪装自己，如果你只靠名字判断，就会把它们当真。

它还给这些爬虫颁了几个趣味奖项，顺便把各自的行为特征暴露得更清楚：

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoYMnxy5zVR7H6ZnVOacY8p2U0ictu2hImuuibxhiaDCT2YpWtfFy2y4yvmKicpFKLtx4OibvnJ8E4ZZfSJvicxdojOtFdfdIian7hf4s/640?wx_fmt=png)

30天爬虫行为奖项：最激进、最礼貌、最执念、最彻底

最礼貌的AI爬虫是GPTBot，平均每页只来1.2次，看完就走。对比之下FacebookBot每页来58.7次，属于反复敲门的类型。

最执念的AI爬虫是ChatGPT-User，平均每页3.5次。因为用户在对话中反复追问同一个话题，AI助手就会反复去读那几个页面。

覆盖最广的AI爬虫是Meta-ExternalAgent，30天读了1,898个不同页面，说明Meta在大规模收集网页内容。

最稀客的AI爬虫是Bytespider（字节跳动），30天里只出现了2天，总共32次访问。

黑鸟认为：

第一，AI抓取已经不是边角料了。23.7%对24.9%，AI爬虫和传统搜索引擎的访问量几乎持平。这意味着你的服务器带宽、内容被读取的范围，正在被一类新的角色大规模占用。如果你还在只统计Googlebot的流量，你对网站真实访问结构的认知是不完整的。

第二，名字不可信，IP验证才是硬标准。GPTBot验证率仅8%、PerplexityBot被截了58个假请求，这些数字说明日志里的User-Agent完全可以伪造。网站如果想搞清楚谁真的在访问，必须做反向DNS核对或对照对方公布的IP段。只看名字就放行或封禁，都会误判。

第三，不同AI爬虫的行为模式差别很大。GPTBot来一次就走，ClaudeBot每天稳定抓取，Meta-ExternalAgent覆盖面最广，FacebookBot反复刷同一页。如果你想通过robots.txt控制哪些AI能读你的页面，这些差异决定了你该针对哪些名字设置规则，以及设置之后要观察实际效果。

第四，这个数据来自单一网站，是一个案例研究而不是行业普查。它的流量规模、内容类型、行业属性都会影响具体数字。但它提供了一个难得的视角：当你把日志里的爬虫逐个验证、逐个分类之后，网络流量的真实结构到底长什么样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpp3rHd84QrflNRrf5BlLzydtP0S6zlhlbYn1vhTA237hSDtPmwlAeD1Kpoia2NDtXibYJ18EQXpelEOJo5DoIIIn8iaGzxibwyM7Y/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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