---
title: ChatGPT+RASP，实现CodeQL漏洞挖掘高效自动化 | 2023INSECWORLD
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247517975&idx=1&sn=dfabd6d89dc49fb318615a303ee628ca&chksm=ce460c07f93185111732a39687ea8631014d6b3a622bda235e9ae816d70f645ab615537ed444&scene=58&subscene=0#rd
source: 深信服千里目安全技术中心
date: 2023-03-24
fetch_date: 2025-10-04T10:30:16.967850
---

# ChatGPT+RASP，实现CodeQL漏洞挖掘高效自动化 | 2023INSECWORLD

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5xySGzFVFtNswpdtIXicA4TXru1AgCzFoMnOpib2JC8cmzdicmASsDnCP3iaicudibziaMJUuIiblEbBshQrg/0?wx_fmt=jpeg)

# ChatGPT+RASP，实现CodeQL漏洞挖掘高效自动化 | 2023INSECWORLD

智安全

深信服千里目安全技术中心

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5zFObpGGvbWzxnyX6UtTRfibHlJCvfKQGPIDhYFImibr1SvBqtkm7KjzZsHVdzmOMBrQuKeYghpKOHA/640?wx_fmt=gif)

*传统用CodeQL进行漏洞挖掘，生成的结果误报较多，影响效率；那么，如果融入ChatGPT和RASP呢？*

3月21日，由Informa Markets主办的**2023 INSEC WORLD 世界信息安全大会**以“聚焦安全 打造多元新格局“为主题，在西安国际会展中心会议楼拉开帷幕。作为一次汇聚各界意见领袖和技术专家的行业开年盛会，大会邀请到逾50位海内外优秀行业大咖分享安全实践经验及最新技术。

**深信服创新研究院安全技术专家高勇杰**受邀在**「漏洞与攻防安全」分论坛**中进行演讲，分享议题为**《CodeQL漏洞挖掘之旅》**。议题详细讲解CodeQL使用思路，以及一个区别于主流使用的利用CodeQL进行半自动化挖掘漏洞的方式。结合当下热门的chatGPT工具，分享了在CodeQL的使用和工作方式的新感悟，可以有效提升漏洞挖掘效率。

![](https://mmbiz.qpic.cn/mmbiz_jpg/EJiaEo3Lq9kquBMshYOrH1zlsAmB0HN6jBtHWsvqmxPQP4saQZicXVic2YrOK27iayrQ2KT2ZAVDA0v7j4HTZSgxUQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/EJiaEo3Lq9kpMIvT6fu0XntZ3goyJllkOH2xuxksC92myRzSn7O0b22kZnd1fF9z5DC8QFG7CTeIW0ibVJOiaX86w/640?wx_fmt=gif)

**区别于主流使用CodeQL的漏洞挖掘方式**

在演讲中，高勇杰使用SecExample开源靶场进行实际案例的演示，讲解不将CodeQL作为扫描工具使用，而是利用CodeQL的分析能力，协助进行代码审计，尽可能地减少在代码审计时的工作量。

![](https://mmbiz.qpic.cn/mmbiz_jpg/EJiaEo3Lq9kpMIvT6fu0XntZ3goyJllkOTRynF8ibXZPe8otq2wBptWbzGzKBYzjaicvhFY2zo9sa54ia4lSzWLK7w/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/EJiaEo3Lq9kpMIvT6fu0XntZ3goyJllkOgZuiaicjA1pwAxIwjtHtNKFpIzGCpslJPF4UU1kxzy7qUiaXXzJ39VhNA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/EJiaEo3Lq9kpMIvT6fu0XntZ3goyJllkOH2xuxksC92myRzSn7O0b22kZnd1fF9z5DC8QFG7CTeIW0ibVJOiaX86w/640?wx_fmt=gif)

**CodeQL+ChatGPT+RASP，实现高效自动化**

高勇杰总结道，CodeQL目前还存在着一些缺陷，例如QL规则需要不断迭代、扫描结果存在误报等等，仅使用CodeQL也无法完成完整的代码审计流程闭环等问题。

针对以上问题，高勇杰也分享了一套借助ChatGPT与RASP技术的全自动化漏洞挖掘方式，不仅可解决QL规则的迭代、扫描规则误报问题，且完成了代码审计流程的闭环。

CodeQL做初步审计，提取关键代码块后交由ChatGPT验证，并基于RASP技术避免了POC生成不稳定对结果的影响，使结果更加稳定、可靠。最终实现高效、精准的漏洞挖掘。

![](https://mmbiz.qpic.cn/mmbiz_jpg/EJiaEo3Lq9kpMIvT6fu0XntZ3goyJllkOMXvNDPjqsYGylnT1Ur32XA8aQtoZbQMPe6MaXNbm6DWV0Rgicp0sMxw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/EJiaEo3Lq9kpMIvT6fu0XntZ3goyJllkONjrPzDNRnqIF7Wia1dFpPglzeNVlpSWdw1ic7qzYXfVejIQ03YKk3f9Q/640?wx_fmt=gif)

深信服千里目安全技术中心-创新研究院一直致力于安全和云计算领域的核心技术前沿研究，推动技术创新变革与落地，拥有安全和云计算领域500+ 专利，实现攻击和检测技术的相互赋能，并及时把能力输入到业务线中，实现自身产品的迭代优化。未来，深信服千里目安全技术中心也将不断提高专业技术造诣，深度洞察网络安全威胁，持续为网络安全赋能。

![](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5zFObpGGvbWzxnyX6UtTRfibFXicTzaYOdfAp1NDOmZN6qj1Ib5bMRxNDYTBZTIwzD8DPrs7kS9sPrQ/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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