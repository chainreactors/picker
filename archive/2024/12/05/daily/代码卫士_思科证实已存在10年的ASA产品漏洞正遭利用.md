---
title: 思科证实已存在10年的ASA产品漏洞正遭利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521684&idx=2&sn=d7717056b8823ba4a6de5202613f9d39&chksm=ea94a4fedde32de8a7cb8b62b8be9a979c6a959069b85ae3d1afdde8ea26be3e36187d94c087&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-05
fetch_date: 2025-10-06T19:38:36.943091
---

# 思科证实已存在10年的ASA产品漏洞正遭利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTFvqKIG48Qz4fia63ypKZ16HicT74pcgevnlgvOtOMdZseK8YLIsYdwMEgQkziaKQJN3IIVVzudicQJg/0?wx_fmt=jpeg)

# 思科证实已存在10年的ASA产品漏洞正遭利用

Eduard Kovacs

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTFvqKIG48Qz4fia63ypKZ16IVaZNfAwt3os3ic4zpicmTByQFHaG1MBgYBAZulj8vQXsndS4RHMe1LQ/640?wx_fmt=png&from=appmsg)

**本周一，思科更新安全公告提醒称，已存在十年之久的一个漏洞正遭在野利用。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTFvqKIG48Qz4fia63ypKZ16qoaCf9t5BW2aSg7tpR9OUdbyLz0D2K8om7p3stmxuthZmSzyqQk2TQ/640?wx_fmt=gif&from=appmsg)

该漏洞的编号是CVE-2014-2120，是中危级别的XSS漏洞，影响思科ASA产品的 WebVPN 登录页面。

思科提到，未认证的远程攻击者能够诱骗 WebVPN 用户点击恶意链接，利用该漏洞发动XSS攻击。思科首次在2014年3月发布安全公告，告知客户称应与支持团队联系获取打补丁的软件版本。

思科在12月2日发布更新提到，“2024年11月，思科产品安全事件响应团队 (PSIRT) 发现更多利用该漏洞的尝试。思科仍然强烈建议客户更新至已修复的软件发布版本以修复该漏洞。”

在思科发布安全公告更新前不久，CISA在11月12日将该漏洞列入必修清单，要求政府机构在12月3日之前必须修复该漏洞。而就在前几天，网络安全公司 CloudSEK 发布博客文章说明了Androxgh0st 僵尸网络的重大变化，包括利用多个漏洞获得对系统的初始访问权限，可能与 Mozi 僵尸网络进行集成。

CloudSEK 公司发现Androxgh0st 僵尸网络尝试利用位于思科、Atlassian、Metabase、Sophos、Oracle、OptiLink、TP-Link、Netgear 和 GPON 产品以及PHP和WordPress 插件中的多个漏洞。而本文所述的CVE-2024-2120就在遭利用的漏洞清单中。该公司提到，Androxgh0st 僵尸网络已攻陷数百台设备。

威胁行动者尝试通过特殊构造的请求利用CVE-2014-2120，远程上传任意文件并将恶意代码添加至服务器的PHP文件中，已获得持久性并进一步安装后门。从此前的报告看出，Androxgh0st 可导致网络犯罪分子获得对网站和业务系统的访问权限，并获得敏感信息如凭据等。他们可滥用这些受陷系统执行更多攻击，如密币挖掘和DDoS 攻击等。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[思科紧急修复已遭利用的 ASA 和 FTD 软件漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521275&idx=1&sn=23094a8bbc6812308a558007e25112aa&scene=21#wechat_redirect)

[黑客在思科商店注入恶意JS，窃取信用卡和凭据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=3&sn=ca7a392b964011a90f44ef9b56046155&scene=21#wechat_redirect)

[思科ASA防火墙中存在多个漏洞，可被用于供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513544&idx=2&sn=6c9886f2668674b71400b4eb1ccba93b&scene=21#wechat_redirect)

[黑客已开始利用思科 ASA 缺陷 (CVE-2018-0101)](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247486465&idx=3&sn=53c0b850ab768e129f36b19450eebc19&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/cisco-warns-of-attacks-exploiting-decade-old-asa-vulnerability/

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