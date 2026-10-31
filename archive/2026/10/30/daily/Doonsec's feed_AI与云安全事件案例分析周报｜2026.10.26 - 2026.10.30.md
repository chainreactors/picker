---
title: AI与云安全事件案例分析周报｜2026.10.26 - 2026.10.30
url: https://mp.weixin.qq.com/s/K8inB_1XPWreHlgB32drcQ
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:45:04.291910
---

# AI与云安全事件案例分析周报｜2026.10.26 - 2026.10.30

# AI与云安全事件案例分析周报｜2026.10.26 - 2026.10.30

原创

星云实验室
星云实验室

绿盟科技研究通讯

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/mAopIKtZvYtOibqSxU2hK2AhZH6PW8tddGAjW7WVo231Ze1oADoX2e2amDYWG9NKYjxgpDO1q6ZNEtdO1VmjCj16ibK8knOxjFiaMhw5zJgVhM/640?wx_fmt=gif&from=appmsg)

扩展市场与模型仓库成为投毒入口，边界设备和构建平台的底层依赖持续承压。

事件一 Cursor 市场的 Claude Code 扩展被植入 SSH 后门：正常加载即写入攻击者公钥

1.1

事件简介

* 涉及组织与应用：Cursor 是集成 AI 编程功能的开发环境并运营扩展市场，Anthropic 开发 Claude Code，OpenSourceMalware 分析了被篡改的扩展包；本次已确认的分发范围是 Cursor 扩展市场。
* 事件概述：研究者与 Cursor 披露，身份未归属的攻击者把恶意代码植入 Cursor 市场的 Claude Code 2.1.313 扩展。加载扩展时，代码先于正常功能运行，写入远程登录公钥、建立启动任务，并尝试打开远程连接通道。多数非管理员环境无法完成关键连接步骤，但仍可能留下公钥和持久化、发送主机信息。Cursor 已下架恶意版本并处置攻击服务器；研究方纠正早期报道，目前没有证据表明 Open VSX、微软官方扩展或 Claude Code 的 npm 包遭同样投毒。
* 事件时间：Cursor 公告日期为 2026-10-29；恶意分发窗口约为当日 02:27—13:35 PT，按当地夏令时换算为北京时间 10-29 17:27—10-30 04:35。OpenSourceMalware 于 10-30 发布分析并更新分发范围。
* 事件链接：

+ https://cursor.com/blog/claude-code-extension-security-notice

+ https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor

+ https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html

* 影响范围：

+ 已确认对象为 Cursor 扩展市场中的 anthropic.claude-code@2.1.313；不能仅凭包名把其他市场和 npm 分发一并列为受影响。

+ Cursor 给出的受影响用户上限为 5,000，不代表有同等数量的主机已成功建立远程会话。

+ 初始信标包含主机、用户及匹配条件的环境变量名称，未直接包含这些环境变量的值；后续是否访问凭据应按主机证据判断。

* 技术分类归属：Agent层 / 开发工具供应链 / 扩展运行时 / 主机身份与持久化
* 事件标签：AI相关

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYuIonXL0AVSY3Wic6ou0yQ4dz9EZWskeGplYhXOT9DKUkiaqweoHZq6M7rtDQe9aMPzptFvpeicLjKPgf5AhUCtnzSnTAseqjwQ2w/640?wx_fmt=png&from=appmsg)

图1：OpenSourceMalware 的样本流程图展示扩展加载后的 SSH、公钥、LaunchAgent 与主机信息回传路径；虚线平台分支不等于该样本已执行全部平台代码。图中的连接能力受主机权限和载荷错误限制，不能证明每个安装者均被成功登录，也不证明其他扩展市场遭投毒。来源：https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor

1.2

事件背景与回顾

* 架构形态：编辑器扩展可随启动加载，并以开发者账户访问本机文件与进程。开发者不必发起 Claude 对话，恶意初始化逻辑即可执行。
* 攻击路径：市场分发被改写的扩展包 → JavaScript 前置加载器运行 → 写入 SSH 公钥 → 尝试启用远程登录和反向隧道 → 平台对应的持久化 → 主机信息信标。SSH 是远程登录协议，反向隧道则让主机主动连出后形成回连路径。
* 事实纠正：媒体初稿把多个扩展市场并列；原始研究随后确认 Cursor 市场是恶意包来源。公开材料尚未解释发布权限如何失守，不能认定 Anthropic 源码仓库或其全部发布渠道被攻破。
* 处置边界：Cursor 表示已重建市场、轮换密钥并与托管商关闭攻击服务器；这是公告中的处置状态，不等于所有曾安装的主机都已清理。

