---
title: Java源码路由提取工具-html单文件
url: https://mp.weixin.qq.com/s/A-5bCXy5BPtD6z21yyTcqg
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:05:42.746095
---

# Java源码路由提取工具-html单文件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TezRTl7qZQSTvib2T5LME6YzX9oTnicY9Iga1MIDzDcIBd4qXVtLlJ6e1d9MB3qqz7GEAml020SBbvSZxPquoxWQ/0?wx_fmt=jpeg)

# Java源码路由提取工具-html单文件

原创

XINYU2428
XINYU2428

XINYU2428

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 0x00 前言

python脚本工具多了经常找不到放哪里去了，想着修改为html单文件版本，加入书签好找，现在更方便了，有浏览器就行。

我觉得把一些日常测试过程中，常用的小工具做成html单文件版本，在浏览器上打开直接使用还挺方便的。

好用的工具可以减少很多重复的工作内容，提高测试效率。

## 0x01 工具使用

**工具主界面**

**![](https://mmbiz.qpic.cn/mmbiz_png/EiaAlibg03DSfm6V7q0IySibEuFCM02dnfuIaNtiaVQpoMb33zoULdDTQRDUuFfqOAQ3iclZicn4h8xp56nMenOZNuKCOCUHicYtpB0gmRd3DXYIXw/640?wx_fmt=png&from=appmsg)**

**Java源码路提取**

现在基本遇到的Java源码，都是spring项目，目前就是针对spring项目做解析。工具会把整个项目里所有的 Java 文件翻一遍，自动识别所有的 Controller。源码里的路由注解，会按照请求类型、路由、参数等等，固定格式完整解析展示出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EiaAlibg03DSdT2X5icLfIdnv5csibficVreUUicJIZF5j8EUDZkjJJn21nr46vAsm7vhURqesuWoeYGrSUXBZ6xNhutU6RX8OWWibDvPLm11RDTiak/640?wx_fmt=png&from=appmsg)

**支持导出表格，在表格文件中，可以很方便的将全部接口直接复制出来，拿到对应的测试目标上进行FUZZ，寻找潜在的未授权接口漏洞。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EiaAlibg03DSd55bsibY5N2XWepBKN736da0IFyFLeDJ6eLciauI9tTuUtiasfnLP1y5LVGH0OEoEMPdq2ickJMNE6ppCFtTvhocwoqw4aRT92RsQ/640?wx_fmt=png&from=appmsg)

**swagger接口解析**

在日常测试中，/v2/api-docs接口泄漏经常能遇到，于是新增了个swagger接口解析功能，同样也支持导出表格。

HTTP/1.1 200 OK...这些请求头内容一起复制进来也可以解析，会自动忽略。

![](https://mmbiz.qpic.cn/mmbiz_png/EiaAlibg03DSdtZYlNDMBWVTE0vSvbtSibvNJIrXFLWdhtBjC85VibWkHgxcEV0xGyGaR7H8PrfDQjga5V50ASjmIwrXM3qG6cex5FXOwJfAQ3Q/640?wx_fmt=png&from=appmsg)

代码里加载了两个与功能模块相关的js文件，可以自己下载下来，放在同目录下本地加载使用，工具完全离线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EiaAlibg03DScia487Y4c2zA0ibgr95N9cUMv1ic4ZwzYlBA8Qy4Rw11BoKIjNdgoNZzshhGXNhMOCf7nlHNrZF1zCNmKSwos04cBjdxd2icN1oD4/640?wx_fmt=png&from=appmsg)

## 0x02 下载方式

**下载地址:**

**https://github.com/xinyu2428/HTML\_TOOLS**

![](https://mmbiz.qpic.cn/mmbiz_png/EiaAlibg03DSfdlyCgtXH8ziaJj0I8cal6ap2alADxX78hC1ibAVmVc1Dibv2AWV36XZ7ZIT0oNOLibpibenibUmts5wzw273p4s7zJic73nQlAlzuV8/640?wx_fmt=png&from=appmsg)

前面私信过我的兄弟们，之前分享的一些工具的下载链接失效的，都放在github上的，可以去看下。后续一些小工具也都会放在这里。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TezRTl7qZQSIRoT5Y77XqSzfjpLr4v7Cx59LztFezUZrYGEicibEaJlyAf0ia5qUHPeknniatgrroJ5XqZvYSJ9rJw/0?wx_fmt=png)

XINYU2428

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TezRTl7qZQSIRoT5Y77XqSzfjpLr4v7Cx59LztFezUZrYGEicibEaJlyAf0ia5qUHPeknniatgrroJ5XqZvYSJ9rJw/0?wx_fmt=png)

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