---
title: 基于SAST+AI代码审计 架构与功能详解
url: https://mp.weixin.qq.com/s/OyaZkFJJ_IbMNdpfp4OThQ
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:29:11.225423
---

# 基于SAST+AI代码审计 架构与功能详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AwziaxUyibcNiaO8WkNibJa15ibSvzKAzbJRGVlODDVGKPcibNiaUzeBpapYbNR9JicK3dKQTV11nvx7ZnhFhlFjXJAZQXvxF1lT3tzXP6YqIe87VY8/0?wx_fmt=jpeg)

# 基于SAST+AI代码审计 架构与功能详解

原创

一寸灰
一寸灰

东方隐侠安全团队

![]()

在小说阅读器中沉浸阅读

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

Java-Audit 架构与功能详解

之前的代码审计项目由同事接手了，然后他改了很多东西。那理论上，我这水逼项目和产品也不搭边了，所以直接开了！

相对于之前优化的点

1. joern扫描结果的过滤： joern扫描出来的结果大部分都是噪音如果我们AI去读取那些结果以做分析会很浪费上下文。所以写了个过滤器，只保留AI用于审计的部分。
2. 路由分析结果外部存储 ：将路由分析的结果写入到向量数据库中，其他Agent要分析的时候直接到向量库里边查找即可。（我感觉这个还能再优化，得空研究研究）

项目地址：https://github.com/sss12365/SAST2AI

项目细节下边就是AI生成的了

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

项目概述

01

Java-Audit 是一个基于 Joern CPG 静态分析 + Claude AI 语义分析 的 Java Web 应用代码审计工具。CLI 界面，Python 实现，通过 OpenAI 兼容 API 调用 Claude 模型。

核心理念 ：Joern 负责精确的代码属性图分析（数据流追踪、Sink 发现），AI 负责 Joern 无法完成的语义理解（鉴权逻辑、业务漏洞、可控性推理）。两者结果通过 ChromaDB 向量数据库共享，Agent 按需检索，最大限度减少 token 消耗。

---

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

项目结构

```
java-audit/ # 3956 行代码
├── main.py # CLI 入口 (click)
├── config.yaml # 配置文件
├── requirements.txt # Python 依赖
│
├── core/ # 核心引擎层
│ ├── config.py # YAML 配置加载 + Pydantic 校验
│ ├── models.py # 数据模型定义
│ ├── orchestrator.py # 三阶段异步编排器
│ ├── joern_runner.py # Joern CLI 交互封装
│ ├── joern_parser.py # Joern 原始输出压缩器 (99.4% 压缩率)
│ ├── java_compressor.py # Java 源码压缩器 (60-85% 压缩率)
│ └── audit_store.py # ChromaDB 向量知识库
│
├── agents/ # AI Agent 层
│ ├── base.py # BaseAgent (OpenAI SDK 封装)
│ ├── route_analysis.py # 路由分析 Agent
│ ├── route_param.py # 参数追踪 Agent
│ ├── auth_analysis.py # 鉴权分析 Agent
│ ├── hardcoded_audit.py # 硬编码审计 Agent
│ └── vuln_verification.py # 漏洞验证 Agent
│
├── prompts/ # Agent System Prompt
│ ├── route_analysis.md # 路由提取指令
│ ├── route_param.md # 参数追踪 + 可控性分析指令
│ ├── auth_analysis.md # 鉴权绕过检测指令
│ ├── hardcoded_audit.md # 硬编码过滤指令
│ └── vuln_verification.md # 漏洞验证 + PoC 生成指令
│
├── joern_scripts/ # Joern Scala 查询脚本
│ ├── find_routes.sc # 路由发现 (Spring/Servlet/JAX-RS/Struts2)
│ ├── find_sinks.sc # Sink 发现 (SQL/CMD/File/HTTP/XML/...)
│ ├── dataflow_analysis.sc # Source→Sink 污点追踪
│ ├── hardcoded_secrets.sc # 硬编码密钥检测
│ └── find_auth.sc # 鉴权代码定位
│
└── report/ # 报告生成层
    ├── generator.py # Markdown 报告生成器
    └── templates/
        └── report_template.md # 报告模板
```

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

执行流水线

02

