---
title: 全新免杀skills：AI自主分析对抗杀软、沙箱！！！
url: https://mp.weixin.qq.com/s/A_KzZMzJwmKQgK0pY0cavQ
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:36:41.633916
---

# 全新免杀skills：AI自主分析对抗杀软、沙箱！！！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cGhMn4Bj3bZhJQFQuic0oNEKo3cPDLERu25TOu6KX69cuIo0y2AbXll5AJ5L40a0qYvtWHvf9FxwsIgQ2Fy8hibv77EohRYN8swyfII5T9GTY/0?wx_fmt=jpeg)

# 全新免杀skills：AI自主分析对抗杀软、沙箱！！！

原创

信益安研究院
信益安研究院

信益安信息安全研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

首席信息安全技术官Jason Tian：

OSCE3（OSEP、OSWE、OSED）、OSCP、CISSP持证者，主要负责安全研究方向包括EDR终端对抗，二进制漏洞挖掘，Opsec后渗透武器库开发以及红队自顶至下技战术研究。参与境外APT组织研究与对抗，涉诈等黑灰产产业链追踪溯源，多单位内部红队培训特聘讲师。

# Win-Offensive-Dev： 免杀 skill2.0 介绍

> 信益安信息安全研究院出品 | XinYiAn Security Research Institute
> 适用场景：授权红队评估、安全研发、攻防演练、内部教学实验

---

## 更新说明

> 之前发布的原始版本是一个纯知识库型 Skill，仅包含技术分类索引和代码风格规范，没有任何命令，没有参考文件目录，没有工具链，也没有自动化能力。新版从零重建的完整系统。

### 1. 主知识库从零构建

原版没有任何技术参考文件。新版构建了完整的 **15 个技术参考模块**，涵盖：

* • **核心文件**：`execution.md`、`persistence.md`、`networking.md`、`reflective_loading.md`、`token_privilege.md`、`lateral_movement.md`、`enumeration.md`、`syscalls.md`、`memory_evasion.md`、`defense_evasion.md`、`process_manipulation.md`、`iat_hiding.md`、`credential_access.md`
* • **自动化命令文件**：`malfuzz.md`（技术池与模板）、`reverse_analysis.md`（分析流程与检测规则）

**新增技术方向**：UAC Bypass系列技术、syscall系列技术、加载/执行技术、加密方式

**OPSEC 元数据标准化**：每个技术条目均包含检测风险评级、Sysmon Event ID、ETW Provider、EDR Hook 点、缓解建议

### 2. 全新的 /malfuzz 命令

**9维度技术池**（相比旧版知识库中的简单描述，新版实现了完整的随机组合引擎）：

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bY83zlgy3bRxibvx0OFUtuaSpLqadphyyGFAg8K1U13ARmNtxADk9IbiaCkSvQuhlCMYHaGcXwWEdZUIzEkGWp7h07wKy4foscD0/640?wx_fmt=png&from=appmsg)**

**完整验证流程**：calc.bin 初始验证（10 秒轮询） → 编译后约束自动验证（strings64/sigcheck64/IAT 解析） → 真实 shellcode 替换重新编译 → 签名掠夺。

**批次多样性评分**：计算 pairwise Hamming distance，覆盖率不足时自动提示重生成。

**EDR 感知加权算法**：指定 `target:<edr_name>` 时，从已有 EDR profile 读取历史数据，对已验证通过的技术组合加权（bypassed=3 / untested=2 / detected=0）。

### 3. 全新的 /reverse 命令

构建完整的恶意软件静态 + 动态分析流水线，分五个阶段：

**Phase 1 — 静态分析**

**Phase 2 — 动态分析**

**Phase 3 — 持久化检查**

**Phase 4 — 报告生成**

**Phase 5 — 自动增强**

### 4. 全新的 /edrfuzz 命令

从零构建了 EDR 检测特征沉淀系统，解决测试经验散落在聊天记录、截图、临时文档里难以复用的问题。

交互流程：自动扫描最近 `fuzz_output_*` 目录 → 列出本次生成的 loader → 用户输入未被检测到的编号 → 指定 EDR 名称 → 自动分析绕过/检测的技术共性 → 保存到 `edr_profiles/<edr_name>/profile.md`。

Profile 记录：已验证通过的技术组合、已验证被检的技术组合、检测趋势变化（按时间记录）、下一轮推荐生成方向。

### 5. 全新的 /sandboxfuzz 命令

沙箱指纹采集与分析工具，用于生成针对性的反沙箱检测代码

### 6. 全新的 /vt 命令

VirusTotal API 自动化分析与自动增强：

### 7. 项目结构完善

