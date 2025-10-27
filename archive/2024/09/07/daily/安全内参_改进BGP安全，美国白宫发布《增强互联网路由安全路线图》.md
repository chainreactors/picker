---
title: 改进BGP安全，美国白宫发布《增强互联网路由安全路线图》
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512559&idx=2&sn=c4b740713f263e37c86d712eeec6ed5c&chksm=ebfaf6cfdc8d7fd993b3f301249592fd645f4dca218ea51ccbb11053f13af1627806a5f51166&scene=58&subscene=0#rd
source: 安全内参
date: 2024-09-07
fetch_date: 2025-10-06T18:28:36.668642
---

# 改进BGP安全，美国白宫发布《增强互联网路由安全路线图》

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7uy3MQMWhrbkuMkBxAkfo8pVbEm77qQLxIlhib8ZR6VAibnPvSibRW3f1PzZASNicQW3INKaahKJLIXiaw/0?wx_fmt=jpeg)

# 改进BGP安全，美国白宫发布《增强互联网路由安全路线图》

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

**修补BGP漏洞，亡羊补牢，为时未晚。**

前情回顾·**BGP安全威胁态势**

* [电信网络运行重大事故：一个账号被盗，一个国家大面积断网数小时](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247510755&idx=1&sn=a35713f1b2e4681a34124c216e8b55d2&chksm=ebfaedc3dc8d64d5b7b8b9518ad220e4a47cf58a8699ea95e49da4ec0a0e0ea35b49886783cf&scene=21#wechat_redirect)
* [苹果网络流量诡异绕道俄罗斯](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247504804&idx=2&sn=655fa241581896c3f358c49983016316&chksm=ebfa9484dc8d1d92f0a31b4f4ae9a351a71a85436407a0d3ef8a6172a30718642f87e243db79&scene=21#wechat_redirect)
* [这个互联网“伴生”的重大安全漏洞，美国FCC要推动解决](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247488380&idx=1&sn=56f2af8b3e987025aae701bb505a5057&chksm=ebf9545cdc8edd4acae13bac9d3aa900a92e50a7099d27e5df4073d142a9b53a1704ef67b70d&scene=21#wechat_redirect)
* [段海新：互联网基础设施安全依赖性研究](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247488380&idx=1&sn=56f2af8b3e987025aae701bb505a5057&chksm=ebf9545cdc8edd4acae13bac9d3aa900a92e50a7099d27e5df4073d142a9b53a1704ef67b70d&scene=21#wechat_redirect)

安全内参9月6日消息，美国白宫日前表示，希望加强互联网路由，特别是边界网关协议（BGP）的安全性。

BGP被称为互联网的“粘合剂”，用于管理不同网络之间的在线流量路径。这些网络被称为自治系统（AS），共同构成了互联网。白宫国家网络总监办公室（ONCD）于9月3日发布了一份《增强互联网路由安全路线图》报告，指出BGP在设计之初并没有充分考虑安全性问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7uy3MQMWhrbkuMkBxAkfo8p3Ow8LEGHxjN8tSrAftiaeweOBr9kOlCEHibPOOtBkTgYiaxvBia2ptcH3w/640?wx_fmt=png&from=appmsg)

报告中写道：“BGP在最初的设计和如今的日常运作中，未能为我们当前面临的风险提供足够的安全性和弹性。关于BGP的基本漏洞问题，已经被讨论了超过25年。”

BGP不会检查远程网络是否有权宣布流量路径的变更，也不会验证网络之间交换的消息是否真实，或检查路由声明是否违反了相邻网络之间的商业政策。

这导致了BGP路由劫持问题的长期存在。举例来说，2008年，巴基斯坦干扰了YouTube的流量；而2022年，俄罗斯在进军乌克兰时利用了BGP的漏洞，限制了推特的流量。

报告指出：“路由劫持可能会泄露个人信息，助长盗窃、勒索以及国家级别的间谍活动；同时也可能破坏安全关键交易，并影响关键基础设施的正常运作。尽管大多数BGP事件都是偶然的，但由于担忧恶意行为者的利用，这个问题已经上升为国家安全的主要议题之一。”

今年6月，美国司法部和国防部曾致函联邦通信委员会（FCC），支持该委员会决定调查互联网路由安全问题。美国司法部和国防部都认可解决BGP风险的必要性，并指出有他国电信公司在2010年以及2015年至2019年期间，曾多次错误地宣布流量路由，将美国的网络流量引导至对方国家。该公司的FCC执照已在2021年被吊销。

有一种现有的加密认证方案可以缓解这些风险：资源公钥基础设施（RPKI），其中包括路由源验证（ROV）和路由源授权（ROA）。然而，这一安全机制并非完美无缺，而且尚未得到广泛部署。

根据白宫的路线图，在欧洲，大约70%的BGP路由已经发布了ROA，并通过了ROV验证。然而，在其他地区，RPKI的采用率较低。在美国，由于美国互联网号码注册管理局（ARIN）管理的IP空间相较于欧洲或亚洲更加庞大且历史悠久，加之美国政府在RPKI的采用上落后于私营部门，美国的RPKI采用率仅为39%。

ONCD发布的路线图旨在加速RPKI在美国公共和私营部门的采用进程。

白宫国家网络总监Harry Coker, Jr.在声明中表示：“互联网的安全性至关重要，不能被忽视。因此，联邦政府将以身作则，推动各个机构迅速增加对BGP安全措施的采用。”

FCC主席Jessica Rosenworcel指出，这一路线图是对FCC此前制定的规则的补充，这些规则要求互联网服务提供商制定应对BGP安全风险的管理计划，并要求大型电信公司每季度发布公共报告。

**参考资料：theregister.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

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