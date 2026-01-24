---
title: 网络安全人士必知的JSFinder爬虫工具
url: https://mp.weixin.qq.com/s/2MJNDb7nNidwyuZBr4e_3Q
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:25:29.306893
---

# 网络安全人士必知的JSFinder爬虫工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1bPeH9Y5EBhCcEwVT4OouD2P3jC5Ca6Licv7ib04ISg4mLWHutbW01FRXAAp09bRhzPHmXISrS6ZURA/0?wx_fmt=jpeg)

# 网络安全人士必知的JSFinder爬虫工具

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/AiaxibnzDXa1asshEnCgBMF2CiayVQfx8e9XK6C8MH2YkouAoA6DRk6ibnPNQ3eSY4Ejfibh8hy8tOGNLnVoicJlWnIg/640?wx_fmt=gif&from=appmsg)![]()![]()![]()

一、概述

在渗透测试与漏洞挖掘过程中，信息收集是决定成败的关键环节。其中，网站加载的 JavaScript文件往往包含大量高价值信息，如隐藏的URL、API接口以及未公开的子域名，是攻击面发现的重要来源。

1.子域名的安全价值

* 发现隐藏服务

许多子域名（如 admin.example.com、dev.example.com）承载着后台管理系统、测试环境或临时业务。这类系统常因运维疏忽、版本滞后而遗留漏洞，安全水平明显低于主站。

* 扩大攻击面

通过枚举和分析子域名，测试人员可以发现更多潜在入口点，包括未加固的管理后台、内部接口或第三方集成系统，从而显著扩展攻击范围。

* 利用安全薄弱点进行横向渗透

子域名通常缺乏与主站同等级别的安全防护，一旦被攻破，可能成为跳板，进一步渗透主系统甚至内部网络环境。

2.URL的安全价值

* 定位潜在漏洞路径

URL结构本身就是重要线索，例如 example.com/login.php、/api/v1/data 等路径，往往对应动态页面、接口或业务逻辑点，是注入、XSS、不安全鉴权等漏洞的高发区域。

* 辅助技术栈与敏感信息识别

通过分析URL的命名规则和文件扩展名（如 .php、.jsp），可推断网站所使用的技术栈、目录结构，甚至发现配置文件、备份文件等敏感资源，为后续深入测试提供方向。

以sohu网站为例，可以在script中看到如下信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1bPeH9Y5EBhCcEwVT4OouD2DjicQAf9I5bc4N5fPGfDanbrqgHiaPXRLuDZOx4WNQaLMoWZxE5SO5xw/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()

JSFinder能够根据URL自动收集JS中的URL和子域名，Github地址如下：

https://github.com/Threezh1/JSFinder

具体实现方式如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1bPeH9Y5EBhCcEwVT4OouD2jgyyybWuq5LTPXic8PdJc8QvECwibiaqB1YY60JN7Njtcxiaf80JrhNDoA/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()

二、使用方式

以搜狐为例来测试，搜狐的网址为：https://www.sohu.com

1.简单爬取

python3 JSFinder.py -u https://www.sohu.com

提取的URL

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1bPeH9Y5EBhCcEwVT4OouD2hNKDHHCllZFTNhMDvE2eiaPiaC9fYrM7MiaSJIibhBFf2iavOVU4bUMU5zQ/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()

 提取的子域名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1bPeH9Y5EBhCcEwVT4OouD2uZ8nHylLQxA8YicAAzKGPjPlKodo8EJXebicRweibibpd7xmRaHnnhZy1Q/640?wx_fmt=png&from=appmsg)![]()![]()![]()

2.深度爬取

python3 JSFinder.py -u https://www.sohu.com-d

3.使用-ou 和 -os来指定保存URL和子域名的文件名

python3 JSFinder.py -u https://www.sohu.com -d -ou sohu\_url.txt -os sohu\_subdomain.txt

4.批量指定URL/指定JS

指定URL：python JSFinder.py -f text.txt

指定JS：python JSFinder.py -f text.txt -j

可以用brupsuite爬取网站后提取出URL或者JS链接，保存到txt文件中，一行一个。

指定URL或JS就不需要加深度爬取，单个页面即可。

5.其他

-c 指定cookie来爬取页面 例：

python JSFinder.py -u http://www.sohu.com -c "session=xxx"

-ou 指定文件名保存URL链接 例：

python JSFinder.py -u http://www.sohu.com -ou sohu\_url.txt

-os 指定文件名保存子域名 例：

python JSFinder.py -u http://www.sohu.com -os sohu\_subdomain.txt

三、总结

无论是子域名还是URL，本质上都是攻击面管理的重要组成部分。对JS文件中泄露的这些信息进行系统化梳理和分析，能够帮助渗透测试人员更全面地还原目标系统的真实暴露面，为漏洞发现和风险评估奠定坚实基础。

END

推荐阅读

