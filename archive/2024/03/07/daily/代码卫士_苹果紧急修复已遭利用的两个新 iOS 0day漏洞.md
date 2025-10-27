---
title: 苹果紧急修复已遭利用的两个新 iOS 0day漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519003&idx=1&sn=87b2f80deede9f2cb8e1092e9732820f&chksm=ea94ba71dde333675f4150799bb36ccc5360912e77c0af8aef77e7426b9b0c244aabb76833e4&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-03-07
fetch_date: 2025-10-06T17:09:25.944468
---

# 苹果紧急修复已遭利用的两个新 iOS 0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRkjTv7icPV6zbzZRZVlAWUuPa4yiaBgF0zJ9ibF6H187ajNlOMlalmDgpBgKPvZoqY65YSJDKBCGuzQ/0?wx_fmt=jpeg)

# 苹果紧急修复已遭利用的两个新 iOS 0day漏洞

Lawrence Abrams

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**苹果发布紧急安全更新，修复了已被用于攻击 iPhone 的两个 iOS 0day漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRkjTv7icPV6zbzZRZVlAWUuYrrFfDXnKFyHalmV5AUib8Y9iagURj8QYFLdzWvJt6boj97pk4xI1LMA/640?wx_fmt=gif&from=appmsg)

苹果公司在周二发布的安全公告中提到，“苹果从一份报告中了解到该漏洞可能已遭利用。”这两个漏洞位于 iOS Kernel (CVE-2024-23225) 和RTKit (CVE-2024-23296) 中，均可导致具有任意内核读写能力的攻击者绕过内核内存防护措施。

该公司表示已通过改进输入验证的方式修复了运行 iOS 17.4、iPad 17.4、iOS 16.76和iPad 16.7.6 版本的设备。

受影响的苹果设备范围广泛，包括：

* iPhone XS 及后续版本、iPhone 8、iPhone 8 Plus、iPhone X、iPad 第5代、iPad Pro 9.7英寸以及iPad Pro 12.9英寸第一代。
* iPad Pro 12.9英寸第2代及后续版本、iPad Pro 10.5英寸、iPad Pro 11英寸第一代及后续版本、iPad Air 第3代及后续版本、iPad 第6代及后续版本以及iPad mini 第5代及后续版本。

苹果公司尚未透露漏洞披露者的身份或是否是内部发现。

虽然苹果公司并未发布这两个漏洞的在野利用情况，但 iOS 0day 漏洞通常被国家黑客组织用于攻击高风险个人如记者、反对派政客以及异见人士。

虽然这两个 0day 漏洞可能仅用于针对性攻击中，但强烈建议尽快安装所发布的安全更新，阻止潜在攻击尝试。

加上这两个漏洞，苹果在2024年已经修复了三个0day漏洞。去年，该公司共计修复了20个已遭利用的0day漏洞，包括：

* 11月：两个0day（CVE-2023-42916 和 CVE-2023-42917）
* 10月：两个0day（CVE-2023-42824 和 CVE-2023-5217）
* 9月：五个0day（CVE-2023-41061、CVE-2023-41064、CVE-2023-41991、CVE-2023-41992和CVE-2023-41993）
* 7月：两个0day（CVE-2023-37450 和 CVE-2023-38606）
* 6月：三个0day（CVE-2023-32434、CVE-2023-32435和CVE-2023-32439）
* 5月：三个0day（CVE-2023-32409、CVE-2023-28204和 CVE-2023-32373）
* 4月：两个0day（CVE-2023-28206 和 CVE-2023-28205）
* 2月：一个WebKit 0day (CVE-2023-23529)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[苹果修复2024年遭利用的第1个0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518729&idx=1&sn=022dec20b1d19ed71466fd78c5c9b7c1&chksm=ea94bb63dde33275e80731ce7aa70dbb77566e3599abe9f927ae24a32dc66aff5a1acd09f3d5&scene=21#wechat_redirect)

[苹果紧急修复两个 iOS 0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518251&idx=1&sn=b501407684b48f59fb89d2d77570a27c&chksm=ea94b941dde3305715701eacd7c1a39f8de6430adaf0c7c820423a0694a1ffdbf0ff60504574&scene=21#wechat_redirect)

[苹果再次紧急修复两个0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517781&idx=2&sn=bb997e52e822a85d9557210284c73b30&chksm=ea94b73fdde33e296eebdd3ed4abe65621d3260c720dc544dd1bf5b285f4673167b913728d31&scene=21#wechat_redirect)

[苹果紧急修复已遭利用的3个0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517726&idx=1&sn=6812214f8fc21189da02ba2731b87720&chksm=ea94b774dde33e62737863151185ae158018de3e7f683d689e2a466982db356c57f6d7c1de92&scene=21#wechat_redirect)

[苹果紧急修复两个已遭利用的 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517599&idx=1&sn=f4c64820b9383523f48091354491d150&chksm=ea94b4f5dde33de3f2f7c7d26b6bc5178d7deb13b62b5e3b5220b9ad188751bce855b427f00b&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/apple/apple-fixes-two-new-ios-zero-days-exploited-in-attacks-on-iphones/

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