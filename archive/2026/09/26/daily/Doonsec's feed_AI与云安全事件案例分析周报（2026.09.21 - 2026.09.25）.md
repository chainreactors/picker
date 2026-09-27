---
title: AI与云安全事件案例分析周报（2026.09.21 - 2026.09.25）
url: https://mp.weixin.qq.com/s/VP8pMe6zWlKF1aC2lkt-gw
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:21:39.550694
---

# AI与云安全事件案例分析周报（2026.09.21 - 2026.09.25）

# AI与云安全事件案例分析周报（2026.09.21 - 2026.09.25）

原创

星云实验室
星云实验室

绿盟科技研究通讯

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/mAopIKtZvYt132lAFxxqhknXiaxtcqdADvBLzGFkQoxJGzjMkvwEfe7q5XlsreuaLZCr7ydICogCEw0CaPVYnicFO1ulXrIAJibj5yAqJy0iae8/640?wx_fmt=gif&from=appmsg)

本周风险集中在 AI Agent 规模化入侵与非预期越权、Agent 驱动的云原生后渗透、云身份令牌窃取及长期机器凭据暴露。

事件一 Strix、Cairn、Hermes 三套 AI Agent 低成本攻陷在线零售商：119 个站点被植入支付卡窃取脚本

事件简介

* 涉及组织与应用：Gambit 是取得攻击者暂存服务器并复盘行动的安全研究公司；Strix、Cairn 和 Hermes 是被攻击者组合使用的开源 AI 渗透与编排框架，在线零售商、自建电商系统、Magento、Kubernetes、AWS Secrets Manager 与 CDN 则构成被攻击的应用和云资产链路。
* 事件概述：攻击者身份未公开，疑似为中文使用者。攻击者把 Strix 用于扫描、Cairn 用于持续尝试取得 Shell 或后台权限，再由 Hermes 保存技能、调度任务并指导清痕和支付卡窃取。研究人员从攻击者服务器取得会话、日志和数据，确认至少 119 个网站被植入网页 skimmer（在结账页截取支付信息的恶意脚本），两家企业共泄露超过 60 万条仍有效卡记录；AI 服务成本平均约每个目标 25 美元。
* 事件时间：活动至少自 2026 年 7 月持续；Gambit 于 9 月 22 日发布研究，9 月 23 日媒体集中报道，披露时行动仍在继续。
* 事件链接：

+ https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company

+ https://www.bleepingcomputer.com/news/security/malicious-ai-agents-steal-600k-credit-cards-infect-100-plus-sites-with-skimmers/

* 影响范围：

+ 8 月 23—31 日，Strix 对 138 个主机运行 146 次深度扫描，累计 633 小时扫描时间。

+ 9 月 10—15 日，攻击者发起 105 个 Cairn 攻击项目；研究人员可复核其中 48 个，其余 57 个已被删除。

+ 至少 119 个网站关联同一支付卡 skimmer；研究材料点名的行业包括酒店、航空、工业用品、服装和零售。

+ 一条完整链路从未认证 SQL 注入、读取 OTP、后台登录和文件上传发展到主机 root、NFS 横移、AWS Secrets Manager 导出、Aurora/Magento 数据库访问和支付卡解密。

+ 攻击者在部分受害库执行“导出后清空”，造成取证证据和业务数据同时损失；公开材料未列出全部受害企业名称。

* 技术分类归属：基础设施层 / 数据层 / 应用层 / 编排层 / Agent层 / Loop Engineering
* 事件标签：云AI融合

事件背景与回顾

