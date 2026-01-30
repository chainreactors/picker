---
title: Gootloader升级投递手法：采用千段拼接ZIP压缩包实现隐秘分发
url: https://www.4hou.com/posts/YZjW
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-29
fetch_date: 2026-01-30T04:02:39.403238
---

# Gootloader升级投递手法：采用千段拼接ZIP压缩包实现隐秘分发

Gootloader升级投递手法：采用千段拼接ZIP压缩包实现隐秘分发 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Gootloader升级投递手法：采用千段拼接ZIP压缩包实现隐秘分发

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-01-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10996

收藏

导语：该载荷在首次启动及每次系统开机时执行，利用 NTFS 短文件名触发 CScript，随后由 PowerShell 生成另一个 PowerShell 进程。

通常用于初始访问的Gootloader恶意软件，现采用一种畸形 ZIP 压缩包设计来规避检测，其手段是将多达 1,000 个压缩包进行拼接。

这样一来，这个本质上是归档 JScript 文件的恶意软件，会导致许多分析工具在尝试解析时直接崩溃。

研究人员称，虽然 Windows 自带的默认解压工具能成功解包该恶意文件，但依赖 7-Zip 和 WinRAR 的工具却会失败。

为实现这一目的，该恶意软件背后的威胁组织将 500 至 1,000 个 ZIP 压缩包拼接在一起，并辅以其他技巧，使分析工具的解析过程变得异常困难。

Gootloader 恶意软件加载器自 2020 年起便活跃至今，被各类网络犯罪活动（包括勒索软件部署）所利用。

据安全研究人员发现，该团伙在沉寂七个月后，于去年 11 月卷土重来。

虽然当时就已出现畸形 ZIP 压缩包，但仅包含微小修改，且在尝试提取数据时会出现文件名不匹配的问题。研究人员对近期样本的分析，为进一步加强该阶段的反分析能力，Gootloader 运营商现已实施了更为广泛的混淆机制。

具体而言，目前采用以下机制来规避检测与分析：

1.拼接多达一千个 ZIP 压缩包：利用解析器从文件末尾开始读取的特性。

2.使用截断的中央目录结束标记（EOCD）：缺失两个强制字节，导致大多数工具解析失败。

3.随机化磁盘数字段：导致工具误认为存在不存在的多磁盘压缩包。

4.添加本地文件头与中央目录项之间的元数据不匹配。

5.为每次下载生成唯一的 ZIP 和 JScript 样本：以规避静态检测。

6.以 XOR 编码的二进制大对象（Blob）形式投递 ZIP：在客户端进行解码并反复追加，直到达到所需大小，以此规避基于网络的检测。

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260120/1768901906766813.png "1768901906766813.png")

本地文件头和中央目录之间的不匹配

一旦在主机上执行，恶意软件的 JScript 会通过 Windows 脚本宿主（WScript）从临时目录激活，并通过在“启动”文件夹中添加指向第二个 JScript 文件的快捷方式（.LNK）来建立持久化。

该载荷在首次启动及每次系统开机时执行，利用 NTFS 短文件名触发 CScript，随后由 PowerShell 生成另一个 PowerShell 进程。

尽管 Gootloader 的作者添加了多种破坏技术以在不影响功能的前提下规避检测，但研究人员利用这些结构异常特征，使防御者能够发现该威胁。

该检测机制依赖于发现特定的 ZIP 头特征组合、数百个重复的本地文件头以及 EOCD 记录。

研究人员建议防御者将打开 JScript 文件的默认应用程序改为记事本（Notepad），而非 Windows 脚本宿主（WSH），以防止其执行。 为减少攻击面，最好在不需要使用 JScript 文件的情况下，阻止 wscript.exe 和 cscript.exe 执行下载的内容。

文章来源自：https://www.bleepingcomputer.com/news/security/gootloader-now-uses-1-000-part-zip-archives-for-stealthy-delivery/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iKHOX23N)

#### 你可能感兴趣的

* [![]()

  2026年网络安全预测：AI驱动攻击加剧，防御需更智能、更持续](https://www.4hou.com/posts/rpjW)
* [![]()

  Gootloader升级投递手法：采用千段拼接ZIP压缩包实现隐秘分发](https://www.4hou.com/posts/YZjW)
* [![]()

  Pwn2Own Automotive 2026 落幕：76 个零日漏洞被攻破，研究人员斩获百万美元奖金](https://www.4hou.com/posts/9jqY)
* [![]()

  决胜2026：当AI开始攻破AI，我们还能做些什么？](https://www.4hou.com/posts/l0JV)
* [![]()

  嘶吼快讯|网安厂商动态汇（第7期）](https://www.4hou.com/posts/0M53)
* [![]()

  GhostPoster攻势再起：17款恶意浏览器扩展伪装潜伏 累计下载量超84万](https://www.4hou.com/posts/VW4O)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [2026年网络安全预测：AI驱动攻击加剧，防御需更智能、更持续](https://www.4hou.com/posts/rpjW)
  2026-01-30 12:00:00
* [Gootloader升级投递手法：采用千段拼接ZIP压缩包实现隐秘分发](https://www.4hou.com/posts/YZjW)
  2026-01-29 12:00:00
* [Pwn2Own Automotive 2026 落幕：76 个零日漏洞被攻破，研究人员斩获百万美元奖金](https://www.4hou.com/posts/9jqY)
  2026-01-28 16:37:40
* [决胜2026：当AI开始攻破AI，我们还能做些什么？](https://www.4hou.com/posts/l0JV)
  2026-01-28 11:48:45

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [2026年网络安全预测：AI驱动攻击加剧，防御需更智能、更持续](https://www.4hou.com/posts/rpjW)

  胡金鱼
* [Gootloader升级投递手法：采用千段拼接ZIP压缩包实现隐秘分发](https://www.4hou.com/posts/YZjW)

  胡金鱼
* [Pwn2Own Automotive 2026 落幕：76 个零日漏洞被攻破，研究人员斩获百万美元奖金](https://www.4hou.com/posts/9jqY)

  胡金鱼
* [决胜2026：当AI开始攻破AI，我们还能做些什么？](https://www.4hou.com/posts/l0JV)

  叮小球
* [嘶吼快讯|网安厂商动态汇（第7期）](https://www.4hou.com/posts/0M53)

  胡金鱼
* [GhostPoster攻势再起：17款恶意浏览器扩展伪装潜伏 累计下载量超84万](https://www.4hou.com/posts/VW4O)

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