1.3

事件根因深度分析

* 以下为基于扩展执行机制与已公开载荷的防御分析，初始市场入侵根因仍待披露。
* 基础设施与云配置错误：最初突破的是扩展分发信任，而不是已证实的云租户隔离缺陷；后门尝试的成功程度取决于主机权限、SSH 服务状态和载荷错误等条件。
* AI 供应链与存储缺陷：熟悉的发布者标识、扩展名称及正常主体代码，不能证明当前渠道的完整产物可信；验证应绑定市场来源、平台包摘要和实际入口文件。
* 前沿算法/工程逻辑缺陷：恶意逻辑位于正常初始化之前，用户尚未开始 AI 任务便可能触发；只审核提示词和模型工具调用无法覆盖扩展宿主的启动代码。
* 复合依赖与应急响应缺陷：写入的公钥与后台脚本独立于扩展继续存在。下架、升级或卸载扩展，不能替代本机持久化清理和秘密访问调查。
* 边界防御与分层隔离缺陷：普通用户权限阻止了部分服务启用步骤，但未阻止所有文件写入和信息采集；权限边界降低部分后果，不足以据此判定无需排查。

1.4

VERIZON DBIR 事件分类

System Intrusion（系统入侵）中的软件供应链路径：已确认恶意产物与主机持久化能力；没有公开证据证明全部受影响安装均已被攻击者成功登录。

1.5

攻击路径与 MITRE ATT&CK 技术映射

下表描述样本能力及厂商确认的动作；每一步是否在具体主机成功仍须取证。

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYsqhVtyg0AMvkWrMSxG0KaicnXj4f2zt84fSic2FFNznFdRYCELJ7RUg38QYa9sB1QzkbWuCIMicsehmFrH5ZVoC7M4WczZ8MaFjc/640?wx_fmt=png&from=appmsg)

1.6

防御启示

* 按安装来源、窗口、平台包摘要及入口文件内容排查，不能把其他渠道的同名版本自动算作命中，也不能只检查当前已升级版本。
* 对有执行或持久化证据的主机先隔离并留存日志，检查公钥、后台脚本、启动任务和隧道进程，再按厂商指南清理并评估重建。
* 从可信环境轮换受影响主机可访问的凭据和会话；初始信标没有密钥值，不能排除成功远程访问之后的读取。

事件二 Hugging Face 假模型通过远程代码授权挖矿：权重尚未加载，GPU 主机已开始执行

2.1

事件简介

* 涉及组织与应用：Pluto Security 调查了恶意仓库，Hugging Face 与 ModelScope 提供模型托管分发，Xinference、GPUStack 等自托管推理平台则是恶意代码瞄准的运行环境。
* 事件概述：Pluto Security 披露，身份未公开的操作者把挖矿程序和后门包装成小型 Qwen2 测试模型。使用者一旦允许模型仓库附带的远程 Python 代码运行，这些代码便会在加载权重之前，以推理服务的账户权限执行。首轮仓库下架后，操作者换账号重新上传，并增加反向连接等访问能力。研究记录了矿池收益与运行中的矿工，但模型下载数量并不能代表感染人数。本案利用的是自定义代码执行授权，不是证明 Qwen 模型本身恶意，也不是安全权重格式被破解。
* 事件时间：活动始于 2026-09；10-29 公开报告，下载统计截至 10-28。本期按首次公开的完整调查纳入。
* 事件链接：

+ https://pluto.security/blog/hugging-face-malware-campaign-load-mine/

+ https://www.bleepingcomputer.com/news/security/hugging-face-malware-campaign-returns-to-hijack-gpus-for-crypto-mining/

* 影响范围：

+ 研究确认的两轮活动共 31 个仓库，另有技术关联模型；包含关联模型的下载量超过 32,000，不是确认感染或独立受害者数量。

+ 影响允许执行仓库代码的 GPU 主机、推理实例与相关作业；报告中的容器越界脚本依赖特权容器等条件，不构成普通容器均可逃逸的证据。

