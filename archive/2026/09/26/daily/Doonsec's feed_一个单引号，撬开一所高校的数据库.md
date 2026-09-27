---
title: 一个单引号，撬开一所高校的数据库
url: https://mp.weixin.qq.com/s/0NzANBMneV02k0uHt6ER-g
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:22:05.561665
---

# 一个单引号，撬开一所高校的数据库

# 一个单引号，撬开一所高校的数据库

三垣网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGKlfJSoUmIXZMDXhlck2iaRuu2ROBZOicic8OIicuDMsI6IcRVa0kw6SIlD1B00s3UFiaPIxNzQvwQzr47CicuUkNkh4icPFlA2ZDB424/640?wx_fmt=png&from=appmsg)

**前言**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLI3omCfvvPKwdUYxKvibYpiaCHY25GH7uOrGSTw3vQ8IiaYBicjSibtfgrQYHIPLC9a6rJ8Q3ic8XQDWiaoyCYI5gpR9Kiaqtlicu4IbNw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGJF3iaxUcDLv8WDlCucibicP9I4aS76EfPShXOoHHLDpVojVIneyPRoKd4qNso5JSqs0RYicoe94qqx0QCAwIicaO9AibKibDEoQHQibFE/640?wx_fmt=png&from=appmsg)

一个不起眼的搜索参数，一个单引号，就让数据库的门缝露了出来。本文完整记录从资产测绘、注入点定位、数据库指纹确认，到布尔盲注验证的全过程，含 payload、复现思路、危害分析。

**1**

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJqg7xJeHTp1tWwh9QOuo52yy7M4a7p8VMEy1xJ4uRoicE2AwM1vNUXnSVJDqBupVgg1pU0MuNFSeD1Bg1E44oI80M2SRQziaCbo/640?wx_fmt=png&from=appmsg)

**缘起：从资产测绘开始**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLdj7P7bmpqPCBIgunK9AlWkIibzC1c7bboXOGQAFxjYk0XTVsd2yWkraNL4UoORFSTUhj218yHhQOvcOfz7LVpQyILXRmYkYr8/640?wx_fmt=png&from=appmsg)

做 SRC 的第一步永远是找面。通过网络空间测绘平台，以学校名称配合业务关键词检索，很快锁定了一台互联网资产：IP 为 xxx.xxx.xx.xxx，开放 443/HTTPS 与 80/HTTP 端口，站点标题 MicrobialBioinformaticG...，后端应用为 PHP。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SxoDJcKqQGJrRDm4Sw7tFdPt3HJVibolbxfunsyuVSkmDgzEJeVSIJ9CCUWARDyUSppUAMuTEpr3B5p9AABzSPAQnTEYIqpkQFD8qWP8lb8E/640?wx_fmt=jpeg&from=appmsg)

从标题判断，这是某高校一个微生物生物信息学数据库站点，对外开放检索功能。这类科研数据库往往是外包开发的「小项目」，安全投入有限，是值得重点关注的对象。

**2**

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGLyBHHg5kz6umbQ7GeCYknQQlsw39AAjRu2acTiamMNVZAlGAibqHBaB50LRIUYeEReBhGS0E7IpWtb3cjQk0IdKib3ICG4snvNtA/640?wx_fmt=png&from=appmsg)

**注入点：一个单引号就报错**

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGIYHKDdJGTZtEia4crapNuhTiat2M0862w5YpReYIwTvGEcuyCoOHk0zDhbqWmSL7iak3CHKKLHhaaFD6eS35XJiao1KuQfq44yxIY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGK8IgQibVcLwCKxzdkVz9ZuxGgQmUw9OYiaJz4hHhib858jjZzCIVWJnrzGmqzYYJht08ic0lHl6GRK8vWnjf4VafcOpZuFdlPUtp4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGKMobPD1HibAvBWPgkrabq1PS0dLDQJ1XDe8tDU1ptPbeeJS3Kz426dQjdv9znibLVSWXBvRHgU4QqZgwqTo5Ze8VJUyUDYPjEgg/640?wx_fmt=png&from=appmsg)

name 参数用于按菌属名检索。老规矩，先在参数后面加一个单引号：

