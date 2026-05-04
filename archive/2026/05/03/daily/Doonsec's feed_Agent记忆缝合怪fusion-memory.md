---
title: Agent记忆缝合怪fusion-memory
url: https://mp.weixin.qq.com/s/vTiS6rVoFhjUIqAK7W1GXw
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:28:55.912078
---

# Agent记忆缝合怪fusion-memory

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImnPWk77o7PCplnCwraTO51HXLJSDx3OEegBudhjM3EXMynxvklvXZvCjeN1ZxRtUqOfjwZjJqU147IwkoYP6v0SmwMV5FmBo5w/0?wx_fmt=jpeg)

# Agent记忆缝合怪fusion-memory

原创

鸿渐
鸿渐

爱唠叨的Nil

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CBe66ugaImlI2vzk5Bk3f9Hicm0zzicPqRd9cpm2Ebgz25JxIiaewjmVk6tTCiampMEntZcULkAHXqdSM4e9ZUIEXdGvxsBvrMUBDwnyISfN46Y/640?wx_fmt=jpeg&from=appmsg)

项目起源于扣子的项目，起初想法很简单，将虾评的所有跟记忆相关的skill，学习一遍，然后融合成一个全新的skill。 第一版的时候使用起来，感觉一般般，没有什么特别的地方。 后续在扣子冲了积分之后，发现用不完，于是想着根据虾评的评论，不断迭代这个skill，目前已经迭代了15个版本

