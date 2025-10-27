---
title: 恶意软件攻击Windows、Linux 和 macOS 开发人员
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520290&idx=2&sn=0dff9cae5a9ad1a39be2e6da027f70a9&chksm=ea94a148dde3285e6c15219e90179e8424cf1b202221d471b6c705e4dba7127f593b4fd64b80&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-02
fetch_date: 2025-10-06T18:03:25.022523
---

# 恶意软件攻击Windows、Linux 和 macOS 开发人员

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS2ibibgibWdRp1DBia14h2Hib3LEoRuJaMR7cial5WPBicXyiaX8vZqWYv1cxo5fOYib7U0b6bIgWIQzxsoCA/0?wx_fmt=jpeg)

# 恶意软件攻击Windows、Linux 和 macOS 开发人员

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Securonix 公司提到，一起正在进行中的针对软件开发人员的恶意软件活动展示了新的恶意软件和技术，将目标扩展至 Windows、Linux 和 macOS 系统。**

该攻击活动被称为 “DEV#popper”，被指与朝鲜存在关联，将韩国、北美、欧洲和中东的开发人员排除在外。研究人员支出，“这种攻击是社工的高阶形式，旨在操纵个体暴露机密信息或执行正常情况下可能不会进行的操作。”该恶意活动伪装成工作招聘广告，下载托管在 GitHub 上的受陷软件。它与 Palo Alto Networks Unit42 发布的 “Contagious Interview” 活动之间存在重合之处。

该恶意活动的范围更为广泛且跨越平台。本月初，研究人员发现针对 Windows 和 macOS 的制品，传播恶意软件 BeaverTail的更新版本。

Securonix 公司记录的攻击链多多少少是一致的。威胁行动者伪装成开发人员岗位的面试者，并督促候选人下载一个 ZIP 压缩文档文件，完成编程任务。该文档中是一个npm模块，一旦安装就会执行混淆的 JavaScript （即 BeaverTail），判断它所运行的操作系统并与一台远程服务器联系，提取感兴趣的数据。

它还能下载下一阶段payload，包括一个 Python 后台 InvisibleFerret，旨在收集详细的系统元数据、存储在 web 浏览器中的访问 cookie、执行命令、上传/下载文件以及记录键击和剪贴板内容。

最近样本中新增的特征包括使用增强混淆、用于维持持久性的AnyDesk 远程监控和管理软件，以及对用于提取数据的FTP机制的改进。另外，该 Python 脚本用于运行负责从多个 web 浏览器中窃取敏感信息的附加脚本。

研究人员表示，“对原始 DEV#POPPER 活动的深入扩展继续利用 Python 脚本执行专注于窃取受害者敏感信息的多阶段攻击，尽管现在能力得到增强。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[软件生产力工具遭劫持，分发恶意软件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519994&idx=2&sn=6c63cb9a8294ab38050d8820b26db689&chksm=ea94bf90dde336866e4631943c2a92ebd4d4e7fd3ebef7f34597feec9d117b39f5d4376bdb7a&scene=21#wechat_redirect)

[韩国 ERP 厂商服务被黑，用于传播 Xctdoor 恶意软件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519977&idx=2&sn=ec4872fbc8011458435995ff149f1f67&chksm=ea94bf83dde33695f8d928605f1d24446573067b877aa4599c889b1c0f04a01e3658f55a4ee0&scene=21#wechat_redirect)

[NSA提醒称朝鲜黑客正在利用薄弱的DMARC邮件策略](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519419&idx=2&sn=2bf4ebf6392d40174b31ed1eb866cb87&chksm=ea94bdd1dde334c7bcc430b56eed6790831e607ff3ae1f75e6e7007dbbaa5a57e477d02a058e&scene=21#wechat_redirect)

[FBI：数千名美国企业的远程信息技术合同工资助朝鲜导弹计划多年](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517948&idx=2&sn=38e39cad12e6761b050523619f28d328&chksm=ea94b796dde33e802827e02695ff95661d9ebdba5bc7b259987eecb4547093c817f7a7084a03&scene=21#wechat_redirect)

[软件供应链投毒 — NPM 恶意组件分析（二）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519078&idx=1&sn=eec7bf30c2e7abec80f62c022aa099c5&chksm=ea94ba0cdde3331aeabc6907e171c8b1e46209449d7af19a294d6cabe1260bb3a418ff465eaf&scene=21#wechat_redirect)

[软件供应链投毒 — NPM 恶意组件分析](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518377&idx=1&sn=9504988637a30aee727161562a17cd5a&chksm=ea94b9c3dde330d5c8364a04723d8e973480d0cd285b4ea0da0b9c6d2640ddcadad09ee6bbb1&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/07/north-korea-linked-malware-targets.html

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