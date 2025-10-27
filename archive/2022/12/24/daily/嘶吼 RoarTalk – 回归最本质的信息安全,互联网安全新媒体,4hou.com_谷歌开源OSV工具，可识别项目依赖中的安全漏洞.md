---
title: 谷歌开源OSV工具，可识别项目依赖中的安全漏洞
url: https://www.4hou.com/posts/17LZ
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-24
fetch_date: 2025-10-04T02:23:58.105375
---

# 谷歌开源OSV工具，可识别项目依赖中的安全漏洞

谷歌开源OSV工具，可识别项目依赖中的安全漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 谷歌开源OSV工具，可识别项目依赖中的安全漏洞

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-12-23 11:40:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)173182

收藏

导语：​谷歌发布OSV开发工具可列出开源项目依赖中的安全漏洞。

谷歌发布OSV开发工具可列出开源项目依赖中的安全漏洞。

**开源软件漏洞问题**

开源软件开发者会使用大量的工具、库和组件，通过依赖这些工具和库可以更加快速地解决复杂问题。与其他代码类似，这些开源软件依赖的组件中也可能存在安全漏洞。当开源软件使用这些有漏洞的依赖时，其安全性也受到影响。对于使用大量依赖的软件来说，追踪每个组件中的安全问题和评估其对程序本身的潜在影响是一个非常复杂的任务。

**谷歌OSV Scanner工具**

谷歌近日发布了OSV Scanner工具，并开源了该工具的源代码。开发者利用该工具可以扫描项目中使用的开源软件依赖中的安全漏洞。扫描工具的数据来源于2021年2月谷歌发布的分布式开源代码漏洞数据库，可以提供影响开源代码已知的安全问题的相关信息。

![](https://thehackernews.com/new-images/img/b/R29vZ2xl/AVvXsEitWA5nGALsIVrl9bo3t73bPXmpRlRu5Lgu3b1IX_lp4DrrcjoUAmiaEC2ifr6dQbw3MKB9keiqkp2x_n5zmoxlMFv510ldazRBqiJYPY8c4Huhh0I7CRp9mfu4bsSQL1oa1Y_DdxbkU7uEO1D5QAf4wLferO94jLmI19nS8KqmWQ-RtFxtyrmSv5DQ/s728-e100/google-1.png)

![Example scan results](https://www.bleepstatic.com/images/news/u/1220909/Tables/results(1).png)

图 扫描结果示例

OSV Scanner是基于Go语言开发的，可以生成可靠的、高质量的漏洞信息。基本思想是识别所有的项目依赖，并利用OSV.DEV数据库中的数据来识别出相关的漏洞。OSV Scanner支持16种生态系统，涵盖主流的开发语言、Linux发行版、以及安卓、Linux kernel、OSS-Fuzz等。

![](https://thehackernews.com/new-images/img/b/R29vZ2xl/AVvXsEhxyQf2fr8kNCpInqwN-okCGaREwlFA8qoZr-OCw_aAPVe3LpWMhD-RkGkiBxxf3gVoaukuOWIaWes0GRs7LryVUs6bknXFm3D-mxL2w4rU-h4hxjRb9Maz49JxKE1q8R6jwLVR4hE_OUY6IDeE19hzBxlIJnJhKFfOsca18_8FbLXRLshu0VtkT9xT/s728-e100/database.png)

**下一步方向**

谷歌称下一步将通过构建高质量的数据库将C/C++漏洞纳入支持范围。

OSV项目地址：<https://osv.dev/>

OSV项目源代码参见GitHub：<https://github.com/google/osv-scanner>

本文翻译自：https://www.bleepingcomputer.com/news/security/google-releases-dev-tool-to-list-vulnerabilities-in-project-dependencies/ 与 https://thehackernews.com/2022/12/google-launches-largest-distributed.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?IesIsl8Z)

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