![](https://mmbiz.qpic.cn/mmbiz_png/CBe66ugaImnUTx7CJiafCxZMAdEX6s55zU4yibWJgGAPFPu9Fqt9EWKmHff3FJfrD33OnqPG0WjwKtCYqibw4UCaFQNhA0TDia0UYSWRobsm1gU/640?wx_fmt=png&from=appmsg)

在迭代到这个版本的时候，将它放在gitee上开源。并且在我的hermes里面实际应用起来了，欢迎大家提出宝贵的意见!

# 融合记忆系统 (Fusion Memory)

**集百家之长，~~打造零依赖~~、自进化的AI记忆系统**

---

## 🆕 多平台适配版 (v1.3.0)

v1.3.0 重磅更新，全面适配 Hermes / OpenClaw / CoPaw 等主流 Agent 框架：

* ✅ 新增 REST API 服务（零依赖，基于 http.server）
* ✅ 新增 MCP (Model Context Protocol) 适配器（stdio + HTTP 双模式）
* ✅ 新增多格式桥接器（hermes / copaw / openclaw / json 互转）
* ✅ 新增可选 SQLite 后端（与 Hermes 存储架构对齐）
* ✅ 所有 v1.x API 保持向后兼容

---

## 🎯 你能用它做什么

> 💡 **非技术用户提示**：本技能主要面向 AI Agent 开发者。如果你只是想找一个笔记软件，建议使用 Notion、Obsidian 等现成工具。如果你正在开发或使用 AI Agent，这个技能可以帮助你的 Agent "记住"主人的偏好、历史交互和经验教训。

| 场景 | 示例 | 一句话说明 |
| --- | --- | --- |
| 记住主人偏好 | `m.add("主人喜欢简洁风格")` | 下次回复自动调整 |
| 记录失败教训 | `m.add("文件操作先检查目录", {"type":"lesson"})` | 避免重复踩坑 |
| 跨会话记忆 | `m.search("上次讨论的AI方案")` | 新会话也能找到 |
| 自动进化 | `m.evolve()` | 从错误中学习变聪明 |

## 📖 一分钟极速入门

### 第一步：复制文件（10秒）

```
# 复制技能文件夹
cp -r fusion-memory-skill ./skills/

# 创建记忆存储目录
mkdir -p memory
```

### 第二步：开始使用（30秒）

```
from fusion_memory import FusionMemory

# 初始化
memory = FusionMemory("./memory")

# 记录重要的事情
memory.add("主人叫云彩收集者")
memory.add("主人偏好简洁直接的回复")
memory.add("遇到文件操作记得先检查目录", {"type": "lesson"})

# 需要时搜索
results = memory.search("主人叫什么名字")
print(results)

# 让系统从错误中学习
stats = memory.evolve()
```

### 常见问题

**Q: 需要安装额外依赖吗？**A: 核心功能零依赖，直接用。如需语义检索：`pip install sentence-transformers`

**Q: 数据存在哪里？**A: 本地 `./memory/` 文件夹，纯文件存储，完全可控

**Q: 和Mem0比有什么区别？**A: 完全免费、支持自进化、零外部依赖

---

## 🔌 多平台快速集成（v1.3.0）

Fusion Memory 现在提供三种标准化接入方式，完美适配 **Hermes**、**OpenClaw**、**CoPaw** 及任何支持 HTTP/MCP 的 Agent 框架。

### 方式一：REST API（最通用）

```
# 启动零依赖 REST 服务
python -m adapters.rest_api --port 8745 --memory ./memory
```

任何平台都可以通过 HTTP 调用：

```
curl -X POST http://127.0.0.1:8745/memory/add \
  -H "Content-Type: application/json" \
  -d '{"content": "主人偏好简洁风格", "options": {"type": "fact"}}'

curl "http://127.0.0.1:8745/memory/search?q=主人偏好"
```

### 方式二：MCP 协议（推荐用于 Hermes）

在 Hermes 配置中添加：

```
{
  "mcpServers": {
    "fusion_memory": {
      "command": "python",
      "args": ["-m", "adapters.mcp_server", "--memory", "./memory"]
    }
  }
}
```

Hermes 即可通过标准 MCP Tools 调用 Fusion Memory。

### 方式三：格式桥接（数据互通）

```
from fusion_memory import FusionMemory
from adapters.format_bridge import ImportExportManager

memory = FusionMemory("./memory")
mgr = ImportExportManager(memory)

# 从 CoPaw 导入
mgr.import_data(copaw_json, "copaw")

# 导出为 Hermes 格式
hermes_data = mgr.export_data("hermes")
```

支持格式：`fusion`（原生）、`hermes`、`copaw`、`openclaw`、`json`。

### 方式四：SQLite 后端（与 Hermes 对齐）

```
# SQLite 统一后端：所有记忆存入单一 SQLite 数据库
memory = FusionMemory("./memory", backend="sqlite")

# Hybrid 混合后端：文件透明 + SQLite 索引
memory = FusionMemory("./memory", backend="hybrid")
```

---

## 🚀 完整使用指南

### 安装

```
# 复制到项目
cp -r fusion-memory-skill ./skills/

# 创建记忆目录
mkdir -p memory
```

### 快速调用（Python）

```
from fusion_memory import FusionMemory

m = FusionMemory('./memory')
m.add('主人喜欢简洁的回复')
print(m.search('主人的偏好'))
```

### 常见使用场景

| 场景 | 代码 |
| --- | --- |
| 记录主人偏好 | `m.add("主人偏好简洁风格")` |
| 记录经验教训 | `m.add("文件操作先检查目录", {"type": "lesson"})` |
| 搜索记忆 | `results = m.search("主人的偏好")` |
| 自进化 | `stats = m.evolve()` |

```
from fusion_memory import FusionMemory

memory = FusionMemory("./memory")

# === 添加各类记忆 ===

# 添加对话记忆
memory.add(
    "主人今天讨论了融合记忆系统的设计",
    options={"entities": [["主人"], ["融合记忆"]], "type": "discussion"}
)

# 添加事实/知识
memory.add(
    "主人偏好简洁的对话风格",
    options={"entities": [["主人"], ["对话风格"]], "type": "fact"}
)

# 添加规则/教训
memory.add(
    "以后遇到文件操作时记得先检查目录是否存在",
    options={
        "entities": [["文件操作"]],
        "type": "lesson",
        "severity": "high"
    }
)

# === 检索记忆 ===

# 多策略搜索
results = memory.search("主人的记忆系统偏好", {
    "strategies": ["bm25", "graph", "temporal"],
    "rerank": True,
    "top_k": 10
})

# === 自进化 ===
stats = memory.evolve()
print(f"扫描: {stats['scans']}, 晋升: {stats['promoted']}")
```

---

## 核心特性

| 特性 | 来源 | 说明 |
| --- | --- | --- |
| 文件即记忆 | 鸿渐 | 零依赖，纯文件存储 |
| 四层存储 | Letta | 工作/情景/语义/程序性 |
| 编译真相 | 鸿渐 | 可更新策略 + 不可变历史 |
| 伤疤自进化 | 鸿渐 | 从失败中学习 |
| DataPoint | Cognee | 原子知识单元 |
| index\_fields | Cognee | 控制检索粒度 |
| 自动提取 | Mem0 | ADD/UPDATE/DELETE/NOOP |
| 时序有效期 | Zep | 事实有效期窗口 |
| 多策略检索 | Hindsight | 4路并行 + 重排 |

---

## 文件结构

```
memory/
├── working.json           # L1工作记忆
├── episodic/              # L2情景记忆
│   └── 2026-04/
│       └── 17.md
├── semantic/              # L3语义记忆
│   ├── entities.md        # 实体索引
│   ├── facts.md           # 事实列表
│   └── compiled.md        # 编译真相
├── procedural/            # L4程序性记忆
│   ├── scars.md           # 伤疤触发器
│   └── rules.md           # 行为规则
├── index/                 # 索引层（可选）
└── config.yaml           # 配置文件
```

---

## 与其他方案的对比

| 维度 | 融合记忆 | Mem0 | Cognee | 鸿渐原生 |
| --- | --- | --- | --- | --- |
| 零依赖 | ✅ | ❌ | ❌ | ✅ |
| 自动提取 | ✅ | ✅ | ✅ | ❌ |
| 自进化 | ✅ | ❌ | ❌ | ✅ |
| 多策略检索 | ✅ | ⚠️Pro版 | ⚠️ | ❌ |
| 时序有效期 | ✅ | ❌ | ❌ | ❌ |
| 编译真相 | ✅ | ❌ | ❌ | ✅ |
| 伤疤触发器 | ✅ | ❌ | ❌ | ✅ |
| 月成本 | **免费** | $249(Pro) | 免费 | 免费 |

---

## 启用向量检索（可选）

向量检索需要额外安装依赖，但保持零依赖核心设计：

```
pip install sentence-transformers
```

修改 `config.yaml`：

```
search:
  vector_enabled: true
  vector_model: "paraphrase-multilingual-MiniLM-L12-v2"
```

---

## 迁移指南（从其他系统迁移）

如果已有其他记忆系统的数据，我们提供了详细的迁移指南：

📄 **完整迁移文档**：references/migration.md

### 支持的迁移来源

| 源系统 | 迁移难度 | 说明 |
| --- | --- | --- |
| Mem0 | ⭐ | API映射，代码改动小 |
| 简单文件存储 | ⭐⭐ | 需要遍历读取再导入 |
| Letta | ⭐⭐ | 概念映射见迁移文档 |
| 其他Agent框架 | ⭐⭐⭐ | 需要根据具体情况处理 |

### 快速迁移示例

```
# Mem0 → Fusion Memory
from mem0 import Memory
from fusion_memory import FusionMemory

# 读取Mem0数据
mem0_client = Memory()
old_memories = mem0_client.get_all(user_id="xxx")

# 导入Fusion Memory
fusion = FusionMemory("./memory")
for mem in old_memories:
    fusion.add(mem["content"], {
        "entities": [[mem["user_id"]], [mem.get("category", "")]],
        "type": "migrated"
    })
```

---

## 版本历史

| 版本 | 日期 | 更新内容 |
| --- | --- | --- |
| **v1.3.0** | **2026-05-01** | **多平台适配层：REST API + MCP + 格式桥接 + SQLite后端** |
| v1.2.1 | 2026-04-30 | 新增5步快速开始清单、完整Agent集成示例、优化OpenClaw格式 |
| v1.2.0 | 2026-04-17 | 新增L5程序化记忆、L6冷库归档、惰性加载、FTS5全文检索、上下文压缩 |
| v1.1.2 | 2026-04-22 | 新增实用场景代码示例，优化向量检索说明，强化迁移指南引用 |
| v1.1.1 | 2026-04-20 | README大幅优化，新增「三分钟入门」教程和常见问题FAQ |
| v1.1.0 | 2026-04-18 | 添加快速入门指南，统一Python示例，添加迁移指南 |
| v1.0.2 | 2026-04-17 | 添加向量检索支持 |
| v1.0.0 | 2026-04-17 | 初始版本 |

---

## 技术架构

详细技术文档请参考 references/architecture.md

---

**相关资源：**

* 技能页面：https://xiaping.coze.site/skill/0b8a6f5a-c4dc-4b3a-8ed8-72776be5d31a
* 开发者：https://xiaping.coze.site/developer/3c76f5cc-bd62-4690-88da-b99f03d819ff

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

爱唠叨的Nil

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Eic0kibODiaic3cnib21814uBlib0RxYwbFZILry66UgHqsZlvOSBByNwCXtjpcFXFhjtcmLx8FpFgVDgPASPuo2YT4w/0?wx_fmt=png)

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