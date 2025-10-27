---
title: L7 DDoS僵尸网络劫持576万台设备发起大规模攻击
url: https://www.anquanke.com/post/id/312075
source: 安全客-有思想的安全新媒体
date: 2025-09-13
fetch_date: 2025-10-02T20:04:21.980968
---

# L7 DDoS僵尸网络劫持576万台设备发起大规模攻击

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

# L7 DDoS僵尸网络劫持576万台设备发起大规模攻击

阅读量**78365**

发布时间 : 2025-09-12 17:36:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/l7-ddos-botnet-hijacked-5-76m-devices/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

2025年3月初，安全团队首次观测到一个前所未有的L7 DDoS僵尸网络，针对多行业Web应用发起攻击。

该僵尸网络从初始133万台受感染设备迅速扩张，通过**HTTP GET泛洪**耗尽服务器资源并绕过传统速率限制。

到5月中旬，威胁进一步升级，僵尸网络规模增长至**460万个节点**，利用受感染物联网（IoT）设备和防护薄弱的端点扩大攻击面。

至9月，这个庞大网络已调动**576万个IP地址**协同攻击某政府机构，每秒生成数千万次请求。

Qrator Labs分析师指出，恶意流量的地理分布发生显著变化，**巴西、越南和美国**成为主要来源地。

攻击分两波展开：首轮约280万台设备参与，一小时后新增300万台节点加入。第二波攻击的HTTP头包含**随机化User-Agent字符串**，旨在规避简单流量过滤。

Qrator Labs研究人员发现，僵尸网络的控制机制出现关键改进，使其能够快速扩张。恶意软件通过加密通道与**去中心化命令控制（C2）基础设施**通信，攻击者频繁轮换C2节点以避免被拉黑。由于每个C2端点仅活跃数小时，基于特征的防御手段难以有效应对。

### **感染机制与持久化**

核心感染向量依赖**暴力破解默认凭证**和常见IoT固件中的**未修补漏洞**。

设备被入侵后，恶意软件部署轻量级rootkit，挂钩网络接口并拦截固件更新程序。

Qrator Labs提取的代码片段揭示了其持久化策略：

```
// Intercept firmware update calls
int hook_update(char *path) {
    if (!strcmp(path, "/usr/bin/fw_update")) {
        launch_payload();
        return 0;
    }
    return orig_update(path);
}
```

这种手段确保恶意模块在每次系统重启后重新加载，使基于简单重启的修复措施失效。

隐蔽的rootkit还会**隐藏可疑进程列表**，进一步增加检测与清除难度。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/l7-ddos-botnet-hijacked-5-76m-devices/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312075](/post/id/312075)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/l7-ddos-botnet-hijacked-5-76m-devices/)

如若转载,请注明出处： <https://cybersecuritynews.com/l7-ddos-botnet-hijacked-5-76m-devices/>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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