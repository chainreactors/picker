---
title: Apache Airflow漏洞导致敏感工作流数据面临潜在攻击风险
url: https://www.anquanke.com/post/id/314423
source: 安全客-有思想的安全新媒体
date: 2026-01-21
fetch_date: 2026-01-22T03:34:43.884325
---

# Apache Airflow漏洞导致敏感工作流数据面临潜在攻击风险

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

# Apache Airflow漏洞导致敏感工作流数据面临潜在攻击风险

阅读量**18181**

发布时间 : 2026-01-21 18:07:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Divya，文章来源：gbhackers

原文地址：<https://gbhackers.com/apache-airflow-flaws-expose-sensitive-workflow-data/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Apache Airflow 已修复其 3.1.6 版本之前存在的**两个独立的凭证泄露漏洞**。

这些漏洞可能允许攻击者通过日志文件和 Web 界面，提取嵌入在代理配置和模板化工作流字段中的**敏感认证数据**，进而可能危及网络基础设施和敏感数据管道的安全。

第一个漏洞影响 Apache Airflow 3.1.6 之前的版本，根源在于 Connection 对象中对代理 URL 的处理不当。

| 维度 | CVE-2025-68675 | CVE-2025-68438 |
| --- | --- | --- |
| 受影响版本 | Apache Airflow < 3.1.6 | Apache Airflow 3.1.0–3.1.6 |
| 严重程度 | 低 | 低 |
| 泄露数据 | 代理凭证 | API 密钥、令牌、机密信息 |
| 涉及组件 | 连接代理字段 | 渲染模板 UI |
| 修复版本 | 3.1.6 | 3.1.6 |

代理配置通常以 `http://username:password@proxy.example.com:8080` 的形式包含嵌入式认证凭证。

这些字段未被标记为敏感信息，这意味着每当连接被渲染或显示时，代理凭证都会以明文形式记录在日志中。

在 Airflow 的日志架构中，当用户查看连接详情、排查数据管道问题或访问审计日志时，任何拥有日志访问权限的人都能看到这些代理凭证。

这在多团队共享 Airflow 实例的环境中尤其危险 —— 攻击者或心怀不满的内部人员可能提取这些凭证，用于拦截网络流量或通过代理基础设施横向移动。

第二个漏洞影响 Airflow 3.1.0 至 3.1.6 版本，涉及渲染模板 UI 中机密信息的**屏蔽机制不当**。

然而，序列化过程中使用的机密信息屏蔽实例未识别用户注册的 `mask_secret()` 模式，导致敏感值在被截断前未被屏蔽而直接暴露。

该漏洞使拥有 Web 界面访问权限的攻击者，能够在渲染模板中查看 API 密钥、数据库凭证和令牌等敏感数据。

由于截断操作发生在序列化之后而非之前，屏蔽层失效，机密信息会完整暴露（除非恰好落在被截断的部分）。

这两个漏洞均要求攻击者**要么直接访问日志文件，要么获得 Airflow Web 界面的认证权限**，这也降低了它们的严重程度评级。

但在云环境中，日志通常会被集中汇总并允许跨团队访问，且 Web 界面的访问权限可能被广泛授予。

Apache 已在 3.1.6 版本中修复了这两个问题。企业应**优先立即升级**，因为这些漏洞会直接危及认证机密的安全。

此外，管理员应审查日志保留策略，并在集中式日志系统中实施机密信息编辑规则，以防止凭证意外泄露。

如需临时缓解风险，企业可限制 Airflow 日志和 Web 界面的访问权限、实施 IP 白名单，并轮换可能已泄露的所有凭证。

安全团队应审计近期日志，排查可疑的认证尝试或未授权的代理访问行为。

这两个漏洞由 lwlkr 和威廉・阿什发现，分别由安基特・乔拉西亚和阿莫格・德赛开发了修复方案。

依赖 Airflow 进行数据管道编排的用户，应将此次升级视为保护工作流基础设施和下游系统安全的**关键任务**。

本文翻译自gbhackers [原文链接](https://gbhackers.com/apache-airflow-flaws-expose-sensitive-workflow-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314423](/post/id/314423)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/apache-airflow-flaws-expose-sensitive-workflow-data/)

如若转载,请注明出处： <https://gbhackers.com/apache-airflow-flaws-expose-sensitive-workflow-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **940**

* 粉丝
* **6**

### TA的文章

* ##### [珠穆朗玛峰勒索软件团伙据称宣称入侵了麦当劳印度系统](/post/id/314403)

  2026-01-21 18:10:24
* ##### [Google Gemini漏洞可被攻击者利用获取私人日历数据](/post/id/314409)

  2026-01-21 18:09:50
* ##### [新型鱼叉式钓鱼攻击借阿根廷联邦法院裁决掩护，植入远程访问木马（RAT）](/post/id/314414)

  2026-01-21 18:09:24
* ##### [密码学基础被攻破：GNU libtasn1中存在一字节溢出漏洞（CVE-2025-13151）](/post/id/314411)

  2026-01-21 18:08:43
* ##### [Apache Airflow漏洞导致敏感工作流数据面临潜在攻击风险](/post/id/314423)

  2026-01-21 18:07:57

### 相关文章

* ##### [珠穆朗玛峰勒索软件团伙据称宣称入侵了麦当劳印度系统](/post/id/314403)

  2026-01-21 18:10:24
* ##### [Google Gemini漏洞可被攻击者利用获取私人日历数据](/post/id/314409)

  2026-01-21 18:09:50
* ##### [新型鱼叉式钓鱼攻击借阿根廷联邦法院裁决掩护，植入远程访问木马（RAT）](/post/id/314414)

  2026-01-21 18:09:24
* ##### [密码学基础被攻破：GNU libtasn1中存在一字节溢出漏洞（CVE-2025-13151）](/post/id/314411)

  2026-01-21 18:08:43
* ##### [亚马逊 100 亿美元押注 OpenAI，旨在推动AI驱动零售的变革](/post/id/314435)

  2026-01-21 18:07:21
* ##### [德以两国承诺共建网络安全联盟](/post/id/314401)

  2026-01-21 18:06:40
* ##### [X开源Grok驱动的算法代码，揭秘内容传播机制](/post/id/314428)

  2026-01-21 18:06:03

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