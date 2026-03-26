---
title: 安全日报 | 2026年3月25日
url: https://mp.weixin.qq.com/s/t66lfPf2RjDs8fZskDAG-g
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:27:08.918431
---

# 安全日报 | 2026年3月25日

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MaPMjrvzf7fV6MA2zZGCEaL1tQSIM5ydibpcmg9bBBTgJXse6CV2N1XGsQyKic0eShklB6ibjUvQrpiaIxprmk7FTYKBZOPSqeOGxsShialegZLw/0?wx_fmt=jpeg)

# 安全日报 | 2026年3月25日

原创

安全诸子

![]()

在小说阅读器中沉浸阅读

# 🔐 安全日报 | 2026年3月25日

> 黑山羊每日安全速递，洞悉网络威胁，守护数字安全

---

## ⚠️ 今日重点威胁

### 1. TeamPCP 供应链攻击升级：LiteLLM 包被植入后门

**威胁等级：严重**

TeamPCP 威胁组织再次发动大规模供应链攻击，这次目标是流行的 Python 包 **LiteLLM**。攻击者通过入侵 Trivy 漏洞扫描器的 CI/CD 流程，在 PyPI 上发布了两个恶意版本（1.82.7 和 1.82.8）。

**攻击细节：**

* **三阶段攻击载荷**：
* 1. 凭据窃取器：收集 SSH 密钥、云凭据、Kubernetes 密钥、加密货币钱包和 .env 文件
   2. Kubernetes 横向移动工具包：在每个节点部署特权 Pod
   3. 持久化后门：通过 systemd 服务 (sysmon.service) 每 50 分钟轮询 C2 服务器
* **影响范围**：LiteLLM 存在于 36% 的云环境中，影响极为广泛
* **攻击路径**：Trivy CI/CD 入侵 → LiteLLM 被污染 → 数万环境凭据泄露 → 连锁攻击

**防护建议：**

* 立即检查是否安装了 LiteLLM 1.82.7 或 1.82.8 版本
* 隔离受影响主机，检查 Kubernetes 集群中的异常 Pod
* 检查网络日志中是否存在对 `models.litellm[.]cloud` 和 `checkmarx[.]zone` 的出站流量
* 撤销并轮换所有可能暴露的凭据
> ⚠️ 该攻击组织声称已与 LAPSUS$ 勒索组织合作，后续攻击可能持续升级。

---

### 2. FAUX#ELEVATE 钓鱼攻击：假简历传播加密货币矿工

**威胁等级：高**

安全研究人员发现针对法语企业环境的钓鱼攻击活动，攻击者使用伪装成简历的 VBScript 文件传播多功能恶意工具包。

**攻击特点：**

* 使用高度混淆的 VBScript 文件（9.7MB，22 万行代码，仅 266 行为实际可执行代码）
* 通过域名加入检测，确保只感染企业设备
* 25 秒内完成完整感染链：凭据窃取 + 数据外传 + 加密货币挖矿

**技术手段：**

* 滥用合法服务：Dropbox 用于载荷托管，WordPress 站点用于 C2 配置
* 使用 ChromElevator 项目绕过 Chrome 浏览器的应用绑定加密保护
* 通过 mail[.]ru SMTP 基础设施外传凭据

**防护建议：**

* 警惕来自未知来源的简历附件，特别是 .vbs、.vbe 等脚本文件
* 加强邮件网关过滤，阻止可疑附件
* 部署端点检测响应 (EDR) 解决方案

---

## 📰 安全动态速览

### 供应链安全

| 事件 | 详情 |
| --- | --- |
| Trivy CI/CD 被入侵 | 开源漏洞扫描器 Trivy 被植入后门，影响超过 10 万 Docker Hub 下载和 32,000 GitHub 星标项目 |
| CanisterWorm 蠕虫传播 | Trivy 入侵引发的连锁攻击已导致自传播蠕虫出现 |

### 漏洞利用

| CVE | 产品 | CVSS | 状态 |
| --- | --- | --- | --- |
| CVE-2026-33017 | Langflow | 9.3 | **已遭利用** - 公开后 20 小时内即被武器化 |
| CVE-2026-20131 | Cisco FMC | 10.0 | **0-day 利用** - Interlock 勒索软件利用 |

### 移动安全

* **DarkSword iOS 漏洞利用套件**：新发现的 iOS 攻击套件，使用 6 个漏洞实现完整 iPhone 入侵，部分攻击针对乌克兰用户
* **Perseus Android 银行木马**：伪装成 IPTV 应用，主要针对土耳其和意大利用户

### 执法行动

美国司法部联合执法行动摧毁了四个大型 DDoS 僵尸网络（AISURU、Kimwolf、JackSkid、Mossad），共计超过 300 万台设备被控制。

---

## 🛡️ 安全建议

* **供应链安全**
* - 审核 CI/CD 管道中使用的所有工具
    - 实施依赖项锁定和完整性验证
    - 建立软件物料清单 (SBOM)
* **凭据管理**
* - 定期轮换敏感凭据
    - 使用密钥管理系统存储机密
    - 实施最小权限原则
* **端点防护**
* - 部署 EDR 解决方案
    - 启用应用程序白名单
    - 保持系统和软件更新

---

## 📊 CVE 关注列表

以下漏洞需要优先处理：

* **CVE-2026-33017** (Langflow) - 已有野外利用
* **CVE-2026-20131** (Cisco FMC) - 已有 0-day 利用
* LiteLLM 供应链后门（PYSEC-2026-2）

---

## 📅 历史上的今天

\*2026年3月25日\* - 供应链安全成为年度焦点，TeamPCP 攻击展示了开源生态系统的系统性风险。

---

> 🐐 **黑山羊提示**：供应链攻击正在成为威胁行为者的首选方式。从开发工具到生产环境，每一个环节都可能成为攻击入口。建立完整的安全供应链审计机制刻不容缓。

---

**来源**：The Hacker News, Endor Labs, JFrog, Securonix, Wiz

\*黑山羊安全团队出品 | 每日 18:00 发布\*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aF48TGQ87PkKpPPA6ia3VYddbMpj9yDP6Aib9kfApUmtUBlCTUnDzXOWn66UuecfNB3WVlS22dbpFAhBMEIy8Ribg/0?wx_fmt=png)

安全诸子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aF48TGQ87PkKpPPA6ia3VYddbMpj9yDP6Aib9kfApUmtUBlCTUnDzXOWn66UuecfNB3WVlS22dbpFAhBMEIy8Ribg/0?wx_fmt=png)

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