---
title: 国内最大IT社区CSDN被挂马，CDN可能是罪魁祸首？
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513271&idx=2&sn=71c4701f2fa02532167afe1be3d32d3b&chksm=ebfaf397dc8d7a81f93ab950975e3552c039bd66d9d4225ab7b0bd6b99c8b5885310703ed697&scene=58&subscene=0#rd
source: 安全内参
date: 2024-12-13
fetch_date: 2025-10-06T19:38:54.580047
---

# 国内最大IT社区CSDN被挂马，CDN可能是罪魁祸首？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehicicLNEYYyfark27O9MBr1fsMJGb194aZHPugdiakibBPHM96Gdl8v6kCpJn20UQMK0FTonFxrCAlkuibA/0?wx_fmt=jpeg)

# 国内最大IT社区CSDN被挂马，CDN可能是罪魁祸首？

安全内参

编者荐语：

近日研究员观察到某恶意域名的访问量从9月初陡增，10月底开始爆发，并观察到恶意的payload ，基于相关日志确认CSDN被挂马。测绘数据显示国内大量网站正文页面中包含该恶意域名，包含政府、互联网、媒体等网站，推测 CDN 厂商疑似被污染。

以下文章来源于奇安信威胁情报中心
，作者红雨滴团队

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7I8QeMG3CujdN79zxbczFS3XAMP0KcY9YcqkRIHEy7CQ/0)

**奇安信威胁情报中心**
.

威胁情报信息共享，事件预警通报，攻击事件分析报告，恶意软件分析报告

“

**鸣谢个人研究员：LugA、Zero17010、Sn2waR提供溯源帮助，共同完成了本次事件的恶意组织披露。**

水坑细节

奇安信威胁情报中心在日常监控中观察到 analyzev.oss-cn-beijing.aliyuncs.com 恶意域名的访问量从 9 月初陡增，一直持续到 9 月底，在此期间并没有观察到可疑的 payload，只有一些奇怪的 js，之后进入了一段时间的潜伏期。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMW6M7jLqiaicAnG6XwUJ7zec4f7051RKjwwHroicMEVIr4CCApmZrMV1OQ/640?wx_fmt=png&from=appmsg)

直到 10 月底开始爆发，并且观察到恶意的 payload 程序。

|  |
| --- |
| **URL** |
| **hxxps://analyzev.oss-cn-beijing.aliyuncs.com/update.exe** |
| **hxxps://analyzev.oss-cn-beijing.aliyuncs.com/ntp.exe** |
| **hxxps://analyzev.oss-cn-beijing.aliyuncs.com/flash\_update.exe** |
| **hxxps://analyzev.oss-cn-beijing.aliyuncs.com/ntp\_windows.exe** |

网络日志显示在请求上述 URL 时的 Referer 字段都是 CSDN 的正常博客，非常奇怪。

|  |
| --- |
| **Referer** |
| **hxxps://blog.csdn.net/Liuyanan990830/article/details/139475453** |
| **hxxps://blog.csdn.net/A186886/article/details/135279820** |
| **hxxps://blog.csdn.net/gitblog\_06638/article/details/142569162** |
| **hxxps://blog.csdn.net/qq\_44741577/article/details/139236697** |
| **hxxps://blog.csdn.net/jsp13270124/article/details/100738172** |

基于相关日志最终确认 CSDN 被挂马，并且成功复现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMMxOk7wqeQicYCsvIVnKSgM6FcxlkWqpiaQJsoc1VhMxNdpyicyic8ib8M9g/640?wx_fmt=png&from=appmsg)

加载了额外的 js：

|  |
| --- |
| **Js** |
| **https://analyzev.oss-cn-beijing.aliyuncs.com/jquery-statistics.js** |

基于奇安信全球鹰测绘数据，国内大量网站正文页面中包含该恶意域名，其中包含政府、互联网、媒体等网站：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsM1PV3E5iaiccQtSr6sXkulo9nqZp6QGc5PaEZNSDI4Nq0seB24naMXCKg/640?wx_fmt=png&from=appmsg)

所涉及的域名均挂有 CDN，对应IP也都为 CDN 节点，由于我们缺乏大网数据，只能推测 CDN 厂商疑似被污染。jquery-statistics.js 解混淆后逻辑如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMGDIXAzibkcAGEwzLhiczL6y9iaic05eHibSsmaYeZWcBoic4wibO9rqmxLPZQ/640?wx_fmt=png&from=appmsg)

获取本机的 IP 与内置的IP列表进行比对，如果匹配成功，则跳转到下一个 js，该 js 主要用来钓鱼，页面如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMIqotgJxohichfZmpYCNh6y9k2VYWVJjbcZpMb8EztUc1zL9b22OF9dw/640?wx_fmt=png&from=appmsg)

诱导有害者更新证书，下载上述 payload 并执行，这一阶段的钓鱼 js 有多种，还观察到 flash 更新页面，正常情况下受害者会误以为该页面是浏览器的更新请求，手动下载该 payload 并执行从而导致中招。

我们对内置的 IP 列表进行了分析，攻击者似乎比较关注媒体行业。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsM46DNIuwEypxUssHyra1e96prlbSZohK7U52iaYKLwhd83pIxUicnia3ibg/640?wx_fmt=png&from=appmsg)

木马分析

初始 payload 一般带有签名：