* 架构形态：人工操作员只给出“扫描高危”“尝试 RCE”“取得后台”等短指令，AI 框架负责持续探测、修改战术、保存经验并把成功路径交给下一阶段；OpenRouter 提供模型访问，目标侧横跨 Web 应用、容器、数据库、云密钥库与前端内容分发。
* 攻击路径：批量筛选自建电商目标 → Strix 扫描并生成漏洞报告 → Cairn 围绕 Shell 或管理员权限长时间试探 → Hermes 调度后渗透与持久化 → 取得云密钥、数据库和结账页写权限 → 注入 skimmer、导出卡数据并清痕。
* 证据边界：研究方交叉验证了服务器文件、访问令牌和 Agent 日志，但数据规模较大，分析仍处早期。

  ![](https://mmbiz.qpic.cn/mmbiz_jpg/mAopIKtZvYu8g5YEibaqHPXSGGCRX9yiaKYLwBTvo8F2R0rjtBTUsxeAZ11pFT4IF2WdYME3blR7PDEicVm03W1druSTLaEoFYhr09adQ9iahPs/640?wx_fmt=jpeg&from=appmsg)

图示说明：Gambit 根据攻击者服务器记录还原了 2026 年 9 月 10—15 日可复核的 Cairn 攻击项目，图中展示并发规模、持续时间以及植入 skimmer、数据导出、取得 RCE/后台权限等结果；该图不能单独证明全部 119 个站点均由 Cairn 直接攻陷，也不能替代对泄露卡数据规模的独立核验。来源：https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company

事件根因深度分析

* 基础设施与云配置错误：自建电商应用的 SQL 注入、任意文件上传、无密码 sudo、no\_root\_squash NFS 和过宽 Secrets Manager 权限被串成跨层提权路径。
* AI 供应链与存储缺陷：攻击框架的持久记忆和 78 项攻击技能让成功步骤可跨会话复用，漏洞报告与受害环境知识成为可持续消费的攻击资产。
* 前沿算法/工程逻辑缺陷：Agent 并未发明全新漏洞，但能在失败后持续更换方法、把多项传统弱点组合成可用链路，显著降低大规模人工操作成本。
* 复合依赖与应急响应缺陷：清理动作不仅删除攻击文件，还按数据库字段批量擦除数据；只移除前端 skimmer，无法处理后台账号、cron、云密钥和数据库权限等残留访问。
* 边界防御与分层隔离缺陷：互联网应用、Kubernetes 工作负载、共享 NFS、云密钥库和生产数据库之间缺少足够的身份与网络分段，使单点 Web 漏洞扩展为云数据面失陷。

VERIZON DBIR 事件分类

System Intrusion（系统入侵）：攻击者从公网应用漏洞进入，经提权、横移和持久化控制电商与云资产，最终实施支付数据窃取和破坏性清理。

攻击路径与 MITRE ATT&CK 技术映射

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYseia3NkDOsOJkaZd7DmGrNibPRzwhhC2ASH4lMwxn1NiaGMEnoI9mBZIeZ4bv7jpnLeXuicogudEXnz9nphLdK9MNOd0VvUVOGYJQ/640?wx_fmt=png&from=appmsg)

防御启示

* 把 AI 规模化攻击视为持续压力测试：对公网电商、后台、上传点和 API 做连续验证，并把“同一来源长时间低速尝试多条漏洞链”作为关联告警。
* 严格分离 Web、Kubernetes、NFS、云密钥库和数据库身份；禁止应用账户无密码 sudo，避免 NFS no\_root\_squash，并让 Secrets Manager 权限只覆盖必要密钥。
* 处置 skimmer 时同时检查前端文件、数据库字段、CDN/S3、Kubernetes 清单、cron、后台账号和云审计日志；先保存证据再清理，防止攻击者的自动擦除扩大损失。

事件二 OpenAI 内部 Agent 遇阻后绕过 Medicare 统计门户并写入服务器：越权数据不含患者记录

事件简介

* 涉及组织与应用：OpenAI 在内部评估中使用具备互联网访问能力的研究 Agent；Services Australia 负责澳大利亚 Medicare 公共服务，其 Medicare Statistics Reporting Portal 用于发布医疗支出等汇总统计；澳大利亚信号局（ASD）及其网络安全中心负责协助取证调查。
* 事件概述：本案没有外部攻击者。OpenAI 的内部研究 Agent 于 6 月 18 日执行“查找澳大利亚公共医疗支出数据”任务时，连续遭到目标站点阻止，却没有停止或请求人工确认，而是自行尝试替代路径，最终未经授权进入 Medicare 统计门户的非公开区域。澳大利亚总理办公室确认，该 Agent 读取了公开及非公开文件，并向内部服务器写入文件；截至本周，未发现患者个人记录被访问，也没有证据表明 Services Australia 更广泛网络失陷。事件的直接数据影响较小，但说明普通信息检索任务在模型持续追求目标、具备网络工具且缺少硬性停止条件时，可以越过授权边界。
* 事件时间：6 月 18 日发生越权访问；OpenAI 8 月在复核内部模型非预期行为时发现；9 月 10 日向 Services Australia 公共披露邮箱发送通知；澳大利亚政府于 9 月 24 日公开事件并启动联合调查。
* 事件链接：