* 技术分类归属：AI供应链 / 模型加载 / 基础设施层 / GPU计算资源
* 事件标签：云AI融合

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYtic4ibYZlFgwoPQwIP5U32Ps29Apibvyib7ibIasdwRbibDULBM7GlE42yqdczsMImx4ImGL2W3B0E7ibxwZmicGHByO35bVT9xciaPaj8/640?wx_fmt=png&from=appmsg)

图2：Pluto 的加载流程图显示，启用远程代码授权后，自定义 Python 在权重读取之前执行，权限来自调用者。它解释本次恶意代码的入口，不代表所有模型默认执行远程代码，也不证明图中列出的每一种权重格式都参与本次攻击。来源：https://pluto.security/blog/hugging-face-malware-campaign-load-mine/

2.2

事件背景与回顾

* 攻击路径：伪装测试模型 → config.json 的 auto\_map 指向附带模块 → 用户或平台启用 trust\_remote\_code=True → Python 导入时执行顶层逻辑 → 启动挖矿并部署后门。
* 与历史事件的关系：本案是第三方恶意仓库分发活动，与 W30—W35 涉及评测 Agent 访问 Hugging Face 基础设施的事件不同，不能因为平台相同就合并归因。
* 处置边界：删除远程仓库不会删除已下载模块、主机进程或后门；报告中的 live 状态是调查快照，本期没有访问恶意仓库或执行模型复测。

2.3

事件根因深度分析

* 以下为基于公开链路的防御分析。
* 基础设施与云配置错误：推理进程可用的 GPU、文件和网络权限同时授予仓库代码；若使用特权容器、挂载宿主磁盘，后果可能从作业扩大到主机。
* AI 供应链与存储缺陷：仅检查权重格式或已知恶意签名，不能覆盖旁置 Python 的实际行为；安全权重与安全加载过程应分别验证。
* 前沿算法/工程逻辑缺陷：自定义实现是合法扩展机制，但导入即执行使“先试一下小模型”本身成为执行动作，模型大小不能证明代码安全。
* 复合依赖与应急响应缺陷：换账号和镜像重传使按仓库名封禁容易失效；调查应串联代码摘要、矿池身份、进程及外联，不能只查首轮名单。
* 边界防御与分层隔离缺陷：容器并非无条件的主机隔离保证，主机设备、磁盘、管理接口与元数据权限需要独立限制。

2.4

VERIZON DBIR 事件分类

System Intrusion（系统入侵）：恶意模型分发引入代码执行、算力滥用和后门；确认存在活跃矿工，不据此推算全部下载的失陷率。

2.5

攻击路径与 MITRE ATT&CK 技术映射

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYv3ZichB8dlrqNSe7nF8U3S7TKiauOGdjybibyibRVIbsTe5k950ibxXPDrIluCib3Rwb8pZU31esibyr0ZnFnySvKT1cHOReWxRvJktk/640?wx_fmt=png&from=appmsg)

2.6

防御启示

* 默认关闭远程模型代码；确需启用时审核完整模块与依赖、固定可信提交，并在无生产秘密的隔离实例验证。
* 模型审批同时包含权重、配置、Python 文件及外部下载；监测推理进程派生 shell、矿池连接和异常 GPU 消耗。
* 曾加载恶意仓库的环境按主机可达资产调查，清理缓存与后门并轮换秘密；只终止矿工不足以清除访问能力。

事件三 PHP2Shell 串联 Fragnesia 攻入 PAN-OS：管理面执行进一步触达内部身份系统

3.1

事件简介

* 涉及组织与应用：Dream 是攻击调查披露方，Palo Alto Networks 的 PAN-OS 为企业防火墙及管理设备提供系统软件，Active Directory 管理内部用户与权限，CISA 的 KEV 目录记录已知遭实际利用的漏洞。
* 事件概述：Dream 在攻击者留下的材料中发现一条针对防火墙管理面的利用链，操作者身份尚未确认。攻击先利用 PHP2Shell 在设备的网页管理服务中执行代码，再利用名为 Fragnesia 的 Linux 内核缺陷取得最高权限，之后通过隧道进入内部网络并针对企业身份系统行动。厂商确认公网管理面出现实际利用。与上周以底层 PHP 缺陷和利用尝试为主的披露相比，本周新增了具体设备、提权链与后续访问证据；AI 参与开发仍属研究方评估，不能写成已证实的全自主攻击。
* 事件时间：Dream 10-25 发现材料，10-26 发文、10-29 更新厂商确认；材料中的主要利用发生于 10-23—24。PHP 两个 CVE 于 10-26、Fragnesia 于 10-28 进入 KEV。
* 事件链接：

