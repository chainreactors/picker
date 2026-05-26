---
title: Skill 评估与提升专家 | 评估和提升其他 Skill 的能力、提供基准测试、红队测试和自主改进循环
url: https://mp.weixin.qq.com/s/gXESwlGIiFls3JwbxvZf0w
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:08:47.521368
---

# Skill 评估与提升专家 | 评估和提升其他 Skill 的能力、提供基准测试、红队测试和自主改进循环

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMIxO2dArOjGLeNxIAj5E78iakyhLSBhDaR60SKibJzkV7jBDgR8m2EZ9xTHbziaichd8QpnjrU0S3UyuDk9or21817IicibAYOFSxWYU/0?wx_fmt=jpeg)

# Skill 评估与提升专家 | 评估和提升其他 Skill 的能力、提供基准测试、红队测试和自主改进循环

lanyasheng
lanyasheng

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**所有工具安全性自测！！！VX：****NightCTI**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**夜组安全**“**设为星标**”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg)

## 工具介绍

Skill Evaluator — Skill 评估与提升专家**评估和提升其他 Skill 的能力，提供基准测试、红队测试和自主改进循环。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMI5BVa8LfLckTzvcqv04UL1BCudS5bFiaicoUhATJenaJnTSyAu5OniaweqfHO46VViaETrJFP5gUzFvzYfNldHODr2G02SvR0mN7g/640?wx_fmt=png&from=appmsg)

## 🚀 快速开始

### 安装

```
# 克隆仓库
git clone https://github.com/lanyasheng/skill-evaluator.git
cd skill-evaluator

# 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 基础评估

```
# 评估单个 Skill
python scripts/evaluate.py --skill-path /path/to/skill --output reports/

# 评估并生成详细报告
python scripts/evaluate.py --skill-path /path/to/skill --output reports/ --verbose

# 评估并导出 JSON 格式
python scripts/evaluate.py --skill-path /path/to/skill --output reports/ --format json
```

### 红队测试

```
# 运行核心测试
python scripts/red_team.py --skill-path /path/to/skill --output reports/

# 运行所有测试（包括 SQL 注入、提示词注入等）
python scripts/red_team.py --skill-path /path/to/skill --output reports/ --all-tests
```

### 自主改进（Karpathy Loop）

```
# 自主改进循环
python scripts/self_improve.py --skill-path /path/to/skill --metric accuracy --max-iterations 100

# 早期停止（10 次无改进自动停止）
python scripts/self_improve.py --skill-path /path/to/skill --metric accuracy --early-stop 10
```

### 能力追踪

```
# 追踪 Skill 能力演进
python scripts/track_progress.py --skill-path /path/to/skill --output reports/

# 生成可视化图表（需要 matplotlib）
python scripts/track_progress.py --skill-path /path/to/skill --output reports/ --plot
```

### 基准对比

```
# 列出所有基准测试用例
python scripts/benchmark_db.py --action list

# 与基准对比
python scripts/benchmark_db.py --action compare --skill-path /path/to/skill --category tool-type

# 获取排行榜
python scripts/benchmark_db.py --action leaderboard --category tool-type
```

### 并行评估

```
# 多 Skill 并行评估
python scripts/parallel_eval.py --skill-paths /path/to/skill1 /path/to/skill2 --max-workers 10

# 生成排行榜报告
python scripts/parallel_eval.py --skill-paths /path/to/skill1 /path/to/skill2 --output reports/
```

### 发布到 ClawHub

```
# 验证 Skill（不发布）
python scripts/publish_to_clawhub.py --skill-path /path/to/skill --level Level2

