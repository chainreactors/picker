---
title: 网安|渗透|电子取证实战 700+ 个 Cybersecurity Skills 精选推荐|适配常见Agent
url: https://mp.weixin.qq.com/s/y_SNJMoDC9p-csKVBPrQNw
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:36:10.546901
---

# 网安|渗透|电子取证实战 700+ 个 Cybersecurity Skills 精选推荐|适配常见Agent

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RPq1g3ib528htHOh2nR8hkOkWu0lNicib7FZnHk4pASoStbp18HwLkgGXiaBHZQS8R46hlMDVuXVBSKibck61cErcoQK9FPdHkqMqjIAvxBCmPD8/0?wx_fmt=jpeg)

# 网安|渗透|电子取证实战 700+ 个 Cybersecurity Skills 精选推荐|适配常见Agent

原创

0xSec笔记本
0xSec笔记本

0xSec笔记本

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 电子取证实战工具清单｜700+ 个 Cybersecurity Skills 精选整理

最近收藏了 GitHub 上一个开源项目 Anthropic-Cybersecurity-Skills[1]，里面收录了 700+ 个网络安全技能模块，涵盖取证、溯源、渗透、情报等方向。

这份清单原本是按功能和对象两个维度分类的，但用起来还是感觉不够顺手——更像是技术词汇表，而不是办案工具箱。所以按照实际工作场景重新梳理了一遍，挑出了真正用得上的部分，分享给做电子取证和网络攻防的朋友。

结合 Claude Code、Hermes、Codex 这几个Agent工具，很多原本要手写的脚本和查询语句现在可以快速生成，效率提升比较明显。

---

## 一、移动端取证

手机是案件里出现频率最高的证据载体，Android 和 iOS 各有一套取证路径，下面这些 Skills 基本覆盖了从采集到分析的完整流程。

| 技能名称 | 功能说明 |
| --- | --- |
| `performing-mobile-device-forensics-with-cellebrite` | Cellebrite 采集与分析 |
| `performing-android-app-static-analysis-with-mobsf` | Android APK 静态分析 |
| `performing-dynamic-analysis-of-android-app` | Android 动态行为分析 |
| `analyzing-android-malware-with-apktool` | APKTool 恶意样本逆向 |
| `reverse-engineering-android-malware-with-jadx` | JADX 反编译分析 |
| `analyzing-ios-app-security-with-objection` | iOS 运行时注入分析 |
| `reverse-engineering-ios-app-with-frida` | Frida Hook iOS 应用 |
| `performing-mobile-app-certificate-pinning-bypass` | 证书绑定绕过 |
| `intercepting-mobile-traffic-with-burpsuite` | BurpSuite 抓包分析 |
| `testing-android-intents-for-vulnerabilities` | Android Intent 漏洞测试 |
| `conducting-mobile-app-penetration-test` | 移动端渗透测试 |

APK 解包这块可以用 Claude Code 写自动化脚本，把解包、字符串提取、URL 筛查串起来，省掉不少重复操作。

---

## 二、终端与介质取证

### Windows 痕迹分析

注册表、事件日志、Amcache 是 Windows 取证的基本功，Sysmon 配合 Sigma 规则能覆盖大部分常见攻击手法。

| 技能名称 | 功能说明 |
| --- | --- |
| `analyzing-windows-event-logs-in-splunk` | Windows 事件日志关联分析 |
| `analyzing-windows-registry-for-artifacts` | 注册表取证 |
| `analyzing-windows-amcache-artifacts` | Amcache 程序执行痕迹 |
| `detecting-mimikatz-execution-patterns` | Mimikatz 执行痕迹检测 |
| `detecting-t1055-process-injection-with-sysmon` | Sysmon 进程注入检测 |
| `performing-active-directory-compromise-investigation` | AD 域渗透调查 |

### Linux 痕迹分析

| 技能名称 | 功能说明 |
| --- | --- |
| `analyzing-linux-audit-logs-for-intrusion` | Linux 审计日志分析 |
| `analyzing-linux-system-artifacts` | Linux 系统痕迹提取 |
| `analyzing-persistence-mechanisms-in-linux` | 持久化机制分析 |
| `performing-linux-log-forensics-investigation` | Linux 日志取证调查 |

### 内存与磁盘取证

内存取证这块 Volatility3 已经是主流，Rekall 用的人越来越少，但部分老镜像还是需要。时间线重建推荐 Plaso，配合 Timesketch 做可视化效果不错。

