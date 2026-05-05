---
title: 速度与激情4，威胁猎手【深狩】：静默不是清白，是我在翻你的上一页
url: https://mp.weixin.qq.com/s/klwCVGH0Dzo070KyxU8xPQ
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:58:54.912696
---

# 速度与激情4，威胁猎手【深狩】：静默不是清白，是我在翻你的上一页

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibANIaIJODOlwT97664yQzLicsS2HQqibiaW2EC9ia4nAibCjXicHQETEqC1pHglsEDrTZ4tlpzXY4yqlNjeTSbONatUrIv8eghvNsnJrDCfzd0Z34/0?wx_fmt=jpeg)

# 速度与激情4，威胁猎手【深狩】：静默不是清白，是我在翻你的上一页

dimu
dimu

AI简化安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**编者按｜背景、内容与读者**

大模型侧 **DeepSeek V4 级别能力带来约 1M token 长上下文**，使"跨周、多块证据一次性共读"在工程上成为可能；同时 **Flash 等档位在批量狩猎场景下更具价格友好性**，适合作为常态化运营的推理入口，复杂个案再路由至更强模型。

本文在此基础上展开 **威胁猎手智能体（Deep Fusion）**：先交代**传统威胁狩猎究竟难在哪里**——为什么SOC"有数据、无结论"是常态；再以 **UEL / 关系图谱** 打通异构源，以 **端侧与网侧图模型 + 融合层** 产出可解释打分与证据指针，通过**三路消融实验**（端侧图→LLM / 网侧图→LLM / 双塔融合→LLM）验证融合层的不可替代性；最后以 **L1–L4 策展包**控制噪声与成本，经 **LLM 网关编排**生成可追溯溯源报告，支持 **工单回写与 KQL/Sigma 规则回填**，形成从被动告警到主动狩猎的运营闭环。

**读者对象**：甲方安全负责人、SOC/Tier2 威胁猎手与数据工程、乙方产品与交付架构师。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOkkafZxEHItDrsPanI9ibAvnREGrDSJWLLydIofqL647kJKWbL6hF8BYMrRuTO2O6L2WKaRUF36ybRjp414aicM3fiaVrDacWQvvA/640?wx_fmt=png&from=appmsg)

---

## 一、传统威胁狩猎的真实困境：为什么 SOC 长期"有数据、无结论"

### 1.1 过去怎么做威胁狩猎

在绝大多数 SOC 现场，威胁狩猎的实际形态是：

* • **事件驱动**：出了告警才查，没告警就当没出事；
* • **单源回溯**：在 SIEM 里手动下 KQL/SPL，围绕一个 IP 或一个 hostname 翻日志；
* • **人工拼图**：EDR 进程树、FW 会话流、AD 审计、NDR 元数据散落在不同控制台，分析师靠脑记和 Excel 做关联；
* • **经验密集**：一个能独立完成 30 天回溯的高级猎手，培养周期通常 >18 个月。

这套流程有两个致命缺陷：一是**查什么取决于"想到了什么"**——没有想到的攻击模式永远不会被搜索；二是**跨 30 天的证据散布在多套系统中，单靠人脑根本拼不出完整故事线**。

### 1.2 核心矛盾：SOC"安静" ≠ 没有攻击者

SOC 安静，往往只能证明两件事：**你的规则在工作，但未必证明你的对手没有工作**。真正危险的攻击，不是"没进来"，而是"进来了但不吵"——每一个信号都很小，但整条链路很长。

| 传统狩猎的瓶颈 | 根因 | 造成的后果 |
| --- | --- | --- |
| **跨源割裂** | 用户名、NAT、会话与主机别名难以对齐 | 同一实体在 EDR/FW/NDR/AD 中有四种身份，人工拼图以小时计 |
| **阈值与白名单膨胀** | 慢速渗出、Living-off-the-land、服务账号滥用被降噪压住 | 攻击链每个环节都"低于规则线" |
| **保留策略不一致** | 热点索引、冷存储、跳板录像保留窗口错位 | 回溯时"看得见 SIEM，看不见全貌" |
| **经验不可复制** | 高级猎手的判断力难以标准化 | 人走经验走，团队没有沉淀机制 |

### 1.3 从"被动响应"到"主动防御"的价值跃迁

传统 SOC 流程：**日志进来 → 规则匹配 → 出告警 → 人工研判 → 关工单**。这个闭环处理的是"已知的坏"，对"未知的坏"和"潜伏中的坏"几乎无能为力。

威胁猎手 Deep Fusion 要做的，是把安全运营从"告警处理中心"升级为"攻击链理解中心"：

* • **从查"一个事件"到还原"一条故事线"**；
* • **从依赖个人经验到沉淀可复用规则**；
* • **从事件驱动到假设驱动**——主动验证"攻击者可能在哪里"，而不是等告警报"哪里着火了"。

