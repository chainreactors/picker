---
title: 谷歌：三星0day漏洞已遭活跃利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521255&idx=3&sn=a3d253a523be442f0e1f72789ba75fb2&chksm=ea94a28ddde32b9b8de1966962ff8445b3814e03944529cc5ba0b88db8ff3ee88e958cd066e8&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-25
fetch_date: 2025-10-06T18:52:41.917877
---

# 谷歌：三星0day漏洞已遭活跃利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTlARBUPmCtrKejMgicDXDIHjrPzsn33ryoyDyxFQMzdZZkEmwFbNibb6iczEWhyhWcdhb3dMqokIyrA/0?wx_fmt=jpeg)

# 谷歌：三星0day漏洞已遭活跃利用

darkreading

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTlARBUPmCtrKejMgicDXDIHAsrKY1hySJXBvmIohxTyGZd1wQhDj1SvNore0frcGENut4nicLczKPw/640?wx_fmt=gif&from=appmsg)

**三星移动处理器中存在一个0day漏洞 (CVE-2024-44068)，正被用于利用链中，实施任意代码执行。**

该漏洞的CVSS评分为8.1，已在三星十月安全更新中修复。

美国标准技术局（NIST）发布安全公告提到，“该漏洞存在于三星 Mobile Processor 和 Wearable Processor Exynos 9820、9825、980、990、850和W920的 m2m 缩放控制器驱动中。”该移动处理器中的UAF漏洞最终可导致提权。

谷歌研究员 Xingju Jin 在今年早些时候报送了该漏洞，谷歌 TAG 研究员 Clement Lecigne 提醒称已在野发现利用。他们提到，“该0day漏洞是提权链的一部分。行动者能够在提权的摄像头服务器进程中执行任意代码。该利用还将进程的名称改为 'vendor.samsung.hardware.camera.provider@3.0-service'，很可能是为了对抗取证。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Cellebrite在40分钟内破解特朗普枪手的三星手机](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520157&idx=1&sn=94ec330c15668d966834f1942a25f714&chksm=ea94bef7dde337e1e2bc530a09a4a06ba1584bf2e4877daa5d692bdcf6754c5b30b28bb9751d&scene=21#wechat_redirect)

[三星遭攻击，英国客户受影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518149&idx=2&sn=dc851a34b77757572b86d0ea0d790c00&chksm=ea94b6afdde33fb99df8d7c792ab96bc3e574b74792e513b387f72d618881e949e965da48fcd&scene=21#wechat_redirect)

[谷歌在三星Exynos 芯片集中发现18个0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515956&idx=1&sn=01fe340192b1659e658210ae4b02ac97&chksm=ea948e5edde30748775821e1c9ed1b389b2c0dd119e01cd78b9292d859542e3f209300000e4c&scene=21#wechat_redirect)

[三星 Galaxy Store应用漏洞可被用于在目标设备上秘密安装应用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514374&idx=2&sn=2d300c548ffc6384b7cdfa4fa2014f9a&chksm=ea94886cdde3017a396b09657b8365e3c13370baa36727a148eda9e128bc91be1903d28d04f4&scene=21#wechat_redirect)

[继英伟达、三星后，育碧也遭攻击，员工密码重置](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510883&idx=2&sn=f393b8f5430d29951a2db1657466ad6e&chksm=ea949a09dde3131f788b175727969c896d47c896c8128815dd13a95456c373ed6008e033313f&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/endpoint-security/samsung-zero-day-vuln-under-active-exploit-google-warns

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