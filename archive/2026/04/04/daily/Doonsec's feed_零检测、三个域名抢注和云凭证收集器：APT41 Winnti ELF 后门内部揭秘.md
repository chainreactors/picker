---
title: 零检测、三个域名抢注和云凭证收集器：APT41 Winnti ELF 后门内部揭秘
url: https://mp.weixin.qq.com/s/vkov6sl9QWPLVYmQ1nhc5w
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:33:30.684807
---

# 零检测、三个域名抢注和云凭证收集器：APT41 Winnti ELF 后门内部揭秘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0EfvjKtwdPr0R1cFQjhHP91xPbDajnxYMS4zI7axLnzqzE4ibbCpGZlCnpol6Xce2LGg4kwPJbwWxwQ1lsAdx7O0GEl0KaDKYLA/0?wx_fmt=jpeg)

# 零检测、三个域名抢注和云凭证收集器：APT41 Winnti ELF 后门内部揭秘

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

当研究员@TuringAlex将一个在VirusTotal上检测结果为零的ELF样本标记为APT41时，我们以为这只是另一个被急于求成的分析师误判的普通Linux木马。但我们错了。

该样本是一个 2.7 MB 的 x86\_64 ELF 二进制文件，经过近乎最大程度的混淆处理。它连接到三个 C2 域名，这些域名均为我国科技公司域名的抢注，最终解析到位于新加坡的同一个阿里云 IP 地址。该 IP 地址两年多来一直未被 Shodan 检测到。该后门程序会从 AWS、GCP、Azure 和阿里云工作负载中窃取云实例元数据，并使用 SMTP 端口 25 作为隐蔽的命令通道。

样本

MD5：f1403192ad7a762c235d670e13b703c3一个 2.7 MB 的 ELF 二进制文件，熵值接近最大值（约 832 KB 的代码，每字节 7.997 位）。这种混淆并非简单的打包，而是使用了自定义代码虚拟化器或指令级转换，使得在没有专用反虚拟化工具的情况下，静态分析几乎不可能进行。

MalwareBazaar 将其标记为 Winnti。ReversingLabs 将其归类为Linux.Backdoor.Winnti。Intezer 确认了代码重用，将其与 Winnti 的谱系联系起来，该谱系可以追溯到六年前：PWNLNX、RedXOR、AzazelFork、Earth Lusca 的 SprySOCKS 和 Melofee。这并非一个全新的恶意软件家族——它是中国情报机构自 2020 年以来一直在迭代开发的工具的最新演化版本。

三个领域，一种模式

该后门连接到三个 C2 域名，这三个域名都冒充合法的中国科技公司：

* ai[.]qianxing[.]co 千信/千星AI
* ns1[.]a1iyun[.]top 阿里云（阿里云） 注意1替换l
* ai[.]aliyuncs[.]help 阿里云存储 aliyuncs = 阿里云服务

这三个域名都解析到43[.]99[.]48[.]196位于新加坡的阿里云实例。这种域名抢注模式是故意的：如果网络防御者a1iyun.top在日志中看到针对该域名的 DNS 查询，它看起来与合法的阿里云流量（aliyun.com）非常相似，足以蒙混过关。ai.子域名前缀在 2026 年又增加了一层可信度，届时每家公司都会拥有一个 AI 子域名。

该a1iyun[.]top域名拥有一个有效期至2023 年 8 月的Let's Encrypt 通配符证书。该基础设施已运行两年半，期间未被销毁、列入黑名单或被报告给任何公共威胁情报机构。

隐形C2

Shodan 返回“无可用信息” 43[.]99[.]48[.]196。未发现开放端口、横幅广告或服务。该 IP 地址在其运行期间完全未被互联网扫描识别。

这是有意为之。C2 服务器只响应发送正确植入握手包的连接。其他所有操作——端口扫描、网络爬虫、研究人员探测——都无法连接。我们通过尝试直接连接到 25、443 和 8088 端口证实了这一点。尽管这三个端口是文档中记录的 C2 服务器端口，但它们都拒绝了我们的探测请求。

端口 25 尤其值得注意。C2 服务器上的 SMTP 协议是一种隐蔽的通信通道选择——端口 25 上的电子邮件流量是预期之内的，通常不会被数据防泄漏 (DLP) 系统检查，并且经常被防火墙列入白名单。植入程序很可能将 C2 命令编码到 SMTP 协议的通信中。

云凭证收集

最具实际意义的能力是后门对云实例元数据的访问169.254.169.254。这是每个主要云提供商用来向正在运行的工作负载提供实例凭证、API 令牌和配置数据的链路本地地址。

当此植入程序部署到云虚拟机上时，它可以收集以下信息：

* AWS：IAM角色凭证、安全令牌、实例身份文档
* GCP：服务账号令牌、项目元数据、Kubernetes 配置
* Azure：托管标识令牌、订阅元数据
* 阿里云：RAM角色凭证、实例元数据

一个被攻破的云工作负载，只要拥有正确的身份和访问管理 (IAM) 权限，就可能导致整个云账户被盗。这并非旨在从单个服务器窃取文件的后门——它的目标是窃取整个云的密钥。

横向移动

该植入程序会向255.255.255.255:6006本地网络广播地址广播UDP数据包。这是一种发现机制，用于识别同一网段上的其他主机，随后可能会尝试使用窃取的凭据或已知的Linux漏洞利用技术进行横向移动。

结合云元数据采集，攻击模型变得清晰：攻破一个工作负载，窃取云凭证，在云环境中横向移动，攻破更多工作负载，如此循环往复。UDP 广播用于处理本地/VPC 网络场景；元数据采集用于处理云 IAM 场景。

归因

基于以下数据，APT41/Winnti 具有高度置信度：

* MalwareBazaar 签名：由提交者社区标记为 Winnti
* ReversingLabs 分类：Linux.Backdoor.Winnti
* Intezer 代码重用：已确认与 Winnti ELF 谱系存在基因联系
* 基础设施模式：阿里云上的中文域名抢注——这与APT41已知的偏好中国云服务提供商的倾向相符。
* 六年谱系：PWNLNX (2020) → RedXOR (2021) → AzazelFork (2022) → Earth Lusca/SprySOCKS (2023) → Melofee (2024) → 本样本 (2025-2026)

网络指标

* ai[.]qianxing[.]co
* ns1[.]a1iyun[.]top
* ai[.]aliyuncs[.]help
* 43[.]99[.]48[.]196（阿里巴巴云，新加坡）

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0FfjK2x7mtngWnEIJUpWytHvo4yPLgRzTbByYLSY1n1P9FnSS4zBvGJiaJWyK8zuKsmyTMqiaia9kk4Mkz9D9wjkIBAiaicmUzRmESs/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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