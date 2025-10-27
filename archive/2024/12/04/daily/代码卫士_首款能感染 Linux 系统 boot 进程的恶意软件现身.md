---
title: 首款能感染 Linux 系统 boot 进程的恶意软件现身
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521662&idx=2&sn=c4ed3ee2f3d46bda404068445f0b9abe&chksm=ea94a414dde32d023e435d79581f93d4f2889247816d38c8514bdaf158dd9a38e43dca8527a6&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-04
fetch_date: 2025-10-06T19:38:48.592589
---

# 首款能感染 Linux 系统 boot 进程的恶意软件现身

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMShIM3W4kDlRhQev1NIsmKPFgryoKLf4icLl7fBvvfA4Mcia9icSwDqxPiaCtZkukzgGAY6EwM9nn2QoQ/0?wx_fmt=jpeg)

# 首款能感染 Linux 系统 boot 进程的恶意软件现身

Jai Vijayan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMShIM3W4kDlRhQev1NIsmKPqykjXIX85BYSTyKWnNdczkLcnmB93uFlT9zHpiaR7c7ZxRkE1SmHu8g/640?wx_fmt=png&from=appmsg)

**研究人员发现首款能够感染 Linux 系统 boot 进程的恶意软件，名为 “Bootkitty”。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMShIM3W4kDlRhQev1NIsmKPfoa6IvF8ibibzNGc4T5jfueNibZpAl083TG9xaswwibW1m6mJLksHz504Q/640?wx_fmt=gif&from=appmsg)

Bootkitty 是韩国学生为一款网络安全训练程序开发的概念验证代码。尽管尚未开发完成，但该bootkit 已可完全运行，甚至其中包含Binarly 公司在2023年11月发现的UEFI 生态系统中 LogoFAIL 多个漏洞其中之一的exp。

**新型概念验证**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMShIM3W4kDlRhQev1NIsmKPfoa6IvF8ibibzNGc4T5jfueNibZpAl083TG9xaswwibW1m6mJLksHz504Q/640?wx_fmt=gif&from=appmsg)

Bootkit 在固件级别操作并在操作系统加载之前执行，从而在启动阶段绕过为保护系统免遭恶意软件攻击的安全启动进程。这类恶意软件在系统重启、操作系统卸载以及取代某些部件如硬盘驱动后，仍然存活。

ESET公司的研究员上个月从 VirusTotal 发现了一份 Bootkitty 样本并分析提到，它是首款针对 Linux 的UEFI bootkit。也就是说现在之前，包含 BlackLotus 和 FinSpy 等最臭名昭著的 bootkit 一直针对的只是 Windows 系统。

ESET 公司的研究员提到，“Bootkitty 的主要目标是禁用内核的签名验证特性，并通过 Linux 初始化进程（Linux 内核在系统启动时执行的首个进程）来预加载两个未知的 ELF 二进制。”

Binarly 公司也分析了 Bootkitty，该公司指出，该恶意软件中包含CVE-2023-40238的exp。该漏洞是该公司在去年发现的多个图像解析漏洞 LogoFAIL 中的一个。该 Bootkitty exp 利用 BMP 文件中内嵌的 shellcode 绕过安全启动进程并使OS 信任该恶意软件。该公司还提到多家厂商易受该exp影响，包括但不限于富士通、惠普等。

Binarly 公司的研究人员提到，“虽然它似乎只是概念验证而非活跃威胁，但Bootkitty 标志着攻击者将 bootkit 攻击扩展到 Windows 生态系统之外的重大变化。该操作系统启动加载器是庞大但常被防御人员忽略的攻击面，复杂度的不断提升让情况更加糟糕。”

UEFI（即此前的BIOS 生态系统）是近年来攻击者的热门目标，因为恶意软件在该层面的操作方式导致它在受陷系统上实际上仍然是无法检测到的。但随着首款可绕过完全打补丁的 Windows 系统安全启动防御措施的恶意软件 BlackLotus 的出现，关于 UEFI 安全的担忧爆发。

该恶意软件利用的是UEFI安全启动进程中的两个漏洞CVE-2022-2189和CVE-2023-24932将其以无法检测和无法删除的方式安装。这款恶意软件相对容易获得，加上微软难以轻松修复的情况，促使CISA呼吁改进UEFI 防御措施。CISA当时提到，“从最近对 UEFI 恶意软件如 BlackLotus 的事件响应情况来看，网络安全社区和UEFI 开发人员似乎仍然处于学习模式。具体而言，UEFI安全启动开发人员并未全部执行PKI实践以启用补丁分发。”

**起作用的bootkit**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMShIM3W4kDlRhQev1NIsmKPfoa6IvF8ibibzNGc4T5jfueNibZpAl083TG9xaswwibW1m6mJLksHz504Q/640?wx_fmt=gif&from=appmsg)

ESET 公司发现，Bootkitty 能够在内存中修改函数，这些函数通常负责验证用于加载Linux 内核在启动阶段的 GRUB 的完整性。然而，Bootkitty 试图在内存中修改的特定函数仅受少量 Linux 设备的支持，表明该恶意软件只是概念验证而非活跃威胁，这可从代码中存在多个未使用部件（含两个用于在执行过程中打印ASCII 艺术和文本的两个函数）中看出。

ESET公司援引开发该bootkit的韩国学生的话表示，他们创建该恶意软件的目的是引起大家对针对 Linux 系统的bootkit的重视。该恶意软件的详情将在之后的安全会议上发布。不过这些学生表示，发现VirusTotal上已出现该bootkit的一些样本。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[严重的 BootHole 漏洞影响所有 Linux 发行版和 Windows 系统（详细分析）](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247494336&idx=1&sn=0e928f1f328cb2dc556e3b3676f80fad&scene=21#wechat_redirect)

[这个 root 漏洞已存在10+年之久，影响Ubuntu Linux](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521546&idx=1&sn=deaef16f3522dccfad4051c26652ad09&scene=21#wechat_redirect)

[因“合规要求”，Linux Kernel 清除了11名俄罗斯开发者的维护者身份](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521303&idx=2&sn=a8f19bf98fa3d8e84ee9c612d1f1d98c&scene=21#wechat_redirect)

[0.0.0.0 Day漏洞已存在18年，影响 MacOS和Linux设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520401&idx=1&sn=fcb5f892311d2858672c9908d0e08554&scene=21#wechat_redirect)

[Linux 内核受新的SLUBStick 跨缓存攻击影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520334&idx=1&sn=836f6bce19d0adc20c9deedfee1cf1de&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/cyber-risk/bootkitty-first-bootloader-target-linux-systems

题图：Pixabay License

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