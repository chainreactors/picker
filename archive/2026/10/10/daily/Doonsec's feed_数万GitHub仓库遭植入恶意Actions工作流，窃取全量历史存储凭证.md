---
title: 数万GitHub仓库遭植入恶意Actions工作流，窃取全量历史存储凭证
url: https://mp.weixin.qq.com/s/sJDHSdvjHv6lPCnY0ntkcw
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:00:00.480394
---

# 数万GitHub仓库遭植入恶意Actions工作流，窃取全量历史存储凭证

# 数万GitHub仓库遭植入恶意Actions工作流，窃取全量历史存储凭证

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX0rh26ZLlia523ooronrNeVCWKePkxVeHwnkY4XCt8VDia3OpoUUW8zcMosA38iaicNGgQ4aSWwYOCyM3ibCreHYjE8mgAbkiagEOEnY/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3zmtxeeJHMYcuyrT3LfUtibGI1ka2xKlBAFviavbgbfFN0Yfq8uudMWMNQvBDxhxR6h3tIUuP2ibVVUxs5ibWkAQopqzNzFP0zQxA/640?wx_fmt=png&from=appmsg)

网络安全研究人员近日披露了一场正在持续的凭证窃取攻击活动。攻击者已攻陷两个知名开源项目维护者的GitHub账号，向超过340个代码仓库推送了恶意GitHub Actions工作流。

Part01

GhostAction活动持续扩散

StepSecurity披露的时间线显示，攻击者首先攻陷Takashi Kitao的账号，并从UTC时间13:20开始向27个仓库推送恶意工作流。Takashi Kitao是游戏引擎pyxel的作者，该项目在GitHub上拥有1.84万星标。

约8小时后，攻击者又拿下Uber开源项目athenadriver原作者Henry Wu（账号henrywoo）的账号，并在UTC时间21:10至21:26的16分钟内，向318个仓库推送了同款恶意工作流。

截至2026年10月9日，安全厂商Socket监测显示，自2026年10月7日攻击进入扩散期以来，已有超过500个GitHub账号向数万个仓库提交了该恶意工作流。

这波攻击是GhostAction大规模供应链攻击活动的延续。该活动最早于2025年9月曝光，当时波及327名GitHub用户名下的817个仓库，攻击者通过攻陷开发者账号，共窃取3325组敏感凭证，包括PyPI、npm、DockerHub的访问令牌。

和此前攻击手法一致，两个被攻陷账号推送的恶意工作流分别命名为Security Audit（对应文件名security-audit.yml）或GitHub Actions Security（对应文件名github\_actions\_security.yml）。这些工作流内置硬编码逻辑，会通过明文HTTP将敏感数据外传至攻击者控制的IP地址193.32.204[.]199。

被窃取的数据覆盖范围极广，包括仓库配置的GitHub Actions命名密钥（涵盖CI/CD密钥），以及工作目录、整个git历史中存储的云服务、AI服务、SaaS凭证。典型的泄露凭证包括AWS密钥、Anthropic、OpenAI、OpenRouter的API密钥，以及GitHub、GitLab访问令牌。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2mZZO1QMIyk1vFLLtFNia0bYMBnSeOgU9v67rUDH3UeoGtxBoSDS3CnBI17Z2WoG5kEfatc15c6iaDRcfOhcx42VWEmKovVA9P4/640?wx_fmt=png&from=appmsg)

Part02

恶意载荷扫描全量Git历史收集凭证

整个攻击链分为四个步骤：

* 攻击者首先获取维护者的GitHub凭证，来源大概率是信息窃取程序日志、公开凭证泄露库中的个人访问令牌（PAT）
* 获得初始访问权限后，攻击者首先扫描仓库内的工作流文件，排查已存储的密钥，完成侦察步骤
* 随后冒用受害者身份，向默认分支注入伪装成安全审计的工作流文件
* 工作流内置的恶意载荷提取目标数据，通过curl发送至攻击者控制的服务器