| 技能名称 | 功能说明 |
| --- | --- |
| `conducting-memory-forensics-with-volatility` | Volatility 内存取证 |
| `performing-memory-forensics-with-volatility3` | Volatility3 内存分析 |
| `extracting-memory-artifacts-with-rekall` | Rekall 内存提取 |
| `extracting-credentials-from-memory-dump` | 内存中凭证提取 |
| `acquiring-disk-image-with-dd-and-dcfldd` | 磁盘镜像采集 |
| `performing-disk-forensics-investigation` | 磁盘取证调查 |
| `recovering-deleted-files-with-photorec` | PhotoRec 文件恢复 |
| `performing-timeline-reconstruction-with-plaso` | Plaso 时间线重建 |
| `extracting-browser-history-artifacts` | 浏览器历史记录提取 |
| `performing-sqlite-database-forensics` | SQLite 数据库取证 |

Volatility3 的自动化脚本用 Codex 生成很方便，pslist、netscan、cmdline 这几个插件串起来跑，结果整理成报告格式，基本不用自己动手写。

---

## 三、网站与网络行为分析

### Web / API 安全分析

| 技能名称 | 功能说明 |
| --- | --- |
| `analyzing-api-gateway-access-logs` | API 访问日志分析 |
| `exploiting-idor-vulnerabilities` | IDOR 漏洞验证 |
| `exploiting-jwt-algorithm-confusion-attack` | JWT 算法混淆攻击 |
| `exploiting-server-side-request-forgery` | SSRF 漏洞利用 |
| `testing-for-xss-vulnerabilities` | XSS 测试 |
| `testing-for-xxe-injection-vulnerabilities` | XXE 注入测试 |
| `testing-cors-misconfiguration` | CORS 配置错误测试 |
| `testing-websocket-api-security` | WebSocket 安全测试 |
| `performing-api-fuzzing-with-restler` | RESTler API 模糊测试 |

### 域名 / 证书 / 基础设施溯源

证书透明度日志（CT Log）在基础设施溯源里很好用，配合 URLScan 和被动 DNS 能还原不少攻击者的历史资产。

| 技能名称 | 功能说明 |
| --- | --- |
| `analyzing-tls-certificate-transparency-logs` | CT 日志证书透明度分析 |
| `performing-dns-enumeration-and-zone-transfer` | DNS 枚举与区域传输 |
| `tracking-threat-actor-infrastructure` | 威胁行为者基础设施追踪 |
| `analyzing-malicious-url-with-urlscan` | URLScan 恶意 URL 分析 |
| `detecting-typosquatting-packages-in-npm-pypi` | 域名抢注 / 包仿冒检测 |

### 流量与协议分析

| 技能名称 | 功能说明 |
| --- | --- |
| `analyzing-network-traffic-with-wireshark` | Wireshark 流量分析 |
| `analyzing-network-packets-with-scapy` | Scapy 数据包解析 |
| `performing-network-traffic-analysis-with-zeek` | Zeek 流量分析 |
| `detecting-command-and-control-over-dns` | DNS C2 通信检测 |
| `detecting-beaconing-patterns-with-zeek` | Zeek 检测 Beacon 心跳 |
| `hunting-for-dns-tunneling-with-zeek` | DNS 隧道狩猎 |
| `analyzing-dns-logs-for-exfiltration` | DNS 数据外传分析 |

---

## 四、云平台与日志调查

云上取证和传统取证差别不小，权限模型、日志格式、保留策略都不一样。CloudTrail 和 Azure Activity Log 是最常见的两个入口，Office365 的审计日志在 BEC 案件里基本是必查项。

| 技能名称 | 功能说明 |
| --- | --- |
| `analyzing-azure-activity-logs-for-threats` | Azure 活动日志威胁分析 |
| `analyzing-office365-audit-logs-for-compromise` | Office365 审计日志调查 |
| `detecting-aws-cloudtrail-anomalies` | AWS CloudTrail 异常检测 |
| `performing-cloud-forensics-investigation` | 云环境取证调查 |
| `performing-cloud-native-threat-hunting-with-aws-detective` | AWS Detective 云上威胁狩猎 |
| `analyzing-kubernetes-audit-logs` | K8s 审计日志分析 |
| `remediating-s3-bucket-misconfiguration` | S3 配置错误处置 |

CloudTrail 原始 JSON 丢给 Hermes，让它按 MITRE ATT&CK 标注可疑调用，比自己逐条看省时间很多。

---

## 五、恶意样本与攻击链分析

