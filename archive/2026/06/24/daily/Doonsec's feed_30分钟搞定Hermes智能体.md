---
title: 30分钟搞定Hermes智能体
url: https://mp.weixin.qq.com/s/ZZCYipMT4Fju9TckGFYywA
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:06:08.620138
---

# 30分钟搞定Hermes智能体

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N46S2sKsyIDO90ExlxibmNqhSA74KPSLnNYak6PEDDib7lyicDwmHpgFj0BcIuLylpZgicYlJ255YJZMia2amVqwh4J7GxQibBwczFTiarp4Vb3NU4/0?wx_fmt=jpeg)

# 30分钟搞定Hermes智能体

原创

ladon
ladon

306Safe

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Hermes Agent 是什么？

Hermes Agent 是由硅谷AI实验室 Nous Research 于2026年2月开源的自进化AI智能体框架，MIT协议完全免费。它和传统AI助手的本质区别：普通AI是"临时工"，用完就忘；Hermes是"长期员工"，越用越强。

截至2026年5月，Hermes Agent 日均Token调用量达2910亿次，超越OpenClaw登顶全球第一。GitHub星标突破14万。

| 维度 | 传统聊天AI | Hermes Agent |
| --- | --- | --- |
| 记忆 | 单次会话，关闭即清 | 跨会话持久记忆，重启不丢 |
| 技能 | 每次重新描述需求 | 自动提炼可复用Skill |
| 接入 | 仅网页/APP | 微信、飞书、钉钉、Telegram等20+平台 |
| 模型 | 绑定单一厂商 | 18+模型自由切换 |

一键安装

**Linux/macOS/WSL2：**

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash hermes --version
```

**Windows PowerShell：**

```
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

**macOS前置：**先装Xcode命令行工具 `xcode-select --install`，建议装好Homebrew和Git。

初始配置：三步走起来

**步骤1：启动配置向导**

```
hermes setup
```

向导引导你：选择LLM提供商（推荐新手选DeepSeek或阿里云百炼） → 输入API Key → 配置消息通道（强烈建议先接Telegram）

**步骤2：配置模型**

```
hermes model   # 切换模型/服务商 hermes tools   # 配置可用工具
```

**步骤3：启动**

```
hermes chat                    # 命令行交互 hermes dashboard               # Dashboard可视化管理(推荐) http://127.0.0.1:9119 hermes gateway                  # 多平台网关模式
```

Profile Builder：5步可视化建站

2026年6月新上线的Profile Builder，把以前需要手打多行CLI命令的配置流程，压缩成网页端5步搞定：

2. **基础信息**

   ：给智能体起名、选择人格风格
4. **模型配置**

   ：下拉选择LLM提供商和模型，填入API Key
6. **技能设置**

   ：勾选需要的工具，划定权限边界
8. **通道接入**

   ：扫码绑定Telegram/微信/飞书
10. **配置审核**

    ：预览完整配置，一键生成

配置耗时从平均30分钟压缩到5分钟，新手不需要写一行代码。

记忆系统：五层架构过目不忘

| 层级 | 名称 | 作用 |
| --- | --- | --- |
| L1 | 短期推理记忆 | 当前任务工作台，会话结束清空 |
| L2 | 过程性技能记忆 | 自动生成的操作指南，存为Skill文件 |
| L3 | 情境持久化检索 | 向量索引+FTS5全文检索，主动匹配 |
| L4 | 用户画像建模 | 偏好、风格、心智模型，USER.md动态更新 |
| L5 | 全文可检索存档 | 回溯任意历史信息，SQLite+FTS5 |

**调优技巧：**首次使用时编辑 `~/.hermes/USER.md` 和 `~/.hermes/MEMORY.md`，先放5-10条最关键的，后面让它自己积累。

```
# USER.md 示例 - 身份：互联网产品经理 - 偏好：简洁输出，不要营销话术 - 沟通风格：直接说结论，不要铺垫  # MEMORY.md 示例 - 当前项目：数据治理平台v2.0 - 核心指标：DAU、留存率、NPS - 待办：6月30日前完成验收
```

技能自进化：越用越快的秘密

当Hermes完成一个复杂任务后，如果满足触发条件（工具调用>5次、中途自主修复、用户纠正等），它会自动生成结构化Skill文档到 `~/.hermes/skills/` 目录。下次再说"分析另一款游戏的评价"，它直接调用Skill，不用重新解释步骤。运行三个月后，65%的新任务可直接调用已有技能。

Cron定时任务

```
# 每天早上9点，抓取Hacker News AI热点 hermes cron add "0 9 * * *" "搜索Hacker News AI热点，总结后Telegram发给我"  # 每周一生成周报 hermes cron add "0 10 * * 1" "汇总上周工作进展，生成周报发到飞书群"
```

注意：本地部署关机就停了，需长期运行请用云端部署。

云端部署与OpenClaw迁移

本地部署关机就停，用阿里云计算巢或腾讯云Lighthouse一键部署，7x24在线。

```
hermes claw migrate              # 交互式迁移(完整预设) hermes claw migrate --preset user-data  # 仅迁移用户数据 hermes claw migrate --dry-run     # 预览将要迁移的内容
```

新手七日养成计划

* **Day 1-2**

  ：安装配置，接入Telegram，简单对话
* **Day 3-5**

  ：喂记忆，写USER.md和MEMORY.md
* **Day 6-7**

  ：执行第一个复杂任务，让它生成第一个Skill
* **Day 8-14**

  ：接Cron定时任务，尝试多Agent协作

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rvkyDDyx4sv53bdQHLc9aiaciaqqxoojmXlic5HzYKRWCHnibkX1MXkqzL652lJpPoacJ8owSC6fuxHgnIgcWDVMIg/0?wx_fmt=png)

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