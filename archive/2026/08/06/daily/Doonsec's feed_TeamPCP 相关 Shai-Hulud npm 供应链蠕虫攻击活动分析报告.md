---
title: TeamPCP 相关 Shai-Hulud npm 供应链蠕虫攻击活动分析报告
url: https://mp.weixin.qq.com/s/7AVSqfRG3LVddO0voZEZkQ
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:22:55.411384
---

# TeamPCP 相关 Shai-Hulud npm 供应链蠕虫攻击活动分析报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Emmib7pWXrXKF6Stv93A9DyUaQ8zpOhT7BprsFHsKmA6CPicDjtqR78vJldrHFJmugbsUSEQKpUh07AM0fJ9joxN9bvccQ8elMaPmdFH5b2r0/0?wx_fmt=jpeg)

# TeamPCP 相关 Shai-Hulud npm 供应链蠕虫攻击活动分析报告

高级威胁研究院
高级威胁研究院

360威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**一、概述**

2026 年 8 月 4 日，一场代号为 Shai-Hulud（源自载荷中外传仓库描述 "Shai-Hulud: Here We Go Again"）的大规模 npm 供应链蠕虫攻击被发现。

攻击者控制或滥用 keyv 包维护者 jaredwray 的 GitHub 账户，向 keyv 的 main 分支推送恶意代码，并通过 GitHub Actions 可信发布流程将 keyv@6.0.0 发布到 npm 注册表。该包在安装时通过 preinstall 钩子静默执行一条多阶段攻击链，集凭证窃取、蠕虫自传播、GitHub 仓库感染和Dead Man's Switch于一体。360已监测到部分受影响用户，主要涉及安装或使用了相关受影响版本的开发者终端和构建环境。

本次攻击是 2026 年 5 月 11 日 TanStack 事件中 Shai-Hulud 行动的延续与升级，显示出攻击者在过去三个月内持续增强其能力。FBI 于 2026 年 7 月 2 日已发布 FLASH-20260702-01 预警，明确将 Shai-Hulud 相关恶意软件归入网络犯罪组织 TeamPCP 的武器库。

TeamPCP组织是一个以供应链攻击为核心战术的组织，已实施了多起协调有序的攻击行动。TeamPCP 擅长通过污染广泛使用的开源工具来投递恶意载荷。历史上，其曾成功入侵 Trivy（容器漏洞扫描工具）、KICS（基础设施即代码安全扫描工具）以及 LiteLLM（大语言模型 API 代理工具）等知名开源项目，并利用这些受信任的软件渠道部署凭证窃取类恶意软件。

此次事件已从最初的少量核心包迅速扩散至数百个包、上千个版本，影响范围覆盖高下载量开源依赖、开发者工作站、构建系统和云资源，属于一次兼具入侵、窃密、传播和持久化能力的典型开源供应链攻击。

**二、攻击活动分析**

## 1.攻击流程分析

攻击者控制维护者的 GitHub 账户或发布链路，向keyv仓库写入恶意提交，并借助 GitHub Actions的可信发布流程，将带有效 SLSA provenance 的恶意版本发布到 npm。受害者在允许lifecycle scripts 的环境中安装受影响版本，package.json 中的 preinstall 自动触发 node setup.mjs。

setup.mjs 先检查本机是否已有 Bun，若没有则从 GitHub 官方 Bun release下载对应平台版本，再解压并启动第二阶段。若本机已安装 Bun，则直接复用。第二阶段JS在 Bun 下运行，进入后台，建立单实例锁，并在非 CI 环境下 detach 自身，尽量减少安装过程中的可见痕迹。载荷系统性收集文件系统、环境变量、SSH、npm、GitHub CLI、GitHub token、AWS、GCP、Azure、Kubernetes、Vault，以及 GitHub Actions runner 内存中的秘密信息。主通道先通过以太坊合约解析可用的 C2 域名，再经 HTTPS /router 发送加密结果。若 C2 返回 code，载荷会在 Bun 进程中直接 eval，形成远程代码执行能力。若主通道不可用，则退回到 GitHub dead-drop 仓库，仓库描述为 Shai-Hulud: Here We Go Again。

一旦拿到 npm token，载荷就枚举该 token 可写的所有包，复制第二阶段载荷与加载器，重写scripts.preinstall，提升 patch 版本，再直接发布，从而把同一恶意链条扩散到其他包。如果拿到 GitHub 凭据，载荷会向可写分支写入 .claude/settings.json、.claude/math\_init.js、.claude/setup.mjs、.vscode/tasks.json、.vscode/setup.mjs 等文件，让开发者打开仓库或启动 Claude code/ VS Code时再次触发。

在具备 workflow scope 的 GitHub token 下，载荷会创建临时分支、注入 workflow，并把 secrets 导出到 artifact；在特定 trusted-publishing 场景中，还会借助 OIDC 和 Sigstore 生成看似合法的 SLSA provenance。SafeDep 确认该样本还包含 token-monitor / dead-man's switch，持续轮询 api.github.com/user，当token 被撤销时触发 handler。

