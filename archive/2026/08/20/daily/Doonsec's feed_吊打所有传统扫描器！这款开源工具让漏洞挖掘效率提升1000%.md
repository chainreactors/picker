---
title: 吊打所有传统扫描器！这款开源工具让漏洞挖掘效率提升1000%
url: https://mp.weixin.qq.com/s/8qgRMizqCfzhcs1K5V_oQA
source: Doonsec's feed
date: 2026-08-20
fetch_date: 2026-08-21T03:01:39.054279
---

# 吊打所有传统扫描器！这款开源工具让漏洞挖掘效率提升1000%

# 吊打所有传统扫描器！这款开源工具让漏洞挖掘效率提升1000%

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明：本工具仅限授权安全测试使用，未经授权扫描他人系统属违法行为，使用者需自行承担法律责任。

RayScan 是一款 Python 编写的全栈 Web 漏洞扫描器，核心采用模块化架构设计，支持 SQL 注入、XSS、OA 专项、WebShell、弱口令、子域名枚举等检测能力。扫描引擎集成 Nuclei 12.5 万 PoC 模板，具备流式爬测协同、断点恢复、AI 误报复核等企业级功能。该项目通过 274 个自动化测试，在 Metasploitable 2 靶机实战中验证发现 83 个漏洞。

## 重点导读核心架构

### PART 01扫描引擎

* `wvs/core/scanner.py` — 主扫描逻辑
* `wvs/core/crawler.py` — 爬虫模块
* `wvs/core/session.py` — HTTP 会话管理
* `wvs/core/rate_limiter.py` — 限速控制
* `wvs/core/cache.py` — 扫描状态缓存

### PART 02检测模块

* `wvs/modules/sqli/` — SQL 注入（error-based/union/boolean-blind/time-based/二阶/宽字节/OOB）
* `wvs/modules/xss/` — 跨站脚本（反射型/存储型/Polyglot/mXSS/SSTI）
* `wvs/modules/oa/` — OA 专项检测（泛微/通达/金蝶/蓝凌/致远/用友/禅道/万户/Nacos/Spring/Jenkins/Confluence）
* `wvs/modules/webshell/` — WebShell 检测
* `wvs/modules/weakpass/` — 弱口令检测
* `wvs/modules/subdomain/` — 子域名枚举
* `wvs/modules/cmdi/` — 命令注入
* `wvs/modules/lfi/` — 本地文件包含
* `wvs/modules/rce/` — 远程代码执行
* `wvs/modules/ssrf/` — 服务端请求伪造
* `wvs/modules/xxe/` — XML 外部实体注入
* `wvs/modules/graphql/` — GraphQL 检测
* `wvs/modules/mcp/` — MCP 工具泄露检测
* `wvs/modules/api/` — API 安全检测
* `wvs/modules/sensitive/` — 敏感信息泄露
* `wvs/modules/waf/` — WAF 检测与绕过
* `wvs/modules/jspathfinder/` — JavaScript 端点发现

### PART 03第三方集成

* `wvs/integrations/nuclei_template_manager.py` — Nuclei PoC 管理（12.5 万模板）
* `wvs/integrations/` — AWVS/Nessus/sqlmap/ffuf 集成层

## 重点导读核心特性

### PART 04流式检测

爬取即检测，不等全部爬完。实战模式爬取 30 页，靶机模式爬取 150 页。

### PART 05双路径分流

检测到靶机 IP/路径自动走靶机流程（自动登录 → 爬取 → 检测），否则走实战流程（跳过靶场路径 → 浅爬 → 即爬即测）。

### PART 06三层降噪

内容特征 + 尺寸聚类 + 校准匹配。仅路径可达不再视为漏洞，基于响应证据判定。

### PART 07断点恢复

30 秒间隔落盘 checkpoint，支持 `--resume` 合并已发现漏洞并跳过已完成模块。

### PART 08AI 复核

支持 `--ai-verify` 误报复核，需配置 `LLM_API_KEY` 环境变量。

### PART 09MCP Server

支持 `--serve` 启动 MCP Server（http://127.0.0.1:18000/mcp），供 Claude/ChatGPT 直接驱动扫描。

## 重点导读检测能力

