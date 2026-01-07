---
title: 仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染
url: https://www.4hou.com/posts/NGMm
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-06
fetch_date: 2026-01-07T03:28:58.836553
---

# 仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染

仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8174

收藏

导语：MAS项目维护者已针对此次攻击事件发出安全预警，提醒用户在执行命令前仔细核对输入内容。

攻击者利用仿冒“微软激活脚本（MAS）”的拼写错误域名，分发恶意PowerShell脚本，使Windows系统感染Cosmali Loader恶意软件。

安全研究员发现，有多名MAS工具用户在Reddit平台反馈，其设备弹出Cosmali Loader感染预警提示。根据用户报告，攻击者搭建了仿冒域名“get.activate[.]win”，该域名与MAS官方激活指南中列出的合法域名“get.activated.win”高度相似。两个域名仅相差一个字符（合法域名多一个“d”），攻击者正是利用用户可能出现的输入失误实施攻击。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260106/1767666034141517.png "1766992414954875.png")

警告信息

安全研究员证实，这些预警提示与开源恶意软件Cosmali Loader相关，且可能与GDATA恶意软件分析师Karsten Hahn此前发现的类似弹窗预警同源。

Cosmali Loader会投放加密挖矿工具与XWorm远程控制木马。目前尚不清楚是谁向用户推送了预警信息，但大概率是研究员获取了该恶意软件的控制面板权限后，通过弹窗告知用户设备已遭入侵。

微软激活脚本（MAS）是一套开源PowerShell脚本集合，通过硬件ID（HWID）激活、KMS模拟及多种绕过技术（如Ohook、TSforge），实现微软Windows系统与Office办公软件的自动化激活。

该项目托管于GitHub平台，由开发者公开维护，但微软将其认定为盗版工具——因其通过未授权方式规避许可验证系统，无需购买正版授权即可激活产品。

MAS项目维护者已针对此次攻击事件发出安全预警，提醒用户在执行命令前仔细核对输入内容。同时建议用户若未完全理解远程代码的功能，切勿随意执行；尽量在沙箱环境中测试未知脚本；避免手动重复输入命令，以降低因访问拼写错误域名而加载危险载荷的风险。

需注意的是，非官方Windows激活工具已多次被用于传播恶意软件，用户使用此类工具时需充分认识潜在风险，保持高度警惕。

文章来源自：https://www.bleepingcomputer.com/news/security/fake-mas-windows-activation-domain-used-to-spread-powershell-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?B9Ze7FBN)

#### 你可能感兴趣的

* [![]()

  仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染](https://www.4hou.com/posts/NGMm)
* [![]()

  Chrome 应用商店恶意扩展程序窃取用户敏感数据](https://www.4hou.com/posts/J109)
* [![]()

  《彩虹六号：围攻》重大黑客入侵事件致无数玩家获赠数十亿游戏币](https://www.4hou.com/posts/MXLP)
* [![]()

  新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)
* [![]()

  国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/LGKp)
* [![]()

  RansomHouse完成加密工具升级：采用多层数据处理技术](https://www.4hou.com/posts/kgAr)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染](https://www.4hou.com/posts/NGMm)
  2026-01-06 12:00:00
* [Chrome 应用商店恶意扩展程序窃取用户敏感数据](https://www.4hou.com/posts/J109)
  2026-01-05 12:00:00
* [《彩虹六号：围攻》重大黑客入侵事件致无数玩家获赠数十亿游戏币](https://www.4hou.com/posts/MXLP)
  2025-12-30 12:00:00
* [新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)
  2025-12-29 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [仿冒微软激活工具域名暗藏恶意脚本致Windows设备感染](https://www.4hou.com/posts/NGMm)

  胡金鱼
* [Chrome 应用商店恶意扩展程序窃取用户敏感数据](https://www.4hou.com/posts/J109)

  胡金鱼
* [《彩虹六号：围攻》重大黑客入侵事件致无数玩家获赠数十亿游戏币](https://www.4hou.com/posts/MXLP)

  胡金鱼
* [新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)

  胡金鱼
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/LGKp)

  胡金鱼
* [RansomHouse完成加密工具升级：采用多层数据处理技术](https://www.4hou.com/posts/kgAr)

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