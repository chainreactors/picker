---
title: ES端口暴露互联网导致数据泄露被罚十五万元
url: https://mp.weixin.qq.com/s/tHpzqo13XwZ12wYZgm9H2Q
source: Doonsec's feed
date: 2026-02-08
fetch_date: 2026-02-09T04:18:14.062472
---

# ES端口暴露互联网导致数据泄露被罚十五万元

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibQklqqtuHFm97k6ng20cQJRORwsPMnsib0oKx97b2rKmic6UwNn3AdRoA0xu2O3D6rBBB6ctBjrRF9oeUKPBuoQDer2kCNRtGibqI/0?wx_fmt=jpeg)

# ES端口暴露互联网导致数据泄露被罚十五万元

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/AiaxibnzDXa1asshEnCgBMF2CiayVQfx8e9XK6C8MH2YkouAoA6DRk6ibnPNQ3eSY4Ejfibh8hy8tOGNLnVoicJlWnIg/640?wx_fmt=gif&from=appmsg)

2026年1月23日，“网信湖南”微信公众号通报一起数据安全违法案件。某信息公司因未依法履行网络安全和数据安全保护义务，被依法处罚。经查，该公司技术负责人为图工作便利，擅自将公司ES数据库公共互联网访问端口开放，且事后未及时关闭，导致数据库数据暴露在互联网上，部分数据发生泄露。同时，该公司未采取必要的技术和管理措施保障数据安全，网络安全和数据安全管理制度不健全，且未按法律规定期限留存网络日志。湖南省网信办依据《中华人民共和国数据安全法》和《湖南省网络安全和信息化条例》，对该公司作出警告，并分别对公司、主管人员和直接责任人员处以15万元、2万元和1万元罚款。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibTwHaxMOyk9brrxTUVtQZc08Rs3KFCfPoVQqKyjFmSpt6kCN6iceKg8MkYQtlpibOLiaYDKOeoQOZPaaXHL6f0sicZRDoEZoV9j3lU/640?wx_fmt=png&from=appmsg)![]()

Elasticsearch（简称 ES）是一款分布式搜索与分析引擎，基于 Lucene 构建，广泛用于日志分析（ELK）、全文检索、监控告警、数据分析等场景。它支持近实时搜索、高并发读写和横向扩展，但默认配置对安全并不友好，如果直接暴露在公网，风险极高。

ES主要有两个端口，9200端作为‌HTTP协的RESTful接口，主要用于‌ES节点与外部客户端‌的通信。所有外部应用（如浏览器、移动应用、后端服务）对Elasticsearch的CRUD操作（如查询、索引文档）都通过此端口进行。例如，通过http://localhost:9200/user/\_search发送查询请求；9300端作TCP协的传输接口，主要用于‌ES集群内部节点之间‌的通信。它负责集群发现、主节点选举、分片分配、节点加入/离开等内部管理任务。在早期版本中，Java客户端也曾直接通过此端口连接集群，但此用法已过时。‌从Elasticsearch 7.0版本开始，官方废通过9300端口进行客户端连接的方式，并在8.x版本中计划完全移除该功能。目前，所有客户端（包括Java客户端）都应通过9200端口的RESTful API与Elasticsearch交互。‌

面临的风险点：未开启认证即可直接读写数据，可被删除索引、植入恶意脚本，易成为勒索、挖矿、数据泄露入口。

1.建议修改端口

编辑配置文件elasticsearch.yml，同时禁止将端口映射至互联网。

http.port: 19200

transport.port: 19300

修改后重启 ES 生效。

改端口 ≠ 安全，只能降低被“扫到”的概率，不能替代认证和访问控制。

2.建议设置访问密码

开启 X-Pack 安全功能（ES 7.x / 8.x），在Elasticsearch中，访问控制是通过X-Pack实现的。首先确保你的Elasticsearch安装了X-Pack。具体设置方法可以上网查询，不再赘述。

3.建议限制访问IP

推荐使用X-Pack的安全特性和网络层面的防火墙规则来限制对Elasticsearch的访问，因为这样可以提供更细粒度的控制和更好的安全性。

该安全事件充分暴露出部分企业在网络与数据安全治理中的基础性问题。一方面，技术人员安全意识薄弱，为追求运维便利擅自开放关键系统的公网访问权限，且缺乏事后复核与关闭机制，反映出安全红线意识不足；另一方面，网络安全基础工作长期不到位，安全配置、日志留存、访问控制等基本要求未形成制度化、常态化落实。“两高一弱”问题依然突出，即高危漏洞、高危端口、弱口令长期存在，而安全管理与防护能力相对薄弱，未能形成有效约束。针对上述问题，企业应从源头加强安全意识建设，将合规与安全要求纳入技术人员日常操作规范；同时，持续开展安全基线核查、漏洞扫描及渗透测试，及时发现和整改配置风险；进一步强化资产和暴露面管理，严格控制对外服务范围，避免核心数据和系统直接暴露于互联网环境中。通过制度、技术和管理多维度协同推进，才能有效降低安全风险，防止类似事件再次发生。

END

推荐阅读