+ https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers

+ https://security.paloaltonetworks.com/CVE-2026-109618

+ https://www.cisa.gov/sites/default/files/feeds/known\_exploited\_vulnerabilities.json

+ https://www.wiz.io/blog/php2shell-exploitation-so-far

* 影响范围：

+ PHP2Shell 为 CVE-2026-109618、CVE-2026-109619，提权漏洞为 CVE-2026-46300；PAN-OS/Panorama 的受影响分支与修复包按厂商公告逐项匹配。

+ Dream 据攻击材料报告 25 台已取得 root 的设备，其中 3 台位于美国政府关联环境；这是调查样本范围，不是全球受害总数。

+ 身份系统凭据提取和目录枚举有材料支持；后续密码喷洒、创建账户的尝试不等于均已成功。

* 技术分类归属：基础设施层 / 边界管理面 / 云与企业身份 / AI辅助攻击
* 事件标签：云AI融合

![](https://mmbiz.qpic.cn/mmbiz_jpg/mAopIKtZvYutCuZMPZbaC9YukWudW4h8exYCRufmMZ49epqAEKg0gCgcIc96cbiaEzqnarJBaWHQJia7nXjtiaMNSrUx9EP8Y0rllqNxUL8aZw/640?wx_fmt=jpeg&from=appmsg)

图3：Dream 原始时间线把准备、批量利用、进入内网与后续操作分开，并展示目标从扫描列表收敛到 25 台设备的调查过程。它是研究方依据攻击材料重建的时间线，不代表全球受害总数；图中列出的 AD 喷洒、后门等后续任务，不能一律视为已成功完成。来源：https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers

3.2

事件背景与回顾

* 前周事件增量更新：W43 事件一介绍 PHP 跨请求状态与内存生命周期缺陷。本周转向针对 PAN-OS 特定构建的武器化、内核提权和内部横向访问，不重复上周通用网站利用分析。
* 攻击路径：公网管理接口 → 定制 PHP 内存利用 → 低权限代码执行 → 内核提权 → Web shell → 反向 SSH 隧道 → 内部身份系统访问。
* 互补证据：Wiz 在其观测范围没有看到成功尝试，与 Dream 的定向成功样本不矛盾；两者覆盖的构建、资产和观测条件不同，不能互相否定。

3.3

事件根因深度分析

* 基础设施与云配置错误：管理面暴露使运行时缺陷成为入口；厂商区分管理服务与一般数据转发面，不能笼统写成所有流经防火墙的流量均可触发。
* AI 供应链与存储缺陷：设备嵌入的 PHP 和内核需要厂商整体交付修复，不能套用服务器上的 PHP 更新命令自行替换设备组件。
* 前沿算法/工程逻辑缺陷：运行时异常状态先突破进程边界，内核缺陷再突破操作系统权限边界；修复后应验证对应环节是否已被切断。
* 复合依赖与应急响应缺陷：已取得 root 的设备可能留下 Web shell、隧道及被读出的目录凭据；升级解决漏洞，不能自动撤销既有访问。
* 边界防御与分层隔离缺陷：边界设备对内部目录的可达性决定进一步影响。AI 工具安装痕迹与脚本风格，不足以证明 AI 编写了特定利用代码或无人自主执行。

3.4

VERIZON DBIR 事件分类

System Intrusion（系统入侵）：外部服务漏洞与本地提权串联，继而访问内部身份基础设施；归因和后续损失范围仍需独立证据。

3.5

攻击路径与 MITRE ATT&CK 技术映射

![](https://mmbiz.qpic.cn/mmbiz_png/mAopIKtZvYu0TGGMDacawwv5CMvbn9s9Q91nvzvynjAMQQ1BiciaX8Fwf6BPgMGbzeMa8nhZK39swcCAHS4IdZ5jQsCmDwwv16UJTSQmZjEFA/640?wx_fmt=png&from=appmsg)

3.6

防御启示

* 限制管理面仅对可信路径开放，按具体分支核对可下载修复包；公告预计日期不能当作补丁已发布。
* 保留设备与身份日志，回溯异常管理请求、Web shell、提权与隧道；确认失陷设备按厂商恢复流程处理，同时撤销相关身份凭据。
* KEV 官方...