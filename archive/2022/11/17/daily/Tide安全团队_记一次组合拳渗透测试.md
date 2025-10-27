---
title: 记一次组合拳渗透测试
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247502299&idx=1&sn=7a9b86a4c9f945016ba7bae2266ecbab&chksm=ce5debbaf92a62ac1e995c796161ef533e776c783ef88d6ca6595104656807043a7ffbcfedf7&scene=58&subscene=0#rd
source: Tide安全团队
date: 2022-11-17
fetch_date: 2025-10-03T23:01:17.752438
---

# 记一次组合拳渗透测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5bdw0icm9WycJxshRobCyEvMXknib8dTjGhUW2063MAjvrcJBMVMG1gPA/0?wx_fmt=jpeg)

# 记一次组合拳渗透测试

原创

lancc

Tide安全团队

## 0x00 前言

在近段时间的实战中，遇到一个使用多漏洞组合方式获取目标系统权限的环境。通过sql注入，账号密码爆破，任意文件下载，文件上传等多个漏洞获取webshell。

0x01 web打点

给到目标后，还是先进行信息收集，队友发现目标使用了jeeplus框架，并且发现该系统存在通用漏洞sql注入漏洞，该漏洞点存在于登录界面的mobile参数。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5ZSoGLRruqibdKGfwZpL5zjY22OKFE2EbIGse2GpnSzrZOpsDAXcyibCg/640?wx_fmt=png)

注入为mysql数据库，并且是dbs权限，通过注入点的报错信息获取绝对路径，尝试使用os-shell获取权限，未成功。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy52icn84K1TsnxyA4zzKV9wPTkayJY4iavn007eC5l5icszicuibcRmzshVnw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5B7ZXzumibNWDSKLl4BmXPPp0OQU02UMaIjCFVXSzjRLVia3wlpd6s9Hw/640?wx_fmt=png)

在注入无果后，发现了系统采用了shiro框架，使用shiro工具进行验证，同样未成功。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5kQRoF0YiaGgm7aplicNyaNMNOp5IlGbPlvveD3zPByARZhSJKDMxjdkA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5rEIvicQtrx2ia3XWhNnVEh48afljq0Eup33PEJwPXFbibfRGmu9823gOA/640?wx_fmt=png)

注入和命令执行都噶了，还是要登录后台找找上传进行尝试，通过注入跑了下账号信息，获取了账号密码信息。后发现jeeplus的密码为魔改的加密算法不可逆，只能获得账户名，又噶住了。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5KYHkXgDLhdwJDXhkrHnotIZRccW1ol4iad0yt4tlVIj5ZTdcZTd1JKA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5jDWcnmZlwRPydwUH0Z26Zfx5cOAicwOfhHqIaSuaAKeGybJYTODOcZg/640?wx_fmt=png)

想起了网上大佬jeeplus的漏洞复现文章，发现jeeplus使用了2个熟悉的组件druid和fastjson。看了大佬的文章知道了druid可以监控DB池连接和sql执行情况。访问/druid/目录即可看到控制台信息，并且控制台可以看到session信息,并且通过session信息可登录系统，赶紧去尝试了一下。"嗯，确实存在控制台，但我的session信息呢？"

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy50qbwlYLWa8tdexG3Eamk9wLg0R7h8Ay6bsk3SxUSTMHW5RqMOu1H0w/640?wx_fmt=png)

又白给了一波后，队友还是准备尝试最稳妥的方式通过注入获取的账号，锁定密码，爆破用户名，尝试是否可以进入系统。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy58K8KVkmUNMe3StDicfVYia9V3NtdAEtMuTwOPnVnoOzZdw0kickZA210Q/640?wx_fmt=png)

运气很好先锁定的123456就爆破出了账号，感觉shell已经在招手了。登录系统直接访问/a/sys/file寻找通用文件上传漏洞，发现该漏洞点已经404了。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5ejEiawibvnLVM8LV5S0Zoias9o1CYZzDoGUKl28NtRAXtibUz9oZen5dOg/640?wx_fmt=png)