![恶意工作流攻击链](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0m2zeHlLVCz2ibdH6hKu1KDUzNMdX60GFdHsZ4PAgQgwNRuTUOfYzFVw8fNlZ4mwIT8OqE4broHTcJDAucQKKialuF05373s4s0/640?wx_fmt=png)

StepSecurity补充道：“这类恶意工作流的触发条件包括workflow\_dispatch事件、以及无过滤的push操作（覆盖任意分支、任意标签）。工作流运行时会将fetch-depth参数设为0拉取全量代码，随后执行名为‘Audit’的单一步骤，完成四项操作。”

具体操作包括：

* 追加侦察阶段发现的仓库命名密钥
* 扫描工作目录，匹配13类凭证特征，覆盖AWS密钥、AI服务、代码托管服务、SaaS及云服务API密钥
* 扫描整个git历史，匹配相同的13类凭证特征，收集开发者意外提交到仓库、后续虽被删除但仍留存在历史记录中的凭证
* 自动匹配AWS访问密钥ID对应的秘密访问密钥，形成完整可用的凭证对

本周早些时候，安全厂商GitGuardian发布报告称，2026年8月31日至9月30日期间，GhostAction攻击活动已向373名GitHub用户及组织名下的772个公共仓库推送了同款恶意工作流。这些被注入的恶意工作流共瞄准2577组凭证，包括SSH私钥、Azure凭证、DockerHub与GHCR容器镜像仓库凭证、数据库凭证、AWS访问密钥、FTP凭证、Google Cloud与Firebase凭证、GitHub令牌、Telegram、Slack、Discord机器人令牌，以及Cloudflare、npm、PyPI和多家AI服务商的访问密钥。

研究人员在2026年8月30日观测到至少一起特殊案例：攻击者篡改了kuafuai/DevOpsGPT仓库，在项目的Docker镜像中植入了XMRig门罗币挖矿程序。截至发稿，攻击者尚未使用窃取到的发布权限推送恶意版本包。

Part03

恶意代码沿fork链路扩散

建议开发者排查轮换凭证

安全人员建议开发者立即排查自有仓库，检查2026年8月31日之后是否出现上述两类恶意GitHub工作流，一旦发现即可判定仓库已失陷。开发者需要立刻吊销失陷的GitHub凭证，轮换所有相关访问密钥，从仓库全部分支中删除恶意工作流。同时还要检查受感染仓库的所有fork，避免恶意代码进一步扩散。

Socket进一步披露，henrywoo账号命名空间下的279个fork均携带该恶意工作流文件。只要仓库开启Actions功能，后续push操作就可能触发凭证窃取流程。下游fork如果在创建时继承了恶意工作流，或后续同步受影响上游仓库时再次拉取恶意代码，同样存在风险。

其中，私有fork和下游镜像的风险尤其高，因为私有仓库往往存放着仍然有效的真实凭证。两个失陷账号发起的攻击还有一个共同特征：无论是否成功扫描到凭证，每次工作流运行都会回传仓库标识符。因此，即使没有直接窃取到密钥，攻击者仍能掌握所有可触达执行环境的完整清单。

参考来源：

Credential-Stealing GitHub Actions Workflows Planted in Tens of Thousands of Repositories

https://thehackernews.com/2026/10/credential-stealing-github-actions.html

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0YicFBBV16wQdPW4H8cTibDhNEfda7XWQYxJejxMQXMkmUHx6wDDLARUIbdeicO6WQyTRZN8jBRKSbL2bT8srvaRb0FMGv7DXJU8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651348384&idx=1&sn=b0d043fbf6f272983df964e3f249232e&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3mETrvTp1xSWg4nsaY8jdaRdeta9l692aSBiaWUg95sD0gVn7BiaQ6bng5NuFFmERdoTibOtYlCXD4z0Fsus60Vbx1ExXibLicvq4s/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

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