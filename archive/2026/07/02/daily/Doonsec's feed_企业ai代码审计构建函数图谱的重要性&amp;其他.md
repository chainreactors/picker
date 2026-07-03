---
title: 企业ai代码审计构建函数图谱的重要性&amp;其他
url: https://mp.weixin.qq.com/s/ajMpxJKA13yNU8ZUBXfLng
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:45:16.193007
---

# 企业ai代码审计构建函数图谱的重要性&amp;其他

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vP5icicMocf9jdmBibLpp4ibWotgFLJmM2P2KGy1ISMCtc9fib3Dxq7t57FxxU2LV2DCnIlhskLVBGZzRZicrpYCQZfEQYGcZOemoLS2NvXp209VA/0?wx_fmt=jpeg)

# 企业ai代码审计构建函数图谱的重要性&其他

原创

黎明Lior
黎明Lior

Moonlight安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

函数图谱解决上下文爆炸/语义稀释、Layer 2 预计算替代"超级传播者"、MoE 模式差异化调度、Layer 5 漏洞组合聚变、单次会话 + 思考有界消灭幻觉 —— 本文解释这 5 个看似独立的优化如何**合起来把 AI 审计从"能用"推向"好用"**。![](https://mmbiz.qpic.cn/mmbiz_png/vP5icicMocf9jdicNlv4vsjmA5tdQRbcoTCNVBAmibC8mZsoIeh2HESVZASAGicJy5dqNqFU7oOD3K2sn86TSWEWoyBRegq9LgmJ9AdyziaonNr8Y/640?wx_fmt=png&from=appmsg)

"AI 审计不是调一次 LLM 就完事。
它要解决**上下文爆炸**、**工具调用思考**、**跨文件追踪**、**思考链不可控**、**漏洞组合盲区**、**AI 幻觉**六大问题。
5 个优化就是答案。"—— AI 审计的工程基座

## 16 大 AI 审计工程难题

THE 6 CHALLENGES

把 AI 用于企业级代码安全审计，工程师会立刻撞上 6 个现实问题。每个问题都有对应的优化方案：

![](https://mmbiz.qpic.cn/mmbiz_png/vP5icicMocf9hPFW1869D50o0CgDvZ1N31bBSeE1xcoWc4XWeDsGVo4Mn13Ah4EMv5q3DxEBXw0gHQVPBZ4hXKUfonY1hpN3YKtaqx4yujiaMI/640?wx_fmt=png&from=appmsg)

**关键洞察：**这 6 个问题不是"AI 不够强"，而是**"没给 AI 合适的工程支撑"**。 本系统用 5 大优化解决它们：函数图谱、Layer 2 预计算、MoE 模式、Layer 5 组合、**单次会话 + 思考有界（消灭幻觉）**。

## 2优化 A：函数图谱 + RAG → 解决上下文爆炸 + 工具调用

FUNCTION GRAPH AS RAG

"LLM 不该去'找代码'。
函数图谱把代码组织好，**LLM 只做判断**。"

### 2.1 上下文爆炸：LLM 看不完 1000 个 API

1000

接口全量代码（行）

~50万

代码行 token 估算

~150万

token / 喂全量一次

🔴 超限

GPT-4 / Claude 也吃不下

**粗暴做法：**每次 LLM 调用前裁剪代码 → 漏掉关键调用链 → 漏判。
**正确做法：**用函数图谱做 RAG，喂相关代码，**不喂无关代码**。

### 2.2 函数图谱 = 精简版的代码上下文

```
# 传统方式：把整个 Service 文件塞进 LLM
prompt = f"""
请审计 UserService.java 的安全漏洞：
{open('UserService.java').read()}  # 500 行
"""
# → 🔴 token 爆炸，思考混乱

# 优化方式：函数图谱 RAG（只喂相关的）
call_graph = build_graph(API='/api/user/update')
# → 只提取 update() 函数的调用链：
#    Controller.update → Service.update → Repository.updateById → JDBC.execute
#    每个节点附带：函数签名 + 关键代码片段（5-20 行）

prompt = f"""
API: POST /api/user/update
调用图谱:
{call_graph.to_compact()}

请基于图谱判断 SQL 注入风险。
"""
# → 🟢 token -70%，专注度 +200%
```

### 2.3 函数图谱 3 重收益

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vP5icicMocf9j4ch6ViaqcwL4HEozSs9L7o5QIfdEK2nic01o3E8fsslSDY5Us7MP0kx39IbwQ4QbicN11ndpAL0yTndLhSweKibiaP83iaLKuAMDxQ/640?wx_fmt=png&from=appmsg)

### 2.4 RAG 优化前后对比

| 指标 | 无图谱（粗暴截断） | 函数图谱 RAG | 改善 |
| --- | --- | --- | --- |
| 单次 LLM 输入 token | ~50万（全量代码） | ~1-2万（裁剪后） | 🟢 -96% |
| 工具调用次数 / 漏洞 | 3-8 次 | 0-1 次 | 🟢 -85% |
| 跨文件追踪准确度 | ~40%（漏报多） | ~95%（图谱已组装） | 🟢 +55% |
| 1000 接口总 token | ~1-2亿（天文数字） | ~3000万 | 🟢 -94% |
| 思考聚焦度 | 分散（整理+判断） | 聚焦（只判断） | 🟢 质量↑ |

### 2.5 关键字匹配优化：进一步筛选

即使有了图谱，**关键字匹配**仍然是加速的关键。具体做法：

```
# 提取 API 的核心关键字
def extract_keywords(api: API) -> set:
    code = get_code(api.endpoint)
    keywords = set()
    # 1. 方法名关键词
    for word in re.findall(r'\b[a-z][a-zA-Z]+(?=\()', code):
        keywords.add(word)  # delete, query, update, etc.
    # 2. SQL 关键字
    for word in re.findall(r'(SELECT|INSERT|UPDATE|DELETE|FROM|WHERE)', code, re.I):
        keywords.add(word.lower())
    # 3. 已知漏洞关键字（来自 vulnerability_types.py）
    for type_name, type_keywords in VULNERABILITY_KEYWORDS.items():
        for kw in type_keywords:
            if kw in code:
                keywords.add(f"{type_name}:{kw}")
    return keywords

# 在 LLM 审计前预过滤：哪些漏洞类型真正相关
def should_audit(api, vuln_type):
    if vuln_type in ALWAYS_SCAN_ALL_TASKS:  # A 档：全开
        return True
    if vuln_type in SAST_ONLY_TASKS:        # C 档：SAST 接管
        return False
    return vuln_type in api.keywords        # B 档：关键字命中才扫
```

**关键字匹配的核心价值：**B 档任务从"无脑全开"变成"按需触发"。一个 API 平均只触发 5-8 类审计，而不是 32 类。**Token 再降 70%**。

### 2.6 灵感延伸：NodeJS 工具找调用链

前端代码经过 webpack/vite 打包后，函数名会被混淆。但有个灵感——

**思路：**用 NodeJS 生态的工具（如 `@babel/traverse` + `source-map-resolve`）**还原混淆前的调用图**。 这样前端代码审计也能享受函数图谱的优势 —— 跨文件、跨 bundle 的污染链追踪成为可能。

## 3优化 B：Layer 2 预计算 → 从"超级传播者"到调用链裁剪

LAYER 2 PRE-COMPUTATION

"超级传播者不好用 → **淘汰**。
但它的核心逻辑保留：Layer 2 预计算调用关系 → RAG → 调用链裁剪 + 用户输入可达性。"

### 3.1 超级传播者的故事：淘汰但留下了什么

#### 📋 超级传播者（Super Spreader）：曾经尝试过的方案

原方案的问题 **目标：**把"被很多 API 调用的核心函数"作为审计重点。
**做法：**统计每个函数被调用次数 → 找出 top N 超级传播者 → 重点审计。
**失败原因：**

* 调用次数多 ≠ 漏洞多（`toString()` 被调一万次，但不是漏洞源）
* 忽略调用上下文（同样的函数在不同上下文安全性不同）
* 工程师反馈：**"看着高大上，实际没啥用"**

**结论：**淘汰

保留的核心思路 **真正有价值的是什么？**

* **调用关系预计算**

  → 应该在 Layer 2 而不是 Layer 4
* 调用链 + 用户输入可达性 = 真正的污染链
* 把"调用次数最多"换成"被最多 **用户输入路径** 经过"

**新方案：**Layer 2 预计算 RAG

### 3.2 新方案：Layer 2 预计算 + RAG 数据库

Layer 2 预计算流程

![](https://mmbiz.qpic.cn/mmbiz_png/vP5icicMocf9hVMsZh5Tc880gXKRnSfQoRXibwE6uYE80W1vjWicHn6tk3qMrowWf7Y5kFmJDLHx1VGfRv4DntORTBBmSicuK38uiaBVdpicskZPNs/640?wx_fmt=png&from=appmsg)

### 3.3 函数嵌入 + 相似性聚类：审计一个推断其他

这是 Layer 2 的核心魔法：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vP5icicMocf9gK9bpUasqkNUJEPaQJiayNWTZFfuXv1dLCfDFO7JTsXnYBC6OfLQc7TYiacIq41pvu4QIQ79e4vgY7nLUGvnUGoyAC5BzgPKyGw/640?wx_fmt=png&from=appmsg)

### 3.4 调用链裁剪 + 用户输入可达性

```
# Layer 2 预提取的 RAG 数据长这样
{
    "api": "POST /api/user/update",
    "call_chain": [
        {
            "node": "UserController.update",
            "user_reachable": true,        # ✅ 标记：用户输入可达
            "auth_protected": true,
            "depth": 0
        },
        {
            "node": "UserService.update",
            "user_reachable": true,        # ✅ 继承自父节点
            "input_sanitized": false,
            "depth": 1
        },
        {
            "node": "PermissionCheck.checkId",
            "user_reachable": false,       # ❌ 系统内部权限检查
            "trusted": true,
            "depth": 2
        },
        {
            "node": "JdbcTemplate.execute",
            "user_reachable": true,        # ✅ 危险 sink
            "sink_type": "sql_execution",
            "parametrized": false,         # ← 关键：未参数化
            "depth": 3
        }
    ]
}

# 调用链裁剪：去掉 user_reachable=False 的分支
# 只保留 user_reachable=True 的节点 → 污染链确认
```

**裁剪意义：**原本 5-8 个节点的调用图，裁剪后只剩 3-4 个用户输入相关的。
LLM 看到的图谱 = **真实可利用的攻击路径**，不是无关代码的干扰。

### 3.5 越权漏洞的强制全开：AI 最强

```
ALWAYS_SCAN_ALL_TASKS = {
    'business_logic_task',      # 业务逻辑漏洞
    'authorization_task',       # 授权安全 ← 越权
    'authentication_task',      # 认证安全
    'race_condition_task',      # 竞态条件
}

# 越权漏洞强制全开，绕过关键字过滤
# 原因：业务理解 + 上下文推理 = AI 最强
# 一旦错过 = 灾难级风险

def should_audit(api, vuln_type):
    if vuln_type in ALWAYS_SCAN_ALL_TASKS:
        return True   # ✅ 强制全开，不管有没有关键字命中
    # ... 其他逻辑
```

**为什么越权必须全开？** 越权漏洞 100% 需要业务上下文判断："这个用户能不能访问这个资源？"关键字匹配根本看不出。**只有 LLM 能判**，所以必须全开。

## 4优化 C：MoE 模式 → 漏洞类型差异化调度

MIXTURE OF EXPERTS

"不是所有漏洞都需要 LLM。
**让 AI 做 AI 该做的，SAST 做 SAST 该做的**。"

### 4.1 MoE：每个漏洞类型 = 一个"专家"

借鉴 LLM 界的 **Mixture of Experts (MoE)** 思想 —— 不同漏洞类型走不同调度策略：前提是构建了api代码图谱

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vP5icicMocf9jDJv1pfmsU6PicUtBpQhSc0bx2o0YVIPuxn5U7kMgMPTNjytnuiauCjtMJGRic0Ulh8mDFNJ8U0JqpT1iaH8JwRrC8I8Gl6icxVOpQ/640?wx_fmt=png&from=appmsg)

