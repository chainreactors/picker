---
title: 利用武器化的 Windows 快捷方式 进行无文件 RokRat 恶意软件的部署
url: https://www.4hou.com/posts/K70x
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-06-26
fetch_date: 2025-10-06T16:54:37.351161
---

# 利用武器化的 Windows 快捷方式 进行无文件 RokRat 恶意软件的部署

利用武器化的 Windows 快捷方式 进行无文件 RokRat 恶意软件的部署 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 利用武器化的 Windows 快捷方式 进行无文件 RokRat 恶意软件的部署

山卡拉
[新闻](https://www.4hou.com/category/news)
2024-06-25 11:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)194977

收藏

导语：黑客利用LNK（Windows快捷方式）文件传播恶意软件，因为它们能够携带恶意代码，在单击快捷方式时自动执行。

![77.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240508/1715159069167274.jpg "1715159069167274.jpg")

黑客利用LNK（Windows快捷方式）文件传播恶意软件，因为它们能够携带恶意代码，在单击快捷方式时自动执行。尽管LNK文件表面看似无害，但它们实际上可以触发恶意软件下载或其他恶意操作，因此成为Windows系统上有效的初始感染方式。

最近，ASEC网络安全研究人员发现，威胁行为者积极利用武器化的Windows快捷方式文件来部署无文件的“RokRat”恶意软件。

**无文件的RokRat恶意软件**

AhnLab 证实，RokRat 恶意软件一直在针对韩国用户，尤其是与朝鲜问题相关的用户。已知的恶意LNK文件名称包括：

**·**National Information Academy 8th Integrated Course Certificate (Final).lnk

**·**Gate access roster 2024.lnk

**·**Northeast Project (US Congressional Research Service (CRS Report).lnk

**·** Facility list.lnk

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgo-pPTMmSYw32skfBbBuo9yEyIhDY7MfpzTWkIA3Lw62XLan2-CqjScnV1pDa-gaf49xI3VA8un9jxMZjkQwRkepRm1GQOzeUt_k-NLyfcjOypiPEKkuSgLRdyamgASgLtTuDlh7yj3saegnpl0ao_e2VYB_SNzNWoE3Dh1I2uyInUT1Z7xJla5FUfP-u/s16000/Confirmed%20properties%20of%20the%20LNK%20files%20(Source%20-%20ASEC).webp)

这些恶意LNK文件通过CMD执行PowerShell，与去年的RokRAT样本相似。值得注意的是，它们在LNK文件中捆绑了以下内容以增加社会工程诱惑：

**·**合法文件

**·**脚本

**·**恶意PE负载

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWiMIaqCdgt-bNfDpm-RnROQXuX8vwY9R2uFD-kweGlxGR7PRNb2xVaIbG-h-fpLOrtZEhOrTxFCTfqoh-FYWsHYUd6M0vWfiHmooP8jgBB51BBE1hRZzEfWt39T94VkdvBOrqbB0S4eHSbRufojitCv-c5S2ahpErA70AfPtNnETgo_oYVHwachNEqVWN/s16000/Operation%20structure%20(Source%20-%20ASEC).webp)运营结构（来源 – ASEC）

当LNK文件运行时，它会使用PowerShell创建一个合法文档诱饵，然后在公共文件夹中创建三个文件（find.bat、search.dat、viewer.dat）。find.bat运行search.dat，它以无文件方式执行viewer.dat中的RokRAT后门有效负载。

RokRAT能够收集用户数据并接收命令，并将窃取的信息泄露到攻击者的云服务器（如pCloud、Yandex和DropBox），同时将请求伪装成Googlebot。利用无文件技术的多阶段执行过程旨在逃避检测。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240508/1715158869780168.png "1715158869780168.png")

有关所使用的云 URL 的详细信息（来源 - ASEC）

RokRAT能够运行命令、显示目录、删除启动文件、收集启动/应用程序数据/最近的文件列表以及收集系统和网络信息。攻击者在渗透到云基础设施（例如伪装成 Googlebot 的 pCloud）之前，被盗数据会存放在临时文件夹中。已知的攻击者电子邮件地址包括tanessha.samuel@gmail.com、tianling0315@gmail.com、w.sarah0808@gmail.com和softpower21cs@gmail.com。

威胁行为者经常瞄准与韩国统一、军事或教育部门相关的目标，涉及这些领域的组织应格外警惕此类性质的持续攻击。

**IoCs**

**·** b85a6b1eb7418aa5da108bc0df824fc0

**·**358122718ba11b3e8bb56340dbe94f51

**·**35441efd293d9c9fb4788a3f0b4f2e6b

**·**68386fa9933b2dc5711dffcee0748115

**·**bd07b927bb765ccfc94fadbc912b0226

**·**6e5e5ec38454ecf94e723897a42450ea

**·**3114a3d092e269128f72cfd34812ddc8

**·**bd98fe95107ed54df3c809d7925f2d2c

本文翻译自：https://gbhackers.com/weaponized-windows-fileles-rokrat-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?hpZoriGD)

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