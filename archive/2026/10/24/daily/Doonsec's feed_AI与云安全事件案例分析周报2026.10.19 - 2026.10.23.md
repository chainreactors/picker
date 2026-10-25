---
title: AI与云安全事件案例分析周报2026.10.19 - 2026.10.23
url: https://mp.weixin.qq.com/s/s5wUGKAeBaNSUTPUuAw1Lw
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:09:28.045193
---

# AI与云安全事件案例分析周报2026.10.19 - 2026.10.23

# AI与云安全事件案例分析周报2026.10.19 - 2026.10.23

原创

星云实验室
星云实验室

绿盟科技研究通讯

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/mAopIKtZvYsQ7cYMhmPlciaVcsk7J8KpxnL8GgXVJ5St6qxg56cTb1nH6aanSx9qEvHhDOL0RlgrtuSFMDknmxpsb85yCOojbopp0ib0iaZjwI/640?wx_fmt=gif&from=appmsg)

AI 串起 PHP 旧缺陷与多云攻击链，发布签名、供应商信任和模型账单接连承压。

事件一 PHP2Shell 无需登录即可远程执行：AI 串起十余年旧缺陷，网站代码没错也可能失守

1.1

事件简介

* 涉及组织与应用：PHP 是大量网站使用的服务器端运行环境，PHP 项目发布补丁，Wiz、Calif 等参与漏洞研究与协调，云服务商则提供攻击观测和临时防护。
* 事件概述：Wiz 等研究方披露，PHP 在一次请求因内存不足异常结束后，可能留下指向已释放内存的内部记录。后续请求复用同一工作进程时，便可能把无效数据当成正常状态，导致其他请求的秘密被读出，或执行攻击者的代码。研究者利用 AI 辅助分析和调试，在常见网站容器中验证了无需登录的利用链。PHP 已发布修复；Cloudflare 报告看到攻击流量，Amazon 的蜜罐也记录了补丁前尝试。网站自身代码没有漏洞，仍可能因底层运行环境受影响。
* 事件时间：2026-10-21 PHP 紧急发布补丁；10-22 的运行时分析补充检测建议。Amazon 报告的蜜罐尝试发生于 10-17，不改写为已确认受害事件。
* 事件链接：

+ https://www.php.net/archive/2026.php#2026-10-21-5

+ https://www.wiz.io/blog/php2shell-php-rce

+ https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/

+ https://blog.cloudflare.com/php-vulnerabilities-waf-protection/

+ https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/

+ https://www.sysdig.com/blog/php2shell-cve-2026-109618-and-cve-2026-109619-detecting-unauthenticated-remote-code-execution-in-php-core

* 影响范围：

+ CVE-2026-109618、CVE-2026-109619；应升级至 PHP 8.5.12、8.4.27、8.3.36、8.2.35 或对应分支的后续安全版，发行版回补应按其公告核对。

+ 影响处理 Web 请求的 PHP 部署；实际利用条件随版本、接口和内存布局变化。WordPress、Drupal、Joomla 是研究验证目标，不是唯一受影响应用。

+ “约七成网站使用 PHP”不是“七成网站已被入侵”，更不是每个部署都已验证可用同一脚本攻破。

* 技术分类归属：基础设施层 / 应用运行时 / Agent辅助漏洞研究
* 事件标签：云AI融合

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYuoq3ZHm6RUoCGEnrfiaPIoS6OFiawuWjydsdiaXLavp7YoLnHzDa9EUicq4OmdOaqeBngxbVbmJJcWm3NV445caZtvO2vozUfCZ9g/640?wx_fmt=png&from=appmsg)

图1：Wiz 的原始攻击路径图展示：特制 HTTP 请求触发底层 PHP 内存缺陷，并在 WordPress、Drupal、Joomla 研究环境中实现远程代码执行。它说明问题来自共同运行时，不能证明所有同类网站均能被同一载荷攻破，也不代表三类网站均已有生产失陷。来源：https://www.wiz.io/blog/php2shell-php-rce

1.2

事件背景与回顾

