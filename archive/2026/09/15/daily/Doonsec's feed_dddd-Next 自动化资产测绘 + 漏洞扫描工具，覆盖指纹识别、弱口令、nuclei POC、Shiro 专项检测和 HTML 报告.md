---
title: dddd-Next 自动化资产测绘 + 漏洞扫描工具，覆盖指纹识别、弱口令、nuclei POC、Shiro 专项检测和 HTML 报告
url: https://mp.weixin.qq.com/s/ZUINewc4p6R1U2h9mGMRcg
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:02:56.603215
---

# dddd-Next 自动化资产测绘 + 漏洞扫描工具，覆盖指纹识别、弱口令、nuclei POC、Shiro 专项检测和 HTML 报告

# dddd-Next 自动化资产测绘 + 漏洞扫描工具，覆盖指纹识别、弱口令、nuclei POC、Shiro 专项检测和 HTML 报告

galact-byte
galact-byte

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**所有工具安全性自测！！！VX：****NightCTI**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**夜组安全**“**设为星标**”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg)

## 项目定位

`dddd-next` 是对原 SleepingBag945/dddd 项目的现代化重写。原项目自 2024 年后基本停更，但其依赖的 `nuclei`、`httpx`、`subfinder` 等仍在快速迭代，内置 POC 也已老化。本项目在保留 dddd 设计哲学的基础上，采用现代 Go 标准结构重构，依赖直接跟随 projectdiscovery 主线版本。

> **当前状态**：核心扫描链路已可用，并经过 Nacos、DVWA、Tomcat、Shiro、Redis、MySQL、Pikachu、sqli-labs、Vulfocus、WebGoat 等靶场回归；常用 `-t <ip> -p 1-65535` 全端口入口已复验。已知差异主要是 masscan 类超大网段加速和部分真实环境下模板兼容性需要持续回归。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMKUmkNwWCXoAU1w300os6X9aIHEia6ibo9vSiaogX4lD6mHCVJnc0npqXLicakPOiaW7Kic6lCSkFDwfEOVYD6DSb9naQxuVH2gRBsqw/640?wx_fmt=webp&from=appmsg)

## 与原项目的差异

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMJN97UQFF9rBlEyib47enDX2FbYjPGSIqvKVqb5Ze2jGWqWmHwLbuL0GxNiapJjaeBLPbWu1PfG3o3TTCoq0ia2HiaRXN4veyr8FCU/640?wx_fmt=webp&from=appmsg)

## 已实现能力

* 输入自动分类（IP / CIDR / IP-Range / URL / Domain / 测绘语法）
* 主动指纹识别（DSL 支持 `与 / 或 / 非 / 括号` 逻辑，8000+ 规则）
* 被动指纹识别（httpx wappalyzer 技术栈识别，含版本号，喂给 POC 精准选择）
* 产品路径二次指纹（探测 /nacos/、/druid/ 等已知产品路径，发现首页漏掉的子路径产品；`-no-dir` 关闭）
* 子域名枚举：被动 subfinder + 主动字典爆破（1721 词，含泛解析检测，`-nsb` 关闭爆破）+ DNS 解析
* 自研 TCP 端口扫描 + 服务指纹识别（fingerprintx，可识别非标准端口上的服务）
* 自定义 / 全端口扫描（`-p "80,443,8000-8100"`、`-p 1-65535` 或 `-p all`；默认使用原版风格 curated 端口集）
* ICMP 存活探测（`-ping` 可选预筛，大网段提速；默认关闭以免漏掉封 ICMP 的主机）
* CDN / WAF 识别（271 条 CNAME 库，含国内主流厂商；默认标记仍探测，`-skip-cdn` 可排除）
* 指纹 → POC 智能映射（只对命中产品发对应 POC，避免无效请求）
* Nuclei v3 漏洞扫描（默认指纹精准模式，`-full` 切全量）
* 弱口令爆破 **11 种**：SSH / FTP / MySQL / PostgreSQL / Redis / MSSQL / Oracle / MongoDB / SMB / RDP / Telnet
* 漏洞探测：MS17-010（EternalBlue 永恒之蓝）SMB 远程命令执行
* 未授权访问探测：memcached / ADB（安卓调试桥，RCE 等价）/ JDWP（Java 调试，RCE 等价）/ Telnet（直进 shell）
* NetBIOS 信息探测（UDP 137 + TCP 139 NTLM，泄露主机名 / 工作组 / 域 / OS 版本）
* Hunter / Fofa / Quake 测绘 API（`.env` 管理密钥）
* TXT / JSON / HTML 三种报告 + 审计日志；HTML 报告已重做为高密度暗色布局，支持严重度筛选、漏洞详情展开、请求 / 响应复制和指纹资产区

## 兼容状态与已知差异

已对齐或补齐的主链路：

* **gopocs 协议**：弱口令、探测型检测和 Shiro 专项爆破均已实现，含 RPC Endpoint Mapper 信息泄露。
* **recon 覆盖能力**：被动指纹、ICMP 存活、CDN 识别、产品路径二次指纹、自定义端口、全端口、主动子域名爆破和 OOB 盲打均已接入。
* **控制开关**：支持 nuclei 过滤（`-severity`/`-tags`/`-exclude-*`）、阶段跳过（`-no-brute`/`-no-poc`）和自定义凭据（`-up`/`-upf`）。
* **真实回归**：近期覆盖 Nacos、DVWA、Tomcat、Shiro、Redis、MySQL、Pikachu、sqli-labs、Vulfocus、WebGoat，并复验 `-t <ip> -p 1-65535` 入口。

仍需持续关注：

* masscan 类超大网段快速扫描（当前 TCP connect 为默认；`-st syn` 可用但依赖 npcap / 管理员权限）。
* nuclei 官方模板持续变化，个别 CVE 是否命中仍取决于模板兼容性、产品指纹和目标环境条件。
* 生产环境使用前建议先用授权靶标或小范围资产做回归确认。

## 工具获取

点击关注下方名片进入公众号

回复关键字【260915】获取下载链接

## 往期精彩

往期推荐

[EduSRC 教育行业漏洞猎洞工具 —— 基于搜索引擎 Dork 的一键式侦察 Chrome 扩展](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497655&idx=1&sn=36b38d3d6c80efc41a4a74da0d3869ef&scene=21#wechat_redirect)

[DeepSeek-V4.1 / V4 Flash 网络安全红队工具（无限四代）v0.3.0 纯净红队版](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497643&idx=1&sn=beef3f54f260361eb96dc8677d124448&scene=21#wechat_redirect)

[SQLMap GUI - 自动 SQL 注入工具](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497606&idx=1&sn=e10c3b90e73fab7a6af939836e94a8d6&scene=21#wechat_redirect)

[渗透测试实战Skill  5阶段方法论/19类攻击playbook/2887份H1真实案例/国产组件指纹库](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497590&idx=1&sn=9629e3f82a03ff2ab4799ed0e3182295&scene=21#wechat_redirect)

[一站式SRC资产测绘与监控模拟：企业资产采集 → 主动测绘 → 每日增量差异→ 本地仪表板](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497584&idx=1&sn=16e2d688b8aabcf67172e50141ed0ad7&scene=21#wechat_redirect)

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