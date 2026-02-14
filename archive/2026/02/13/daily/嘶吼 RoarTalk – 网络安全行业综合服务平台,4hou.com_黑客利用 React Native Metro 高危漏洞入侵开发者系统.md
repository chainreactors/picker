---
title: 黑客利用 React Native Metro 高危漏洞入侵开发者系统
url: https://www.4hou.com/posts/DxG5
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-13
fetch_date: 2026-02-14T04:07:13.275587
---

# 黑客利用 React Native Metro 高危漏洞入侵开发者系统

黑客利用 React Native Metro 高危漏洞入侵开发者系统 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用 React Native Metro 高危漏洞入侵开发者系统

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2026-02-13 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10477

收藏

导语：该漏洞的根源在于Metro服务器的/open-url HTTP端点会接收POST请求中用户提交的URL参数，且该参数未经任何安全清理，便直接传递给系统的open()函数执行。

黑客正针对开发者群体发起攻击，其手段是利用React Native框架Metro服务器中编号为CVE-2025-11953的高危漏洞，向Windows与Linux系统投放恶意载荷。

在Windows系统环境下，未授权攻击者可借助该漏洞，通过发送POST请求执行任意操作系统命令；而在Linux和macOS系统中，该漏洞则可能导致攻击者在有限参数控制的前提下，运行任意可执行文件。

Metro是React Native项目的默认JavaScript打包工具，是应用开发阶段构建和运行程序的核心组件。

默认情况下，Metro会绑定外部网络接口，并开放仅供开发调试使用的HTTP端点（/open-url），以满足本地开发需求。

研究人员发现了这一漏洞，并于去年11月初对外披露。漏洞公开后，多个概念验证（PoC）利用程序随即出现。

据悉，该漏洞的根源在于Metro服务器的/open-url HTTP端点会接收POST请求中用户提交的URL参数，且该参数未经任何安全清理，便直接传递给系统的open()函数执行。

该漏洞影响范围覆盖@react-native-community/cli-server-api工具的4.8.0至20.0.0-alpha.2版本，官方已在20.0.0及后续版本中完成漏洞修复。

2025年12月21日，有威胁者开始利用这一漏洞发起攻击，该攻击活动被命名为Metro4Shell。此后在次年1月4日和21日，攻击者仍在通过该漏洞投放相同的恶意载荷。

攻击者已通过该漏洞在Linux和Windows平台成功投递高级恶意载荷，这表明Metro4Shell已成为一种切实可行的跨平台初始访问手段。

研究人员发现，在这三次攻击中，攻击者均将经过Base64编码的PowerShell恶意载荷隐藏在恶意请求的HTTP POST请求体中，发送至暴露在外的Metro服务器端点。

这些载荷解码并启动后，会执行以下一系列恶意操作：

1.禁用终端防护：调用Add-MpPreference命令，将当前工作目录和系统临时目录添加至微软 Defender 的排除路径，躲避查杀；

2.获取后续载荷：与攻击者控制的服务器建立原始TCP连接，发送GET /windows请求以获取下一阶段的恶意程序；

3.写入恶意文件：将接收的数据写入系统临时目录，保存为可执行文件；

4.执行恶意程序：运行下载的二进制文件，并附带一段由攻击者指定的超长参数字符串。

此次攻击中投放的Windows平台载荷，是一个基于Rust语言开发、经UPX加壳处理的二进制文件，内置基础反分析逻辑。攻击者控制的同一服务器中，还存放有对应的Linux平台恶意程序，可见该攻击活动同时覆盖两大主流操作系统。

据扫描数据显示，目前暴露在公网环境中的React Native Metro服务器约有3500台。 尽管该漏洞已被攻击者持续利用超过一个月，但在漏洞利用预测评分系统中，其风险评分仍处于较低水平。

研究人员强调：“企业切不可等待该漏洞被列入CISA已知被利用漏洞目录、厂商发布相关通报或行业形成广泛共识后，才采取防护措施。”

文章来源自：https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-react-native-metro-bug-to-breach-dev-systems/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?sUArtTGB)

#### 你可能感兴趣的

* [![]()

  黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)
* [![]()

  vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)
* [![]()

  黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报](https://www.4hou.com/posts/XPgo)
* [![]()

  CSTIS：关于防范MuddyWater组织网络攻击的风险提示](https://www.4hou.com/posts/8gpW)
* [![]()

  严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听](https://www.4hou.com/posts/J14v)
* [![]()

  GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库](https://www.4hou.com/posts/nl2Y)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)
  2026-02-13 12:00:00
* [vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)
  2026-02-02 12:43:48
* [黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报](https://www.4hou.com/posts/XPgo)
  2026-01-30 11:59:00
* [CSTIS：关于防范MuddyWater组织网络攻击的风险提示](https://www.4hou.com/posts/8gpW)
  2026-01-26 11:42:29

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)

  胡金鱼
* [vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)

  胡金鱼
* [黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报](https://www.4hou.com/posts/XPgo)

  胡金鱼
* [CSTIS：关于防范MuddyWater组织网络攻击的风险提示](https://www.4hou.com/posts/8gpW)

  胡金鱼
* [严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听](https://www.4hou.com/posts/J14v)

  胡金鱼
* [GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库](https://www.4hou.com/posts/nl2Y)

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