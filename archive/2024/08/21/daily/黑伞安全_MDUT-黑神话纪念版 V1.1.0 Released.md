---
title: MDUT-黑神话纪念版 V1.1.0 Released
url: https://mp.weixin.qq.com/s?__biz=MzU0MzkzOTYzOQ==&mid=2247489484&idx=2&sn=c611fd8ad50e5e19bbc6b024bde2ea80&chksm=fb029a94cc751382addc71d495e1079cea48f807bbd87d4ae6ab26d80fadd39bbcad18a5f3b2&scene=58&subscene=0#rd
source: 黑伞安全
date: 2024-08-21
fetch_date: 2025-10-06T18:04:51.639069
---

# MDUT-黑神话纪念版 V1.1.0 Released

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdwJbxKeutvDNBIGiccHrrtj5a0uHicI5yY3ibSmDWhONszqvbH7hRo29hbA/0?wx_fmt=jpeg)

# MDUT-黑神话纪念版 V1.1.0 Released

S0cke3t

黑伞安全

#### 前言

前段时间笔者发布了MDUT-Extend的第一个版本,在发布之后得到了许多师傅的支持和打赏。并提出了许多改进的建议，笔者对师傅们提的建议进行了汇总。着重实现了几个提到相对较多的问题，本来打算在原帖下进行回复的，考虑到此版本可能存在一些需要注意的点，所以就重新开了一篇。

同时此版本也是快速更新的最后一版,以后可能就要随缘更新了。师傅们可以随时提交issue后等累积更新版本。

#### 更新内容

##### Socks5代理功能支持

**注意: 启动时需添加 -Doracle.jdbc.javaNetNio=false JVM选项**

首先就是许多师傅一致要求添加的socks代理功能,此次更新添加了对socks5和socks4a代理的支持(其实都是一样的，只是在界面上做了区分)

师傅们可在文件菜单进行设置

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdwIZxrhAqOWarCiaucCl8r1mPIqubnn08OXKaFe0enREpXRQwK9HSZpdw/640?wx_fmt=png&from=appmsg)

image-20240820142118051

代理实现方式使用了两种不同方式实现

其中在实现redis代理时，笔者发现原本的jedis驱动包并不支持直接使用代理。

所以笔者使用了自编译的一个基于3.0版本魔改的jedis驱动包

首先通过getClient获取一个client对象

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdwOFVA1ibu0sFQmibxh0XUg8sjaPfpONUaI5EHFwoSKBoUEbWlQCRGmhvQ/640?wx_fmt=png&from=appmsg)

image-20240820143154074

随后直接将client传入setproxy中设置代理

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdwOhqic7ScLzXNcJzdIxk6xHJH3WQqGS5M0sG2ysEIbT59Ticocstedjicg/640?wx_fmt=png&from=appmsg)

image-20240820143259108

其中`client.setProxy`为魔改驱动包中实现的方法

其他数据库类型均采用了`System.setProperty`进行全局设置的方式(暂时没找到更合适的方式)

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdwR4naUfux0sS5ct4VmsABY5ibqjJRLhGvYqjnI0J430rDabyMlJ9UzQA/640?wx_fmt=png&from=appmsg)

image-20240820143425748

以下是使用`suo5`测试的效果

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdw2klaAYDriaP8A753AeNuv3k1fcUSwwa2sl588aN60Pj4umpfDlJtxCA/640?wx_fmt=png&from=appmsg)

image-20240820143957215

##### Postgresql文件管理功能

此次更新对postgresql实现了文件管理功能(暂时只适配了windows)

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdwqIdrskMC9ibtdxmKCWg9ko98PNVP6UtzCtJCiagiaDrtf4O1JmCEQBJAQ/640?wx_fmt=png&from=appmsg)

image-20240820144540075

由于目录的读取和展示均使用了`pg_ls_dir`函数实现,笔者只在代码层面对目录和文件进行了简单的区分，所以在展示上可能存在一定差异

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdws1ql1lAia9pfJIx1RfGqQMJIRrneBVPJCZLXnEVAThZuPKS5aLr2icbA/640?wx_fmt=png&from=appmsg)

image-20240820145858241

师傅们在实际使用时请注意自行甄别,其中文件上传和读取的代码参考自`PostgreUtil`工具，在上传较大文件时建议使用`io_import`方式

如果目录或文件显示乱码可调整命令执行的标签页的编码选项,目前已知的问题是**无法读取中文目录**

#### redis windows系统支持

此次更新添加了对windows下redis的支持

笔者参考`RedisModules-ExecuteCommand-for-Windows`项目重写了windows下redis主从模块

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdwYwZEucWPjTgP2oHtntN6UXtKYaKqmcjHhUFGNarzianOgXeNO6fNZpw/640?wx_fmt=png&from=appmsg)

image-20240820150703798

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdwTdCqf5m3nf4yP3q9UFwN9K65fW3AiajwbYwrib7OVbAQuL8vYicgqy0Sw/640?wx_fmt=png&from=appmsg)

image-20240820150739844

在原来的基础上添加了文件读写功能,同时对redis利用模块的界面进行了重新的调整

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdwk71zTfiaAY6DmGJmeAIulRyjwhg2kXLDGSMY4kibnnS3eVrAyene2dOQ/640?wx_fmt=png&from=appmsg)

image-20240820150930784

由于命令执行没做编码处理，可能会存在部分乱码的问题

#### 其他一些改动

* 修复了窗口关闭后数据库链接遗留的问题
* 修复postgresql执行命令utf-8报错问题
* 修复mysql执行udf时显示no select database问题

**视频教程**

#### 下载

回复0820获取下载地址

如果你是一个长期主义者，欢迎加入我的知识星球，目前POC库&知识库7k star,我们一起冲，一起学。每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款。

![](https://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGq71YhicyuZoVktXiaoo8BDdwSEfoibNhCVQ6dySB2K7ojIYkLjl3UDMbE9GUBXYREQHcnLiaMqzPoHpg/640?wx_fmt=png&from=appmsg)

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