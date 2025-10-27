---
title: F5修复BIG-IP 和 NGINX Plus 中的多个高危漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520531&idx=1&sn=3711327c08007954c754b1a665f4b963&chksm=ea94a079dde3296fb3e16aed65fdb526227e260cd11c96212ca1fd8bbde8380e989c2c1c2f57&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-21
fetch_date: 2025-10-06T18:04:13.460406
---

# F5修复BIG-IP 和 NGINX Plus 中的多个高危漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSAqQO6PyAV4RqncNmZp5QsiaDXXZKfLYZEtCqUJlgoVFTu3UPngNibENlcNrg8ws1NibrVwdMA9qtKA/0?wx_fmt=jpeg)

# F5修复BIG-IP 和 NGINX Plus 中的多个高危漏洞

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**F5 公司发布2024年8月季度安全通告，为9个漏洞发布补丁，其中包括为 BIG-IP和NGINX Plus 高危漏洞发布的补丁。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSAqQO6PyAV4RqncNmZp5QsNPPQUJWzLt6MFfibXeL1QzcMiaIe6PMYqBZEsHTicAywQk2ltJibCzLAZw/640?wx_fmt=png&from=appmsg)

在这些漏洞中，最严重的是影响 BIG-IP Next Central Manager 的CVE-2024-39809，它是一个会话失效不充分漏洞，因用户会话刷新令牌未在登出时失效而引发。

F5公司在安全公告中提到，“能够访问用户会话cookie 的攻击者能够在用户登出后，继续使用该会话来访问 BIG-IP Next Central Manager 和由 BIG-IP Next Central Manager 管理的系统。不存在数据面板暴露问题，只是一个控制面板问题。”该漏洞影响 BIG-IP Next Central Manager 20.1.0版本，已在20.2.0版本中修复。

无法应用该修复方案的用户可通过如下方式缓解该漏洞：将管理权限仅限制给可信用户和设备、使用webUI后登出并关闭所有的web浏览器实例，并使用不同的浏览器管理 webUI等。

第二个高危漏洞是CVE-2024-39778，是位于BIG-IP中的视线弱点，可导致虚拟服务器不再处理客户端连接，流量管理微内核 (TMM) 在配置了高速桥 (HSB) 的无状态虚拟服务器上停止。F5公司解释称，“当系统自动重启时，流量被破坏。该漏洞可导致远程未认证攻击者在 BIG-IP 系统上引发拒绝服务。并不存在控制面板暴露，只是数据面板问题。”该漏洞影响BIG-IP 15.x、16.x 和17.x 版本，已在16.1.5和17.1.1中修复。将虚拟服务器配置为“标准 (Standard)”并将相关UDP配置的“空闲超时”值修改为使用“即时 (Immediate)”可缓解该漏洞。

另外一个高危漏洞位于可使用 MQTT 过滤器模块的 NGINX Plus 实例中，编号为CVE-2024-39792，可导致引发资源利用增多的未披露请求。成功利用该漏洞可导致性能降级，最终导致NGINX的master和worker流程被强制或手动重启。NGINX Plus 版本 R32 P1和R31 P3修复了该漏洞，不过可通过禁用MQTT过滤器模块的方式缓解该漏洞。

第四个高危漏洞是CVE-2024-41727，它是资源耗尽增多漏洞，影响在 r2000和r4000 系列硬件上运行的BIG-IP多租户和使用 Intel E810 SR-10V NIC 的BIG-IP 虚拟版本。远程未认证攻击者可利用该漏洞降级服务，直到TMM进程被迫重启，引发拒绝服务条件。该漏洞影响 BIG-IP 15.x 和16.x，已在16.1.5版本中修复。

F5公司还修复了位于 BIG-IP和NGINX（Plus和Open Source）中的五个中危漏洞，它们可导致拒绝服务条件、账户登出、用户名称暴露和凭据登录在日志文件后果。

F5公司并未提到这些漏洞是否已遭在野利用。更多信息可参见该公司发布的季度安全通告。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[F5修复可导致RCE的 BIG-IP 认证绕过漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518011&idx=2&sn=bc312f0c5810515223f4c329eb996ee3&chksm=ea94b651dde33f47c81f15553198c52a0b6b0ced84cf7a06c3f8cca4a506c0b5a7b5f9aa959c&scene=21#wechat_redirect)

[F5 BIG-IP 高危漏洞可导致拒绝服务和代码执行](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515460&idx=1&sn=300b30047d4cb364fa903361e05d3052&chksm=ea948c2edde30538eab915c12ac7b6a1d83fe856638e1a22d727813fb060b9c1ad7f612dfa10&scene=21#wechat_redirect)

[F5 多款产品中存在多个RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514661&idx=1&sn=ed03e7c7fed936ce5c82e4583a0df074&chksm=ea948b4fdde302593a589756559c66f23db2dff4547b4b3a335485b1a65abafd877d7bc5310a&scene=21#wechat_redirect)

[F5 BIG-IP 中存在严重的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511649&idx=1&sn=2d9be3c3a8cdaf6d29d8a13e49ef8ade&chksm=ea949f0bdde3161d6555a751e3ebbfcafc81bf7054808d430d94245936a2cff9d6591e182d51&scene=21#wechat_redirect)

[F5紧急修复严重的 BIG-IP 预认证 RCE 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247502189&idx=3&sn=61decbf4d30e5620cdc2da9411057ff4&chksm=ea94f807dde371116d47ae9dcfbe607adfc79f03bb74b3f0af9cdb81963f832173d29c0031c1&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/f5-patches-high-severity-vulnerabilities-in-big-ip-nginx-plus/

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