---
title: 工具分享 | 一款全功能 Web 漏洞扫描工具
url: https://mp.weixin.qq.com/s/dMcvIyMpjhuvUTm1l_7vaA
source: Doonsec's feed
date: 2026-09-01
fetch_date: 2026-09-02T06:38:47.115027
---

# 工具分享 | 一款全功能 Web 漏洞扫描工具

# 工具分享 | 一款全功能 Web 漏洞扫描工具

huocai250
huocai250

篝火信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

0x00 简介

WebVulnScanner 是一款检测 / 评估型安全扫描器（与 OWASP ZAP、Nikto、Nuclei 同类）。

它探测目标是否存在常见漏洞、梳理攻击面并给出整改建议，不包含利用、提权、 数据窃取或持久化功能（详见「关于漏洞利用」）。请仅在已获得书面授权的目标上使用。

v9 亮点：新增 YAML 模板签名引擎（可无代码扩展规则）、内置 1000+ 检测规则/签名、35 个检测模块，并新增 JS 密钥、敏感路径暴露、API 发现、缓存投毒、版本漏洞、 前端安全、子域名接管等模块。

![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVukm5ZRVPcFLFC3AJGrYKn7hpKHf8XRUF6cDibC3hmP2GZ89KMfFnWrncMJvEWkISODMFhcIIj4xSvTgLib4sxfNGhGStKmhTUQA/640?wx_fmt=png&from=appmsg)

0x01 检测模块（35 个）

* 信息收集与指纹：爬虫、信息收集、指纹识别（60+ 规则）、版本漏洞提示、 robots/sitemap/well-known 情报、子域名枚举、子域名接管指纹。
* 配置与传输：安全头（9 项）、SSL/TLS、配置错误/点击劫持、前端安全（SRI/混合内容/CSP）、 HTTP 方法、Host 头注入、CORS、CSRF。
* 信息泄露：敏感信息、JS 密钥/端点、敏感路径暴露（600+ 路径）、 模板签名库（YAML，可扩展）、API 文档发现、CMS 专项。
* 注入与漏洞：SQL 注入、XSS/SSTI、LFI/命令注入、路径穿越、XXE、SSRF、 CRLF 注入、开放重定向、缓存投毒、Log4Shell、JWT 安全。
* 主动扫描：端口扫描（60+ 高危端口）、目录枚举。

启动时会显示实际加载的内置检测规则/签名总量（模板 + 敏感路径 + 指纹 + 载荷 + 端口 + 字典），当前 1000+，且可通过模板持续扩展。

0x02 模板签名引擎（v9 核心）

内置 templates/ 目录下的 YAML 模板即「可扩展的检测规则库」，新增检测无需改代码， 只要新增一个 YAML 文件。

格式类似 nuclei：

```
id: git-config-exposureinfo:  name: Git 配置文件暴露  severity: medium  category: 敏感信息泄露requests:  - path: /.git/config          # 或 paths: [/a, /b]    matchers-condition: and     # and | or    matchers:      - type: status            # status | word | regex | header        status: [200]      - type: word        words: ["[core]", "repositoryformatversion"]        condition: or
```

用 --templates DIR 追加你自己的模板目录。引擎只做「请求 + 声明式匹配」，不执行模板中的任何代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVuIDhOpzicticcX4rLruc1SEfqKicv31gJYreyjCgld4Q2H2cm2qr7e3TFcWKRXdiceHynqdZ7Lw3CH1COoq85U3shsfCBH4jO2qmQ/640?wx_fmt=png&from=appmsg)

0x03 基础设施

* Web UI：--web 启动 Flask 界面，SSE 实时进度、在线查看结果与报告
* 插件系统：--plugins DIR 从目录热加载自定义 BaseScanner 子类
* 批量扫描：-f targets.txt 用 asyncio 并发扫描多目标（--concurrency N）
* 配置文件：--config scanner.cfg 集中管理默认参数
* 多格式报告：JSON / HTML / Markdown / CSV + 风险评分 + 修复建议
* 负责任扫描护栏：作用域锁定、限速（令牌桶）、礼貌延迟、被动模式

0x04 安装与用法

pip install -r requirements.txt

pip install flask        # 仅使用 Web UI 时需要

# 基本扫描（启动时显示已加载规则总量）

python main.py https://example.com

![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVtvK1PzwIddI1N0XGDAeK6g7mXCMxZ7XyVkvXQeq0dpK8YZRoR8JZxDvA3icsT8lWf3oOakNl1e8r61bYS0jW9ekAOEOCaE6edA/640?wx_fmt=png&from=appmsg)

# 快速模式（跳过端口/目录/暴露/子域名等重型模块）

python main.py https://example.com --fast --html report.html

# 被动模式（仅非侵入式检测）

python main.py https://example.com --passive

# 追加自定义模板 + 插件

python main.py https://example.com --templates my\_templates --plugins plugins

# 带外探测（Log4Shell/SSRF）指定你自己的 collaborator

python main.py https://example.com --canary your.collaborator.net

# 批量扫描

python main.py -f targets.txt --concurrency 5 --html out.html

# Web UI

python main.py --web        # http://127.0.0.1:5000

![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVuaPiamjVR9u3icvaRNvftOpYUZSbyUjAbHGDnf0xa8b0CX2svsDwqGoKUkyFZSdd9fpcnibDibiajcMWk4tuiaBBhgqiceiaCC1hKPhWA/640?wx_fmt=png&from=appmsg)

# 作为模块运行

python -m webscanner https://example.com

完整参数见 python main.py -h。重型模块（exposure / ports / dirbust / subdomain） 请求量较大，可用 --fast 或 --skip <模块> 控制。

0x05 关于漏洞利用（重要）

本工具刻意只做「检测」不做「利用」。它会告诉你某处是否存在 SQL 注入 / SSRF / XXE / 路径穿越等，并给出证据与整改建议，但不会： 自动 dump 数据库、反弹 Shell、生成 Cookie 窃取 payload、通过 SSRF 读取 云元数据 / 内网 / 文件、通过 XXE 外带数据，或爆破 JWT 密钥 / 登录口令。 这些「利用」步骤会把「发现弱点」变成「实施攻击 / 窃取数据 / 取得控制权」， 超出评估型扫描器的职责。合法授权的漏洞验证若确需利用，请使用相应专用工具。

## **0x06 免责声明**

本工具仅供授权的安全测试与教育研究。使用者须确保已获得目标系统所有者的 书面授权。任何未经授权的扫描或攻击均属违法，开发者不对滥用行为负责。

请在使用本工具之前仔细阅读并理解上述免责声明。使用本工具即表示您同意遵守上述条款，并自行承担相应责任。

![](https://mmbiz.qpic.cn/mmbiz_gif/CQf7uHzmVb3icxXWABkpMvXDJ1aDF6RgkCFLMvzDgLEx7jjY4A1n7yTEc2AZmg5CFFoeHJLb3AiblNHRLVFBqlfw/640?wx_fmt=gif&from=appmsg)

```
下载地址

进入公众号回复关键字【20260901】获取项目链接
```

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/CQf7uHzmVb0EIJ0ELczkKSQrgZ1wuessmpgrvoBoc0mRN89FJMbDeXJQ0pGuUBicR84xicvbJe5iaqtVcpBuWMl4w/0?wx_fmt=png)

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