[伊朗国家电视台的信号被劫持，播放反政府视频煽动暴乱](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492468&idx=1&sn=383aa6f3b13dd27d6284731c3712114a&scene=21#wechat_redirect)

2026-01-20

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1Z2ia1wr0taI6icIaUicNKfdKym4aWQ4BJYMLntiaQLGAGAheJibNjGfkyfjU0CleVhib3UmARy3FgOh4og/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492468&idx=1&sn=383aa6f3b13dd27d6284731c3712114a&scene=21#wechat_redirect)

[一文讲清：Hadoop集群到底该用JBOD还是 RAID？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492463&idx=1&sn=a489501733275cbd1780ecdcd32c7ce0&scene=21#wechat_redirect)

2026-01-19

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1ZMWCIwumlxZBGOnxRvQGtfZQAhjicoJFskNr3AWXwmvDzlfplrpyWTKRaaWOMjNjiciafvBTwcyEibiag/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492463&idx=1&sn=a489501733275cbd1780ecdcd32c7ce0&scene=21#wechat_redirect)

[网络安全人士必知的尼尔森十大原则](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492455&idx=1&sn=a60fd134bec77afaf6945aaf87aa23b2&scene=21#wechat_redirect)

2026-01-18

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1a3xTnURg30WM0ERdZc3R7bLvibRicepAF6dzjEqsIGdaxq4Yxe15icibNxQhdY1ic8ibIREKa89R1p5QTw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492455&idx=1&sn=a60fd134bec77afaf6945aaf87aa23b2&scene=21#wechat_redirect)

[浅谈网络安全产品SaaS多租户设计](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492450&idx=1&sn=7a1ce1582d57f2346b547a7125e975fc&scene=21#wechat_redirect)

2026-01-17

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1bSOxUjETc0w2MBQAw7Z2PXvbSeXFDIoo8LT0SFL1yPxf5933iaaWPv4bg7ruKEXOCw6pKYI36VFEg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492450&idx=1&sn=7a1ce1582d57f2346b547a7125e975fc&scene=21#wechat_redirect)

[国产操作系统格局迎来大变！华为鸿蒙、欧拉；阿里云、中兴新支点通过安可测评](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492438&idx=1&sn=c9383f00b09e41bf5a2cfa4e383814fe&scene=21#wechat_redirect)

2026-01-16

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1Ysp4282VcAiacv7YYOU9iaAP9spK8ibH2tIu2ODzaqkNfiadJBFqnUI1CMaSoYAq0FpiamQM8ERZMJd3g/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492438&idx=1&sn=c9383f00b09e41bf5a2cfa4e383814fe&scene=21#wechat_redirect)

[网络安全人士必知的普渡模型](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492430&idx=1&sn=c25c526a9ddc16734fc0252531d943df&scene=21#wechat_redirect)

2026-01-11

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1ZGNjF0dicYHHqic6Gb49Hxia5FKL3cg7gvzHtuw2jVrGht5b5tuhquS5Jp80kgQzUWibL6N0Laqj0kBA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492430&idx=1&sn=c25c526a9ddc16734fc0252531d943df&scene=21#wechat_redirect)

[美国发动网络战，先毁产业再毁系统](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492424&idx=1&sn=a26a3f2664d323b3aaddc870ad4dacd6&scene=21#wechat_redirect)

2026-01-10

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1agfhuatjqG5BXk0aSFhicHg6ZYxGSibKKG9yRKHqMWTDAOnxicX9CZhkLFcfAYHfaYJ8PENFiarJIzpg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492424&idx=1&sn=a26a3f2664d323b3aaddc870ad4dacd6&scene=21#wechat_redirect)

[网络安全人士必知的产品安全设计15大原则](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492419&idx=1&sn=5de642ece3d2f826c3b6048e5707c4b2&scene=21#wechat_redirect)

2026-01-09

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1agfhuatjqG5BXk0aSFhicHgFayic7iaialVJt4Nd91O4F6xo5Jqj2dp8VlBUNszkqKYah7LmhDsFAUjg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492419&idx=1&sn=5de642ece3d2f826c3b6048e5707c4b2&scene=21#wechat_redirect)

[委内瑞拉遭遇的网络攻防实践与启示](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492414&idx=1&sn=9473d2db6367018428d4ffd658a9e4d4&scene=21#wechat_redirect)

2026-01-06

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1blQ3kq9feqFujBEb2UwNPJmsYGLgJmdOGy7xLvAwoaGEsY0HACQQX8DPHxnAdhTicUaIBXrASpiafQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492414&idx=1&sn=9473d2db6367018428d4ffd658a9e4d4&scene=21#wechat_redirect)

[从IAM到ITDR：身份安全将重塑企业防御体系](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492409&idx=1&sn=56d7b93404b98aaa1eca7360953da30a&scene=21#wechat_redirect)

2026-01-03

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1akLxBTYZ5ibDhTeicvdMdr1yicxH9dNgq0locLpA53cu0dlboO71PTaicxB29vPfVINNTmChFh4rjZaw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247492409&idx=1&sn=56d7b93404b98aaa1eca7360953da30a&scene=21#wechat_redirect)

预览时标签不可点

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