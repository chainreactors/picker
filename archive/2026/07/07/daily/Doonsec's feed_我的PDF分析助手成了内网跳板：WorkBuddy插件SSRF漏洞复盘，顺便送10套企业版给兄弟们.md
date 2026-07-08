---
title: 我的PDF分析助手成了内网跳板：WorkBuddy插件SSRF漏洞复盘，顺便送10套企业版给兄弟们
url: https://mp.weixin.qq.com/s/jPnioOdeII6xTJkpkXwImQ
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T04:59:40.173166
---

# 我的PDF分析助手成了内网跳板：WorkBuddy插件SSRF漏洞复盘，顺便送10套企业版给兄弟们

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3oR6eMARh6yaXrjKqdfgLYpROIKr48ehZSKRPdf3ljA9EEy1F7vVxNWicgHxrSiaDjQqo5yJEe9PN3hGUQZzVzDnI81z1YtkGGicDI179SIltk/0?wx_fmt=jpeg)

# 我的PDF分析助手成了内网跳板：WorkBuddy插件SSRF漏洞复盘，顺便送10套企业版给兄弟们

原创

逍遥
逍遥

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

上个月我在WorkBuddy上装了个“AI PDF分析”的Skill，本意是想让它帮我自动审合同、提取关键条款。结果这玩意儿差点把我的云服务给搞穿——它有个“URL抓取”功能，本意是分析PDF里引用的链接是否安全，结果被我用一条简单的请求直接打穿，拿到了我云服务器的元数据凭证。

还好这只是在测试环境搞的，但也足够让我背后一凉。今天把这个漏洞从头到尾复盘一遍，顺便讲讲WorkBuddy企业版是怎么帮我们防住这类风险的。文末还有福利：抽10套WorkBuddy企业版送给做AIOPC的兄弟们。

**一、发现：一个“贴心”的URL抓取功能**

这个PDF分析Skill在WorkBuddy的生态里下载量不小，主要功能是扫描PDF文档，自动提取里面的法律条款、金额、日期，还能分析文档中嵌入的链接是否指向恶意网站。

它的工作流程是：用户上传PDF → Skill解析出文本中的URL → 服务器去请求这些URL → 返回页面标题和风险评分。就是这个“服务器去请求URL”的功能，埋下了SSRF的雷。

我故意构造了一个恶意的PDF文件，里面插入了一行文字：“参考链接：http://169.254.169.254/latest/meta-data/”。然后上传给这个Skill进行分析。

几分钟后，分析结果出来了。在“链接安全评估”一栏，赫然显示着：

```
URL: http://169.254.169.254/latest/meta-data/标题: iam/security-credentials/安全评分: 未知
```

它成功访问了AWS的元数据服务，还返回了目录结构！

**二、深入利用：从元数据到云凭证**

有了第一步，后面就顺理成章了。我不断修改PDF里的链接，依次请求：

* `http://169.254.169.254/latest/meta-data/iam/security-credentials/` —— 返回了角色名。
* `http://169.254.169.254/latest/meta-data/iam/security-credentials/my-role` —— 返回了完整的AccessKeyId、SecretAccessKey、Token。

整个过程，Skill没有做任何过滤。它就像一个忠实的HTTP客户端，帮我从内网的元数据端点拿回了最敏感的云凭证。

拿到这些凭证后，我试着在本机配置了一下AWS CLI，直接`aws s3 ls`，看到了我测试账号下的所有S3存储桶。如果这是生产环境，攻击者已经可以随意读取、篡改、删除所有云上的数据。

**三、漏洞根因：AI应用的通病**

这个Skill的问题很典型，几乎所有带URL抓取功能的AI应用都可能犯：

1. **未校验目标地址**。对于用户传入的URL，没有做任何过滤，直接发起请求。黑名单式的拦截（比如只封禁169.254.169.254）很容易被绕过，比如换成十进制IP、IPv6、DNS重绑定。
2. **内网权限过大**。服务器所在的云主机绑定了过高的IAM角色，并且没有限制元数据服务的访问（如IMDSv2）。
3. **缺乏网络隔离**。AI Skill运行环境与云基础设施核心网络没有隔离，SSRF一穿到底。

