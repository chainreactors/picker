---
title: GrafanaGhost：攻击者可利用 Grafana 泄露企业数据
url: https://hackernews.cc/archives/64054
source: HackerNews
date: 2026-04-08
fetch_date: 2026-04-09T04:30:38.444523
---

# GrafanaGhost：攻击者可利用 Grafana 泄露企业数据

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![生成特定网络漏洞图片_副本](https://hackernews.cc/wp-content/uploads/2026/03/生成特定网络漏洞图片_副本.png)

# GrafanaGhost：攻击者可利用 Grafana 泄露企业数据

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-04-08](https://hackernews.cc/archives/64054 "10:57")
分类: [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
[暂无评论](https://hackernews.cc/archives/64054#respond)

* 浏览次数 178
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

Noma Security最新研究显示，**Grafana AI组件处理信息的方式存在漏洞，可能允许攻击者绕过应用防护并泄露企业信息。**

Grafana是一款开源分析和可视化应用，从各种来源摄取数据，通常对企业数据拥有广泛访问权限，包括财务指标、基础设施、客户信息和遥测数据。

新发现的GrafanaGhost漏洞允许攻击者绕过客户端保护和安全防护栏，将私有数据链接至外部服务器，在后台无需用户交互即可暴露敏感信息。

攻击者可通过在用户与条目日志交互时针对Grafana的AI功能利用该弱点。后台恶意提示触发问题，将Grafana转变为外泄载体。

为发动攻击，威胁行为体需制作指向外部资源的路径。经Grafana处理后，条目日志为攻击者提供对企业环境的访问权限。

随后，攻击者使用隐藏在外部上下文中的间接提示，指示Grafana的AI助手忽略其防护栏并渲染外部图像，迫使系统确认外部URL。

当AI助手尝试渲染图像时，会向攻击者服务器发出请求，受害者数据作为URL参数一并发送。”系统尝试显示图像时数据即泄露，”Noma表示。

该网络安全公司发现，**问题在于攻击者可通过猜测数据结构和模型”伪造任何使用Grafana的公司路径”。**此外，攻击者可使用应用数据存储中保存提示的位置。

从那里，攻击者可通过制作相应提示，滥用Grafana通过图像标签外泄数据。虽然Grafana设有阻止从外部域加载图像的保护措施，但验证图像URL的函数存在缺陷，可被利用绕过保护。

AI模型也设有防止注入包含图像Markdown提示的防护栏，但Noma发现关键词”intent”可用于绕过保护，向模型发出指令合法的讯号。

“将这些发现串联起来，我们实现了零用户交互的自动数据外泄。数据外泄完全在后台进行。对数据团队、DevSecOps或CISO而言，这看起来像是数据可视化的平常一天，”Noma指出，并补充Grafana在接到通知后立即修复了这些弱点。

BeyondTrust副首席信息安全官Bradley Smith表示，使用间接提示注入通过渲染内容外泄数据是众所周知的攻击向量，针对加固Grafana部署的可利用性尚不明确。

“实际可利用性很大程度上取决于部署细节：AI功能是否启用、是否存在出口控制、环境如何处理外部数据摄取。这不是Grafana的通用绕过；而是演示当AI组件处理不受信任输入且缺乏足够架构控制时可能发生的情况，”Smith表示。

Acalvio首席执行官Ram Varadarajan表示，GrafanaGhost表明AI的广泛采用已将防御转移到应用层之外，需要网络级URL阻断和加固AI以防范提示注入。

“最终，该漏洞证明边界控制不足。保护AI驱动工具的唯一方式是从监控代理被告知的内容，转向对其实际行为进行运行时行为监控，”Varadarajan表示。

---

**消息来源：[securityweek.com](https://www.securityweek.com/grafanaghost-attackers-can-abuse-grafana-to-leak-enterprise-data/)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[Grafana](https://hackernews.cc/archives/tag/grafana)[黑客](https://hackernews.cc/archives/tag/%E9%BB%91%E5%AE%A2)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用-美国](https://hackernews.cc/wp-content/uploads/2025/10/flag-2141861_960_720-210x140.jpg)](https://hackernews.cc/archives/64067 "洛杉矶市律师系统遭入侵，敏感警局文件泄露")

##### [洛杉矶市律师系统遭入侵，敏感警局文件泄露](https://hackernews.cc/archives/64067 "洛杉矶市律师系统遭入侵，敏感警局文件泄露")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-09

[![可用-wordpress-581849_1280](https://hackernews.cc/wp-content/uploads/2025/02/可用-wordpress-581849_1280-210x140.jpg)](https://hackernews.cc/archives/64053 "黑客利用 Ninja Forms WordPress 插件关键漏洞")

##### [黑客利用 Ninja Forms WordPress 插件关键漏洞](https://hackernews.cc/archives/64053 "黑客利用 Ninja Forms WordPress 插件关键漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-08

[![可用-代码](https://hackernews.cc/wp-content/uploads/2026/02/data-5606639_1920-210x140.jpg)](https://hackernews.cc/archives/64037 "朝鲜关联黑客利用 GitHub 作为 C2 基础设施攻击韩国")

##### [朝鲜关联黑客利用 GitHub 作为 C2 基础设施攻击韩国](https://hackernews.cc/archives/64037 "朝鲜关联黑客利用 GitHub 作为 C2 基础设施攻击韩国")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-07

[![可用-恶意代码](https://hackernews.cc/wp-content/uploads/2025/08/matrix-5028059_640-210x140.jpg)](https://hackernews.cc/archives/64026 "黑客利用 CVE-2025-55182 入侵 766 台 Next.js 主机窃取凭证")

##### [黑客利用 CVE-2025-55182 入侵 766 台 Next.js 主机窃取凭证](https://hackernews.cc/archives/64026 "黑客利用 CVE-2025-55182 入侵 766 台 Next.js 主机窃取凭证")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-03

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team