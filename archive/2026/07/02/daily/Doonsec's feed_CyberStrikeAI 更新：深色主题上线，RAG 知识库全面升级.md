---
title: CyberStrikeAI 更新：深色主题上线，RAG 知识库全面升级
url: https://mp.weixin.qq.com/s/BHtENQayhsF5EUZ-_jSxXg
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:44:11.677734
---

# CyberStrikeAI 更新：深色主题上线，RAG 知识库全面升级

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ufQ2xnAD33szHCGonluMNhceFicuGmGrwZ4vC80EcicmRvgdGyib8m8m92elibNYBluIcLyNiaVe0v2h4EnQk8Dh8LyVJkTUc5EoWIGESiaeialicU0/0?wx_fmt=jpeg)

# CyberStrikeAI 更新：深色主题上线，RAG 知识库全面升级

原创

学安全也就图一乐
学安全也就图一乐

低调学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 更适合深夜挖洞的眼睛，也更懂安全问题的知识引擎。

---

## 一、写在前面

做安全测试的人，大概都经历过这样的夜晚：屏幕亮得刺眼，终端、Burp、浏览器、AI 对话窗口来回切换，眼睛越来越酸，效率却越来越高。

**CyberStrikeAI** 最新版本带来两项重要更新：**全站深色主题**，以及基于 **CloudWeGo Eino** 重构的 **RAG 知识检索管线**。一个照顾你的用眼体验，一个提升 AI 在安全场景下的「专业判断力」。

如果你已经在用 CyberStrikeAI，这次更新值得立刻升级体验；如果还在观望，不妨从这两个能力开始了解它。

---

## 二、深色主题：为长时作战而生

### 为什么要有深色模式？

安全测试往往不是「打开网页点两下」就能结束。渗透、漏洞验证、攻击链梳理、批量任务排队执行……动辄数小时连轴转。浅色界面在暗光环境下刺眼，深色主题能：

* **减轻视觉疲劳**，更适合夜间值守与长时间盯屏
* **降低屏幕眩光**，多窗口并排时更舒服
* **统一作战氛围**，控制台、对话页、文档页风格一致

### 三种模式，一键切换

CyberStrikeAI 支持 **跟随系统 / 浅色 / 深色** 三种主题偏好：

| 模式 | 说明 |
| --- | --- |
| 跟随系统 | 自动匹配操作系统深浅色设置 |
| 浅色 | 经典明亮界面，适合白天与演示场景 |
| 深色 | 低对比护眼风格，适合深夜与机房环境 |

点击界面右上角 **主题切换按钮**，即可在三种模式间循环切换。你的选择会保存在本地，下次打开自动恢复，无需重复设置。

### 覆盖范围

深色主题已覆盖平台核心界面，包括：

* 系统仪表盘
* Web 控制台与对话页
* 任务管理、漏洞管理、知识库等模块
* API 文档页

从宏观态势到细节操作，**整站视觉体验统一**，不再出现「主界面是深色、某个子页面突然闪白」的割裂感。

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33shAC7tUfsPzXwjEg5WCa7asLtQkvgHsr7ibZc3BpbfonMbXW4HIWmWIDoGoEvEiaLnyAkiaiameZ78Fhvq6KAOqANubu696s2d1s0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33urOBpWhjwbrBC0tMVxDDiac7TCVHSzZndQutqe6XC9su4RSyhibm1bUvEREDcaJnSDOck3bgRKj0icxA13fpwQqK7YBx4EIneqAA/640?wx_fmt=png&from=appmsg)

---

## 三、RAG 升级：让 AI 更懂安全知识

知识库一直是 CyberStrikeAI 的核心能力之一。智能体在测试过程中可以调用 `search_knowledge_base`，检索 SQL 注入、XSS、API 安全、云安全等领域的沉淀知识。

**这一次，我们把整条 RAG 管线搬到了 Eino 上，检索链路更完整、结果更精准、工程上更稳健。**

### 新管线一览

```
用户提问
   ↓
MultiQuery（LLM 查询改写，生成多条语义变体）
   ↓
多路向量检索 + 候选融合
   ↓
HTTP 精排（DashScope gte-rerank / Cohere 兼容接口）
   ↓
后处理（去重、字符/Token 预算、Top-K 截断）
   ↓
注入对话上下文，辅助 AI 决策
```

