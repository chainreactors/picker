---
title: 【攻防实战4】记一次某地市卫校内网穿透
url: https://mp.weixin.qq.com/s/3h1VMWgwrwYyEjF09_-Y6A
source: Doonsec's feed
date: 2026-02-26
fetch_date: 2026-02-27T04:05:51.528925
---

# 【攻防实战4】记一次某地市卫校内网穿透

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRKpicam1icCAtvib37NvsbU1wPuBsW1I9qeLxicPWgGKDupibZ5Fia4hwK0mg/0?wx_fmt=jpeg)

# 【攻防实战4】记一次某地市卫校内网穿透

安全研究实验室

![]()

在小说阅读器中沉浸阅读

编者荐语：

推荐

以下文章来源于十二主神
，作者十二

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5SmoGvQhdVZt3HnJhCaTsqw8CDhd2U8EH28EHwbYicjLA/0)

**十二主神**
.

十二主神安全团队，成立于2022年05月26日，是一群白帽子组织成立的非营利性的研究机构，以网络信息安全领域为焦点，致力于网络安全、应用安全与WEB安全领域的研究探索。

**“** 此次针对某地市卫生学校的实战攻防，通过shiro反序列化拿到口子，提权至root权限后，进行内网漫游和穿透，获取永恒之蓝漏洞2个，2个redis未授权，1台SSH服务器，2个MSSQL数据库权限，3个web应用弱口令，3个FTP匿名登录，2个SMB弱口令，智慧宿舍平台弱口令，4台RDP远程桌面权限。**”**

师傅们，阅读之前，动动小手指，设个星标，灰常感谢

01-入口打点

—

shiro反序列化

shiro使用了默认的key，密钥 kPH+bIxk5D2deZiIxcaaaA==

通过工具直接利用，获取命令执行权限。

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRrg95qrAuYSoNXmfVC1DcMusudxfSPWbzgBryUA25KQbCcn9JqbOsFQ/640?wx_fmt=png&from=appmsg)

执行whoami后，没有获取到管理员的权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRd6rqvjDhhsVLEnZe6CliaNR4CbVOwicfB7oVpByEkSBibAuwmACLhkfsg/640?wx_fmt=png&from=appmsg)

使用Pwnkit进行提权，拿到root权限，通过socks协议把内网代理出来

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRU75J6ZGAAibtmWx3k0jY8NmLOibWsjzJnCKtgvUwvBE9UeVSGAbOCaBw/640?wx_fmt=png&from=appmsg)

02-内网穿透

—

内网权限

##### MS17-010 永恒之蓝漏洞

因漏洞利用有一定系统崩溃风险，现提供验证截图，暂不进行利用

192.168.197.189

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRbJYZeXQvCfCTIxqppQhibZ5VX1yjZt232LegAU3BPsZmJkibLgicmD8Dg/640?wx_fmt=png&from=appmsg)

192.168.197.162

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRsT4aic45hzK70Z7tsajru2x17hInA23tPibOJMicXoqw8HDqHxY422siaA/640?wx_fmt=png&from=appmsg)

##### redis未授权-192.168.200.210

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRiaTKYILx7a3a82KZM4M2muxxvdrDyx73C8j64TOGyibqkmTzplRz4S5A/640?wx_fmt=png&from=appmsg)

##### redis未授权 -192.168.209.236:6379

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRAO0atbGzPZ6yFVa0qLbZFriaIsYiaXXzOibwdicXrGp3XOXUSia2LJib8rOg/640?wx_fmt=png&from=appmsg)

获取一台SSH服务器的权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRzCmMJ4sbxZiaLl7ZX7Tw3jNcASibadNJXVcJxSNLMhLfz5AqBS4ic4Klg/640?wx_fmt=png&from=appmsg)

获取2个mssql数据库的sa权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRdWfsLNia7ntRvTcsfXnFlofBrwicrNLJ8Nk4b8Qe7wlmLPAtRw1ekJMw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRsw7CP55YrbPYvTmicNrFUByJDCkm4pRGn9Z837UX7uYaACTTGZeP7AA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRrvYE0vquXBxx78NfcibXhshLRTqN4F2JwVPC7AgW0JLCCu8icTBl2xmA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxR34RV1fmxqS7rmb0Ghdjc1aqAF1jYYX58yzHrhZTicynupZmnkVM0nBA/640?wx_fmt=png&from=appmsg)

