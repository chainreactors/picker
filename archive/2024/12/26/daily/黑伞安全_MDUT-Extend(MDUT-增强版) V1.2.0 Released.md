---
title: MDUT-Extend(MDUT-增强版) V1.2.0 Released
url: https://mp.weixin.qq.com/s?__biz=MzU0MzkzOTYzOQ==&mid=2247489554&idx=1&sn=d3d5aa81f68c323b815bcabe78f0b46a&chksm=fb02954acc751c5c4e4fb8794c7fd8d318bad2e8a08d1b57b229c977358b61d0f75d7c1202f9&scene=58&subscene=0#rd
source: 黑伞安全
date: 2024-12-26
fetch_date: 2025-10-06T19:39:28.845674
---

# MDUT-Extend(MDUT-增强版) V1.2.0 Released

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6IeSyGr0gBGo9vlO88hFnY8Fn8JMt7GfTy3sric1Ukyqibg1lwKbz8ZzJw/0?wx_fmt=jpeg)

# MDUT-Extend(MDUT-增强版) V1.2.0 Released

黑伞安全

编者荐语：

更新的 redis 先备份再 shell 模块很舒服，再也不用只拿账户分了

以下文章来源于警戒线安全
，作者S0cke3t

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7cfNAOu49ANW9eiby6sgz9nBJyrj4ezkNuSajkbAelnnw/0)

**警戒线安全**
.

警戒线安全

## Ⅰ前言

经过几个月的缝缝补补,`MDUT-Extend`终于迎来了`v1.2.0`的累积更新. 此次的更新主要着重于修复师傅们提出的BUG和相关优化建议以及对`Postgresql`和`Mssql`上的功能增强.

**Here we go**

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6IVrq5MyxPjRPRsts3vSRe2y6yIMkibdTq7IY2U4uXtVKkHTvia9ziaUMsg/640?wx_fmt=png&from=appmsg)

**注意: 从此版本开始全面取消了对Http隧道模式的支持,如果师傅们需要此功能那么请不要使用此版本**

## Ⅱ更新内容

### Postgresql文件管理重写

在此版本中对`postgresql`中的文件管理功能进行重写和增强

现在`postgresql`的文件管理支持使用`PG FUNC`和`CVE`两种方式,两种方式均支持`windows`和`linux`

其中`PG FUNC`依赖postgresql内置的文件管理函数

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6Iu8OxyTtgCFl8radibhbg2cqmiaYvicsRoVy0h7aGvVib0fto6tgaHR7zmA/640?wx_fmt=png&from=appmsg)

由于内置函数的限制,此方式只能获取基础的文件名,并且此方式不支持读取中文目录

`CVE`方式则使用`CVE-2019-9193`进行读取和管理

**Windows**

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6Iria7eHM6Uycwj0nIKsiaicWiaLRdJK057WZLsD9bkcxfcg1q76B2cFseRQ/640?wx_fmt=png&from=appmsg)

**Linux**

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6IW0gKoGbUeG8w1KVAGlcWYicNnT5MD2QLE50SZbcJ0G4e23s9DmTzxTw/640?wx_fmt=png&from=appmsg)

相对于`PG FUNC`使用`CVE`方式能获取较为详细的目录和文件信息，同时也支持读取中文目录

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6IZP3qqLWRKuyOw3wPVD2xibdqhuDbs1xDIJSSR8sm6ib7flMHekm6F0Cg/640?wx_fmt=png&from=appmsg)

### Postgresql新增CVE方式读取文件

在postgresql文件管理右键菜单中新增了`读取文件(CVE)`选项,该选项主要弥补无法读取含有中文字符和内容的文件问题

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6IEOHpEoQ4iaakBicEEEw68HJib3OKsMIqXJ4v3ohT2fiaTlYhhSRo5SLyXw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6IKe9No7Wez28nN5ykzvVyicA4SJFicmgmzQdIurOd7BRZ4ZtYtEUk3JjA/640?wx_fmt=png&from=appmsg)

### 优化Postgresql命令执行问题

**@badboycxcc**

在上一版本中,针对postgresql命令执行`UTF-8`报错问题只对windows情况进行了处理(#14).

此版本中对该问题进行了优化.选项由`direct`更改为`base64`

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6ImhQbZic4YxPNPEwOky6B4caaq2zOdR4kEGulOR1skicC4nNxqagMtJ2w/640?wx_fmt=png&from=appmsg)

### 修复Mssql下载文件大小问题

**@Conan924**

在原版和之前版本中,使用mssql下载文件时只能保存前10kb的数据(#15).

此版本中对该BUG进行了修复

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6IochGsaxTjU71Bu1utjkNoEKmsphQe5NW7uJuF96Yic5Z0icfYobjBpRA/640?wx_fmt=png&from=appmsg)

### 新增Mssql提权对Godpotato支持

此版本中对Mssql的CLR命令执行功能进行了增强,添加了`Godpotato`提权方式

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6IiaItNmmJHqkzziacsEArVb2VCLk1qIYnCLphiaZ68wqFV3MZWHdvRdibqg/640?wx_fmt=png&from=appmsg)

### 修复Redis命令执行问题

此版本修复了之前redis执行命令时回显存在多余空格和中文字符乱码的问题

需配合最新版本的redis模块文件使用

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6Iicmx8iaWFaXTh6LSmaRUeZjKnXSUguYhkArSw98kTHYDMGm7aXHDxg8Q/640?wx_fmt=png&from=appmsg)

### 新增Redis主从同步前数据备份

**@枇杷哥**

新增在利用redis主从同步前,对redis中的内存数据同步到磁盘.以防数据丢失

![](https://mmbiz.qpic.cn/mmbiz_png/KGyt5Iecd5FdNbgG2ran6WdRiaUlTGl6ILh14JCKhvnPd1EtREzNYad0N9IwbTTy1dw4qInQ0z8WZEKmOiaQenibw/640?wx_fmt=png&from=appmsg)

### 其他

* 修复配置文件刷新问题
* 修复postgresql文件删除失败问题
* UI界面调整

## Ⅲ下载

后台回复20241220获取下载地址

```
MDUT-Extend-1.2.0.zip  ADEA3261855D4C7F0D9002E4A8416EBE0D6E4397
redis-module-extend-windows.zip 3CF830E474D5E2C22DB2198DD5A52AC36DBBAD30
redis-module-extend-linux.zip  750B6EBA467B636C7A1A2C80B80AD32414D1BC4
```

**By the way,关于timetravel-boy师傅提出的Oracle`ORA-24345`等问题(#10)，暂时没找到解决方法.****如果其他师傅有解决方法,欢迎回帖或留言**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

黑伞安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

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