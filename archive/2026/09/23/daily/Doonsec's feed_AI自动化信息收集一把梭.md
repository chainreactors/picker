---
title: AI自动化信息收集一把梭
url: https://mp.weixin.qq.com/s/R6b2sak2Sb70vs80va7zeQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:05:59.949273
---

# AI自动化信息收集一把梭

# AI自动化信息收集一把梭

Dest1ny-Sec
Dest1ny-Sec

HACK之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

### 工具介绍

## 它不是 nmap 套壳，而是一个 **Claude 智能评分的多 Agent 侦察系统**

传统侦察工具是"哑管道" —— 跑扫描、拿数据、手动翻。Desinter\_scan 不同：**22 个 collector 并发扫，Claude 按 6 维度智能评分，按攻击优先级排序输出**，告诉你"打哪"。

* **22 个**

  collector 并发扫（subfinder / nuclei / httpx / nmap / gau / waybackurls / assetfinder）
* Claude 按 **6 维度**（业务敏感度 / 攻击面 / 历史漏洞 / 暴露度 / 资产价值 / 攻击复杂度）智能评分
* 按**攻击优先级**排序输出 — Critical → High → Medium，告诉你"打哪"

**inter\_scan** 是一个多 Agent 并发信息收集系统，将资产发现、服务探测、深度扫描三阶段流水线化，扫描完成后由 Claude AI 自动进行多维度价值评估，输出按攻击优先级排序的资产列表。

## **![Desinter_scan — AI 自动化信息收集一揽子](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic6ibBaHTkMC6w5KOlrqMCkh2VbzE5dfhIkkW1AvMsQep6V8TavicAqSpGD83DCicGDCjsNO7Km6FZ5h4uSFNuTP4Bk0Imhxe16iciayo/640?wx_fmt=png&from=appmsg)![]()**

## 快速开始

```
# 环境检测python3 run.py--check-tools
# 快速扫描（默认）— DNS 爆破 2000 条 + Top 端口 + 中字典python3 run.py--target example.com
# 深度扫描 — DNS 爆破 8000 条 + 全端口 + 大字典python3 run.py--target example.com--deep
# 全并发模式（跳过 Phase 依赖，所有 collector 同时跑）python3 run.py--target example.com--flat
# 启用截图 + 查看进度python3 run.py--target example.com--phase4python3 run.py--target example.com--status
# 断点续扫python3 run.py--target example.com--resume
# 只跑指定 collectorpython3 run.py--target example.com--agents subdomain,port_scan,source_leak
```

## Claude AI 集成

在 Claude Code 中直接对话使用：

```
/recon example.com        # 扫描 + 智能评分，一键搞定/prioritize example.com   # 已有扫描结果，只做评分分析
```

Claude 会自动：

1. 读取扫描结果（优先读 vulnerable / leak / cloud 高价值资产）
2. 按 6 维度评分引擎打分
3. 输出五层优先级报告（★★★★★ → ★）

## 架构

```
run.py (并行引擎)  ├─ Phase 1: 6 个 Collector 串行（资产发现，有依赖）  │   enterprise → subdomain → dns_enum → asn_bgp → cdn_ip → cloud_assets  ├─ Phase 2: 2 个 Collector 串行（服务探测）  │   port_scan → network_space  ├─ Phase 3: 14 个 Collector 全并发（深度扫描）  │   http_probe / waf_detect / dir_scan / cms_finger /  │   source_leak / js_api / crawler / mobile / github_leak /  │   nuclei_scan / wayback_history / site_metadata / api_probe /  │   legacy_hunter  └─ Phase 4: 可选（screenshot）         ↓  SQLite 数据库（实时写入）         ↓  Claude 读取 → 智能评估 → 输出优先攻击面
```

### 23 个 Collector