有趣的是，这个Skill的开发者在收到我的报告后，很快做了修复：加入了URL白名单，只允许访问外网80/443端口的HTTP/HTTPS链接，并且禁用了对内网IP、元数据地址的访问。WorkBuddy官方也因为这个案例，在企业版里强化了Skill运行时的沙箱机制。

**四、WorkBuddy企业版如何从架构上防范SSRF？**

这个漏洞虽然是在第三方Skill里发现的，但它暴露的问题却是平台级的。WorkBuddy企业版针对这类风险，提供了一套完整的解决方案：

**1. Skill运行沙箱（Sandbox）**
企业版允许管理员对每个Skill设置网络策略，比如：

* 禁止访问内网IP段（10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16）
* 禁止访问云元数据服务（169.254.169.254）
* 只允许白名单域名/端口的出站连接

这样即使某个Skill存在SSRF漏洞，攻击者也打不到内网。

**2. 多租户数据隔离**
企业版的多租户工作区，保证了不同业务、不同客户的文档、凭证、配置完全隔离。就算一个Skill沦陷，攻击者也无法横向移动到其他租户的数据。

**3. 最小权限原则**
企业版在部署时可以配置云主机的IAM角色权限，不会赋予AI应用过高的权限。同时强制要求使用IMDSv2，防止元数据被直接请求。

**4. 审计日志与实时告警**
企业版记录所有Skill的网络请求日志，管理员可以设置规则：一旦检测到对内网地址的请求，立即触发告警并暂停Skill。这在漏洞初期就能阻断攻击。

**五、给AI应用开发者和使用者的建议**

如果你是开发者：

* 永远不要信任用户提供的任何URL。
* 使用白名单机制，只允许访问特定的外部域名。
* 不要在服务端代码或系统提示词中存放云凭证、数据库密码等敏感信息。
* 将AI服务与核心业务网络隔离，部署在独立的VPC中。

如果你是使用者（特别是企业）：

* 优先使用有沙箱机制的平台（如WorkBuddy企业版）。
* 定期审查已安装Skill的权限和网络行为。
* 为云主机配置最小权限的IAM角色，并启用IMDSv2。
* 监控异常的网络请求，如对169.254.169.254的访问。

**六、抽奖：送10套WorkBuddy企业版，感谢兄弟们一路支持**

文章写到这里，顺便送个福利。

做AIOPC这一年多，从最初的一个人瞎摸索，到现在有了一群志同道合的兄弟一起交流、一起挖洞、一起搞钱，真的很感慨。为了感谢大家的支持，我自掏腰包买了10套WorkBuddy企业版（月度授权），免费送给正在做AI安全、AI开发、或者打算用AI创业的兄弟们。

**参与方式**：
在本公众号后台回复关键词“**WorkBuddy抽奖**”，获取抽奖链接。我们会在7月10日晚上8点开奖，随机抽出10位做OPC或者企业兄弟，每人赠送WorkBuddy企业版十套。

中奖的兄弟，如果你是企业用户，我们还会额外提供一次免费的“后续购买相关云服务产品也会有优惠哦

没有中奖的兄弟也别急，后续我们还会定期搞这样的活动。你们的每一次点赞、在看、转发，我都记在心里。

**严正声明**
本文所述漏洞已在授权范围内进行测试并完成修复。所有案例均经过脱敏处理，仅保留技术原理供学习参考。利用SSRF攻击未授权系统属于违法行为，请务必在合法合规的前提下进行安全研究。AI开发者和使用者应共同维护网络安全生态。

**期待与你继续同行，一起把AIOPC的路走宽。先扫码拿名额哦 自费掏出10套workbuddy企业版**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3oR6eMARh6wy9vyAlB86sRom4xFkAYOjPUtVIss3Sic98Yb55ul6NsYKkmLAX3mmkW9bkU5FsFBYJIEMKWYHdoqyFf8FEn312kg58WpExGWc/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6x6n1Wb1pmwN6kAz3L4jCKjzXFiapPubIuT2OpX0FibbHamG6peZ1SKqicC6cNuENqACmDbBYnem2XNzHH87F25ADeRoMicGPyF7Sk/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zxPsSBiaTT0QiaBjibScxViciathof2tlahJCticqia6DncZNe4Fiatd1zWxPQKdTAqnyRPFWmxviaJJm5R8JLbEAURJnZRMiaKa1quLS8k/0?wx_fmt=png)

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