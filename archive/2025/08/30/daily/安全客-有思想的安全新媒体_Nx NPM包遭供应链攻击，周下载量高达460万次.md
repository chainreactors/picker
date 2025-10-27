---
title: Nx NPM包遭供应链攻击，周下载量高达460万次
url: https://www.anquanke.com/post/id/311717
source: 安全客-有思想的安全新媒体
date: 2025-08-30
fetch_date: 2025-10-07T00:17:54.855690
---

# Nx NPM包遭供应链攻击，周下载量高达460万次

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Nx NPM包遭供应链攻击，周下载量高达460万次

阅读量**92531**

发布时间 : 2025-08-29 16:06:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Mann，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/supply-chain-attack-hits-nx-npm-package-with-4-6m-weekly-downloads/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

研究人员披露，一起复杂的供应链攻击入侵了 **Nx NPM 包**——一款由 AI 驱动的单体仓库（monorepo）构建系统，每周下载量超过 **460 万次**。此次事件导致大量开发者的敏感凭证泄露至公开可访问的 GitHub 仓库。

## 事件经过

此次入侵通过 **恶意更新**实现，攻击者在 Nx 包中植入了利用 AI CLI 工具和 **post-install 脚本** 的恶意代码，用于收集凭证并外传数据。

事件由 Wiz 安全研究团队披露，他们指出：

**·** 恶意版本于 **2025 年 8 月 26 日** 被上传至 npm registry，涉及 Nx 主包及多个子模块。

**·** 在这些版本中，一个名为 **telemetry.js** 的文件被注入 Linux/macOS 定向的恶意负载，并通过 npm 的 **post-install** 脚本触发。

**·** 一旦执行，恶意代码会搜索并窃取敏感资产，包括加密货币钱包、.env 文件、SSH 私钥、GitHub 认证令牌以及 npm token。

Nx 由 **Nrwl** 开发，是一款智能构建平台，广泛应用于 Angular、React、Node.js 等前后端框架的单体仓库管理。由于其已深度集成至 **VSCode 插件、create-nx-workspace 脚手架以及 CI/CD 工具链**，此次攻击波及范围极为广泛。

## 攻击手法

恶意代码通过利用已安装的 AI CLI 工具（包括 **Anthropic Claude、Google Gemini、Q**）进行外传。攻击者滥用这些工具的不安全参数（如 `--dangerously-skip-permissions` 和 `--trust-all-tools`），从受害系统提取文件数据。

提取的数据经过多重 **Base64 编码** 后，被上传至攻击者在受害者 GitHub 账户下新建的仓库中。仓库名称遵循固定模式：

* `s1ngularity-repository`
* `s1ngularity-repository-0`
* `s1ngularity-repository-1`

GitHub 于 **8 月 27 日 9:00 UTC** 介入并禁用了已知恶意仓库，但攻击发生的 **8 小时窗口**可能已足够攻击者甚至其他第三方克隆数据。

根据 Wiz 报告：

**·** 存在数千个相关仓库

**·** 泄露数据包括 **1000+ 有效 GitHub token**、数十个云与 npm 凭证、约 **2 万个文件**

**·** 恶意代码不仅在开发者本地执行，还可能在 **GitHub Actions 等 CI 流水线**中触发

## 受影响版本

* **nx**：20.9.0 ~ 20.12.0，21.5.0 ~ 21.8.0
* **@nx/devkit**：20.9.0，21.5.0
* **@nx/enterprise-cloud**：3.2.0
* **@nx/eslint, @nx/js, @nx/key, @nx/node, @nx/workspace**：20.9.0 与 21.5.0

## 攻击痕迹

研究人员还发现了如下关联伪迹：

* 修改 Shell 配置文件（~~/.bashrc、~~/.zshrc），加入 `sudo shutdown -h 0`，阻止用户调试感染
* 在 `/tmp` 目录中生成临时文件（如 `inventory.txt`, `.bak`），列出敏感路径
* 调用 GitHub API 上传数据，相关文件命名为 `results.b64`

Step Security 验证了该恶意行为，指出关机命令的目的是封锁用户排查；Wiz 也确认攻击中存在对 AI 工具的侦察性滥用。

## 应对建议

受影响用户应立即采取以下措施：

* **移除恶意版本**：执行 `rm -rf node_modules && npm cache clean --force`，并从 npm 重新安装干净版本；
* **清理系统残留**：手动检查并删除 ~~/.bashrc、~~/.zshrc 中的恶意命令及 /tmp 下的临时文件；
* **审计 GitHub 账户**：排查是否存在以 “s1ngularity” 命名的仓库，检查审计日志中的可疑 API 调用；
* **撤销与重置凭证**：包括 GitHub token、npm token、SSH key、云凭证与环境变量；
* **加密货币防护**：如钱包私钥被泄露，应立即转移资金；
* 使用 Wiz 发布的 **YARA 规则与 IoC** 检测潜在入侵迹象。

此次事件再次提醒，**供应链攻击正在快速演化，甚至利用 AI 工具进行渗透与外传**。开发者和企业必须建立严格的软件供应链安全策略，避免成为下一个受害者。

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/supply-chain-attack-hits-nx-npm-package-with-4-6m-weekly-downloads/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311717](/post/id/311717)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/supply-chain-attack-hits-nx-npm-package-with-4-6m-weekly-downloads/)

如若转载,请注明出处： <https://cyberinsider.com/supply-chain-attack-hits-nx-npm-package-with-4-6m-weekly-downloads/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [事件经过](#h2-0)
* [攻击手法](#h2-1)
* [受影响版本](#h2-2)
* [攻击痕迹](#h2-3)
* [应对建议](#h2-4)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)