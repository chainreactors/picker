---
title: TrueConf 零日漏洞在针对东南亚政府网络攻击中被利用
url: https://hackernews.cc/archives/63997
source: HackerNews
date: 2026-04-01
fetch_date: 2026-04-02T04:29:39.009198
---

# TrueConf 零日漏洞在针对东南亚政府网络攻击中被利用

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![hacker-1500899_可用](https://hackernews.cc/wp-content/uploads/2025/02/hacker-1500899_可用.jpg)

# TrueConf 零日漏洞在针对东南亚政府网络攻击中被利用

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-04-01](https://hackernews.cc/archives/63997 "11:05")
分类: [漏洞](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E),[网络犯罪](https://hackernews.cc/archives/category/%E7%BD%91%E7%BB%9C%E7%8A%AF%E7%BD%AA)
[暂无评论](https://hackernews.cc/archives/63997#respond)

* 浏览次数 205
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

TrueConf 客户端视频会议软件中一个严重安全漏洞，在名为 “TrueChaos” 的针对东南亚政府机构的攻击活动中，被作为零日漏洞在实际中利用。

该漏洞编号为 **CVE – 2026 – 3502**（通用漏洞评分系统 CVSS 得分为 7.8），是在获取应用程序更新代码时缺乏完整性检查，攻击者借此可分发篡改后的更新，从而导致任意代码执行。**本月早些时候发布的 TrueConf Windows 客户端 8.5.3 版本起已修复此漏洞。**

Check Point 在今日发布的一份报告中称：“该漏洞源于对 TrueConf 更新验证机制的滥用，攻击者若控制本地 TrueConf 服务器，就能在所有连接的端点上分发并执行任意文件。”

换句话说，成功控制本地 TrueConf 服务器的攻击者，可将更新包替换为含恶意代码的版本，由于客户端应用程序对服务器提供的更新未进行充分验证以确保未被篡改，就会下载该恶意更新包。

已发现 “TrueChaos” 攻击活动利用更新机制中的这一漏洞，很可能将开源的 Havoc 命令与控制（C2）框架部署到易受攻击的端点。

这家网络安全公司在 2026 年初首次记录到利用该漏洞的攻击，客户端对更新机制的信任被利用，推送了恶意安装程序，进而通过 DLL 侧加载启动 DLL 后门。

研究还观察到，DLL 植入程序（“7z – x64.dll”）会执行手动操作进行侦察、设置持久化，并从 FTP 服务器（“47.237.15 [.] 197”）检索其他有效载荷（“iscsiexe.dll”）。“iscsiexe.dll” 的主要目的是确保执行一个良性二进制文件（“poweriso.exe”），通过该文件侧加载后门程序。

尽管此次攻击最终阶段所投放的确切恶意软件尚不清楚，但可以高度确信，其最终目标是部署 Havoc 植入程序。

Check Point 表示：“利用 CVE – 2026 – 3502 漏洞，攻击者无需逐个入侵每个端点。相反，攻击者滥用了本地中央 TrueConf 服务器与其客户端之间的信任关系。通过将合法更新替换为恶意更新，他们把产品的正常更新流程变成了跨多个相连政府网络的恶意软件分发渠道。”

---

**消息来源：[thehackernews.com](https://thehackernews.com/2026/03/trueconf-zero-day-exploited-in-attacks.html)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[TrueConf](https://hackernews.cc/archives/tag/trueconf)[零日漏洞](https://hackernews.cc/archives/tag/%E9%9B%B6%E6%97%A5%E6%BC%8F%E6%B4%9E)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![微软](https://hackernews.cc/wp-content/uploads/2020/10/微软.jpg)](https://hackernews.cc/archives/62998 "微软 Office Word 零日漏洞遭在野利用")

##### [微软 Office Word 零日漏洞遭在野利用](https://hackernews.cc/archives/62998 "微软 Office Word 零日漏洞遭在野利用")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-02-12

[![可用-AI](https://hackernews.cc/wp-content/uploads/2023/07/cyborg-2765349_640-210x140.jpg)](https://hackernews.cc/archives/62456 "Gemini MCP 工具存在零日漏洞，允许远程攻击者执行任意代码")

##### [Gemini MCP 工具存在零日漏洞，允许远程攻击者执行任意代码](https://hackernews.cc/archives/62456 "Gemini MCP 工具存在零日漏洞，允许远程攻击者执行任意代码")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-01-29

[![可用 微软](https://hackernews.cc/wp-content/uploads/2026/01/可用-微软-210x140.jpg)](https://hackernews.cc/archives/62411 "微软紧急更新修复在野利用的 Office 零日漏洞")

##### [微软紧急更新修复在野利用的 Office 零日漏洞](https://hackernews.cc/archives/62411 "微软紧急更新修复在野利用的 Office 零日漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-01-27

[![hacking-1685092_可用](https://hackernews.cc/wp-content/uploads/2025/02/hacking-1685092_可用-210x140.jpg)](https://hackernews.cc/archives/61895 "Gogs 未修复零日漏洞遭利用，700多个实例在主动攻击中受侵")

##### [Gogs 未修复零日漏洞遭利用，700多个实例在主动攻击中受侵](https://hackernews.cc/archives/61895 "Gogs 未修复零日漏洞遭利用，700多个实例在主动攻击中受侵")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2025-12-12

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team