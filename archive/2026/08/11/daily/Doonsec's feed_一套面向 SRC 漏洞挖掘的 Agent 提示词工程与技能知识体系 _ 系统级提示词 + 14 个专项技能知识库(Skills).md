---
title: 一套面向 SRC 漏洞挖掘的 Agent 提示词工程与技能知识体系 | 系统级提示词 + 14 个专项技能知识库(Skills)
url: https://mp.weixin.qq.com/s/g_pASa1fOVTfsqtFtTigBg
source: Doonsec's feed
date: 2026-08-11
fetch_date: 2026-08-12T04:00:54.991503
---

# 一套面向 SRC 漏洞挖掘的 Agent 提示词工程与技能知识体系 | 系统级提示词 + 14 个专项技能知识库(Skills)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMLBJgcJA6Q7rzvoZsU6M1CxLichPfHwqYPtficm1ZuWmaHmDvDhC3yDsO7OyBtjxxRKhGfDhiaicILBO3sqOgIDf1Xw45tWEqt1ZjQ/0?wx_fmt=jpeg)

# 一套面向 SRC 漏洞挖掘的 Agent 提示词工程与技能知识体系 | 系统级提示词 + 14 个专项技能知识库(Skills)

zhaji2333
zhaji2333

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

## 工具简介

CK-Skills 是一套面向 SRC 漏洞挖掘的 **Agent 提示词工程与技能知识体系**,以 Claude Code / Codex 等通用 Agent 框架为运行时,通过 **系统级提示词(AGENTS.md)+ 14 个专项技能知识库(Skills)**,让通用 Agent 在垂直安全领域达到专家级表现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMIYibMibxjiajS0BVnL6VicJ1YrWhf3fyoTgcJBaLKq2zD9oqk8H8kyRNYou5qfFjeXlDRe5vWAObzwicupEgu8riasdQtfsu2iaEshr4/640?wx_fmt=png&from=appmsg)

> 基于 Claude Code / Codex 的 SRC 漏洞挖掘 Agent 技能体系 —— 将顶尖安全研究员的方法论沉淀为可调度、可复用的 Skill 知识资产。

针对通用 Agent 在垂直领域的三大痛点:

* 方法论散、覆盖不全
* 浅尝辄止、不按专家流程执行
* 业务逻辑 / 越权 / WAF 绕过等经验型漏洞难以自动化

## 架构设计

四层架构,各司其职:

```
┌──────────────────────────────────────────────┐
│  Agent 运行时(Claude Code / Codex)           │  推理与工具调用
├──────────────────────────────────────────────┤
│  系统级提示词 AGENTS.md                        │  身份 / 约束 / 纪律 / 调度
├──────────────────────────────────────────────┤
│  14 个专项 Skills(知识层)                     │  方法论 / 场景表 / 步骤
├──────────────────────────────────────────────┤
│  触发路由(场景→技能 / 漏洞类型→技能)         │  专家知识按需加载
└──────────────────────────────────────────────┘
```

* **AGENTS.md**:六段式总纲(身份-约束-纪律-调度-评估-输出),定义 Agent 人格、Extended Thinking 推理链、十条测试执行纪律、结构化输出标准
* **Skill**:用 Markdown DSL 编写,frontmatter(触发语义)+ 六要素(触发条件 / 方法论 / 场景表 / 挖掘步骤 / 验证要点 / 修复建议)
* **路由表**:场景→技能 / 漏洞类型→技能 / 优先级 / 组合场景,借鉴 MoE 思想实现专家知识按需加载

## 📚 Skills 列表

| 技能 | 覆盖范围 |
| --- | --- |
| `recon-js-analysis` | 资产测绘、webpack / source map 还原、API 与密钥提取 |
| `auth-access-control` | 认证绕过、越权、IDOR、多租户隔离、密码重置、JWT |
| `injection-vulns` | SQL / NoSQL / 命令 / SSTI / 表达式注入 |
| `business-logic-race` | 支付逻辑、状态机建模、金额篡改、竞态条件 |
| `file-handling` | 文件上传 getshell、路径穿越、Zip Slip、CSV 注入 |
| `ssrf-internal-network` | SSRF、云元数据、内网探测、DNS 重绑定 |
| `deserialization-xxe` | 反序列化 RCE、XXE、原型污染、利用链构造 |
| `xss-frontend-security` | XSS、CSRF、CORS、Clickjacking |
| `api-protocol-security` | BOLA、GraphQL、WebSocket、HTTP 走私 |
| `mobile-iot-device-security` | Android / iOS 逆向、WebView、固件安全 |
| `cloud-infra-supply-chain` | 云配置错误、K8s、CI/CD、SBOM、供应链 |
| `source-code-audit` | 输入点 → 传播链 → Sink 静态审计 |
| `waf-bypass-techniques` | Level 1-7 对抗升级框架 |
| `ai-llm-agent-security` | 提示词注入、越狱逃逸、System Prompt 泄露、RAG/记忆污染、Agent 工具滥用致 RCE/SSRF、沙箱逃逸、模型供应链 |

