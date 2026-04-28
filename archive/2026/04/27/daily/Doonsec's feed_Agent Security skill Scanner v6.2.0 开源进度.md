---
title: Agent Security skill Scanner v6.2.0 开源进度
url: https://mp.weixin.qq.com/s/uItBWILyTeG1msnO43EOdw
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:23:44.368167
---

# Agent Security skill Scanner v6.2.0 开源进度

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5f9ibvu2qYVIlo2ZRzrPKl8Oib4xZRjpIhRqePWxwYJsqLjfz3t2ic4u4KtlOicwawp1TJ5QxXQ2JxbaWYHIMv5a9EXeGjkA8uEZ84wm6RjR5CI/0?wx_fmt=jpeg)

# Agent Security skill Scanner v6.2.0 开源进度

原创

小东2025
小东2025

小东安全日记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

```
放下AI焦虑:
1、AI厂商新闻不提供数据或者使用的产品真实可以感受的，不要轻易相信，   40分必须说成100分，要不没有人关注
2、让你焦虑的媒体，大部分他们的目的不是为了给你传递信息内容本身。
3、AI可以快速给你成就感，但是做到深入的东西依然要你付出代价   所以不要害怕担心焦虑慢慢用就好了，边用工具边提升   4、请注意，自嗨的东西很多   很多时候你甚至会发现你的说话的方式都变成有点儿AI给你说的
5、你自己的agent懂的，并不是你懂的
6、工程约束可以提高产出质量，高质量的数据也一样。
以上说的都是错。以下之前开源题目结一下题，这是我尝试的过程产物，60分的卷子先交了。
```

# Agent Security skill Scanner v6.2.0

 AI Agent 安全扫描工具

---

## 📊 核心变化概述

| 指标 | v6.2.0 | 说明 |
| --- | --- | --- |
| 规则数 | 846 | 去重优化后实际生效 |
| 新增模块 | 7 | 风险分级/攻击链检测/熔断等 |
| 检测架构 | 三层 | PatternEngine-> RuleEngine->  → LLM |
| 扫描速度 | ~385 文件/秒 | 8 worker 并发 |

本次改进：

AC自动机快速筛选提速，命中再继续RuleEngine（要用才知道，有问题可以继续优化）

## 近期测试数据：

📊 数据集一：ClawHub 全量技能扫描 (v6.1.9)

扫描范围：ClawHub 市场全量技能，159,164 个文件
扫描时间：2026-04-21，耗时 1 小时 24 分钟
扫描架构：分层 AC 自动机 (Layer1 关键词筛选 + Layer2 签名验证)

| 指标 | 数值 |
| --- | --- |
| 总文件数 | 159,164 |
| 检出数量 | 26,611 (16.72%) |
| 安全数量 | 132,553 (83.28%) |
| CRITICAL | 0 |
| HIGH (误报) | 425 (CONFIG-MALICIOUS 规则) |
| 扫描速度 | 31.4 it/s |
| 内存占用 | ~1.8GB |
| 超时文件 | 16 (0.01%) |

📊 数据集二：Benchmark 全量样本测试 (v6.2.0)

样本集：132,539 个样本 (from-templates 模板生成)
规则总数：927 条

10 种恶意攻击类型 — 全部 100% 检出 ✅

| 攻击类型 | 检出率 | 样本数 |
| --- | --- | --- |
| prompt\_injection | 100.00% | 2,180 |
| memory\_pollution | 100.00% | 8,542 |
| persistence | 100.00% | 8,513 |
| evasion | 100.00% | 8,677 |
| supply\_chain\_attack | 100.00% | 8,582 |
| credential\_theft | 100.00% | 8,550 |
| data\_exfiltration | 100.00% | 8,661 |
| tool\_poisoning | 100.00% | 8,705 |
| remote\_load | 100.00% | 8,562 |
| resource\_exhaustion | 100.00% | 8,560 |

误报测试

| 样本类型 | 误报率 | 样本数 |
| --- | --- | --- |
| false\_prone (良性) | 12.77% | 8,796 |

核心指标

| 指标 | 目标 | 实际 |
| --- | --- | --- |
| 恶意检出率 | ≥95% | 100% ✅ |
| 误报率 | ≤15% | 12.77% ✅ |
| 扫描速度 | ≥1000 it/s | 1100+ ✅ |
| 规则数 | — | 927 |

## 🔥 v6.2.0 新特性

### 1. 风险分级体系

* **Curl 风险分级**

  : 白名单域名 + 敏感参数检测
* **凭据窃取检测**

  : 攻击链识别 (诱导→混淆→外传)
* **5 级风险体系**

  : CRITICAL/HIGH/MEDIUM/LOW/INFO

### 2. 单 Skill 熔断机制

* 默认阈值: 500 文件/目录
* 防止恶意软件塞入大量文件拖慢扫描
* 参数: `--skill-max-files N`

### 3. 规则库优化

* 去重 88 条规则 (928 → 846)
* 标准化 419 条 severity 为大写
* 新增 6 条凭据攻击链规则 (CRED-CHAIN-001~006)

##

## 发布文件清单 (20 个)

**核心模块 (8 个)**:

| 文件 | 功能 |
| --- | --- |
| `scanner.py` | 主扫描器 (三层架构) |
| `whitelist_filter.py` | 白名单过滤 |
| `config_detector.py` | 配置文件检测 |
| `context_aware_filter.py` | 上下文感知过滤 (新增) |
| `credential_theft_classifier.py` | 凭据窃取攻击链检测 (新增) |
| `curl_risk_classifier.py` | Curl 风险分级 (新增) |
| `risk_tier_classifier.py` | 5 级风险体系 (新增) |
| `security_tool_detector.py` | 安全工具识别 (新增) |

**规则库 (2 个)**:

* `rules/dist/all_rules.json`

  — 846 条规则
* `rules/rule_optimizer.py`

  — 规则优化器 (新增)

**引擎模块 (9 个)**:

* `src/encoding_utils.py`
* `src/engines/`

  (8 个检测引擎)

**入口 (3 个)**:

* `scan`

  — CLI 入口
* `index.js`

  — Node.js 入口
* `index.d.ts`

  — 类型定义

**文档/配置 (5 个)**:

* `package.json`
* `requirements.txt`
* `README.md`
* `RELEASE_NOTES.md`
* `SKILL.md`

## 🔧 配置选项

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `--workers` | 4 | 并发线程数 |
| `--skill-max-files` | 500 | 单 Skill 文件数熔断阈值 |
| `--timeout` | 3.0 | 单文件超时 (秒) |
| `--output` | text | 输出格式 (text/json) |
| `--output-file` | - | 输出文件路径 |

## 📝 许可证

MIT License

## 🔗 仓库

* **Gitee**

  : https://gitee.com/caidongyun/agent-security-skill-scanner-master
* **GitHub**

  : https://github.com/caidongyun/agent-security-skill-scanner
* **NPM**

  : @caidongyun/security-scanner@6.2.0
* clawhub

  ```
  openclaw skills install caidongyun/agent-security-skill-scanner
  ```

## 快速开始

### 安装

```
npm install -g @caidongyun/security-scanner
```

### 使用

```
# 扫描目录agent-scanner /path/to/skills# 并发扫描agent-scanner /path/to/skills --workers 8# 输出 JSON 报告agent-scanner /path/to/skills --output json --output-file report.json
```

预览时标签不可点

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