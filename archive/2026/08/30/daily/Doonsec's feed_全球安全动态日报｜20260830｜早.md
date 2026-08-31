---
title: 全球安全动态日报｜20260830｜早
url: https://mp.weixin.qq.com/s/w3PYb_zSp45z0Y4W9u9XrA
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:50:44.472135
---

# 全球安全动态日报｜20260830｜早

# 全球安全动态日报｜20260830｜早

安全资讯
安全资讯

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 全球安全动态日报｜20260830｜早

本期整理昨日公开的全球安全动态，并同步收录 HackerOne 昨日公开且获得赏金的漏洞报告。

The Hacker News：

2026年8月29日共收录5条安全动态，内容涵盖勒索支付争议、区块链与软件漏洞利用及Android 17隐私功能。

The Hacker News **5**  ·  HackerOne **0**

## The Hacker News

### 01 柏林拒绝向窃取该市州政府网络数据的黑客支付赎金

**公开时间：**2026年08月29日 05:30

AI 解读

柏林州政府确认其州行政网络在2026年8月被入侵后成为勒索威胁目标，并表示不会支付黑客的赎金要求。泄露工作发现交通、运输、气候保护和环境部的数据在8月7日至12日被外泄，范围和内容仍在调查，可能包括个人或非公开数据。泄露网站宣称窃取5.79TB数据和12076名个人信息。州长凯·韦格纳表示“柏林州正在被敲诈”。州刑事警察、公诉人和联邦安全机构正在调查嫌疑者，但未确定黑客团伙。Rhysida团伙在暗网泄露网站声称对此负责，该团伙使用被盗外部服务账户、Zerologon漏洞和网络钓鱼进行初始访问。美国CISA、FBI和MS-ISAC警告不要支付赎金，因为支付不保证恢复并可能助长对手攻击其他组织。柏林于8月17日披露事件，部门已于8月23日重新连接网络。

原文：https://thehackernews.com/2026/08/berlin-refuses-to-pay-hackers-who-stole.html

### 02 Cosmos EVM 漏洞遭利用，此前 Cosmos Labs 已知晓所有运行该组件的区块链均存在漏洞

**公开时间：**2026年08月29日 04:38

AI 解读

Cosmos Labs称，共享Cosmos EVM模块的关键余额处理漏洞（GHSA-7g4w-cg88-2cq2）在2026年8月20日至25日被利用，导致六条区块链资金被抽走。漏洞源于EVM仅记录可支配余额，而Cosmos SDK托管账户还包含锁定余额；委托金额超过可支配余额时发生未检查下溢并回绕至约2^256，状态对账可铸造或销毁资产。该漏洞4月报告后曾被误判为仅影响非18位小数网络，8月13日才确认所有Cosmos EVM链受影响，但修复仍通过公开静默补丁流程发布。受影响资产据称约有287万美元在去中心化交易所、另有约285万美元在中心化交易所售出，前者数据未经独立审计。

原文：https://thehackernews.com/2026/08/cosmos-evm-flaw-exploited-after-cosmos.html

### 03 攻击者利用两个PaperCut漏洞链实现未认证代码执行

**公开时间：**2026年08月29日 01:12

AI 解读

攻击者利用PaperCut NG和MF中的两个漏洞链式攻击，未认证攻击者可通过未授权请求修改服务器配置并执行任意Java代码。CVE-2026-82078存在于数据库连接工具中，CVE-2026-81578存在于Web管理界面下未认证请求可触发后端动作。Huntress研究人员指出此漏洞使攻击者远程控制PaperCut受信任配置，攻击链包括执行命令识别用户账户和操作系统，并部署.class文件指纹机器并列出文件目录写入/data/content/Udydn.out。PaperCut发布了针对v24 v25 v26的紧急补丁以进行额外加固，但攻击者发现了补丁绕过。

原文：https://thehackernews.com/2026/08/attackers-chain-two-papercut-flaws-to.html

### 04 Android 17 新增系统级 ECH 功能，向网络提供商隐藏网站访问记录

**公开时间：**2026年08月29日 00:20

AI 解读

Google宣布Android 17新增多项网络隐私与安全保护。系统级支持加密客户端问候（ECH），并默认启用ECH GREASE，与私有DNS配合隐藏访问域名及相关元数据，降低网络提供商和窥探者识别用户访问网站或应用的能力；OkHttp核心库也已支持ECH。系统还要求应用获用户许可后才能扫描或连接本地网络设备，默认启用证书透明度，并允许参与运营商为用户默认关闭2G，以减少降级攻击、恶意基站和短信轰炸器带来的风险。

原文：https://thehackernews.com/2026/08/android-17-adds-os-wide-ech-to-hide.html

### 05 五个严重的 WordPress 插件和主题漏洞可导致网站接管或远程代码执行 (RCE)

**公开时间：**2026年08月29日 00:00

AI 解读

文章披露了5个WordPress插件或主题的严重漏洞，均可被未认证攻击者利用，影响包括认证绕过、管理员账户接管、权限提升、任意文件写入及远程代码执行。WPMU DEV Dashboard在启用特定SSO配置时可导致站点接管；Avada与Fusion Builder组合可写入并执行PHP文件；TranslatePress可泄露管理员密码重置信息；Pods可提升为管理员或覆盖任意账户密码；GiveWP则因不安全反序列化、攻击者可控捐赠数据及现成利用链，可能实现服务器任意命令执行。

原文：https://thehackernews.com/2026/08/five-critical-wordpress-plugin-and.html

## HackerOne

昨日暂无符合标准的漏洞发布

![一个不正经的黑客 · 全球安全动态与知识分享](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR0wxk6alKwgl2znYoglw9fzyQU1dNd3QicIdQ2gekg7VXOz7LPmL1Kl2dpO5I60zgwgGuO6fVrTAo2PpLibVdWOo4OZYc7FQ4W7Q/640?from=appmsg)

继续阅读

点击文末「阅读原文」，可前往网站主页查看完整资讯与 AI 解读。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoPgcybP7CdwQuthRKXPkpYnwaQcOnXgEZT4r1rNWBU8D1I9HAMGWEWricXrOJ2UZNjo3YghpiaevyQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过