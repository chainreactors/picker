---
title: 新型恶意软件家族正劫持暴露的Docker API
url: https://www.anquanke.com/post/id/312005
source: 安全客-有思想的安全新媒体
date: 2025-09-11
fetch_date: 2025-10-02T19:57:01.998272
---

# 新型恶意软件家族正劫持暴露的Docker API

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

# 新型恶意软件家族正劫持暴露的Docker API

阅读量**125863**

发布时间 : 2025-09-10 17:14:02

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/beyond-cryptominers-a-new-malware-strain-is-hijacking-exposed-docker-apis/>

译文仅供参考，具体内容表达以及含义原文为准。

Akamai Hunt安全团队发现了一种针对暴露Docker API的新型恶意软件。与早期专注于加密挖矿的版本不同，该变体扩展了感染能力，包括持久化机制、端口阻塞，甚至可能为构建分布式僵尸网络奠定基础。

2025年6月，趋势科技首次报告了一个利用配置不当Docker API部署Tor隐藏加密挖矿程序的恶意软件家族。当时攻击者通过Base64编码负载在新容器中执行代码，修改SSH配置实现持久化，并安装masscan和torsocks等工具后启动XMRig挖矿程序。

但到2025年8月，Akamai研究人员观察到一个策略转变的新变体：“二进制文件完全不同；Akamai Hunt发现的变体不再投放加密挖矿程序，而是释放包含其他工具的文件，其感染能力远超原始版本。”

### **攻击链与核心技术**

新型恶意软件通过HTTP请求调用Docker API，基于Alpine镜像启动容器。在容器内，Base64解码的脚本会准备环境、安装Tor，并从Tor隐藏服务拉取`docker-init.sh` 脚本。

Akamai指出：“该脚本分两阶段执行：第一阶段安装curl和Tor；第二阶段从Tor域名获取`docker-init.sh` 。”

脚本通过修改`/root/.ssh/authorized_keys`植入攻击者公钥，利用cron任务实现持久化，并安装扫描工具。最关键的是，它会**阻塞主机的2375端口（Docker API默认端口）**，阻止其他攻击者接入——从而“独占”受感染系统。

### **横向传播与潜在威胁**

下载的Go语言二进制文件（命名为`dockerd`）会释放额外工具，并运行masscan扫描其他暴露Docker API的实例。一旦发现目标，便重复感染流程，实现跨主机传播。

值得注意的是，该二进制文件还包含**Telnet（23端口）和Chromium远程调试（9222端口）的休眠模块**。尽管这些功能尚未激活，但暗示了未来扩展方向。Hunt团队警告：“部分底层机制表明，该变体可能是复杂僵尸网络的初始版本，但目前尚未发现完整形态。”

1. **Telnet模块**：使用默认路由器凭证登录，将成功登录信息发送至远程Webhook。若登录用户为root，恶意软件会判定为蜜罐——这是一种巧妙的反监控措施。
2. **Chromium模块**：利用`chromedp`库连接暴露的调试端口。尽管尚未观察到高级利用行为，但该技术可扩展为窃取Cookie、劫持会话或泄露浏览器敏感数据。

### **检测与防御建议**

Akamai Hunt团队提出多项检测策略：

1. 监控**启动后立即执行apt/yum安装并通过curl/wget拉取脚本的容器**
2. 警惕**2375、23、9222端口的新连接**及masscan扫描活动
3. 追踪Docker容器内执行的**Base64编码命令**
4. 检查**异常crontab修改**或`/root/.ssh/authorized_keys`新增SSH密钥

防御方面，报告建议实施**严格网络分段**、限制Docker API暴露范围、将Chrome调试端口绑定至可信IP，并对所有设备强制执行强密码轮换。

本文翻译自securityonline [原文链接](https://securityonline.info/beyond-cryptominers-a-new-malware-strain-is-hijacking-exposed-docker-apis/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312005](/post/id/312005)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/beyond-cryptominers-a-new-malware-strain-is-hijacking-exposed-docker-apis/)

如若转载,请注明出处： <https://securityonline.info/beyond-cryptominers-a-new-malware-strain-is-hijacking-exposed-docker-apis/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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