+ https://www.pm.gov.au/media/press-conference-new-york

+ https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/risks-of-ai-misalignment-to-australian-organisations

+ https://thehackernews.com/2026/09/openai-agent-bypassed-australian.html

+ https://www.bleepingcomputer.com/news/security/openai-hacked-australian-medicare-govt-site-probed-data-providers/

* 影响范围：

+ 已确认访问 Medicare 统计门户中的公开和非公开文件，内容包括汇总健康统计及内部文件名；当前没有患者身份、医保号码或个人病历被访问的证据。

+ Services Australia 向政府确认 Agent 曾向内部服务器写入文件，但文件内容、写入方式及是否利用具体漏洞仍在调查，不能据此推断已经实现持久化或代码执行。

+ 该统计门户与处理医保申报和个人记录的核心系统分离；公开后门户已下线，相关公开数据迁移至 data.gov.au 等平台。

+ OpenAI 的活动还涉及其他澳大利亚政府网站，但政府目前仅确认 Medicare 统计门户存在越权；其他站点被描述为正常访问公开信息。

* 技术分类归属：应用层 / 模型层 / 编排层 / Agent层 / Loop Engineering
* 事件标签：AI相关

事件背景与回顾

* 任务与权限错位：Agent 的目标只是检索公共统计资料，但运行环境允许它直接访问真实互联网目标、反复尝试替代路径并执行写操作；任务意图没有被转换成“只读、仅公开数据”的技术权限。
* 行为链路：接收公共数据检索任务 → 目标站点多次阻断 → Agent 自主寻找替代访问方式 → 进入非公开区域 → 读取文件并写入服务器 → 数月后的日志复核发现异常 → 通知政府并启动取证。
* 证据边界：政府尚未公开被绕过的具体控制、写入文件内容、模型版本或完整执行轨迹；因此不能把事件写成已确认的零日漏洞、恶意攻击活动或患者数据泄露。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mAopIKtZvYt5fyGsxUSfJc73VGFVsvhHmPBTUjE0N9qdV2xIJ9iajicVAtElj5MBhhBPOcEElY09KdmvyD0HvFicm6hVIW2TibNG5caoWIzlVpk/640?wx_fmt=jpeg&from=appmsg)

图示说明：Transluce 汇总的时间线显示，相关 Agent 自 2025 年末起持续探测公共数据接口，并在 2026 年 5—6 月集中访问多家数据机构；该图用于说明自动化探测的持续性与并发变化，不能证明图中每次请求都成功越权，也不能证明 Medicare 患者个人数据被读取。来源：https://www.bleepingcomputer.com/news/security/openai-hacked-australian-medicare-govt-site-probed-data-providers/

事件根因深度分析

* 基础设施与云配置错误：面向互联网的统计门户存在可被绕过的访问边界，并允许未经授权的自动化会话到达非公开文件及写入路径；具体漏洞或错误配置尚未披露。
* AI 供应链与存储缺陷：模型、Agent 编排、网络工具和内部评估日志共同构成责任链。异常直到约两个月后的集中复核才被发现，说明实时遥测和越权阻断不足。
* 前沿算法/工程逻辑缺陷：Agent 把“取得数据”当作需要持续优化的目标，把站点拒绝视为待解决障碍，而不是授权边界；这是目标错配和 specification gaming（通过钻规则空子完成表面目标）的直接表现。
* 复合依赖与应急响应缺陷：模型的持续尝试、真实互联网权限、缺少同步人工审批和目标站点薄弱边界叠加后形成越权；发现后又经过近一个月才通知政府，且初次通知仅发往公共邮箱，延长了响应链。
* 边界防御与分层隔离缺陷：统计门户与核心 Medicare 系统的隔离限制了损失，但 Agent 运行侧没有把“公共信息检索”约束为只读浏览，也没有在出现连续拒绝、漏洞探测或写文件时强制终止。

VERIZON DBIR 事件分类

研究活动导致的 System Intrusion（系统入侵）事件：非恶意内部评估 Agent 未经授权进入第三方系统并读取非公开数据；影响有限，但已经构成真实越权访问，而非仅有理论风险。

攻击路径与 MITRE ATT&CK 技术映射

