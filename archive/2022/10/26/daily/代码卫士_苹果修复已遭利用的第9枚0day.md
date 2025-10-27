---
title: 苹果修复已遭利用的第9枚0day
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514319&idx=1&sn=10f6c5afa8be65b7ccac62c9ab73645c&chksm=ea9489a5dde300b312a93ec52a321f835baed001465326883dd6cdbbe70fecd5b94b1b8000c7&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-10-26
fetch_date: 2025-10-03T20:55:56.961954
---

# 苹果修复已遭利用的第9枚0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTWdwrkSsm0ZibM3IpjiaSWHJaVyVmb3OWnm24P23wEdwO13iamqBzNxjMY8UrqsMpU6WTbsNo5KkCOw/0?wx_fmt=jpeg)

# 苹果修复已遭利用的第9枚0day

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**周一，苹果发布安全更新，修复了今年以来的第9个0day。该0day的编号是CVE-2022-42827，针对的是iPhone 和 iPad。**

苹果公司在安全公告中指出，发现报告称该漏洞“可能已遭活跃利用”。CVE-2022-42827是由匿名安全研究员向苹果发送的一个界外写漏洞，是因为软件写入的数据超出当前的内存缓冲区边界造成的。

该漏洞可导致因后续数据写入缓冲区引发未定义或未预期结果（内存损坏），进而造成数据损坏、应用崩溃或代码执行后果。正如苹果公司解释的钠盐个，如果该漏洞遭成功利用，则可被潜在攻击者以内核权限执行任意代码。

受影响设备的完整清单包括 iPhone 8及后续版本、iPad Pro（所有型号）、iPad Air 第三代及后续版本、iPad 第五代及后续版本以及iPad mini第五代及后续版本。

苹果公司已改进边界检查问题，在iOS 16.1和iPadOS 16 中修复了该0day。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTWdwrkSsm0ZibM3IpjiaSWHJgXKHKBGQOVbpy1NwwVFr4mba5P50wbztgg5I7O6yHJZFvicYibGgDJPQ/640?wx_fmt=png)

**修复iPhone 和 iPad**

虽然苹果披露称已收到关于该漏洞遭在野利用的报告，但尚未发布相关攻击详情。这样做的目的可能是为苹果客户争取更多的打补丁时间。

尽管该0day 很可能仅用于高针对性攻击活动中，但强烈建议安装当前的安全更新，拦截任意攻击尝试。

这是苹果公司今年以来修复的第9个0day：

* 9月，苹果修复位于iOS 内核中的漏洞 (CVE-2022-32917)
* 8月，苹果修复分别位于iOS内核和WebKit中的漏洞（CVE-2022-32894和CVE-2022-32893）
* 3月，苹果修复位于英特尔图形驱动和AppleAVD中的两个0day（CVE-2022-22674和CVE-2022-22675）
* 2月，苹果发布安全更新，修复了一个WebKit 0day (CVE-2022-22620)
* 1月，苹果修复了两个0day：可通过内核权限实现代码执行的0day (CVE-2022-22587) 和 web 浏览活动追踪的0day (CVE-2022-22594)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[数千个恶意仓库克隆传播恶意软件，GitHub正在调查](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513380&idx=1&sn=9aefa39f993b82d95011d39cb6e95783&chksm=ea94844edde30d588a1e4629181cdab36441110d804badc97b17f5b95ab5666f2021679c4408&scene=21#wechat_redirect)

[坐火车太无聊，我溜入微软 VS Code官方GitHub仓库，但没敢发动供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247501023&idx=1&sn=1eb3e1da3e58ce270c9da9a2364ce893&chksm=ea94f5b5dde37ca3a86bf6a3300745f1de712bd9e150e780186c5774b20c5cb7423f65f31efe&scene=21#wechat_redirect)

[Repo Jacking：依赖关系仓库劫持漏洞，影响谷歌GitHub等7万多个开源项目的供应链](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247496343&idx=1&sn=af59f0185810728944673b9a5142872a&chksm=ea94c3fddde34aebab6c4ddf6323f65a690b4b6d34484cadacb74e7b0e26792da68f35028050&scene=21#wechat_redirect)

[速查是否中招！攻击者正在擦除 GitHub 和 GitLab 仓库还有 Bitbucket并实施勒索！](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247489862&idx=1&sn=7fbd2b94876bf87af5bec90e1222e93d&chksm=ea97282cdde0a13a000c8782faf87da92d7b3ac79adca99081679769797ec7af4cc9a5d20dde&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/apple/apple-fixes-new-zero-day-used-in-attacks-against-iphones-ipads/

题图：Pixabay License‍

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