[网络安全企业如何面对舆情危机](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492556&idx=1&sn=61d5aba7b958ebc80715fc868bdbe5d4&scene=21#wechat_redirect)

2026-02-05

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibSJ57a06DE5Xiacu8NibkBGyyiaIedcKiaRkyNYRvlQiaPDUud4A8MeNE55s7r1GkiaSzM9DQymdqbWpiaTappvabm50DS8Mp2hYzzqbc/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492556&idx=1&sn=61d5aba7b958ebc80715fc868bdbe5d4&scene=21#wechat_redirect)

[重磅！军队采购网发布军队信息安全产品测评认证要求](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492544&idx=1&sn=d0dc78ba54f3bad3c1e92f58076ab490&scene=21#wechat_redirect)

2026-02-04

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1YYUTCicwSEO3Qib6y7Gf6tL3A8QfibhEdd9O7TxV6wbTt5CXRBVoUbAW6KcqSmjHDlyqzuM2HYx6cwg/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492544&idx=1&sn=d0dc78ba54f3bad3c1e92f58076ab490&scene=21#wechat_redirect)

[净利润翻倍背后，深信服2025年做对了什么？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492506&idx=1&sn=6c7a358fb3ce0ab08b266169ab9ca5be&scene=21#wechat_redirect)

2026-02-01

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1ZeLxg6mD0Htuq4ld6nvJdejtfgh6BUY6fvxqJXcmLPAzBDUoHymfFVXsVxibuibdicFm1dUOtxSxzlg/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492506&idx=1&sn=6c7a358fb3ce0ab08b266169ab9ca5be&scene=21#wechat_redirect)

[兰花豆正式推出AI知识库啦！](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492497&idx=1&sn=a0bab0700ee0e440526ce1bee290b926&scene=21#wechat_redirect)

2026-01-30

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1afheOzYHn8KecN4ZWPqdYLEfAIDDNpcibXMSxicy14Xp54cL5JDyNbQPnicun5pzOF1iakeXu814aM4w/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492497&idx=1&sn=a0bab0700ee0e440526ce1bee290b926&scene=21#wechat_redirect)

[网络安全人士必知的BAS/AEV技术及国内代表厂商](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492489&idx=1&sn=729e13676d9e4b30b756a83676cf1b36&scene=21#wechat_redirect)

2026-01-28

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1atvzQWOZXKdsczpb82TgWNdL4FmdQaTPxBcswiavrKg5LqLeKyOHCDicBdKXibXQaLJMSty4VcQMTpQ/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492489&idx=1&sn=729e13676d9e4b30b756a83676cf1b36&scene=21#wechat_redirect)

[网络安全人士必知的JSFinder爬虫工具](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492477&idx=1&sn=d1ca586751a0448e0d2a9f251d688642&scene=21#wechat_redirect)

2026-01-23

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1bPeH9Y5EBhCcEwVT4OouD2NY32sblPXnoxicv1Zgh7ocOXIHtDMW5euyLvIn6BOsTRwoY3zic5yZCg/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492477&idx=1&sn=d1ca586751a0448e0d2a9f251d688642&scene=21#wechat_redirect)

[伊朗国家电视台的信号被劫持，播放反政府视频煽动暴乱](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492468&idx=1&sn=383aa6f3b13dd27d6284731c3712114a&scene=21#wechat_redirect)

2026-01-20

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1Z2ia1wr0taI6icIaUicNKfdKym4aWQ4BJYMLntiaQLGAGAheJibNjGfkyfjU0CleVhib3UmARy3FgOh4og/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492468&idx=1&sn=383aa6f3b13dd27d6284731c3712114a&scene=21#wechat_redirect)

[一文讲清：Hadoop集群到底该用JBOD还是 RAID？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492463&idx=1&sn=a489501733275cbd1780ecdcd32c7ce0&scene=21#wechat_redirect)

2026-01-19

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1ZMWCIwumlxZBGOnxRvQGtfZQAhjicoJFskNr3AWXwmvDzlfplrpyWTKRaaWOMjNjiciafvBTwcyEibiag/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492463&idx=1&sn=a489501733275cbd1780ecdcd32c7ce0&scene=21#wechat_redirect)

[网络安全人士必知的尼尔森十大原则](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492455&idx=1&sn=a60fd134bec77afaf6945aaf87aa23b2&scene=21#wechat_redirect)

2026-01-18

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1a3xTnURg30WM0ERdZc3R7bLvibRicepAF6dzjEqsIGdaxq4Yxe15icibNxQhdY1ic8ibIREKa89R1p5QTw/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492455&idx=1&sn=a60fd134bec77afaf6945aaf87aa23b2&scene=21#wechat_redirect)

[浅谈网络安全产品SaaS多租户设计](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492450&idx=1&sn=7a1ce1582d57f2346b547a7125e975fc&scene=21#wechat_redirect)

2026-01-17

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1bSOxUjETc0w2MBQAw7Z2PXvbSeXFDIoo8LT0SFL1yPxf5933iaaWPv4bg7ruKEXOCw6pKYI36VFEg/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492450&idx=1&sn=7a1ce1582d57f2346b547a7125e975fc&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1bqMxJDjlKHibBJTuOHAm4PzybElibGMCHZGroraSd6iaHnj8pWulIehECXslFK73RTa1QToRib1WU9hw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1bqMxJDjlKHibBJTuOHAm4PzcHqhBmpuwkzVfnA6GQibB8BNDgLBkX5tjuANrbFWeqqY9JYjfWGoEYw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

兰花豆说网络安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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