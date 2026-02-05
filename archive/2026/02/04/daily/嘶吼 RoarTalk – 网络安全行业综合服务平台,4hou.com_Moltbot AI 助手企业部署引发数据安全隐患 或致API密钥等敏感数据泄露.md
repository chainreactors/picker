---
title: Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露
url: https://www.4hou.com/posts/omMk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-04
fetch_date: 2026-02-05T04:07:31.043289
---

# Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露

Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-02-04 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9871

收藏

导语：这款AI助手默认未开启沙箱隔离机制，这意味着该机器人拥有与用户完全相同的数据访问权限。

安全研究人员发出警告，企业环境中对Moltbot（前身为Clawdbot）人工智能助手的非安全化部署，可能导致API密钥、OAuth令牌、对话记录及各类凭证信息泄露。

据悉，Moltbot是一款可深度集成系统的开源个人AI助手，能本地部署在用户设备中，还可直接与即时通讯工具、邮件客户端等应用及文件系统实现集成。

与云端聊天机器人不同，Moltbot可在本地7×24小时运行，支持持久化记忆、主动向用户推送提醒/通知、执行定时任务等功能。正是这些实用功能与简便的部署方式，让Moltbot迅速走红，甚至推动了Mac Mini的销量增长——不少人为这款机器人专门购置了专属部署主机。

**管理界面暴露引安全风险**

多名安全研究人员提醒，若对Moltbot的部署操作疏忽大意，结合其在主机上的权限与访问级别，可能引发敏感数据泄露、企业数据曝光、凭证被盗、命令执行等一系列安全问题。

有相关人员重点指出了其中部分安全隐患。因反向代理配置错误，目前已有数百个Clawdbot Control管理界面暴露在公网中。

由于Clawdbot会自动通过所有“本地”连接请求，部署在反向代理后的该程序，往往会将所有网络流量均视为可信来源，这导致许多暴露的实例存在未授权访问、凭证被盗、对话记录可被查看、命令可被执行，甚至能被获取系统根级访问权限等问题。

该研究人员称：“有人在其面向公网的clawdbot控制服务器上，绑定了自己的Signal加密即时通讯账户，且该服务器拥有该账户的完整读取权限。”

服务器上不仅有Signal设备的关联统一资源标识符，还有对应的二维码。在安装了Signal的手机上点击该标识符，就能配对该账户并获得完整访问权限。

研究人员曾尝试与该聊天机器人交互以解决上述问题，机器人虽回复会提醒服务器所有者，却无法提供任何联系方式。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260129/1769669493594127.png "1769669112149817.png")

研究人员与暴露的 Moltbot 实例互动

此外，工作人员还发布了第二部分研究成果，演示了如何通过供应链攻击针对Moltbot用户——通过制作一个包含简易“ping”载荷的技能模块（封装指令集或功能模块），以此实施攻击。

该开发者将这个恶意技能模块发布至Moltbot官方的MoltHub（原ClawdbotHub）注册表，并人为刷高其下载量，使其成为该平台最热门的资源。

在不到8小时的时间里，已有来自7个国家的16名开发者，下载了这个被人为推广的恶意技能模块。

**企业面临多重安全威胁**

尽管Moltbot本更适用于个人用户，但安全公司称，其22%的企业客户中，均有员工在未获得IT部门批准的情况下，擅自使用该AI助手。

目前已识别出多项潜在风险，包括网关与API/OAuth令牌暴露、凭证信息以明文形式存储在~/.clawdbot/目录下、通过AI中介访问导致企业数据泄露，以及提示注入攻击面扩大等。

其中一大核心隐患是，这款AI助手默认未开启沙箱隔离机制，这意味着该机器人拥有与用户完全相同的数据访问权限。

多个安全团队均针对Moltbot发出了类似的安全警告。据发现，已有攻击者将暴露的Moltbot端点作为目标，实施凭证窃取与提示注入攻击。像RedLine、Lumma和Vidar等信息窃取恶意软件，近期或将完成适配，把Moltbot的本地存储作为攻击目标，窃取其中的敏感数据与账户凭证。

此外，有安全研究人员还发现了一起仿冒Clawdbot的恶意VSCode插件事件，该插件会在开发者的设备中安装ScreenConnect远程访问木马。

安全部署Moltbot需要相关的专业知识与严谨的操作态度，其中关键是将AI实例隔离在虚拟机中运行，并为其网络访问配置防火墙规则，而非直接以根权限在主机操作系统中运行该程序。

文章来源自：https://www.bleepingcomputer.com/news/security/viral-moltbot-ai-assistant-raises-concerns-over-data-security/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?D6eK9JOX)

#### 你可能感兴趣的

* [![]()

  新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)
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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)
  2026-02-05 12:00:00
* [Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露](https://www.4hou.com/posts/omMk)
  2026-02-04 12:00:00
* [新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击](https://www.4hou.com/posts/W15n)
  2026-02-03 12:00:00
* [豆包手机掀起 AI 风暴：智能便利背后的安全与规则之争](https://www.4hou.com/posts/xyYE)
  2026-01-31 11:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)

  胡金鱼
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