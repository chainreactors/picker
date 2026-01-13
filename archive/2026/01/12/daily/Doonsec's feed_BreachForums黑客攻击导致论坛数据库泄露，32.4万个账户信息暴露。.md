---
title: BreachForums黑客攻击导致论坛数据库泄露，32.4万个账户信息暴露。
url: https://mp.weixin.qq.com/s/ij3yLJR5ekeHltz7svr_cw
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:29:06.056845
---

# BreachForums黑客攻击导致论坛数据库泄露，32.4万个账户信息暴露。

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pcgSUGCDdKLia5736RicxEr9l2NpK3QAb8MsXwDTHNq3WV6VyFkPOeTrkK8Qj5Ifnz4dU0WQ908RJ531uICy7xtQ/0?wx_fmt=jpeg)

# BreachForums黑客攻击导致论坛数据库泄露，32.4万个账户信息暴露。

原创

网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

臭名昭著的黑客论坛 BreachForums 的最新版本遭遇数据泄露，其用户数据库表已在网上泄露。

BreachForums 是一系列黑客论坛的名称，这些论坛用于交易、出售和泄露被盗数据，以及出售对企业网络和其他非法网络犯罪服务的访问权限。

该网站是在第一个此类论坛 RaidForums被执法部门查封，其所有者“Omnipotent”被捕后推出的。

虽然 BreachForums 过去曾遭受数据泄露和警方的调查，但它已多次在新域名下重新上线，一些人指责它现在已成为执法部门的诱饵。

昨天，一个名为 ShinyHunters 勒索团伙的网站发布了一个名为 brokeedforum.7z 的 7Zip 压缩文件。

此压缩包包含三个文件，文件名分别为：

* shinyhunte.rs-the-story-of-james.txt
* databoose.sql
* breachedforum-pgp-key.txt.asc

ShinyHunters 勒索团伙的一名代表向 BleepingComputer 声称，他们与分发此存档的网站没有任何关联。

存档中的“breachedforum-pgp-key.txt.asc”文件是2023年7月25日创建的PGP私钥，BreachForums使用该私钥签署管理员的官方消息。虽然该密钥已被泄露，但它受密码保护，没有密码，就无法滥用该密钥签署消息。

![受密码保护的 BreachForums PGP 私钥](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pcgSUGCDdKLia5736RicxEr9l2NpK3QAb8AVnxfyPCRn5AXAmXGdVIDcPS1ODibFJBWdanvOatXwHsa5cwEib74WAg/640?wx_fmt=jpeg&from=appmsg)

“databoose.sql”文件是一个MyBB用户数据库表（mybb\_users），其中包含323,988条成员记录，包括成员显示名称、注册日期、IP地址和其他内部信息。

BleepingComputer 对该表的分析表明，大多数 IP 地址都映射到本地环回 IP 地址 (0x7F000009/127.0.0.9)，因此它们用处不大。

然而，有70,296条记录不包含127.0.0.9这个IP地址，而且我们测试的记录都指向一个公共IP地址。这些公共IP地址可能对相关人员构成安全隐患，但对执法部门和网络安全研究人员来说却很有价值。

最新泄露的用户数据库中，最后一次注册日期为2025年8月11日，与之前位于breachforums[.]hn的BreachForums论坛关闭日期相同。此次关闭是由于部分涉嫌运营者被捕所致。

当天，ShinyHunters勒索团伙的一名成员在名为“Scattered Lapsus$ Hunters”的Telegram频道上发帖称，该论坛是执法部门的诱饵陷阱。BreachForums的管理员随后否认了这些指控。

2025 年 10 月，执法部门查封了brokeforums[.]hn 域名，此前该域名被重新用于勒索受ShinyHunters 勒索团伙实施的Salesforce 数据盗窃攻击影响的公司。

当前 BreachForums 管理员（代号“N/A”）已承认此次新的数据泄露事件，并表示 MyBB 用户数据库表的备份文件暂时暴露在一个不安全的文件夹中，且仅下载过一次。

“我们想回应最近关于所谓数据库泄露的讨论，并清楚地解释发生了什么，”N/A 在 BreachForums 上写道。

“首先，这并非近期发生的事件。相关数据源自2025年8月的一次用户表泄露事件，当时BreachForums正在从.hn域名恢复/重建。”

“在恢复过程中，用户表和论坛 PGP 密钥曾短暂地存储在一个不安全的文件夹中。我们的调查显示，该文件夹在那段时间内只被下载过一次，”管理员继续说道。

虽然管理员表示 BreachForums 成员应该使用一次性电子邮件地址来降低风险，并且大多数 IP 地址都映射到本地 IP，但该数据库仍然包含执法部门可能感兴趣的信息。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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