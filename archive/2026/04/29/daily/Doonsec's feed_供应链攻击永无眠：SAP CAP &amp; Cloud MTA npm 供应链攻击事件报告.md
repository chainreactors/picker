---
title: 供应链攻击永无眠：SAP CAP &amp; Cloud MTA npm 供应链攻击事件报告
url: https://mp.weixin.qq.com/s/gaeeRzgxg-E_9G6_vtfO_g
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:24:35.060587
---

# 供应链攻击永无眠：SAP CAP &amp; Cloud MTA npm 供应链攻击事件报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOqic37lj6UrPXO2KA2C3Ziadwk9VGly31ZuiaQDYicus2o3cCIx2emY0jKyichjSZcRt0ib8MTDJVnoRW82T8ibe2yY5pIXuDlYnUWMqzc/0?wx_fmt=jpeg)

# 供应链攻击永无眠：SAP CAP & Cloud MTA npm 供应链攻击事件报告

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**事件概述**

这是一起**针对 SAP CAP（Cloud Application Programming Model）和 Cloud MTA（Multi-Target Application）生态的精准 npm 供应链攻击**。攻击者通过劫持/污染 SAP 官方维护的 npm 包，在安装阶段（`preinstall` 钩子）注入恶意引导程序，最终执行一个 **11.7 MB 的高度混淆凭证窃取与自传播框架**。
影响范围集中在开发者本地环境和 CI/CD 流水线（GitHub Actions、云凭证等），属于“中小规模但高影响”攻击（Aikido 原话）。

### **事件时间线**

* • **2026年4月29日 UTC 上午–中午**：恶意版本陆续发布。
* • **同日下午**：Socket Security 率先在 X 上公开警报（用户提供的推文）。
* • **同日下午**：Aikido Security 发布博客，提供完整技术拆解、IOCs 和检测工具。
  事件仍在快速发展中，npm 官方已 unpublish 部分恶意版本（尤其是 `@cap-js/sqlite@2.2.2`）。

### **受影响包及影响范围**

| 包名称 | 恶意版本 | 每周下载量（约） | 用途 |
| --- | --- | --- | --- |
| mbt | 1.2.48 | 52,000 | SAP Cloud MTA 构建工具 |
| @cap-js/sqlite | 2.2.2 | 250,000 | CAP 本地 SQLite 集成（最常用） |
| @cap-js/postgres | 2.2.2 | 10,000 | CAP PostgreSQL 集成 |
| @cap-js/db-service | 2.10.1 | 260,000 | CAP 数据库服务核心 |

这些包是 **SAP BTP 开发者、CAP Node.js 项目、MTA 部署流水线** 的核心依赖。任何在 4 月 29 日暴露窗口内执行 `npm install` 的环境均可能感染。

### **攻击技术细节（Socket + Aikido 整合）**

* • **入口**：恶意版本在 `package.json` 中新增 `"preinstall": "node setup.mjs"` 脚本（此前这些 SAP 官方包从未使用 preinstall）。
* • **第一阶段（setup.mjs）**：Bun 运行时引导程序。

+ • 检测 OS/架构 → 从 GitHub Releases 下载 Bun v1.3.13 ZIP（未经验证 HTTP 下载）。
+ • 解压并立即执行 `execution.js`。

* • **第二阶段（execution.js）**：11.7 MB 混淆 payload（使用 `ctf-scramble-v2` 字符串混淆）。

+ • 行为特征：

- • 检测 CI 环境 → 非 CI 机器上 daemonize（后台驻留）。
- • 跳过俄罗斯 locale（可能规避特定沙箱）。
- • **凭证窃取**（极全面）：

* • GitHub token（`gh auth token`）
* • npm token（`~/.npmrc`）
* • AWS（STS、Secrets Manager、SSM）
* • Azure（订阅、Key Vault）
* • GCP（项目身份、Secret Manager）
* • Kubernetes service account token
* • 本地工具配置（Claude AI、MCP、Signal、Electrum、VPN 等）
* • GitHub Actions runner 上通过嵌入式 Python 内存 dump 提取 secrets

+ • **数据外传**：使用 AES-256-GCM + RSA 加密，通过 **GitHub 死投（commit messages / public repos）** 外传（伪装成 “chore: update dependencies” 提交，作者显示为 `claude@users.noreply.github.com`）。
+ • **自传播**：修改 package tarballs、注入 GitHub workflows，关键词 “OhNoWhatsGoingOnWithGitHub” 和 “A Mini Shai-Hulud has Appeared”。

**关键 IOCs（Aikido 提供）**：

* • 文件：`setup.mjs`（SHA256: `4066781fa830224c8bbcc3aa005a396657f9c8f9016f9a64ad44a9d7f5f45e34`）
* • 文件：`execution.js`（SHA256: `6f933d00b7d05678eb43c90963a80b8947c4ae6830182f89df31da9f568fea95`）
* • 字符串：`A Mini Shai-Hulud has Appeared`、`OhNoWhatsGoingOnWithGitHub`、`ctf-scramble-v2`、`tmp.987654321.lock`
* • GitHub 搜索关键词：`OhNoWhatsGoingOnWithGitHub`（commits）或仓库描述含 “A Mini Shai-Hulud has Appeared”
* • Bun 下载域名：`github.com/oven-sh/bun/releases/download/bun-v1.3.13/`

### **威胁归因及与 Shai-Hulud 的关联**

Aikido 将其明确归类为 **Mini Shai-Hulud**，与 2025 年 Shai-Hulud V1（chalk/debug 等 18 个包）和 V2（自传播蠕虫）手法高度一致（install-time 执行 + 凭证窃取 + GitHub 传播）。本次规模更小（仅 4 个包），但 payload 更成熟、专业化，针对企业开发者/CI 环境优化。暂无公开威胁演员归因，但手法与此前 Axios、TeamPCP 等北韩相关活动有相似性。

### **立即缓解与检测建议（优先级最高****）**

1. 1. **审计**：

* • `npm ls mbt @cap-js/sqlite @cap-js/postgres @cap-js/db-service`
* • 搜索项目中 `setup.mjs`、`execution.js`、`preinstall` 脚本

2. 2. **清理**：

* • 删除 `node_modules` + lockfile → `npm ci --ignore-scripts` 或切换 pnpm
* • 检查 4月29日构建日志（Bun 下载、PowerShell 执行）

3. 3. **响应**：

* • **立即轮换**所有 GitHub、npm、云凭证、Kubernetes token
* • GitHub 搜索上述关键词，检查可疑 commits / repos

4. **长期防护**：

* • 使用 Aikido Safe Chain / Socket.dev / StepSecurity 等 SCA 工具
* • CI 中强制 `--ignore-scripts`
* • 监控 SAP Security Patch Day + npm unpublish 公告

**Aikido 评估**：虽然包数量少，但因目标是 SAP 开发者/CI 环境，“潜在影响极高”。

此事件再次证明 npm 供应链攻击已成为常态，尤其针对企业框架如 SAP CAP。Socket 负责快速警报，Aikido 提供了目前最完整的 payload 逆向和 IOC 列表。

### **参考链接**

[1].https://www.aikido.dev/blog/mini-shai-hulud-has-appeared
[2].https://x.com/SocketSecurity/status/2049479949644374507

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq9yWObL9W5ibgeHZBd0e5Y1Ex1c5ULAWdhLUaHOsdMavA730h9c4R00iaLXlo9ibNaJia74PbibsRJ9u4CyoVeqCRVYqEicCL5BKicM0Q/640?wx_fmt=gif&from=appmsg)

点击阅读原文至**ALPHA 9.3**

即刻助力威胁研判

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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