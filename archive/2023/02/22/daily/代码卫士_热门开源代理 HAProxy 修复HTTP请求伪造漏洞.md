---
title: 热门开源代理 HAProxy 修复HTTP请求伪造漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515656&idx=2&sn=75097008dc3956ef9f875f11ccec6d4d&chksm=ea948f62dde306749d121190dcb5ebb30950231f44947d0194107e5f848801a0c9dce99f5818&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-02-22
fetch_date: 2025-10-04T07:43:32.939443
---

# 热门开源代理 HAProxy 修复HTTP请求伪造漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQewZ9OBTKBbLmCRHRYok1olQpSAGr4nFluDyqk8fGHecia1jTT1xiacklBbVv5U3l0f6BiaLSlgwG9g/0?wx_fmt=jpeg)

# 热门开源代理 HAProxy 修复HTTP请求伪造漏洞

Ben Dickson

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**热门的开源负载均衡器和反向代理 HAProxy 修复了一个漏洞，可导致攻击者发动HTTP请求走私攻击。攻击者可发送恶意构造的HTTP请求，绕过HAProxy的过滤器并获得对后端服务器的越权访问权限。**

**0****1**

**被释放的标头**

HAProxy 的维护人员Willy Tarreau 指出，“正确构造的HTTP 请求可导致HAProxy 在解析至少是部分处理后释放某些重要的标头字段如 Connection、Content-length、Transfer-Encoding、Host等。”如此可使HAProxy 感到困惑并强制它在无需应用过滤器的情况下将请求发送到后端服务器。

例如，攻击者可绕过HAProxy 对某些URL进行认证检查或使攻击者访问受限资源。该漏洞利用并不难，不过具体影响取决于目标web 服务器以及它对HAProxy过滤器保护资源的依赖程度。Tarreau 指出，“它只要求对HTTP协议的知识以及走私攻击的运作方式有一些了解即可。一般的HTTP猎洞人员会立即了解如何利用该漏洞并将只需要两三次测试，就能证实自己的假设是否正确，这也是为何无需包含太多详情的原因所在。”

**0****2**

**自2019年就存在**

该漏洞是由西北大学、Akamai技术公司和谷歌运行测试并报告的。

Tarreau 表示该漏洞自HAProxy 2.0版本时就存在，而该版本于2019年6月发布。Tarreau 表示，“任何支持客户端上的HTTP/1和支持服务器上的HTTP/1的配置都易受攻击，除非它在已修复版本上运行或者包含我所提出的应变措施。因此基本被暴露的部署是百分之百的。”

在基础设施更深处部署的实例如API网关并不受影响，因为不存在生成此类不合法请求的应用程序或前端代理。Tarreau 一直在积极维护HAProxy的7个版本并为它们发布修复方案。

他指出，“负载均衡器是基础设施中的关键组件，一般来说用户不希望进行升级，除非真的是有必要或者需要新特性。因此我们五年来对每个稳定版本都进行着维护，这样用户能够在必要时验证升级。”

**0****3**

**应变措施**

如果用户无法立即升级至最新版本，则可使用Tarreau 提供的临时的基于配置的应变措施，通过检测利用该漏洞引起的内部条件来阻止攻击。

如果用户正在运行老旧的HAProxy 版本，Tarreau 提醒称，“最佳的临时选择就是立即升级至下一个分支，该分支的变动最小。请不要试图升级过时版本。如果你在五年内都没有考虑更新，那么任何人都不会考虑帮你追赶。”

该漏洞并非影响HAProxy的首个严重的HTTP请求走私漏洞，2021年9月该平台就被之存在类似问题。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[开源的代理服务器HAProxy 易遭严重的 HTTP 请求走私攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507788&idx=3&sn=57a31cb649788c04a8f3cedc547d8e8c&chksm=ea94ee26dde36730ac46f670d5524d800229b30c8e50c5afd1310a1bc7e43a7d3fefe6e25921&scene=21#wechat_redirect)

[思科开源杀软ClamAV中存在严重的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515647&idx=2&sn=704411c89c34c85e52e2ad18ff0fb77c&chksm=ea948c95dde305838410d09bd123fd529f7be43231802fc228e4300929816f4adb5d4f72007e&scene=21#wechat_redirect)

[热门开源Dompdf PHP 库中存在严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515460&idx=2&sn=6ff90ed5a1a5cfe857a4aa75a16def08&chksm=ea948c2edde305386563b822262353daa67aecbbe719fdcbf7b97f402220ee247091ea7aeac0&scene=21#wechat_redirect)

[热门开源库 JsonWebToken 存在RCE漏洞，可引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515233&idx=1&sn=1e9a33dc52094b1fa20a75a16e81d1af&chksm=ea948d0bdde3041d97220eab3c1615d2e8e9d7bf783d606a1571bea4c078d16aed093074a0d6&scene=21#wechat_redirect)

**原文链接**

https://portswigger.net/daily-swig/http-request-smuggling-bug-patched-in-haproxy

题图：Pixabay License

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