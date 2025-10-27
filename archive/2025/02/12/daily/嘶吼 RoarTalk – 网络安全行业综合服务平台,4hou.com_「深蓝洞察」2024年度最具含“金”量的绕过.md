---
title: 「深蓝洞察」2024年度最具含“金”量的绕过
url: https://www.4hou.com/posts/1MMq
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-12
fetch_date: 2025-10-06T20:33:19.009952
---

# 「深蓝洞察」2024年度最具含“金”量的绕过

「深蓝洞察」2024年度最具含“金”量的绕过 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 「深蓝洞察」2024年度最具含“金”量的绕过

企业资讯
[行业](https://www.4hou.com/category/industry)
2025-02-11 15:17:56

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)56422

收藏

导语：基于浏览器漏洞的攻击，自2000年代初出现以来直至今日，一直是一种主流、有效且场景丰富的攻击手段。以下为本期《深蓝洞察 | 2024 年度安全报告》的第二篇。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20250211/1739258253879959.png "1739257717899700.png")

[上期回顾：「深蓝洞察」2024年度最别开生面的安全新生态](https://www.4hou.com/posts/W11o)

基于浏览器漏洞的攻击，自2000年代初出现以来直至今日，一直是一种主流、有效且场景丰富的攻击手段。以下为本期《深蓝洞察 | 2024 年度安全报告》的第二篇。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20250211/1739258257130461.png "1739257717170928.png")

根据市场调查机构Statcounter公布的最新报告，Chrome浏览器无可争议地牢牢占据了市场占有率第一的宝座。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20250211/1739258258188919.png "1739257718423854.png")

https://gs.statcounter.com/browser-market-share#monthly-202412-202412-bar

Chrome以其卓越的安全性而著称，Google安全团队一直致力于研究应用最前沿的漏洞缓解机制。MiraclePtr就是其中最为知名的缓解机制之一，旨在防止浏览器中的UAF漏洞被攻击者利用。

> Chrome中的PartitionAlloc堆分配器在分配和释放对象时维护了一个用户无感知的refcount字段，简单概括MiraclePtr这一缓解机制就是：若对象在被释放时，对该对象的refcount并不是0，这意味着代码中存在危险的引用，这是一个潜在的UAF对象，此时堆管理器会将此危险的对象隔离，从而阻止了后续可能的漏洞利用。

* 2022年6月，全新的安全机制MiraclePtr正式地在Windows和Android平台下的browser进程中启用；
* 2022年9月，扩大启用范围，除renderer进程外的所有进程皆启用；
* 2023年6月，MiraclePtr在全平台启用（ChromeOS, macOS, 和Linux）；
* 2024年7月，Chrome VRP宣布：被MiraclePtr保护住的UAF漏洞将不再视为安全问题。

是什么给了Chrome安全团队如此底气，直接无视这一类严重的内存破坏问题？

想回答这个问题，就不得不提到24年的一例MiraclePtr绕过。在24年的5月，Chrome发布的一则巨额漏洞奖金格外引人注目，其数额高达10万美元，这正是Chrome VRP悬赏的MiraclePtr Bypass的赏金数字。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20250211/1739258259118060.png "1739257718935684.png")

https://chromereleases.googleblog.com/2024/06/stable-channel-update-for-desktop.html

待issue完全公开后，大家才终于明白绕过的细节。PartitionAlloc中在进行refcount加一的操作后，代码中会检测refcount是否溢出，若发生溢出则会触发进程的主动崩溃。

```
CountType old_count = count_.fetch_add(kPtrInc, std::memory_order_relaxed); --------------[1]
// Check overflow.
PA_CHECK((old_count & kPtrCountMask) != kPtrCountMask);  -----------------[2]
```

安全研究员Micky发现，在发生溢出后，这个CHECK并不会立即崩溃，进程处理崩溃相关的逻辑还需要一定的时间，在程序实际停止运行前，仍存在约180ms的时间（在测试环境中），这就给了攻击者生死竞速的机会，攻击者若能在这段时间内完成堆喷占位和后续控制PC等操作，则可以成功利用被MiraclePtr保护的UAF漏洞。

满足攻击成功需要诸多条件：

* 精准地溢出长度为29 bit的refcount字段。
* 释放对象的代码与其他攻击所需的代码不运行在同一线程，且都一定程度受攻击者控制。
* 攻击者可自由地控制目标对象的refcount。
* 在极短的时间窗口内赢得race并完成漏洞利用。

综合了以上种种限制，这就使得这个绕过技术几乎只存在于理论中，但Chrome团队仍慷慨地奖励了这一发现。

除此之外，DARKNAVY于24年11月也发现了MiraclePtr实现上的缺陷，报告给了Chrome团队并得到了确认。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20250211/1739258259850780.png "1739257718142304.png")

综合这一发现以及此前多个高质量漏洞报告，DARKNAVY位列Chrome VRP 2024年度top 20安全研究员/机构。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20250211/1739258261143023.png "1739257718210003.png")

https://issues.chromium.org/issues/386306231

了解这般背景后，不难看出，历史上仅有的绕过方式存在诸多限制，且MiraclePtr缓解机制稳定运转了两年多，时间已经检验了它的有效性，相信Google是在深思熟虑后决定的“无视”大部分UAF漏洞。

Google历经两年多的时间终于基本根除了一个心头大患，这对消费者来说是可喜可贺的。在Chrome的Q3季度总结中还提到了数个对Chrome内存安全的加固，如移除C语言库libpng的依赖，改为使用Rust实现的PNG、JSON等解码；再如将图形渲染模块ANGLE移植到渲染进程中以获得更强大的沙箱保护。这方方面面的努力，无不预示着未来的Chrome将更难以使用内存破坏漏洞突破。

**深蓝洞察**

> 从MiraclePtr的部署到绕过案例的出现，再到其机制的不断完善，Chrome展现的不仅是技术防御的进化，更是一种安全哲学：
>
> 通过奖励机制激励发现潜在问题，通过技术迭代增强整体体系，而非仅关注单点漏洞。
>
> 这种模式体现了Chrome团队对“攻防对抗”的深刻认知——安全从不是一劳永逸的结果，而是一场拉锯战。
>
> 随着安全研究和技术手段的同步发展，Chrome的安全或许无法做到“绝对防御”，但却可以通过这种系统化的策略，将威胁持续降低至可接受的范围，赢取用户的信任，让安全成为产品的核心竞争力。

**参  考：**

[1] <https://gs.statcounter.com/browser-market-share#monthly-202412-202412-bar>

[2] <https://chromereleases.googleblog.com/2024/06/stable-channel-update-for-desktop.html>

[3] <https://issues.chromium.org/issues/386306231>

明日，请继续关注《深蓝洞察 | 2024 年度安全报告》第三篇。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?syy1df6Q)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

这个家伙很懒,什么也没说!

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/aQWl)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

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