下面是该事件时间线整理。

| 时间 (2026-08-04 UTC) | 事件 |
| --- | --- |
| 09:02:37 | 提交 ee2681a9（未签名）：release: v6.0.0，添加 setup.mjs + Math\_Symbol.js |
| 09:04:30 | 提交 d8c850c7（GitHub 已验证，伪造为 github-actions[bot]）：添加 IDE 钩子文件 |
| 09:23:50 | 提交 f97eabcd（未签名）：删除 preinstall.test.ts（清理痕迹） |
| 09:30–09:32 | @keyv/\* 作用域包发布 6.0.0 tarball（不含 preinstall 钩子但可疑） |
| ~09:35 | keyv@6.0.0 发布 — 第一个携带恶意 preinstall 钩子的版本 |
| ~09:38 | @thiennq/docs-viewer@1.6.2 发布（蠕虫已扩散至命名空间外） |
| 09:39:45 | 向所有 @keyv/\* 包添加 setup.mjs 和 Math\_Symbol.js |
| 10:09–10:14 | cacheable 家族集中爆发（9 个包） |
| 10:12–10:18+ | @hubsync/web-sdk-react 爆发开始 |
| 10:19–10:20 | 48 个 @ornikar 包名、117 个版本，约每秒 1 次发布 |
| 10:32–10:46 | 集中爆发：@arv-bedrock、@deliveroo、@picsart、@onereach/@or-sdk、@servicetitan、@qlik |
| 13:18 | Umacloud（比集中爆发晚 2.5 小时） |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXI0icLmnIwXFEDLojl8Biarb6fUsoDnKICTm5xJ63YvggjYtlX5AKPR0Z1umwo23JOfcRgWib4Mpl9QJpic0U3yj1icsHU03borKrpA/640?wx_fmt=png)

图 1 流程图

## 2.攻击组件分析

我们以keyv@6.0.0作为示例分析。npm install keyv@6.0.0（或将其作为依赖安装）时，npm 自动执行 package.json 中定义的 preinstall 脚本："preinstall": "node setup.mjs"

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXJxXULmW4xO5cXm5BtRboo98YO3eTvf84W0ksghhdrPa73ZSod6eOE3ZO7MIUQggyZEHfoWp0rRwoic5onYpRCWpic8B3hmOLeUQ/640?wx_fmt=png)

图 2 脚本示例

setup.mjs 是obfuscator.io 风格混淆脚本。setup.mjs 是第一阶段加载器，用于准备 Bun 运行环境并拉起第二阶段载荷。脚本先判断系统 PATH 中是否已有 Bun；若不存在，则根据操作系统、CPU 架构及 musl/Alpine 环境下载对应的 Bun 压缩包到 bun-dl-\* 临时目录。随后脚本优先调用系统 unzip 解压，Windows 环境可使用 PowerShell Expand-Archive，必要时回退到内置 JS ZIP 解析逻辑。Bun 准备完成后，脚本通过 execFileSync执行第二阶段载荷，执行结束后删除临时目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXKzzP5xPEPlVW5xGT1libAyrQiaFGGuaibXEuOhibS9IZEDE7ibCNiaSf6JYI6rGSM1UnncRawn02ofXJSwBkj7fbBxUiag0IbphCEnicM/640?wx_fmt=png)

图 3 setup.mjs代码示例

第二阶段载荷(Math\_Symbol.js)经过多层混淆和加密。该载荷经过Base91 字符串表、控制流平坦化、PBKDF2-HMAC-SHA256 和 AES-256-GCM等多层混淆/加密处理，解密后包含凭证收集、加密外传、npm自传播和可信发布滥用等模块，可窃取本地、CI/CD、云平台与代码仓库凭据，并利用有效 npm/GitHub凭据继续污染其他包和仓库。

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXK0sEtSk5PUTXiavsGUcolUDl4KsyD8ibar7BJibeT2WWG6MxQwaC0rpia7uvFR7nWib5oicSTuLl5Zh18hzmLJey2txr9rlYr5HYwYQ/640?wx_fmt=png)

图 4 二阶段载荷混淆加密代码示例

C2 与外传组件不硬编码固定域名，而是通过以太坊合约动态获取 C2 地址，并向 /router 路径发送加密的凭证数据。主通道不可用时，载荷会使用 GitHub publicrepository 作为 dead-drop，仓库描述包含 Shai-Hulud: Here We Go Again，并将加密结果写入 results/目录。该机制依赖 GitHub 和公共 Ethereum RPC 等合法基础设施，提高了通信通道的隐蔽性和抗封禁能力。

在传播阶段，载荷会利用窃取到的 npm token 验证其是否具备 bypass\_2fa 和包写入权限，并枚举该 token可发布的包。随后下载目标包最新 tarball，注入 setup.mjs 与 math\_init.js，将 package.json 改写为preinstall: node setup.mjs，递增 patch 版本后重新打包并发布至 npm registry，从而使一个高权限 token能够污染维护者名下多个包，推动恶意载荷在 npm 命名空间内快速扩散。

