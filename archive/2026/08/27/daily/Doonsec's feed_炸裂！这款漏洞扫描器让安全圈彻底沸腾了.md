---
title: 炸裂！这款漏洞扫描器让安全圈彻底沸腾了
url: https://mp.weixin.qq.com/s/RBmdjtaXllVpFS1KsiOelQ
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:35:09.176957
---

# 炸裂！这款漏洞扫描器让安全圈彻底沸腾了

# 炸裂！这款漏洞扫描器让安全圈彻底沸腾了

棉花糖糖糖
棉花糖糖糖

棉花糖网络安全工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本工具仅允许在拥有完整授权的靶场环境使用。未经授权扫描、渗透属于违法行为，使用者自行承担全部法律责任。

## 重点导读简介

MrCipher 是一款基于 dddd 深度改造的综合漏洞扫描器，融合多源渗透工具链，集成高级漏洞挖掘引擎。该工具将主机发现、端口扫描、协议识别、子域枚举、Web 指纹探测、漏洞检测、后渗透验证整合为自动化流水线，面向红队攻防、安全服务、授权渗透测试场景。

## 重点导读核心架构

### PART 01工作流设计

```
目标输入 → 类型识别 → 主机发现 → 端口扫描 → 协议识别
    ↓
Web 探针 → 指纹识别 → 漏洞映射 → Nuclei 检测 → GoPoc 爆破
    ↓
高级引擎 → 深度扫描 → WAF 绕过 → 小众检测 → OWASP Top10
    ↓
报告生成 → 审计日志
```

### PART 02模块划分

| 模块 | 职责 |
| --- | --- |
| `advanced/` | 高级漏洞挖掘引擎 |
| `common/` | 核心功能、CLI 参数、配置文件 |
| `gopocs/` | GoPoc 服务爆破引擎 |
| `lib/` | 内置第三方库 |
| `structs/` | 数据结构定义 |
| `utils/` | 工具函数 |

## 重点导读高级引擎

### PART 03深度扫描

敏感路径探测覆盖 `.git`、`.svn`、`.env`、`swagger`、`actuator` 等 200+ 路径。

GraphQL 内省与注入检测。JavaScript 文件分析支持 API 端点提取、硬编码密钥识别、Source Map 解析。API 端点枚举与调试端点探测（pprof/jolokia/debug）。备份文件发现。云元数据获取（AWS/GCP/Azure/阿里云/腾讯云）。

### PART 04WAF 绕过

支持 Cloudflare、Akamai、ModSecurity、安全狗、云盾、360 等 WAF 指纹识别。

SQL 注入绕过手段包括编码、大小写、注释、空格替代、双重编码。XSS 过滤绕过涵盖标签变形、事件处理器、编码、DOM Clobbering、CSP 绕过。命令注入绕过支持空格替代、变量拼接、通配符、花括号、编码。路径穿越编码绕过支持双重 URL 编码、Unicode、混合编码。文件上传绕过包括双扩展名、Null byte、Content-Type、Magic bytes、.htaccess。认证绕过支持 JWT none、SQL 注入登录、参数污染、方法覆盖。

### PART 05小众检测

SSTI 检测支持 Jinja2、Twig、Freemarker、Velocity、Smarty、Mako、Pebble。SSRF 深度测试覆盖云元数据、内部服务、DNS 重绑定、协议走私。XXE 检测支持基础、OOB、盲注、SVG、SOAP、XInclude。JWT 攻击涵盖 none 算法、弱密钥、RS256→HS256、kid 注入、JWK 注入。反序列化检测覆盖 Java、PHP、Python、.NET。HTTP 请求走私支持 CL.TE、TE.CL、TE.TE、H2C。额外检测项包括原型污染、竞态条件、CORS 配置错误、Host 头注入、Web 缓存中毒。

### PART 06深度验证

SQL 注入验证可提取数据库版本、库名、用户、表、敏感数据。RCE 验证支持执行 id、whoami、uname、读取 /etc/passwd。SSRF 验证可提取云凭据、访问内部服务。文件读取验证覆盖 /etc/passwd、SSH 密钥、云凭据、应用配置。文件上传验证上传测试文件并验证代码执行。XXE 验证支持文件读取、OOB 外带。SSTI 验证识别引擎并执行命令。信息泄露验证通过正则扫描响应体中的敏感数据。默认凭证验证支持表单、Basic Auth、API Token。

### PART 07OWASP Top10

