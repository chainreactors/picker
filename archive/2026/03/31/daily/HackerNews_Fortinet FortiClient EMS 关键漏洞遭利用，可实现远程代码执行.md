---
title: Fortinet FortiClient EMS 关键漏洞遭利用，可实现远程代码执行
url: https://hackernews.cc/archives/63984
source: HackerNews
date: 2026-03-31
fetch_date: 2026-04-01T04:46:15.779566
---

# Fortinet FortiClient EMS 关键漏洞遭利用，可实现远程代码执行

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用——写代码](https://hackernews.cc/wp-content/uploads/2026/02/innovalabs-software-development-6523979_1920.jpg)

# Fortinet FortiClient EMS 关键漏洞遭利用，可实现远程代码执行

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-03-31](https://hackernews.cc/archives/63984 "15:23")
分类: [漏洞](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E)
[暂无评论](https://hackernews.cc/archives/63984#respond)

* 浏览次数 181
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

**Fortinet FortiClient EMS平台的关键漏洞CVE-2026-21643（CVSS评分9.1）正遭主动利用，攻击者可通过SQL注入执行远程代码。**

Defused研究人员警告称，威胁行为体正在利用Fortinet FortiClient EMS平台的该漏洞。Defused在X平台发文称：”Fortinet FortiClient EMS CVE-2026-21643——目前CISA及其他已知被利用漏洞（KEV）列表标记为未利用——据我们数据显示已于4天前首次遭利用。攻击者可通过HTTP请求中的’Site’头走私SQL语句。据Shodan统计，近1000个FortiClient EMS实例公开暴露。”

今年2月，Fortinet发布紧急公告修复该关键漏洞。该漏洞为FortiClientEMS中SQL命令特殊元素处理不当（”SQL注入”）问题，未经认证的攻击者可触发该漏洞，通过特制HTTP请求执行未授权代码或命令。

公告指出：”FortiClientEMS中SQL命令特殊元素处理不当（’SQL注入’）漏洞[CWE-89]可能允许未经认证的攻击者通过特制HTTP请求执行未授权代码或命令。”

成功攻击可使攻击者在目标网络中获得初始立足点，实现横向移动或恶意软件部署。

该漏洞由Fortinet产品安全团队Gwendal Guégniaud内部发现并报告。

**受影响版本：**

| 版本 | 受影响情况 | 解决方案 |
| --- | --- | --- |
| FortiClientEMS 8.0 | 不受影响 | 不适用 |
| FortiClientEMS 7.4 | 7.4.4 | 升级至7.4.5或更高版本 |
| FortiClientEMS 7.2 | 不受影响 | 不适用 |

今年2月，厂商未披露该漏洞是否正遭野外主动利用。

尽管尚未出现在主要被利用列表中，但现实世界攻击已被观察到。

Shadowserver研究人员报告称，约2000个FortiClient EMS实例在线暴露，其中大部分位于美国（756个）和欧洲（683个）。

2024年3月，美国网络安全与基础设施安全局（CISA）曾将FortiClient EMS SQL注入漏洞CVE-2023-48788加入其KEV目录。

---

**消息来源：[securityaffairs.com](https://securityaffairs.com/190158/security/critical-fortinet-forticlient-ems-flaw-exploited-for-remote-code-execution.html)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[Fortinet](https://hackernews.cc/archives/tag/fortinet)[漏洞](https://hackernews.cc/archives/tag/%E6%BC%8F%E6%B4%9E)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用](https://hackernews.cc/wp-content/uploads/2026/01/blue-hand-2228501_640-210x140.jpg)](https://hackernews.cc/archives/63996 "Claude AI 发现 Vim 和 Emacs 文件打开时触发的远程代码执行漏洞")

##### [Claude AI 发现 Vim 和 Emacs 文件打开时触发的远程代码执行漏洞](https://hackernews.cc/archives/63996 "Claude AI 发现 Vim 和 Emacs 文件打开时触发的远程代码执行漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-01

[![可用-恶意软件](https://hackernews.cc/wp-content/uploads/2026/02/geralt-data-theft-9480279_1920-210x140.jpg)](https://hackernews.cc/archives/63968 "Smart Slider 插件文件读取漏洞影响 50 万 WordPress 网站")

##### [Smart Slider 插件文件读取漏洞影响 50 万 WordPress 网站](https://hackernews.cc/archives/63968 "Smart Slider 插件文件读取漏洞影响 50 万 WordPress 网站")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-30

[![可用](https://hackernews.cc/wp-content/uploads/2025/12/ai-generated-9294294_960_720-210x140.png)](https://hackernews.cc/archives/63964 "Citrix NetScaler 关键漏洞遭主动侦察，内存越界读取风险加剧")

##### [Citrix NetScaler 关键漏洞遭主动侦察，内存越界读取风险加剧](https://hackernews.cc/archives/63964 "Citrix NetScaler 关键漏洞遭主动侦察，内存越界读取风险加剧")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-30

[![可用-黑客](https://hackernews.cc/wp-content/uploads/2025/08/ai-generated-8630602_640-210x140.png)](https://hackernews.cc/archives/63953 "Citrix NetScaler 严重漏洞或致数据泄露，建议立即更新")

##### [Citrix NetScaler 严重漏洞或致数据泄露，建议立即更新](https://hackernews.cc/archives/63953 "Citrix NetScaler 严重漏洞或致数据泄露，建议立即更新")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-25

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team