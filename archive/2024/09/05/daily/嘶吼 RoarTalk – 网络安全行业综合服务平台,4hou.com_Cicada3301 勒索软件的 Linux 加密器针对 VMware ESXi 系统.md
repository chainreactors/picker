---
title: Cicada3301 勒索软件的 Linux 加密器针对 VMware ESXi 系统
url: https://www.4hou.com/posts/QXkY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-05
fetch_date: 2025-10-06T18:23:59.341542
---

# Cicada3301 勒索软件的 Linux 加密器针对 VMware ESXi 系统

Cicada3301 勒索软件的 Linux 加密器针对 VMware ESXi 系统 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Cicada3301 勒索软件的 Linux 加密器针对 VMware ESXi 系统

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-09-04 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)102517

收藏

导语：Cicada3301 RaaS 已于 2024 年 6 月 在勒索软件和网络犯罪论坛 RAMP 的论坛帖子中首次开始推广该行动并招募会员。

一个名为 Cicada3301 的新勒索软件即服务 (RaaS) 行动迅速在全球发起了网络攻击，已在其勒索门户网站上列出了 19 名受害者。

这项新的网络犯罪行动以游戏命名，该游戏涉及复杂的加密谜题，并使用相同的徽标在网络犯罪论坛上进行推广。然而，其实两者之间没有任何联系。

Cicada3301 RaaS 已于 2024 年 6 月 在勒索软件和网络犯罪论坛 RAMP 的论坛帖子中首次开始推广该行动并招募会员。

然而，外媒早已注意到 Cicada 攻击，这表明该团伙在试图招募分支机构之前是独立运作的。

![cicada3301-forum.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240902/1725265016149713.png "1725263228962101.png")

Cicada3301 勒索软件运营商在 RAMP 论坛上寻找附属机构

与其他勒索软件操作一样，Cicada3301 采取双重勒索策略，即入侵公司网络、窃取数据，然后加密设备。然后利用加密密钥和泄露被盗数据的威胁作为手段，恐吓受害者支付赎金。

威胁者运营一个数据泄露网站，将其用作双重勒索计划的一部分。

![cicada3301-site.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240902/1725265017169974.png "1725263273130882.png")

Cicada3301 勒索门户

Truesec 对新恶意软件的分析显示，Cicada3301 与 ALPHV/BlackCat 之间存在显著的重叠，表明可能是由前 ALPHV 核心团队成员创建的品牌重塑或分叉。

这是基于以下事实：

**·**两者都是用 Rust 编写的。

**·**两者都使用 ChaCha20 算法进行加密。

**·**两者都使用相同的 VM 关闭和快照擦除命令。

**·**两者都使用相同的用户界面命令参数、相同的文件命名约定和相同的勒索信解密方法。

**·**两者都对较大的文件使用间歇性加密。

具体来说，ALPHV 在 2024 年 3 月初实施了一次退出骗局，涉及虚假声称 FBI 正在进行的打击行动，此前他们从 Change Healthcare 的一家附属公司窃取了 2200 万美元的巨额付款。

Truesec 还发现有迹象表明，Cicada3301 勒索软件行动可能与 Brutus 僵尸网络合作或利用该网络对企业网络进行初始访问。该僵尸网络之前曾与针对思科、Fortinet、Palo Alto 和 SonicWall 设备的全球规模 VPN 暴力破解活动有关。

值得注意的是，Brutus 活动是在 ALPHV 关闭运营两周后首次发现的，因此从时间线来看，这两个组织之间的联系仍然存在。

**VMware ESXi 面临另一个威胁**

Cicada3301 是一款基于 Rust 的勒索软件，同时具有 Windows 和 Linux/VMware ESXi 加密器。作为 Truesec 报告的一部分，研究人员分析了勒索软件操作的 VMWare ESXi Linux 加密器。

与 BlackCat 和其他勒索软件系列（如 RansomHub）一样，必须输入特殊密钥作为命令行参数才能启动加密器。此密钥用于解密加密的 JSON blob，其中包含加密器在加密设备时将使用的配置。

Truesec 表示，加密器会使用密钥解密勒索信来检查密钥的有效性，如果成功，则继续执行其余的加密操作。

其主要功能（linux\_enc）使用 ChaCha20 流密码进行文件加密，然后使用 RSA 密钥加密过程中使用的对称密钥。加密密钥是使用“OsRng”函数随机生成的。

Cicada3301 针对与文档和媒体文件匹配的特定文件扩展名，并检查其大小以确定在哪里应用间歇性加密（> 100MB）以及在哪里加密整个文件内容（<100MB）。

在加密文件时，加密器会在文件名后附加一个随机的七个字符的扩展名，并创建名为“RECOVER-[扩展名]-DATA.txt”的勒索信，如下所示。

值得注意的是，BlackCat/ALPHV 加密器也使用了随机的七个字符的扩展名和名为“RECOVER-[扩展名]-FILES.txt”的勒索信。

![ransom-note.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240902/1725265018187265.png "1725263441153718.png")

Cicada3301 勒索信

勒索软件的操作员可以设置休眠参数来延迟加密器的执行，从而可能逃避立即检测。“no\_vm\_ss”参数还命令恶意软件加密 VMware ESXi 虚拟机而不尝试先关闭它们。

但是，默认情况下，Cicada3301 首先使用 ESXi 的“esxcli”和“vim-cmd”命令关闭虚拟机并删除其快照，然后再加密数据。

```
esxcli –formatter=csv –format-param=fields==\”WorldID,DisplayName\” vm process list | grep -viE \”,(),\” | awk -F \”\\\”*,\\\”*\” \'{system(\”esxcli vm process kill –type=force –world-id=\”$1)}\’ > /dev/null 2>&1;

for i in `vim-cmd vmsvc/getallvms| awk \'{print$1}\’`;do vim-cmd vmsvc/snapshot.removeall $i & done > /dev/null 2>&1
```

Cicada3301 的成功率表明攻击者经验丰富，且目的明确清晰。这进一步支持了 ALPHV 重启的假设，或者至少利用了具有勒索软件经验的关联方。

新勒索软件专注于 ESXi 环境，凸显了其战略设计，旨在最大限度地破坏企业环境，而许多威胁者现在将企业环境作为获利目标。

Cicada3301 将文件加密与破坏虚拟机操作和删除恢复选项的能力相结合，确保可以发起影响整个网络和基础设施的高影响力攻击，从而最大限度地给受害者施加压力。

文章翻译自：https://www.bleepingcomputer.com/news/security/cicada3301-ransomwares-linux-encryptor-targets-vmware-esxi-systems/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?CTbIcw73)

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