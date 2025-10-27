---
title: Inception瞬态执行攻击影响所有AMD Zen CPU
url: https://www.4hou.com/posts/EXXY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-20
fetch_date: 2025-10-04T11:59:07.496800
---

# Inception瞬态执行攻击影响所有AMD Zen CPU

Inception瞬态执行攻击影响所有AMD Zen CPU - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Inception瞬态执行攻击影响所有AMD Zen CPU

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-08-19 11:50:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)115209

收藏

导语：​新瞬态执行攻击Inception可从所有AMD Zen CPU泄露敏感数据。

新瞬态执行攻击Inception可从所有AMD Zen CPU泄露敏感数据。

苏黎世联邦理工学院（ETH Zurich）研究人员发现一种新的瞬态执行攻击——'Inception'攻击。攻击可从攻击者控制的地址发起推测执行，引发信息泄露。漏洞CVE编号CVE-2023-20569，影响所有AMD Zen CPU。

瞬态执行攻击利用了现代处理器的推测执行特征，通过猜测接下来要执行的内容来提高CPU的性能。如果猜测正确，CPU就无需等到操作执行结束，如果猜测失败，只需要回滚并继续执行操作即可。猜测执行存在的问题是会留下痕迹，攻击者可以查看和分析这些有价值的数据用于攻击活动。

苏黎世联邦理工学院研究人员融合了'Phantom speculation' (CVE-2022-23825)和一种新的瞬态执行攻击（TTE，Training in Transient Execution）创建了更加强大的inception攻击。'Phantom speculation'允许攻击者在无错误预测源处无需任何分支就可以触发错误预测，比如在任意异或XOR指令创建推测执行周期（瞬态窗口）。TTE是一种对未来错误预测的操纵，通过注入新的预测到预测分支来创建可利用的推测执行。Inception攻击融合了以上两种概念，使得被攻击的CPU认为XOR指令是一个递归调用指令。Inception攻击会用攻击者控制的目标地址来覆写返回栈缓存，攻击者可从AMD Zen CPU运行的非特权进程泄露任意数据。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230809/1691587335438228.png "1691586950498544.png")

图 Inception攻击逻辑

Inception攻击可实现39字节/秒的数据泄露速率，泄露一个16字符的密码只需要0.5秒，泄露一个RSA密钥只需要6.5秒。Inception攻击可以绕过现有推测执行攻击的修复措施，如Spectre和瞬时控制流劫持等。

Inception攻击是针对AMD CPU的，所以是由AMD CPU的设备都受到Inception和 Phantom攻击的影响。研究人员分析发现Phantom也会影响Intel CPU，此外部分Intel CPU也受到特定TTE变种的影响。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230809/1691587337136037.png "1691586978179739.png")

图 特定TTE变种对CPU的影响

研究人员开发的PoC运行在Linux系统上，但Inception 和Phantom攻击是针对的是硬件漏洞。因此，任何受影响的CPU上运行的操作系统都会受到影响。

AMD建议使用Zen 3和Zen 4 CPU架构的用户使用µcode补丁或BIOS更新，对于Zen和Zen 2 CPU架构用户无需使用µcode补丁或BIOS更新。此外，AMD还计划发布更新的AGESA。

相关研究成果已被安全顶会Usenix security 2023录用，论文下载地址：https://comsec.ethz.ch/wp-content/files/inception\_sec23.pdf

更多参见：https://comsec.ethz.ch/research/microarch/inception/

本文翻译自：https://comsec.ethz.ch/research/microarch/inception/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?CBYPw3MB)

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