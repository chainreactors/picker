---
title: 新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信
url: https://www.4hou.com/posts/VWYO
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-14
fetch_date: 2026-02-15T04:25:32.119394
---

# 新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信

新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-02-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)11226

收藏

导语：SSHStalker 感染主机后，会下载 GCC 编译工具，在受害设备上直接编译恶意载荷，以提升程序可移植性与规避检测能力。

安全研究员最新发现的一款 Linux 僵尸网络 SSHStalker，采用IRC（互联网中继聊天）通信协议实现命令与控制（C2）操作。

据了解，该协议于 1988 年问世，在 20 世纪 90 年代达到普及高峰，成为当时用于群组与私密通信的主流文本即时通信方案。技术社区至今仍青睐其实现简单、互操作性强、带宽占用低且无需图形界面（GUI）等特点。

SSHStalker 僵尸网络并未采用现代化命令与控制框架，而是依托经典 IRC 机制运行，例如使用多个基于 C 语言编写的木马程序、多服务器/多频道冗余设计，更注重韧性、规模化与低成本，而非隐蔽性与技术新颖性。

研究人员表示，这种思路也体现在 SSHStalker 的其他攻击行为中，例如使用特征明显的 SSH 扫描、每分钟执行一次的定时任务，以及大量距今已有 15 年历史的漏洞（CVE）。

据悉，安全研究人员实际发现的是一个特征明显、拼凑而成的僵尸网络工具包，融合了传统 IRC 控制、在主机上编译二进制程序、大规模 SSH 攻陷以及基于定时任务实现持久化等手段。简单来说，这是一套优先规模、注重可靠而非隐蔽的运营模式。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260211/1770791899136413.png "1770791877123571.png")

受感染主机 IRC 频道

SSHStalker 通过自动化 SSH 扫描与暴力破解实现初始入侵，其使用的 Go 语言二进制程序会伪装成知名开源网络探测工具 Nmap。

被攻陷的主机随后会被用于扫描更多 SSH 目标，形成类似蠕虫的传播扩散机制。

研究人员发现了一份包含近 7000 条僵尸网络扫描结果的文件，均来自今年 1 月，攻击目标主要集中在Oracle Cloud等云服务商。

SSHStalker 感染主机后，会下载 GCC 编译工具，在受害设备上直接编译恶意载荷，以提升程序可移植性与规避检测能力。

首批载荷为基于 C 语言的 IRC 木马，内置硬编码的控制服务器与频道信息，将新受害主机纳入僵尸网络的 IRC 控制体系。

随后，该恶意软件会下载名为 GS 和 bootbou 的压缩包，其中包含用于统一调度与按序执行的不同木马变体。

持久化机制通过每 60 秒运行一次的定时任务实现，该任务采用看门狗式更新逻辑，检查主木马进程是否运行，若被终止则重新启动。

该僵尸网络还集成了针对 2009—2010 年版本 Linux 内核的 16 个漏洞利用程序，在暴力破解获得低权限用户访问权限后，用于实现权限提升。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260211/1770791903191292.png "1770791903191292.png")

攻击链概述

在牟利方式上，该僵尸网络会窃取 AWS 密钥、扫描网站，并集成了挖矿程序，包括高性能以太坊挖矿工具 PhoenixMiner。

僵尸网络同样具备分布式拒绝服务（DDoS）攻击能力，但研究人员表示暂未观测到相关攻击行为。事实上，SSHStalker 木马目前仅连接控制服务器后便进入闲置状态，表明其仍处于测试或囤积访问权限阶段。

研究人员尚未将 SSHStalker 归属到特定攻击组织，但发现其与 Outlaw/Maxlas 僵尸网络体系存在相似之处，并出现多项与罗马尼亚相关的特征线索。

威胁情报机构建议，在生产服务器上应部署针对编译器安装与执行行为的监控方案，并对 IRC 类型的出站连接设置告警。来自异常路径、执行周期极短的定时任务，也是高度危险的预警信号。

安全研究人员提出了一些防御建议，例如关闭 SSH 密码认证、从生产环境镜像中移除编译器、强制实施出站流量过滤，以及限制从 /dev/shm目录执行程序等举措。

文章来源自：https://www.bleepingcomputer.com/news/security/new-linux-botnet-sshstalker-uses-old-school-irc-for-c2-comms/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?BJfXUWCR)

#### 你可能感兴趣的

* [![]()

  新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信](https://www.4hou.com/posts/VWYO)
* [![]()

  AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证](https://www.4hou.com/posts/5M6A)
* [![]()

  AI真的能取代人类吗？提升效率利用AI辅助写代码，真的靠谱吗？](https://www.4hou.com/posts/1M2G)
* [![]()

  2025年全球加密货币网络犯罪激增，黑客与勒索攻击事件持续高发](https://www.4hou.com/posts/EyJ4)
* [![]()

  黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种](https://www.4hou.com/posts/wxXz)
* [![]()

  八问+一图，读懂《汽车数据出境安全指引（2026版）》](https://www.4hou.com/posts/MXRR)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信](https://www.4hou.com/posts/VWYO)
  2026-02-14 12:00:00
* [AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证](https://www.4hou.com/posts/5M6A)
  2026-02-14 11:59:00
* [AI真的能取代人类吗？提升效率利用AI辅助写代码，真的靠谱吗？](https://www.4hou.com/posts/1M2G)
  2026-02-13 12:01:00
* [2025年全球加密货币网络犯罪激增，黑客与勒索攻击事件持续高发](https://www.4hou.com/posts/EyJ4)
  2026-02-11 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型Linux僵尸网络SSHStalker利用传统IRC协议实现命令与控制（C2）通信](https://www.4hou.com/posts/VWYO)

  胡金鱼
* [AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证](https://www.4hou.com/posts/5M6A)

  胡金鱼
* [AI真的能取代人类吗？提升效率利用AI辅助写代码，真的靠谱吗？](https://www.4hou.com/posts/1M2G)

  山卡拉
* [2025年全球加密货币网络犯罪激增，黑客与勒索攻击事件持续高发](https://www.4hou.com/posts/EyJ4)

  胡金鱼
* [黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种](https://www.4hou.com/posts/wxXz)

  胡金鱼
* [八问+一图，读懂《汽车数据出境安全指引（2026版）》](https://www.4hou.com/posts/MXRR)

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