* 架构形态：PHP worker 可连续处理不同请求；正常隔离要求每次请求结束后清理相关状态。漏洞使请求已释放的内存仍被后续处理逻辑引用。
* 验证路径：特制请求进入上传或错误处理逻辑 → 内存分配失败中断初始化 → 清理不完整留下失效状态 → 同一或相关 worker 后续复用 → 内存泄露或内存破坏 → 研究环境验证远程代码执行。
* AI 与云关联：研究方明确使用模型辅助发现、构造和适配复杂利用链；攻击面则是云主机、托管站点及容器中的 PHP 运行时，不是模型本体被攻破。

1.3

事件根因深度分析

* 基础设施与云配置错误：根因位于运行时内存生命周期，不要求云 IAM 配错；若被入侵 worker 还能读取高权限云身份或数据库秘密，影响才会继续扩大。
* AI 供应链与存储缺陷：修复网站应用而不重建其 PHP 基础镜像，会留下底层漏洞；更新镜像标签也不保证旧容器或旧 worker 已退出。
* 前沿算法/工程逻辑缺陷：请求异常中止没有完整撤销已发布的全局状态，使前一请求的无效内存跨越到后一请求。多条变体表明只封堵单一功能开关不足以替代引擎修复。
* 复合依赖与应急响应缺陷：WAF 可争取时间，但原站直连、不同触发变体及旧进程都会影响覆盖；攻击流量、成功读取和成功执行应分别取证。
* 边界防御与分层隔离缺陷：部分处理发生在应用认证逻辑之前，登录保护不构成充分防线；运行时身份与容器权限仍应按最小范围设置。

1.4

VERIZON DBIR 事件分类

System Intrusion（系统入侵）潜在及已尝试路径：公开材料同时包含实验利用和野外攻击流量，不据此推算真实失陷规模。

1.5

攻击路径与 MITRE ATT&CK 技术映射

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYvBXf2dBvUsDxEZqj0oKicApJW2nMnwGqGsPEX2xUVVUQ0Np63KMsDQg8szDiazF6vrktkO7ZnBKcYYa7Y4Evzib1Ucg3iaew2NkM0/640?wx_fmt=png&from=appmsg)

1.6

防御启示

* 更新 PHP 或采用厂商明确回补的软件包，重建镜像、滚动替换容器并重启所有 worker；同时核对实际 Web 运行环境，而非只检查命令行版本。
* 联查异常上传、内存错误、worker 崩溃及随后产生的 shell 或外联；没有 shell 不足以排除独立的内存泄露。
* 按官方公告临时收紧请求处理和功能配置，并评估业务影响；不把降低内存限制或单一 WAF 规则当作完整修复。

事件二 LiteLLM 官方发布链遭投毒：1.107.0 窃取云与模型密钥，合法签名也没能拦住

2.1

事件简介

* 涉及组织与应用：LiteLLM 是统一接入多家模型 API 的开源网关，GitHub 承载其代码与发布审批，PyPI 和容器仓库分发安装包，维护方与 Wiz 分别披露发布链和恶意载荷分析。
* 事件概述：攻击者身份未归属。LiteLLM 披露，攻击者持有三名开发者的 GitHub 命令行授权令牌，利用其中的组织管理权限绕过分支保护，再让官方发布任务从名称相近的恶意仓库构建代码。正常签名与发布步骤随后把含窃密程序的 1.107.0 送入软件包和容器仓库。受影响环境启动 Python 时，恶意模块便会收集云和模型服务密钥。维护方认为令牌可能来自内部模型网关日志，但最初如何进入该网关仍未确认；不能把怀疑的漏洞入口写成定论。
* 事件时间：2026-10-21 投毒和下架；10-22 的研究更新补充下载量与云凭据被后续使用的证据。下文时间均为 UTC。
* 事件链接：

+ https://docs.litellm.ai/blog/security-incident-oct-21-2026

+ https://github.com/BerriAI/litellm/issues/47826

+ https://www.wiz.io/blog/litellm-compromised-steals-credentials

* 影响范围：

+ PyPI 的 litellm==1.107.0 七个 wheel，厂商给出的分发窗口为 11:39:51—13:23；Docker Hub 受影响标签为 v1.107.0、latest、main-latest、main-stable，窗口为 11:46:56—14:20；GHCR 同类产物也受影响。

