---
title: 微软禁用 BitLocker 安全修复程序，建议手动缓解
url: https://www.4hou.com/posts/OGMN
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-21
fetch_date: 2025-10-06T18:01:02.839686
---

# 微软禁用 BitLocker 安全修复程序，建议手动缓解

微软禁用 BitLocker 安全修复程序，建议手动缓解 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 微软禁用 BitLocker 安全修复程序，建议手动缓解

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-08-20 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)82121

收藏

导语：禁用修复程序后，微软建议那些想要保护其系统和数据免受 CVE-2024-38058 攻击的用户应用 KB5025885 公告中详述的缓解措施。

由于固件不兼容问题导致已修补的 Windows 设备进入 BitLocker 恢复模式，Microsoft 已禁用针对 BitLocker 安全功能绕过漏洞的修复。

该漏洞被标记为 CVE-2024-38058，它可让攻击者绕过 BitLocker 设备加密功能，并通过物理访问目标设备来访问加密数据。

该公司在更新中解释道：“当客户将针对此漏洞的修复程序应用于他们的设备时，我们收到了有关固件不兼容问题的反馈，这些问题导致 BitLocker 在某些设备上进入恢复模式。因此，随着 2024 年 8 月安全更新的发布，我们将禁用此修复程序。”

禁用修复程序后，微软建议那些想要保护其系统和数据免受 CVE-2024-38058 攻击的用户应用 KB5025885 公告中详述的缓解措施。

但是，他们现在不必部署安全更新，而是必须经历一个 4 阶段的过程，该过程还需要重新启动受影响的设备八次。

此外，微软警告说，在具有安全启动功能的设备上应用缓解措施后，即使重新格式化磁盘，他们也无法再将其删除。

在设备上启用此问题的缓解措施后，即已应用缓解措施，如果用户继续在该设备上使用安全启动，则无法恢复。即使重新格式化磁盘也无法删除已应用的撤销。

在本月的补丁星期二，雷德蒙德还修复了 7 月 Windows 安全更新引发的一个已知问题，该问题导致一些 Windows 设备启动到 BitLocker 恢复。

虽然这与迫使微软禁用 CVE-2024-38058 修复的固件不兼容问题相符，但该公司没有提供任何有关实际根本原因或如何解决该问题的信息。

微软只是建议受影响的客户为他们的设备安装最新更新，因为它包含重要的改进和问题解决方，而没有以任何方式将该错误或其修复与 CVE-2024-38058 漏洞联系起来。

文章翻译自：https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-bitlocker-security-fix-advises-manual-mitigation/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?M3sJVJ3R)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

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