同时，载荷还会利用 GitHub 凭据感染代码仓库。其会枚举可访问仓库及分支，跳过 dependabot/\* 和copilot/\* 分支，并提交 .claude 与 .vscode 相关钩子文件，使开发者在打开仓库或启动 Claude Code会话时再次执行加载器。相关提交伪装为 chore: update config，并可包含 Co-authored-by: claude，以降低异常配置变更的可见性。

在获取具备 workflow 权限的 GitHub token 后，载荷还会创建临时分支并注入 GitHub Actions workflow，将${{ toJSON(secrets) }} 写入 artifact 后取回，从而获取仓库或组织级 Actions secrets。回收的npm、GitHub 或云平台凭据会重新进入收集和传播流程，形成递归扩散。

此外，样本还包含 token-monitor/dead-man's switch 机制。该组件会在 ~/.config/gh-token-monitor/中保存 token、handler 和启动时间，并通过 macOS LaunchAgent 或 Linux systemd user service持久化。其每 60 秒请求 api.github.com/user 检查 token 状态，若 token 被撤销并返回 HTTP4xx，则执行攻击者配置的 handler；组件约 24 小时后清理状态文件并退出。

**三、归属研判**

FBI 于 2026 年 7 月 2 日发布的 FLASH-20260702-01 警告[1]中，明确将网络犯罪组织 TeamPCP（又名 PCPcat、ShellForce、DeadCatx3）与 Shai-Hulud 活动关联，并在其恶意软件工具集中列出 Mini Shai-Hulud 和 Miasma等与 Shai-Hulud 相关的自复制、跨生态供应链蠕虫能力。并且该警告报告与本次攻击活动之间存在直接 IOC 重叠-29ac906c8bd801dfe1cb39596197df49f80fff2270b3e7fbab52278c24e4f1a7。同时，经过披露的样本比对，存在高度相似性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXJxL2AdkdJticbEcJJfsKLiaXX8bPNiaahibSDpibQAf2dj3rtmoe8Q6NhIw5QSMkqr6Raf4Cu2jW8hwQB2rQydQFmqcQPbt9noJb7I/640?wx_fmt=png&from=appmsg)

图 5 本次攻击活动样本代码(左)与FBI警告报告中披露的样本代码(右)对比图

综合现有证据，本次 keyv/cacheable npm 供应链攻击可高置信归入 TeamPCP 相关 Shai-Hulud活动。

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXLLVWx96KVpy9p3ibBxRzEzcLD9dQAJhnsR1hRKXzgTN0YTr1lPia5jauSSqKpW4gWwTciaHAqhy8IiclTJZH4wQr1H269F7ZT1y2I/640?wx_fmt=png&from=appmsg)

防范排查建议

针对本次 npm 供应链攻击，建议：

1、从依赖侧排查是否安装过受影响版本，重点检查 package-lock.json、pnpm-lock.yaml、yarn.lock、npm cache 和 node\_modules 中是否存在 keyv@6.0.0、cacheable、flat-cache、file-entry-cache 等已披露恶意版本。

2、对CI/CD环境和开发者终端，应重点搜索 setup.mjs、Math\_Symbol.js、math\_init.js、.claude/settings.json、.vscode/tasks.json、.github/workflows/codeql\_analysis.yml、format-results.txt 等可疑文件。

3、长期防护方面，建议在 CI 中默认使用 npm ci --ignore-scripts  或按需白名单允许生命周期脚本，避免新发布版本立即进入生产或构建环境；对 npm token、GitHub PAT  和云凭据实施最小权限、短周期轮换和分环境隔离；GitHub Actions 应固定第三方 action 的 commit SHA，限制workflow 权限，并定期审查 OIDC trusted publishing 配置。

4、建议用户安装并开启360安全卫士，保持实时防护、木马查杀、下载防护、漏洞修复和可疑脚本行为拦截能力处于开启状态。对于开发者终端，360安全卫士可作为基础终端安全防护手段，配合企业 EDR、代码仓库审计和凭据轮换流程使用，提升对恶意脚本、异常进程和可疑文件落地行为的发现能力。

**参考链接**

[1].https://www.ic3.gov/CSA/2026/260702.pdf

**附录 IOC**

f92ee93a0af971a3966bfa8efa9c2625

4140f7e17e6f97f83aa3472473e01add

7bcf8d9f6834c44450eac145a967d2f2

dbb9b09957113463bbeb420c2c4108b5

00ca0c04d247ef09f2b2acc452029345

930553e362f99aa05d217ccaa68e9719

db189867d98264bdce58eae5b1f72df4

3a184af1cdf87456eeeb77e1b598af9a

632f2228c7fdb566a041a32968722cb8

setup.mjs

Math\_Symbol.js

math\_init.js

0xE1f2395ee43e45A1556EC6438a88c31B83493103

https://npm-cache.com:443/router

**360****高级威胁研究院**

360高级威胁研究院是360数字安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

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