### 四大升级点

**1. MultiQuery 查询改写（始终启用）**

用户往往不会把问题问得「刚刚好」。同一句「怎么绕过 WAF 测 SQL 注入」，换个说法、换个角度，向量检索的召回结果可能天差地别。

MultiQuery 会由 LLM 自动生成最多 4 条语义变体，**多路检索再融合**，显著提升召回率——尤其是专业术语多、表述方式杂的安全领域。

**2. HTTP 精排，结果更贴题**

向量检索擅长「找相关」，但不总能保证「最相关」排在最前。升级后的管线在召回之后增加 **HTTP 精排** 环节：

* 阿里云 DashScope：`gte-rerank`
* 兼容 Cohere 的 `/v1/rerank` 端点

精排会根据 query 与文档片段的语义相关性重新排序，把真正有用的知识片段顶到前面。

**更关键的是：精排失败时自动降级为融合排序，检索不会中断。** 工程上追求「宁可略逊一筹，也不让功能挂掉」。

**3. Eino Compose 索引流水线**

索引侧同样基于 **Eino Compose** 构建，对 `knowledge_base/` 下的 Markdown 文档：

* 按标题结构切分
* 递归分块（可配置 chunk\_size / overlap）
* 自动构建向量嵌入索引

知识更新后，索引流程更清晰、可维护性更好。

**4. 更灵活的后处理与配置**

在 `config.yaml` 中可精细调控：

* `multi_query.max_queries`：改写变体数量
* `post_retrieve.prefetch_top_k`：每条变体的向量候选数
* `post_retrieve.max_context_chars / max_context_tokens`：注入上下文的长度预算
* `similarity_threshold`：相似度过滤阈值

Web 设置页也支持可视化配置 MultiQuery、精排、预取候选数等参数，**不用改配置文件也能调优**。

### 对实战意味着什么？

| 场景 | 升级后的体验 |
| --- | --- |
| 遇到陌生漏洞类型 | AI 能召回更全面的知识片段，减少「胡编乱造」 |
| 复杂攻击链推演 | 精排把最相关的 Payload、Bypass 技巧排在前面 |
| 团队知识沉淀 | Markdown 知识库自动索引，检索日志可审计 |
| 快速上手 | Releases 提供预构建 `knowledge.db`，下载即用 |

---

## 四、如何体验

### 深色主题

升级/拉取最新代码后启动服务，打开 Web 界面，点击右上角主题按钮即可切换。**零配置，开箱即用。**

### RAG 知识库

**方式一：使用预构建知识库（推荐新手）**

1. 从 GitHub Releases 下载 `knowledge.db`
2. 放到项目 `data/` 目录
3. 在 `config.yaml` 中设置 `knowledge.enabled: true` 并配置嵌入模型
4. 重启服务

**方式二：自建知识库**

1. 将 Markdown 文档放入 `knowledge_base/` 目录
2. 配置 `embedding` 相关参数
3. 通过 Web 知识库管理界面触发索引

智能体在对话中会自动调用 `search_knowledge_base`，你也可以在设置页查看检索日志，调试召回效果。

---

## 五、写在最后

CyberStrikeAI 的定位从未改变：**做安全团队的 AI 原生测试平台**——100+ 工具编排、MCP 协议、多代理协同、攻击链可视化、漏洞全生命周期管理，以及面向授权场景的内置 C2 能力。

深色主题，是对「人」的体贴；RAG 升级，是对「智」的加码。

如果你正在构建自己的 AI 红队/蓝队工作流，欢迎 Star、Fork、提 Issue，也欢迎加入社区一起打磨：

* **GitHub**：https://github.com/Ed1s0nZ/CyberStrikeAI
* **Discord**：https://discord.gg/8PjVCMu8Zw
* **微信群**：见项目 README 二维码

---

**CyberStrikeAI** —— 让 AI 成为你最靠谱的安全搭档。

*本文档版本：2026-07 · 深色主题 & Eino RAG 管线升级*

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

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