| Phase | Collector | 功能 |
| --- | --- | --- |
| 1 | enterprise | 企业产权 WHOIS/ICP 备案 |
| 1 | subdomain | 14 源子域名 + DNS 爆破（智能根域识别） |
| 1 | dns\_enum | 全 DNS 记录 + AXFR + SPF |
| 1 | asn\_bgp | ASN → IP 段展开 |
| 1 | cdn\_ip | CDN 检测 + IP 反查 + Favicon 哈希 |
| 1 | cloud\_assets | crt.sh 云搜索 + CNAME 分析 + Bucket 探测 |
| 2 | port\_scan | 全端口 + UDP + 敏感服务检测 |
| 2 | network\_space | FOFA / Shodan / ZoomEye |
| 3 | http\_probe | 批量 HTTP + Title + 聚类 |
| 3 | waf\_detect | WAF/CDN 15+ 特征识别 |
| 3 | dir\_scan | 7000+9638+45522 字典 + 平台专属路径 |
| 3 | cms\_finger | WhatWeb + 30+ 内置指纹 |
| 3 | source\_leak | .git/.svn/.env/备份/Swagger/Actuator/Druid |
| 3 | js\_api | JS 密钥 + API 端点提取 |
| 3 | crawler | 爬虫 + 隐藏子域/外链 |
| 3 | mobile | ⭐ APK下载+解包+密钥提取 + iOS探测 + 小程序检测 |
| 3 | github\_leak | GitHub dork 搜索密钥/配置 |
| 3 | nuclei\_scan | Nuclei CVE 扫描 |
| 3 | wayback\_history | Wayback Machine 历史 URL |
| 3 | site\_metadata | robots.txt/sitemap/邮箱/第三方服务 |
| 3 | api\_probe | GraphQL 内省 + API 版本探测 |
| 3 | legacy\_hunter | 🆕 过期框架检测 (Struts/Axis/WebLogic) + 死端点复活 + EOL 版本 |
| 4 | screenshot | gowitness 批量截图 |

## 实时告警

扫描中以下发现会**立即标记** ★：

| 告警 | 触发条件 |
| --- | --- |
| ★ Redis 未授权 | 6379 PING → PONG |
| ★ Docker API 未授权 | /containers/json → 200 |
| ★ Elasticsearch 未授权 | /\_cat/indices 可读 |
| ★ MongoDB 未授权 | 27017/27018 开放 |
| ★ 公开 S3 Bucket | Bucket URL → 200 |
| ★ .git 泄露 | /.git/HEAD → 200/403 |
| ★ GitHub 密钥泄露 | AKIA / secret\_key / password |
| ★ JS 硬编码密钥 | AK/SK/Bucket/Token |

## AI 评分引擎

扫描完成后 Claude 按以下维度评分：

| 维度 | 权重 | 满分标准 |
| --- | --- | --- |
| 服务风险 | 30% | Redis/Docker 未授权, 敏感端口 |
| 泄露严重度 | 25% | GitHub 密钥, .git 可恢复, 备份文件 |
| 云资产暴露 | 15% | 公开 S3, 受限 Bucket, 云函数 |
| CMS 漏洞潜力 | 15% | 已知 RCE CMS + 旧版本 |
| API/管理面 | 10% | Swagger+Actuator+Druid, 管理后台 |
| 关联度 | 5% | 直连 IP > CDN 后 > 同 C 段 |

输出五层报告：

```
apis:  fofa_email: ""  fofa_key: ""  shodan_key: ""  zoomeye_key: ""  ipinfo_token: ""# 免费 50k/月
```

项目地址

https://github.com/Dest1ny-Sec/Desinter\_scan

> V8 / Kernel 方向师傅看过来 👀
>
> 这边有个长期线上项目，主要找 V8 / Chromium、Kernel、Pwn、二进制相关方向的师傅。一道题最高 5000 元现金。
>
> 自己能做，直接来。
>
> 自己不做也没关系，转发文章还能领500刀 Token 。
>
> 项目具体做什么、怎么参与、奖励怎么领，扫码进去看👇
>
> ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HqolA1dQic69jYTxLhAglNccgEyqrN4JuzhlehB5LHx8Et9RZhhKeSYRCUOicM0TcCS0WDxfmxJrvURusXuniaK9f2HNgUqiaFdQmn3YMQhsDrE/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GzdTGmQpRic1orFibqtmBJd06F33KoWTM6qEUAG7ZbwicA5MhTqx9stelHv8cMgibthiahUBTtgbPgn3ia2bYLpBElTQ/0?wx_fmt=png)

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