这个价值不是"省了几个分析师工时"，而是让组织具备了**主动发现潜伏攻击的系统性能力**——此前这项能力完全绑定在少数高级猎手的个人经验上。

---

## 二、案例背景：制造企业网络拓扑与"安静 SOC"困局

下文对标合成企业 **"华枢智造科技（FabricTech）"**：

* • **行业**：工业控制器、精密传感器研发与代工；图纸与 BOM 存放在 PLM/DMS
* • **布局**：上海总部 + 深圳（研发副中心）+ 苏州（工场与仓储）+ 西安（国产化替代测试）
* • **域环境**：全员 Windows 域终端 + 研发 macOS/Linux 混合接入零信任网关
* • **网络分区**：INET / DMZ / DC‑CORE / DC‑DATA / SEC‑MGMT / OFC‑TERM / OT‑EDGE
* • **探针覆盖**：EDR（MDE + SentinelOne）、NDR（Darktrace / ExtraHop / Cisco SNA）、边界防火墙（PA + FortiGate）+ IPS、DMZ WAF、AD 审计、SIEM 与 ServiceNow
* ![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOl9mayh0LMgibFkicR3alHxMibeYFYicSUrcniaKfEefOcEMKia86sN6AYcA41cqbFF7aU6W0Zm48LWnLjLzwiacL06sp56txEYKvlgDw/640?wx_fmt=png&from=appmsg)

### 2.1 事件表象：SIEM 安静，但现场"觉得不对"

约 3～4 周内：

* • PLM/DMS **偶发卡顿**，IT 归因存储与巡检窗口；
* • 有人看到 EDR"已处理"类提示（钓鱼宏）但未建单；
* • 工场 MES 网关 **单次**短连接异常，记在运维笔记，**未升级安全**。

但在技术侧，多个信号分散在各自系统里：

| 来源 | 现象 | 为何未告警 |
| --- | --- | --- |
| EDR | Excel → PowerShell → `update.microsoft-pki.com`（仿冒） | 归并到管理员例外或低风险 |
| 防火墙 | 持续 443 至云 OSS、上行小包多频 | 无"慢渗漏"专项策略；与备份场景混淆 |
| NDR | JA3 与常见云客户端撞脸 | 未开强基线模型（怕误报） |
| JMPT | 服务账号 srv-backup 非窗登录、PS -enc | 在变更白名单，规则压制 |
| AD | 无 DCSync 等大声事件 | 攻击者慢速、合法路径优先 |

这就是**传统狩猎最典型的困局**：每一条日志都"看起来没什么"，每种工具都"单独看不值得升级"。但把它们拼在一起——有人进来了，一直没走。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibANIaIJODOlCZvkmBTBL5jx3BkZSmm80cCuiaCnDw4LeX5jwxhYVnVn8mwj0JDJTT71oQhY3EWjPDpSgGULAzBDLjEMWz7FrwFEAOyL0PGK0/640?wx_fmt=png&from=appmsg)

---

## 三、威胁猎手智能体整体设计

### 3.1 设计原则（四不四要）

**四不**：

1. 1. **不替代现网 SIEM**：检测、降噪、SOAR、工单主链路保留
2. 2. **不把全量原始日志喂模型**：成本、泄露、上下文浪费三道红线
3. 3. **不自动封网**：模型结论打 ★ 标记，处置走工单与人审
4. 4. **不依赖单一数据源做判断**：端侧证据与网侧证据必须融合互验

**四要**：

1. 1. **要先做实体对齐再建模**：UEL 统一实体层是地基
2. 2. **要端侧 + 网侧双塔独立建模**再跨域融合
3. 3. **要 L1–L4 分层策展**充当长上下文的节流阀
4. 4. **要证据可回链**：每条结论带 `evidence_refs`，每条输出配 SIEM 复核 KQL

### 3.2 数据价值链：从"数据过载"到"证据驱动"

传统 SOC：**多源日志 → SIEM 索引 → 规则/ML Job → 降噪 → 告警**。这条链路对弱信号不友好。

Deep Fusion 在旁路新增一条证据价值链：

```
多源日志 ──→ UEL 实体对齐 ──→ 端侧图 + 网侧图 ──→ 双塔融合打分
                                                    │
                                           ┌───────┘
                                           ▼
                                    L1–L4 分层策展
                                           │
                                           ▼
                                    LLM 长上下文推理
                                           │
                                           ▼
                             溯源报告 + KQL复核 + 规则回填
```

本质变化：**从"等告警→查日志→靠经验拼图"变成"假设→图谱检测→融合打分→长上下文叙事→回填规则"**。

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOly5ARiciaZlSMIqqbeCjaCct3cWpW2QKEXia15HXKKRWYPNsCZhsh4vzOM4lthWF7otB358oPwcQlq2jnULxoWuiaKW4X6fWpe8lw/640?wx_fmt=png&from=appmsg)

