---
title: 高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密
url: https://www.anquanke.com/post/id/313468
source: 安全客-有思想的安全新媒体
date: 2025-11-28
fetch_date: 2025-11-29T03:11:22.075618
---

# 高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密

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

# 高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密

阅读量**21381**

发布时间 : 2025-11-28 18:04:22

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/shai-hulud-v2-exploits-github-actions-workflows/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

软件供应链正遭受“**沙虫蠕虫 v2（Shai Hulud v2）**”的猛烈攻击，这一复杂恶意软件活动已攻陷 npm 和 Maven 生态系统中的 **834 个包**。

新一轮攻击专门针对 **GitHub Actions 工作流**，利用 `pull_request_target` 触发器向广泛使用的库注入恶意代码。攻击已影响 PostHog、Zapier 和 AsyncAPI 等主要项目，通过劫持自动化令牌系统性感染下游依赖。

感染过程依赖名为 `setupbun.js` 的预安装脚本启动的 **双阶段加载器**：该脚本安装 Bun 运行时以执行混淆 payload `bunenvironment.js` ，同时抑制标准输出以避免在构建日志中被检测。

通过攻陷的 CI 流水线，恶意软件获取仓库密钥的 **特权访问权限**，能够修改源代码、递增补丁版本并将受感染包重新发布到公共 registry。

Socket.dev 安全分析师发现了该恶意软件独特的持久化机制：使用特征短语“**Sha1-Hulud The Second Coming**”搜索 GitHub 以重新触发感染。这确保即使个别仓库被清理，攻击者仍能定位并重新攻陷易受攻击的端点。

### 攻击影响范围

此次活动影响广泛，暴露了数万个仓库的敏感凭据，标志着自动化供应链攻击的危险演进。

一旦侵入 CI 环境，恶意软件会执行全面的凭据窃取例程：

1. 捕获所有环境变量，重点目标包括 `GITHUB_TOKEN`、`NPM_TOKEN` 和 `AWS_ACCESS_KEY_ID`
2. 部署 TruffleHog 二进制文件扫描本地文件系统中的嵌入式密钥
3. 枚举云基础设施，遍历 AWS、Google Cloud 和 Azure 的所有区域以提取托管密钥库中的机密

![]()

所有窃取数据均通过 **三层 Base64 编码** 混淆，随后泄露至受害者账户内随机生成的 GitHub 仓库。

此外，恶意软件会在 Linux 运行器上尝试权限提升：通过操纵 `sudoers` 文件或执行 `Docker run --privileged` 命令获取 root 权限。若未找到有效凭据传播蠕虫，则执行 **破坏性擦除函数** 删除文件。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/shai-hulud-v2-exploits-github-actions-workflows/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313468](/post/id/313468)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/shai-hulud-v2-exploits-github-actions-workflows/)

如若转载,请注明出处： <https://cybersecuritynews.com/shai-hulud-v2-exploits-github-actions-workflows/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **750**

* 粉丝
* **6**

### TA的文章

* ##### [大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件](/post/id/313473)

  2025-11-28 18:08:08
* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
* ##### [Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击](/post/id/313482)

  2025-11-28 18:07:08
* ##### [Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃](/post/id/313486)

  2025-11-28 18:05:53
* ##### [高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密](/post/id/313468)

  2025-11-28 18:04:22

### 相关文章

* ##### [大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件](/post/id/313473)

  2025-11-28 18:08:08
* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
* ##### [Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击](/post/id/313482)

  2025-11-28 18:07:08
* ##### [Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃](/post/id/313486)

  2025-11-28 18:05:53
* ##### [逾390个被弃用的iCalendar同步域名存在安全隐患，可能导致近400万台设备暴露于安全风险之下](/post/id/313462)

  2025-11-28 18:02:37
* ##### [纳闽再保险启用绿色数据中心，实现效能提升与运营成本优化](/post/id/313459)

  2025-11-28 18:00:45
* ##### [遗留Python包中的代码漏洞，可通过劫持其依赖域名进而危及整个PyPI软件生态](/post/id/313453)

  2025-11-28 18:00:14

### 热门推荐

文章目录

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