---
title: 新型Rowhammer攻击变种可绕过SK Hynix DDR5内存最新防护机制
url: https://www.4hou.com/posts/jB1W
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-25
fetch_date: 2025-10-02T20:37:50.830645
---

# 新型Rowhammer攻击变种可绕过SK Hynix DDR5内存最新防护机制

新型Rowhammer攻击变种可绕过SK Hynix DDR5内存最新防护机制 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型Rowhammer攻击变种可绕过SK Hynix DDR5内存最新防护机制

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)35548

收藏

导语：目前，Phoenix攻击所利用的漏洞已被标记为CVE-2025-6202，危险等级为“高”。

目前，研究人员已开发出一种新型Rowhammer攻击变种，能够绕过SK Hynix DDR5内存芯片上的最新防护机制。

Rowhammer攻击的原理是：通过高速读写操作反复访问内存单元的特定行，产生足够强的电干扰，使相邻位（bit）的值在0和1之间异常翻转（即“位翻转”）。攻击者可借此破坏数据、提升系统权限、执行恶意代码，或获取敏感数据。

针对Rowhammer攻击的主流防护机制之一是“目标行刷新（Target Row Refresh，TRR）”——当检测到某一内存行被频繁访问时，TRR会发出额外的刷新指令，从而防止位翻转。

**针对DDR5的Rowhammer攻击：以提权为目标**

瑞士苏黎世联邦理工学院计算机安全小组与谷歌的研究团队合作，开发了一种名为“Phoenix”的新型DDR5 Rowhammer攻击技术。该技术可通过触发内存芯片中的位翻转，为恶意活动创造条件。

研究团队的测试基于Hynix的DDR5产品——Hynix是全球最大的内存芯片制造商之一，市场份额约36%，但此类安全风险或同样波及其他厂商的产品。

研究人员首先对Hynix为抵御Rowhammer攻击所设计的复杂防护机制进行逆向工程，摸清其工作原理后发现：该防护机制并未对某些刷新间隔进行采样监测，这一漏洞可被攻击者利用。

此外，团队还为Phoenix开发了一种同步方法：当检测到错过某次刷新操作时，攻击程序会自我修正，从而实现对数千次刷新操作的跟踪与同步。

为绕过TRR防护，Phoenix攻击中的Rowhammer模式覆盖了128个和2608个刷新间隔，并仅在精准时机对特定“激活时隙”发起攻击。

借助这套攻击模型，研究人员成功在测试池中所有15块DDR5内存芯片上触发了位翻转，并开发出首个基于Rowhammer的权限提升漏洞利用程序。

测试显示，在“采用默认设置的商用DDR5系统”上，研究人员仅用不到两分钟就获取了具备root权限的shell（命令行界面）。

**实际攻击场景测试与风险范围**

研究人员还探索了Phoenix攻击技术的实际利用可能性，以验证其能否控制目标系统：

1. 内存读写权限突破：通过攻击页表项（PTEs）构建“任意内存读写原语”时，发现所有测试产品均存在漏洞；

2. SSH认证破解：针对共存虚拟机的RSA-2048密钥发起攻击，试图破坏SSH认证，结果显示73%的双列直插内存模块易受攻击；

3. 本地权限提升：通过篡改sudo二进制文件，尝试将本地权限提升至root级别，在33%的测试芯片上成功实现这一目标。

![Phoenix_Rowhammer-attacks.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250916/1758012394190573.jpg "1758012050140757.jpg")

所有测试过的DDR5模块都对新的Phoenix Rowhammer攻击易感

测试数据表明，所有受测内存芯片均易受Phoenix攻击所使用的至少一种Rowhammer模式影响。其中，覆盖128个刷新间隔的较短模式效果更显著，平均触发的位翻转次数更多。

**漏洞评级与防御建议**

目前，Phoenix攻击所利用的漏洞已被标记为CVE-2025-6202，危险等级为“高”，影响2021年1月至2024年12月期间生产的所有DIMM内存模块。

尽管Rowhammer是全行业性的安全问题，且无法通过修复现有内存模块彻底解决，但用户可通过将DRAM刷新间隔（tREFI）延长至原来的三倍，来阻止Phoenix攻击。不过，这种操作可能导致内存出现错误或数据损坏，进而引发系统不稳定。

研究团队已发表题为《Phoenix：基于自修正同步的DDR5 Rowhammer攻击》的技术论文，并计划于明年在IEEE安全与隐私研讨会上展示该研究成果。

此外，研究人员还公开了一个资源仓库，内含可复现Phoenix攻击的相关材料，包括：基于现场可编程门阵列（FPGA）逆向工程TRR实现的实验数据，以及概念验证漏洞利用程序的代码。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-phoenix-attack-bypasses-rowhammer-defenses-in-ddr5-memory/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GOTCibAh)

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