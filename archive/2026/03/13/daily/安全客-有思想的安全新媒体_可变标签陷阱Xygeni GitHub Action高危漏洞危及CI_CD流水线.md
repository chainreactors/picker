---
title: 可变标签陷阱Xygeni GitHub Action高危漏洞危及CI/CD流水线
url: https://www.anquanke.com/post/id/315171
source: 安全客-有思想的安全新媒体
date: 2026-03-13
fetch_date: 2026-03-14T04:03:16.128262
---

# 可变标签陷阱Xygeni GitHub Action高危漏洞危及CI/CD流水线

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

# 可变标签陷阱Xygeni GitHub Action高危漏洞危及CI/CD流水线

阅读量**23818**

发布时间 : 2026-03-13 10:31:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/the-mutable-tag-trap-critical-9-4-cvss-attack-on-xygeni-github-action-exposes-ci-cd-pipelines/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Xygeni 官方的 **xygeni-action** GitHub Action 遭遇了一起**精密的供应链投毒攻击**。

2026 年 3 月 3 日，攻击者利用被盗凭证绕过标准分支保护机制，将**命令与控制（C2）后门**注入到开发者普遍信任的版本标签中。

该漏洞编号为 **CVE-2026-31976**，**CVSS 评分高达 9.4**，对 CI/CD 流水线构成**极度危险**。

攻击流程如下：

攻击者先创建多个包含**混淆 Shell 代码**但未合并的 Pull Request。尽管分支保护规则已阻止这些 PR 合入主干，但攻击者利用泄露的 GitHub App 凭证实施了**标签投毒（tag poisoning）**。

报告揭露了这一技术漏洞：

攻击者将**可变的 v5 标签指向了某个未合并 PR 中的恶意提交**。

由于该提交仍保留在 Git 对象库中，**任何引用 @v5 的工作流都会拉取并执行恶意代码**，即便它从未被正式合并。

这段恶意代码伪装成无害的 “扫描器版本遥测” 步骤，旨在 CI 运行环境中实现**高度隐蔽与持久化**。触发后，后门按三步执行：

1. **注册上线**：CI 执行机向 C2 服务器注册，上报主机名、用户名与系统版本。
2. **指令执行**：在 180 秒内持续轮训服务器，**通过 eval 接收并执行任意系统命令**。
3. **数据回传**：指令执行结果经压缩、Base64 编码后回传给攻击者。

为进一步规避检测，该恶意程序使用**随机轮询间隔**、关闭 TLS 证书校验并屏蔽所有错误输出。

此次漏洞暴露窗口约 6 天，从 2026 年 3 月 3 日至 3 月 10 日。

尽管潜在危害极大，但实际影响范围相对可控。报告指出：**v5 标签主要被 Xygeni 自有及关联仓库使用**，目前未发现外部公共仓库受影响。

Xygeni 已删除被投毒的 v5 标签，仍引用该标签的工作流会直接报错 “reference not found”。

为恢复安全，管理员必须立即采取以下措施：

* **固定到安全提交**：将工作流更新为指向 v6.4.0 的校验通过提交哈希：

  `xygeni/xygeni-action@13c6ed2797df7d85749864e2cbcf09c893f43b23`
* **密钥轮换**：**轮换所有 CI 执行机可访问的密钥**，包括云令牌、部署密钥、仓库密钥等。
* **审计排查**：检查 CI 日志中是否存在对恶意 IP `91.214.78.178`的连接，并核查近期构建产物是否被篡改。

如需完全避开受影响的 GitHub Action，Xygeni 建议直接使用**CLI 安装方式**，该方式不受本次事件影响。

本文翻译自securityonline [原文链接](https://securityonline.info/the-mutable-tag-trap-critical-9-4-cvss-attack-on-xygeni-github-action-exposes-ci-cd-pipelines/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315171](/post/id/315171)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/the-mutable-tag-trap-critical-9-4-cvss-attack-on-xygeni-github-action-exposes-ci-cd-pipelines/)

如若转载,请注明出处： <https://securityonline.info/the-mutable-tag-trap-critical-9-4-cvss-attack-on-xygeni-github-action-exposes-ci-cd-pipelines/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1090**

* 粉丝
* **6**

### TA的文章

* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现](/post/id/315152)

  2026-03-13 10:33:36
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13

### 相关文章

* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现](/post/id/315152)

  2026-03-13 10:33:36
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13
* ##### [Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据](/post/id/315158)

  2026-03-13 10:32:51
* ##### [Armadin获1.9亿美元融资 用AI实现自动化红队攻防](/post/id/315161)

  2026-03-13 10:32:28

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