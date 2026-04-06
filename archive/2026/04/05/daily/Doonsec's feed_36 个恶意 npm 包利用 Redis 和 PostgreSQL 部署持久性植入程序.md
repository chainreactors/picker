---
title: 36 个恶意 npm 包利用 Redis 和 PostgreSQL 部署持久性植入程序
url: https://mp.weixin.qq.com/s/eR5dAiGZX9-atxFMh8tP0w
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:39:28.452733
---

# 36 个恶意 npm 包利用 Redis 和 PostgreSQL 部署持久性植入程序

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7Mhf6pSB6RpWxAdSY0m4GsLwBOFasiap5szB5nj0Vic0VcwRkatPYMv7AOSXeImcPxibXGShykYP4QJWibhCmjuicNCUwyA7tYiaBWPw/0?wx_fmt=jpeg)

# 36 个恶意 npm 包利用 Redis 和 PostgreSQL 部署持久性植入程序

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

网络安全研究人员在 npm 注册表中发现了 36 个恶意软件包，这些软件包伪装成 Strapi CMS 插件，但带有不同的有效载荷，可用于利用 Redis 和 PostgreSQL、部署反向 shell、收集凭据以及投放持久性植入程序。

SafeDep表示：“每个软件包都包含三个文件（package.json、index.js、postinstall.js），没有描述、存储库或主页，并使用 3.6.8 版本，以显示为成熟的 Strapi v3 社区插件。”

所有已识别的 npm 包都遵循相同的命名规则，以“strapi-plugin-”开头，后面跟着“cron”、“database”或“server”之类的短语，以此来欺骗不知情的开发者下载它们。值得注意的是，官方的 Strapi 插件位于“@strapi/”目录下。

以下列出了四个名为“umarbek1233”、“kekylf12”、“tikeqemif26”和“umar\_bektembiev1”的傀儡账号在13小时内上传的软件包 -

* strapi-plugin-cron
* strapi-plugin-config
* strapi-plugin-server
* strapi-plugin-database
* strapi-plugin-core
* strapi-plugin-hooks
* strapi-plugin-monitor
* strapi-plugin-events
* strapi-plugin-logger
* strapi-plugin-health
* strapi-plugin-sync
* strapi-plugin-seed
* strapi-plugin-locale
* strapi-plugin-form
* strapi-plugin-notify
* strapi-plugin-api
* strapi-plugin-sitemap-gen
* strapi-plugin-nordica-tools
* strapi-plugin-nordica-sync
* strapi-plugin-nordica-cms
* strapi-plugin-nordica-api
* strapi-plugin-nordica-recon
* strapi-plugin-nordica-stage
* strapi-plugin-nordica-vhost
* strapi-plugin-nordica-deep
* strapi-plugin-nordica-lite
* strapi-plugin-nordica
* strapi-plugin-finseven
* strapi-plugin-hextest
* strapi-plugin-cms-tools
* strapi-plugin-content-sync
* strapi-plugin-debug-tools
* strapi-plugin-health-check
* strapi-plugin-guardarian-ext
* strapi-plugin-advanced-uuid
* strapi-plugin-blurhash

对软件包的分析表明，恶意代码嵌入在安装后脚本钩子中，该钩子会在执行“npm install”时自动执行，无需任何用户交互。它以与安装用户相同的权限运行，这意味着它会在 CI/CD 环境和 Docker 容器中滥用 root 权限。

本次行动中分发的有效载荷的演变过程如下：

* 利用本地可访问的 Redis 实例，通过注入 crontab（即 cron 表）条目，每分钟从远程服务器下载并执行一个 shell 脚本，从而实现远程代码执行。该 shell 脚本通过 SSH 向 Strapi 的公共上传目录写入 PHP Web shell 和 Node.js 反向 shell。它还会尝试扫描磁盘以查找敏感信息（例如 Elasticsearch 和加密货币钱包的助记词），并窃取 Guardarian API 模块。
* 结合 Redis 漏洞利用和 Docker 容器逃逸，可以将 shell 有效载荷写入容器外部的主机。它还会直接在 4444 端口启动一个 Python 反向 shell，并通过 Redis 将反向 shell 触发器写入应用程序的 node\_modules 目录。
* 部署反向 shell，并通过 Redis 编写 shell 下载器，然后执行生成的文件。
* 扫描系统以查找环境变量和PostgreSQL数据库连接字符串。
* 扩展凭证收集器和侦察有效载荷，用于收集环境转储、Strapi 配置、通过运行 INFO、DBSIZE 和 KEYS 命令提取 Redis 数据库、网络拓扑映射以及 Docker/Kubernetes 密钥、加密密钥和加密货币钱包文件。
* 攻击者利用硬编码的凭据连接到目标 PostgreSQL 数据库，并查询 Strapi 特有的表以获取密钥，从而实施 PostgreSQL 数据库攻击。此外，攻击者还会导出匹配的加密货币相关模式（例如，钱包、交易、存款、取款、热币、冷币和余额），并尝试连接到六个 Guardarian 数据库。这表明攻击者已经掌握了这些数据，这些数据可能是通过先前的入侵或其他途径获得的。
* 部署一个持久性植入程序，旨在保持对特定主机名（“prod-strapi”）的远程访问。
* 通过扫描硬编码路径并生成持久反向 shell 来窃取凭证。

SafeDep 表示：“这八个有效载荷展现了一个清晰的叙事：攻击者一开始采取激进策略（Redis 远程代码执行、Docker 逃逸），发现这些方法行不通后，转向侦察和数据收集，使用硬编码凭据直接访问数据库，最终通过有针对性的凭据窃取实现持久访问。”