* • 新增 `SysinternalsSuite/` 工具目录（strings64 / sigcheck64 / Procmon64 / Listdlls64 / handle64 / pipelist64 / autorunsc64 / procexp64）
* • 新增 `edr_profiles/` EDR 知识库（含某绒 100% 绕过案例）
* • 新增 `sandboxfuzz_output/` 沙箱指纹输出目录

---

## 项目目录结构

```
win-offensive-dev_2.1/
├── .claude/
│   └── skills/
│       ├── win-offensive-dev/   # 主知识库 Skill（自动触发）
│       ├── malfuzz/             # /malfuzz 批量生成
│       ├── reverse/              # /reverse 分析评估
│       ├── edrfuzz/             # /edrfuzz 结果沉淀
│       ├── sandboxfuzz/         # /sandboxfuzz 沙箱指纹采集
│       └── vt/                  # /vt VirusTotal 分析
├── references/                  # 技术参考文件（15 个模块）
│   ├── execution.md             # 加载与执行方式
│   ├── iat_hiding.md           # API 隐藏
│   ├── syscalls.md             # 系统调用
│   ├── defense_evasion.md      # 防御规避
│   ├── memory_evasion.md        # 内存逃逸
│   ├── process_manipulation.md  # 进程操作
│   ├── credential_access.md     # 凭据访问
│   ├── persistence.md           # 持久化机制
│   ├── networking.md            # C2 通信
│   ├── reflective_loading.md    # 反射加载
│   ├── token_privilege.md       # 令牌与权限
│   ├── lateral_movement.md      # 横向移动
│   ├── enumeration.md           # 主机与网络枚举
│   ├── malfuzz.md              # /malfuzz 技术池与模板
│   └── reverse_analysis.md     # /reverse 分析流程
├── edr_profiles/                # EDR 检测画像知识库
│   ├── README.md
│   └── huorong/
│       └── profile.md          # 某绒 100% 绕过记录
├── sandbox_profiles/            # 沙箱指纹画像（自动生成）
├── sandboxfuzz_output/          # 沙箱指纹收集输出
├── fuzz_output_*/               # 每次生成的样本、源码、报告
├── SysinternalsSuite/           # Sysinternals 分析工具集
├── calc.bin                     # 验证用载荷（x64 calc shellcode）
├── agent.x64.bin                # 真实测试载荷
├── test_syscall.obj             # Syscall 测试目标
├── loader_0*.obj                # 真实生成的 loader 目标文件
├── sandbox_info*.txt            # 真实沙箱环境指纹
├── sandbox_report_*.md          # 沙箱分析报告
├── vt_config.json               # VirusTotal API Key 配置
├── SKILL.md                     # 主 Skill（兼容旧版加载）
└── README.md
```

---

## 加载方式

Skills 通过 `.claude/skills/` 目录自动加载，无需手动注册。进入项目目录后启动 Claude Code 即可：

```
cd C:\Users\你的用户名\Downloads\win-offensive-dev
claude
```

启动后输入 `/`，即可看到可用命令：

`/malfuzz`、`/reverse`、`/edrfuzz`、`/sandboxfuzz`、`/vt`。

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bYkQphbUN2zn8DtAXNmGqYoorzGSzFibLFMWyRd5XXcDaU0nfW1eZQYx9ibrlqggM67dOUwSAicsL7wNEa9FB0PqFIEHpjxACt7S4/640?wx_fmt=png&from=appmsg)

---

## 核心命令一：/malfuzz 批量生成 Loader

`/malfuzz` 是这套 Skills 里最直观的命令。它根据指定语言、数量和测试载荷，批量生成多个不同形态的 loader，并自动完成编译、验证、替换真实载荷的完整流程。

### 语法

```
/malfuzz <语言> <数量> <shellcode路径> [sign] [sandbox] ["描述"]
```

| 参数 | 说明 |
| --- | --- |
| 语言 | `C、C++ 或 Rust` |
| 数量 | 生成 loader 的数量（建议 3-10） |
| shellcode路径 | `.bin` 文件路径，支持相对或绝对路径 |
| sign | 可选，启用签名掠夺（复制合法 EXE 的签名/图标/版本信息） |
| sandbox | 可选，启用反沙箱 + 反调试技术 |
| 描述 | 可选，用引号包裹，指定技术偏好或目标 EDR |

### 使用示例

```
# 基础生成
/malfuzz C++ 5 ./payload.bin

# 带签名掠夺
/malfuzz C++ 5 ./payload.bin sign

# 全套：签名 + 反沙箱
/malfuzz C 8 ./payload.bin sign sandbox

# 指定目标 EDR
/malfuzz C++ 5 ./payload.bin sign sandbox "target:defender"

# 指定技术偏好
/malfuzz C++ 3 ./payload.bin "只用callback执行，不要fiber"

# Rust 版本
/malfuzz Rust 4 ./payload.bin sandbox
```

