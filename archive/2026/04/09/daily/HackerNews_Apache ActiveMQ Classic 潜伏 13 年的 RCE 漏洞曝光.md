---
title: Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光
url: https://hackernews.cc/archives/64066
source: HackerNews
date: 2026-04-09
fetch_date: 2026-04-10T04:45:11.847267
---

# Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用 代码](https://hackernews.cc/wp-content/uploads/2026/01/可用-代码.jpg)

# Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-04-09](https://hackernews.cc/archives/64066 "12:16")
分类: [漏洞](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E)
[暂无评论](https://hackernews.cc/archives/64066#respond)

* 浏览次数 168
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

Horizon3.ai报告，**Apache ActiveMQ Classic中潜伏13年的远程代码执行（RCE）漏洞可与旧漏洞链接以绕过认证。**

Apache ActiveMQ是开源消息和集成模式服务器，作为处理消息队列的中间件代理，广泛应用于众多行业。ActiveMQ Classic是该代理的原始版本。

新发现的漏洞编号**CVE-2026-34197**，允许攻击者通过Jolokia API调用管理操作，诱使代理检索远程配置文件并执行操作系统命令。

据Horizon3.ai称，该安全缺陷是CVE-2022-41678的绕过方案——该漏洞允许攻击者通过调用特定JDK MBean将Web shell写入磁盘。修复方案添加了一个标志，允许通过Jolokia调用每个ActiveMQ MBean的所有操作。代码执行问题出现在运行时设置代理间桥接的操作中。

然而，该漏洞的利用还需针对ActiveMQ的VM传输功能——该功能设计用于在应用程序内嵌入代理，导致客户端和代理在同一JVM内直接通信。

如果VM传输URI引用不存在的代理，ActiveMQ会创建一个，并接受指示其加载可能包含攻击者提供URL的配置参数。

通过链接这两种机制，攻击者可诱使代理检索并运行Spring XML配置文件，”实例化所有bean定义，导致远程代码执行”，Horizon3.ai表示。

该网络安全公司还指出，在某些部署中，可通过利用CVE-2024-32114实现无需认证的RCE——该漏洞将Jolokia API暴露给未经认证的用户。

“CVE-2024-32114是ActiveMQ 6.x中的独立漏洞，/api/\*路径（包括Jolokia端点）被无意中从Web控制台的安全约束中移除。这意味着在ActiveMQ 6.0.0至6.1.1版本中，Jolokia完全无需认证，”Horizon3.ai解释。

新发现的安全缺陷已在ActiveMQ Classic 5.19.4和6.2.3版本中修复，建议用户尽快更新部署。

---

**消息来源：[securityweek.com](https://www.securityweek.com/rce-bug-lurked-in-apache-activemq-classic-for-13-years/)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[Apache](https://hackernews.cc/archives/tag/apache)[漏洞](https://hackernews.cc/archives/tag/%E6%BC%8F%E6%B4%9E)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用-犯罪](https://hackernews.cc/wp-content/uploads/2025/08/criminal-8444883_640-1-210x140.jpg)](https://hackernews.cc/archives/64065 "OpenSSL 修复数据泄露等七处漏洞")

##### [OpenSSL 修复数据泄露等七处漏洞](https://hackernews.cc/archives/64065 "OpenSSL 修复数据泄露等七处漏洞")

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