## 🚀 快速开始

### 1. 安装

将本项目 `.agents/` 目录与 `AGENTS.md` 放入你的工作目录,Agent 会自动加载 `AGENTS.md` 作为系统提示词,并根据触发信号加载对应 Skill。

### 2. 目录结构

```
CK-Skills/
├── AGENTS.md                      # 系统级提示词总纲
├── .agents/
│   └── skills/                    # 14 个专项技能
│       ├── recon-js-analysis/
│       │   └── SKILL.md
│       ├── auth-access-control/
│       │   └── SKILL.md
│       └── ...                    # 其余专项技能
```

### 3. 使用

在 Claude Code / Codex 中直接描述测试场景,Agent 会根据触发信号自动加载对应 Skill 并按方法论执行:

```
目标:https://example.com,已登录普通用户,需要测试越权
→ 自动加载 auth-access-control,按"权限三问"执行
```

## 🎯 设计理念

* **JS 不吃透,不发包**:信息收集先行,吃透前端再动手
* **覆盖度自检**:✅已测 / ❌未测 / 🔄变种 / 💡关联
* **失败升级**:Level 1-7,至少到 Level 4 才能下"无漏洞"结论
* **业务建模**:状态机 + 角色矩阵 + 非法路径 + 一致性校验 + 并发
* **跨接口关联**:信息流 / 凭证 / 状态 / 权限 / 时序五问

## 工具获取

点击关注下方名片进入公众号

回复关键字【260811】获取下载链接

## 往期精彩

[微信小程序全自动化渗透工具

2026-08-10

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMIh0xiaJLYDSP5dcSicZFR7XhtMLInbJSk0S5jrialeQqwnqpicgFD8kqIHScya3qw0eJx1HzzlaFq4lEwjRfq9sh1SmQiasvUCSCO8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497358&idx=1&sn=f91cc417e69da38675f15e7020c297f9&scene=21#wechat_redirect)[漏洞监测平台 | 一个面向内部安全运营的漏洞影响评估与受控验证平台

2026-08-07

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLicVDvwtvzrLicB9wcBV93gDnbhsX5uWic8zQOCMCrPsSicfBAW1lMUbiaYnwibRqtu3FnBeDHkzcljJPibpCuVY7icqftsw71AYRGj6A/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497353&idx=1&sn=3b6916c04b7acf57dd419b2dad4cd73e&scene=21#wechat_redirect)[面向 libvirt/KVM 宿主机的 RDP 智能网关与虚拟机电源管家：连接即唤醒、空闲即休眠、暴力破解自动封禁

2026-08-06

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMKLLktNqq9CgWcv9UJBGvpHc5VXI4SqbwswOWTX9P65BPLPib8R8aEtKibGGOxcLlJic8dWjicxYx0UAVR8dyee5DlOkqbUUjvzxDA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497345&idx=1&sn=28c64078d37a2f07522cf214f2c7da34&scene=21#wechat_redirect)[Windows 离线 Linux 提权辅助查询工具 | 以 Sudo、SUID、受限 SUID 和 Capabilities 等权限场景查询，减少人工翻查成本

2026-08-05

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLoTueSpiaZ1JvbAzKiaHib4HlHiaRQNBD9UDax0UyKa2ebPStjZyaHxqH6rLLicIlWtJmBw72ibbqKXuDibm6dGv7ChJLiaFPOscKSHEs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497340&idx=1&sn=15aa5b84d2ac00667738a6e038716f6d&scene=21#wechat_redirect)[.NET免杀生成工具| 将任意 .NET PE client 打包为免落盘的 PowerShell 反射加载链

2026-08-04

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMIWHtnYvIVmyzWR1BtibhM7qISTcBiaLDEsqMLD8JT89uEYUGIyJaf2eiaicBOBNgzMf6Esc939MS5xQQdubzQOuVZriaHxykoNdO28/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497335&idx=1&sn=f734dce8f7858b1263fc980f634fb72b&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp)

预览时标签不可点

阅读原文

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