### 技术组合维度（9 个维度）

每个 loader 从 9 个维度随机选取技术，保证批次内多样性：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bY83zlgy3bRxibvx0OFUtuaSpLqadphyyGFAg8K1U13ARmNtxADk9IbiaCkSvQuhlCMYHaGcXwWEdZUIzEkGWp7h07wKy4foscD0/640?wx_fmt=png&from=appmsg)

### 执行流程

```
1. 生成阶段：使用 calc.bin 作为 payload 生成所有 loader 源码并编译
2. 编译后约束验证：strings64 检查敏感字符串，sigcheck64 检查熵值，IAT 解析验证
   → 违反约束则自动修复源码并重新编译
3. 自动验证：逐个运行 EXE，轮询检测 calc.exe 进程（每秒检测，最多 10 秒）
   - 检测到 calc.exe → 验证通过，自动 kill
   - 未检测到 / 提前退出 → 报告失败原因，提供修复
4. 替换阶段：验证通过的 loader 自动替换为真实 shellcode，重新加密编译
5. 签名掠夺（sign 选项）：从系统合法 EXE 复制 Authenticode 签名
6. 生成每个 loader 的技术说明文档 + README.md 汇总（含多样性评分）
```

### 输出结构示例

```
fuzz_output_20260510_000000/
├── README.md                          # 汇总表格 + 多样性评分
├── common/
│   └── peb_resolve.h                  # 共享 PEB walk 头文件
├── loader_01_tpwait_xorbf_uuid.cpp    # 源码
├── loader_01_tpwait_xorbf_uuid.exe    # 编译产物（含签名）
├── loader_01.md                       # 技术说明
├── loader_02_geo_cha20_mac.cpp
├── loader_02_cha20_mac.exe
├── loader_02.md
├── loader_03_fiber_aes_ipv4.cpp
├── loader_03_fiber_aes_ipv4.exe
├── loader_03.md
├── payload_uuids.inc                  # UUID 编码载荷（loader_01）
├── payload_macs.inc                   # MAC 编码载荷（loader_02）
└── payload_ips.inc                    # IPv4 编码载荷（loader_03）
```

### 实际生成示例

以 `target:huorong` 为目标，生成 3 个 C loader 的结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3baD0GpZ9RIia76dTia19xbknyZqfoQiaHia2TceqhQ5AOXzkEPgP9yDKkPnYS7WVn0BArNkudicx2HIkPr6JT5VyFMuV0GoNMnTZP4w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3baNWJeTicefhiaOxrAZficKUK6JTeiaNeB7CblEsI6Pw9WsTmVaFJWS98IB8gicOwEAGz3Gfea6tjF5dCM4AHdG8l3zzTA9HsicWl4ss/640?wx_fmt=png&from=appmsg)

某绒实际测试结果：**100% 绕过率**，批次多样性评分：**0.78**

---

## 核心命令二：/reverse 自动分析 EXE

生成样本之后，下一步是分析检测面。`/reverse` 对单个 EXE 或整个目录里的 EXE 进行静态 + 动态分析，输出 Markdown 报告，并可根据报告自动提出增强方案。

### 语法

```
/reverse <exe路径|文件夹路径>
```

### 使用示例

```
# 分析单个 EXE
/reverse ./fuzz_output_20260510_000000/loader_01_tpwait_xorbf_uuid.exe

# 分析整个输出目录
/reverse ./fuzz_output_20260510_000000/

# 分析任意路径
/reverse C:\tools\my_implant.exe
```

### 分析流程（四个阶段 + 持久化检查）

**Phase 1 — 静态分析**

* • `strings64.exe` 双趟扫描：提取可读字符串，检查敏感 API/DLL 名泄露
* • `sigcheck64.exe`：检查签名状态、计算熵值、读取版本信息
* • PE 导入表解析
* • 计算熵值

**Phase 2 — 动态分析**

* • `Procmon64.exe`：自动启动监控 → 运行目标 EXE → 捕获行为 → 导出 CSV 分析
* • `Listdlls64.exe`：DLL 枚举，检查异常 DLL 加载（非 System32、未签名）
* • `handle64.exe`：句柄分析，检查跨进程句柄（注入指标）
* • `pipelist64.exe`：命名管道扫描，执行前后 diff 新增管道

**Phase 3 — 持久化检查**

* • `autorunsc64.exe`：执行前后 diff，覆盖 Run 键/IFEO/COM 劫持/服务/计划任务/WMI/...