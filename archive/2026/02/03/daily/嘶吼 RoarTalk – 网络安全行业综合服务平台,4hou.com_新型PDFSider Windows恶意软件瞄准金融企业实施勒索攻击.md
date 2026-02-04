---
title: 新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击
url: https://www.4hou.com/posts/W15n
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-03
fetch_date: 2026-02-04T04:05:56.103144
---

# 新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击

新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-02-03 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)13213

收藏

导语：由于 AI 驱动的编码技术兴起，网络犯罪分子寻找可被利用的易受攻击软件变得越来越容易。

安全研究人员最新发现，勒索软件攻击者在针对一家财富100强金融企业的攻击中，使用了一种名为PDFSider的新型恶意软件变种，旨在向 Windows 系统投递恶意载荷。

攻击者通过伪装成技术支持人员，诱骗企业员工安装微软的Quick Assist（快速助手）工具，以此获取远程访问权限。

安全研究人员在一次事件响应过程中发现了 PDFSider，并将其描述为一种用于长期维持访问的隐蔽后门，指出其具备“通常与 APT攻击手法相关的特征”。

**合法EXE，恶意DLL**

PDFSider 已被发现在Qilin勒索软件攻击中部署。然而，有威胁狩猎团队指出，这个后门已经被“多个勒索软件团伙积极使用”来启动他们的载荷。

PDFSider 后门通过鱼叉式钓鱼邮件投递，邮件中附带一个 ZIP 压缩包，内含一个来自Miron Geek Software GmbH的PDF24 Creator工具的合法、数字签名可执行文件（EXE）。但该安装包中还包含了一个恶意版本的 DLL 文件（cryptbase.dll），而该应用程序正常运行恰好需要此文件。

当合法的 EXE 文件运行时，它会加载攻击者的 DLL 文件——这是一种被称为DLL 侧加载（DLL Side-loading）的技术，从而在系统上实现代码执行。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260120/1768895654975240.png "1768895620831404.png")

可执行文件的有效签名

在其他情况下，攻击者会利用看似针对目标定制的诱饵文档，诱骗邮件接收者启动恶意文件。一旦启动，该 DLL 将以加载它的 EXE 文件的权限运行。

EXE 文件拥有合法签名；然而，PDF24 软件存在漏洞，攻击者能够利用这些漏洞加载此恶意软件，并有效地绕过 EDR（端点检测与响应）系统。

研究人员称，由于 AI 驱动的编码技术兴起，网络犯罪分子寻找可被利用的易受攻击软件变得越来越容易。

**技术细节与隐蔽性**

PDFSider 直接加载到内存中，几乎不留下磁盘痕迹，并使用匿名管道通过 CMD 启动命令。 受感染的主机被分配一个唯一标识符，系统信息会被收集并通过 DNS（53端口）窃取至攻击者的 VPS 服务器。

PDFSider 利用 Botan 3.0.0加密库和 AES-256-GCM算法来保护其命令与控制（C2）通信，在内存中解密传入数据以最大程度减少其在主机上的足迹。

此外，数据通过 GCM 模式下的AEAD（带有关联数据的认证加密）进行身份验证。这种加密实现方式是针对性攻击中使用的远程 Shell 恶意软件的典型特征，在这类攻击中，保持通信的完整性和机密性至关重要。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260120/1768895666256532.png "1768895666256532.png")

PDFSider 运营概述

该恶意软件还具备多种反分析机制，例如 RAM 大小检查和调试器检测，以便在检测到运行于沙箱环境时提前退出。

基于评估，研究人员表示 PDFSider 更接近于间谍活动工具，而非以经济利益为动机的恶意软件，它被构建为一种隐蔽的后门，能够维持长期的秘密访问，并提供灵活的远程命令执行和加密通信功能。

文章来源自：https://www.bleepingcomputer.com/news/security/new-pdfsider-windows-malware-deployed-on-fortune-100-firms-network/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?v5nIUQiv)

#### 你可能感兴趣的

* [![]()

  Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露](https://www.4hou.com/posts/omMk)
* [![]()

  新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击](https://www.4hou.com/posts/W15n)
* [![]()

  豆包手机掀起 AI 风暴：智能便利背后的安全与规则之争](https://www.4hou.com/posts/xyYE)
* [![]()

  2026年网络安全预测：AI驱动攻击加剧，防御需更智能、更持续](https://www.4hou.com/posts/rpjW)
* [![]()

  Gootloader升级投递手法：采用千段拼接ZIP压缩包实现隐秘分发](https://www.4hou.com/posts/YZjW)
* [![]()

  Pwn2Own Automotive 2026 落幕：76 个零日漏洞被攻破，研究人员斩获百万美元奖金](https://www.4hou.com/posts/9jqY)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露](https://www.4hou.com/posts/omMk)
  2026-02-04 12:00:00
* [新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击](https://www.4hou.com/posts/W15n)
  2026-02-03 12:00:00
* [豆包手机掀起 AI 风暴：智能便利背后的安全与规则之争](https://www.4hou.com/posts/xyYE)
  2026-01-31 11:00:00
* [2026年网络安全预测：AI驱动攻击加剧，防御需更智能、更持续](https://www.4hou.com/posts/rpjW)
  2026-01-30 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露](https://www.4hou.com/posts/omMk)

  胡金鱼
* [新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击](https://www.4hou.com/posts/W15n)

  胡金鱼
* [豆包手机掀起 AI 风暴：智能便利背后的安全与规则之争](https://www.4hou.com/posts/xyYE)

  山卡拉
* [2026年网络安全预测：AI驱动攻击加剧，防御需更智能、更持续](https://www.4hou.com/posts/rpjW)

  胡金鱼
* [Gootloader升级投递手法：采用千段拼接ZIP压缩包实现隐秘分发](https://www.4hou.com/posts/YZjW)

  胡金鱼
* [Pwn2Own Automotive 2026 落幕：76 个零日漏洞被攻破，研究人员斩获百万美元奖金](https://www.4hou.com/posts/9jqY)

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