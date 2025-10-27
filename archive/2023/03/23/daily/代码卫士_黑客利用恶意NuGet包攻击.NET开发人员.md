---
title: 黑客利用恶意NuGet包攻击.NET开发人员
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516005&idx=2&sn=8ccfbfa2c6c7f2cdcdeec6e438b0c42b&chksm=ea948e0fdde3071930ec2a7d165d6c048dc678b9150e6ef75295c477a49813c801510facb385&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-23
fetch_date: 2025-10-04T10:23:16.379107
---

# 黑客利用恶意NuGet包攻击.NET开发人员

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQQ2tqs0GRCnrmRXuqk3UIiawCYf7kmjokW4sI8kTZmVqmOQPVjoVDKtTE6g13q07o4mer4WyqTetA/0?wx_fmt=jpeg)

# 黑客利用恶意NuGet包攻击.NET开发人员

Robert Lemos

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQQ2tqs0GRCnrmRXuqk3UIiaBicZcRc1PQbaBKnyPBwFv094lW6vIYqIiaJp3VfCrXx39ZgJWJ3J50eQ/640?wx_fmt=png)

**JFrog 发布分析报告称，托管在 .NET 软件开发人员 NuGet 仓库上的数十个程序包实际上是恶意木马组件，它们将攻陷安装系统并下载含有后门功能的密币窃取恶意软件。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQQ2tqs0GRCnrmRXuqk3UIiaCrwNzKa56aT79kcoWvTrTXVrLRliam3PplzszrSorYJfVH12m7m6h8Q/640?wx_fmt=png)

报告指出，该程序包已下载超过16.6万次，它模拟为其它合法软件如Coinbase和微软 ASP.NET。研究人员发现init.ps1文件在安装时执行，随后下载并执行了一个可执行文件后，检测到这起攻击。发现恶意代码意味着攻击者正在进一步攻陷软件供应链，从而攻陷开发人员。

该公司的安全主管Shachar Menashe 认为，“在NuGet 程序包安装时执行恶意代码的方式虽然不难，但在Python或JavaScript中很少见到，其中一些已不受重视，因此一些初级攻击者认为不可能实现。NuGet可能能够更好地自动过滤恶意包。”

软件供应链遭受的攻击越来越多，攻击者试图攻陷开发人员的系统或将无人注意的代码通过开发人员的应用程序发送给终端用户。PyPI和NPM生态系统常常是开源供应链攻击的目标。

.NET 软件生态系统由近35万个唯一程序包组成，这次攻击是恶意包首次针对NuGet的攻击，不过该公司还指出，此前曾有垃圾邮件攻击将钓鱼链接发送给开发人员。

**Typosquatting仍然是个问题**

这次攻击说明，typosquatting 仍然是个问题。这种攻击涉及创建与合法包具有类似名称的程序包或包含常见拼写错误名称的程序包，寄望于用户将错误拼写常见包或不会注意到错误。

开发人员应当在使用新包时多加注意。研究人员指出，“尽管NuGet仓库此前并未发现恶意代码攻击，但我们能够找到通过typosquatting等方法分发恶意代码的至少一起攻击。和其它仓库一样，应当在该软件的开发生命周期的每一步采取安全措施，确保软件供应链的安全。”

**立即执行代码问题重重**

研究人员指出，被开发工具自动执行文件的功能是一个安全弱点，应当被清除或被限制以减少攻击面。相比Go包生态系统，该功能是NPM和PyPI生态系统存在投毒问题的一个重要原因。

研究人员指出，“尽管NuGet之前已删除了所发现的恶意包，但由于NuGet 包中仍然包含在包安装时立即运行代码的功能， .NET 开发人员仍然处于高风险中。尽管已不受重视，但初始化脚本仍然适用于Visual Studio，在安装NuGet包时没有任何警告就会运行。”

JFrog公司建议开发人员检查所导入和安装的程序包中是否存在输入错误，并表示开发人员应当确保“不要在项目中不慎安装这些包，或者将其提及为依赖”。另外，开发人员应当查看程序包内容，确保没有下载并自动执行可执行文件。虽然这类文件在一些软件生态系统中很常见，但他们通常表明恶意意图。

该NuGet以及NPM和PyPI 仓库已经采取一系列措施，虽然缓慢但肯定消除了这些安全弱点。他表示，“我认为NuGet未来将不会成为攻击目标，尤其是在NuGet 维护人员将完全去除在包安装时运行代码的情况下，他们实际上已经开始这么做了。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[第三方依赖关系的风险：利用数十个易受攻击的 NuGet包瞄准 .NET 平台](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506255&idx=1&sn=5dff2ef15506b4ba509e43afdb2a22d8&chksm=ea94e825dde36133ca8a76bcae239a587bc8d70d829538a83e9bd71b020a584d93437c3ccb70&scene=21#wechat_redirect)

[本周起，GitHub强制要求活跃开发人员执行2FA机制](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515900&idx=1&sn=7af020d3e088fab4b57a745603e09389&chksm=ea948f96dde3068079b9292ed144160bf188c1e4eae8b756deaec8121df464d81e8cde52e99d&scene=21#wechat_redirect)

[Python 开发人员提醒：PyPI 木马包假冒流行库发动攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515700&idx=2&sn=28c134528939223ed316b6f5b450dcd6&chksm=ea948f5edde306489a6bb564bbb5995de242208d44ab2dde95fce873e09f15d1fc295584cb61&scene=21#wechat_redirect)

[开发人员注意：VSCode 应用市场易被滥用于托管恶意扩展](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515219&idx=1&sn=faa32338df1d68e7cd738a80222f3a44&chksm=ea948d39dde3042f86e921180dbc7e21443164668b07c9b20a7252306940ec30acb34b5c7c49&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/application-security/net-devs-targeted-with-malicious-nuget-packages

题图：Pexels License

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