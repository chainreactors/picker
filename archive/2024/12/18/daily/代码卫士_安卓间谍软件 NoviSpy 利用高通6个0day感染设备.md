---
title: 安卓间谍软件 NoviSpy 利用高通6个0day感染设备
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521826&idx=2&sn=2e115cf641ac90636ca05cde8df5fa09&chksm=ea94a748dde32e5e240c297499b4a7753baff26f7b887420df59da0631b3b45cc44b73026012&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-18
fetch_date: 2025-10-06T19:42:27.189421
---

# 安卓间谍软件 NoviSpy 利用高通6个0day感染设备

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTjkvuqYkg1eXE7YH0LtsaE4IibkKSmjSJt8kF2CUPtInU2r5hCaMqPEeibNtRoicF7ZyOfBPibRODcew/0?wx_fmt=jpeg)

# 安卓间谍软件 NoviSpy 利用高通6个0day感染设备

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**塞尔维亚政府利用高通的多个0day漏洞，解锁并通过新型间谍软件 “NoviSpy” 感染安卓设备，监控活动家、记者和抗议人员。**

与这些攻击相关联的其中一个高通漏洞是CVE-2024-43047。谷歌 Project Zero 团队在2024年10月将其标记为已遭活跃利用的0day漏洞，安卓在11月份获得修复方案。

从通信内容来看，这款间谍软件似乎由塞尔维亚当局部署。该通信由Amnesty International 安全实验室查看记者从警局取回的手机时发现。该实验室在一份报告中提到，“2024年2月，位于塞尔维亚季米特洛夫格勒市的一名报道本地新闻的独立记者 Slaviša Milanov，因看似平常的交通违章被带到警局。Slaviša获释后，发现自己按警察要求放到警局前台的手机表现奇怪：数据和无线设置被关闭了。Slaviša认为这可能是被黑的迹象，并出于对塞尔维亚记者所面临的监控威胁的警惕，联系 Amnesty International 安全实验室分析自己的手机。”

随后，研究员向谷歌威胁分析团队TAG提供了利用工件，发现了位于高通DSP 驱动中的缺陷。该驱动用于将多媒体处理卸载到DSP核心。虽然谷歌不确定NoviSpy 利用了哪些漏洞，但有证据表明这款间谍软件通过一个利用链绕过了安卓安全机制并将自身持久地安装在内核层。

**NoviSpy 部署在塞尔维亚**

报告提到，塞尔维亚安全信息局 (BIA) 和塞尔维亚警察在对设备进行物理监管期间，使用 Cellebrite 解锁工具解锁手机后，部署了 NoviSpy。

从被遭篡改设备上的取证证据来看，研究人员认为 Cellebrite 利用高通的多个0day漏洞解锁安卓手机。报告提到，“在做研究期间，安全实验室还发现了取证证据，安卓中的一个提权0day漏洞用于在塞尔维亚一名活动家的设备上提权。该漏洞是与安卓厂商谷歌的安全研究员协同发现的，影响使用热门高通芯片集的数量庞大的安卓设备，影响全球数百万台安卓设备。”

该间谍软件和与BIA直接相关的IP范围的服务器进行通信，而样本中的配置数据发现了与该国之前间谍软件采购计划相关的一名人员。间谍软件的目标包括记者、人权活动家和政府异见人士。报告中提到的特定案例包括 Slaviša Milanov、Krokodil非政府组织的一名成员以及三名活动家。不过，研究员表示这些技术证据表明，在过去几年NoviSpy 至少被安装在数十台甚至数百台安卓设备中。

从最初的攻陷来看，Amnesty International 表示，恢复的工件与利用安卓呼叫特性如 Voci-over-Wifi 或VoLTE 功能的一次零点击攻击活动有关。它们存在于已查看的失陷设备中，是 RCS 呼叫的一部分。报告提到，一些活动家可能已遭一个零点击安卓漏洞利用的攻击。从由很多数位组成的不合法电话号码处接收电话通话即可利用该漏洞。

**谷歌发现多个高通缺陷**

谷歌TAG收到由 Amnesty International 捕获的利用所生成的内核 panic 日志，修复了高通adsprpc 驱动中的6个漏洞。这些驱动用于数百万台安卓设备。

这六个漏洞如下：

* CVE-2024-38402: 驱动中的引用计数问题可导致内核空间中的释放后使用和任意代码执行后果。
* CVE-2024-21455: 'is\_compat'标记处理存在问题，可导致受用户控制的指针被当作内核指针处理，从而创建任意读/写原语并导致提权后果。
* CVE-2024-33060: 'fastrpc\_mmap\_create' 中的条件竞争导致驱动易受释放后使用漏洞的影响，在处理全局内存映射时尤为如此，可造成内核内存损坏后果。
* CVE-2024-49848：处理持久映射中的逻辑错误在映射引用发布不当时触发释放后使用场景，造成持久性机制。
* CVE-2024-43047：'fastrpc\_mmap' 中的内存映射重合问题可导致对象引用损坏，可能导致内存损坏后果。
* 无CVE编号：fastrpc\_mmap\_find 验证不当问题泄露内核地址空间信息，导致内核地址空间布局随机化（KASLR）遭绕过。

谷歌研究员证实CVE-2024-43047已遭利用并假设称余下漏洞在复杂攻击链中遭利用。在本文写作之时，高通尚未发布 CVE-2024-49848的补丁，尽管谷歌已在145天前就将其告知高通。谷歌也提到，高通超过了对CVE-2024-49848和CVE-2024-21455的打补丁期限，打补丁的行业标准期限为90天。

对此，高通的一名发言人提到，“开发支持强健安全性和隐私性的技术是高通技术公司的优先工作。我们感谢谷歌Project Zero 和 Amnesty International 安全实验室研究人员的协同披露。针对他们的FastRPC 驱动研究，自2024年9月开始，我们已经向客户提供了修复方案。我们鼓励终端用户届时应用设备厂商推出的安全更新。”

高通表示，CVE-2024-49848的修复方案已开发，目前在走披露流程，相关的安全通告将于2025年1月发布。关于无CVE编号的漏洞，高通表示其补丁已在2024年9月份与CVE-2024-33060的补丁封装，因此已得到修复。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[谷歌修复已遭利用的两个安卓 0day 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521406&idx=1&sn=af981c3476e81115ffa11866a0bb7b7d&scene=21#wechat_redirect)

[谷歌修复已遭利用的安卓内核0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520345&idx=2&sn=e480c7108b41c03d874e5bd6bc1c39bf&scene=21#wechat_redirect)

[Telegram 0day可导致攻击者将恶意安卓APK以视频形式发送](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520167&idx=2&sn=7d6a9321b744778cdce41dc0464f4c3d&scene=21#wechat_redirect)

[Crowdfense 出价3000万美元收购安卓、iOS和浏览器0day利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519250&idx=1&sn=a9eb759176bc25d080dd038567016edc&scene=21#wechat_redirect)

[谷歌修复已遭利用的安卓 0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517584&idx=1&sn=37b84a3349271c0f40eb59108b6ebf14&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/new-android-novispy-spyware-linked-to-qualcomm-zero-day-bugs/

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过