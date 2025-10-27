---
title: 攻击者在勒索活动中利用公开的.env文件入侵云账户
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546519&idx=2&sn=4a17ef4b5ba45130843a6e86c90997b0&chksm=fa938056cde409406d1fd6ab4fe87b364d44e11cd59efefd89242550b9aee2cded8ae55a5add&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-21
fetch_date: 2025-10-06T18:04:22.362436
---

# 攻击者在勒索活动中利用公开的.env文件入侵云账户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176mr1B3rdwQp6J42DS4wSBI7nBPrlqAc2ahwmNQGkJSpww3250Rsia82ic8kicl2Iibz35pbJfflENbiczw/0?wx_fmt=jpeg)

# 攻击者在勒索活动中利用公开的.env文件入侵云账户

网络安全应急技术国家工程中心

近日，一场大规模勒索活动利用可公开访问的环境变量文件（.env）入侵了多个组织，这些文件包含与云和社交媒体应用程序相关的凭据。

「在这次勒索活动中存在多种安全漏洞，包括暴露环境变量、使用长期凭证以及缺乏最小权限架构 。」Palo Alto Networks Unit 42 在一份报告中指出。

该活动的显著特点是在受感染组织的亚马逊网络服务（AWS）环境中设置了攻击基础设施，并将其作为跳板，扫描超过 2.3 亿个唯一目标的敏感数据。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38F3ibHODlJJXwFzdbiaKoBricSgeWFCQM4DbjPISuorgMpBuucIKE6j9FoP7AHiaR0uVP31TEGaR8kvQ/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic)

据了解，该恶意活动以 11 万个域为目标，在 .env 文件中获取了超过 9 万个独特变量，其中 7000 个变量属于组织的云服务，1500 个变量与社交媒体账户相关联。

Unit 42 表示，这次活动攻击者成功对托管在云存储容器中的数据进行勒索。不过，攻击者并没有在勒索之前对数据进行加密，而是将数据提取出来，并将勒索信放在被入侵的云存储容器中。

这些攻击最引人注目的一点是，它并不依赖于云提供商服务中的安全漏洞或错误配置，而是源于不安全 Web 应用程序上的 .env 文件意外曝光，从而获得初始访问权限。

成功破坏云环境为广泛的发现和侦察步骤铺平了道路，目的是扩大他们的影响力，威胁行为者将 AWS 身份和访问管理（IAM）访问密钥武器化，以创建新角色并提升他们的权限。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38F3ibHODlJJXwFzdbiaKoBricicwZUbR0AXV1mdsicCpoH4hJIRwicA3IQ1icf4Cu6VlNUPnjeHtrgMibl8g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

具有管理权限的新 IAM 角色随后被用于创建新的 AWS Lambda 函数，以启动包含数百万个域名和 IP 地址的全网自动扫描操作。

Unit 42 的研究人员 Margaret Zimmermann、Sean Johnstone、William Gamazo 和 Nathaniel Quist 说：「脚本从威胁行为者利用的可公开访问的第三方 S3 桶中检索到了潜在目标列表。恶意 lambda 函数迭代的潜在目标列表包含受害者域名的记录。对于列表中的每个域名，代码都会执行一个 cURL 请求，目标是该域名暴露的任何环境变量文件（即 https://<target>/.env）。」

如果目标域名托管了已暴露的环境文件，文件中包含的明文凭据就会被提取出来，并存储在另一个由威胁行为者控制的公共 AWS S3 存储桶中新建的文件夹中。目前，该存储桶已被 AWS 关闭。

研究人员发现，这场攻击活动特别针对包含 Mailgun 凭证的 .env 文件实例，表明攻击者试图利用它们从合法域名发送钓鱼邮件并绕过安全保护。

感染链的最后，威胁者会从受害者的 S3 存储桶中提取并删除敏感数据，并上传一张勒索信，提醒受害者联系并支付赎金，以避免敏感信息在在暗网上被出售。

威胁行为者试图创建新的弹性云计算（EC2）资源用于非法加密货币挖矿，但以失败告终，这也表明了攻击的经济动机。

目前还不清楚谁是这场活动的幕后黑手，部分原因是使用了 VPN 和 TOR 网络来掩盖其真实来源，不过 Unit 42 表示，它检测到两个 IP 地址分别位于乌克兰和摩洛哥，是 lambda 功能和 S3 提取活动的一部分。

研究人员强调：「这次活动背后的攻击者很可能利用了大量自动化技术来成功、快速地开展行动。这表明，这些威胁行为者在高级云架构流程和技术方面既熟练又专业。」
参考资料：

https://thehackernews.com/2024/08/attackers-exploit-public-env-files-to.html

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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