获取3个设备web账号权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRRrM7q10YSbwp9MYJF8Cvb5Yo4hSfE0TqdzoJ7dpsZkTPSbr6JYLfXA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxREDY988xhPCZI2TAR4U2A4UibDpcZLEhaba56Ufyw466pTMDwlVflAAw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRtfiaSicV6yaDmHNYyhBlibgWrKSQciakLZLPZ5nESBhKia9OMpg9pmWVnxw/640?wx_fmt=png&from=appmsg)

获取3个ftp匿名登录

ftp://192.168.190.30:21

ftp://192.168.197.42:21

ftp://192.168.197.178:21

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRVc8FRYgQubr73n7CoCEcH7tHKaIxdsoaJoib9KVJQvz38cMsAAVtoWw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRfmbrWghGibXKvkNfzofQgjdxaap1WOA9NvDlmnbbicqiaKNQ9VfpI5CVg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRe014wS7o0ye2jM1Gdo63JhplpgJo392ayXsuTzoZO7dfylQGyLSKQg/640?wx_fmt=png&from=appmsg)

获取2个smb弱口令

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRkzAMM346V9BSSoSE1pTkYaJGyib6K5UaCkkpa4YiarA9MNuW0La4wzDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRlgx933dpnNzZictIAfAibDcIogL37jPm3S7daeRIlibR6UkickibOrrUCVw/640?wx_fmt=png&from=appmsg)

智慧宿舍管理平台又是一个弱口令，管理员权限到手

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRT7pZBK2MrMRkiakMrdIwHuA39YnmHaribibR6HTYvGWcOQIpYNoeusJfQ/640?wx_fmt=png&from=appmsg)

获取4个RDP远程桌面管理员权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRelOXGfmNfeEUucEcAFgzl0wq7pmJuicTUtmNpgIPviaHb6vx1ovAiaZvw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRTqTdkjvNpDcKJTjiciaxRE1Oqk3icPKH1poJsJ41wdR16W6q9emNic4K1w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRRxZTblA8bibd4JiaZwVH2n3elahcAuSGw5aOXqwJRnE1TgYjevynZEmQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRib31MsdbxE1XKZLBy1BxcMLP0k2ccEyIdsJKOX7fsgvRibFSAIZwNKZQ/640?wx_fmt=png&from=appmsg)

##### SpringBoot未授权泄露账号密码

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxRcuvz37Alkk4icqkJUgUERic21tYJ44CfPNtuX1n8ajicnXkLEZH39S9Fw/640?wx_fmt=png&from=appmsg)

##### Swagger接口泄露

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAm9ZxV8w54WQpwlDzp4icxR1iarJBXVNVg6ZoCZPbWP2BjaplEcMlwXTd1efibicQ2IluleBnqeRib50Q/640?wx_fmt=png&from=appmsg)

## 免责声明：

本文章仅做网络安全技术研究使用！严禁用于非法犯罪行为，请严格遵守国家法律法规；请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。使用本文所提供的信息或工具即视为同意本免责声明，并承诺遵守相关法律法规和道德规范。公众号发表的一切文章如有侵权烦请私信联系告知，我们会立即删除并对您表达最诚挚的歉意！感谢您的理解！

安全研究实验室星球，覆盖src、渗透、安全技术：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bBJAh4fz6PEZeusBnaNCbLicwPSNtsvicE4YoSqLOfN74JKTAU6hjXlfvC2LzVI6ibj6ywfkAjtXY16ZSBF1rAF5545O1wiczbjVfWJyZs6iaiaek/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/bBJAh4fz6PFyHfEV3qpkLr4Z6Gto0mdpPaL9gtZU7mibiaScpoiaBbR4d2BS9EibspIoosQEVr5NWO3qibCBKtsrE7kWyu0WtYVDHTQf1bDiaQ1ias/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TvvmibSlOcicKLxfKjvRuGzwlGVEfTx8lTHSoDft6PXdzgYiawxeD5fnCZIGnq4vzDyyYNWVQGRbmVXdID4508FVg/0?wx_fmt=png)

安全研究实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TvvmibSlOcicKLxfKjvRuGzwlGVEfTx8lTHSoDft6PXdzgYiawxeD5fnCZIGnq4vzDyyYNWVQGRbmVXdID4508FVg/0?wx_fmt=png)

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