+ 官方 Git 源码标签不含恶意文件，不能只检查源码标签就排除已安装二进制包或容器的风险；厂商称私有企业发布通道未受影响。

+ Wiz 引用的约 49,000 次下载不是独立受害者数量；其另观测到失窃 AWS 身份被验证并查询模型服务，不能把所有下载都写成成功入侵。

* 技术分类归属：应用层 / AI供应链 / CI/CD / 云身份与凭据管理
* 事件标签：云AI融合

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mAopIKtZvYsiaYcJyZjlTibY8iafhYdwEeeL7qOqycfZENrbcBdmrJJ6kNOfRFTo1GtluRP4WmPmTK1vWNaS7yXPHJGEI29rGQbfPKicWC8Shia4/640?wx_fmt=png&from=appmsg)

图2：Wiz 原始 SVG 按其 16:9 画布渲染为 PNG，未改写内容；左侧是 Python 启动即执行的凭据收集与外传，右侧是周期检查地址并加载代码的能力。原图明确标注右侧远程执行当时未观察到激活，不能据此认定所有分支均已实战运行。图中仅含公开恶意样本的固定 IOC 和代码片段，没有客户密钥。来源：https://www.wiz.io/blog/litellm-compromised-steals-credentials

2.2

事件背景与回顾

* 与历史事件的关系：W37、W42 已分析 LiteLLM 的认证、路由与凭据风险。本次是新的发布产物投毒事件，不能直接认定由那些 CVE 引发，也不能将旧版本“未被本次投毒”理解为没有其他漏洞。
* 攻击路径：被盗开发者令牌 → 组织所有者权限绕过保护 → 修改发布源为 Berri-AI/litellm → 官方工作流构建、审批、签名并分发 → Python 启动钩子加载窃密代码 → 凭据外传 → 部分云身份被后续滥用。
* 载荷机制：cook.pth 加载 cook.py 执行窃密；sitecustomize.py 设置远程载荷加载能力。Wiz 当时未观察到后者的动态二阶段地址投入实际使用，须与已执行窃密分开。

2.3

事件根因深度分析

* 基础设施与云配置错误：内部 LiteLLM 部署可被公网访问；维护方发现异常账户，但初始认证或漏洞利用路径尚未坐实。应将已确认的发布权限滥用与待确认入口分开处置。
* AI 供应链与存储缺陷：维护方称特定情形下 Claude Code 的响应会包含 GitHub CLI 令牌，若网关记录响应就可能保存秘密；这说明模型调用日志也是凭据资产，而非只有提示词分析价值。
* 前沿算法/工程逻辑缺陷：正常发布任务接受被改写的构建来源，合法签名证明产物经过该流程，却无法证明输入代码可信；源码、构建来源、产物摘要必须绑定核对。
* 复合依赖与应急响应缺陷：临时扩大发布权限叠加多组被盗令牌，使构建与审批的身份分离未能阻止攻击；撤销源头令牌也不会自动撤销已经从下游环境偷走的密钥。
* 边界防御与分层隔离缺陷：模型网关进程可触及多家供应商凭据，载荷还读取云身份和本机配置。运行身份权限、凭据可见范围及外联限制决定实际损失上限。

2.4

VERIZON DBIR 事件分类

System Intrusion（系统入侵）：开发者有效凭据被滥用后污染官方分发链，继而窃取下游环境秘密。

2.5

攻击路径与 MITRE ATT&CK 技术映射

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mAopIKtZvYvP1tN1gEcRsyo1Pyb51HonPMTvrLp0nTwJMkMdkw0KUd1wGKeC9Vglia2KPee12hUfqZz2tLsjcSBWicpgCFFdCSNvxtcibNLYFI/640?wx_fmt=png&from=appmsg)

2.6

防御启示

* 先隔离受影响环境并保留证据，再从可信环境重建；维护方特别提醒，不应先在受污染环境直接启动 pip，以免再次触发 Python 启动钩子。
* 按镜像摘要、实际安装产物和分发时间排查，清查缓存及 CI runner；在未受污染环境轮换该进程可访问的云、数据库和模型服务密钥。
* 固定构建仓库与提交、限制组织管理员绕过发布保护的能力，对日志中的授权令牌做检测与脱敏；人工审批还须核对构建来源。

