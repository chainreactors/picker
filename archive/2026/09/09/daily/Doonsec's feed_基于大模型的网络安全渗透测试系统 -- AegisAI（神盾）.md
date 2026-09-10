---
title: 基于大模型的网络安全渗透测试系统 -- AegisAI（神盾）
url: https://mp.weixin.qq.com/s/wMHJt71d1VuQ91lk4DdGtg
source: Doonsec's feed
date: 2026-09-09
fetch_date: 2026-09-10T06:47:04.335438
---

# 基于大模型的网络安全渗透测试系统 -- AegisAI（神盾）

# 基于大模型的网络安全渗透测试系统 -- AegisAI（神盾）

bai-yi-meng
bai-yi-meng

Web安全工具库

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，大家都要把工具当做病毒对待，在虚拟机运行。如有侵权请联系删除。个人微信：ivu123ivu

**0x01 工具介绍**

AegisAI（神盾）是一个由大模型驱动的自动化渗透测试系统：智能体自主规划「侦察 → 资产枚举 → 漏洞检测 → AI 分析与报告」的完整测试流程，集成 Nmap 端口扫描、Web 指纹识别、敏感路径枚举、SQL 注入 / XSS / 弱口令 / 命令注入 / 路径穿越检测器与本地 CVE 知识库，并自动生成专业渗透测试报告。内置本地演练靶场（127.0.0.1:9001），无需安装 DVWA 等外部靶机即可完整演示。核心特性：

| 特性 | 说明 |
| --- | --- |
| 🧠 大模型驱动智能体 | LLM 每一步自主决策「下一步调用什么工具」，输出推理过程；决策异常自动回退内置策略引擎 |
| 🔌 大模型可插拔 | 支持 DeepSeek / 智谱 GLM / 通义千问 / Kimi / OpenAI 及任意 OpenAI 兼容接口；**未配置 Key 时以离线策略引擎运行**（功能完整，可演示） |
| 🛠 工具链集成 | Nmap（自动检测，缺失时回退内置纯 Python 扫描器）、HTTP 指纹、目录枚举（含软 404 识别）、5 类 Web 漏洞检测器（全部带对照验证防误报） |
| 📚 本地 CVE 知识库 | 30+ 条「产品+版本」漏洞规则与暴露面加固提示，离线匹配，可按需扩充 |
| 🎯 内置演练靶场 | 一键启动的本地靶场（SQLi / XSS / 弱口令 / 命令注入※ / 路径穿越※ / 敏感文件 / 需登录的成员页），※为模拟实现，不执行真实命令、不读取真实文件 |
| 🔑 靶场凭据（选填） | 新建任务可填靶场账号密码：智能体先登录目标（自动兼容 CSRF 表单，适配 DVWA 类靶场）再检测，并可发现**登录后页面**的漏洞；凭据只在内存中使用，不落盘、接口不回显 |
| 📄 自动报告 | Markdown + 可打印 HTML 渗透测试报告（封面 / 执行摘要 / 风险统计 / 证据 / AI 分析 / 修复建议） |
| 📡 实时可视化 | WebSocket 推送智能体的每一步思考、工具调用与发现；深色安全运维风格 Web 界面 |
| 🔐 合规设计 | 创建任务必须勾选授权确认；扫描范围强制限定在授权 scope 内；只做检测验证，不投放破坏性利用载荷 |

![界面预览](https://mmbiz.qpic.cn/sz_mmbiz_png/U7LDNXUGXQuLwj08MDJxYM5JEPFmvKq2Sf7ySP6jztFqIAmmbDicGkXEte00XBNjcywAXuZ4Zic7iceOP14mEyx6z5Fg2U2g0nOQlmDSsic1SicY/640?wx_fmt=png&from=appmsg)

**0x02 安装与使用**

1. 安装依赖（建议使用虚拟环境）

```
python -m venv .venv.venv/Scripts/python -m pip install -r requirements.txt     # Windows# .venv/bin/python -m pip install -r requirements.txt       # macOS / Linux
```

2. 一键启动（平台 :8000 + 本地靶场 :9001）

```
.venv/Scripts/python scripts/start_all.py
```

3. 浏览器打开

```
#    http://127.0.0.1:8000#    新建任务 → 目标填 127.0.0.1:9001 → 勾选授权确认 → 启动智能体
```

命令行方式（无界面）

```
.venv/Scripts/python cli.py scan -t 127.0.0.1:9001 --name 演示 --authorized .venv/Scripts/python cli.py tools       # 查看可用检测工具
```

运行测试：

```
.venv/Scripts/python -m pytest tests -q
```

网盘下载链接（一定要在虚拟机运行）：

```
后台回复：20260909获取下载链接，仅一天有效
```

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U7LDNXUGXQvcQ6NvGFpD17ZHlkabrBPRPo2hTSFZ70qDImj2dOpicNMUXTJ5MF9z4tGbcCd1RKhHmDGS5z1z0K5Emib9ib8tJ5iaNfggPiaSyxZQ/640?wx_fmt=jpeg&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8H1dCzib3UibsC4yYFwgTnJrN0q57DearHJhaWSE6XQllpkUviaibg5MqTYgdUQYDNt8ysfV2v6o4jsN34pmq3DAOg/640?wx_fmt=jpeg&from=appmsg) |

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

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