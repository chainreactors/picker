---
title: 几乎所有现代CPU都将数据泄漏给新的Collide+Power侧信道攻击
url: https://www.4hou.com/posts/GXKJ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-04
fetch_date: 2025-10-04T12:04:07.840147
---

# 几乎所有现代CPU都将数据泄漏给新的Collide+Power侧信道攻击

几乎所有现代CPU都将数据泄漏给新的Collide+Power侧信道攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 几乎所有现代CPU都将数据泄漏给新的Collide+Power侧信道攻击

布加迪
[新闻](https://www.4hou.com/category/news)
2023-08-03 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)110420

收藏

导语：一种名为Collide+Power的新的功率侧信道攻击让攻击者可以获得敏感信息，这种攻击几乎可以攻陷任何现代CPU。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691029601121651.jpg "1691016876138066.jpg")

一种可以导致数据泄漏的新侧信道攻击方法几乎可以攻陷任何现代CPU，但我们不太可能在短期内看到它被广泛实际利用。

这项研究是由来自奥地利格拉茨科技大学和德国CISPA亥姆霍兹信息安全中心的八名研究人员共同进行的。参与这项研究的一些专家发现了臭名昭著的Spectre和Meltdown漏洞，以及另外几种侧信道攻击方法。

这种新的攻击名为Collide+Power，其破坏力与Meltdown和一类名为微架构数据采样（MDS）的漏洞相提并论。

Collide+Power是一种基于软件的通用型攻击，针对搭载英特尔、AMD或Arm处理器的设备，它适用于任何应用程序和任何类型的数据。芯片制造商们正在发布各自的安全公告，该漏洞已被命名为CVE-2023-20583。

然而研究人员指出，Collide+Power不是一个真正的处理器漏洞，它利用一些CPU部件旨在共享来自不同安全域的数据这一点大做文章。

攻击者可以利用这些共享的CPU部件将自己的数据与来自用户应用程序的数据结合起来。攻击者在改变他们控制的数据时，可以数千次迭代测量CPU功耗，这使他们能够确定与用户应用程序关联的数据。

没有特权的攻击者（比如通过在目标设备上植入恶意软件）可以利用Collide+Power攻击，获得有价值的数据，比如密码或加密密钥。

研究人员特别指出，Collide+Power攻击增强了其他功率侧信道信号，比如PLATYPUS和Hertzbleed攻击中使用的信号。

研究人员解释道：“PLATYPUS和Hertzbleed等以前基于软件的功率侧信道攻击针对加密算法，需要确切了解目标机器上执行的算法或受害者程序。相比之下，Collide+Power针对的是CPU内存子系统，内存子系统把精确的实现抽取出来，因为所有程序都以某种方式需要内存子系统。此外，任何反映功耗的信号都可以被使用，因为Collide+Power利用了基本的功率泄漏。”

研究人员发表了一篇详细介绍其研究工作的论文，还推出了Collide+Power网站，专门介绍这一研究发现。

他们描述了Collide+Power攻击的两种变体。在要求启用超线程机制的第一种变体中，攻击目标是与不断访问秘密数据（比如加密密钥）的应用程序相关的数据。

“在此过程中，受害者不断将秘密数据重新加载到被攻击的共享CPU部件中。在同一物理核心上运行线程的攻击者现在可以利用Collide+Power，强制秘密数据与攻击者控制的数据之间发生碰撞。”

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230803/1691029601936331.png "1691016864160446.png")

图1

攻击的第二种变体不需要超线程机制，也不需要目标不断访问秘密数据。

专家们表示：“攻击者在这里利用了操作系统中一个所谓的预读取小装置。这个预读取小装置可以用来将任意数据引入到共享的CPU部件中，再次强行造成数据碰撞，并找回数据。”

虽然从理论上来说这种攻击方法可能会产生重大影响，但在实践中，数据泄漏率比较低，这种方法也不太可能在短期内被用来攻击最终用户。

研究人员已经在这种场景下设法实现了每小时泄漏4.82比特的数据：被攻击的应用程序不断访问秘密信息，攻击者可以通过直接报告CPU功耗情况的运行平均功率限制（RAPL）接口，直接读取CPU功耗数值。按照这个泄漏率，攻击者需要几个小时才能获得密码，需要几天才能获得加密密钥。

研究人员发现，在特殊场景下，攻击者可以大大提高数据泄漏率，最高每小时可泄漏188比特的数据。

格拉茨科技大学参与这个项目的研究人员之一Andreas Kogler告诉安全外媒：“攻击者可以达到每小时188比特的泄漏率，具体取决于被攻击的应用程序和内存中的秘密数据。比如说，密钥或密码是否多次出现在缓存行中。”

另一方面，在实际环境的攻击模拟中，研究人员遇到了实际限制，这大大降低了泄漏率——如果采用遏制手段，泄露每比特就需要一年多。

尽管目前这种攻击带来的风险比较小，但Collide+Power研究强调了潜在的问题，并为未来的研究铺平了道路。

至于缓解措施，在硬件层面防止这类数据碰撞并非易事，需要重新设计通用CPU。另一方面，可以通过确保攻击者无法观察到与功率相关的信号来阻止攻击，这种类型的缓解措施适用于所有的功率侧信道攻击。

本文翻译自：https://www.securityweek.com/nearly-all-modern-cpus-leak-data-to-new-collidepower-side-channel-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?oYBPjhru)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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