事件三 ARTEX 借 ConnectWise 凭据进入下游云租户：AI 把供应商信任变成批量攻击通道

3.1

事件简介

* 涉及组织与应用：ConnectWise 为服务商和企业提供云备份及管理工具，Microsoft 365 是企业邮件与协作平台，ARTEX 是可调用大模型规划并执行渗透任务的工具，Microsoft 与 Wiz 披露其在真实攻击中的使用。
* 事件概述：攻击者利用 ARTEX 加速扫描、密码喷洒和应用身份滥用，随后借被盗的 ConnectWise 云应用凭据进入已经信任这些应用的客户租户。租户可理解为企业独立的云服务空间，应用凭据则让程序无需人员交互登录就能调用接口。部分环境出现目录侦察、应用凭据和权限变更，带来持续访问风险；但应用被安装、登录成功与客户数据被窃取，分别需要证据，不能合并统计。
* 事件时间：活动最早追溯至 2026 年 9 月；ConnectWise 10-16 首次公告；Microsoft 10-21、Wiz 10-22 发布归因、攻击链与调查增量。
* 事件链接：

+ https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/

+ https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors

+ https://www.huntress.com/blog/vendor-credential-enables-unauthorized-access

+ https://www.connectwise.com/contentassets/10777cd3364d440c86ed5270a94a5f24/connectwise-cloud-backup-technical-investigation-and-remediation-guide-1.pdf

* 影响范围：

+ Microsoft 报告下游登录尝试涉及超过 2,250 个租户；这是触达范围，不能写成同等数量的租户失陷。

+ 另一组密码喷洒遥测涉及 8 个组织、327 个账户、超过 151,000 次失败登录；该组活动未观察到成功认证，不能与应用凭据滥用后的成功路径混算。

+ Wiz 在多个 IT 与软件供应商环境发现相似基础设施、工具和攻击模式；工具相同本身不能证明所有事件属于同一操作者。

* 技术分类归属：Agent层 / 云身份层 / SaaS供应链 / 数据层
* 事件标签：云AI融合

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mAopIKtZvYvRBQ7F6uicnia7jBeobyYLpqshLIGjf9brXxd6rtahPicepiaPH5gPWJRxg4F8zfpjkajpib1ut22LdBVibth4dwX1xicVWlwqiaibsqlM/640?wx_fmt=png&from=appmsg)

图3：Microsoft 将超过 2,250 个租户的应用登录触达、8 个组织的 327 个密码喷洒目标账户，以及超过 151,000 次失败登录放在同一信息图中，说明活动覆盖与速度；这些是不同子活动的口径，不能相加或当作已泄露人数。该密码喷洒组未观察到成功认证，图中的租户触达也不等于客户数据已被读取。来源：https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/

3.2

事件背景与回顾

* 前周事件增量更新：W40—W41 合刊已分析 ARTEX 在韩国金融机构外围系统攻击中的使用。本期新增 Microsoft 的特定活动归因、ConnectWise 供应链入口与下游身份变更证据；不将韩国案例追溯归于 Storm-0940。
* 攻击路径：供应商应用认证材料失窃 → 使用客户早已授予的信任关系登录 → Microsoft Graph 侦察 → 添加应用凭据或调整角色 → 即使原供应商应用被停用，新增身份仍可能留下访问路径。
* 处置边界：ConnectWise 官方指南明确，供应商侧停用应用和撤销凭据不等于各客户租户的本地配置已清理；指南完成也不代表可自行恢复连接。

3.3

事件根因深度分析

* 基础设施与云配置错误：应用既有权限和租户授权把供应商认证材料转化为客户云内的访问能力；本案不应写成 Microsoft 云底层被攻破。
* AI 供应链与存储缺陷：供应链风险来自托管应用身份，而不要求客户安装恶意更新。盘点范围应包含已停用业务但仍保留授权的旧应用。
* 前沿算法/工程逻辑缺陷：ARTEX 加速多个攻击分支的验证与反馈，但突破边界的仍是凭据、权限和应用信任；公开证据不足以把全部活动描述为完全无人操作。
* 复合依赖与应急响应缺陷：只轮换供应商密钥可能留下攻击者新加的凭据、角色与授权；必须把登录之...