---
title: 已存在13年的Apache ActiveMQ 严重漏洞可用于远程执行命令
url: https://mp.weixin.qq.com/s/AXG9IXCFNtX7C7lMrS4YIg
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:43:16.400296
---

# 已存在13年的Apache ActiveMQ 严重漏洞可用于远程执行命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfUdaQc6JcJe4papxQRoelnMBytibE8F8wSZEe17OAWjThYX0ltevTY2suLianicxgsuQK1fWPyl9JZShjO6RyJibl5OTDBvFtEicBlM/0?wx_fmt=jpeg)

# 已存在13年的Apache ActiveMQ 严重漏洞可用于远程执行命令

Bill Toulas
Bill Toulas

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**安全研究人员利用 Claude AI 助手，从 Apache ActiveMQ Classic 中发现了一个远程代码执行 (RCE) 漏洞CVE-2026-34197（CVSS评分8.8）。该漏洞已存在13年之久，可用于执行任意命令。该漏洞影响 Apache ActiveMQ/Broker 5.19.4之前以及从6.0.0到6.2.3的所有版本。**

Apache ActiveMQ 是一个用 Java 编写的开源消息中间件，通过消息队列或主题来实现异步通信。尽管 ActiveMQ 已推出性能更优的新版 Artemis 分支，但受该漏洞影响的 Classic 版本仍广泛部署于各类基于 Java 构建的企业系统、Web 后端以及政府、公司内部系统中。

Horizon3 公司的研究员 Naveen Sunkavally 表示，他“仅通过几次基础提示词”就借助 Claude 发现了这个问题，“这个成果八成归功于 Claude，剩下两成是人工包装润色。”Sunkavally 指出，Claude 在逐一分析了多个独立组件（Jolokia、JMX、网络连接器以及 VM 传输协议）后，很快就定位到了该漏洞。他提到，“每个功能单独来看都符合预期，但把它们组合在一起就产生了危险。这正是 Claude 大显身手的地方——它能毫无预设偏见且思路清晰地将这条攻击路径从头到尾串联起来。”该研究员于 3 月 22 日向 Apache 维护人员报告了这一漏洞，后者在 3 月 30 日发布的ActiveMQ Classic 6.2.3 和 5.19.4 版本中修复了该漏洞。

Horizon3 发布技术报告指出，该漏洞的根源在于 ActiveMQ 的 Jolokia 管理 API 暴露了函数addNetworkConnector，可滥用于加载外部配置。攻击者可通过发送精心构造的请求，强制消息代理拉取一个远程 Spring XML 文件，并在初始化过程中执行任意系统命令。

触发该漏洞通常需要经过 Jolokia 的身份认证，但由于另一个漏洞 CVE-2024-32114（该漏洞导致 API 在没有访问控制的情况下被暴露）的存在， 6.0.0 至 6.1.1 版本无需进行认证。

研究人员指出，最新披露的漏洞风险不容小觑，并援引了其他已被黑客用于真实攻击的 ActiveMQ 高危漏洞。研究人员提到，“我们建议所有运行 ActiveMQ 的组织机构优先处理该漏洞，因为 ActiveMQ 一直是真实攻击场景中被反复利用的目标，而且针对它的利用及后渗透方法已经相当成熟。无论是影响 Web 控制台的认证 RCE 漏洞 CVE-2016-3088，还是影响 Broker 端口的未认证 RCE 漏洞 CVE-2023-46604，均已被列入美国 CISA 的已知遭利用漏洞目录（KEV）。”

尽管目前尚未有报告显示 CVE-2026-34197 已遭积极利用，但研究人员指出，已在 ActiveMQ Broker 的日志中清晰看到漏洞利用迹象。建议排查使用内部传输协议 VM 的可疑 Broker 连接，以及包含 “brokerConfig=xbean:http://”查询参数的请求。命令执行会在多次连接尝试过程中触发。研究人员表示，如果系统出现了关于配置问题的警告信息，则意味着恶意载荷已经被执行。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Apache Syncope 漏洞可用于劫持用户会话](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525048&idx=2&sn=58b797888d5027994282725ccb9f23de&scene=21#wechat_redirect)

[Apache Struts 2 严重 XXE 漏洞可用于窃取敏感数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524857&idx=1&sn=7d98b989a61c9b25103ccef5b0524560&scene=21#wechat_redirect)

[Apache StreamPipes 严重漏洞可用于获取管理员权限](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524778&idx=2&sn=17e6675d731950fb6f61f841bb161ef5&scene=21#wechat_redirect)

[速修复！Apache Tika 中存在严重的满分XXE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524600&idx=1&sn=fe09ca1df38ec9061341a2100567e69b&scene=21#wechat_redirect)

[Apache Tomcat 漏洞导致服务器易受RCE攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524305&idx=2&sn=151df83a78bc5a9f5351bf4c295a1d03&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/13-year-old-bug-in-activemq-lets-hackers-remotely-execute-commands/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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