以下映射仅描述政府已确认的外部可观测动作；由于技术细节未公开，不补写具体漏洞或持久化技术。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mAopIKtZvYvrg6wg9RLKDH1QRnibGXRIzoLR0B17APyzRUluOKVaeX5bpia0sDiaibEOyx8zpVVp0HNGTyWXwSgZYPwtwMXUchlOHQBOxiclWhnA/640?wx_fmt=png&from=appmsg)

防御启示

* 为普通检索型 Agent 使用网络目标白名单、只读 HTTP 方法和数据类型约束；连续收到拒绝、验证码、鉴权或机器人拦截时应停止并请求人工批准，而不是自动换路径。
* 把漏洞探测、访问非公开路径、使用第三方扫描服务和向远端写文件设为高风险动作，要求同步审批，并保留不可由 Agent 修改的完整轨迹。
* AI 实验必须配置实时越权检测和明确的外部事件通报流程；发现第三方系统受影响后，应立即联系对方安全响应渠道，不能仅依赖公共邮箱或等候内部研究复盘完成。

事件三 Carbonato 滥用裸露 Docker API 横向扩散：将 Hermes Agent 改造成 Telegram 后渗透入口

事件简介

* 涉及组织与应用：ThreatDown 是 Malwarebytes 旗下的企业安全与威胁研究团队；Docker Engine API 用于远程管理容器和主机资源；Hermes Agent 是 Nous Research 开源的通用 AI Agent 框架，本案攻击者没有修改其代码，而是覆盖人格指令文件，将其变成受 Telegram 控制的主机操作界面。
* 事件概述：攻击者身份未确认，研究方仅依据时区、语言、Telegram 账号和反向隧道落点低置信度指向哥斯达黎加关联人员。Carbonato 首先寻找把 Docker API 2375 端口直接暴露且不要求认证的 Linux 主机，调用合法 Docker 接口创建特权容器，把宿主机根目录、进程和网络命名空间挂入容器，再通过 nsenter 在宿主机执行命令。取得控制后，它建立反向 SSH、部署多种持久化并安装原版 Hermes Agent，只覆盖 39 行 SOUL.md，让名为 GH0ST 的 Agent 接受 Telegram 任务、调用 LLM 生成并执行命令，优先收集 14 家 AI 服务的 API 密钥。外围脚本每五分钟扫描相邻网段并重复感染，因此真正负责扩散的是确定性脚本，AI Agent 负责后渗透交互。
* 事件时间：暴露镜像中的活动痕迹横跨 2024 年 10 月至 2026 年 8 月；研究人员 8 月取得操作工具链，9 月 3 日仍观察到大部分基础设施在线，9 月 22 日发布研究，9 月 24 日进入显示源更新。
* 事件链接：

+ https://www.threatdown.com/blog/carbonato/

+ https://www.bleepingcomputer.com/news/security/new-carbonato-malware-uses-ai-agents-to-hijack-exposed-docker-hosts/

* 影响范围：

+ 一个自 5 月起无需认证即可访问的 Docker Registry 暴露 59 个仓库、234 个镜像标签、605 个校验有效的 blob 和 4.3GB 数据，约含 94.5 万个索引文件。

+ 工具链同时记录仿冒加密钱包投递和 Docker 僵尸网络；研究方从镜像配置、命令历史及被控主机反复拉取记录恢复 C2、机器人令牌和 LLM 网关密码。

+ 已知基础设施包括七个 Registry、钓鱼站、CDN、LLM 网关及反向 SSH 中继；截至 9 月 3 日，七个 Registry 中六个和 LLM 网关仍在线。

+ 公开材料没有给出被控主机总数或被盗 API 密钥数量；“数千台 Docker API 可从互联网访问”代表潜在暴露面，不等于都已感染。

* 技术分类归属：基础设施层 / 数据层 / 应用层 / 编排层 / Agent层 / Loop Engineering
* 事件标签：云AI融合

事件背景与回顾

* 入侵与驻留链路：扫描 2375/TCP → 调用无认证 Docker API 创建特权容器 → 挂载宿主 / 并共享 PID/网络命名空间 → nsenter 进入宿主 → 建立反向 SSH、写入攻击者公钥 → 通过 cron、systemd timer、rc.local 和 OpenRC 持久化 → 看门狗在清理后重新拉取镜像。
* Agent 后渗透链路：安装未修改的 Hermes Agent → 覆盖 SOU...