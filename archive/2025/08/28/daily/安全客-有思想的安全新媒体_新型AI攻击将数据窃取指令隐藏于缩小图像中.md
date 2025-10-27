---
title: 新型AI攻击将数据窃取指令隐藏于缩小图像中
url: https://www.anquanke.com/post/id/311537
source: 安全客-有思想的安全新媒体
date: 2025-08-28
fetch_date: 2025-10-07T00:18:26.997125
---

# 新型AI攻击将数据窃取指令隐藏于缩小图像中

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 新型AI攻击将数据窃取指令隐藏于缩小图像中

阅读量**65258**

发布时间 : 2025-08-27 17:47:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/new-ai-attack-hides-data-theft-prompts-in-downscaled-images/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

研究人员开发了一种新型攻击，通过在AI系统处理的图片中注入恶意提示，从而盗取用户数据。这种方法依赖于全分辨率的图片，这些图片在经降质处理后，肉眼无法察觉其中的指令，但当图像质量因重新采样算法而降低时，隐藏的内容便会显现出来。

这一攻击方法由Trail of Bits的研究员Kikimora Morozova和Suha Sabi Hussain开发，基于2020年USENIX会议上德国布伦瑞克大学提出的一项理论，该理论探讨了图像缩放攻击在机器学习中的可能性。

![]()

## 攻击原理

当用户将图像上传至AI系统时，系统通常会自动将图像降质以提高性能和降低成本。

根据系统不同，图像的重新采样算法可能会采用最近邻插值、双线性插值或双三次插值等方法。

这些方法会引入混叠伪影，从而使经过特殊设计的图像中的隐藏模式在降质图像中显现出来。

在Trail of Bits的示例中，恶意图像的特定暗区在使用双三次插值降质处理时会变成红色，从而使隐藏的黑色文字显现出来。

![]()

## 降质图像中隐藏的消息示例

AI模型将这些文字解读为用户的指令，并自动将其与合法输入结合。

从用户的角度来看，似乎没有任何异常，但实际上，模型已经执行了隐藏的指令，可能导致数据泄露或其他风险行为。

在一个涉及Gemini CLI的示例中，研究人员成功地将Google日历数据泄露到任意邮箱，同时使用Zapier MCP中的“trust=True”自动批准工具调用，而无需用户确认。

Trail of Bits表示，这一攻击方法需要根据每个AI模型使用的降质算法进行调整，但研究人员已确认该方法在以下AI系统中是可行的：

1. Google Gemini CLI；

2. Vertex AI Studio（使用Gemini后台）；

3 .Gemini的网页界面；

4. Gemini API通过llm CLI；

5. Android手机上的Google Assistant；

6. Genspark。

由于这一攻击向量广泛，可能会超出已测试工具的范围。此外，为了验证这一发现，研究人员还创建并发布了Anamorpher（目前处于beta阶段），这是一款可以根据上述降质方法生成图像的开源工具。

研究人员指出，作为缓解和防御措施，AI系统在用户上传图像时应实施尺寸限制。如果需要降质处理，建议向用户提供处理结果的预览，确保他们了解将传输给大语言模型（LLM）的图像内容。

他们还建议，针对敏感的工具调用，尤其是当图像中检测到文字时，应该寻求用户的明确确认。

然而，研究人员强调，最强的防御措施是实施安全的设计模式和系统化的防御机制，减少多模态提示注入攻击的影响，这也是他们在6月发布的一篇论文中提到的，旨在帮助构建能够抵御提示注入攻击的大型语言模型的设计模式。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/new-ai-attack-hides-data-theft-prompts-in-downscaled-images/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311537](/post/id/311537)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/new-ai-attack-hides-data-theft-prompts-in-downscaled-images/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/new-ai-attack-hides-data-theft-prompts-in-downscaled-images/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [攻击原理](#h2-0)
* [降质图像中隐藏的消息示例](#h2-1)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)