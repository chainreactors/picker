---
title: vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码
url: https://www.4hou.com/posts/qoOk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-02
fetch_date: 2026-02-03T04:08:57.450284
---

# vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码

vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)5237

收藏

导语：根源在于vm2库未能对处理异步操作的Promise组件实现完善的沙箱隔离，导致无法确保代码始终在独立的隔离环境中执行。

近日，Node.js沙箱库vm2曝出一个高危漏洞（CVE-2026-22709），攻击者可利用该漏洞突破沙箱限制，在底层主机系统上执行任意代码。

这款开源的vm2库能够创建安全执行环境，支持用户运行不受信任的JavaScript代码，且限制其访问文件系统，是实现代码隔离执行的常用工具。

vm2历来被广泛应用于支持用户脚本执行的SaaS平台、在线代码运行工具、聊天机器人及各类开源项目中，仅在GitHub平台上，使用该库的项目就超20万个。不过因沙箱逃逸漏洞频发，该项目曾在2023年停止维护，且被判定为不适用于运行不受信任的代码。

去年10月，项目维护者决定重启vm2项目，并发布3.10.0版本，该版本修复了当时已知的所有漏洞，同时保持“向下兼容至Node 6版本”的特性。

目前该库在npm平台上依旧拥有极高的人气，过去一年间，其周下载量稳定在100万次左右。

**漏洞根源：数据清理机制存在疏漏**

此次曝出的最新漏洞，根源在于vm2库未能对处理异步操作的Promise组件实现完善的沙箱隔离，导致无法确保代码始终在独立的隔离环境中执行。

vm2虽会对其自身内置Promise实现所绑定的回调函数做数据清理处理，但异步函数返回的是全局Promise对象，该对象的.then()和.catch()回调函数并未得到妥善的清理校验。

项目维护者表示：“在vm2 3.10.0版本中，Promise.prototype.then和Promise.prototype.catch的回调函数清理机制可被绕过”，而这一漏洞“会让攻击者得以突破沙箱限制，运行任意代码”。

据开发者介绍，vm2 3.10.1版本已对该CVE-2026-22709沙箱逃逸漏洞做出部分修复，后续推出的3.10.2版本则进一步强化了修复措施，避免漏洞被再次绕过。

同时开发者还公开了相关演示代码，展示了攻击者如何在vm2沙箱中触发该漏洞、实现沙箱逃逸，并在主机系统上执行命令。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260129/1769670749129469.png "1769670474435277.png")

已发布的漏洞利用片段

鉴于在受影响的vm2版本中，CVE-2026-22709漏洞的利用方式极为简易，官方建议所有用户尽快将库版本升级至最新版。

**历史漏洞：沙箱逃逸问题屡发**

vm2此前也曾多次曝出高危沙箱逃逸漏洞，其中包括被披露的CVE-2022-36067，攻击者利用该漏洞可突破隔离环境，在主机系统上执行命令。

2023年4月，研究人员发现另一同类漏洞（CVE-2023-29017），且相关利用程序随即被公开；同月晚些时候，研究人员又发布了CVE-2023-30547漏洞的利用程序，这也是影响vm2的又一个高危沙箱逃逸漏洞。

其开发者表示，目前vm2的最新版本为3.10.3，所有已披露的漏洞均在该版本中得到妥善修复。

文章来源自：https://www.bleepingcomputer.com/news/security/critical-sandbox-escape-flaw-discovered-in-popular-vm2-nodejs-library/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?uODpmIqK)

#### 你可能感兴趣的

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
* [![]()

  CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)
  2026-02-02 12:43:48
* [黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报](https://www.4hou.com/posts/XPgo)
  2026-01-30 11:59:00
* [CSTIS：关于防范MuddyWater组织网络攻击的风险提示](https://www.4hou.com/posts/8gpW)
  2026-01-26 11:42:29
* [严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听](https://www.4hou.com/posts/J14v)
  2026-01-22 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

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
* [CVE-2026-20824漏洞：Windows远程协助存在安全功能绕过风险](https://www.4hou.com/posts/EyY4)

  山卡拉

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