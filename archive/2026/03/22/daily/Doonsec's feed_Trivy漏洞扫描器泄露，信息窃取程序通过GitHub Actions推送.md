---
title: Trivy漏洞扫描器泄露，信息窃取程序通过GitHub Actions推送
url: https://mp.weixin.qq.com/s/det-fCBHTpc_DrLXhJGJdg
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:21:23.266199
---

# Trivy漏洞扫描器泄露，信息窃取程序通过GitHub Actions推送

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7ObJEccbyk9d72HnQP6AcENchO3iaKWgSFXWhXAokjRyZKqptHQnqic2mlr166I6S1mKiaicemaebXVPwBle14j6StCahQSb05ib2ME/0?wx_fmt=jpeg)

# Trivy漏洞扫描器泄露，信息窃取程序通过GitHub Actions推送

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

Trivy 漏洞扫描器在供应链攻击中遭到名为 TeamPCP 的威胁行为者的入侵，该行为者通过官方版本和 GitHub Actions 分发窃取凭证的恶意软件。

Trivy 是一款流行的安全扫描器，可帮助识别容器、Kubernetes 环境、代码库和云基础设施中的漏洞、错误配置和泄露的密钥。由于开发人员和安全团队经常使用它，因此它也成为攻击者窃取敏感身份验证密钥的高价值目标。

安全研究员Paul McCarty首先披露了此次安全漏洞，他警告称 Trivy 版本 0.69.4 已被植入后门，恶意容器镜像和 GitHub 版本已发布给用户。

Socket和 Wiz的进一步分析确定，此次攻击影响了多个 GitHub Actions，几乎破坏了 trivy-action 存储库的所有版本标签。

研究人员发现，威胁行为者破坏了 Trivy 的 GitHub 构建过程，将GitHub Actions 中的**entrypoint.sh替换为**恶意版本，并在 Trivy v0.69.4 版本中发布了木马二进制文件，这两者都充当了主扫描器和相关 GitHub Actions（包括**trivy-action**和**setup-trivy）**的信息窃取程序。

攻击者滥用了已被泄露的、拥有代码库写入权限的凭证，从而发布了恶意版本。这些被泄露的凭证来自三月份早些时候的一次安全漏洞事件，当时凭证从 Trivy 的环境中被窃取，但并未完全隔离。

威胁行为者强制推送了 aquasecurity/trivy-action 存储库中的 76 个标签中的 75 个，并将它们重定向到恶意提交。

因此，任何使用受影响标签的外部工作流程都会在运行合法的 Trivy 扫描之前自动执行恶意代码，使得这种入侵难以被检测到。

Socket 报告称，信息窃取程序收集了侦察数据，并扫描了系统，寻找已知存储凭据和身份验证密钥的各种文件和位置，包括：

* **侦察数据：**主机名、whoami、uname、网络配置和环境变量
* **SSH：**私钥、公钥及相关配置文件
* **云和基础设施配置：** Git、AWS、GCP、Azure、Kubernetes 和 Docker 凭据
* **环境文件：** .env 及其相关变体
* **数据库凭证：** PostgreSQL、MySQL/MariaDB、MongoDB 和 Redis 的配置文件
* **凭证文件：**包括包管理器和 Vault 相关身份验证令牌
* **CI/CD 配置：** Terraform、Jenkins、GitLab CI 和类似文件
* **TLS 私钥**
* **VPN 配置**
* **Webhooks：** Slack 和 Discord 令牌
* **Shell 历史文件**
* **系统文件：** /etc/passwd、/etc/shadow 和身份验证日志
* **加密货币钱包**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/obqSK4blwJJ340gSE8nTd78Y2xqPibE5axW7qASPgsuojqCvJQL9myGuKTslC63icTicGtopa0TMPVjzcb3vpIrnsHqRK9utiaH1Eic2UZQLOLwA/640?from=appmsg)

恶意脚本还会扫描 GitHub Actions Runner.Worker 进程使用的内存区域，查找 JSON 字符串“ " `" <name> ":{ "value": "<secret>", "isSecret":true}`”，以查找其他身份验证密钥。