A01 失效访问控制涵盖 IDOR、路径穿越、参数篡改、JWT 操纵。A02 加密失效覆盖 HTTPS、TLS、Cookie 标志、弱哈希、硬编码密钥。A03 注入涵盖 NoSQL、LDAP、XPath、CRLF、EL 注入。A04 不安全设计涵盖速率限制、密码策略、账户枚举、业务逻辑。A05 安全配置错误涵盖目录浏览、缺失安全头、调试模式、危险 HTTP 方法。A06 易受攻击组件涵盖版本检测、CVE 关联。A07 认证失效涵盖暴力破解、用户枚举、会话管理、密码重置。A08 数据完整性涵盖反序列化、JWT、CI-CD 暴露。A09 日志监控失效涵盖日志文件暴露、监控端点。A10 SSRF 涵盖云元数据、内部端口扫描、协议走私。

## 重点导读融合工具

OA-EXPTOOL 提供 111 个 OA 漏洞 POC，覆盖蓝凌、万户、致远、通达 OA。OneForAll 子域名字典合并 977K+ 条目。Nuclei Templates 集成工作流、SSL、DNS 模板。gonmap 内置协议识别功能。

## 重点导读服务爆破

GoPoc 引擎支持 SSH、FTP、MySQL、MSSQL、Oracle、Redis、MongoDB、RDP、SMB、Telnet、PostgreSQL 暴力破解。额外支持 MS17-010 永恒之蓝检测、Shiro Key 爆破。

## 重点导读使用模式

### PART 08命令行模式

```
bashMrCipher -t 192.168.0.1
MrCipher -t 192.168.0.0/24
MrCipher -t http://test.com
MrCipher -t example.com -sd
MrCipher -t http://www.xxx.com -npoc
MrCipher -t http://test.com -na
MrCipher -t http://test.com -poc log4j
MrCipher -t 172.16.100.1 -a
```

### PART 09交互式控制台

无参数运行进入交互界面，63 个可配置选项。扫描检测到 SQL 注入时自动进入后渗透控制台，支持库、表、列枚举与脱库操作。

```
bashMrCipher
MrCipher poc list
MrCipher poc POC-001
MrCipher poc POC-001 sqli dbs
```

### PART 10Web 界面

```
bashMrCipher -ui
MrCipher -ui -ui-bind 0.0.0.0:8787
```

浏览器访问 `http://127.0.0.1:8787` 进入可视化控制台，支持配置全部扫描参数、实时流式回显结果、MSF 模块面板、PoC 后渗透面板。

## 重点导读空间搜索

支持 Hunter、Fofa、Quake 三大网络空间搜索引擎。可从空间搜索引擎导入目标资产并进入扫描流程。

## 重点导读指纹体系

指纹数据库 `finger.yaml` 支持 header、body、server、title、cert、port、protocol、path、status、banner 等规则类型。各类规则支持与（&&）、或（||）、非（!）任意组合。

主动指纹数据库 `dir.yaml` 支持指定路径探测，覆盖 Nacos、Druid、Geoserver 等应用。

工作流数据库 `workflow.yaml` 建立指纹到漏洞的映射，确保只对匹配目标发起漏洞检测。

## 重点导读输出报告

文本/JSON 格式结果输出至 `result.txt`。HTML 漏洞报表包含请求/响应包留存、数据库基础信息、SMB 共享目录信息。审计日志记录程序运行日志与收发包详细信息。

## 重点导读项目地址

本文介绍的项目开源地址如下：

```
https://github.com/AWY-Cipher/MrCipher
```

本公众号非项目作者，仅做技术分享。

## 广告时间

**低价考证包括但不限于CISP系列、PMP等等国内网安证书、网络安全交流群请关注公众号后点菜单栏的找棉花糖。**

**糖心会员站，网络安全必备网站，包括在线内网靶场、web靶场、src靶场、应急响应靶场，以及各种网安资料、教程、方案模版、以及超级多在线工具，99元包年！详细介绍：**[棉花糖会员站介绍(26年4月26日版本) ：在线内网靶场、网安资料方案、在线工具全能资源站](https://mp.weixin.qq.com/s?__biz=MzkyOTQzNjIwNw==&mid=2247493656&idx=1&sn=ef2aad19a122c739055604331f93f34c&scene=21#wechat_redirect)**，看完介绍百分百心动！**

![棉花糖会员站介绍图1](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0UqBGoJAqNPLsFoSBXW00LQhxGeT2sS3Z07EA5eo3W3fl9xAjbHyaU4Tde5gGCRfd6V7F2xh6zz7ZKCNdH4xQ08HC0tmgj9QxhI/640?from=appmsg)

![棉花糖会员站介绍图2](https://mmbiz.qpic.cn/sz_mmbiz_png/x5l8unjI0Uoicuibsak5SxZ1CF9ibCTARelIFc8JXgAEZVMEtlHavfYVAO0w18xQwa58hJx9xfKLNfroMogNXbX23wibTz6kiaDEiaN5ToIS8a4Y8/640?from=appmsg)

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