| 漏洞类型 | 检测维度 |
| --- | --- |
| SQL 注入 | error-based / union / boolean-blind / time-based / stacked / 二阶 / 宽字节 / OOB |
| XSS | reflected / stored / Polyglot / mXSS / SSTI |
| OA 系统 | 泛微Ecology / 通达OA / 金蝶Kingdee / 蓝凌Landray / 致远Seeyon / 用友Yonyou / 禅道Zentao / 万户Whir / Nacos / Spring Boot / Jenkins / Confluence |
| WebShell | 路径扫描 + 内容特征 + 启发式检测 |
| 弱口令 | 表单登录 + phpMyAdmin + Tomcat Manager |
| 子域名 | DNS 爆破 + crt.sh 证书透明度 |

## 重点导读使用方式

### PART 10命令行扫描

```
bashpython -m wvs scan https://target.com --insecure --rate 10
python -m wvs scan https://target.com --all-modules
python -m wvs batch targets.txt
python -m wvs list-modules
```

### PART 11Web UI（推荐）

```
bashpip install flask
python web_ui/app.py
```

浏览器访问 http://localhost:5000。

![RayScan Web UI](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UoDEyTic7k2MRe387BRM6r3om4En8lqGKC5BowMZM0SsfdkbqC5jz83mEap6vwF3HosdvDicy2oR33PBztcL4JqKficpFPdjYqYVg/640?from=appmsg)

RayScan Web UI

### PART 12报告输出

支持 HTML / JSON / CSV / Markdown / Console 格式输出。

```
bashpython -m wvs scan https://target.com -o report.json -f json
```

## 重点导读项目结构

```
rayscan/
├── wvs/                       # 核心扫描库
│   ├── core/                  # 扫描引擎
│   ├── modules/               # 检测模块
│   ├── integrations/          # 第三方集成
│   ├── reporting/             # 报告生成
│   ├── profiles/              # 扫描配置
│   └── plugins/               # 认证插件
├── web_ui/                    # Flask Web UI
├── scripts/                   # 工具脚本
├── tools/                     # 辅助工具
├── tests/                     # 测试用例
├── docs/                      # 技术文档
├── full_scan.py               # 全量扫描入口
├── quick_scan.py              # 快速扫描入口
└── pyproject.toml             # 项目配置
```

## 重点导读实战验证

RayScan 在 Metasploitable 2 靶机上的扫描结果：

* 检测出 83 个漏洞
* SQL 注入提取 5 个用户账号密码
* LFI 成功读取 /etc/passwd
* 发现 /test/ 目录、phpinfo.php、phpMyAdmin 密码泄露等敏感信息

![RayScan CLI 扫描结果](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Urf4GEQpSJkq8AnSRKziaLP08mFRu8KZrlJ3RwG4Dd7M8UwcNETw0nxnAx4HZkQV3zVs4UxmtYQWJK20THx7MaHLP7gdOGcjk8E/640?from=appmsg)

RayScan CLI 扫描结果

![RayScan CLI 漏洞详情](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uple9DiaSIBgkvzThXE5uCFLmULrRLUiaNIwzSnGc7CwrCTsiaNqL4UwOJst9Fh3En6icsnuQffOLnzic7clDbHBCaQ0ibMEMFSYXNz0/640?from=appmsg)

RayScan CLI 漏洞详情

## 重点导读技术亮点

* **Nuclei 12.5 万 PoC 引擎**：扫描主流程默认启用，支持智能模板选择，无 CLI 时走内置内容特征回退
* **OA 三级检测链路**：内容指纹识别 → 版本识别 → 规则级响应证据验证 + 版本过滤
* **扫描断点恢复**：30 秒间隔落盘，支持任务中断后恢复
* **误报治理基线**：全部检测判定基于响应证据，仅路径可达不再视为漏洞
* **流式检测**：爬取即检测，不等全部爬完
* **双路径自动分流**：靶机/实战自动识别并切换流程

本公众号非项目作者，仅做技术分享。

本文介绍的项目开源地址如下：

```
https://github.com/xiabai2008/rayscan
```

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uo92ttpaST81DYDXCO9kpTbkQhluCSo7YVwcYCsNH47b2Y0us0AdaKpZqqQ7EIc6Y7EWEcYcG0hLgVo0nAaEP84Mua5llK8hicc/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UoGia3qhL3RGWg6LIBkooYQhFOuTcVM0woWiaribbU2GGJXBibCKenAhf0DnY8ZHT4Fl67VrtoZpyQ7prkWNIm93FjQEPcWBqT7O7o/640?from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0UrCSxv33ws9W4q7NCsLZiaWAQPkO1Tr0E81AlzPiah3DzibhDxWLTTViaTb8BXvSoRhkkJ3hqFMlfrhIxlSZ8CWyBib5lyyLQyJ36Wo/0?wx_fmt=png)

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