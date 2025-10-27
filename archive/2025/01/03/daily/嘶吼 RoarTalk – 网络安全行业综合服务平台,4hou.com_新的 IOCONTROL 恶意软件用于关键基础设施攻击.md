---
title: 新的 IOCONTROL 恶意软件用于关键基础设施攻击
url: https://www.4hou.com/posts/7MVO
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-01-03
fetch_date: 2025-10-06T20:07:45.352890
---

# 新的 IOCONTROL 恶意软件用于关键基础设施攻击

新的 IOCONTROL 恶意软件用于关键基础设施攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 IOCONTROL 恶意软件用于关键基础设施攻击

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-01-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)114179

收藏

导语：该恶意软件以“iocontrol”名称存储在“/usr/bin/”目录中，使用模块化配置来适应不同的供应商和设备类型，针对广泛的系统架构。

伊朗恶意分子正在利用名为 IOCONTROL 的新恶意软件来破坏以色列和美国关键基础设施使用的物联网 (IoT) 设备和 OT/SCADA 系统。

目标设备包括路由器、可编程逻辑控制器 (PLC)、人机界面 (HMI)、IP 摄像头、防火墙和燃料管理系统。该恶意软件的模块化特性使其能够危害不同制造商的各种设备，包括 D-Link、Hikvision、Baicells、Red Lion、Orpak、Phoenix Contact、Teltonika 和 Unitronics。

Claroty 的 Team82 研究人员发现了 IOCONTROL 并对其进行了采样进行分析，他们报告说，这是一种民族国家网络武器，可以对关键基础设施造成严重破坏。

鉴于持续的地缘政治冲突，IOCONTROL 目前用于针对以色列和美国的系统，例如 Orpak 和 Gasboy 燃料管理系统。据报道，该工具与一个名为 CyberAv3ngers 的伊朗黑客组织有关，该组织过去曾对攻击工业系统表现出兴趣。

OpenAI 最近还报告称，该威胁组织使用 ChatGPT 来破解 PLC、开发自定义 bash 和 Python 漏洞利用脚本，并计划入侵。

**IOCONTROL 攻击**

Claroty 从 Gasboy 燃油控制系统中提取了恶意软件样本，特别是该设备的支付终端 (OrPT)，但研究人员并不确切知道黑客是如何用 IOCONTROL 感染它的。

在这些设备内部，IOCONTROL 可以控制泵、支付终端和其他外围系统，从而可能导致中断或数据被盗。

威胁者在 Telegram 上声称破坏了以色列和美国的 200 个加油站，这与 Claroty 的调查结果一致。这些攻击发生在 2023 年末，大约与水处理设施中的 Unitronics Vision PLC/HMI 设备遭到破坏的时间相同，但研究人员报告称，新的攻击活动于 2024 年中期出现。截至 2024 年 12 月 10 日，66 个 VirusTotal 防病毒引擎均未检测到 UPX 打包的恶意软件二进制文件。

![gasboy.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241216/1734337890792688.png "1734337759105548.png")

Gasboy 燃油控制系统是从中提取恶意软件的地方

**恶意软件功能**

该恶意软件以“iocontrol”名称存储在“/usr/bin/”目录中，使用模块化配置来适应不同的供应商和设备类型，针对广泛的系统架构。它使用持久性脚本（“S93InitSystemd.sh”）在系统启动时执行恶意软件进程（“iocontrol”），因此重新启动设备不会将其停用。

它通过端口 8883 使用 MQTT 协议与其命令和控制 (C2) 服务器进行通信，这是物联网设备的标准通道和协议。唯一的设备 ID 嵌入到 MQTT 凭证中，以实现更好的控制。

DNS over HTTPS (DoH) 用于解析 C2 域，同时规避网络流量监控工具，并且恶意软件的配置使用 AES-256-CBC 进行加密。

IOCONTROL 支持的命令如下：

**·发送“hello”**：向C2报告详细的系统信息（例如主机名、当前用户、设备型号）。

**·检查执行**：确认恶意软件二进制文件已正确安装且可执行。

**·执行命令**：通过系统调用运行任意操作系统命令并报告输出。

**·自删除**：删除自己的二进制文件、脚本和日志以逃避检测。

**·端口扫描**：扫描指定的 IP 范围和端口以识别其他潜在目标。

上述命令是使用从“libc”库动态检索的系统调用执行的，并将输出写入临时文件以进行报告。

![flow.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241216/1734337891766805.png "1734337884101808.png")

简化的攻击流程

鉴于 IOCONTROL 目标在关键基础设施中的作用以及该组织的持续活动，Claroty 的报告为防御者提供了宝贵的资源，可以帮助他们识别和阻止威胁。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-iocontrol-malware-used-in-critical-infrastructure-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?I39YafNq)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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