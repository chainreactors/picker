---
title: 打印服务也犯错！最新CUPS漏洞可攻陷操作系统
url: https://mp.weixin.qq.com/s/PEbh04GR873lOvayH9x39w
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:06:41.228667
---

# 打印服务也犯错！最新CUPS漏洞可攻陷操作系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6liaItc9B4ZicNJic1ebBwBAchEWOiaxfdwEIibkP7gcwcJvUY93PJibfMn8zQ4YMoKlNudslbjAicX7xJibgNH3tHS2YnKicTAVI4nz2o74d1P6kT5I/0?wx_fmt=jpeg)

# 打印服务也犯错！最新CUPS漏洞可攻陷操作系统

原创

打印机安全
打印机安全

打印机安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CUPS是什么？

CPU？UPS？嗑CP？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6liaItc9B4ZibPmMicssUu9TDLJBdwrwdn89ick9FKDHZaDOFaTLEC9LicPjkQ4dbFYfJ3ib1RpvboczpqsWZVQ6JOuQyLNKeZ5yrRneLwHhEq9gw/640?wx_fmt=jpeg&from=appmsg)

CUPS是在苹果电脑、Linux系统、Unix系统、以及基于Linux深度开发的国产操作系统里管理打印的服务。

CUPS就是在你的电脑里负责接受处理打印任务的一个服务，和Windows系统里的Print Spooler服务类似。

CUPS的功能非常强大：

1）军训教官：假如多个打印任务是一个个小兵，CUPS就是那个教官，让小兵们听训听话，一个个排好队，顺序上车。

2）翻译：如果把jpg、pdf、txt等格式文件直接交给打印机，打印机不一定能直接打印出来，打印机有自己的语言PCL等，CUPS就负责翻译工作，把电脑里的文件翻译成打印机能理解的文件。

3）送信的：光在电脑里翻译好了还不行，还要送给打印机才可以，CUPS就通过专属的通道（如USB、IPP等）把翻译好的文件交给送给打印机。

所以，CUPS就是操作系统里主管打印的尽心尽职的全能管家！

但是！正因为尽心尽职，所以全能管家就犯错了！

比如CVE-2026-34890和CVE-026-34990这两个最新漏洞，就让CUPS成为恶人的帮凶。

利用漏洞攻陷操作系统：

现在我们假设，操作系统是一个防守非常严密的军营，敌对势力正对着军用虎视眈眈，但又因为军营防守严密，所以就想用间谍混进军营，于是，他们盯上了尽心尽职的全能管家-CUPS。

![](https://mmbiz.qpic.cn/mmbiz_png/6liaItc9B4Z8jcx7OIHRTAf9Bh55bumkxO9PAibZ6jxKEibQuu8vnOATTkOjoSEpLVCw5EfSYxm2j8NE9X2msL32GYkomMJU9H8GbylJ1uTsmw/640?wx_fmt=png&from=appmsg)

CVE-2026-34890漏洞：小兵们正排着队进军营呢，间谍来了，穿着同样的军装。CUPS非常尽心尽职，因为这已经不是他第一次接受从兄弟连队插队进来的小兵了。凡是小兵，他都接受。

间谍顺利地进入了军营，但是他没有钥匙，没有打开重要房间的钥匙。

间谍开始思考，钥匙在哪里？

CVE-2026-34990漏洞：钥匙其实一直是由CUPS保管着的，但是，CUPS有个不好的习惯，他在带某些小兵（IPP）进入军营时，他会把钥匙随便乱放。这个坏习惯被间谍看到了，于是，间谍就拿着钥匙，进入了军营重要位置，开始胡作非为。

最终，间谍成功地攻陷了军营。

![](https://mmbiz.qpic.cn/mmbiz_png/6liaItc9B4Z8bS7Q1BpSvAxOeEm20lIf8Rt64sNzzJHy2WcItdxmox9hUPNPcoITt5yH0rgcIyMXAfn4gSVEWAgrRhkhYN4jM99fF1JwtgDc/640?wx_fmt=png&from=appmsg)

值得注意的是：

1）目前针对的版本是CUPS2.4.16

2）这两个漏洞是借助人工智能发现的。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TeIldibXx0Qk3WFficqIB2ksTRbFiawe9toURBGn2QoN0trWKdeBKbWMpFzYA7pbia57KLibKRPuOK7YHH0e3ykcxVw/0?wx_fmt=png)

打印机安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TeIldibXx0Qk3WFficqIB2ksTRbFiawe9toURBGn2QoN0trWKdeBKbWMpFzYA7pbia57KLibKRPuOK7YHH0e3ykcxVw/0?wx_fmt=png)

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