GET/TADB3/search\_tax.php?level=genus&name=Escherichia'&type= HTTP/1.1 Host: xxx.edu.cn

页面直接报错——典型的参数未过滤，SQL 语句被拼坏了

**3**

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGKyxqTomNRJS6V5Yz2iasCHQVnITw5XfbyNx9MjUJ5IB7iblcOBp7TYLp5O9kicSy9HVbfIt0g4P35hdibveJwFiaiatO3sUOhibSFH8U/640?wx_fmt=png&from=appmsg)

**指纹：/phppgadmin/ 暴露的数据库类型**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLWs6CticJSFfL74QzDFGwfLI6oaQ2EKc2XLhDiaW5T37bdwVMO4QduUsiasDRBibseXpwYzEUEKb51Gj4Hk3JJecN1uAKdicEXvFXE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGIcs9C0QbAK08rK5ia9cVZnUmR4DVRTMoZe0aQUZ841iafoAxma8D2K75pYzXXYedAiczvBrwNuicYZWqib8BbzS9UpM330IicyULqRE/640?wx_fmt=jpeg&from=appmsg)

动手打注入之前，先确认数据库类型。前期信息搜集用 dirsearch 扫目录时，扫到一个关键路径：https://xxx.edu.cn/phppgadmin/

phpPgAdmin 是 PostgreSQL 的 Web 管理工具。打开一看，版本 5.6，服务器列表显示 PostgreSQL 运行在 5432 端口——至此确认：后端数据库是 PostgreSQL。

这一步很关键，因为 PostgreSQL 在字符串拼接、类型转换上的语法与 MySQL 差异很大，直接影响 payload 的构造方式。

**4**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLBteiag95xqYIl1p3Fm6OtEux07kXqtH5jJrribI9cKcVb5Ne3huOQLVyicEqtNL6jONoiaFZujWUKXG17iaaCRth3N7mYReCnL6SM/640?wx_fmt=png&from=appmsg)

**构造 payload：布尔盲注的思路**

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJ4165SeREmtxzUBIx1HBWpP1sibuaktenGG4Q8icXDgN7ggGqAucPsIcibdJlhQa3Z6yeiaHLH84wicaGv0jTXpPpU8XcM9nvH4UXg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGI6yuBhNjn5NbubTZhn2gX6JyfSwa6GxPBPLeOUUQsibQfupruCkLHickG2PRGaPaKJHicEB9VMT3YiaXUdRgib1sblzhEN5P278MHI/640?wx_fmt=jpeg&from=appmsg)

1、先确认正常检索：

name=Escherichia 是能搜到东西的。然后构造布尔条件：

Escherichia'+and+(user+like+'r%')+or+'0

2、逻辑拆解：Escherichia' 负责闭合原查询里的字符串；and (user like 'r%') 判断当前数据库用户是否以 r 开头；or '0 兜底，保证语法闭合、页面不报错。条件为真，页面返回数据；条件为假，返回空结果——这就是布尔盲注的判定依据。

3、为了确认 user 首字母，用 Burp Intruder 对 payload 中的字母位做爆：

GET/TADB3/search\_tax.php?level=genus&name=Escherichia'+and+(user+like+'r%')+or+'0&type= HTTP/1.1 Host: xxx.edu.cn

4、当字母为 r 时，页面返回了 Escherichia coli str. K-12 substr. MG1655 的记录，其余字母均为空——证明当前数据库用户名首字母为 r，SQL 注入确实存在。

觉得有收获的请关注三垣网安

更多技术分享我们将及时推送与你，感谢支持

请为我点个赞再走

#安全漏洞 #网络安全实战 #sql注入#教育src信息搜集 #漏洞挖掘

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLQVV2IO5FbVALdF84PuibKKeFiamLlic3BR3Uga3NAwm3M2UmVvbfJuvwZ5bQIFbZzMqQUGec23PiaAIvqar9qkuu9e4TFhapx87M/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJaWOwicn7raXm5k4xXDlBia0Okyg0R9d4niakArWeAcFZe0mbIWPKXdgcJHv0mIY6picqR7UB0GmPPeMC70E9VFWMXDEdYOj8GS3o/0?wx_fmt=png)

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