攻击载荷的性质，加上其针对数字资产的攻击以及使用硬编码的数据库凭证和主机名，表明此次攻击活动很可能是针对加密货币平台的定向攻击。建议已安装上述任何软件包的用户假定其账户已被入侵，并立即轮换所有凭证。

这一发现与多起针对开源生态系统的供应链攻击的发现不谋而合——

* 一个名为“ ezmtebo ”的GitHub账户已在多个开源仓库中提交了超过256个包含凭证窃取有效载荷的拉取请求。SafeDep表示：“它通过CI日志和PR评论窃取密钥，注入临时工作流来转储密钥值，自动应用标签以绕过pull\_request\_target门控，并在主脚本退出后运行后台/proc扫描器10分钟。”
* 攻击者劫持了经过验证的 GitHub 组织“ dev-protocol ”，并利用其恶意 Polymarket 交易机器人分发带有拼写错误 npm 依赖项（例如“ts-bign”和“levex-refa”或“big-number”和“lint-builder”）的恶意程序。这些机器人会窃取钱包私钥、泄露敏感文件，并在受害者的机器上打开 SSH 后门。“levex-refa”用于窃取凭证，“lint-builder”则用于安装 SSH 后门。“ts-bign”和“big-number”分别被设计为传递依赖项，以分发“levex-refa”和“lint-builder”。
* 流行的 Emacs 包“ kubernetes-el/kubernetes-el ”遭到入侵，利用其 GitHub Actions 工作流中的Pwn Request 漏洞，通过 pull\_request\_target 触发器窃取存储库的 GITHUB\_TOKEN，窃取 CI/CD 密钥，篡改存储库，并注入破坏性代码以删除几乎所有存储库文件。
* 有人利用窃取的维护者凭证入侵了合法的“ xygeni/xygeni-action ”GitHub Actions 工作流，植入了反向 shell 后门。Xygeni 已实施新的安全控制措施来应对此次事件。
* 攻击者通过账户劫持入侵了合法的 npm 包“ mgc ”，并推送了四个恶意版本（1.2.1 至 1.2.4）。这些恶意版本中包含一个投放脚本，该脚本能够检测操作系统，并从 GitHub Gist 获取特定平台的有效载荷——一个用于 Linux 的 Python 木马和一个用于 Windows 的 PowerShell 变种，名为 WAVESHAPER.V2。此次攻击与近期针对 Axios 的供应链攻击有直接的重叠之处，后者已被归因于一个被追踪为 UNC1069 的朝鲜威胁集群。
* 一个名为“ express-session-js ”的恶意 npm 包，它抢注了“express-session”的名称，并包含一个投放器，该投放器从 JSON Keeper 中检索下一阶段的远程访问木马 (RAT)，通过使用 Socket.IO 库连接到“216.126.237[.]71”来进行数据窃取和持久访问。
* 攻击者利用合法的 PyPI 软件包“ bittensor-wallet ”（版本 4.0.2）部署后门，该后门会在钱包解密操作期间触发，利用 HTTPS、DNS 隧道和原始 TLS 作为泄露通道，将钱包密钥泄露到硬编码的域或使用域名生成算法 (DGA) 创建的、每日轮换的域。
* 一个名为“ pyronut ”的恶意PyPI软件包，通过抢注流行的Python Telegram API框架“pyrogram”的域名，嵌入了一个隐蔽的后门。该后门会在每次Telegram客户端启动时触发，从而控制Telegram会话和底层主机系统。Endor Labs表示：“该后门会注册隐藏的Telegram消息处理程序，允许两个硬编码的攻击者控制账户在受害者的机器上执行任意Python代码（通过/e命令和meval库）以及任意shell命令（通过/shell命令和subprocess）。”
* 由“ IoliteLabs ”发布的三款恶意 Microsoft Visual Studio Code (VS Code) 扩展程序——“solidity-macos”、“solidity-windows”和“solidity-linux”——最初自 2018 年以来一直处于休眠状态，但在 2026 年 3 月 25 日进行了更新，在应用程序启动时会启动一个针对 Windows 和 macOS 系统的多阶段后门程序，以建立持久性。在被移除之前，这些扩展程序总共被安装了 27,500 次。
* Open VSX 上的多个“ KhangNghiem/fast-draft ”VS Code扩展（0.10.89、0.10.105、0.10.106 和 0.10.112）会执行一个托管在 GitHub 上的下载器，从 GitHub 仓库部署第二阶段的 Socket.IO RAT、信息窃取程序、文件窃取模块和剪贴板监控程序。值得注意的是，0.10.88、0.10.111 和 0.10.129-135 版本未被发现。“这并非单个被入侵版本或维护者完全转向恶意行为时所预期的发布模式，”Aikido 表示，“这看起来更像是两个相互竞争的发布流共享同一个发布者身份。”

Group-IB 在 2026 年 2 月发布的一份报告中指出，软件供应链攻击已成为“重塑全球网络威胁格局的主导力量”，并补充说，威胁行为者正在攻击受信任的供应商、开源软件、SaaS 平台、浏览器扩展程序和托管服务提供商，以获得对数百个下游组织的继承访问权限。

供应链威胁可以迅速将一次局部入侵升级为具有大规模、跨境影响的事件，攻击者将供应链破坏产业化，并将其变成一个“自我强化”的生态系统，因为它具有覆盖范围广、速度快、隐蔽性强的特点。

Group-IB表示： “像npm和PyPI这样的软件包仓库已经成为主要攻击目标，被盗的维护者凭证和自动化的恶意软件蠕虫会入侵广泛使用的库，从而将开发流程变成恶意代码的大规模分发渠道。”

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