---
title: 【安全圈】微软蓝屏事件波及全球，遭知名厂商CrowdStrike“背刺”？
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652062936&idx=1&sn=29fb84fbb20520f27ba7a0fde108c14d&chksm=f36e6898c419e18e63ab8763be1905fc729a113b1fd896179f09061c6dced83674206c99f709&scene=58&subscene=0#rd
source: 安全圈
date: 2024-07-20
fetch_date: 2025-10-06T17:43:48.500924
---

# 【安全圈】微软蓝屏事件波及全球，遭知名厂商CrowdStrike“背刺”？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg6026oDdia0zibXxlXXXtaeiaZY2lRdcUZDZBKrlvmIKZdeU4Zq59yAQUVZ7SKqXiajMYKs6H5Pr0hoQ/0?wx_fmt=jpeg)

# 【安全圈】微软蓝屏事件波及全球，遭知名厂商CrowdStrike“背刺”？

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

Windows系统

今天（7月19日）下午，全球多地的Windows系统用户遭遇了电脑崩溃的问题，一时间“微软蓝屏”的话题登上微博热搜榜首，热度居高不下。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg6026oDdia0zibXxlXXXtaeiagGiafGxQ6CkiaFh7LLvHqiaX9UF9WoSGYRcqSA9GNkJJfDBzSq7nj92sw/640?wx_fmt=jpeg&from=appmsg)

点进相关话题下，有大量网友晒出自己的电脑呈现蓝屏画面，其中不少出现了“csagent.sys”错误。还有网友戏称：“提前过上周末了。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg6026oDdia0zibXxlXXXtaeiakfzZkVsgseI0lP9iaxqkWlSWhelXqicKmgVjgKiaDJl38e7r0c5NnOkfQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg6026oDdia0zibXxlXXXtaeiaj9RgvbJXyQkzWo4Sr0F5mtic1RmOK1HocrhDQKryENNuW78G0CcaQEQ/640?wx_fmt=jpeg&from=appmsg)

有安全专家表示，此次全球蓝屏事件的原因是由CrowdStrike代理（csagent.sys）导致的“WIN32K\_POWER\_WATCHDOG\_TIMEOUT”错误，从而引发了系统崩溃，出现蓝屏。由于全球大量用户使用了CrowdStrike的网络安全解决方案，从而引发大范围的服务中断，看起来似乎是一个“全球事件”。

据阿里云监控发现，北京、深圳、上海、杭州、东京、新加坡、印度尼西亚（雅加达）、菲律宾（马尼拉）、泰国（曼谷）、德国（法兰克福）、英国（伦敦）等地域的Windows 系统的云服务器ECS 实例异常重启，阿里云工程师已向微软反馈，目前正在紧急介入排查。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg6026oDdia0zibXxlXXXtaeiaHb4ErLE9zBpjxfObJlMTaZK396cCORaqwMolQjvF2Gvvg8bSicm2Ckw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg6026oDdia0zibXxlXXXtaeiavyYic5OzicD9z3DGjH7nwra29zWtaWesmqBjNxN8WkmDPSTYhmHc7gjQ/640?wx_fmt=jpeg&from=appmsg)

据悉，此次 Windows 系统中断还波及到了LME交易所、多家银行、航空公司等行业。

根据美国联邦航空管理局空中交通管制系统指挥中心，美国联合航空、美国航空和达美航空已对所有航班发出地面停飞指令。德国柏林机场也称，由于技术故障，登机手续将出现延误。

对此，专家提出了以下可能有效的方案：
1、三次异常重启进入安全模式
2、打开路径C:\Windows\System32\drivers\CrowdStrike找到csagent.sys，修改此文件名

## 网友反馈曾多次遇到更新错误

昨天（7月18日），科技媒体Windows Latest发文称有网友反馈，在安装Windows 11的7月份累积更新 KB5040442 过程中，曾多次遇到0x80d02002、0x800f081f、0x80073cf3等错误。还有网友反馈，连续安装3次KB5040442更新，每次都会报告0x80d02002错误。

另一位网友从Microsoft Catalog Update下载更新，手动安装更新也失败了。Windows 11用户还反馈安装7月份累积更新KB5040442之后，出现了拖慢性能、循环重启、卡死在修复模式（最终蓝屏）的问题。此外还有一位Reddit用户，在更新之后电脑和虚拟机变砖。

微软出现蓝屏，通常是指Windows操作系统在运行过程中出现的屏幕显示蓝色错误信息的现象，‌通常伴随着系统崩溃，‌严重影响了用户的工作效率。

此次Windows操作系统遭遇大范围蓝屏故障，‌引发了用户对其安全性的担忧。‌

## Microsoft 365系列服务访问中断

除此之外，微软还发布官方消息称，旗下Microsoft 365系列服务出现访问中断，受影响的包括但不限于Microsoft 365各个应用，状态页面警告称客户可能无法访问SharePoint Online、OneDrive for Business、Teams、Intune、PowerBI、Microsoft Fabric、Microsoft Defender和Viva Engage。

微软方面表示，服务中断始于美国东部时间周四下午6点左右，其部分客户在美国中部地区的多项Azure服务中遇到了问题，目前微软的策略是将流量路由到其他未受影响的区域尝试恢复恢复。Azure是一个云计算平台，提供用于构建、部署和管理应用程序和服务的服务。另外，微软表示正在调查影响各种Microsoft 365应用和服务的问题。该公司还表示，随着问题不断得到缓解，其观察到服务可用性呈现积极趋势。

根据网站故障追踪软件 Downdetector 今天（7 月 19 日）公布的数据来看，日本用户报告 Microsoft 365 出现了问题。截至当地时间下午 1:35 左右，共有 2800 多份故障报告，其中 69% 的报告与 Onedrive 有关。

微软的Azure状态页面建议，已设置灾难恢复程序的客户可以考虑尝试采取措施将其服务故障转移到其他地区，如果遇到问题，可以考虑使用编程选项。目前，微软虽然已经宣布美国中部地区已恢复运营，但Microsoft 365 仍处于降级状态，许多服务对部分用户不可用。

文章来源综合自网络

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhEa6M1AIDFKXVZYkvibHolmkkAPfB37l9kuvJwPeIj3M2HPo6EqUv8YiaxAez2icXYq3tZkq3u65IlQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhEa6M1AIDFKXVZYkvibHolmibB3GD6iaNBbs0L0OA2X1H5BibicFPCnLbkcSibESZczEdcKfhM7ia7oibibaA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhEa6M1AIDFKXVZYkvibHolmzFL32jQmbjYal3cpaopjjqN4NUJ8OibpoiaKN3EpcCJY9Wo9pRXUTSnw/640?wx_fmt=png)[【安全圈】新加坡要求银行三个月内淘汰一次性密码](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652062916&idx=3&sn=d0f3cfef85f8e2ac1b5c07812f9c3b45&chksm=f36e6884c419e192fb33660afb03e17311e3b54a818d01cd27ec0ede526c9658ad21787b9c69&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhEa6M1AIDFKXVZYkvibHolmA51qtiaeTciahSlHAuBunhsFO8YLZriboDPG7icn7OeZzkJxkgk4iavFnicw/640?wx_fmt=jpeg)[【安全圈】科技巨头被曝未经授权用 YouTube 内容训练 AI，苹果、英伟达在列](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652062916&idx=4&sn=320b04e041e86a1907c39453a528416f&chksm=f36e6884c419e19281c3f04e7415caf77720532af8701028529d05e35bfff68e8590378b3932&scene=21#wechat_redirect)

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

预览时标签不可点

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