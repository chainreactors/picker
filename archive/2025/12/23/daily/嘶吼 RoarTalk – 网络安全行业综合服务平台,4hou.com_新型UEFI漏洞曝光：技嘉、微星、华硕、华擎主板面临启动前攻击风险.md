---
title: 新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险
url: https://www.4hou.com/posts/0MWV
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-23
fetch_date: 2025-12-24T03:21:35.699745
---

# 新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险

新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-12-23 10:36:23

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)6758

收藏

导语：目前已确认，该漏洞影响华擎、华硕、技嘉、微星的部分主板型号，其他硬件厂商的产品也可能受到波及。

华硕、技嘉、微星、华擎部分型号主板的UEFI固件实现存在安全漏洞，可被直接内存访问（DMA）攻击利用，绕过系统启动初期的内存防护机制。

受厂商实现方式差异的影响，该安全问题被分配了多个漏洞编号：CVE-2025-11901、CVE-2025‑14302、CVE-2025-14303、CVE-2025-14304。

DMA是一项硬件功能，支持显卡、雷电设备、PCIe设备等外设绕开CPU，直接对内存（RAM）进行读写操作。IOMMU则是硬件级别的内存防火墙，运行于外设与内存之间，用于管控各设备可访问的内存区域范围。

在系统启动初期的UEFI固件初始化阶段，IOMMU必须先于DMA攻击的可能触发时机完成激活，否则系统将缺乏防护机制，无法阻止攻击者通过物理访问对内存区域进行读写操作。

**受影响系统无法启动《无畏契约》**

该漏洞由拳头游戏（Riot Games）的研究员发现。受漏洞影响，即使IOMMU未完成正确初始化，UEFI固件仍会显示DMA防护已启用，导致系统暴露在攻击风险中。

根据测试，计算机开机后会进入“权限最高的状态：可不受限制地访问整个系统及所有连接的硬件”。只有在加载初始固件（当前大多为UEFI）之后，系统才会获得防护能力——UEFI会以安全的方式完成硬件与软件的初始化，而操作系统是启动流程中最后加载的组件之一。

在存在漏洞的系统中，拳头游戏的部分游戏产品（如热门游戏《无畏契约》）将无法启动，这与其内核级反作弊系统“Vanguard”的机制有关：该系统的作用是防范游戏作弊行为。

拳头游戏表示：“如果作弊程序先于我们加载，就更有可能隐藏到我们无法检测的位置。这会让作弊程序有机会躲避检测，在游戏中造成更久的不良影响，这是我们无法接受的。”

尽管研究员是从游戏行业的角度对该漏洞进行说明——作弊程序可在系统启动初期完成加载，但该漏洞的安全风险并不止于此，恶意代码也可借助它入侵操作系统。

这类攻击需要攻击者获得物理访问权限：在操作系统启动前，将恶意PCIe设备接入设备发起DMA攻击，在此期间，恶意设备可随意读取或修改内存数据。

卡内基梅隆大学CERT协调中心（CERT/CC）的安全公告指出：“尽管固件声明DMA防护已启用，但在启动流程的初期交接阶段，它并未完成IOMMU的正确配置与激活。”

这一安全缺口使得具备DMA能力的恶意PCIe外设，可在操作系统层面的防护机制建立前，通过物理访问读取或修改系统内存。

由于攻击发生在操作系统启动之前，安全工具不会发出任何警告、权限提示或告警信息，用户无法感知攻击的发生。

**影响范围广泛**

目前已确认，该漏洞影响华擎、华硕、技嘉、微星的部分主板型号，其他硬件厂商的产品也可能受到波及。各厂商受影响的具体型号，可查看对应厂商（华硕、微星、技嘉、华擎）发布的安全公告与固件更新说明。

建议用户检查设备是否有可用的固件更新，在备份重要数据后完成安装。目前，拳头游戏已对其内核级反作弊系统Vanguard进行更新，该系统为《无畏契约》《英雄联盟》等游戏提供反脚本与反作弊防护。

如果系统受该UEFI漏洞影响，Vanguard将阻止《无畏契约》启动，并弹出弹窗告知用户启动游戏需要进行的操作。

文章来源自：https://www.bleepingcomputer.com/news/security/new-uefi-flaw-enables-pre-boot-attacks-on-motherboards-from-gigabyte-msi-asus-asrock/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?gILcaW2e)

#### 你可能感兴趣的

* [![]()

  新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)
* [![]()

  黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)
* [![]()

  漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)
* [![]()

  新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)
* [![]()

  漏洞预警 | React/Next.js组件存在RCE漏洞（CVE-2025-58360）](https://www.4hou.com/posts/mkrE)
* [![]()

  微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)
  2025-12-23 10:36:23
* [黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)
  2025-12-18 12:00:00
* [漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)
  2025-12-11 15:50:27
* [新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)
  2025-12-09 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型UEFI漏洞曝光：技嘉、微星、华硕、华擎主板面临启动前攻击风险](https://www.4hou.com/posts/0MWV)

  胡金鱼
* [黑客借 React2Shell 漏洞发起 EtherRAT 恶意软件攻击](https://www.4hou.com/posts/J1v9)

  胡金鱼
* [漏洞预警 | React/Next.js组件RCE漏洞（CVE-2025-55182）详情分析-【附验证环境】](https://www.4hou.com/posts/NGzm)

  盛邦安全
* [新型Mirai衍生僵尸网络ShadowV2现身 瞄准多品牌IoT设备漏洞发起攻击](https://www.4hou.com/posts/wxGm)

  胡金鱼
* [漏洞预警 | React/Next.js组件存在RCE漏洞（CVE-2025-58360）](https://www.4hou.com/posts/mkrE)

  盛邦安全
* [微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)

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