寻找系统其他上传点，发现系统上传头像处和公告信息处存在上传点，进行测试后发现系统没有对后缀进行过滤，但是文件上传后只能进行下载，不进行解析。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5qySJkiaTBRMuBeBdTI3WpF09V0fyRBNxC3AJfGXl5BAZrv5PQaEObZg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5M77c0Mib2e3wqicbWDgFialdg4WCqNia3qIcddf1WKSJgTK667KiaxgxFiag/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy53NuA3icXPVzPPrnuPAZTicptibcTLZ6xyyjibHHns7tXpviabGeE9ePicNAA/640?wx_fmt=png)

就在要放弃的时候突然发现在上传数据包中，存在一个路径参数。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5ichdj4tiaq2VTc6wsT940fnKa506jXrEL7ocNPV6P21O3r8TFlF4faIA/640?wx_fmt=png)

在删除原先的路径后依旧上传了文件，并且原先的路径去除了删除的路径。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy59a3QpRleUibYzCbPEb7xXCVLhrzePicWsaKUXWjEhmlkmdrLMg7e1WHA/640?wx_fmt=png)

尝试使用../看是否能让文件存在上一级目录中，发现文件确实进行上传，并且存放在了上一级目录。这个目录跨越又让人看到了希望。既然目前的目录直接下载文件不进行解析，那只要上传到web目录下说不定就可以进行解析。从文件上传处获取的路径和注入爆出的web目录不是一个目录。尝试将文件上传到web目录下。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5KQhr5en7WAWVZSb5FTIwI775ddkhvJibFSQpX4Ec8g92jibdnz1BoVZw/640?wx_fmt=png)

系统在/a/sys/file/download/处存在任意文件下载漏洞，我们通过此漏洞判断文件是否上传成功。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5hT9JaFia2lzck8HjmZHgNVBicErSlD6IzS81ZCuYLoZAGmC4b2anOAuQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5Nje42USv0GJNXDQEx2gmS8PicwgV3wOyu2f2iaXtJWLuz6ticQE4kUKVA/640?wx_fmt=png)

根据注入路径进行上传，成功目录跨越进行webshell上传，获取目标系统目标系统权限。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5MqibzmpOmowJroicpGIrJLUyYHVmhGbCubp7eeoFCpiaMmt8j0BdG0VOA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXQOiayI0u5LO3pkpUXTJmy5h2ppibWRhyG099IR1ytzPLpzgbIaOvRYyic51wPzeTEsL4rOk0WnibrEQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/rTicZ9Hibb6RWbGNtVfIZbm2rmGO4hQDzQUrLN62vEGlA4fPmib5utUAp9gbQicb6FC82RjsVI5vx7wEc9yAAiaFEoQ/640?wx_fmt=gif)

E

N

D

**知识星球产品及服务**

**团队内部平台**：潮汐在线指纹识别平台 | 潮听漏洞情报平台 | 潮巡资产管理与威胁监测平台 | 潮汐网络空间资产测绘 | 潮声漏洞检测平台 | 在线免杀平台 | CTF练习平台 | 物联网固件检测平台 | SRC资产监控平台  | ......

**星球分享方向**:Web安全 | 红蓝对抗 | 移动安全 | 应急响应 | 工控安全 | 物联网安全 | 密码学 | 人工智能 | ctf 等方面的沟通及分享

**星球知识wiki**：红蓝对抗 | 漏洞武器库 | 远控免杀 | 移动安全 | 物联网安全 | 代码审计 | CTF | 工控安全 | 应急响应 | 人工智能 | 密码学 | CobaltStrike | 安全测试用例 | ......

**星球网盘资料**：安全法律法规 | 安全认证资料 | 代码审计 | 渗透安全工具 | 工控安全工具 | 移动安全工具 | 物联网安全 | 其它安全文库合辑  | ......

扫码加入一起学习吧~

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RWbGNtVfIZbm2rmGO4hQDzQvvk4mDJOoZHS64icia8WtbOojy8cia4Ztwv8TTFUkBf4kkdoNEpNKkFbg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUGxmZ0l89buUNbyVALKxic2nM7hnDCkAKIrjKhdcDfVkGq3PxNzgs7m55BBMwmicc0AvFpYcrd6J6Q/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

Tide安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

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