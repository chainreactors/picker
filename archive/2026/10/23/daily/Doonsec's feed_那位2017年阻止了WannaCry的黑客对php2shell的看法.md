---
title: 那位2017年阻止了WannaCry的黑客对php2shell的看法
url: https://mp.weixin.qq.com/s/Gja5uR7W3tLnYxEAgfukew
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:44:08.768694
---

# 那位2017年阻止了WannaCry的黑客对php2shell的看法

# 那位2017年阻止了WannaCry的黑客对php2shell的看法

tuto
tuto

杂杂咱谈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

我得承认，我在漏洞利用开发方面很平庸，但我接触过足够多的极其优秀的漏洞利用开发者，所以我可以肯定地说:

任何声称自己"轻松"用AI生成了一个可用的php2shell漏洞利用的人，要么是:

a) 世界一流的漏洞利用开发者，患有极端冒充者综合征。

b) 目前正盯着某个听起来很自信但完全错误的LLM输出。

基于我在GitHub上看到的那些AI幻觉生成的漏洞利用数量，我相当确定是后者。威胁行为者还在用"php2shell"漏洞利用疯狂轰炸我的蜜罐网络，这些利用不仅不起作用，甚至离漏洞实际工作原理差了十万八千里。

我已经在多个所谓的"php2shell漏洞利用"中看到了附图中的相同技术，包括GitHub上一个有超过100个星标的那个。问题是，这不是php2shell，甚至根本不是漏洞。这是一种名为"会话投毒"的技术，可以被用来利用PHP应用中的本地文件包含(LFI)漏洞(不是PHP本身)。

它与CVE-2026-109618/CVE-2026-109619唯一的共同点是它们两者都是同时使用了"PHP\_SESSION\_UPLOAD\_PROGRESS"功能。而且，两者的缓解建议都提到了将"session.upload\_progress.enabled"设置为"Off"。

人们把漏洞的零散细节塞进LLM，LLM抓住了"PHP\_SESSION\_UPLOAD\_PROGRESS"这个字符串，然后生成与实际CVE毫无关系的会话投毒代码。而且因为做这件事的人完全不知道自己在干什么，他们自信满满地把他们的"概念验证漏洞利用"发到GitHub上，并在社交媒体上分享。

所以如果你看到有人谈论"会话投毒+LFI"，很可能他们的LLM基于Orange Tsai 2018年的一篇关于本地文件包含攻击向量的博客，幻觉出了一个漏洞利用。

更糟糕的是，"安全研究员"们接着用LLM来分类这些利用尝试，也受害于同样的幻觉，然后确认存在正在进行的大规模利用(目前并没有)。

真正的漏洞利用非常难利用，到目前为止，我还没见过任何人成功地在超过少数几个高度特定配置的PHP版本上让它工作。

LLM在熟练专业人士手中是有用的工具，但对其他人来说，它们往往只是邓宁-克鲁格效应的加速器。

显然，利用PHP漏洞远没有许多人最初想象的那么简单。

几乎所有流传的利用工具都是AI垃圾！

所以说网络上的poc可信度可利用度都是不高的？

附:

CVE-2026-115560 新的RCE漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xoBWaEOhvRFkwCtC2m5ZWuP9k7tTAcIjFxwSwuvEL1k1bxGacsEY1pibDBzqAhp07QkJAXcLVk0TiaV63dDhjz5BXar8icFxiaQrN7gymglWOibc/640?wx_fmt=png&from=appmsg)

https://www.php.net/archive/2026.php#2026-10-23-1

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LCF75xtxMiaiaUiauC6TKOGdQ4TYySakdjbD0xCM5iakCGJ1S98zU7AahSSrSrtoqdNQUSjoQZ2ia7KHDichAXQSQsPw/0?wx_fmt=png)

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