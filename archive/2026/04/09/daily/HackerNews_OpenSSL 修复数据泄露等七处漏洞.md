---
title: OpenSSL 修复数据泄露等七处漏洞
url: https://hackernews.cc/archives/64065
source: HackerNews
date: 2026-04-09
fetch_date: 2026-04-10T04:45:19.122810
---

# OpenSSL 修复数据泄露等七处漏洞

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用-犯罪](https://hackernews.cc/wp-content/uploads/2025/08/criminal-8444883_640-1.jpg)

# OpenSSL 修复数据泄露等七处漏洞

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-04-09](https://hackernews.cc/archives/64065 "12:16")
分类: [漏洞](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E)
[暂无评论](https://hackernews.cc/archives/64065#respond)

* 浏览次数 194
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

最新OpenSSL更新修复了七处漏洞，其中包括一个可导致敏感数据泄露的缺陷。

该数据泄露问题编号CVE-2026-31790，评级为”中等严重性”，影响使用RSASVE密钥封装建立秘密加密密钥的应用程序。问题在于OpenSSL有时未能正确验证加密是否成功，但仍可能返回”成功”消息，将未初始化内存缓冲区的数据暴露给攻击者。

“未初始化缓冲区可能包含应用程序进程先前执行的敏感数据，导致敏感数据泄露给攻击者，”OpenSSL开发者在公告中解释。

该安全漏洞影响3.6、3.5、3.4、3.3和3.0版本，OpenSSL 1.0.2和1.1.1不受影响。

其余漏洞均被评为”低严重性”，多数可被利用导致应用程序崩溃和拒绝服务（DoS）条件。其中两处缺陷理论上可能导致任意代码执行，但一处影响不常见的OpenSSL配置，另一处涉及发送特制的1GB X.509证书。

OpenSSL开发者1月发布的更新修复了12处漏洞，包括一个可被利用实现远程代码执行的高严重性缺陷。目前OpenSSL的高严重性漏洞已较为罕见，2025年仅发现一处。

---

**消息来源：[securityweek.com](https://www.securityweek.com/data-leakage-vulnerability-patched-in-openssl/)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[OpenSSL](https://hackernews.cc/archives/tag/openssl)[漏洞](https://hackernews.cc/archives/tag/%E6%BC%8F%E6%B4%9E)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用 代码](https://hackernews.cc/wp-content/uploads/2026/01/可用-代码-210x140.jpg)](https://hackernews.cc/archives/64066 "Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光")

##### [Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光](https://hackernews.cc/archives/64066 "Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-09

[![可用-AI安全](https://hackernews.cc/wp-content/uploads/2026/02/techmanic-digital-art-8420361_1920-210x140.jpg)](https://hackernews.cc/archives/64062 "Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞")

##### [Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞](https://hackernews.cc/archives/64062 "Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-09

[![可用-wordpress-581849_1280](https://hackernews.cc/wp-content/uploads/2025/02/可用-wordpress-581849_1280-210x140.jpg)](https://hackernews.cc/archives/64053 "黑客利用 Ninja Forms WordPress 插件关键漏洞")

##### [黑客利用 Ninja Forms WordPress 插件关键漏洞](https://hackernews.cc/archives/64053 "黑客利用 Ninja Forms WordPress 插件关键漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-08

[![可用-游戏](https://hackernews.cc/wp-content/uploads/2025/02/fortnite-4129124_1280-210x140.jpg)](https://hackernews.cc/archives/64052 "Flowise 严重 RCE 漏洞遭攻击者利用")

##### [Flowise 严重 RCE 漏洞遭攻击者利用](https://hackernews.cc/archives/64052 "Flowise 严重 RCE 漏洞遭攻击者利用")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-08

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team