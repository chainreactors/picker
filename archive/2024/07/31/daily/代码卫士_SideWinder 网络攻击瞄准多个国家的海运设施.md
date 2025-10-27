---
title: SideWinder 网络攻击瞄准多个国家的海运设施
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520250&idx=2&sn=298380a43c5a67d741a887cc38f55bfb&chksm=ea94be90dde33786aa6c81860e706bc291434bd656bfc414301695529be20b340a55bc39b661&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-31
fetch_date: 2025-10-06T17:44:01.821218
---

# SideWinder 网络攻击瞄准多个国家的海运设施

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSbibIenYMLre3g6d7ouGv3CpUgdC98jCKsT3AXFpoicOuDNbz5ORZJx0BaxnLSWsyibf2mibibZibK42Ig/0?wx_fmt=jpeg)

# SideWinder 网络攻击瞄准多个国家的海运设施

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**国家黑客组织 SideWinder 被指攻击位于印度洋和地中海的港口和海运设施。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSbibIenYMLre3g6d7ouGv3Cmw6WtUb3iaGQsKq7AdqComQfAvrnRaOeqVMXTscG5MDicEiaqLQU2EfpA/640?wx_fmt=gif&from=appmsg)

BlackBerry 研究和情报团队发现了该攻击活动，提到该鱼叉式钓鱼攻击的目标包括多个国家如巴基斯坦、埃及、斯里兰卡、孟加拉国、缅甸、尼泊尔和马尔代夫。

SideWinder 也被称为 “APT-C-17”、”Baby Elephant”、“Hardcore Nationalist”、“Rattlesnake”和 “Razor Tiger”，被指与印度存在关联。该组织自2012年起开始运营，通常利用鱼叉式钓鱼作为交付恶意payload以触发该攻击链的向量。

BlackBerry 提到，“SideWinder 利用邮件鱼叉式钓鱼、文本利用和DLL侧加载技术，避免被检测和传播目标植入。”最新的这些攻击活动利用与性骚扰、员工解雇和工资削减有关，目的是影响收件人的情绪状态，诱骗他们打开有陷阱的word文档。一旦该恶意文件被打开，攻击者就会利用一个已知漏洞 (CVE-2017-0199)与伪装成巴基斯坦港口和航运总局 ("reports.dgps-govtpk[.]com") 来检索 RTF 文件。

该RTF文件会下载利用CVE-2017-11882 的文档，而涉及的漏洞也是在Microsoft Office Equation Editor 中已存在多年的漏洞。攻击者这样做的目的是执行负责启动 JavaScript 代码的 shellcode，但只有确保受陷系统是合法的且威胁行动者感兴趣之后才会实施。

目前尚不清楚 JavaScript 恶意软件所传播的内容，不过从此前 SideWinder 发动的攻击来看，最终目标可能是收集情报。BlackBerry 表示，“SideWinder攻击者继续改进其基础设施以攻击位于新区域中的受害者。该网络基础设施和交付 payload 的稳步演进表明 SideWinder 将继续在可预见的未来实施攻击。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[德勤印度员工竟是计算机黑客团伙头目，七年专攻英国企业等](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514431&idx=2&sn=902256c522d92d4ea1018538355dc38d&chksm=ea948855dde30143a8f93804ebecae7681e7fd34c5dcad54411a3c5fd48f502a73bd4c0e45db&scene=21#wechat_redirect)

[研究员详述巴基斯坦黑客如何攻击印度和阿富汗政府](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247509574&idx=3&sn=aad3f2151c44fa8a4e7bfe994a6172f2&chksm=ea94972cdde31e3aa5116e2349dd1580e5a1971d80f5facd1e476efc207c7b5159461dd47746&scene=21#wechat_redirect)

[网络间谍组织 SideCopy 攻击印度政府和军队组织](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506255&idx=2&sn=bfc4d6e77782f98bf1f0015ab1ce171d&chksm=ea94e825dde36133a95cb324a808ab8fd0bdaa23f39e51b58cfed5f39f5c456c2b025d3bac54&scene=21#wechat_redirect)

[研究人员发现针对印度军队的网络间谍活动](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247495243&idx=2&sn=2ba0729f77d1f1cf9c1bd13800839bb4&chksm=ea94df21dde3563741358047a00d84e634a1c168196a6bce1573f8846cb24e37b5725afbd230&scene=21#wechat_redirect)

[谁在指使这家印度 IT 公司攻击全球政治家、投资者和记者？](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493460&idx=2&sn=ff899a5ce87835dd82e8de632bdfcdfb&chksm=ea94d63edde35f28ea826b3549f684ed22392be986001a468e98a8499d634e41ddcf26b7916f&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/07/new-sidewinder-cyber-attacks-target.html

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