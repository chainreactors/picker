---
title: PyPI攻击：通过 Python 库传播 JarkaStealer
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521578&idx=2&sn=54734e7515c71beca1602a65e343a991&chksm=ea94a440dde32d561dfa4703e1dac3a713db2ce5d2a039c7936a177efd7602f8353298c3bf00&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-26
fetch_date: 2025-10-06T19:20:26.933926
---

# PyPI攻击：通过 Python 库传播 JarkaStealer

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQTNyIq9lHg7ReSleicIApiahSH5q7mkJ4icibCfdYyEkNzay3mXYmqtyKI5XBLpkVUiaQTicm9ibUic5qFng/0?wx_fmt=jpeg)

# PyPI攻击：通过 Python 库传播 JarkaStealer

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全研究员发现两个恶意程序包被上传到 PyPI 仓库中，它们模拟热门人工智能 (AI) 模型如 OpenAI ChatGPT 和 Anthropic Claude 传播信息窃取工具 JarkaStealer。**

这些程序包名称为 “gptplus” 和 “claudeai-eng”，由名为 “Xeroline” 的用户在2023年11月上传，分别吸引了1748次和1826次下载量。这两个库目前均无法从 PyPI 中下载。

卡巴斯基发文表示，“一名作者将这些恶意包上传到该仓库，而它们之间的唯一不同之处在于名称和描述。”这些包旨在提供访问 GPT-4 Turbo API 和 Claude AI API，但利用了恶意代码，在安装时就会启动部署恶意软件。具体而言，这些程序包中的 “\_\_init\_\_.py” 文件中包含 Base64 编码的数据，它们集成代码，从 GitHub 仓库 ("github[.]com/imystorage/storage") 中下载一个 Java 文档文件 (“JavaUpdater.jar”)。如果主机上尚未安装 Java，那么它在运行 JAR 文件前还会从一个 Dropbox URL 中下载 Java 运行时环境 (JRE)。

该JAR 文件是一款基于 Java 的信息窃取工具，名为“JarkaStealer”，可从多种应用如 Telegram、Discord 和 Steam 中窃取大量敏感信息如浏览器数据、系统数据、截屏和会话令牌等。

在最后阶段，这些收集的信息被归档，传输到攻击者的服务器，之后从受害者机器删除。JarkaStealer 被指通过 Telegram 频道通过恶意软件即服务 (MaaS) 模型提供，售价为20到50美元不等，尽管其源代码已在 GitHub 上遭泄露。

ClickPy 数据显示，这些数据包主要由位于美国、中国、印度、法国、德国和俄罗斯的用户下载，是以年计的供应链攻击活动的一部分。

卡巴斯基研究员 Leonid Bezvershenko 表示，“这一发现体现了软件供应链攻击的持久风险，并凸显了在将开源组件集成到开发流程中时保持警惕的重要性。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[恶意PyPI 包窃取AWS密钥](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521454&idx=2&sn=b633886fd9fb660b4f61e571a43cbad6&chksm=ea94a5c4dde32cd2e2c06f0f88a616b32a2a6ee31289e30255795b9c3c104fce4af3f04b476b&scene=21#wechat_redirect)

[“复活劫持”供应链攻击威胁2.2万个PyPI包的安全](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=2&sn=18f9b633ae22eab04a32ea14664dde07&chksm=ea94a0c1dde329d773200df4470e2f6dfba305c7c3c4e70dee8ce91ebb53fbf1ea18dd3ea9c1&scene=21#wechat_redirect)

[恶意 PyPI 包伪装成答案，滥用StackExchange 进行传播](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520319&idx=2&sn=360f04eb666396afc086ba0444d3574a&chksm=ea94a155dde32843a4384290c019878dee3a50300c5875932b84d3eab63f5555288c00209369&scene=21#wechat_redirect)

[恶意PyPI 包针对 macOS，窃取谷歌云凭据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520240&idx=2&sn=549c4734cb750f652f9105a8e5df0546&chksm=ea94be9adde3378cb08b546c169a09789a83585332fb65831b5ffee17189c48aba808fc2a92c&scene=21#wechat_redirect)

[PyPI 恶意包假冒合法包，在PNG文件中隐藏后门](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519478&idx=2&sn=4ecf7e9d8f867e65b249517a604a9ca3&chksm=ea94bd9cdde3348a8bd5578938ed713cda546b3b38f95941ded9cbdbeab717010101393d326a&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/11/pypi-attack-chatgpt-claude.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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