|  |  |  |
| --- | --- | --- |
| **MD5** | **Name** | **签名** |
| 0b42839d1d07f93f2c92c61416d589c3 | sslupdate.exe | Octopus  Data Inc. |
| cafe15fde16f915c014cc383b9503681  dc0d62cb42a56a3fd7458a2f5519f4cc | ntp\_windows.exe | Chengdu Nuoxin Times Technology Co., Ltd. |
| eba2a788cf414ab9674a84ed94b25d46 | flash\_update.exe | Chengdu  Nuoxin Times Technology Co., Ltd. |

相关样本在 VT 上 0 查杀：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMGIicAicU1icHWCXuq60xQ3Wicm0iaFOGCzd939WeYJhkMJsHxd5gZOKicpbg/640?wx_fmt=png&from=appmsg)

目前奇安信天擎已经可以对上述样本进行查杀：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMxqAoE1JJk0d058cGfY9o5k7IBpu3SgboxY938fj3bzvvKuDZ0BDyXw/640?wx_fmt=png&from=appmsg)

sslupdate.exe 是个 downloader，首先解密出要链接的 C2：server.centos.ws:8848。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMqLwqhvM9kSHbNI0fGLwMMgEo8YDJhjBicDYswJcRX12EBSnbe84KgFw/640?wx_fmt=png&from=appmsg)

之后连接 C2 并发送数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMCDBm4QCOBtlnb14sLgzEIKibyEbQ0F1fyYdwJ0XWRtT4Ku6WUyNmrRQ/640?wx_fmt=png&from=appmsg)

发送和接收的数据包有固定前缀特征 64 6D 07 08。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMuOVJztiafMkUybiamJCpp0GbU9ibibOeh0NoWsdPd0o0jAvfSx30yU8Ocw/640?wx_fmt=png&from=appmsg)

之后 recv 接收数据，收到的数据是个 .NET DLL。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMdibcFLQ0UZYTBVCru9CSjvibyYcVQuVbobHGE7v2VXjaEhj8xwWMoNLQ/640?wx_fmt=png&from=appmsg)

接收完毕后会加载 CLR 执行该 DLL，调用其导出函数 Client.Program.Start。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMLuWwh2UfS2fXq3E9oic4xDXqic0qy4yyQeMRlU7QkTUZFj36z3HeNtDQ/640?wx_fmt=png&from=appmsg)

此 DLL 是个特马，将其配置信息加密后以 Base64 形式存储，解密后如下，C2 与 Loader 一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMeeNoSy8xTH3aLqVPBuuVOExAwLVeIicxSqP9N5XSZXiaJZfsy5MC635g/640?wx_fmt=png&from=appmsg)

该后门的插件需要攻击者手动下发。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMWSrwek3MaibxYvH3yzJulfmicCf4kjSSItnlXJOD7eh3SaibH4rGKUPJw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMXVKf43EEURU2R7V9gQAbT2hMgQyfEmkef7s7GW4kBnFxE4x4yEfzJw/640?wx_fmt=png&from=appmsg)

溯源分析

jquery-statistics.js 中的 IP 列表除了国内的目标 IP 之外还包含了一些境外 IP，推测可能是攻击者的测试 IP 或者境外目标，境外 IP 大部分为 p2p 节点和 tor 节点，如果将其当作目标很难入侵到对应的人员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMquDI0eRJ4uhYdnnph62ppbLpUR3gmbfTiaUqYFcdgTQrXvzerv4nFnA/640?wx_fmt=png&from=appmsg)

基于奇安信 xlab 的僵尸网络数据 80.67.167.81 的 tor 节点最近非常活跃，使用jenkins RCE Nday 漏洞投递 lucifer 团伙的挖矿木马。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMJj3OJUXHj9uvvsh1oa10ytuY4nFgC44yuLicmEqFhg5YVPX5sNVhSWg/640?wx_fmt=png&from=appmsg)

该 tor 节点似乎由法国的 NGO 组织提供，目前已经被黑灰产团伙所利用，如果是测试 IP，那么本次活动可能与 lucifer 团伙有关。

总结

目前，基于奇安信威胁情报中心的威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、天擎、天眼高级威胁检测系统、奇安信NGSOC、奇安信态势感知等，都已经支持对此类攻击的精确检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehicicLNEYYyfark27O9MBr1fsMSvbfZeTQEJQnWwD00jDgZic0OmUefrYwYJZEAaf6SCCJtPHNUarq7Bw/640?wx_fmt=png&from=appmsg)

IOC

**C2：**

update.sslcsdn.com

fix-ssl.com

47.243.177.243:443

analyze.sogoudoc.com

107.148.62.90:443

47.243.177.243:443

107.148.61.185:8084

8.217.107.66:443

csdnssl.com

sogoucache.com

sslcsdn.com

sogoudoc.com

flash-update.com

centos.ws

45.205.2.101:8848

103.112.98.83:8848

sslupdate.org

analyzev.oss-cn-beijing.aliyuncs.com

updateboot.com

ntpfix.com

**MD5：**

0b42839d1d07f93f2c92c61416d589c3

cafe15fde16f915c014cc383b9503681

dc0d62cb42a56a3fd7458a2f5519f4cc

eba2a788cf414ab9674a84ed94b25d46

31f84f78241819e6e6b9f80005bc97ae

ede730817f76f4e3c47a522843125eb8

cc15da6879fd31262d71a7e471925548

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehicicLNEYYyfark27O9MBr1fsMN5qDujcicyy1n63s0iaCUmcLgGfibjkULhLO2ibY5l2Xu8t8y8PrHK6UUw/640?wx_fmt=gif&from=appmsg)

点击阅读原文至**ALPHA 7.0**

即刻助力威胁研判

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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