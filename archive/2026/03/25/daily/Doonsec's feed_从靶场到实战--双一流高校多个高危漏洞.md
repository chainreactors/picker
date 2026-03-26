---
title: 从靶场到实战--双一流高校多个高危漏洞
url: https://mp.weixin.qq.com/s/yZ_LVi21yVVvTewMcct3sw
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:29:31.736760
---

# 从靶场到实战--双一流高校多个高危漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mwFvjeHDLkhskg9Pypq5XITG5BgJnaYqNfMkWaECq6VVn1VsvS1t5OVR9qQBlNwhExoiaRxpzEQicMgvciaFVavpE6ic4qhAtLtvtuUBH2B45ew/0?wx_fmt=jpeg)

# 从靶场到实战--双一流高校多个高危漏洞

大白
大白

蚁景网络安全

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5znJiaZxqldyq3SBEPw0n6hCXNk6PmR3gyPFJDUCibH91GiaAHHKiaCpcsfnQJ2oImQunzubgDtpxzxNHONU88CypA/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

本文结合其它用户案例分析讲解挖掘某双一流站点的过程，包含日志泄露漏洞深入利用失败，到不弱的弱口令字典进入后台，再到最后偶遇一个貌似只在靶场遇到过的高危漏洞。

**信息搜集：**

web站点的话从域名，ip等入手范围太大了，于是决定直接从小程序入手。

微信搜索学校名称，便直接可以通过公众号，小程序寻找目标。这里注意如果你要挖掘某edu的漏洞，就可以多关注他们的公众号，小程序，看看最近有没有什么新的功能出现，这种功能点漏洞比较容易出现。

于是我直接在某公众号发现了一个新功能：报名入口。临近毕业，所有有很多公司可能会来学校宣讲或者招人，这种时候就很有可能出现新功能，本案例就是。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6NqIoPcL2qFQgr53p05rXiaNvic0VVy8h8OyklCH4uR2LHvKduRMeng0Q/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

照常点击功能，出现跳转，直接转浏览器测web页面。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6mGs8aIlwHmW44pNB6Gic20qOIZDx39so5fSNzVHIqhPRKQrHactfYEQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**日志泄露nday：**

在登陆时发现限定了登陆时间，而目前已经不在时间内，可见这其实就是一个临时的系统。

我检查js信息尝试调试js绕过，没成功就通过报错发现为thinkphp框架，直接上工具一把梭。

链接：https://github.com/Lotus6/ThinkphpGUI

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6pCKJ11dHfuuOB5UhHEb6E15kUIia17g00LXrYf3mM109YY4s9j827sQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

只可惜只存在一个日志泄露的nday,没能shell。

根据日志泄露目录可以发现能够遍历近一年的日志信息，此时的思路就是从日志中看能不能拿到管理员或者其它用户登陆的敏感信息，例如账号密码之类，这样就可以扩大日志泄露危害，进一步挖掘利用。

参考文章：

https://cloud.tencent.com/developer/article/1752185

这篇文章就是利用kali自带工具whatweb探测出thinkphp框架：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6PNqBZ3G1ficv2AsoSSibZhuCeWrQibBiccdyTZIxyf5YQECiaEWsFicoUFHQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

并通过dirb扫除.svn泄露：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r61Vtyd7ochqR6YPW9UGFDbBSfbOK93TuUc4hQrpxKfnvzrYBvib2qB7A/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

再通过svnExploit工具进行下载利用：

链接：https://github.com/admintony/svnExploit

并在svn中发现大量日志泄露：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r64ImxdrCaiboYyianqpQml9IXJzR9APibm72NGcEQWDDibIQIVpEwMice2WQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

并通过找到最新的日志信息，找到密码hash值，通过cmd5实现解密并成功进入后台：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6acGsxiaIS077Q6h53Nxp0picoaqfHdBekZcPejfRDD4CY2RgRRn1J6uA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

https://blog.csdn.net/qq\_41781465/article/details/144092247

这篇文章也是在日志信息中成功找到账号密码，配合dirsearch扫出后台，成功登陆：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6FNYcB6xek2PH2G0LMwx849lvyMUDQZVGicTbjRoOdTvy7zbgKoKoe5A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

不过我这次日志信息量虽然很大，且经过我实际尝试也确实会记录我的一些操作信息，但翻遍日志却并貌似不存在敏感信息：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6WZQVVd7qWMBxpq41tI95CXhM8sibWAXS3iaVZupB7bNbSneUhGicDjBog/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

