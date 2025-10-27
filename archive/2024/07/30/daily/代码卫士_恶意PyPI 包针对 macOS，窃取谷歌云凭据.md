---
title: 恶意PyPI 包针对 macOS，窃取谷歌云凭据
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520240&idx=2&sn=549c4734cb750f652f9105a8e5df0546&chksm=ea94be9adde3378cb08b546c169a09789a83585332fb65831b5ffee17189c48aba808fc2a92c&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-30
fetch_date: 2025-10-06T17:45:06.762649
---

# 恶意PyPI 包针对 macOS，窃取谷歌云凭据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMR5ak8ywjbpVBaJuu0EfeUQOTHTN4ibSFFJXssVibobc8zf9oa5xD727aoVf9ibC2SlwyEjia1EZSicGibw/0?wx_fmt=jpeg)

# 恶意PyPI 包针对 macOS，窃取谷歌云凭据

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全研究员发现了 PyPI 仓库中的一个恶意包，它针对苹果 macOS 系统，窃取受害者的谷歌云凭据。**

该恶意包名为 “Ir-utils-lib”，在被下线前共有59次下载。它在2024年6月初被上传到该注册表。

Checkmarx 公司的安全研究员 Yehuda Gelb 在上周五的一份报告中提到，“该恶意软件通过预定义哈希，针对特定的 macOS  机器并尝试收割谷歌云认证数据。被收割的凭据被发送到一台远程服务器中。”该包的一个重要之处在于，它受陷查看自己是否被安装在 macOS 系统中，之后才会比对该系统的UUID和一份由64个哈希组成的硬编码清单。

如受陷机器位于该预定义集中，它会尝试访问两个文件 applicaton\_default\_credentials.json 和 credentials.db，它们位于 ~/.config/gcloud 目录中，后者包含谷歌云认证数据。被捕获的信息随后通过HTTP被传递到远程服务器 "europe-west2-workload-422915[.]cloudfunctions[.]net"中。

Checkmarx 公司表示已在 LinkedIn 上发现名为 “Lucid Zenith” 的虚假资料，和该包的所有人匹配，并错误地声称为 Apex Companies 的首席执行官，这表明该攻击中涉及社工元素。

虽然目前尚不清楚该攻击的幕后黑手是谁，但Phylum 公司在两个月之后才披露了涉及 Python 包 “requests-darwin-lite”的详情。该包在检查了 macOS 主机 UUID 之后才释放了恶意动作。

这些攻击活动表明，威胁行动者们已经提前了解了自己想要渗透的 macOS 系统，并最终确保这些恶意包仅分发给这些特定机器。恶意人员利用这种技术分发看似相似的程序包，从而欺骗开发人员将它们集成到自己的应用程序中。

Gelb 表示，“虽然目前尚不清楚该攻击针对的是个人还是企业，但这类攻击可对企业造成重大影响。虽然最初的攻陷通常仅发生在个体开发人员的机器上，但它对于企业的影响是巨大的。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[PyPI 恶意包假冒合法包，在PNG文件中隐藏后门](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519478&idx=2&sn=4ecf7e9d8f867e65b249517a604a9ca3&chksm=ea94bd9cdde3348a8bd5578938ed713cda546b3b38f95941ded9cbdbeab717010101393d326a&scene=21#wechat_redirect)

[PyPI暂停新用户注册，阻止恶意软件活动](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519178&idx=2&sn=1933612977a1f4eec1b23d3ac5d81da4&chksm=ea94baa0dde333b632f229c81fa83436cee2bcc37585dea1c6a108f61c6cea82fa940cda0313&scene=21#wechat_redirect)

[日本指责朝鲜发动PyPI供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519041&idx=2&sn=625e27daa5f7fbaf8fadcd0a61cf215b&chksm=ea94ba2bdde3333d5d9856c4aa11c870e10488820d2bfba6fce2c519ed62b76b869a5da33117&scene=21#wechat_redirect)

[谷歌云 SQL Service 中存在严重漏洞，导致敏感数据遭暴露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516609&idx=1&sn=e6bef0b6cbbd3d38ef6d69c14130bdcc&chksm=ea94b0abdde339bd0efab5037b36b84212e32e77cb0a866ec8ea90ff15509d9afb7433ee96d5&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/07/malicious-pypi-package-targets-macos-to.html

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