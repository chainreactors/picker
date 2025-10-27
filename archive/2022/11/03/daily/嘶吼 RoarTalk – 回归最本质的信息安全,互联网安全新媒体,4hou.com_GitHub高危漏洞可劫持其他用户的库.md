---
title: GitHub高危漏洞可劫持其他用户的库
url: https://www.4hou.com/posts/50oq
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-03
fetch_date: 2025-10-03T21:36:48.575579
---

# GitHub高危漏洞可劫持其他用户的库

GitHub高危漏洞可劫持其他用户的库 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GitHub高危漏洞可劫持其他用户的库

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-11-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)170548

收藏

导语：​研究人员发现GitHub存在库劫持漏洞，攻击者利用该漏洞可接管其他用户的库。

研究人员发现GitHub存在库劫持漏洞，攻击者利用该漏洞可接管其他用户的库。

GitHub库在创建库的用户账号下有唯一的URL。当其他用户想要下载或复制该库时，会使用到该库的完整URL。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20221101/1667272050167675.png)

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20221101/1667272051701314.png)

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20221101/1667272052193880.png)

**库劫持**

库劫持（RepoJacking）是指通过利用逻辑漏洞破坏原始重定向过程，实现劫持修改了用户名的URL的流量并重定向到攻击者库的过程。研究人员在GitHub中发现了一个库劫持漏洞，当创建者决定修改其用户名，而老的用户名可以用于注册时就会出现可劫持库的情况。

从GitHub库名与创建者用户名之间的关系可以看出，GitHub可以创建一个新的GitHub账户与现有用户使用的老库URL一致。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20221101/1667272053441455.png)

此时，默认的重定向就被禁用了，所有现有流量都会立刻路由到攻击者的恶意GitHub库。

**GitHub应对方法**

为应对此类行为，GitHub实施了流行库命名空间退出（popular repository namespace retirement）保护策略：超过100个clone的库在用户账户修改时会会被标记为退出（retired）状态，无法被其他人使用。比如，repo库被clone超过100次，用户名“account-takeover-victim”就无法再创建名为repo的库：

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20221101/1667272056971881.png)

**绕过GitHub保护**

研究人员进一步分析发现GitHub提出的应对保护措施可以被绕过。新的绕过方法使用了“Repository Transfer”特征，具体步骤如下：

“victim/repo”是受GitHub retirement保护的GitHub 库，

“helper\_account”账户创建了repo库；

“helper\_account”将repo库的所有权转给了“attacker\_account”；

“attacker\_account”将其用户名重命名为“victim”。

新的“victim”账号实际上就是之前的“attacker\_account”，会接受所有权的转移。

victim/repo”就会被攻击者控制。

**影响**

攻击者成功利用该漏洞可以控制主流的包管理器的代码包，包括“Packagist”、“Go”、“Swift”等。研究人员发现有超过1万个重命名的包受到该漏洞的影响。此外，攻击者利用该漏洞还可以发起供应链投毒攻击。

**时间轴**

2021年11月8日，研究人员将GitHub命名空间退出特征绕过方法提交给了GitHub。2022年3月，GitHub回复称已修复该绕过。5月，研究人员发现该漏洞仍然是可利用的，5月25日，GitHub修复该问题。6月，研究人员发现了绕过GitHub命名空间退出特征保护机制的绕过方法，并报告给了GitHub。9月19日，GitHub修复该漏洞，并将该漏洞分类为高危。

本文翻译自：https://checkmarx.com/blog/attacking-the-software-supply-chain-with-a-simple-rename/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?r5Ssdusy)

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

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

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

[查看更多](https://www.4hou.com/member/e7OO)

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