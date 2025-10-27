---
title: vm2再爆沙箱逃逸漏洞
url: https://www.4hou.com/posts/m0wp
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-26
fetch_date: 2025-10-04T11:32:59.464746
---

# vm2再爆沙箱逃逸漏洞

vm2再爆沙箱逃逸漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# vm2再爆沙箱逃逸漏洞

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-04-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)126184

收藏

导语：vm2再爆沙箱逃逸漏洞，CVSS评分9.8。

vm2再爆沙箱逃逸漏洞，CVSS评分9.8。

VM2是nodejs 实现的一个沙箱环境，一般用于测试不受信任的 JavaScript 代码。允许代码部分执行，可以预防对系统资源和外部数据的非授权访问。VM2通过NPM的月下载量超过1600万，被广泛应用于IDE、代码编辑器、FaaS解决方案、渗透测试框架、安全工具和其他JS相关的产品中。

过去几周，多名安全研究人员先后发现了VM2中的多个沙箱逃逸漏洞，分别是Seongil Wi发现的CVE-2023-29017漏洞和SeungHyun Lee发现的CVE-2023-29199、CVE-2023-30547漏洞。攻击者利用这些漏洞可以绕过沙箱环境的限制运行恶意代码。CVE-2023-29017漏洞影响vm2 3.9.14之前版本，VM2已在3.9.15版本中修复了该漏洞。

**CVE-2023-30547：沙箱逃逸漏洞**

CVE-2023-30547漏洞是由来自韩国科学技术院（KAIST）的SeungHyun Lee发现的，该漏洞属于异常处理漏洞，允许攻击者在handleException()内引发未处理的主机异常，CVSS评分9.8分。

handleException()函数负责处理沙箱中的异常以预防主机信息泄露。但如果攻击者设置一个定制的getPrototypeOf()代理处理器来抛出未处理的主机异常，handleException()函数就无法处理该异常。那么攻击者就可以访问主机函数，即绕过沙箱的限制实现逃逸，并可以在主机环境内执行任意代码。

**PoC**

Lee同时在GitHub上发布了该漏洞的PoC代码以证明攻击的可行性，PoC代码如下所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682044499107189.png "1682044499107189.png")

在该PoC中，攻击者成功在主机上创建了一个明文pwned的文件。PoC代码参见：https://gist.github.com/leesh3288/381b230b04936dd4d74aaf90cc8bb244

**漏洞影响和补丁**

漏洞影响 VM2 3.9.16及之前版本。目前VM2已在v3.9.17版本中修复了该漏洞。建议所有用户和软件开发人员对包含了VM2库的项目进行升级以修改该漏洞。

经与Seongil Wi确认，Seongil Wi发现的漏洞与Lee发现的漏洞之间并无关联。

本文翻译自：https://www.bleepingcomputer.com/news/security/new-sandbox-escape-poc-exploit-available-for-vm2-library-patch-now/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Gk9BT893)

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