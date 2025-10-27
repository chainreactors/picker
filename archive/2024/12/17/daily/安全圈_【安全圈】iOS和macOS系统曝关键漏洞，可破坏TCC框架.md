---
title: 【安全圈】iOS和macOS系统曝关键漏洞，可破坏TCC框架
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066638&idx=4&sn=34b67f730621eac29fece525a015ab35&chksm=f36e7f0ec419f618bf50a593773d4d2d4b959a327145ed7417a53af1c019d9bf5dd1598e609c&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-17
fetch_date: 2025-10-06T19:40:17.934656
---

# 【安全圈】iOS和macOS系统曝关键漏洞，可破坏TCC框架

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia9FWvibdhmxgaDM3kRE4kXYxlqIsC7647qpbPuK92vebvY6KSVvZlCHVDeL33uOXxJ2DDdcaooRnw/0?wx_fmt=jpeg)

# 【安全圈】iOS和macOS系统曝关键漏洞，可破坏TCC框架

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

近日，苹果iOS和macOS系统中被曝光一个关键的安全漏洞，若被成功利用，可能会绕过透明度、同意和控制（TCC）框架，导致用户敏感信息被未经授权访问。漏洞编号CVE-2024-44131，存在于文件提供组件中，苹果通过在iOS 18、iPadOS 18和macOS Sequoia 15中增强符号链接的验证来修复此问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylia9FWvibdhmxgaDM3kRE4kXYa0AFqKicvur3FpGlOMwmqx7LDL2VODaJS0ZHkRBqP7vkqwhFEv5sklw/640?wx_fmt=jpeg&from=appmsg)

TCC作为苹果设备上的一项关键安全功能，允许用户对应用程序访问敏感数据的请求进行授权或拒绝，如GPS位置、联系人和照片等。

Jamf Threat Labs发现并报告该漏洞，该公司指出，“这种TCC绕过允许未经授权地访问文件和文件夹、健康数据、麦克风或摄像头等，而不会通知用户，这削弱了用户对iOS设备安全性的信任，并使个人数据面临风险。”

漏洞允许恶意应用在后台运行时，拦截用户在文件应用中复制或移动文件的操作，并将它们重定向到其控制的位置。这种劫持行为利用了fileproviderd的高权限，这是一个处理与iCloud和其他第三方云文件管理器相关的文件操作的守护进程，它移动文件后可以将它们上传到远程服务器。

Jamf进一步解释：“具体来说，当用户在后台运行恶意应用可访问的目录内使用Files.app移动或复制文件或目录时，攻击者可以操纵符号链接欺骗文件应用。新的符号链接攻击方法是，首先复制一个正常的文件，为恶意进程复制已开始的可检测信号。然后在复制过程已经开始后插入一个符号链接，有效地绕过符号链接检查。”

因此，攻击者可以利用这种方法复制、移动甚至删除路径“/var/mobile/Library/Mobile Documents/”下的各个文件和目录，以访问与第一方和第三方应用相关的iCloud备份数据，并将它们窃取。这个漏洞的严重之处在于它完全破坏了TCC框架，并且不会向用户触发任何提示。尽管如此，可以访问的数据类型取决于执行文件操作的系统进程。

Jamf表示：“这些漏洞的严重性取决于目标进程的权限，这揭示了对某些数据类型的访问控制执行存在差距，由于这种竞态条件，并非所有数据都可以在不发出警报的情况下提取。例如，由随机分配的UUID保护的文件夹中的数据，以及通过特定API检索的数据不受这种类型的攻击影响。”

与此同时，苹果发布了软件更新，以修复包括WebKit中的四个漏洞在内的多个问题，这些漏洞可能导致内存损坏或进程崩溃，以及音频中的一个逻辑漏洞（CVE-2024-54529），该漏洞可能允许应用程序执行具有内核权限的任意代码。

iPhone制造商还修复了Safari中的一个漏洞（CVE-2024-44246），该漏洞可能允许网站在启用私人中继的设备上将其添加到阅读列表时获取原始IP地址。苹果表示，它通过“改进Safari发起请求的路由”来解决这个问题。

参考来源：https://thehackernews.com/2024/12/researchers-uncover-symlink-exploit.html

***END***

阅读推荐

[【安全圈】千万悬赏：美国追捕四川黑客关天峰，指控其全球感染8万防火墙](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066618&idx=1&sn=a53c860727d887307f935b429a2162da&scene=21#wechat_redirect)

[【安全圈】最高人民检察院：三名小伙「变相换汇」USDT 与人民币，遭判处五年徒刑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066618&idx=2&sn=7387c9bfc5ce3c826968c7e7dc0ec037&scene=21#wechat_redirect)

[【安全圈】超 30 万 Prometheus 服务器暴露：凭证和 API 密钥在线泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066618&idx=3&sn=e357cb32259162fcaa4e589951d9e4ea&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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