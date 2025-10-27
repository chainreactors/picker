---
title: Windows 在新的网络钓鱼攻击中感染了后门 Linux 虚拟机
url: https://www.4hou.com/posts/rpMk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-03
fetch_date: 2025-10-06T19:34:58.027389
---

# Windows 在新的网络钓鱼攻击中感染了后门 Linux 虚拟机

Windows 在新的网络钓鱼攻击中感染了后门 Linux 虚拟机 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Windows 在新的网络钓鱼攻击中感染了后门 Linux 虚拟机

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-12-02 14:44:41

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)101044

收藏

导语：Securonix 研究人员发现的一项新活动是使用网络钓鱼电子邮件执行无人值守的 Linux 虚拟机安装，以破坏企业网络并获得持久性。

一种名为“CRON#TRAP”的新网络钓鱼活动通过 Linux 虚拟机感染 Windows，该虚拟机包含内置后门，可以秘密访问公司网络。

使用虚拟机进行攻击并不是什么新鲜事，勒索软件团伙和加密货币挖矿者利用虚拟机来秘密执行恶意活动。然而，威胁者通常在破坏网络后手动安装这些软件。

Securonix 研究人员发现的一项新活动是使用网络钓鱼电子邮件执行无人值守的 Linux 虚拟机安装，以破坏企业网络并获得持久性。

网络钓鱼电子邮件伪装成“OneAmerica 调查”，其中包含一个 285MB 的大型 ZIP 存档，用于安装预装后门的 Linux 虚拟机。

该 ZIP 文件包含一个名为“OneAmerica Survey.lnk”的 Windows 快捷方式和一个包含 QEMU 虚拟机应用程序的“data”文件夹，其中主要可执行文件伪装为 fontdiag.exe。

启动快捷方式时，它会执行 PowerShell 命令将下载的存档解压到“%UserProfile%\datax”文件夹，然后启动“start.bat”以在设备上设置并启动自定义 QEMU Linux 虚拟机。

![cron-trap.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241105/1730794968157681.png "1730794799171519.png")

Start.bat批处理文件安装QEMU Linux虚拟机

安装虚拟机时，同一个批处理文件将显示从远程站点下载的 PNG 文件，该文件显示虚假服务器错误作为诱饵，这意味着调查链接已损坏。

![error.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241105/1730794969662993.png "1730794828156005.png")

显示假错误的图像

名为“PivotBox”的定制 TinyCore Linux VM 预装了一个后门，可保护持久的 C2 通信，允许攻击者在后台进行操作。

由于 QEMU 是一个经过数字签名的合法工具，因此 Windows 不会对其运行发出任何警报，并且安全工具无法检查虚拟机内运行的恶意程序。

![lnk-contents.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241105/1730794970994079.png "1730794875323638.png")

LNK 文件内容

**后门操作**

后门的核心是一个名为 Chisel 的工具，这是一个网络隧道程序，经过预先配置，可通过 WebSockets 与特定命令和控制 (C2) 服务器创建安全通信通道。

Chisel 通过 HTTP 和 SSH 传输数据，允许攻击者与受感染主机上的后门进行通信，即使防火墙保护网络也是如此。

为了持久性，QEMU 环境设置为在主机通过“bootlocal.sh”修改重新引导后自动启动。同时，会生成并上传 SSH 密钥，以避免重新进行身份验证。

Securonix 突出显示了两个命令，即“get-host-shell”和“get-host-user”。第一个在主机上生成一个交互式 shell，允许执行命令，而第二个用于确定权限。

然后可以执行的命令包括监视、网络和有效负载管理操作、文件管理和数据泄露操作，因此攻击者拥有一组多功能的命令，使他们能够适应目标并执行破坏性操作。

![ash.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241105/1730794971140620.png "1730794943174407.png")

恶意分子的命令历史记录

**防御 QEMU 滥用**

CRON#TRAP 活动并不是黑客第一次滥用 QEMU 与其 C2 服务器建立秘密通信。

2024 年 3 月，卡巴斯基报告了另一场活动，威胁者使用 QEMU 创建虚拟网络接口和套接字类型网络设备来连接到远程服务器。

在这种情况下，隐藏在仅运行 1MB RAM 的 Kali Linux 虚拟机内的一个非常轻的后门被用来建立一个隐蔽的通信隧道。

要检测和阻止这些攻击，请考虑为从用户可访问的文件夹执行的“qemu.exe”等进程放置监视器，将 QEMU 和其他虚拟化套件放入阻止列表中，并从系统 BIOS 禁用或阻止关键设备上的虚拟化。

文章翻译自：https://www.bleepingcomputer.com/news/security/windows-infected-with-backdoored-linux-vms-in-new-phishing-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?TBKsD6Ps)

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