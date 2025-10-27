---
title: VM2远程代码执行漏洞曝光
url: https://www.4hou.com/posts/wgwm
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-15
fetch_date: 2025-10-03T19:55:15.203801
---

# VM2远程代码执行漏洞曝光

VM2远程代码执行漏洞曝光 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# VM2远程代码执行漏洞曝光

ang010ela
[漏洞](https://www.4hou.com/category/vulnerable)
2022-10-14 11:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)499917

收藏

导语：​VM2现10分漏洞，可在沙箱外运行代码。

VM2现10分漏洞，可在沙箱外运行代码。

vm2是JS沙箱库，每个月通过npm的下载量超过1600万。Oxeye安全研究人员在vm2中发现了一个非常严重的远程代码执行漏洞，漏洞CVE编号为CVE-2022-36067，CVSS评分10分，攻击者利用该漏洞可以从沙箱环境逃逸并在主机系统上运行命令。

沙箱是与操作系统其他部分隔离开来的隔离环境。开发者常用沙箱来运行或测试不安全的代码，因此从受限的环境中逃逸并在主机上执行代码是一个非常大的安全隐患。

**漏洞分析**

Node.js允许应用开发者定制应用遇到错误时的调用stack。定制调用stack可以通过Error对象的“prepareStacktrace”方法来实现。也就是说错误在发生时，错误对象的stack属性会被访问，node.js会调用该方法，并提供给该方法一个字符串表示和“CallSite”对象作为参数。Node.js调用“prepareStackTrace”函数如下所示：

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20221012/1665581194544017.png)

数组中的每个“CallSite”对象都表示不同的stake帧。“CallSite”对象的严格方法getThis负责返回this对象。该行为可能会引发沙箱逃逸，因为有“CallSite”对象可能会返回通过调用“getThis”方法时创建的对象。在获得沙箱外创建的“CallSite”对象后，就可能访问节点的全局对象并执行任意系统命令。

![](https://global-uploads.webflow.com/60c0a2657a42950c051d890b/633aa0ca7b7cb71edcc8d988_VM2%20Diagram%403x.png)

PoC代码如下所示：

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20221012/1665581196130403.png)

攻击者利用该漏洞可以绕过vm2沙箱环境，并在沙箱主机上运行shell命令。

**漏洞修复**

Vm2维护人员意识到覆写“prepareStackTrace”可能会引发沙箱逃逸，并尝试封装Error对象和“prepareStackTrace”方法来进行应对。Vm2已于v 3.9.11版本中修复了该漏洞。使用沙箱的用户应检查确认是否依赖vm2，并更新到最新版本。

完整技术分析参见：https://www.oxeye.io/blog/vm2-sandbreak-vulnerability-cve-2022-36067

本文翻译自：https://www.bleepingcomputer.com/news/security/critical-vm2-flaw-lets-attackers-run-code-outside-the-sandbox/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?NYiEl1p8)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/e7OO)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

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