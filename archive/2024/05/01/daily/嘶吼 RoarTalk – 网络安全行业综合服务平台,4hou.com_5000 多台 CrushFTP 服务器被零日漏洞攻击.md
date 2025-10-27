---
title: 5000 多台 CrushFTP 服务器被零日漏洞攻击
url: https://www.4hou.com/posts/6xgR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-05-01
fetch_date: 2025-10-06T17:15:47.124968
---

# 5000 多台 CrushFTP 服务器被零日漏洞攻击

5000 多台 CrushFTP 服务器被零日漏洞攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 5000 多台 CrushFTP 服务器被零日漏洞攻击

山卡拉
[新闻](https://www.4hou.com/category/news)
2024-04-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)117087

收藏

导语：黑客经常以 CrushFTP 服务器为目标，因为它们包含敏感数据并用于文件共享和存储。

![111.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714443705193469.jpg "1714294557194281.jpg")

CrushFTP 服务器包含敏感数据并用于文件共享和存储，这使得它们经常成为黑客数据盗窃和勒索软件攻击的目标。

此外，CrushFTP服务器中的漏洞可能被用来未经授权地访问网络或向连接的系统分发恶意软件。

最近，Silent Push的研究人员发现，在版本10.7.1/11.1.0之前的CrushFTP中存在有严重的零日漏洞，标识为CVE-2024-4040，其CVSS评分为9.8。

**技术分析**

未经身份验证的漏洞允许攻击者通过Web界面逃离虚拟文件系统，获取管理员访问权限和远程代码执行功能。

CrushFTP强烈建议立即进行升级，即使是在DMZ（隔离区域）部署的情况下也是如此。

研究人员正在监控此漏洞，并利用易受攻击的域、托管服务的IP和基础设施填充数据源，并积极利用CVE-2024-4040进行早期检测。

Silent Push每天进行互联网范围内的扫描，利用SPQL对数据进行分类，以定位相关的基础设施和内容。

利用CVE-2024-4040的信息，已确定了暴露于互联网的CrushFTP Web界面可利用的情况。

由此产生的易受攻击的域和IP已经被聚集到两个批量数据源中，供企业客户分析受影响的基础设施。

下面，提到了这两个批量数据源：

**·**CrushFTP 易受攻击的域

**·**CrushFTP 易受攻击的 IP

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714443706195446.png "1714295722936981.png")

SPQL的核心是一种跨越90多个类别的DNS数据分析工具。纵观全球范围内，CrushFTP接口容易受到CVE-2024-4040的攻击的国家，大多数位于美国和加拿大，但也有许多可以在南美洲、俄罗斯、亚洲和澳大利亚以及其他地方找到。

企业用户可以下载原始数据，并以API端点的形式导出批量数据源，其中列出易受攻击的CrushFTP域和IP。

有了这些信息，安全团队就可以识别其网络中的弱点，并告知用于评估外部危险的风险评分系统。

同时，用于早期检测的源可以实时跟踪入侵尝试，同时记录与这些尝试相关的基础设施，以便可以自动阻止它。

本文翻译自：https://gbhackers.com/crushftp-servers-zero-day-hack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?m0ZrLt3H)

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

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

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

[查看更多](https://www.4hou.com/member/azxO)

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