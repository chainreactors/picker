---
title: 新型CrystalRAT恶意软件新增远程控制、数据窃取等功能
url: https://www.4hou.com/posts/LGMD
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-04-09
fetch_date: 2026-04-10T04:44:51.651009
---

# 新型CrystalRAT恶意软件新增远程控制、数据窃取等功能

新型CrystalRAT恶意软件新增远程控制、数据窃取等功能 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型CrystalRAT恶意软件新增远程控制、数据窃取等功能

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-04-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9711

收藏

导语：这款木马与WebRAT高度相似，二者拥有相同的控制面板设计、均使用Go语言编写，且采用类似的机器人销售系统。

一款名为CrystalRAT的新型远程控制木马正在Telegram上以恶意软件即服务（MaaS）模式推广，提供远程控制、数据窃取、键盘记录与剪贴板劫持等核心功能。

该恶意软件于今年1月现身，采用分级订阅模式运营。除Telegram频道外，运营者还在YouTube开设专门营销账号，通过功能演示视频进行推广。

卡巴斯基研究人员在最近发布的报告中指出，这款木马与WebRAT（Salat窃密木马）高度相似，二者拥有相同的控制面板设计、均使用Go语言编写，且采用类似的机器人销售系统。

CrystalX还内置了大量恶作剧功能，用于骚扰用户或干扰其正常工作。尽管带有“娱乐化”外观，该木马仍具备全面且强大的数据窃取能力。

![图片68.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260403/1775202525188586.png "1775202525188586.png")

Telegram频道推广CrystaX RAT

**CrystalX RAT功能详情**

卡巴斯基表示，该恶意软件配备了易用的管理后台与自动化生成工具，支持多项自定义配置，包括地域限制、可执行文件定制，以及反调试、虚拟机检测、代理检测等反分析防护能力。

生成的恶意载荷会经过zlib压缩，并使用ChaCha20对称流加密算法进行保护。

木马通过WebSocket协议连接指挥控制服务器（C2），并上传主机信息用于设备画像与感染追踪。

CrystalX的窃密模块目前处于临时禁用状态，官方称正在进行升级。该模块主要针对基于Chromium内核的浏览器（借助ChromeElevator工具）、Yandex浏览器与Opera浏览器，同时还会窃取Steam、Discord、Telegram等桌面应用中的数据。

远程控制模块支持通过CMD执行命令、上传与下载文件、浏览文件系统，并通过内置VNC实现对主机的实时操控。

该木马还具备典型间谍软件行为，可调用麦克风录制音频、抓取屏幕画面。

此外，CrystalX内置键盘记录器，可将按键记录实时回传至服务器；同时搭载剪贴板篡改工具，通过正则表达式识别钱包地址，并替换为攻击者指定的地址。

![图片69.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260403/1775202555177900.png "1775202555177900.png")

CrystalX RAT控制面板中的远程桌面功能

**附加“恶作剧”功能**

在竞争激烈的恶意软件即服务市场中，CrystalX的独特之处在于其丰富的恶作剧功能。

据分析，该木马可在受感染设备上执行以下操作：

**·**修改桌面壁纸

**·**旋转屏幕显示方向

**·**强制关机

**·**重映射鼠标按键

**·**禁用键盘、鼠标、显示器等输入输出设备

**·**弹出伪造系统通知

**·**自动移动鼠标光标

**·**隐藏桌面图标、任务栏、任务管理器、命令提示符等系统组件

**·**开启攻击者与受害者的聊天窗口

尽管上述功能无法直接提升黑产牟利效率，但能让该工具在同类产品中脱颖而出，吸引初级攻击者订阅使用。

研究人员认为，加入此类恶作剧功能的另一目的，是在后台窃取数据的同时干扰、迷惑受害者，降低其警觉性。为降低感染风险，用户应谨慎对待网络内容，避免从不信任或非官方来源下载软件与媒体文件。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-crystalrat-malware-adds-rat-stealer-and-prankware-features/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?tE5yTiEm)

#### 你可能感兴趣的

* [![]()

  Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行](https://www.4hou.com/posts/MXOm)
* [![]()

  嘶吼安全动态|八部门联合发布《 科技数据安全管理暂行规定》，4月10日起实施 黑客利用像素级SVG技巧隐藏信用卡窃密代码](https://www.4hou.com/posts/8gPj)
* [![]()

  新型CrystalRAT恶意软件新增远程控制、数据窃取等功能](https://www.4hou.com/posts/LGMD)
* [![]()

  嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散](https://www.4hou.com/posts/6MLO)
* [![]()

  Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马](https://www.4hou.com/posts/J1GK)
* [![]()

  嘶吼安全动态｜国家安全部提醒：“囤词元暴富” 背后，暗藏间谍窃取数据陷阱 苹果Mac威胁50.32%来自木马，盗窃用户隐私成主要目的](https://www.4hou.com/posts/YZoA)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行](https://www.4hou.com/posts/MXOm)
  2026-04-10 12:00:00
* [嘶吼安全动态|八部门联合发布《 科技数据安全管理暂行规定》，4月10日起实施 黑客利用像素级SVG技巧隐藏信用卡窃密代码](https://www.4hou.com/posts/8gPj)
  2026-04-10 11:59:00
* [新型CrystalRAT恶意软件新增远程控制、数据窃取等功能](https://www.4hou.com/posts/LGMD)
  2026-04-09 12:00:00
* [嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散](https://www.4hou.com/posts/6MLO)
  2026-04-09 11:59:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行](https://www.4hou.com/posts/MXOm)

  胡金鱼
* [嘶吼安全动态|八部门联合发布《 科技数据安全管理暂行规定》，4月10日起实施 黑客利用像素级SVG技巧隐藏信用卡窃密代码](https://www.4hou.com/posts/8gPj)

  胡金鱼
* [新型CrystalRAT恶意软件新增远程控制、数据窃取等功能](https://www.4hou.com/posts/LGMD)

  胡金鱼
* [嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散](https://www.4hou.com/posts/6MLO)

  胡金鱼
* [Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马](https://www.4hou.com/posts/J1GK)

  胡金鱼
* [嘶吼安全动态｜国家安全部提醒：“囤词元暴富” 背后，暗藏间谍窃取数据陷阱 苹果Mac威胁50.32%来自木马，盗窃用户隐私成主要目的](https://www.4hou.com/posts/YZoA)

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