### 4.2 三档调度的实现

| 档位 | 类型示例 | 触发条件 | 处理方式 |
| --- | --- | --- | --- |
| A 档 | 业务逻辑 / 授权 / 认证 / 竞态 | **必扫** ，绕过关键字过滤 | LLM 全量判断（AI 最强） |
| B 档 | SQL 注入 / XSS / SSRF / IDOR / 路径穿越等 | 关键字命中才扫 | LLM 按需审计 |
| C 档 | 依赖组件 / 密钥 / 加密 / 配置 | **永远不调 LLM** | SAST 引擎直接接管 |

### 4.3 强度模式可调 → 流程可传入 Layer 4

同一个项目不同场景，需要不同的"扫描强度"：

```
# 配置扫描强度模式
audit_configs = {
    'light':  {
        'A_tier': True,                  # A 档必开
        'B_tier_filter': 'strict',       # B 档严格关键字（少触发）
        'C_tier_sast': True,             # C 档 SAST
        'max_iterations': 5,             # 思考深度限制
    },
    'standard': {
        'A_tier': True,
        'B_tier_filter': 'normal',       # B 档正常关键字
        'C_tier_sast': True,
        'max_iterations': 12,            # 平衡
    },
    'deep': {
        'A_tier': True,
        'B_tier_filter': 'loose',        # B 档宽松关键字（多触发）
        'C_tier_sast': True,
        'max_iterations': 25,            # 深度思考
        'call_chain_analysis': True,     # 调用链深度分析
    },
}

# 通过流程传入 Layer 4
def run_layer4(intensity='standard'):
    config = audit_configs[intensity]
    for vuln_type in get_active_tasks(config):
        audit_one_vuln(api, vuln_type, config)

# CI/CD 调用方式
python run_flow.py --intensity light         # 每次 PR
python run_flow.py --intensity standard      # 每周
python run_flow.py --intensity deep          # 上线前
```

**已实现：**通过 AI 识...