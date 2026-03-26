---
title: LiteLLM供应链投毒事件解析【聚合情报】
url: https://mp.weixin.qq.com/s/KTK0O8Qzvh4PowUf2_sTNA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:27:58.292878
---

# LiteLLM供应链投毒事件解析【聚合情报】

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/frAs2k03Ypm6LWtiafoEkZJdWTa1jLa5bh9ezhzj3yzSedGRSnUIaO8PFskWzqsWDaqZYvskZ1REiaNkLjfUysgfKCH4BUowIKjf6ia8w0eQRY/0?wx_fmt=jpeg)

# LiteLLM供应链投毒事件解析【聚合情报】

安天垂直响应平台

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

安天基于loongClaw（龙爪）平台自动获取信息聚合生成“LiteLLM供应链投毒事件解析”文章。

**0****1**

**概述**

2026年3月24日，AI基础设施领域发生了一起性质极为恶劣、影响范围巨大的供应链攻击事件。知名开源Python库LiteLLM在PyPI软件仓库上的版本1.82.7和1.82.8被植入恶意代码，实现了“安装即中招”的自动化攻击。该库作为一个统一调用各大模型API的流行工具，月下载量超过9500万次，并被超过2000个项目直接或间接依赖，同时由于OpenClaw的流行，也带动了LiteLLM的装机量，导致潜在受感染环境数量极为庞大。