但我发现在日志中泄露了sql语句，貌似可以寻找对应接口，参数拼接成数据包尝试sql注入，但我找遍了日志都没有发现可以直接使用的接口或者代入了sql语句的参数。

**不弱的弱口令：**

翻找js文件，尝试直接拼接登陆验证接口，和其它查询接口全部失败。

不过根据找到的其它js路径发现其目录结构基本拼接在/syl/下，于是根据经验在目录后拼接admin,系统跳转到后台管理员登陆界面，输入账户为admin页面显示密码错误，输入其它账户页面显示账号不存在，可知账户为admin。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6DbYZibicDSmjnsicjXgEqXMmVvMNnI7ficKJ2YPhvxE8icfe5Z5R6aj4SWg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6yKrrbyib1f5w7UEia9GyCSicA3icfVzTh6mXjGCtBC7GuDwrNZia6awW0Ew/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

根据页面特征制作字典并加上弱口令top500的内容，尝试爆破成功：密码为页面根路径字母syl+88888888。

这种:syl88888888一看就是弱口令，但如果你只是通过现存的什么top100，top500这种字典是爆破不出来的，所以在进行渗透测试时一定还要根据页面特征，关键字，系统名称首字母等信息制作特定的社工字典尝试。

比如kali自带的cewl工具，便是一种基于爬虫，对页面目录信息进行循环爬取再生成字典的工具。

工具分析文章：https://www.cnblogs.com/jackie-lee/p/16132116.html

成功进入后台。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6Soehvxa3dlsibuIjdEbokaWkbVRh8GtzhNUVAouDPBiakJ2u1NEQGOFw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

并发现大量信息泄露：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6TpslV33NjERTOQiaOXzqThibKX3oSmx56kh09ETmzYoBPTk5ib84Zhgtg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

存在四千多条用户敏感信息泄露。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6r7AOHOxKwicOvFJfg8Ca9uePE4qM0EsUllK1N0Yyyy8S5mQevFLzmOQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

爬出靶场的高危：

通过dirsearch扫描目录，看有没有结果。

直接扫出来了好几条.git路径，直接访问泄露的路径看不出什么敏感信息。

但很明显站点存在.git信息泄露漏洞，一个我曾经只在ctf技能树复现过的漏洞。

Git就是一个开源的分布式版本控制系统，在执行git init初始化目录时会在当前目录下自动创建一个.git目录，用来记录代码的变更记录等，发布代码的时候如果没有把.git这个目录删除而是直接发布到服务器上，那么攻击者就可以通过它来恢复源代码，从而造成信息泄露等一系列的安全问题。

尝试githack进行探测利用（只能python2使用）

工具链接：**https://github.com/BugScanTeam/GitHack**

该工具基本原理就是解析.git/index文件，找到工程中所有的文件，文件名，再去.git/objects/文件夹下下载对应的文件，并通过zlib解压文件并按原始的目录结构写入源代码

结果我直接把整个git扒了下来，得到站点整套源码，于是通过vscode打开分析：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r68PZhPYaCCWaKHcRjFCdjP7u1hFMEicichZw6aa96L3icaRw0qBibGddEEA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

随意翻找文件，找到mysql数据库账号密码，于是扫描端口发现开启3306，尝试连接，发现似乎做了IP白名单限制，于是放弃。

再翻找文件，发现居然直接把后台部分用户的信息写在了.sql文件内，包含姓名，身份证，电话等信息，不过只有几百条。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxsUzPDqXoK67WC0ibIM9r6sJggVOXMSjjWrShBODHooiaP3JFx0FlhHLfiammRkvF0MJfJ5eSp8VJw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

此处其实还可以深入对php源码进行审计，发现更多高危漏洞，但我却不会php代审，所以打到这里就收工了，觉得应该可以拿证了。

整个渗透过程很顺利，大概就两三个小时，还是信息搜集做得好，不然都不一定能出成果，同时需要多阅读漏洞挖掘文章，这样在渗透测试过程中才能对漏洞利用更加熟练。

[![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldwoHriaVoyA6JNsGroYQAQp8xrlxS8RibJWibDF8T1pmkgSXqiaWQvmVB43S1IVCFBDOKTEQFDAP0QL5g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNTIwNTkyNg==&mid=2247549615&idx=1&sn=5de0fec4a85adc4c45c6864eec2c5c56&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

蚁景网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

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