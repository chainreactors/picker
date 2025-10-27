---
title: 新型NPM包利用 QR 码获取 cookie 的恶意软件
url: https://www.4hou.com/posts/VWE5
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-29
fetch_date: 2025-10-02T20:50:00.203314
---

# 新型NPM包利用 QR 码获取 cookie 的恶意软件

新型NPM包利用 QR 码获取 cookie 的恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型NPM包利用 QR 码获取 cookie 的恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)29910

收藏

导语：传统隐写术常将恶意代码隐藏在图片、媒体文件或元数据中，而此次攻击更进一步，印证了威胁者会利用任何可用载体实施攻击的趋势。

近期发现的npm包“fezbox”通过二维码从攻击者服务器获取窃Cookie恶意软件。该包伪装成实用工具库，借助这种新颖的隐写技术，从受感染设备中窃取用户凭据等敏感数据。

**二维码再添恶意用途**

二维码传统上为方便使用而设计，用于承载营销内容或分享链接，但攻击者已为其找到新用途——在二维码内部隐藏恶意代码。

本周，Socket威胁研究团队发现一款名为“fezbox”的恶意包被发布至npmjs.com（全球最大的JavaScript与Node.js开源包仓库）。该恶意包包含隐藏指令，会先获取一张内含二维码的JPG图片，随后对图片进行处理，运行攻击流程中的第二阶段混淆载荷。

据npmjs.com数据显示，在仓库管理员下架该包前，其下载量至少已达327次。

![fezbox.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250924/1758697555492441.jpg "1758697109386250.jpg")

fezbox 恶意软件包在 npmjs.com 上

**反向存储恶意URL规避检测**

已确认，以1.3.0版本为例，恶意载荷主要存在于包内的dist/fezbox.cjs文件中。Socket威胁分析师Olivia Brown解释：“文件中的代码经过了压缩，格式化后可读性会显著提升。”代码中的条件判断语句会先检测应用是否运行在开发环境中。

这通常是一种隐蔽策略。威胁者不想在虚拟环境或非生产环境中暴露行踪，因此常会为漏洞利用的运行时机和方式设置防护栏。若未处于开发环境，代码会在120秒后解析并执行来自反向字符串所指向的二维码中的代码。

![fezbox-hidden-link.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250924/1758697556147643.jpg "1758697148339184.jpg")

在CJS文件中反向存储的恶意链接

上图截图中的字符串反转后为：hxxps://res[.]cloudinary[.]com/dhuenbqsq/image/upload/v1755767716/b52c81c176720f07f702218b1bdc7eff\_h7f6pn.jpg

Brown表示，将URL反向存储是攻击者的隐蔽手段，目的是绕过代码中查找“以http(s)://开头的URL”的静态分析工具。

**二维码藏混淆代码，专攻Cookie窃取**

![1758697223292247.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250924/1758697557499530.jpg "1758697223292247.jpg")

恶意网址返回的二维码

上述URL指向的二维码有别于日常营销或商务场景中常见的二维码——它的密度异常高，承载的数据量远超普通二维码。

事实上，测试发现，普通手机摄像头无法稳定识别该二维码。威胁者专门设计这款条码，用于传递可被“fezbox”包解析的混淆代码。

Brown解释，该混淆载荷会通过document.cookie读取Cookie数据：“随后它会获取用户名和密码，这里同样使用了字符串反转的混淆手段（如将password写为drowssap）。”

若窃取的Cookie中同时包含用户名和密码，载荷会通过HTTPS POST请求将信息发送至https://my-nest-app-production[.]up[.]railway[.]app/users；若不满足条件，则静默退出，不执行任何操作。

**攻击创新点：无需人工介入的二维码滥用**

此前，我们已见过无数二维码在社会工程学骗局中的应用——从虚假问卷到伪造“停车罚单”等，但这类场景均需人工介入（例如用户扫描二维码后被引导至钓鱼网站）。

而Socket本周的发现展现了二维码滥用的新套路：受感染设备可通过二维码与命令控制（C2）服务器通信，且在代理或网络安全工具看来，这种通信与普通的图片传输流量并无二致。

传统隐写术常将恶意代码隐藏在图片、媒体文件或元数据中，而此次攻击更进一步，印证了威胁者会利用任何可用载体实施攻击的趋势。

文章翻译自：https://www.bleepingcomputer.com/news/security/npm-package-caught-using-qr-code-to-fetch-cookie-stealing-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?b7ZxYsdQ)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

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

[查看更多](https://www.4hou.com/member/BVMN)

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