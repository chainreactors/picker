---
title: 朝鲜黑客瞄准macOS用户
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247522644&idx=1&sn=5a56c13c590a887a2ebe207884c2cea7&chksm=c144ebe9f63362ff7b974b95398235afe0c9e5f1011d2dee6710716874f1c4104adc2da419cd&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-11-14
fetch_date: 2025-10-06T19:19:23.897937
---

# 朝鲜黑客瞄准macOS用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqpHaVv3cCWCfNLvDFcQYnSOiafsr57Xk2EDsfOVQaWbAL667HoFUH4jYWZrUoT05OdOxPaghAetfNw/0?wx_fmt=jpeg)

# 朝鲜黑客瞄准macOS用户

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqpHaVv3cCWCfNLvDFcQYnSOOnuAbzC8D8ecX0h5oVzEAjVFYutWZKEiatoQEV7WCssIte6rjQ7cZMQ/640?wx_fmt=png&from=appmsg)

与朝鲜民主主义人民共和国（DPRK）有联系的威胁行为者已被观察到针对与加密货币相关的企业，使用一种多阶段恶意软件，能够感染苹果 macOS 设备。

网络安全公司 SentinelOne 将该活动称为隐藏风险，并以高度信心将其归因于 BlueNoroff，该组织之前与诸如RustBucket、KANDYKORN、ObjCShellz、RustDoor（又名Thiefbucket）和TodoSwift等恶意软件家族有关联。

这项活动“利用传播关于加密货币趋势的虚假新闻的电子邮件，通过伪装成 PDF 文件的恶意应用程序感染目标，”研究人员拉法埃尔·萨巴托、菲尔·斯托克斯和汤姆·黑格尔在与《黑客新闻》分享的报告中表示。

“该活动可能早在 2024 年 7 月就开始，使用电子邮件和 PDF 诱饵，配以关于加密相关主题的假新闻标题或故事。”

根据美国联邦调查局（FBI）在 2024 年 9 月的公告，这些活动是针对在去中心化金融（DeFi）和加密货币领域工作的员工的“高度定制、难以检测的社会工程”攻击的一部分。

这些攻击以虚假的工作机会或企业投资的形式出现，与目标进行长时间的互动以建立信任，然后再投放恶意软件。

SentinelOne 表示，它在 2024 年 10 月底观察到一起针对加密相关行业的电子邮件钓鱼尝试，该尝试发送了一个伪装成 PDF 文件的投放程序（“Hidden Risk Behind New Surge of Bitcoin Price.app”），该文件托管在 delphidigital[.]org 上。

该应用程序是用 Swift 编程语言编写的，已于 2024 年 10 月 19 日被发现签名并公证，开发者 ID 为“Avantis Regtech Private Limited (2S8XHJ7948)”。该签名已被 iPhone 制造商撤销。

在启动时，该应用程序从 Google Drive 下载并向受害者显示一个诱饵 PDF 文件，同时秘密地从远程服务器检索第二阶段的可执行文件并执行它。一个 Mach-O x86-64 可执行文件，这个基于 C++的未签名二进制文件充当后门以执行远程命令。

后门还结合了一种新颖的持久性机制，利用了 zshenv 配置文件，这标志着该技术首次在恶意软件作者的实际应用中被滥用。

“研究人员表示：‘这在现代版本的 macOS 上具有特别的价值，因为苹果在 macOS 13 Ventura 中引入了后台登录项的用户通知。’”

“苹果的通知旨在警告用户何时安装持久性方法，特别是经常被滥用的 LaunchAgents 和 LaunchDaemons。然而，滥用 zshenv 在当前版本的 macOS 中并不会触发这样的通知。”

该威胁行为者还被观察到使用域名注册商 Namecheap 建立一个围绕与加密货币、Web3 和投资相关主题的基础设施，以赋予其合法性表象。Quickpacket、Routerhosting 和 Hostwinds 是最常用的托管服务提供商之一。

值得注意的是，攻击链与 Kandji 在 2024 年 8 月强调的之前的活动有一定程度的重叠，该活动也使用了一个名为“Bitcoin 价格下跌的风险因素正在出现(2024).app”的 macOS 投放应用来部署 TodoSwift。

目前尚不清楚是什么促使威胁行为者改变战术，以及这是否是对公众报道的回应。“北朝鲜行为者以其创造力、适应能力和对其活动报告的意识而闻名，因此我们很可能只是看到他们的网络攻击计划中出现了不同的成功方法，”斯托克斯告诉《黑客新闻》。

另一个令人担忧的方面是 BlueNoroff 能够获取或劫持有效的 Apple 开发者账户，并利用这些账户让他们的恶意软件获得 Apple 的认证。

“在过去的 12 个月左右，北朝鲜的网络行动者针对与加密相关的行业进行了系列活动，其中许多活动涉及通过社交媒体对目标进行广泛的‘培养’，”研究人员说。

“隐秘风险”运动偏离了这一策略，采取了一种更传统和粗糙的电子邮件钓鱼方法，尽管这并不一定效果较差。尽管初始感染方法比较直接，但其他朝鲜民主主义人民共和国支持的运动的特征仍然明显。

这一发展也发生在朝鲜黑客策划的其他活动之中，他们试图在西方的各家公司寻找工作，并通过伪装成招聘挑战或任务的方式，向潜在求职者传递恶意软件，使用带有陷阱的代码库和会议工具。

这两个入侵组，称为 Wagemole（又名 UNC5267）和 Contagious Interview，已被归因于一个被追踪的威胁组，名为 Famous Chollima（又名 CL-STA-0240 和 Tenacious Pungsan）。

ESET 将 Contagious Interview 称为DeceptiveDevelopment，并将其归类为一个新的 Lazarus Group 活动集群，旨在针对全球的自由开发者进行加密货币盗窃。

“传染性面试和工资虫活动展示了朝鲜威胁行为者不断演变的战术，他们继续窃取数据，在西方国家获得远程工作，并绕过金融制裁，”Zscaler ThreatLabz 研究员朴成洙本周早些时候说。

"凭借精细的混淆技术、多平台兼容性和广泛的数据盗窃，这些活动对企业和个人构成了日益严重的威胁。"

\* 本文为闫志坤编译，原文地址：https://thehackernews.com/2024/11/north-korean-hackers-target-crypto.html
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqXZatwW85WHD0ggOUzguusylfEicp7y64ic36rtZXpLGPKXds2NvBpuExtgAMicK0LB71waZTVKfpPw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513359&idx=1&sn=2f3bd51b24862de02cca6078688bafeb&chksm=c144c7b2f6334ea415adac810ce4803cdb3cd5e5ba194ff394b7278ebbb48cc830c8d405427a&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqpHaVv3cCWCfNLvDFcQYnSOGJkGK06YzCAmUzUNJGKFLF1pTy7Y4jianelrbREgL2WiaY2HnFVHfvuw/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247498164&idx=1&sn=23acf12d5264aded6d45548d5324297b&chksm=c1448b09f633021faaab09c54bf5b9380a926adba2d954dbf58511ff26da9b6aab6c7d05427c&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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