在开发者机器上，被植入木马的 Trivy 二进制文件执行类似的数据收集操作，收集环境变量，扫描本地文件中的凭据，并枚举网络接口。

**收集到的数据被加密并存储在名为tpcp.tar.gz**的存档中，然后被泄露到 scan.aquasecurtiy[.]org 的拼写错误命令和控制服务器上。

如果数据外泄失败，恶意软件会在受害者的 GitHub 账户中创建一个名为**tpcp-docs的公共存储库，并将窃取的数据上传到那里。**

为了在被入侵的设备上持续运行，该恶意软件还会向**~/.config/systemd/user/sysmon.py**投放一个 Python 有效载荷，并将其注册为 systemd 服务。该有效载荷会检查远程服务器，寻找其他可投放的有效载荷，从而使攻击者能够持续访问该设备。

据信此次攻击与名为 TeamPCP 的威胁行为者有关，因为攻击中使用的其中一个信息窃取有效载荷的 Python 脚本最后一行包含“TeamPCP Cloud stealer”注释。

Socket解释说：“该恶意软件在嵌入式文件系统凭证收集器的最后一行Python注释中将自己标识为TeamPCP Cloud stealer。TeamPCP，也被称为DeadCatx3、PCPcat和ShellForce，是一个有记录的云原生威胁行为者，以利用配置错误的Docker API、Kubernetes集群、Ray仪表板和Redis服务器而闻名。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7OW8DMf9NicBakwFoLUjHtlY3puTrVaKIYENrPeHyl6lenxnDZO3DpPe8css5cTq30icIfzxLBbusJXVzR59hNLWjODJTO8tWCXs/640?wx_fmt=png&from=appmsg)

Aqua Security 证实了这起事件，并表示有威胁行为者使用了之前未得到妥善控制的事件中泄露的凭证。

“这是对近期（2026年3月1日）凭证泄露事件的后续行动。我们对第一次事件的控制并不彻底，” Aqua Security解释道。

“我们轮换了密钥和令牌，但这个过程并非原子性的，攻击者可能已经获取了更新后的令牌。”

恶意 Trivy 版本（v0.69.4）上线约 3 小时，被入侵的 GitHub Actions 标签保持活动状态长达 12 小时。

攻击者还篡改了该项目的代码库，删除了 Aqua Security对 3 月份早些时候发生的事件的最初披露。

在事件发生期间使用受影响版本的组织应将其环境视为完全被入侵。

这包括轮换所有密钥，例如云凭证、SSH 密钥、API 令牌和数据库密码，并分析系统是否存在其他安全漏洞。

## 后续攻击通过 npm 传播 CanisterWorm。

Aikido的研究人员还将同一威胁行为者与后续活动联系起来，该活动涉及一种名为“CanisterWorm”的新型自传播蠕虫，该蠕虫的目标是 npm 包。

该蠕虫会入侵软件包，通过 systemd 用户服务安装持久后门，然后使用窃取的 npm 令牌向其他软件包发布恶意更新。

“自我传播的蠕虫。deploy.js 获取 npm 令牌，解析用户名，枚举所有可发布的包，更新补丁版本，并将有效载荷发布到整个范围内。不到 60 秒即可发布 28 个包，”Aikido 指出。

该恶意软件使用互联网计算机 (ICP) 容器进行去中心化的命令和控制机制，ICP 容器充当死信箱解析器，提供用于其他有效载荷的 URL。

使用 ICP 罐可以使行动更难被取缔，因为只有罐的控制器才能将其移除，任何阻止行动的尝试都需要治理提案和网络投票。

该蠕虫还具备从配置文件和环境变量中收集 npm 身份验证令牌的功能，使其能够在开发人员环境和 CI/CD 管道中传播。

在分析时，一些辅助有效载荷基础设施处于非活动状态或配置了无害内容，但研究人员表示，这种情况随时可能改变。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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