### 样本分析与逆向

| 技能名称 | 功能说明 |
| --- | --- |
| `analyzing-cobalt-strike-beacon-configuration` | CS Beacon 配置分析 |
| `analyzing-malware-behavior-with-cuckoo-sandbox` | Cuckoo 沙箱行为分析 |
| `performing-malware-triage-with-yara` | YARA 规则分类筛查 |
| `extracting-config-from-agent-tesla-rat` | AgentTesla RAT 配置提取 |
| `extracting-iocs-from-malware-samples` | 恶意样本 IOC 提取 |
| `deobfuscating-powershell-obfuscated-malware` | PowerShell 混淆代码还原 |
| `deobfuscating-javascript-malware` | JavaScript 恶意代码去混淆 |
| `reverse-engineering-malware-with-ghidra` | Ghidra 逆向分析 |
| `reverse-engineering-rust-malware` | Rust 恶意软件逆向 |

### 勒索软件专题

勒索软件案件量这两年持续上涨，加密机制分析和密钥恢复是核心难点，下面几个 Skills 针对性比较强。

| 技能名称 | 功能说明 |
| --- | --- |
| `analyzing-ransomware-encryption-mechanisms` | 勒索软件加密机制分析 |
| `reverse-engineering-ransomware-encryption-routine` | 勒索加密算法逆向 |
| `recovering-from-ransomware-attack` | 勒索软件攻击恢复 |
| `hunting-for-cobalt-strike-beacons` | CS Beacon 狩猎 |

根据样本特征生成 YARA 规则这块，Claude Code 写起来很快，给出字节序列或行为描述，直接出规则，调整一下就能用。

---

## 六、邮件与社会工程取证

邮件取证在 BEC、钓鱼、内部泄密案件里都是基础工作，邮件头解读是入口，DMARC/DKIM/SPF 验证是判断伪造发件人的关键。

| 技能名称 | 功能说明 |
| --- | --- |
| `analyzing-email-headers-for-phishing-investigation` | 邮件头钓鱼调查 |
| `detecting-business-email-compromise` | BEC 商业邮件欺诈检测 |
| `detecting-email-account-compromise` | 邮件账号入侵检测 |
| `investigating-phishing-email-incident` | 钓鱼邮件事件调查 |
| `implementing-dmarc-dkim-spf-email-security` | DMARC/DKIM/SPF 邮件安全配置 |
| `detecting-qr-code-phishing-with-email-security` | 二维码钓鱼检测 |
| `performing-phishing-simulation-with-gophish` | GoPhish 钓鱼模拟演练 |
| `testing-for-email-header-injection` | 邮件头注入测试 |
| `building-phishing-reporting-button-workflow` | 钓鱼举报一键工作流 |

邮件原始头（Raw Header）直接粘给 Hermes，让它按发件 IP、验证结果、伪造发件人特征这几个维度逐项分析，比手动解读快不少，批量处理时候特别有用。

---

## 七、情报收集与威胁归因

OSINT 和 IOC 富化是溯源的两条腿，MISP 做情报共享、OpenCTI 做关联分析，这套组合在有一定规模的团队里比较成熟。

| 技能名称 | 功能说明 |
| --- | --- |
| `building-threat-actor-profile-from-osint` | OSINT 威胁行为者画像 |
| `analyzing-apt-group-with-mitre-navigator` | MITRE Navigator APT 分析 |
| `analyzing-threat-actor-ttps-with-mitre-attack` | ATT&CK TTP 关联分析 |
| `tracking-threat-actor-infrastructure` | 基础设施追踪 |
| `building-ioc-enrichment-pipeline-with-opencti` | OpenCTI IOC 富化流水线 |
| `building-threat-feed-aggregation-with-misp` | MISP 情报聚合 |
| `processing-stix-taxii-feeds` | STIX/TAXII 情报处理 |
| `automating-ioc-enrichment` | IOC 自动富化 |
| `generating-threat-intelligence-reports` | 威胁情报报告生成 |
| `performing-brand-monitoring-for-impersonation` | 品牌仿冒监控 |
| `monitoring-darkweb-sources` | 暗网情报监控 |
| `correlating-threat-campaigns` | 威胁活动关联分析 |

---

## 八、工具搭配说明

这几个工具各有侧重，按场景选对了用起来顺很多：

| 使用场景 | 推荐工具 |
| --- | --- |
| 脚本 / 代码编写 | Claude Code、Codex |
| 长日志关联分析 | Herm...