---
title: “Tsundere”僵尸网络利用游戏诱饵及基于以太坊的命令与控制服务器在Windows平台进行扩张
url: https://www.anquanke.com/post/id/313308
source: 安全客-有思想的安全新媒体
date: 2025-11-21
fetch_date: 2025-11-22T03:06:39.859709
---

# “Tsundere”僵尸网络利用游戏诱饵及基于以太坊的命令与控制服务器在Windows平台进行扩张

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

# “Tsundere”僵尸网络利用游戏诱饵及基于以太坊的命令与控制服务器在Windows平台进行扩张

阅读量**13545**

发布时间 : 2025-11-21 17:53:47

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2025/11/tsundere-botnet-expands-using-game.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员警告称，一个名为 **Tsundere** 的僵尸网络正在积极扩张，目标直指 Windows 用户。

该威胁自2025年年中开始活跃，旨在执行从命令与控制（C2）服务器获取的 **任意 JavaScript 代码**，卡巴斯基研究员 Lisandro Ubiedo 在今日发布的分析报告中表示。

### 传播途径与诱饵策略

目前尚无关于该僵尸网络恶意软件传播方式的详细信息；但至少在一个案例中，幕后威胁行为者被指利用 **合法的远程监控与管理（RMM）工具** 作为 conduit，从受攻陷网站下载 MSI 安装文件。

恶意软件工件的命名——**Valorant**、**r6x（彩虹六号：围攻 X）** 和 **cs2（反恐精英2）**——也暗示植入程序可能通过 **游戏相关诱饵** 传播。搜索这些游戏盗版版本的用户可能是攻击目标。

### 感染链与持久化机制

无论采用何种传播方法，伪造的 MSI 安装程序都会：

1. 安装 **Node.js** 并启动加载器脚本，负责解密和执行与僵尸网络相关的主 payload。
2. 通过 `npm install` 命令下载三个合法库：**ws**、**ethers** 和 **pm2**，以准备环境。

Ubiedo 解释：“安装 pm2 包是为确保 Tsundere 僵尸程序保持活跃并用于启动僵尸网络。此外，pm2 通过写入注册表并配置为登录时重启进程，帮助实现系统持久化。”

卡巴斯基对 C2 面板的分析显示，恶意软件还以 **PowerShell 脚本** 形式传播，通过在受感染主机上部署 Node.js 并下载 ws 和 ethers 作为依赖项，执行类似操作序列。

尽管 PowerShell 感染程序不使用 pm2，但它会创建注册表键值，确保每次登录时通过生成新实例来执行僵尸程序，这与 MSI 安装程序中的行为一致。

### 以太坊区块链与动态 C2 机制

Tsundere 僵尸网络利用 **以太坊区块链** 获取 WebSocket C2 服务器详情（例如 `ws://193.24.123[.]68:3011` 或 `ws://185.28.119[.]179:1234`），形成一种弹性机制，使攻击者只需通过智能合约即可轮换基础设施。该合约创建于2024年9月23日，迄今已有26笔交易。

![]()

获取 C2 地址后，程序会检查其是否为有效 WebSocket URL，然后与特定地址建立 WebSocket 连接，接收服务器发送的 JavaScript 代码。卡巴斯基表示，在观察期间未发现服务器发送任何后续命令。

“评估代码的能力使 Tsundere 僵尸程序相对简单，但也提供了灵活性和动态性，允许僵尸网络管理员将其调整用于广泛操作，”卡巴斯基称。

僵尸网络操作通过一个控制面板实现，允许登录用户：

1. 使用 MSI 或 PowerShell 构建新工件
2. 管理管理功能
3. 查看任意时间点的僵尸数量
4. 将僵尸程序转换为代理以路由恶意流量
5. 通过专用市场浏览和购买僵尸网络

Tsundere 的幕后操作者身份不明。该活动被评估与 Checkmarx、Phylum 和 Socket 于2024年11月记录的恶意 npm 攻击活动存在功能重叠。

此外，同一服务器被发现托管与 **123 Stealer** 信息窃取器相关的 C2 面板，该窃取器以每月120美元的订阅制提供。Outpost24 的 KrakenLabs 团队称，威胁行为者“koneko”于2025年6月17日在暗网论坛首次宣传该窃取器。

“感染可通过 MSI 和 PowerShell 文件发生，这为伪装安装程序、将钓鱼作为入口点或与其他攻击机制集成提供了灵活性，使其成为更可怕的威胁，”卡巴斯基称。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2025/11/tsundere-botnet-expands-using-game.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313308](/post/id/313308)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2025/11/tsundere-botnet-expands-using-game.html)

如若转载,请注明出处： <https://thehackernews.com/2025/11/tsundere-botnet-expands-using-game.html>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **716**

* 粉丝
* **6**

### TA的文章

* ##### [N-able N-central 中存在严重漏洞，允许攻击者未授权交互遗留API并读取敏感文件](/post/id/313330)

  2025-11-21 17:56:21
* ##### [TamperedChef攻击活动滥用日常应用部署恶意软件，并为攻击者开启远程访问通道](/post/id/313323)

  2025-11-21 17:55:57
* ##### [新型macOS窃密木马DigitStealer伪装成DynamicLake，专门针对苹果M2/M3芯片设备](/post/id/313320)

  2025-11-21 17:55:18
* ##### [欧盟提出GDPR全面修订案，拟重新界定个人数据范畴与用户同意规则](/post/id/313317)

  2025-11-21 17:54:53
* ##### [Windows图形组件存在关键漏洞，可致攻击者通过单张图片夺取系统控制权](/post/id/313312)

  2025-11-21 17:54:23

### 相关文章

* ##### [N-able N-central 中存在严重漏洞，允许攻击者未授权交互遗留API并读取敏感文件](/post/id/313330)

  2025-11-21 17:56:21
* ##### [TamperedChef攻击活动滥用日常应用部署恶意软件，并为攻击者开启远程访问通道](/post/id/313323)

  2025-11-21 17:55:57
* ##### [新型macOS窃密木马DigitStealer伪装成DynamicLake，专门针对苹果M2/M3芯片设备](/post/id/313320)

  2025-11-21 17:55:18
* ##### [欧盟提出GDPR全面修订案，拟重新界定个人数据范畴与用户同意规则](/post/id/313317)

  2025-11-21 17:54:53
* ##### [Windows图形组件存在关键漏洞，可致攻击者通过单张图片夺取系统控制权](/post/id/313312)

  2025-11-21 17:54:23
* ##### [WSUS中存在关键远程代码执行漏洞（CVE-2025-59287），正被积极利用以部署ShadowPad后门](/post/id/313305)

  2025-11-21 17:52:53
* ##### [新型Sturnus木马可突破WhatsApp/Signal加密防护并完全控制Android设备](/post/id/313302)

  2025-11-21 17:51:00

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