---
title: AI 赋能安全测试-基于 Trae + IMA 协同的智能自动化安全测试实践
url: https://mp.weixin.qq.com/s/qVT5gHV0TeUIU2tficubqA
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:45:38.793799
---

# AI 赋能安全测试-基于 Trae + IMA 协同的智能自动化安全测试实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xY9ZTT0gDw5khECvGJDWIBDhTvY1l3lKKwKzCck4gYmiaRbDQ27nFB0hVB1eAZnDNUBj0sqrbgOZ6aG587akbSHO7uxpiby33ILKHzFv7Jiaiao/0?wx_fmt=jpeg)

# AI 赋能安全测试-基于 Trae + IMA 协同的智能自动化安全测试实践

原创

huan666
huan666

huan666

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、前言

Trae：字节跳动 AI 原生 IDE，是能理解需求、自主调用工具完成安全测试全流程的AI 执行智能体，负责自动化跑用例、生成 PoC/Payload、复现漏洞并输出报告。

IMA：是腾讯的AI智能知识库工具，负责存储、检索知识，为 Trae 提供 测什么、怎么测、如何判定” 的知识依据。

一句话记分工：Trae 动手执行，IMA 提供知识，协同实现自动化安全测试。

二、工具下载

```
Trae：https://www.trae.cn/ide/downloadIMA：https://ima.qq.com/download
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6taZhibsjmxIhCdoL9nP5FbNV6iauBcLSUpOkotLXcMBhLicdfkR5lq1mOa1HwFsFCS1dOqWvWyY3bVQ5X9ov5mibNKJkM97frAsg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw4pt4355ldtnDq82nUhBTqHTQvrCLzZatKjU1P0iaBeTMwiblicicib0xdIfcm6Kk87Eoan5IYmkj46Q8Mwv8fOcms5dsD323H1QlWc/640?wx_fmt=png&from=appmsg)

三、环境配置

1、获取IMA API key

```
https://ima.qq.com/agent-interface
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw7cZ2rkvvE3BFPDFXEZJRIXtWq5u2jd46kdg1Leg7ErwP7G1RqdLeVB8QMrTJF0FkC5hQiasVLYdjTCB1XiaRdZPjicPMoGHDcbt4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw4B3ShdkwSjK74rJ2c9NhXqDFG9kzUln0gexnBEuFRTQ0sHFWHUssg1LC480A5BOegFDPPX06IWdGny7dhkhoGnTN7FIgNDSVU/640?wx_fmt=png&from=appmsg)

2、Trae安装ima Skills和API key

一键复制安装命令，自动安装skill、配置api key

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5duGoJBAicW7yicvTBiaJ3vrVN61oOZ4zF0cKATNangr6R11UDZ9YOiabCB5M7p3aJLyS7TezicbQZfH0icBHTlGJ7eiae3uCmpFS9Ag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw4E8ItFvZ5Gn2TANgohOCeLf3YPFErkaUZGOIyI1nK4KyXasibjzwtKwYdCL3pdnJwJoznp4vW3CMN97EBURicjhUiagBqHennbjE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw7uNgJ9SMuhGNV91N8CAfSKnT0tiaYcjbSXA1MUOjSruEiau4Z4dqQfaemeWTiawFrvsKdIAZukEVHCDCD50EOqRosVsOIpJO2efI/640?wx_fmt=png&from=appmsg)

client\_id和api\_key存储位置

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5FzHcB2oNH3IVvyfFndb4Lt0RdQHO9mTp2m2DRCKsYDfzeCZcuvTuspmvYJh0nVyVTcOHKQjTqTeVojqX5znia54yf8zVFQnwU/640?wx_fmt=png&from=appmsg)

client\_id和api\_key需替换为真实数据

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw7hsAZWMcibXZBMsj69sL1AiaBjTfJWOoCibuGkK2znsu97ptpX5hoqPauvibRD9kXhDLLxt6lBuuTicWjkT49jArQ8ibZ03DvNUIxIg/640?wx_fmt=png&from=appmsg)

四、环境验证

1、IMA创建知识库，命名为网络安全知识库

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw7lo53BJKaPqic62aesUvTMficnoyDGB26qLgJbjJolx3icQTO0OAUQd6AibpPFF8Yyv9VriaEjsTDFwJsBwRQLvXBFwKfNPusr4aKw/640?wx_fmt=png&from=appmsg)

2、用Trae连接IMA，给一个文章链接，让IMA存入知识库中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw73lTjxUiaO5oEeSicFCcwpxOJ2ZWHmrjbOFIBjmNVe6FBgjSbelZlGgqQOKGNaU0TYsbcXD76BFXoEOibP6iaAB7FSicPJBTXTPTpI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw56eRtpe0pKpeaDNxeNeaa9rS18YykQAX4oJewZDCgY6BtjhzrnA1f8YErwic7fgncoUPXhU6dhtwymXacKmcg8weYVfxJjDN5o/640?wx_fmt=png&from=appmsg)

3、IMA验证结果

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw7iaXLL4Q99Y3fDniboKqM4NTVb2kNEhBDIBeUia2EJTeYSHpV0XmBTIJsPUZsicMZ0ibLp8Le9BF4HRp4XyTbzI2QiaiaKZ93rRkAVf4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw4euvoWNBaPL2hGsrVwWDzKnvTUoxYdVgMtwXw3uxBMib791dxCCtArevPickTHiaFPvTfD5IUIBRetaRKktHtuZXooPhDSPk6Vr0/640?wx_fmt=png&from=appmsg)

4、IMA支持上传附件，你可以把历史安全测试报告、漏洞资料全传进去。数据越多，它的安全知识越全，检测效果越好。

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5cBhSiaaHLvUYZKWMLpNfIiamEYoURLRcY0t1JW2816avYOI5hGAE75v1yy5Q0A5pFkBOA6XqoSSbTO4hgJgMunjCc8DdAOwzicE/640?wx_fmt=png&from=appmsg)

五、案例演示

提示词：

```
/ima-skill 学习知识库中的技术，根据学习到的思路对target.txt文件，进行真实的安全测试，并出具安全测试报告，要求漏洞必须真实存在的，在报告中带上请求和返回包
需要爆破的话字典用dict.txt文件
```

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw6oGiau3dNmokzCACIHiayLhhvVtfkibGVozRmDF0Xdrs4dm6uDuDpibfv2oOTNE5AeWMddIsQQUM3IruQqTaHqxuTvvxA0FRicibiac4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5E2UOvBpwvokicnEibjXyaSEOibsvxjLsDib9aiaaQQj4cMZhs9VA0FibbH0luzicckMnrmgoCCS67TJDFoG7hMwfDFHRWhibl8QFym0k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw7xDRiasnIRYtCSc7k3OyR7kqR5JfPIffJljZmkBEZQlE26CibLmocFSuKakI5ibaEWxhun5QEBPcWFichB0UppW4yVI4Eqn1Qfkjo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw718Pqy0K6BwnQQblTzetb2LVkGj9cJD50WpicfxmpSWc9GyP9ox9oahyy0ZGdZiaNyRZBBdKibKcbHkovIptFzn7ibaDiaQ0Q5v9ibI/640?wx_fmt=png&from=appmsg)

六、总结

本次借助 Trae 执行 + IMA 知识库 组合开展安全测试，仅为个人实践思路分享，重在演示AI 协同自动化安全测试的可行方向，供大家参考与优化。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

huan666

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

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