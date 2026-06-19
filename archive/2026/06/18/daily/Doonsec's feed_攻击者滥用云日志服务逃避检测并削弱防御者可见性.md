---
title: 攻击者滥用云日志服务逃避检测并削弱防御者可见性
url: https://mp.weixin.qq.com/s/2AUkP12CM6yybYqKMrBlzg
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:02:26.505665
---

# 攻击者滥用云日志服务逃避检测并削弱防御者可见性

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1vNWBX2Jss8gGSumialDsOS3mbB3N607jlfnxr57wChQD5QPpNFbgZassybmTK17KcDgRawvnaVTj6EGiap8Y9KDYUqU0ypfR88/0?wx_fmt=jpeg)

# 攻击者滥用云日志服务逃避检测并削弱防御者可见性

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3yQibENXyKSz4XIccGiapiadYQAWbCoZ8jGOGCh1EU827WbxXiaQPYmFcbh2TCYJC9luczLEbdkOf1mEfsD3Biax8zuJG1PicLiaCNLc/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2YL6uicKS8KhYegrdzqgEonnjv3oPvsFacS9uyt3pIb0ia10hXveJ9evjarnBkuWllsYN0QA3zstwlMuq5ibrXGul7MY8IWVczkY/640?wx_fmt=png&from=appmsg)

根据Palo Alto Networks Unit 42的最新研究，威胁行为者正越来越多地针对云日志服务实施攻击，以逃避检测并维持对已入侵环境的持续可见性。这些本应作为关键安全层的服务，现正被武器化以制造云基础设施中的监控盲区。

Part01

云日志服务成为攻击目标

AWS CloudTrail和Google Cloud Logging等云日志平台本是追踪云环境活动的主要依据。安全团队严重依赖这些日志为SIEM（安全信息和事件管理）、SOAR（安全编排自动化与响应）和CSPM（云安全态势管理）工具提供支持。但获得足够权限的攻击者可以操纵这些系统来破坏可见性，甚至窃取日志供其监控使用。

研究人员将这些攻击分为两大主要战术：防御规避和持续可见性。在防御规避场景中，攻击者专注于禁用或篡改日志机制以避免被发现。

Part02

防御规避技术剖析

最直接的技术之一是彻底停止日志收集。在AWS中，拥有CloudTrail:StopLogging权限的攻击者可通过API调用中止日志记录，使监控系统立即失效。类似地，在Google Cloud中，攻击者可以利用logging.sinks.Update权限禁用日志接收器。

另一种常见技术是删除日志存储目标。例如，拥有s3:DeleteBucket权限的攻击者可以移除CloudTrail日志存储桶，从而销毁取证证据。在Google Cloud中，日志存储桶虽可删除，但会进入延迟删除状态，提供有限的恢复窗口。

![通过攻击者控制的加密密钥攻击流程破坏AWS日志记录](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0kjZsTPrLmO1ibxA6p3q5P8cKV8k2uQicYCD3MFibyb0eB1bqZfsJjYXzfhgu7dAAgxRg7cqCRBZf531AJ5QW7xOXvU0AwKOXWzc/640?wx_fmt=jpeg)

更高级的攻击者可能通过操纵加密密钥来破坏日志记录。通过用攻击者控制的密钥替换合法的AWS KMS密钥，然后撤销访问权限，日志将变得不可读或完全无法写入。在Google Cloud中使用客户管理的加密密钥（CMEK）也可实施类似攻击，有效将防御者锁定在自己的日志之外。

Part03

日志污染与重定向攻击

日志污染是另一种隐蔽技术。拥有对象级访问权限的攻击者可以下载、修改并重新上传存储在Amazon S3等服务中的日志文件，破坏数据完整性并误导事件响应团队。

![加密密钥不可访问的后果](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX36aAd9IRKcxbKzpbWwbOVWbfZJm2UcS7dfDibtWxmPIJSw5qlIhVJnb1QWlcv8jSJsUcQvwvyrvRcIOUliapITeia28jGUYVB4GI/640?wx_fmt=jpeg)

除了规避防御，攻击者还利用日志系统实现持续可见性。他们不再通过主动侦察触发警报，而是配置新的日志路由机制将日志副本发送到攻击者控制的环境。在AWS中，这涉及创建指向外部S3存储桶的新CloudTrail跟踪；在Google Cloud中，攻击者则滥用日志接收器来重定向日志。

日志重定向特别危险，因为它会悄无声息地将实时活动数据（包括IAM变更、VM部署和数据访问事件）传输给威胁行为者。Palo Alto Networks Unit 42表示，这些技术的影响范围从可见性丧失到隐蔽持久化和数据窃取不等。例如，停止日志记录会导致监控完全失效，而日志重定向则使攻击者能够持续洞察受害者环境。

Part04

防御建议

为降低这些风险，组织必须对日志资源实施严格的访问控制。应将update-trail、logging.sinks.update和存储修改等关键权限限制在高度特权角色范围内。启用完整性验证功能（如AWS CloudTrail日志文件验证）有助于检测篡改行为。

云服务提供商也提供内置保护措施。AWS为管理操作维护90天不可变事件历史记录，而Google Cloud提供无法更改或删除的系统创建日志存储桶。但这些保护措施可能无法覆盖所有日志记录场景，特别是在自定义配置中。组织必须将日志管道视为关键资产，并实施分层防御，确保攻击期间可见性不受损害。

参考来源：

Hackers Abuse Cloud Logging Services to Evade Detection and Defender's Visibility

https://cybersecuritynews.com/hackers-abuse-cloud-logging-service/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2cVdntRnNdReFrEC9uicNrkrzxp72OgpNDz7srDyd0sPwPYZejHF5E9TqvpJWJ5qHkqqDtlREdb65n2YIfXD2jnNBFTqRI2LhM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1uQ9xLm3d4ZLoKboK1GHqPxkP2twtDHay11g4CqZnzXFyjmtib8WT7iaP1Libibnib4wCE0UreN6hUMgkYJ6NP9gD2ib8g2RNFTUAj8/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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