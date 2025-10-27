---
title: 热门Java 框架Quarkus中存在严重的RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514853&idx=1&sn=10d64bdf4f72858d7013dd2cff5fe37e&chksm=ea948b8fdde30299e8387c194b6f4ea7215218284949ef26ba92e2bee711fe42c1b49615e283&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-12-02
fetch_date: 2025-10-04T00:18:05.467183
---

# 热门Java 框架Quarkus中存在严重的RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSXU3yX3JfkwE20YdSXMFEI9P5G6jWJzHNHWF7juBibWTrHQ6hwEsowLEuvrKAOkkNsjM5D7Yb69nQ/0?wx_fmt=jpeg)

# 热门Java 框架Quarkus中存在严重的RCE漏洞

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSXU3yX3JfkwE20YdSXMFEIrIkntER4Tr90Zhj3SLRHO8EwI0rmzhQiavicAGEMsVwk4Jy5d3nPiaf9g/640?wx_fmt=gif)

**Contrast Security 公司的安全研究员 Joseph Beeton 提醒称，热门 Quarkus 框架受严重漏洞（CVE-2022-4116，CVSS评分9.8）影响，可导致远程代码执行后果。**

Quarkus 发布于2019年，是一款开源的 Kubernetes 原生Java 框架，专为 GraalVM 和 HotSpot 虚拟机而设计。该漏洞位于 Dev UI Config 编辑器中，可通过路过式下载本地主机攻击利用。

Beeton 表示，“该漏洞并不难利用，恶意人员无需任何权限即可利用。”由于和本地主机绑定的服务可从外部访问，因此攻击者可创建恶意网站，专门攻击使用易受攻击 Quarkus 版本实例的开发人员。他提到，“如运行 Quarkus 的开发人员本地访问了具有恶意JavaScript 的网站，则该JavaScript 可在开发者机器上悄悄执行代码。”

问题在于，JavaScript 代码可在无需预检的情况下向本地主题发起请求。这些“简单请求”不会像所调用的JavaScript 返回数据，但所需响应时间可用于判断该请求是否成功。Beeton 解释称，“通过这些限制条件，攻击者很有可能访问本地主机，并在一定条件下可触发任意代码执行。”

Beeton 已发布PoC 代码，启动目标机器上的计算器应用，不过他提醒称恶意利用该漏洞可造成更广泛的影响，具体取决于开发人员在密钥、服务器和其它资源上的访问权限，如可在本地机器上安装键击记录器捕获生产系统的登录信息或者使用GitHub 令牌修改源代码等。

Beeton 还指出，攻击者可能针对使用 Quarkus 的开发人员发起鱼叉式钓鱼攻击，诱骗他们点击导致可利用该漏洞的 JavaScript的链接。

本周，Quarkus 表示该漏洞的补丁已包含在 2.14.2.Final 和2.13.5.Final 版本中，提醒称恶意攻击者可利用该漏洞获得对开发工具的本地访问权限，督促开发人员尽快修复。

Red Hat 在一份安全公告中指出，其自建 Quarkus 也受影响，但并未透露何时发布补丁。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Java模板框架 Pebble易受命令注入攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514082&idx=1&sn=e5f47cf95f861ab419805a85f2b77ddb&chksm=ea948688dde30f9e7dab3fe0e015db7f59b41f26ab34b0e762da365423999e608fd0d9a4e9f9&scene=21#wechat_redirect)

[JavaScript 沙箱 vm2修复远程代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514120&idx=3&sn=70433e477638c9c6b3ed925cbdb9cb76&chksm=ea948962dde300745c90d6d6c46d60584f699d5afcb625367d464f79bbbb7bf930be487ee4b9&scene=21#wechat_redirect)

[Java库中充斥着大量反序列化安全弱点](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513642&idx=2&sn=578939f666058f85fd2e4c44e8cb8d46&chksm=ea948740dde30e56322ed889bb709c1b98880d5e843fafb19e3fb1ce4772647aeab3a8e1eae2&scene=21#wechat_redirect)

[谷歌 OAuth客户端库（Java版）中存在高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511856&idx=2&sn=8af051f10bbd30805bce19d5ee116756&chksm=ea949e5adde3174c36f981c8ee950fcc91f0843043f87bf24e5070783d7c9039471df24668cb&scene=21#wechat_redirect)

[年度加密漏洞提前锁定：Java JDK 加密实现漏洞可用于伪造凭据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511475&idx=3&sn=d944ace06613bb0fc7ab6099e251b30e&chksm=ea949cd9dde315cf4a1d48d11a8ef9a7f9d085aa16678adad9cc7ebee49b39f9415ceacb18eb&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/developers-warned-critical-remote-code-execution-flaw-quarkus-java-framework

题图：Pexels License‍

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