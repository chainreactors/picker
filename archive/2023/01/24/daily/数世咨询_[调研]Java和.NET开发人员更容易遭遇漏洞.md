---
title: [调研]Java和.NET开发人员更容易遭遇漏洞
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247496979&idx=1&sn=96f7d68a74d716551585d051bdc3cc99&chksm=c14487aef6330eb8dfd4c939b0051998a55902aff8704791933bd5e9dc59f4157d8edf8638d5&scene=58&subscene=0#rd
source: 数世咨询
date: 2023-01-24
fetch_date: 2025-10-04T04:39:30.483555
---

# [调研]Java和.NET开发人员更容易遭遇漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y9btpvDIDqqBLaAKgOr2DHbmXtAEGdQ9Pt8QVxtbDVjlJE0qvA0zdxCOPhzQibteubHZQvCvQyKbawdWORLubEw/0?wx_fmt=jpeg)

# [调研]Java和.NET开发人员更容易遭遇漏洞

nana

数世咨询

![](https://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqBLaAKgOr2DHbmXtAEGdQ9o9Tia8hGbJKfQJeuuw51WJhoDSic1FFKTxNx0btfSuvxoF4MhuFrBBlg/640?wx_fmt=png)

开发人员通常将开放式Web应用程序安全项目（OWASP）十大漏洞榜单用作应用程序安全的基准，但超过四分之三的Java和.NET应用程序至少含有一个OWASP榜上漏洞。

上述结论出自安全测试公司Veracode针对近76万个应用程序所做的分析。分析还发现，采用这两个编程生态的应用程序中，大约五分之一至少存在一个高危漏洞。

总体而言，应用程序平均每个月有27%的几率引入至少一个漏洞，编写较差和不经常扫描的应用程序可能存在更多漏洞，而安全流程更完善且由训练有素的开发人员编写的应用程序则不太可能引入新的漏洞。

Veracode战略产品管理副总裁Tim Jarrett表示，分析凸显了将安全集成进开发流程的重要性。

他说道：“数据始终表明，一旦流程中树立起安全惯例，你就会得到更好的结果，无论是在整个漏洞修复方面，还是在减缓漏洞涌现方面。这能起到很大的改善。”

同时，软件公司和开发团队仍在努力清除应用程序代码里的缺陷和漏洞。但Veracode于1月11日发布的《软件安全状况》报告揭示，尽管开发人员和开源项目在加快软件缺陷修复速度，漏洞的平均半衰期仍旧以月计，而非以日或周计。

例如，占调研所分析全部应用程序71%的Java和.NET应用程序，就分别在243天和158天之后仍有半数漏洞留存。

![](https://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqBLaAKgOr2DHbmXtAEGdQ9Io2EenKykhUczJc8vd4bUs6LU8iapuUsh3YIjRxCF3zQ1RWkyRMhU4g/640?wx_fmt=png)图：Verocode《软件安全状况》报告

应用程序膨胀和过时都会对其安全性产生极大影响。平均而言，应用程序的代码量增加了40%左右，更可能存在漏洞。分析发现，面世两年的应用程序中大约54%存在漏洞，推出五年之久的应用程序则69%都存在漏洞。

**JavaScript的安全性令人颇感意外**

出乎意料的是，用JavaScript编写或者采用JavaScript框架的应用程序在漏洞扫描中往往表现更好。大约80%的Java和.NET应用程序都存在漏洞，但仅有56%的JavaScript应用程序含有漏洞。同时，约20%的Java和.NET应用程序存在高危漏洞，但JavaScript应用程序存在高危漏洞的比例不足10%。

Jarret表示，JavaScript框架更新，安全性更强，而且具有开源生态的优势，而Java从开源生态获益较晚。

“JavaScript是较新的编程语言，所以用JavaScript编写的应用程序也更新，而且之前的分析报告也告诉我们，应用程序的年限和漏洞修复时间之间存在关联。适用于JavaScript的很多工具都相当成熟了，这种编程语言受到完备的支持。”

此外，Java应用程序中的漏洞是个第一方问题，需要开发人员自己来修复，而在JavaScript和Node.js框架中，漏洞往往是个第三方问题，因为漏洞往往出现在软件依赖的组件中。

“很大程度上，Java应用程序安全问题的修复方式仍旧是修改类文件再编译之。”Jarret称，“而在JavaScript应用程序中，漏洞修复更像是个包管理问题。这对于开发人员来说就是另一码事了，包管理可能更加简单。”

**新编程语言式微**

报告数据还凸显出开发人员想要学习的编程语言和大多数企业实际在用的编程语言之间的差异。Veracode观察到的主流编程语言和生态，即Java、.NET和JavaScript，并非开发人员的编程技术之选。

Stack Overflow的《2022年开发者调查》揭示，JavaScript和基于JS的框架，如Node.js、React.js和Angular，统领开发人员首选技术榜单；而Java是最不受待见的编程语言——54%的受访者都非常害怕Java，只有46%喜欢这种语言。

然而，Veracode扫描的应用程序中，用Java编写的占据了近半壁江山（44%），用JavaScript编写的仅占14%。

此外，开发人员最钟爱的编程语言Rust，甚至都没在Veracode的数据中出现；而在开发人员心目中排名第六的编程语言Python，只占了所扫描应用程序的不到4%。

Veracode战略产品管理副总裁Jarret表示，出现这种割裂的部分原因在于，成熟应用程序是用成熟编程语言编写的。

“所有代码如果是座海上冰山，新兴开发就是冰山的山尖尖，只有在这么小块地方你才会看到人们选择Go、Rust、Dart和Flutter。”

由于大量应用程序代码库都是用这些成熟的老旧编程语言编写的，这种情况不太可能会改变。

“很遗憾，老旧应用程序长存不死，所以企业里存在很多具有这些笨重Java代码库和.NET代码库的关键应用。”

Verocode《软件安全状况》报告
*https://www.veracode.com/state-of-software-security-report*

Stack Overflow《2022年开发者调研》
*https://survey.stackoverflow.co/2022/#technology-most-loved-dreaded-and-wanted*

---

**参考阅读**[2022年应用安全报告：重要趋势与挑战](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247494727&idx=1&sn=12f51bf32ac2399cdba2bce8ba0f4c55&chksm=c1449efaf63317ecc446fe337c774cc28059a4dfe42c7d9b15c3247ed7ccce4b0b7bf10d605a&scene=21#wechat_redirect)
[2022年漏洞管理报告要点梳理](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247496726&idx=2&sn=50c1973dbbcc1cb9bab81cd0f5e6d8e6&chksm=c14486abf6330fbdafdffde25d7affddc2f35eb7e064532f2ea248d20cd4d4fb496eada04922&scene=21#wechat_redirect)
[漏洞管理方案的最佳实践](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247495582&idx=1&sn=b78286f57e616df92c46ca2cea4f977f&chksm=c1449d23f6331435e9dcb4816d78bed2e38423d4945385fd5548fe32bebf206f2d71cf6047cd&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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