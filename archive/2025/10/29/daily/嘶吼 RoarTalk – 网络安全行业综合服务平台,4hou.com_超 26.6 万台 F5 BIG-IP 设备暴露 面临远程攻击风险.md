---
title: 超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险
url: https://www.4hou.com/posts/1M83
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-10-29
fetch_date: 2025-10-30T03:09:38.739046
---

# 超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险

超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)13745

收藏

导语：F5于表示黑客入侵其网络，窃取了源代码及未公开的BIG-IP安全漏洞信息，但尚未发现攻击者泄露或利用这些未公开漏洞发起攻击的证据。

互联网安全非营利组织Shadowserver基金会发现，在网络安全公司F5披露安全入侵事件后，全球有超过26.6万台F5 BIG-IP设备暴露在公网上。

F5于表示黑客入侵其网络，窃取了源代码及未公开的BIG-IP安全漏洞信息，但尚未发现攻击者泄露或利用这些未公开漏洞发起攻击的证据。

F5还发布补丁修复44个漏洞（包括此次入侵中被盗取信息的漏洞），并敦促客户尽快更新设备。该公司表示：“针对BIG-IP、F5OS、面向Kubernetes的BIG-IP Next、BIG-IQ及APM客户端的更新现已上线。尽管目前未发现存在未公开的严重漏洞或远程代码执行漏洞，但仍强烈建议尽快更新BIG-IP软件。”

网络监管机构Shadowserver目前已追踪到266,978个带有F5 BIG-IP特征的IP地址。其中，近半数（超14.2万个）位于美国，另有10万个分布在欧洲和亚洲。

不过，目前尚无数据表明，这些设备中有多少已完成安全加固，以防范可能利用本周披露的BIG-IP漏洞发起的攻击。

![F5 devices exposed online.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251020/1760948897469983.png "1760948897469983.png")

在线公开的 F5 设备

目前，CISA已发布紧急指令，对美国联邦机构提出明确要求：

1. 在10月22日前，通过安装最新F5安全补丁，完成对F5OS、BIG-IP TMOS、BIG-IQ及BNK/CNF产品的安全加固；

2. 网络中其他所有F5硬件和软件设备的修复截止日期延长至10月31日；

3. 断开并停用所有已达“支持终止期”且暴露在公网上的F5设备——这类设备将不再获得补丁更新，极易在攻击中被攻陷。

近年来，国家级威胁组织与网络犯罪团伙均将BIG-IP漏洞作为攻击重点，通过漏洞可实现多种恶意操作：

**·**测绘受害者内部服务器；

**·**劫持受害者网络中的设备；

**·**入侵企业网络、窃取敏感文件；

**·**部署数据擦除恶意软件。

此外，被攻陷的F5 BIG-IP设备还可能让威胁者窃取凭证与应用程序接口（API）密钥，在受害者网络中横向移动，并建立持久化控制。

文章翻译自：https://www.bleepingcomputer.com/news/security/over-266-000-f5-big-ip-instances-exposed-to-remote-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?akIJjzoE)

#### 你可能感兴趣的

* [![]()

  超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)
* [![]()

  工信部通报20款智能终端存在侵害用户权益行为](https://www.4hou.com/posts/pn01)
* [![]()

  新型恶意攻击瞄准macOS用户 仿冒三大平台植入窃密软件](https://www.4hou.com/posts/ZgJv)
* [![]()

  窃取加密货币的恶意 VSCode 插件在 OpenVSX 平台再度出现](https://www.4hou.com/posts/PGvz)
* [![]()

  国家安全机关破获美国国家安全局重大网络攻击案](https://www.4hou.com/posts/2X5J)
* [![]()

  新型 Android Pixnapping 攻击：逐像素窃取MFA码](https://www.4hou.com/posts/QXw7)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)
  2025-10-29 12:00:00
* [工信部通报20款智能终端存在侵害用户权益行为](https://www.4hou.com/posts/pn01)
  2025-10-27 15:08:24
* [新型恶意攻击瞄准macOS用户 仿冒三大平台植入窃密软件](https://www.4hou.com/posts/ZgJv)
  2025-10-24 12:00:00
* [窃取加密货币的恶意 VSCode 插件在 OpenVSX 平台再度出现](https://www.4hou.com/posts/PGvz)
  2025-10-21 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)

  胡金鱼
* [工信部通报20款智能终端存在侵害用户权益行为](https://www.4hou.com/posts/pn01)

  胡金鱼
* [新型恶意攻击瞄准macOS用户 仿冒三大平台植入窃密软件](https://www.4hou.com/posts/ZgJv)

  胡金鱼
* [窃取加密货币的恶意 VSCode 插件在 OpenVSX 平台再度出现](https://www.4hou.com/posts/PGvz)

  胡金鱼
* [国家安全机关破获美国国家安全局重大网络攻击案](https://www.4hou.com/posts/2X5J)

  胡金鱼
* [新型 Android Pixnapping 攻击：逐像素窃取MFA码](https://www.4hou.com/posts/QXw7)

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