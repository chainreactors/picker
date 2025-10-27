---
title: Jenkins Docker 镜像漏洞可致网络路径被攻击者渗透
url: https://www.anquanke.com/post/id/306506
source: 安全客-有思想的安全新媒体
date: 2025-04-15
fetch_date: 2025-10-06T22:05:11.064128
---

# Jenkins Docker 镜像漏洞可致网络路径被攻击者渗透

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

# Jenkins Docker 镜像漏洞可致网络路径被攻击者渗透

阅读量**53642**

发布时间 : 2025-04-14 15:09:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/jenkins-docker-images-vulnerability-let-attackers-insert-themselves/>

译文仅供参考，具体内容表达以及含义原文为准。

在广泛使用的 Jenkins Docker 镜像中发现了一个严重的安全漏洞，这有可能危及数千家组织的构建管道。

2025 年 4 月 10 日发布的 Jenkins 安全公告披露了这一漏洞，它影响了某些 Docker 镜像中的 SSH 主机密钥处理功能，攻击者可能会利用该漏洞对 Jenkins 构建环境发动中间人攻击。

该问题被追踪为 CVE-2025-32754 和 CVE-2025-32755，影响 jenkins/ssh-agent Docker 镜像（版本为 6.11.1 及以下）以及已弃用的 jenkins/ssh-slave 镜像的所有版本。

#### ****Jenkins********Docker 镜像漏洞****

该漏洞源于 SSH 主机密钥是在映像创建期间生成的，而不是基于 Debian 的映像的容器启动。

公告警告称：“因此，所有基于相同版本镜像的容器都使用相同的 SSH 主机密钥。”

这从根本上破坏了 SSH 的安全模型，而在 SSH 安全模型中，主机密钥本应用于唯一标识服务器并建立信任关系。

Jenkins 项目感谢安全研究人员 Abhishek Reddypalle 发现并报告了这一漏洞。

漏洞摘要如下：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ****CVE 编号**** | ****受影响产品**** | ****影响**** | ****利用前提条件**** | ****CVSS 3.1 评分**** |
| CVE-2025-32754 | Jenkins ssh-agent Docker 镜像（基于 Debian，版本≤ 6.11.1） | 中间人攻击、未经授权的访问、凭据窃取、构建操纵 | SSH 客户端（Jenkins控制器）与 SSH 构建代理之间的网络路径被拦截 | 9.1（严重） |
| CVE-2025-32755 | Jenkins ssh-slave Docker 镜像（基于 Debian，所有版本） | 中间人攻击、未经授权的访问、数据操纵 | SSH 客户端（Jenkins控制器）与 SSH 构建代理之间的网络路径被拦截 | 9.1（严重） |

#### ****受影响的镜像****

该漏洞具体影响以下镜像变体：

****jenkins/ssh-agent：****

1.所有未明确指定操作系统的标签，包括所有带有 -jdk\* 和 -jdk\*-preview 后缀的标签（2025 年 4 月 10 日前的版本）。

2.所有包含 debian、stretch、bullseye 或 bookworm 的镜像（2025 年 4 月 10 日前的版本）。

****jenkins/ssh-slave（已弃用）：****

1.latest、jdk11、latest-jdk11、revert-22-jdk11-JENKINS-52279 标签的镜像。

2.基于 Alpine、Windows 和 Nanoserver 的变体不受此漏洞影响。

#### ****攻击途径及影响****

该漏洞使得能够拦截 Jenkins 控制器与 SSH 构建代理之间网络流量的攻击者，能够在不触发 SSH 真实性警告的情况下冒充合法代理。

这种攻击途径可能会导致严重后果，包括：

1.拦截或修改构建工件

2.收集构建过程中使用的凭据或机密信息

3.向构建管道中注入恶意代码

在持续集成 / 持续交付（CI/CD）环境中，此类攻击尤其令人担忧，因为受影响的构建过程可能会引发供应链攻击，进而影响下游系统和客户。

Jenkins 项目已发布了 6.11.2 版本的更新后的 jenkins/ssh-agent 镜像，其中引入了一项关键的安全改进：

“基于 Debian 的 jenkins/ssh-agent 6.11.2 Docker 镜像会删除在镜像创建过程中自动生成的 SSH 主机密钥。新的主机密钥将在容器首次启动时生成。”

管理员可以通过检查 Docker 镜像来验证是否运行的是已打补丁的版本。已打补丁的镜像行为会为每个容器实例生成唯一的 SSH 主机密钥，而不是在所有部署中重复使用相同的密钥。

各组织应立即将其 Docker 镜像更新到此版本。已弃用的 jenkins/ssh-slave 镜像将不会收到更新，用户应迁移到 jenkins/ssh-agent 镜像。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/jenkins-docker-images-vulnerability-let-attackers-insert-themselves/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306506](/post/id/306506)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/jenkins-docker-images-vulnerability-let-attackers-insert-themselves/)

如若转载,请注明出处： <https://cybersecuritynews.com/jenkins-docker-images-vulnerability-let-attackers-insert-themselves/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**6赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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