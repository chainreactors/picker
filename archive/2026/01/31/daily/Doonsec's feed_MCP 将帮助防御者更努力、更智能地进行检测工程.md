---
title: MCP 将帮助防御者更努力、更智能地进行检测工程
url: https://mp.weixin.qq.com/s/C_zDLN4DFpx6jIi1bKywKQ
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:22:43.839965
---

# MCP 将帮助防御者更努力、更智能地进行检测工程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4Ln7j9YplYnKDJsKJvs3QVoIj1wTHX6ibGcuFaHLMZW5wZVvJ0jf0uqmg1XOlH4RLKYM7PqtZjDqPpjE7y6EsWA/0?wx_fmt=jpeg)

# MCP 将帮助防御者更努力、更智能地进行检测工程

原创

网络安全民工
网络安全民工

网络安全民工

![]()

在小说阅读器中沉浸阅读

# 安全检测 MCP

**一个 MCP（模型上下文协议）服务器，允许 LLM 查询Sigma**、**Splunk ESCU**、**Elastic**和**KQL**安全检测规则的统一数据库。

![安装 MCP 服务器](https://mmbiz.qpic.cn/mmbiz_svg/Sqqm3oJYw2hianfBkpbm8Dn0LGmYVvkthQHoSM8fseicC8ozExYiaR8Olv66JC6k9elsLj01jFTuOW6zCic2abBxldxWqNoxgKMI/640?wx_fmt=svg&from=appmsg)

## 🆕 MCP 提示 - 专家检测工作流程

此服务器包含**11 个预置的 MCP 提示，**可为常见的安全检测任务提供结构化的专家级工作流程。您无需费心研究使用哪些工具以及使用顺序，只需按名称请求提示，即可获得全面专业的分析。

### 如何在光标中使用提示

只需告诉克劳德使用某个提示词即可：

```
You: "Use the ransomware-readiness-assessment prompt"
You: "Run apt-threat-emulation for APT29"
You: "Execute the executive-security-briefing prompt for our CISO"
You: "Use detection-engineering-sprint with capacity 5 and focus on ransomware"
```

### 可用提示

| 迅速的 | 描述 | 论点 |
| --- | --- | --- |
| `ransomware-readiness-assessment` | 包含风险评分和补救路线图的全面杀伤链分析 | `priority_focus`预防/检测/应对/全部 |
| `apt-threat-emulation` | 评估针对特定威胁行为者（APT29、Lazarus、Volt Typhoon 等）的防护覆盖范围 | `threat_actor`（必需的），`include_test_plan` |
| `purple-team-exercise` | 生成包含流程和预期检测结果的完整测试计划 | `scope`（战术或技术）`environment` |
| `soc-investigation-assist` | 调查辅助人员，提供分诊指导、问题排查和升级标准。 | `indicator`（必需的），`context` |
| `detection-engineering-sprint` | 优先级排序的检测待办事项，包含用户故事和验收标准 | `sprint_capacity`，`threat_focus` |
| `executive-security-briefing` | 包含业务风险术语和投资建议的高管报告 | `audience`董事会/首席信息安全官/首席技术官`include_benchmarks` |
| `cve-response-assessment` | 快速评估新出现的网络安全威胁和威胁 | `cve_or_threat`（必需的） |
| `data-source-gap-analysis` | 分析遥测需求以提高检测覆盖率 | `target_coverage` |
| `detection-quality-review` | 对特定技术的检测结果进行深入的质量分析 | `technique_id`（必需的） |
| `threat-landscape-sync` | 将检测优先级与当前威胁形势保持一致 | `industry` |
| `detection-coverage-diff` | 将覆盖范围与威胁行为者或基线进行比较。 | `compare_against`（必需的） |

### 示例：勒索软件评估

```
You: "Use the ransomware-readiness-assessment prompt"

Claude will automatically:
1. Get baseline stats with get_stats
2. Analyze ransomware-specific gaps with identify_gaps
3. Review coverage by tactic with analyze_coverage
4. Map gaps to the ransomware kill chain
5. Generate prioritized remediation roadmap
6. Output a professional report with risk scores
```

### 示例：APT威胁评估

```
You: "Run apt-threat-emulation for Volt Typhoon"

Claude will:
1. Research Volt Typhoon using MITRE ATT&CK data
2. Get all 81 techniques attributed to the group
3. Check your detection coverage for each technique
4. Calculate coverage percentage and identify blind spots
5. Generate a purple team test plan (optional)
6. Provide prioritized detection recommendations
```

## 特征

* **🆕 MCP 提示**- 11 个预置的专家工作流程，适用于勒索软件评估、APT 模拟、紫队演练、高管简报等。
* **🆕 MCP 资源**- 无需工具调用即可阅读 LLM 的相关背景信息（统计数据、覆盖率摘要、差距）。
* **🆕 参数补全**- 输入时自动补全技术 ID、CVE 和进程名称
* **🆕 服务器使用说明**- 内置使用指南，包含示例，帮助您更好地理解 LLM
* **🆕 结构化错误**- 提供建议和类似项目的实用错误信息
* **🆕 交互式工具**- 基于表单输入的差距优先级排序和迭代计划（Cursor 0.42+）
* **统一搜索**- 通过单一界面查询 Sigma、Splunk ESCU、Elastic 和 KQL 检测结果
* **全文搜索**- 基于 SQLite FTS5 的搜索功能，支持搜索名称、描述、查询、MITRE 策略、CVE、进程名称等。
* **MITRE ATT&CK 映射**- 按技术 ID 或战术过滤检测结果
* **CVE 覆盖范围**- 查找针对特定 CVE 漏洞的检测结果
* **进程名称搜索**- 查找引用特定进程的检测结果（例如，powershell.exe、w3wp.exe）
* **分析故事**- 按 Splunk 分析故事查询（可选 - 增强上下文）
* **KQL 分类**- 按类别筛选 KQL 查询（Defender For Endpoint、Azure AD、威胁狩猎等）
* **自动索引**- 启动时自动从配置的路径索引检测结果
* **支持多种格式**- YAML（Sigma、Splunk）、TOML（Elastic）、Markdown（KQL）
* **Logsource 过滤**- 按类别、产品或服务过滤 Sigma 规则
* **严重性筛选**- 按严重级别筛选

## 快速入门

### 选项 1：npx（推荐）

无需安装 - 只需配置并运行：

```
npx -y security-detections-mcp
```

### 方案二：克隆并构建

```
git clone https://github.com/MHaggis/Security-Detections-MCP.gitcd Security-Detections-MCP npm install npm run build
```

## 配置

### 光标 IDE

添加到您的 MCP 配置（`~/.cursor/mcp.json`或`.cursor/mcp.json`您的项目中）：

```
{  "mcpServers": {    "security-detections": {      "command": "npx",      "args": ["-y", "security-detections-mcp"],      "env": {        "SIGMA_PATHS": "/path/to/sigma/rules,/path/to/sigma/rules-threat-hunting",        "SPLUNK_PATHS": "/path/to/security_content/detections",        "ELASTIC_PATHS": "/path/to/detection-rules/rules",        "STORY_PATHS": "/path/to/security_content/stories",        "KQL_PATHS": "/path/to/Hunting-Queries-Detection-Rules"       }     }   } }
```

### 克劳德桌面

添加`~/Library/Application Support/Claude/claude_desktop_config.json`：

```
{  "mcpServers": {    "security-detections": {      "command": "npx",      "args": ["-y", "security-detections-mcp"],      "env": {        "SIGMA_PATHS": "/Users/you/sigma/rules,/Users/you/sigma/rules-threat-hunting",        "SPLUNK_PATHS": "/Users/you/security_content/detections",        "ELASTIC_PATHS": "/Users/you/detection-rules/rules",        "STORY_PATHS": "/Users/you/security_content/stories",        "KQL_PATHS": "/Users/you/Hunting-Queries-Detection-Rules"       }     }   } }
```

### Visual Studio Code

添加`~/.vscode/mcp.json`：

```
{  "servers":  {    "security-detections": {      "type": "stdio",      "command": "npx",      "args": ["-y", "security-detections-mcp"],      "env": {        "SIGMA_PATHS":  "/Users/you/sigma/rules,/Users/you/sigma/rules-threat-hunting",        "SPLUNK_PATHS": "/Users/you/security_content/detections",        "ELASTIC_PATHS": "/Users/you/detection-rules/rules",        "KQL_PATHS": "/Users/you/kql-bertjanp,/Users/you/kql-jkerai1",        "STORY_PATHS": "/Users/you/security_content/stories"       }     }   }
```

### WSL 和 Visual Studio Code

添加`~/.vscode/mcp.json`：

```
{  "servers":  {    "security-detections": {      "type": "stdio",      "command": "wsl",      "args": ["npx", "-y", "security-detections-mcp"],      "env": {        "SIGMA_PATHS":  "/Users/you/sigma/rules,/Users/you/sigma/rules-threat-hunting",        "SPLUNK_PATHS": "/Users/you/security_content/detections",        "ELASTIC_PATHS": "/Users/you/detection-rules/rules",        "KQL_PATHS": "/Users/you/kql-bertjanp,/Users/you/kql-jkerai1",        "STORY_PATHS": "/Users/you/security_content/stories"       }     }   }
```

### 环境变量

| 多变的 | 描述 | 必需的 |
| --- | --- | --- |
| `SIGMA_PATHS` | 以逗号分隔的 Sigma 规则目录路径 | 至少需要一个信息来源 |
| `SPLUNK_PATHS` | 以逗号分隔的 Splunk ESCU 检测目录路径 | 至少需要一个信息来源 |
| `ELASTIC_PATHS` | 以逗号分隔的 Elastic 检测规则目录路径 | 至少需要一个信息来源 |
| `KQL_PATHS` | 以逗号分隔的 KQL 查询目录路径 | 至少需要一个信息来源 |
| `STORY_PATHS` | 以逗号分隔的 Splunk 分析故事目录路径 | 否（增强上下文） |

## 获取检测内容

### 快速入门：下载所有规则（复制粘贴）

创建一个`detections`文件夹，并使用稀疏检出方式下载所有源代码（仅下载规则，不下载完整存储库）：

```
# Create detections directorymkdir -p detections &&cd detections# Download Sigma rules (~3,000+ rules)git clone --depth 1 --filter=blob:none --sparse https://github.com/SigmaHQ/sigma.gitcd sigma && git sparse-checkout set rules rules-threat-hunting &&cd ..# Download Splunk ESCU detections + stories (~2,000+ detections, ~330 stories)git clone --depth 1 --filter=blob:none --sparse https://github.com/splunk/security_content.gitcd security_content && git sparse-checkout set detections stories &&cd ..# Download Elastic detection rules (~1,500+ rules)git clone --depth 1 --filter=blob:none --sparse https://github.com/elastic/detection-rules.gitcd detection-rules && git sparse-checkout set rules &&cd ..# Download KQL hunting queries (~400+ queries from 2 repos)git clone --depth 1 https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules.git kql-bertjanp git clone --depth 1 https://github.com/jkerai1/KQL-Queries.git kql-jkerai1echo"Done! Configure your MCP with these paths:"echo"  SIGMA_PATHS: $(pwd)/sigma/rules,$(pwd)/sigma/rules-threat-hunting"echo"  SPLUNK_PATHS: $(pwd)/security_content/detections"echo"  ELASTIC_PATHS: $(pwd)/detection-rules/rules"echo"  KQL_PATHS: $(pwd)/kql-bertjanp,$(pwd)/kql-jkerai1"echo"  STORY_PATHS: $(pwd)/security_content/stories"
```

### 替代方案：完全克隆

如果您需要完整的 Git 历史记录：

```
# Sigma Rulesgit clone https://github.com/SigmaHQ/sigma.git# Use rules/ and rules-threat-hunting/ directories# Splunk ESCUgit clone https://github.com/splunk/security_content.git# Use detections/ and stories/ directories# Elastic Detection Rulesgit clone https://github.com/elastic/...