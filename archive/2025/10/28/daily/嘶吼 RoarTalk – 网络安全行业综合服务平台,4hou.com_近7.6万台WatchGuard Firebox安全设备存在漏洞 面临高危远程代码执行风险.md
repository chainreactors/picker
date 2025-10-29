---
title: 近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险
url: https://www.4hou.com/posts/7M5w
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-10-28
fetch_date: 2025-10-29T03:14:44.354300
---

# 近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险

近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7911

收藏

导语：目前尚未有报告显示CVE-2025-9242漏洞已被攻击者活跃利用，但官方强烈建议尚未安装安全更新的管理员，尽快为设备部署补丁。

全球有近7.6万台WatchGuard Firebox网络安全设备暴露在公网上，且仍未修复高危漏洞CVE-2025-9242——远程攻击者无需身份验证，即可利用该漏洞执行代码。

Firebox设备是网络核心防御枢纽，负责管控内网与外网间的流量。它通过策略管理、安全服务、虚拟专用网络提供防护，并借助WatchGuard Cloud实现实时可视化监控。

**设备暴露与地域分布：超7.5万台受影响，欧美占比高**

据Shadowserver基金会的扫描数据显示，目前全球共有75,835台存在漏洞的Firebox设备，多数分布在欧洲与北美地区。具体国家分布排名如下：

1. 美国：24,500台（数量最多）；

2. 德国：7,300台；

3. 意大利：6,800台；

4. 英国：5,400台；

5. 加拿大：4,100台；

6. 法国：2,000台。

10月19日，Shadowserver基金会曾检测到75,955台存在漏洞的Firebox防火墙。该机构发言人称，当前扫描结果具备可靠性，数据反映的是真实部署设备数量，暂未包含蜜罐（用于诱捕黑客的模拟设备）。

**漏洞详情：高危CVE-2025-9242，源于Fireware OS进程漏洞**

WatchGuard于9月17日在安全公告中披露CVE-2025-9242漏洞，将其风险等级定为“高危”，CVSS评分为9.3分。该漏洞本质是Fireware OS操作系统中“iked”进程存在“越界写入”问题，而“iked”进程负责处理IKEv2协议的VPN协商流程。

攻击者利用漏洞的方式无需认证：向存在漏洞的Firebox设备发送特制IKEv2数据包，迫使设备将数据写入非预期内存区域，进而触发恶意代码执行。

**1. 受影响设备与版本范围**

该漏洞仅影响同时满足以下两个条件的Firebox设备：

功能层面：使用IKEv2 VPN且对接“动态网关节点”；

版本层面：Fireware OS版本为11.10.2至11.12.4\_Update1、12.0至12.11.3、2025.1。

**2. 特殊场景与临时防护**

若设备仅配置“分支办公室VPN”且对接“静态网关节点”，暂不受该漏洞直接影响。厂商建议此类用户参考官方文档，通过IPSec与IKEv2协议加固连接，作为临时防护方案。

WatchGuard官方明确建议用户将设备升级至以下安全版本，以彻底修复漏洞：

**·**2025.1.1

**·**12.11.4

**·**12.5.13

**·**12.3.1\_Update3（版本号B722811）

需特别注意：Fireware OS 11.x版本已达“支持终止期”，厂商不再为该版本提供安全更新。仍使用11.x版本的用户，需尽快升级至仍受支持的版本，避免因无法修复漏洞持续暴露风险。

目前尚未有报告显示CVE-2025-9242漏洞已被攻击者活跃利用，但官方强烈建议尚未安装安全更新的管理员，尽快为设备部署补丁——Firebox设备作为网络边界核心防护，一旦被攻陷，可能导致内网完全暴露，风险不可忽视。虽无活跃攻击报告，仍需紧急打补丁。

文章翻译自：https://www.bleepingcomputer.com/news/security/over-75-000-watchguard-security-devices-vulnerable-to-critical-rce/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?gSaehaDy)

#### 你可能感兴趣的

* [![]()

  近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)
* [![]()

  RondoDox僵尸网络在全球攻击行动中针对56个n-day漏洞发起攻击](https://www.4hou.com/posts/ArVB)
* [![]()

  Redis已存在13年之久的Lua漏洞可导致远程代码执行](https://www.4hou.com/posts/rp3w)
* [![]()

  关于防范PS1Bot恶意软件的风险提示](https://www.4hou.com/posts/xy3J)
* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)
  2025-10-28 12:00:00
* [RondoDox僵尸网络在全球攻击行动中针对56个n-day漏洞发起攻击](https://www.4hou.com/posts/ArVB)
  2025-10-17 12:00:00
* [Redis已存在13年之久的Lua漏洞可导致远程代码执行](https://www.4hou.com/posts/rp3w)
  2025-10-11 12:00:00
* [关于防范PS1Bot恶意软件的风险提示](https://www.4hou.com/posts/xy3J)
  2025-10-10 15:15:14

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)

  胡金鱼
* [RondoDox僵尸网络在全球攻击行动中针对56个n-day漏洞发起攻击](https://www.4hou.com/posts/ArVB)

  胡金鱼
* [Redis已存在13年之久的Lua漏洞可导致远程代码执行](https://www.4hou.com/posts/rp3w)

  胡金鱼
* [关于防范PS1Bot恶意软件的风险提示](https://www.4hou.com/posts/xy3J)

  胡金鱼
* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

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