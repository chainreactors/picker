---
title: 新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测
url: https://www.4hou.com/posts/nlEY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-29
fetch_date: 2025-12-30T03:25:46.799499
---

# 新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测

新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7896

收藏

导语：该恶意软件以经过代码签名和公证的Swift应用形式，封装在名为zk-call-messenger-installer-3.9.2-lts.dmg的磁盘镜像文件中。

针对macOS系统的MacSync信息窃取恶意软件最新变种，正通过经数字签名且过公证的Swift应用进行传播。

苹果设备管理平台的安全研究人员指出，与以往采用“拖放至终端”或ClickFix等较低级手段的版本相比，此次传播方式有了显著升级。

该恶意软件以经过代码签名和公证的Swift应用形式，封装在名为zk-call-messenger-installer-3.9.2-lts.dmg的磁盘镜像文件中，通过https://zkcall.net/download网站分发，无需用户与终端进行任何直接交互。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251223/1766476678122755.png "1766476198135982.png")

有效的数字签名和公证

研究人员在分析之时，这款MacSync最新变种持有有效的签名，能够绕过macOS系统的安全机制——Gatekeeper的检测。

安全研究员对这一通用架构的Mach-O二进制文件进行检查后确认，它既经过代码签名，也完成了Apple公证，其签名与开发者团队ID GNJLS3UYZ4相关联。不过，在研究人员将该证书直接上报Apple公司后，该证书现已被吊销。

该恶意软件通过编码形式的“投放器”植入目标系统。研究人员对载荷解码后，发现了MacSync信息窃取恶意软件的典型特征。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251223/1766476684853541.png "1766476256139587.png")

解混淆后的载荷

研究人员还指出，这款窃取软件具备多种规避检测的机制，包括：嵌入诱饵PDF文件将DMG镜像文件大小膨胀至25.5MB、清除执行链中使用的脚本，以及在执行前进行网络连接检测以规避沙箱环境。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251223/1766476687188078.png "1766476298107019.png")

膨胀后的磁盘镜像文件内容

MacSync信息窃取软件于2025年4月由名为“Mentalpositive”的黑客以“Mac.C”的名称推出，同年7月开始广泛传播，与AMOS、Odyssey等恶意软件一同跻身macOS窃取类恶意软件领域——该领域虽不像其他恶意软件领域那样拥挤，但仍具备较高获利空间。

此前MacPaw Moonlock对Mac.C的分析显示，该恶意软件可窃取iCloud钥匙串凭证、浏览器中存储的密码、系统元数据、加密货币钱包数据，以及文件系统中的各类文件。

值得关注的是，在2025年9月Mentalpositive接受研究员采访时提到，macOS 10.14.5及后续版本中更严格的应用公证政策，对其开发计划影响最大——这一点也体现在目前发现的恶意软件最新版本中。

文章来源自：https://www.bleepingcomputer.com/news/security/new-macsync-malware-dropper-evades-macos-gatekeeper-checks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?p6hOL2ez)

#### 你可能感兴趣的

* [![]()

  新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)
* [![]()

  国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/LGKp)
* [![]()

  RansomHouse完成加密工具升级：采用多层数据处理技术](https://www.4hou.com/posts/kgAr)
* [![]()

  Clop勒索软件发起数据窃取攻击：Gladinet CentreStack成目标](https://www.4hou.com/posts/jBzY)
* [![]()

  新型ConsentFix攻击：借助Azure CLI劫持微软账户](https://www.4hou.com/posts/ZgP2)
* [![]()

  新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标](https://www.4hou.com/posts/gywZ)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)
  2025-12-29 12:00:00
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/LGKp)
  2025-12-29 11:00:38
* [RansomHouse完成加密工具升级：采用多层数据处理技术](https://www.4hou.com/posts/kgAr)
  2025-12-26 12:01:00
* [Clop勒索软件发起数据窃取攻击：Gladinet CentreStack成目标](https://www.4hou.com/posts/jBzY)
  2025-12-26 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)

  胡金鱼
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/LGKp)

  胡金鱼
* [RansomHouse完成加密工具升级：采用多层数据处理技术](https://www.4hou.com/posts/kgAr)

  胡金鱼
* [Clop勒索软件发起数据窃取攻击：Gladinet CentreStack成目标](https://www.4hou.com/posts/jBzY)

  胡金鱼
* [新型ConsentFix攻击：借助Azure CLI劫持微软账户](https://www.4hou.com/posts/ZgP2)

  胡金鱼
* [新一轮OAuth钓鱼攻击来袭：微软365账户成攻击目标](https://www.4hou.com/posts/gywZ)

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