此次事件并非孤立发生，而是开源软件供应链“连锁崩塌”的一个典型样本。攻击始于对另一关键安全工具Trivy的攻陷，并利用窃取的凭证横向渗透，最终在AI开发者的核心工具链中引爆，其手法之精准、后果之严重，为整个开源生态和软件开发安全敲响了警钟。[安天AVL SDK反病毒引擎](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650211782&idx=1&sn=06dcc3c05ffce88f87cd134034aaf559&scene=21#wechat_redirect)已强化AI相关检测能力，保障智能体基础设施环境安全。

**0****2**

**事件详情**

## 2.1 **时间线**

3月19日：攻击组织TeamPCP攻陷了流行漏洞扫描工具Trivy的CI/CD系统。

3月24日18:39及18:52：攻击者利用从LiteLLM被污染的CI/CD环境中窃取的PyPI发布令牌，先后发布了包含恶意代码的litellm==1.82.7和litellm==1.82.8版本。

3月24日20:20：安全研究人员通过一个由恶意代码自身BUG引发的“Fork 炸弹”崩溃现象，意外发现了此次投毒。

后续：社区报告后，攻击者迅速发动“噪音淹没”攻击，尝试掩盖事件，但最终被社区和官方遏制。官方随后下架恶意版本，并发布了干净的1.82.9版本。

## 2.2 **攻击手段**

恶意载体：恶意版本中包含一个名为litellm\_init.pth的特殊文件。在Python环境中，.pth文件会在每次Python解释器启动时自动执行，这意味着无需用户显式导入或调用LiteLLM，只要环境中安装了受污染版本，恶意代码便会自动运行。

持久化与扩散：恶意代码在启动时执行，具备极强的持久性。更严重的是，一旦检测到运行在Kubernetes集群中，它会利用服务账户令牌创建特权Pod，试图横向扩散到集群中的每个节点。

## 2.3 **恶意代码功能**

该恶意代码是一个功能全面的敏感信息窃取器，其收集范围包括：

1. 云服务凭证：AWS、Google Cloud、Azure的访问密钥和配置文件。

2. 基础设施密钥：SSH私钥、Kubernetes配置 (kubeconfig)、Docker凭证。

3. 开发与数据资产：环境变量文件(.env)、数据库配置文件、Git凭证。

4. 加密货币钱包：常见钱包的私钥文件。

所有收集到的数据会被加密打包，外传到攻击者控制的域名(checkmarx[.]zone、models.litellm[.]cloud) 下。

**0****3**

**技术分析**

1. 典型的供应链攻击链：本次事件清晰地展示了一条“上游污染 -> 凭证窃取 -> 下游投毒”的攻击链。攻击者首先攻陷了开发流程中广泛使用的安全工具Trivy。当LiteLLM在其CI/CD流水线中使用被污染的Trivy进行漏洞扫描时，其环境（包括PyPI发布令牌）即被攻击者窃取。这暴露了一个残酷的现实：我们用来加固安全的安全工具，一旦被攻破，反而会成为攻击者最锋利的矛。

2. “噪音淹没”式反制：在社区成员于GitHub提交Issue报告此事后，攻击者在102秒内利用数十个被盗账号发布了大量垃圾评论，并试图直接关闭Issue，企图快速“灭口”以延缓事件曝光。这种自动化、规模化的反制手段，表明攻击者具备成熟的运营能力，且对开源社区的响应模式有深入研究。

3. 讽刺性的暴露方式：事件的发现极具偶然性。恶意代码在触发时，由于编程逻辑缺陷，创建的子进程会再次触发.pt文件，导致进程数量呈指数级增长，最终引发“Fork 炸弹”使系统崩溃。正如知名AI研究者Andrej Karpathy所指出的，若无此BUG，此次投毒可能潜伏数日甚至数周，其造成的真实损失将难以估量。

**0****4**

**影响与警示**

1. “连锁崩塌”效应：Wiz安全研究员Gal Nagli将此事描述为“开源供应链的连锁崩塌”。Trivy的失守导致LiteLLM被投毒，而LiteLLM窃取的数万份云凭证、密钥，将成为攻击者进行下一轮更精准、更深入攻击的“弹药”。这种环环相扣的连锁反应，使得单一组件的风险被急剧放大。

2. 对AI基础设施的信任危机：LiteLLM作为连接众多AI应用与底层模型的核心桥梁，其被投毒直接动摇了当前AI工具链的安全基础。大量基于其构建的AI应用（如DSPy, MLflow, Cursor的MCP 服务器等）在不知情的情况下引入了致命后门。这迫使行业必须重新审视对关键开源依赖的信任模型。

3. “最小依赖”理念的回归：Karpathy在此事件后再次强调了对软件供应链的深度担忧，并表示将更倾向于让大模型生成简单功能代码，而非直接引入外部依赖。这反映出顶级开发者群体中一种日益增长的倾向：在便利性与安全性之间，开始向后者做出更明显的倾斜。

**0****5**

****应对与防护建议****

1. 立即自查与处置：

在Python环境中执行pip show litellm检查版本。

仅1.82.6及更早版本是安全的。如果安装了1.82.7或1.82.8，应立即卸载，因为所有相关环境的凭证都可能已经泄露。

紧急更换凭证：立即更换所有可能曾被存储在受影响环境中的凭证，包括但不限于云服务密钥、SSH 密钥、API令牌、数据库密码等。

2. 加强CI/CD安全：

对CI/CD系统中使用的所有工具（尤其是安全扫描工具）进行严格的来源验证和完整性校验。

为关键项目的发布流程设置多人审核（MFA）、短时效令牌，并实施网络隔离，最小化凭据泄露风险。

3. 依赖项管理升级：

使用pip-audit等工具持续监控依赖项中的已知漏洞。

考虑锁定依赖版本(pip freeze > requirements.txt)，并定期进行审查和选择性更新。

对于关键项目，评估引入“软件物料清单”（SBOM）机制以清晰掌握供应链组成。

4. 安装安天智甲终端防御系统

[安天智甲终端防御系统](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650205228&idx=3&sn=72473850250f89f2d1b2896b6e5fa702&scene=21#wechat_redirect)（简称“智甲”）是面向办公机、服务器、虚拟化主机等设备的终端安全防护产品。智甲按照执行体治理安全理念设计，内置安天自主研发的AVL SDK反病毒引擎和驱动级主防、主机防火墙、应用行为管理、介质管控、邮件客户端防护（含WEB Mail）、敏感对象（目录、文件、注册表等）保护、动态关键数据备份等功能模块，支撑网络管理者实现资产管理、威胁拒止、威胁检测与分析、主机管控、事件调查等业务，打造“可管理”、“可感知”、“可防护”、“可响应”的全场景、一体化的终端安全纵深防护体系。

智甲根据龙虾（OpenClaw）进行了主防规则的专门优化，安装在养虾机后，可以有效改善养虾环境安全，防范攻击风险。

****附录：参考资料****

[1] LiteLLM 官方事件通告及修复版本

<https://github.com/BerriAI/litellm/releases/tag/v1.82.9>

[2] GitHub Issue #24512

https://github.com/BerriAI/litellm/issues

[3] TeamPCP Backdoors LiteLLM Versions 1.82.7–1.82.8 via Trivy CI/CD Compromise

https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html

[4] KICS GitHub Action Compromised: TeamPCP Strikes Again in Supply Chain Attack

<https://www.wiz.io/blog/teampcp-attack-kics-github-action>

[5] 安天反病毒引擎强化对OpenClaw Skills的检测点

[https://mp.weixin.qq.com/s/aO\_ze\_88Fzuw81EQl6Y-qQ](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214116&idx=1&sn=baaca6ee357f982c1faec003d4e5b266&scene=21#wechat_redirect)

[6]安天智甲护航用户安全养虾（OpenClaw）

[https://mp.weixin.qq.com/s/N5hYuPmJb8Wzckl8NuR09g](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214267&idx=1&sn=1642b541c74712aad5429b66d939697d&scene=21#wechat_redirect)

loongClaw（龙爪）是安天支撑黑龙江省数字运营公司定制的OpenClaw安全加固版本，可以拓展编码开发、威胁分析、信息汇聚采编等技能。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yicx1jVK2eOnMpQiaccCDTrrxNFUNEkjj9HOFJY9d1a1PkIWPTeH4uXSslP7nKTo0qUORjCREJq8BISLcgCepGgw/0?wx_fmt=png)

安天垂直响应平台

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yicx1jVK2eOnMpQiaccCDTrrxNFUNEkjj9HOFJY9d1a1PkIWPTeH4uXSslP7nKTo0qUORjCREJq8BISLcgCepGgw/0?wx_fmt=png)

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