```
┌─────────────────────────────────────────────────────────────────┐
│ Stage 0: 预处理与索引 │
│ ┌──────────────────────┐ ┌─────────────────────────────────┐ │
│ │ Java 源码压缩 │ │ Joern 原始输出压缩 │ │
│ │ 565 files → 426 docs │ │ 3.2MB → 18KB (99.4%) │ │
│ │ aggressive compress  │ │ 去噪 + 去重 + 关键步骤提取 │ │
│ └──────────┬───────────┘ └──────────────┬──────────────────┘ │
│ └──────────┬──────────────────┘ │
│ ▼ │
│ ┌──────────────────┐ │
│ │ ChromaDB 向量库 │ │
│ │ source_code 集合 │ │
│ │ joern 集合 │ │
│ └──────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│ Stage 1: 信息收集 (并行) │
│ ┌──────────────────────┐ ┌─────────────────────────────────┐ │
│ │ Route Analysis Agent │ │ Joern Full Scan                 │ │
│ │ AI 提取路由+参数 │ │ CPG 构建 → 路由/Sink/数据流 │ │
│ │ 压缩源码 60K chars   │ │ 或加载已有 joern-raw-output     │ │
│ └──────────┬───────────┘ └──────────────┬──────────────────┘ │
│ └──────────┬──────────────────┘ │
│ ▼ 写入 routes / joern 集合 │
├─────────────────────────────────────────────────────────────────┤
│ Stage 2: 深度分析 (并行) │
│ ┌──────────────────────┐ ┌─────────────────────────────────┐ │
│ │ Route Param Agent    │ │ Auth Analysis Agent             │ │
│ │ 从 store 按批加载路由 │ │ 从 store 检索 Filter/Config 代码 │ │
│ │ 检索相关 ServiceImpl │ │ 语义匹配鉴权相关 Joern 发现 │ │
│ │ 追踪 Source→Sink     │ │ URI 绕过 + CVE + 架构分析 │ │
│ └──────────┬───────────┘ └──────────────┬──────────────────┘ │
│ └──────────┬──────────────────┘ │
│ ▼ 写入 dataflows / auth 集合 │
├─────────────────────────────────────────────────────────────────┤
│ Stage 3: 验证与报告 (并行) │
│ ┌──────────────────────┐ ┌─────────────────────────────────┐ │
│ │ Hardcoded Audit Agent│ │ Vuln Verification Agent         │ │
│ │ Joern 结果语义过滤 │ │ 从 store 只加载 HIGH+ 发现 │ │
│ │ 排除误报 │ │ 检索可控 dataflow               │ │
│ └──────────┬───────────┘ │ 代码证据验证 │ │
│ │ │ CVSS 三维评分 │ │
│ │ │ 生成 PoC + 伪代码 │ │
│ │ └──────────────┬──────────────────┘ │
│ └──────────┬──────────────────┘ │
│ ▼ │
│ ┌──────────────────┐ │
│ │ Report Generator  │ │
│ │ Markdown 审计报告 │ │
│ └──────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

核心模块详解

03

1. CLI 入口 ( `main.py` , 144 行)

```
命令:
  scan <project_path>     完整审计
    --config, -c          配置文件路径 (默认 config.yaml)
    --output, -o          输出目录
    --joern-output, -j    已有 Joern 输出文件 (跳过 Joern 扫描)

  check 检查配置和依赖
  parse-joern <file>      独立压缩 Joern 输出
    -output, -o          输出文件
```

伪代码:

```
def scan(project_path, config, output, joern_output):
    cfg = load_config(config) # 加载 YAML
    orchestrator = AuditOrchestrator(cfg) # 初始化编排器
    report = asyncio.run( # 异步执行
        orchestrator.run(project_path, output, joern_output)
    )
    print(f"Report: {report}")
```

2. 配置系统 ( `core/config.py` , 52 行)

```
# config.yaml
model:
  base_url: "https://your-api.com"       # OpenAI 兼容 API 地址
  api_key: "sk-xxx"                       # API 密钥 (或 ANTHROPIC_API_KEY 环境变量)
  model_id: "claude-opus-4-6"             # 模型 ID
  max_tokens: 16000 # 最大输出 token

joern:
  home: "/path/to/joern-cli"              # Joern 安装目录

output:
  dir: "./audit_output"                   # 输出目录 (仅 --output 指定时使用，默认输出到项目 report/)
```

Pydantic 校验:

* api\_key: 为空时自动读取ANTHROPIC\_API\_KEY环境变量
* joern.home: 校验目录存在

3. 数据模型 ( `core/models.py` , 141 行)

```
# 核心数据结构
RouteInfo # 路由: path, method, handler_class, handler_method, params, burp_template
RouteParam # 参数: name, java_type, http_location, required
CallChainNode # 调用链节点: level, class_name, method_name, code_snippet, param_mapping
DataFlowChain # 数据流: source_param → sink_type + chain[] + controllable + pseudocode
Vulnerability # 漏洞: vuln_id, severity_score, poc_request, dataflow_chain, remediation
AuthInfo # 鉴权: framework, version, route_auth_mapping, bypass_findings
HardcodedSecret # 硬编码: secret_type, value_preview(脱敏), file_path
JoernResult # Joern 结果: routes, sinks, dataflows, hardcoded_secrets
AuditReport # 最终报告: 所有结果汇总

# CVSS 三维评分
SeverityScore:
  score = R × 0.40 + I × 0.35 + C × 0.25   # R=可达性, I=影响, C=复杂度 (0-3)
  cvss = score / 3.0 × 10.0
  severity:
    C (Critical): score >= 2.70, CVSS 9.0-10.0
    H (High): score >= 2.10, CVSS 7.0-8.9
    M (Medium): score >= 1.20, CVSS 4.0-6.9
    L (Low): score >= 0.10, CVSS 0.1-3.9

# Sink 类型枚举
SinkType: SQL | COMMAND | HTTP | FILE | XML | LDAP | EXPRESSION | DESERIALIZE | RESPONSE | PATH
```

4. 编排器 ( `core/orchestrator.py` , 220 行)

```
async def run(project_path, output_dir, joern_output_file):
    # 默认输出到 <project_path>/report/，每次清空重建
    output = output_dir or Path(project_path) / "report"
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    store = AuditStore(output / ".audit_store")
    store.reset()

    # Stage 0: 索引源码到向量库
    index_source_code(project_path)
    # → 读取所有 .java → aggressive 压缩 → 存入 source_code 集合

    # Stage 1: 并行
    if joern_output_file:
        # 加载已有 Joern 输出 → 压缩 → 存入 joern 集合
        parsed = parse_joern_output(raw_text)
        compact = to_compact_text(parsed)
        store.store_joern_findings(compact, parsed.findings)
        route_result = await route_agent.analyze...