### 3.3 分层总体架构

```
┌─────────────────────────────────────────────────────┐
│                    数据源层                           │
│  EDR/XDR │ NDR/流 │ NGFW/WAF/IPS │ AD/IAM │ CMDB    │
└─────────────────────┬───────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│          数据工程层（规范化/去重/PII策略/血缘）        │
└─────────────────────┬───────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│   UEL 统一实体 + 端侧图(HGT/RGCN) + 网侧图(TGN)       │
│                  │                  │                │
│                  └── 融合层 ────────┘                │
│              Cross-Attention / MLP                   │
└─────────────────────┬───────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│         L1–L4 证据策展（节流阀 + 合规最小化）          │
└─────────────────────┬───────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│   LLM 推理网关（配额/审计/路由）→ DeepSeek V4 API     │
└─────────────────────┬───────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────┐
│  溯源报告 · KQL复核草案 · Sigma规则 · ITSM工单回写    │
└─────────────────────────────────────────────────────┘
           治理横切：RBAC · 脱敏 · RACI · 回归
```

![](https://mmbiz.qpic.cn/mmbiz_png/ibANIaIJODOl8p6P1F8vjdPuu4dI5svqLM0HpwELZ83Xjb7IRV8zEn9jIEM91k9oVauWia7oQUk2ibo3ibLtFMYTiap1cRiaJBRTVMnqfMTnkWZwQ/640?wx_fmt=png&from=appmsg)

---

## 四、详细设计：逐模块拆解

### 4.1 数据源与接入层

| 类别 | 典型来源 | 接入要求 |
| --- | --- | --- |
| 终端 | EDR (MDE / SentinelOne) | 进程树、脚本块、网络 connect 事件 |
| 网络 | NGFW (PA / FortiGate) + NDR (Darktrace / ExtraHop / Cisco) | 会话流、JA3/JARM、DNS 解析链 |
| 边界 | WAF (F5 ASM)、IPS | 攻击特征、误报标记 |
| 身份 | AD Security / IAM | 登录、权限变更、服务账号行为 |
| 运营上下文 | SIEM 告警、ITSM Case、CMDB | 告警生命周期、资产归属、处置状态 |

### 4.2 UEL 统一实体层

UEL 解决的核心问题：**同一个实体在不同系统中的身份不一样**。

| 实体 | UEL 主键 | 关键对齐逻辑 |
| --- | --- | --- |
| Host | `hostname + mac` | EDR ↔ FW ↔ NDR 资产视图对齐 |
| User | `tenant + account_id + account_type` | 区分服务账号与人工账号 |
| Process | `host_id + pid + process_start_ts` | 避免 PID 复用造成误关联 |
| IP | `ip + scope(internal/external)` | NAT 场景保留 pre\_nat/post\_nat |
| Network Flow | `5-tuple + window_id` | 终端 connect 与网络 flow 的 join 键 |

**NAT 还原是 UEL 落地第一道坎**：若不做 `pre_nat/post_nat` 还原，终端 connect 的 `src_ip` 与防火墙 flow 的 `src_ip` 就是两个不同实体，后续所有跨域关联全部断裂。

### 4.3 端侧知识图谱（终端异构行为图）

* • **节点**：`Process`、`File`、`Network`、`Registry`、`User`
* • **边**：`spawn`、`read/write`、`connect`、`load`、`login`
* • **每条边必带**：`event_ts`、`host_id`、`confidence`、`source_ref`
* • **GNN 选型**：**HGT（异构图表征）** 或 **RGCN**，用于异常子图/节点评分
* • **核心要求**：完整恢复 PPID 链路（进程树是终端证据的物质基础），syscall 序列以"边特征"存储而非仅保留单点事件

端侧图独立回答：**这台机器上发生了什么？**——进程父子关系、文件操作链、登录时间线。

### 4.4 网侧知识图谱（网络时序图）

* • **节点**：`Host`、`Domain`、`ExternalIP`、`Service`
* • **边**：`flow`、`dns_query`、`resolve`、`lateral`、`access`
* • **流量边特征**：`bytes`、`packets`、`duration`、`interval_entropy`、`policy_hit`
* • **GNN 选型**：**TGN（时序图网络）** 或 **EvolveGCN**，用于 beaconing、横移时序异常
* • **快照粒度**：默认 15m 或 1h 快照图（可配置）；内网横移边单独打标签

网侧图独立回答：**流量去了哪里、频率如何？**——DNS 解析链是否异常、外联是突发还是持续、横移路径如何。

### 4.5 跨域融合层：为什么端侧图和网侧图必须"结婚"

这是新架构中最关键的一层。通过 `connect` 事件与网络 `flow` 做时间窗 join（默认 ±120s，按 `5-tuple + 时间差最小 → 流量最大` 优先级匹配），形成：

```
Proc...