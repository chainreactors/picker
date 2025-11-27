---
title: 微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃
url: https://www.4hou.com/posts/QX9q
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-26
fetch_date: 2025-11-27T03:10:29.534970
---

# 微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃

微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/loginIng)
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

# 微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7303

收藏

导语：该漏洞对采用虚拟桌面基础架构管理非持久性企业环境的机构影响尤为严重。

微软已确认Windows 11 24H2版本存在一处高危漏洞：自2025年7月起发布的累计更新在系统部署过程中，会导致文件资源管理器、开始菜单及其他关键系统组件崩溃。

该漏洞的触发场景包括两种：一是“安装累计更新后的首次用户登录”；二是使用非持久性操作系统安装环境（如虚拟桌面基础架构环境）的用户每次登录时——此类环境中应用包需在每个会话周期重新安装。在受影响的系统中，更新后XAML依赖包无法正常注册，进而导致Windows 11多个核心外壳组件出现故障。

微软在近期发布的支持文档中解释称，依赖XAML包（具体为MicrosoftWindows.Client.CBS、Microsoft.UI.Xaml.CBS和MicrosoftWindows.Client.Core）的应用程序，在更新安装后未能及时完成注册。这一计时同步问题会在系统中连锁扩散，导致关键界面组件无法正常初始化。

最终造成Explorer.exe（文件资源管理器进程）、StartMenuExperienceHost（开始菜单体验主机进程）、ShellHost.exe（外壳主机进程）等外壳组件出现显性错误崩溃或隐性运行失败，用户系统将陷入部分功能失效状态，无法正常显示各类导航工具。

受影响用户可能遭遇多种问题，包括：开始菜单崩溃（常伴随严重错误提示）、文件资源管理器运行时任务栏缺失、核心ShellHost进程（外壳基础结构主机或Windows外壳体验主机）崩溃、设置应用静默启动失败等。

微软表示：“在部署了2025年7月及之后发布的Windows 11 24H2月度累计更新（KB5062553及后续版本）后，开始菜单体验主机、搜索、系统设置、任务栏或文件资源管理器等多个应用可能出现运行异常。”

**提供临时解决方案**

微软称目前正推进修复方案开发，但尚未给出具体修复时间线。在永久性补丁发布前，微软提供了通过PowerShell命令手动注册缺失包的临时解决方法。

受影响用户需执行以下三条Add-AppxPackage命令（分别针对每个受影响的XAML包），随后重启系统即可恢复功能：

 Add-AppxPackage -Register -Path 'C:\Windows\SystemApps\MicrosoftWindows.Client.CBS\_cw5n1h2txyewy\appxmanifest.xml' -DisableDevelopmentMode
Add-AppxPackage -Register -Path 'C:\Windows\SystemApps\Microsoft.UI.Xaml.CBS\_8wekyb3d8bbwe\appxmanifest.xml' -DisableDevelopmentMode
Add-AppxPackage -Register -Path 'C:\Windows\SystemApps\MicrosoftWindows.Client.Core\_cw5n1h2txyewy\appxmanifest.xml' -DisableDevelopmentMode

然而，该漏洞对采用虚拟桌面基础架构管理非持久性企业环境的机构影响尤为严重——此类环境中员工每次登录都需重新部署应用程序。

对此，微软建议在非持久性操作系统安装环境中部署登录脚本，确保该脚本在文件资源管理器启动前执行。该批处理文件包装器可保证桌面环境加载前所需包已完全部署，从而避免计时竞争条件引发的故障。

上周，英伟达也发布了GeForce热修复显示驱动程序，以解决2025年10月Windows 11累计更新（KB5066835）引发的游戏性能问题；与此同时，微软发布了带外紧急更新，修复了扩展安全更新（ESU）安装错误及Windows 11热补丁安装循环问题。

文章翻译自：https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-11-24h2-bug-crashes-key-system-components/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?vn7igE6T)

#### 你可能感兴趣的

* [![]()

  微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)
* [![]()

  Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)
* [![]()

  ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)
* [![]()

  高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)
* [![]()

  Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)
* [![]()

  Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)
  2025-11-26 12:01:00
* [Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)
  2025-11-26 12:00:00
* [ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)
  2025-11-21 12:00:00
* [高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)
  2025-11-19 11:10:33

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [微软：Windows 11 24H2 高危漏洞导致文件资源管理器等核心组件崩溃](https://www.4hou.com/posts/QX9q)

  胡金鱼
* [Grafana ：最高级别漏洞可实现管理员身份冒充](https://www.4hou.com/posts/W13X)

  胡金鱼
* [ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)

  胡金鱼
* [高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)

  胡金鱼
* [Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)

  胡金鱼
* [Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)

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