---
title: 英特尔的SGX 崩溃了？别慌！
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520613&idx=2&sn=e824d92177a0c7fa364083bc68bbf256&chksm=ea94a00fdde32919a1eca24c3e4c23055e1b083a071fb86ebd32514d7fb5341525d2ebe31cf7&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-29
fetch_date: 2025-10-06T18:05:10.738721
---

# 英特尔的SGX 崩溃了？别慌！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSwic8nfoftiaOqRzibJpyh8DHEtSu563VumPeIza7Ijs1oI7A28gP3onOCicJxTyE9cADKaUnsZZTNfA/0?wx_fmt=jpeg)

# 英特尔的SGX 崩溃了？别慌！

Simon Sharwood

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**最近关于英特尔公司的软件防护扩展 (SGX) 安全系统易遭滥用的新闻可能言过其实了。**

Positive Technologies 公司的俄罗斯研究员 Mark Ermolov 发现，一个编码错误可导致攻击者完全访问SGX 的安全飞地。似乎本应安全的数据可能通过已达生命周期的 Gemini 客户端和服务器系统以及虽老旧但受支持的 Xeons 进行访问。

Ermolov 发文表示，“经过数年的研究，我们最终提取了 Intel SGX Fuse Key0，即 Root Provisioning Key。它与 FK1或 Root Sealing Key（也受陷）一起，代表的是 SGX 的根信任。它们真的在竭尽全力地保护该密钥：ucode 部分完美运行但他们忘记清理持有从熔断器控制器获得的所有熔断器（包括 FK0）的内部缓冲区。”

这一消息很糟糕。Key0 访问权限可使攻击者完全访问 SGX中的任何安全数据，而且虽然英特尔已经弃用客户端处理器系统，但很多仍在运行中，尤其在嵌入式系统中更是如此。

不过，英特尔公司指出，要让攻击起作用，攻击者不仅要物理访问机器，这些问题还必须都是未修复状态，“Positive Technologies 公司所找到的问题基于DFX Aggregator 逻辑中此前已被缓解的漏洞，要求物理访问不具备 Intel 固件版本控制能力的Gemini Lake 系统。攻击者必须物理访问受此前漏洞（CVE-2017-5705、CVE-2017-5706、CVE-2017-5707和CVE-2019-0090）影响从而可实现Intel 解锁状态的且未得到缓解的系统。英特尔公司已经为这些漏洞提供了缓解措施。”

话虽如此，Gemini 处理器仍然有很多。显然，它并不位于高性能区域——英特尔在去年弃用了 Gemini，但它们仍然存在。约翰霍普斯金大学的研究员 Pratyush Tiwari 表示，在这些处理器上运行的任何东西都用于飞地中，所有这些可信飞地很可能不再值得信任。”

问题在于用于锁定 SGX 的软件。糟糕的编程可导致攻击者获得对 SGX锁定材料的访问权限，尽管目前尚不清楚攻击是否可远程进行还是需要本地访问权限。

SGX 在2015年连同 Skylake 处理器系列一起推出，本应保护甚至是制造商自己的密钥代码，但它很快遇到问题。SGX虽然在后续芯片中被弃用但它仍然存在，尤其有很多嵌入式系统仍然依赖于它。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[研究员使用新型CPU攻击技术 “SmashEx” 攻破 Intel SGX](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247508508&idx=3&sn=2ec7c592224e06ed77569dd2dc239bbb&chksm=ea949376dde31a60ee08a388f4c89bd1b3afd8c935ca664bf005a3d537eaabb4f3eb0c8c337b&scene=21#wechat_redirect)

[30美元攻陷Intel SGX enclave，Intel 不打算修复](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247497314&idx=2&sn=d3f512263e2d8b35e8db046474c74651&chksm=ea94c708dde34e1ed242e97961c70b6d772c42aa727c5f8e9c3c97d7aaade8e673b2f17b5cb4&scene=21#wechat_redirect)

[Spectre 攻击变体 SgxSpectre 现身 能从 Intel SGX 封装中提取数据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247486594&idx=2&sn=cd651cff5346815a5012d56047d6d897&chksm=ea973de8dde0b4febae9f3134b22ea3faf95002d1da1794e662af1938e9980a88bdffa19e693&scene=21#wechat_redirect)

[研究人员展示因特尔SGX如何泄露密钥](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485571&idx=5&sn=426324adabd862a00bcbff5cf4f7fe9f&chksm=ea9739e9dde0b0ff9f0c7c870e72bc49656a62c8c5cf87f81b932904be1b21eb9300bd74e952&scene=21#wechat_redirect)

**原文链接**

https://www.theregister.com/2024/08/27/intel\_root\_key\_xeons/

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