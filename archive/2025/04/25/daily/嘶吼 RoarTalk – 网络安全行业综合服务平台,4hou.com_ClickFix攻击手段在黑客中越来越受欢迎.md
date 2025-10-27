---
title: ClickFix攻击手段在黑客中越来越受欢迎
url: https://www.4hou.com/posts/jBNv
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-25
fetch_date: 2025-10-06T22:03:13.734360
---

# ClickFix攻击手段在黑客中越来越受欢迎

ClickFix攻击手段在黑客中越来越受欢迎 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ClickFix攻击手段在黑客中越来越受欢迎

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-04-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)54882

收藏

导语：ClickFix是一种社会工程策略，恶意网站冒充合法软件或文档共享平台。目标是通过网络钓鱼或恶意广告引诱，并显示虚假的错误信息，声称文件或下载失败。

ClickFix攻击在威胁分子中越来越受欢迎，来自朝鲜、伊朗和俄罗斯的多个高级持续威胁（APT）组织在最近的间谍活动中采用了这种技术。

ClickFix是一种社会工程策略，恶意网站冒充合法软件或文档共享平台。目标是通过网络钓鱼或恶意广告引诱，并显示虚假的错误信息，声称文件或下载失败。

然后，受害者被提示点击“修复”按钮，该按钮指示他们运行PowerShell或命令行脚本，从而在他们的设备上执行恶意软件。

微软威胁情报团队去年2月报告称，朝鲜黑客“Kimsuky”也将其用作虚假“设备注册”网页的一部分。

![admin-exec.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745219507606261.png "1745216139208454.png")

点击修复假设备注册页面

来自Proofpoint的一份最新报告显示，在2024年底到2025年初之间，Kimsuky（朝鲜）、MuddyWater（伊朗）以及APT28和UNK\_RemoteRogue（俄罗斯）都在他们的目标间谍活动中使用了ClickFix。

![timeline.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745219508847032.png "1745216190143883.png")

ClickFix攻击的时间轴

**ClickFix启用智能操作**

从Kimsuky开始，攻击发生在2025年1月至2月，目标是专注于朝鲜相关政策的智库。朝鲜黑客利用欺骗的韩语、日语或英语电子邮件，假装发件人是日本外交官，以启动与目标的联系。

在建立信任之后，攻击者发送了一个恶意的PDF文件，链接到一个假的安全驱动器，提示目标通过手动复制PowerShell命令到他们的终端来“注册”。

这样做会获取第二个脚本，该脚本为持久化设置计划任务并下载QuasarRAT，同时向受害者显示一个诱饵PDF以进行转移。

![quasar.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745219508515313.png "1745216310725156.png")

Kimsuky攻击流

MuddyWater攻击发生在2024年11月中旬，以伪装成微软安全警报的电子邮件攻击了中东的39家组织。

收件人被告知，他们需要通过在计算机上以管理员身份运行PowerShell来应用关键的安全更新。这导致了“Level”的自我感染，这是一种可以促进间谍活动的远程监控和管理（RMM）工具。

![muddywater.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745219509109611.png "1745216348623122.png")

MuddyWater收件

第三个案例涉及俄罗斯威胁组织UNK\_RemoteRogue，该组织于2024年12月针对与一家主要武器制造商密切相关的两个组织。

这些恶意邮件是从Zimbra服务器上发送的，欺骗了微软办公软件。点击嵌入的链接，目标就会进入一个假的微软Word页面，上面有俄语说明和YouTube视频教程。

运行代码执行的JavaScript启动了PowerShell，从而连接到运行Empire命令和控制（C2）框架的服务器。

![document.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250421/1745219509618151.png "1745216484171061.png")

登陆页欺骗Word文档

Proofpoint报告称，早在2024年10月，GRU单位APT28也使用了ClickFix，使用仿冒谷歌电子表格、reCAPTCHA步骤和通过弹出窗口传达的PowerShell执行指令的网络钓鱼邮件。

运行这些命令的受害者在不知情的情况下建立了SSH隧道并启动了Metasploit，为攻击者提供了访问其系统的后门。

ClickFix仍然是一种有效的方法，因为缺乏对未经请求的命令执行的意识，仍被多个黑客组织采用。

文章翻译自：https://www.bleepingcomputer.com/news/security/state-sponsored-hackers-embrace-clickfix-social-engineering-tactic/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?qXWUS4Qv)

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