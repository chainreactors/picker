---
title: 新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招
url: https://www.4hou.com/posts/YZ1O
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-12
fetch_date: 2026-01-13T03:26:09.933157
---

# 新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招

新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)14198

收藏

导语：该工具宣称攻击转化率最高可达60%，并能识别目标设备的系统类型，投放与之兼容的恶意载荷。

最近，一款名为ErrTraffic的新型网络犯罪工具可助力威胁组织实现ClickFix攻击的自动化操作，其原理是在已入侵的网站上生成“虚假故障”，以此诱骗用户下载恶意载荷或执行恶意指令。

该工具宣称攻击转化率最高可达60%，并能识别目标设备的系统类型，投放与之兼容的恶意载荷。

ClickFix是一种社会工程学攻击手段，攻击者会编造看似合理的借口（如修复技术故障、验证用户身份等），诱骗目标在自身设备上执行危险命令。

自2024年起，这种攻击手段的使用率持续攀升，尤其是在今年，因其能够有效绕过常规安全防护措施，已被网络犯罪分子和有国家背景攻击组织广泛采用。

**ClickFix攻击自动化实现方案**

据悉，ErrTraffic是一款全新的网络犯罪工具，由一名化名LenAI的用户在俄语黑客论坛上首次推广。该工具本质上是一套自托管流量分发系统（TDS），专门用于部署ClickFix攻击诱饵，采用一次性付费模式，售价为800美元。

![图片11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260104/1767514011527746.png "1767512516981198.png")

黑客论坛上推广的恶意服务

安全研究人员对该平台开展了技术分析，发现其配备了操作便捷的控制面板，不仅提供多项配置选项，还支持查看攻击活动的实时数据。

攻击者需预先控制一个可接收受害者流量的网站——或已向某个合法网站植入恶意代码，随后通过嵌入一行HTML代码，即可将ErrTraffic集成到目标网站中。

![图片12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260104/1767514016746292.png "1767512702157350.png")

主面板

对于不符合攻击条件的普通访客，网站的显示和功能完全正常；而一旦访问者的地理位置与操作系统指纹匹配预设条件，网站的文档对象模型（DOM）就会被篡改，呈现出各种视觉故障。

这些故障表现形式多样，包括文本乱码或无法识别、字体被替换为符号、伪造Chrome浏览器更新提示、系统字体缺失报错等。

网站“故障”的假象会营造出问题场景，进而诱导受害者按照提示采取“解决措施”，例如安装浏览器更新、下载系统字体、在命令提示符中粘贴指定代码等。

一旦受害者执行相关操作，一段PowerShell恶意命令就会通过JavaScript代码自动复制到剪贴板。受害者运行该命令后，设备便会下载并执行恶意载荷。

![图片13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260104/1767514019197809.png "1767512759159377.png")

ClickFix 交付机制在 ErrTraffic

安全研究员明确指出，该工具针对不同系统投放的恶意载荷各不相同：Windows系统为Lumma和Vidar信息窃取器，安卓系统为Cerberus木马，macOS系统为AMOS（原子窃取器），Linux系统则为未明确命名的后门程序。

![图片15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260104/1767514032816357.png "1767514032816357.png")

定义每个操作系统的有效负载

ErrTraffic的使用者可针对不同架构的目标设备自定义恶意载荷，并指定实施攻击的目标国家和地区。值得注意的是，工具内置了对独联体（CIS）国家的访问排除机制，这一特征或可暗示ErrTraffic开发者的地域背景。

在绝大多数情况下，攻击者会将窃取到的用户数据在暗网市场出售，或利用这些数据进一步入侵更多网站，再次植入ErrTraffic恶意脚本。

文章来源自：https://www.bleepingcomputer.com/news/security/new-errtraffic-service-enables-clickfix-attacks-via-fake-browser-glitches/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?gBqQwp5K)

#### 你可能感兴趣的

* [![]()

  新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)
* [![]()

  GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)
* [![]()

  国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)
* [![]()

  2025 年度全球网络安全与网络攻击重大事件盘点](https://www.4hou.com/posts/W1Y4)
* [![]()

  2025年十大网络安全事件盘点：数字风险已闯入寻常生活](https://www.4hou.com/posts/jBXY)
* [![]()

  CSTIS：关于防范SleepyDck恶意软件的风险提示](https://www.4hou.com/posts/kgYr)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)
  2026-01-12 12:00:00
* [GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)
  2026-01-09 12:00:00
* [国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)
  2026-01-09 10:51:13
* [2025 年度全球网络安全与网络攻击重大事件盘点](https://www.4hou.com/posts/W1Y4)
  2026-01-08 15:18:41

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)

  胡金鱼
* [GlassWorm恶意软件新变种来袭 植入后门加密钱包瞄准Mac设备](https://www.4hou.com/posts/pn4X)

  胡金鱼
* [国家计算机病毒应急处理中心检测发现71款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/wxog)

  胡金鱼
* [2025 年度全球网络安全与网络攻击重大事件盘点](https://www.4hou.com/posts/W1Y4)

  胡金鱼
* [2025年十大网络安全事件盘点：数字风险已闯入寻常生活](https://www.4hou.com/posts/jBXY)

  山卡拉
* [CSTIS：关于防范SleepyDck恶意软件的风险提示](https://www.4hou.com/posts/kgYr)

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