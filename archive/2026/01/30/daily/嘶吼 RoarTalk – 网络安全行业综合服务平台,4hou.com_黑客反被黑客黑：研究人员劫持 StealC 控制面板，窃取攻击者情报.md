---
title: 黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报
url: https://www.4hou.com/posts/XPgo
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-30
fetch_date: 2026-01-31T04:03:26.273396
---

# 黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报

黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2026-01-30 11:59:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9218

收藏

导语：CyberArk 指出，恶意软件即服务（MaaS）平台虽然能实现快速扩展，但也给威胁者带来了巨大的暴露风险。

StealC 信息窃取恶意软件运营商所使用的基于 Web 的控制面板中存在一个 跨站脚本（XSS）漏洞，该漏洞允许研究人员观察活跃会话，并收集攻击者的硬件情报。

StealC 于 2023 年初在暗网网络犯罪频道上通过激进推广而兴起。凭借其规避检测和广泛的数据窃取能力，它迅速流行起来。

在随后的几年里，StealC 的开发者不断进行多项增强。去年 4 月发布 2.0 版本时，恶意软件作者引入了 Telegram 机器人支持以实现实时警报，并推出了一个新的构建器，可基于模板和自定义数据窃取规则生成 StealC 样本。

大约在同一时间，该恶意软件管理面板的源代码被泄露，这为研究人员提供了分析机会。

CyberArk的研究人员发现了一个 XSS 漏洞，利用该漏洞，他们能够收集 StealC 运营商的浏览器和硬件指纹，观察活跃会话，窃取面板的会话 Cookie，并远程劫持面板会话。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260120/1768900856251134.png "1768900832139004.png")

The StealC 构建面板

为了防止 StealC 运营商迅速查明并修复该漏洞，CyberArk 未披露有关该 XSS 漏洞的具体技术细节。重点介绍了一位名为 “YouTubeTA”的 StealC 客户案例。该客户可能利用泄露的凭证劫持了旧的、合法的 YouTube 频道，并植入了感染链接。

这名网络犯罪分子在整个 2025 年期间运行恶意软件活动，收集了超过5,000 条受害者日志，窃取了约39 万个密码和3000 万个Cookie（其中大部分是非敏感的）。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260120/1768900860158423.png "1768900860158423.png")

YouTubeTA的标记页面

来自威胁者面板的截图显示，大多数感染发生在受害者搜索Adobe Photoshop和Adobe After Effects的破解版本时。

通过利用 XSS 漏洞，研究人员能够确定该攻击者使用的是基于Apple M3的系统，语言设置为英语和俄语，使用东欧时区，并通过乌克兰访问互联网。

当威胁者忘记通过 VPN 连接 StealC 面板时，其位置就会暴露，泄露了他们的真实 IP 地址，该地址与乌克兰 ISP TRK Cable TV相关联。

CyberArk 指出，恶意软件即服务（MaaS）平台虽然能实现快速扩展，但也给威胁者带来了巨大的暴露风险。

文章来源自：https://www.bleepingcomputer.com/news/security/stealc-hackers-hacked-as-researchers-hijack-malware-control-panels/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mCuxEsin)

#### 你可能感兴趣的

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
* [![]()

  HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报](https://www.4hou.com/posts/XPgo)
  2026-01-30 11:59:00
* [CSTIS：关于防范MuddyWater组织网络攻击的风险提示](https://www.4hou.com/posts/8gpW)
  2026-01-26 11:42:29
* [严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听](https://www.4hou.com/posts/J14v)
  2026-01-22 12:00:00
* [GoBruteforcer 僵尸网络新攻势：利用AI生成配置漏洞 瞄准加密货币数据库](https://www.4hou.com/posts/nl2Y)
  2026-01-19 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

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
* [HPE Aruba漏洞致敏感信息遭未授权访问](https://www.4hou.com/posts/DxX5)

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