---
title: 新型 “whoAMI” 攻击利用AWS AMI 名称混淆实现远程代码执行
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522246&idx=2&sn=fbca692993726f368c05fa16b80eb5a8&chksm=ea94a6acdde32fba818898dc5b3793d9312e2f4883cf817d13cb650172d5a2898b6b96717130&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-18
fetch_date: 2025-10-06T20:39:47.415970
---

# 新型 “whoAMI” 攻击利用AWS AMI 名称混淆实现远程代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSia6g9ibXm81W2NhfYicjuNlFOMmgqqwicSLhBOGE37xqS6n9omYWJ8q70yUczEae4xTHSWPF4W7RrVQ/0?wx_fmt=jpeg)

# 新型 “whoAMI” 攻击利用AWS AMI 名称混淆实现远程代码执行

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSia6g9ibXm81W2NhfYicjuNlF810BZjgWPnoMta19ia0tyvJb4coD15kHbY1gxibEmicbIyjNFumSRzoog/640?wx_fmt=gif&from=appmsg)

**网络安全研究人员披露了名称混淆攻击 “whoAMI”，它可使发布具有特定名称的亚马逊机器镜像 (AMI) 的任何人在AWS账户中获取代码执行权限。**

Datadog Security Labs 公司的安全研究员 Seth Art 在一份报告中提到，“如被大规模执行，该攻击可用于访问数千个账户。该易受攻击的模式见于很多私密和开源代码仓库中。”

该技术的核心是供应链攻击，涉及发布恶意资源并诱骗配置不当的软件使用它。该攻击利用的第一个事实是任何人均可将用于引导 AWS 中 EC2 实例的虚拟机镜像上传到Community分类，而利用的第二个事实是开发人员通过ec2:DescribeImages API查找AMI时忘记提到 “—owners” 属性。

换句话说，该名称混淆攻击要求在受害者通过API检索AMI ID时，需要满足如下三个条件：

* 使用名称过滤器
* 未能识别owner、owner-alias或owner-id 参数；
* 从返回的匹配镜像清单中提取最近创建的镜像 (“most\_recent=true”)。

这就导致攻击者能够以匹配搜索标准中制定的模式的恶意AMI，导致通过威胁行动者的极其相似的 AMI 创建EC2实例，从而获得实例的RCE能力，初始化利用后的操作。而攻击者需要做的就是通过一个AWS账户在公开的Community AMI 分类中发布安装后门的AMI并选择目标所寻找的匹配AMI的名称。Art 提到，“它与以来混淆攻击非常类似，不过在依赖混淆攻击中，恶意资源是一个软件依赖（如pip包），而在 whoAMI 名称混淆攻击中，该恶意资源是一个虚拟机镜像。”

Datadog 提到，该公司所监控的约1%的组织机构受 whoAMI 攻击影响，并发现了用Python、Go、Java、Terraform、Pulumi 和 Bash shell 使用易受攻击标准编写的代码公开示例。

研究人员在2024年9月16日将该漏洞告知亚马逊公司，后者在三天后将其修复。亚马逊公司表示目前尚未发现该技术遭在野利用的迹象。该公司提到，“所有的AWS服务都按设计运行。从扩展的日志分析和监控中发现，该技术仅由授权研究人员自身执行，并非发现遭其他方利用的迹象。该技术可影响通过 ec2:DescribeImages API 检索而未制定owner值的AMI ID。2024年12月，我们引入了‘Allowed AMIs’，它是账户范围内的设置，可使客户在自己的AWS账户中限制AMIs的发现和使用。我们建议客户评估并执行这一新兴安全控制。”

截止到去年11月，HashiCorp Terraform 在用户使用 “most\_recent = true” 而terraform-provider aws 5.77.0中不存在owner 过滤器时，发出告警。该告警有望在6.0.0版本升级为出错提醒。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[在线阅读版：《2024中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520484&idx=1&sn=8a845b39720a318c297075e98f5fe5e0&scene=21#wechat_redirect)

[在线阅读版：《2023中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517225&idx=1&sn=8154b433ae2be87ccbae15bc0fb09a00&scene=21#wechat_redirect)

[在线阅读版：《2022中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&scene=21#wechat_redirect)

[Google Cloud 依赖混淆漏洞影响数百万台服务器](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520848&idx=4&sn=5dd6c8f2b2d48123ef978d8ef1b071ff&scene=21#wechat_redirect)

[什么鬼？我能通过依赖混淆攻击在 Halo 游戏服务器中执行命令，微软不 care？！](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506074&idx=1&sn=40b66f0cbedbc7f81a5e8ea6b5f96000&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2025/02/new-whoami-attack-exploits-aws-ami-name.html

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