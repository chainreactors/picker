---
title: BreachForums黑客论坛再遭数据泄露 用户数据库被公之于众
url: https://www.4hou.com/posts/pn4m
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-14
fetch_date: 2026-01-15T03:30:19.895079
---

# BreachForums黑客论坛再遭数据泄露 用户数据库被公之于众

BreachForums黑客论坛再遭数据泄露 用户数据库被公之于众 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# BreachForums黑客论坛再遭数据泄露 用户数据库被公之于众

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)12680

收藏

导语：一个以ShinyHunters勒索团伙命名的网站发布了一个名为breachedforum.7z的7Zip压缩包。

本周，臭名昭著的黑客论坛BreachForums遭遇“黑吃黑”，其最新版本再次遭遇数据泄露，用户数据库表被神秘黑客泄露至网络。

BreachForums是一系列黑客论坛的统称，主要用于交易、出售和泄露被盗数据，以及贩卖企业网络访问权限和其他非法网络犯罪服务。该网站是在其前身RaidForums被执法部门查封、创始人Omnipotent被捕后应运而生的。

尽管BreachForums过去曾多次遭遇数据泄露和警方打击，但它总能更换新域名卷土重来，甚至有传言称该平台现已沦为执法部门的诱捕陷阱。

近日，一个以ShinyHunters勒索团伙命名的网站发布了一个名为breachedforum.7z的7Zip压缩包。

该压缩包包含三个文件：

**·**shinyhunte.rs-the-story-of-james.txt

**·**databoose.sql

**·**breachedforum-pgp-key.txt.asc

ShinyHunters 勒索团伙的一名代表表示，他们与发布该压缩包的网站并无关联。 压缩包中的breachedforum-pgp-key.txt.asc文件是BreachForums管理员用于签署官方消息的PGP私钥，该密钥创建于2023年7月25日。虽然密钥已泄露，但它受密码短语保护，若无密码则无法被滥用于签署消息。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260112/1768200940232337.png "1768200940232337.png")

带有密码保护的BreachForums PGP私人密钥

databoose.sql文件是一个 MyBB 用户数据库表（mybb\_users），包含323,988条会员记录，涵盖会员显示名、注册日期、IP地址及其他内部信息。

分析显示，大多数IP地址均指向本地回环地址（0x7F000009/127.0.0.9），因此价值不大。

然而，其中70,296条记录并未使用127.0.0.9 IP 地址，且经测试，这些记录映射至真实的公网IP。对于相关用户而言，这些公网IP可能构成操作安全（OPSEC）隐患，同时也对执法部门和网络安全研究人员具有重要价值。

新泄露用户数据库中的最后注册日期为2025年8月11日，这与此前位于breachforums[.]hn的BreachForums站点关闭的日期一致。该次关闭发生在其部分涉嫌运营者被捕之后。

当天，ShinyHunters 勒索团伙的一名成员在Scattered Lapsus$ Hunters Telegram频道发帖，声称该论坛是执法部门的蜜罐。随后，BreachForums管理员否认了这些指控。

breachforums[.]hn域名后来被ShinyHunters勒索团伙用于敲诈受大规模Salesforce数据盗窃攻击影响的企业，最终于2025年10月被查封。

目前的BreachForums管理员（代号N/A）已承认此次新泄露事件，称MyBB用户数据库表的备份曾暂时暴露在一个不安全的文件夹中，且仅被下载过一次。

N/A表示，这并非近期发生的事件。相关数据源自2025年8月的一次旧用户表泄露，当时正值BreachForums从.hn 域名进行恢复/重建期间。在恢复过程中，用户表和论坛PGP密钥曾在一个不安全的文件夹中临时存储了很短一段时间。调查显示，该文件夹在那段时间内确实仅被下载过一次。

虽然管理员表示BreachForums成员应使用一次性电子邮件地址以降低风险，且大多数IP地址均映射至本地IP，但该数据库仍包含可能令执法部门感兴趣的信息。

目前，该网站现已更新了 BreachForum PGP 私钥的密码。且有安全研究人员证实，密码确实是该密钥的正确密码。

文章来源自：https://www.bleepingcomputer.com/news/security/breachforums-hacking-forum-database-leaked-exposing-324-000-accounts/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ZnU3uV31)

#### 你可能感兴趣的

* [![]()

  盘点2025年改变网络安全游戏规则的七大网络安全关键词](https://www.4hou.com/posts/vwnM)
* [![]()

  BreachForums黑客论坛再遭数据泄露 用户数据库被公之于众](https://www.4hou.com/posts/pn4m)
* [![]()

  云文件共享平台成为企业数据盗窃攻击的目标](https://www.4hou.com/posts/0MwV)
* [![]()

  新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)
* [![]()

  GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)
* [![]()

  国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [盘点2025年改变网络安全游戏规则的七大网络安全关键词](https://www.4hou.com/posts/vwnM)
  2026-01-14 12:00:00
* [BreachForums黑客论坛再遭数据泄露 用户数据库被公之于众](https://www.4hou.com/posts/pn4m)
  2026-01-14 11:59:00
* [云文件共享平台成为企业数据盗窃攻击的目标](https://www.4hou.com/posts/0MwV)
  2026-01-13 12:00:00
* [新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)
  2026-01-12 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [盘点2025年改变网络安全游戏规则的七大网络安全关键词](https://www.4hou.com/posts/vwnM)

  山卡拉
* [BreachForums黑客论坛再遭数据泄露 用户数据库被公之于众](https://www.4hou.com/posts/pn4m)

  胡金鱼
* [云文件共享平台成为企业数据盗窃攻击的目标](https://www.4hou.com/posts/0MwV)

  胡金鱼
* [新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)

  胡金鱼
* [GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)

  胡金鱼
* [国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)