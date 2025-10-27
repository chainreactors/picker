---
title: 蓝队值守利器：一款IP溯源工具
url: https://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247489664&idx=1&sn=68a5db9df81822ef0cb8e1a38162f7c0&chksm=fad4c597cda34c815832ee100aaf2162e0916a4b3e77433456e86bc58e7dc797a6d0b0dcd77f&scene=58&subscene=0#rd
source: NOVASEC
date: 2024-07-19
fetch_date: 2025-10-06T17:42:33.925245
---

# 蓝队值守利器：一款IP溯源工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSvB2ODZ7HlmeQ1V0uoF2QwdEibYkgic94W0tZKWVuSvpDYRoEAeUl2tYQ/0?wx_fmt=jpeg)

# 蓝队值守利器：一款IP溯源工具

NOVASEC

编者荐语：

力荐

以下文章来源于安服仔的救赎
，作者雁过留痕

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM67q6j80blnygF9QDd2wUgwNCyhz4nJgt9c1icremnicq0A/0)

**安服仔的救赎**
.

本公众号用于分享作者平时工作中遇到的各种安全知识，包括渗透、应急等

# IP溯源工具使用说明

**温馨提示：**

该工具运行时不会对目标IP主动扫描，但是会调用第三方接口，所以会存在对互联网发送大量HTTP请求情况，如果网络环境比较特殊的场景下请勿使用该工具，避免引起不必要的麻烦。

**免责声明：**

此工具仅限于学习交流，请在下载后24小时内删除，请勿非法使用该工具，用户承担因使用此工具而导致的所有法律和相关责任！作者不承担任何法律责任！

# 一、工具背景

背景：

在攻防演练期间，对于重保值守人员，某些客户要求对攻击IP都进行分析溯源，发现攻击IP的时候，需要针对攻击IP进行分析，如果有关键信息输出报告，针对该需求，产生了这个工具。

# 二、功能实现

## V1.2修改：

1.把基于本地telnet的IP端口查询方式改成调用接口查询。

2.whois信息查询接口单一，增加多个接口，确保whois信息查询的准确性。

3.增加多线程技术，提高程序运行速度。

4.修复cdn查询过长的bug。

5.更新过滤ip地址，现在输入的IP可以加其他字符，会自动过滤出字符串里面存在的IP。

6.增加IP反查域名的接口，新增接口报错和成功写入日志文件。

7.优化更新ip归属地的获取，增加2个接口，确保归属地查询到。

8.端口查询优化，增加端口查询接口。

9.整改企业微信推送方式，从原本一个IP推送一次变成IP查询一轮推送一次，每轮查询的IP个数可以在配置文件里面修改。

10.修改日志输出格式，所有日志输出格式固定。

11.增加每轮查询后程序延时，确保接口不会频繁请求而请求失败。

## V1.1新增：

1.新增将查询到的word报告发送至企业微信。

## v1.0功能：

1.实现支持多IP查询，会自动对IP进行去重，去掉非公网IP，去掉非IP；

2.实现基于IP查询归属地的情况；

3.实现基于IP查询端口开放情况，基于telnet的方式探测端口是否开放，查询端口：`21, 22, 23, 80, 135, 137, 138, 443, 888, 8888, 1433, 3306, 3389, 8080, 8081, 8082, 9090, 9091, 9092, 50050`；

4.实现基于IP查询域名绑定的情况；

5.实现基于查询出的域名查询whois和icp备案的情况；

6.实现整合内容输出为文本文件和word文件，如果一个IP没有绑定域名，那么认为这个IP没有价值，则输出文本文件，如果绑定了域名，则输出word；

7.实现将内容输出至企业微信机器人。

# 三、使用手册

1、程序的config.ini是配置文件，[icpapi]下面的appid和key的icp备案兜底付费查询接口，icp备案一共调用三个接口，会先调用两个免费接口，如果两个免费接口都没有查询到数据，则会调用第三个付费接口，建议申请添加appid和key，申请地址：https://www.icpapi.com/user.html的appid和key填写位置如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSQVjk2iaIicVk4ibPUcnTSBNNPsqq7qqtzwMYibvy2Q6icGBHm4GSIeePWPQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSZ1z8OdNPlOB41Dcx2icRxWSoyF8uIGx1Dm7EPVibfYbHlfibwmyNFVCpg/640?wx_fmt=png&from=appmsg)

2、配置文件中[scanport]下的open参数是指是否开启端口扫描，默认设置为0，如果要扫描端口需要设置为1，port里面是需要扫描的端口，可以修改。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSVEA8RxqPuzhuniaibbBcKGAOUuFWCos16UYfanRhqdsf2gfFOEWh9zVw/640?wx_fmt=png&from=appmsg)

3、配置文件中的[wechat]下的send设置是否使用企业微信机器人发送提醒，设置为0不开启，设置为1开启，如果设置为1，则需要添加企业微信机器人的apikey，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSRkueicFaZl7yhZqeIfkbgcJ9cD1TRhyrQ7Dr4UFh96njcRe6qicf1aeA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSd8jh0l62NGFxJGTWicUibcq0ib4lbaLcZPx2HKP8AVVwxgn9EWVBdPFYg/640?wx_fmt=png&from=appmsg)

4、配置完成后即可开始使用，将需要查询的IP放到ip.txt文件下，无需去重。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSAYBaUib6LNBia9pN94udPeLghpbETx7BkOaLNZ508Mc16darKwqwPX0A/640?wx_fmt=png&from=appmsg)

5、双击运行：IP\_Traceability\_ToolV1.2.exe，等待程序运行结束。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QS91H7UYdCT4M3o71L4jCtFlIf3YBtDUiclwuNdpmnIic06SHiaVyMiagCMg/640?wx_fmt=png&from=appmsg)

6、程序运行时，如果配置了企业微信机器人接口，会将查询到的结果使用机器人发送查询结果和报告。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSkm9cXkeMOCo6r0VkV7IQ1MDgl6uvH3N6FEA3FOFml7MHsgc23PuVMw/640?wx_fmt=png&from=appmsg)

7、如果查询到了域名，则认为这个IP属于高价值溯源IP，会在output\_word下按照日期创建文件夹生成word报告并发送至企业微信，如果没有查到域名，则认为这个IP属于低价值溯源IP，会在output\_txt下按照日期创建文件夹生成文本文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSTsZUZZkJSUgAWmGFqicrzWyIFaZasaz12TQ7XicYXTdLkfibA5am8bqXQ/640?wx_fmt=png&from=appmsg)

8、程序的运行日志，可在logs目录下查看，以当前日期命名的log文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSHIw64fJzvvy1MdVBSDYSefzqM2ichpia2bXEYuI47RBrIcl3RVOzFdww/640?wx_fmt=png&from=appmsg)

工具下载地址：https://github.com/xingyunsec/IPTraceabilityTool

欢迎关注微信公众号：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zqf6HKI56gJFCHcN5wOScNgF4JNQG1QSPLlTnlibZ1pLpr1Zy8twlnEUelY5QqdUydiadaibIUELRV2ESOg9nWCVw/640?wx_fmt=jpeg&from=appmsg)

往期精彩内容推荐：

[蓝队防守：如何判断安全告警的正误报？](http://mp.weixin.qq.com/s?__biz=MjM5ODkxMTEzOA==&mid=2247484275&idx=1&sn=f3919c0645b4675ce518f9a4acd6442a&chksm=a6c2cebe91b547a8a32c3242afb15612d285d20f7c9e26c560fd932211ce9d01755aba58446d&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

NOVASEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

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