# 执行发布
python scripts/publish_to_clawhub.py --skill-path /path/to/skill --level Level2 --publish
```

## 📊 核心功能

### 1. 按类别调整权重

支持 5 种 Skill 类别，每种类别有独立的权重配置：

| 类别 | 准确性 | 可靠性 | 效率 | 成本 | 覆盖率 | 安全性 |
| --- | --- | --- | --- | --- | --- | --- |
| **工具型** | 35% | 20% | 25% | 15% | 5% | - |
| **流程型** | 25% | 30% | 20% | 15% | 10% | - |
| **分析型** | 40% | 20% | 20% | 15% | 5% | - |
| **创作型** | 30% | 20% | 20% | 10% | 10% | - |
| **评估型** | 45% | 20% | 15% | 10% | 10% | 10% |

### 2. 红队测试

内置 5 种安全测试：

* ✅ SQL 注入测试
* ✅ 提示词注入测试
* ✅ 资源限制测试
* ✅ XSS 攻击测试
* ✅ 路径遍历攻击测试

### 3. 自主改进循环（Karpathy Loop）

借鉴 Karpathy autoresearch 的核心设计：

```
评估 → 小改动 → 再评估 → 保留/回滚 → 重复
```

**实测效果**：5 次迭代改进 16.3%（75.55% → 87.84%）

### 4. 能力演进追踪

* 加载评估历史
* 计算趋势（improving/stable/declining）
* 生成 Markdown 报告
* 可视化图表（需 matplotlib）

### 5. 基准数据库

* 15 个默认基准测试用例
* 5 个类别全覆盖
* 支持排行榜功能

### 6. 多 Agent 并行评估

* 最大支持 10 并发
* 实测加速比 3.3x
* 自动生成排行榜报告

## 🏆 测试验证

### 单元测试

* ✅ **19/19 通过（100%）**
* 执行时间：0.04s
* 覆盖模块：evaluate.py 核心功能

### 红队测试

* ✅ **3/3 通过（100%）**
* 测试类型：SQL 注入、提示词注入、资源限制

### 基准数据库

* ✅ **15/15 基准用例加载成功**
* 5 个类别全覆盖

### 自主改进循环

* ✅ \*\*改进幅度 16.3%\*\*（75.55% → 87.84%）
* 5 次迭代，2 次有效改进

### 测试覆盖率

* ✅ **整体覆盖率 92%**
* 7 个核心模块全部覆盖

详见：TESTING\_REPORT.md

## 🎯 Skill 能力分级

| 等级 | 名称 | 标准 | 发布策略 |
| --- | --- | --- | --- |
| **Level 1** | 基础可用 | ✅ 能完成核心任务 ✅ 有基本错误处理 ⚠️ 测试覆盖率 < 50% | 仅限内部使用 |
| **Level 2** | 稳定可靠 | ✅ 能完成核心任务 ✅ 有完整的错误处理 ✅ 测试覆盖率 > 80% ✅ 有基准测试 | 可发布到 GitHub/ClawHub |
| **Level 3** | 生产就绪 | ✅ 能完成核心任务 ✅ 有完整的错误处理 ✅ 测试覆盖率 > 95% ✅ 有红队测试 ✅ 有用户反馈循环 | 优先推荐到 ClawHub 首页 |

## 工具获取

点击关注下方名片进入公众号

回复关键字【260525】获取下载链接

## 往期精彩

[一个面向安全团队、渗透测试、资产侦察、威胁追踪和红队编排的 AI CLI

2026-05-22

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMIibFBsnKMDQurQMF0R00d4bCqQKZvlnyZxKkLwAbRYhn9ibECQrOFuRZ6l7Zyib8KCAWlHXORDIZMnFvX0T0Bon3ydLicnsLribDnM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496888&idx=1&sn=e6b250cdeb0076d7dc5851402a02bbc3&scene=21#wechat_redirect)[AI代码审查助手 | 支持30+语言，自动发现Bug/安全漏洞/性能问题

2026-05-21

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMLmwXutufc60CGia6kctJaMxrOiaqbeibdmxNF6t86ls1BBXyXAAIkibKURyibZgORx8kUv5v7eIvgp7cG3IyHxtqDlSDJibl7QZ4n8c/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496862&idx=1&sn=0aa9360f536a44cad0353946bc3e2278&scene=21#wechat_redirect)[网络安全全流程Skills — 39大模块，195个安全Skills，覆盖完整攻击面与防御面

2026-05-19

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMINeXMDkAkLSVsU9xaoqjWACTaFRDKKwVEJqObCjgzp6E139DNCx8mMic2b0hHbFUmw4Byn9lFpdjU8fZJMLpEA7jnYntHLiakA8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496857&idx=1&sn=d6a3d84dd7b52cb2c8f1ec797f5fac85&scene=21#wechat_redirect)[Linux 本地提权工具  | 支持多个提权漏洞

2026-05-18

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMLTnewYJCOKUSxQpTItakrGdibva4aL1Qug4nibOjdOMbHrYHoHXib6ZFwYhxsfYVelUcDPO4OfPgpXNEXPHC1WYEtPIXwnBtEXXI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496852&idx=1&sn=c41f8e2df45a5f1e809b5a121501bc66&scene=21#wechat_redirect)[Web 代码审计技能skills |  PHP / Java / .NET / Node.js · 50+ 审计文件 · 动态调试 · 漏洞链挖掘

2026-05-15

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMJK3HPWjsM7j2TCmrbqKxu108u7wefRDHotb8nmuibhVXnrBiaAMb0n0kUpgeyRTwOKprjnd20bO3P80ecmhDKg4dubmXn4Gn1dI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496844&idx=1&sn=b4f066c9ccbd761abc8b0c60303f3454&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

夜组安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

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