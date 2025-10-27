---
title: PyPI 包窃取击键并劫持社交账号
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521893&idx=2&sn=b8ab43380cd434651d9fb5b279b4e78e&chksm=ea94a70fdde32e198c90c0de35896b541eac44bb76ecb18e337212b6da4e8d297a574791cb91&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-26
fetch_date: 2025-10-06T19:38:49.506874
---

# PyPI 包窃取击键并劫持社交账号

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQAziaFIBouMS7MoF4tVTYp7rFkkgiawy96E1eNWMR6tVNKXKPicFcibttCMEIIVxzeyVN9sgV6DeZZDQ/0?wx_fmt=jpeg)

# PyPI 包窃取击键并劫持社交账号

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Fortinet公司的FortiGuard 实验室提到，网络安全研究员发现两个恶意包zebo 和 cometlogger被上传到 PyPI 仓库中，能够从失陷主机中窃取敏感信息。**

这两个恶意包在下架前的下载量分别为118和164次。ClickPy 数据显示，下载主要源自美国、中国、俄罗斯和印度。Zebo 是一款“典型的恶意软件，其功能旨在实施监控、提取数据并实施越权控制”，cometlogger“还表现出恶意行为的迹象，如动态文件操纵、webhook 注入、信息窃取和反病毒机器检查”。

Zebo 使用多种混淆技术如十六进制编码字符串，来隐藏它通过HTTP请求进行通信的C2服务器的URL。它还通过一系列特性收割数据，包括利用pynput 库捕获键击和 ImageGrab，定期每个小时抓取截屏并将其保存到一个本地文件夹，之后通过从C2服务器检索到的API密钥，将其上传到免费的图片托管服务 ImgBB。除了提取敏感数据外，Zebo 还通过创建启动 Python 代码的batch 脚本以及将其添加到 Windows 启动文件夹的方式，来在机器上设立持久性，每次机器重启时，它都会自动执行。

Comtlogger集合了很多特性，会从多款应用如 Discord、Steam、Instagram、X、Tiktok、Reddit、Twitch、Spotify 和 Roblox，嗅探大量信息，如cookie、密码、令牌和与账户相关的数据。它还能够收割系统元数据、网络和WiFi 信息、运行进程清单以及剪贴板内容。此外，它还集成检查以避免在虚拟环境中运行，并终止web浏览器相关的进程以确保不受限制的文件访问权限。研究人员指出，“通过异步执行任务，该脚本将效果最大化，在短时间内窃取了大量数据。虽然某些特性是合法工具的一部分，但缺乏透明度以及可疑的功能使其以不安全的方式执行。应在运行前审查代码并避免与来自未经验证来源的脚本进行交互。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[PyPI攻击：通过 Python 库传播 JarkaStealer](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521578&idx=2&sn=54734e7515c71beca1602a65e343a991&scene=21#wechat_redirect)

[恶意PyPI 包窃取AWS密钥](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521454&idx=2&sn=b633886fd9fb660b4f61e571a43cbad6&scene=21#wechat_redirect)

[“复活劫持”供应链攻击威胁2.2万个PyPI包的安全](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=2&sn=18f9b633ae22eab04a32ea14664dde07&scene=21#wechat_redirect)

[恶意 PyPI 包伪装成答案，滥用StackExchange 进行传播](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520319&idx=2&sn=360f04eb666396afc086ba0444d3574a&scene=21#wechat_redirect)

[恶意PyPI 包针对 macOS，窃取谷歌云凭据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520240&idx=2&sn=549c4734cb750f652f9105a8e5df0546&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/12/researchers-uncover-pypi-packages.html

题图：Pexels License

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