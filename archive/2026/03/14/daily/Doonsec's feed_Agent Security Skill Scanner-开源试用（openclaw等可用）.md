---
title: Agent Security Skill Scanner-开源试用（openclaw等可用）
url: https://mp.weixin.qq.com/s/CUv8FRyeMK9tNziNKhNKxg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:28:56.958808
---

# Agent Security Skill Scanner-开源试用（openclaw等可用）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5f9ibvu2qYVIkr2AueG8ibCicTm7o1sce4EM9XE70KsBIDWO3eo1DF3D1JkuGAY93ibnJnn8BMXg0yQJH6MOhAibNZAXPRGZ8rK6CcpkD8Urnyeo/0?wx_fmt=jpeg)

# Agent Security Skill Scanner-开源试用（openclaw等可用）

原创

小东
小东

小东安全日记

![]()

在小说阅读器中沉浸阅读

# - 对外发布说明

> **版本**: v2.0.1-beta
> **发布日期**: 2026-03-14

---

## 📌 项目简介

**Agent Security Skill Scanner** 是一款 AI Agent 技能安全扫描工具，用于检测恶意技能、后门代码、权限滥用等安全风险。

⚠️ **Beta 版本**: 此版本为公开测试版，可能存在未知问题，生产环境请谨慎使用。

https://github.com/caidongyun/agent-security-skill-scanner.git

https://gitee.com/caidongyun/agent-security-skill-scanner.git

---

## 🎯 核心功能

📋 规则分类汇总

| 分类 | 规则数 | 权重 | 严重性分布 |
| --- | --- | --- | --- |
| 恶意代码检测 | 12 条 | 30% | 4 CRITICAL, 3 HIGH, 5 MEDIUM |
| 后门模式检测 | 10 条 | 25% | 4 CRITICAL, 4 HIGH, 2 MEDIUM |
| 权限滥用检测 | 9 条 | 20% | 2 CRITICAL, 4 HIGH, 3 MEDIUM |
| 硬编码凭据检测 | 15 条 | 25% | 4 CRITICAL, 8 HIGH, 3 MEDIUM |
| 数据泄露检测 | 8 条 | 15% | 3 HIGH, 5 MEDIUM |

🎯 严重性分布

| 严重性 | 规则数 | 占比 | 说明 |
| --- | --- | --- | --- |
| CRITICAL | 35 条 | 31.8% | 立即拒绝 |
| HIGH | 52 条 | 47.3% | 人工审查 |
| MEDIUM | 20 条 | 18.2% | 标记观察 |
| LOW | 3 条 | 2.7% | 记录日志 |

🔍 核心检测能力

| 能力 | 规则数 | 覆盖率 | 检出率 |
| --- | --- | --- | --- |
| 恶意代码 | 12 条 | 95% | 98% |
| 后门检测 | 10 条 | 90% | 96% |
| 凭据泄露 | 15 条 | 98% | 97% |
| 网络攻击 | 7 条 | 92% | 95% |
| 钓鱼检测 | 10 条 | 88% | 94% |

---

## 📊 测试数据

| 指标 | 数值 | 说明 |
| --- | --- | --- |
| 检测规则 | 110 条 | 5 大类别 |
| 综合检出率 | 95.6% | 2,100 个测试样本 |
| 误报率 | 3.0% | 正常样本测试 |
| 扫描速度 | 2.3 秒/技能 | 平均耗时 |
| 样本库规模 | 298,381 个 | 真实技能样本 |
| 代码规模 | 3,338 行 | Python 核心代码 |

---

## 🚀 获取方式和自我迭代方式拷贝下面信息给你openclaw等：

```
起源仓库：https://github.com/caidongyun/agent-security-skill-scanner.githttps://gitee.com/caidongyun/agent-security-skill-scanner.git

规则迭代流程 (7 步)步骤 1: 发现新威胁   ↓步骤 2: LLM 分析威胁 (OpenClaw)   ↓步骤 3: LLM 生成规则 (OpenClaw)   ↓步骤 4: 创建测试样本   ↓步骤 5: 验证规则   ↓步骤 6: 添加到规则库   ↓步骤 7: 提交分享每步都有代码示例，结合 OpenClaw LLM 能力！2️⃣ 误报处理指南3 种方案 (从简单到推荐):方案难度适用场景方案 1: 文件加白⭐ 最简单整个文件可信方案 2: 模式加白⭐⭐ 精确控制特定代码模式方案 3: LLM 辅助加白⭐⭐⭐ 推荐OpenClaw 场景每种方案都有:✅ 操作步骤✅ 代码示例✅ 验证方法🚀 快速使用规则迭代# 步骤 2-3: 使用 OpenClaw LLMfrom openclaw import llm# 分析威胁threat = llm.analyze("分析代码安全威胁...")# 生成规则rule = llm.generate_rule("生成检测规则...")误报处理# 方案 1: 文件加白 (最简单)vim data/whitelist/local.json# 添加{  "files": ["skills/my-skill/main.py"]}# 验证python cli.py scan skills/my-skill/
```

## 下载地址

## ```  https://github.com/caidongyun/agent-security-skill-scanner.git ``` ``` ``` https://gitee.com/caidongyun/agent-security-skill-scanner.git ``` ```

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SIaa7Ribxiaic5UU4m0THwwUC6DRqf2dHKHLibqicAmfs7QBF5vpVX1dzpcOw9ep6JEFtibwMkMVYMhwqTokSVHXDwEQ/0?wx_fmt=png)

小东安全日记

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SIaa7Ribxiaic5UU4m0THwwUC6DRqf2dHKHLibqicAmfs7QBF5vpVX1dzpcOw9ep6JEFtibwMkMVYMhwqTokSVHXDwEQ/0?wx_fmt=png)

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