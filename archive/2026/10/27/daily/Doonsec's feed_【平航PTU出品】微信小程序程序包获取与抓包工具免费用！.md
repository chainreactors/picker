---
title: 【平航PTU出品】微信小程序程序包获取与抓包工具免费用！
url: https://mp.weixin.qq.com/s/Bu7JjA2Dkkr-dQ8T4Pq9eA
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:42:22.451741
---

# 【平航PTU出品】微信小程序程序包获取与抓包工具免费用！

# 【平航PTU出品】微信小程序程序包获取与抓包工具免费用！

平航科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/yt52qCDA2icrmfGlsTfLaJ9rGbic4K1UicjwWImiaS4Q1yFDrJ98rf0ZjDnNiaxVmTibSbbhS2LX6chQ4iaV8W8IA56UQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3dkZpcsMPxW937blicWvhJ10DcEwUtqCEB2eCMNkiaaibwajJGthicOXSckib7RgLPp4zjhEIPBldozyfbpLbocS3Wj5v4b4sWb0iaEqURZbYWM7U/640?wx_fmt=png&from=appmsg)

**写在前面**

Link+本期分享微信小程序程序包获取与抓包工具，同步配套IP地址批量查询工具，两款一并免费开放！

![](https://mmbiz.qpic.cn/mmbiz_png/3dkZpcsMPxXagHTr60gOlCRcO9T9TTDEXskibMnIVDkVeLmA7V4mzmcYgwC4kGKdm2o0L96U8XMHhDvnfk7PrlQfTC2NLdvEtHWJfmAQoBcw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxUZMMW7fNXbUPM5joxDoL6A8diazPgsy757dP9R2DMOfquItxNBiaDeRjTSzrng1x7lb9xRs4a7sxUUdz96HNEjNlwZh5Xll2q8I/640?wx_fmt=png&from=appmsg)

一条“年报提醒”短信，把个体工商户C某引向一个“政务平台”小程序。

案件中，C某按小程序页面提示填写信息、支付完所谓的“补办费”后，才发现被骗。**仿冒小程序往往是这类诈骗流程中的关键一环。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxVy8mkf6G0fnkKd1zlFpc589nFLjvupILWTG8YF6MEYJc6ibpwkCgzib2ICibB4HobHNIqrsian9ENU9Fzbgzib27mov7HvztFOtCQ8/640?wx_fmt=png&from=appmsg)

分析这类小程序，可以从**静态**和**动态**两方面入手：

* 静态分析程序包中的代码和配置，查找页面功能、开发框架及第三方服务等线索；
* 动态分析用户操作时的网络请求，确认数据与哪些地址交互。

将两方面的结果对应起来，可以梳理数据去向，为后续调证提供依据。

**微信小程序包是什么**

**在哪里找**

**01**

微信小程序在应用内运行，页面、脚本、配置和图片等内容会**以程序包的形式**供客户端加载。

在Windows微信的本地数据中，这类程序包通常以.wxapkg为后缀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxXRl3sLNbBubQGv9EYvckRibbjy2ibEZS6M3EeiaibJYib5GowkUrHyxdFrM1JnRhNcVsazh5EXUUUz2SwwhFqYTCp7pKXGzjIz3Vvw/640?wx_fmt=png&from=appmsg)

同一个小程序可能包含**主包、分包和插件包**，本地也可能保存不同版本。

取得文件时，需核对**AppID、账号和版本**，以免漏掉关联的包，或混入其他版本。以部分Windows微信版本为例，可以从以下位置查找：

![](https://mmbiz.qpic.cn/mmbiz_png/3dkZpcsMPxWgarQmoSO9PhXlHcpkOML70KPEp5rd95QiaVSzY4llmUBzhOcNxSVDlQFwRDQetpGqrIvK0miat17MeiaX6Y5Oibw9ibC2ia94rsBb8/640?wx_fmt=png&from=appmsg)

%APPDATA%\Tencent\xwechat\radium\Applet\packages\

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxW3ZDbgjwCkCkTibxW1XEnKCsEbNMEicibv92BaMbbmeN5vUvQuoHVEQDzXjQNJOCpic0T090n3Qj9IXNRVa2jwyTaL6nU3ibPDpTMA/640?wx_fmt=png&from=appmsg)

%APPDATA%\Tencent\xwechat\radium\users\<账号哈希>\applet\packages\

![](https://mmbiz.qpic.cn/mmbiz_png/3dkZpcsMPxWxFicHbiaRH7abwG6D0PzdGC5XvwZuE20yxwqR4Zx4GPWwVqY63T9AaulDN46DFhU59ovhc4pJvKGxjEzqG2dzUn9246WW0KR0A/640?wx_fmt=png&from=appmsg)

**平航微信小程序程序包**

**获取与抓包工具怎么用？**

**02**

平航Link+上线**微信小程序程序包获取与抓包工具**，支持扫描Windows端微信常见的程序包目录，也可以在已提取的文件中查找目标程序包，并提供网络抓包功能。

![](https://mmbiz.qpic.cn/mmbiz_png/3dkZpcsMPxWmJcwBSXMPGlOYPRXseibu8x59dFicKrowbe8lIiaM4a0adqNEhLZJG9awzNh3pBhucHq6jsuF0s2eaNV8uUagf5rYANyYTvwlSc/640?wx_fmt=png&from=appmsg)

**如何使用？**

**1**

**固定目标小程序程序包**

通过规范操作，固定目标小程序对应的程序包文件。

**2**

**下载安装工具**

通过平航Link+工具箱 -> 选择“平航PTU工具” -> 下载安装**“平航微信小程序程序包获取与抓包工具”**

![](https://mmbiz.qpic.cn/mmbiz_png/3dkZpcsMPxU1DcV9KSLAibuggesSDV7dM0OTlfGshib3rPiaLzP3Cy6sia8y6dTzFzibcm0MkoKO49xpibs0MS1pfNad0K7x9WCic66ib8aiaO2j91Uo/640?wx_fmt=png&from=appmsg)

**3**

**导入程序包使用**

根据指引选择目标程序包并导入后，选择目标小程序进行解析。

**静态分析**

在工具中选择目标小程序进行反编译，查看相关代码。代码和配置中可以分析是否存在**开发框架、第三方SDK服务（地图、统计等）、代码注释、请求域名和接口路径等线索**，供后续核查和调证使用。

![](https://mmbiz.qpic.cn/mmbiz_png/3dkZpcsMPxUQ7whVOuUNGzWAMjq1bmH4icIYk0YFK4ASG8FeicPe7JqyLFeyGGopPIWIicc6Pxtia0Hm1d53Y8eaVzwNnexOK9Rzko2HWgufskM/640?wx_fmt=png&from=appmsg)

**动态分析**

需要获取动态数据时，打开目标小程序，在工具的“网络抓包”页面进行动态抓包。

在小程序中操作相关功能，如**提交登录、点击某项按钮**等，结合抓包时请求的数据，重点看**域名、接口路径、提交的参数，以及能够取得的返回内容**。将这些信息与程序包中的操作对应起来，可以确认本次操作实际出现了哪些请求，数据发往了哪里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxUlRtR6AccVPUPSEYzBvPialB6KCcIYU2cCGg51ZadIHRVDYqxEsdSHvBupmYUnzaHRdTuFic4kON02rpxmdFVktwCIqX65fkiaia4/640?wx_fmt=png&from=appmsg)

此外，平航Link+同时提供**IP地址批量查询工具**，用于协助判断抓包获得的IP地址归属地。

通过本地离线库**批量查询IPv4归属地**，查询结果包含国家、省市、运营商等信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxVicuibm2TUzlStG1wzoUibcpfibSTZXyk2UEwcIeibAWqzPDcBhOt8CQ7n7Y71U1mia0b5oaeBAJS1gLtLNzbaRb61ZDKJBOvbh0qMg/640?wx_fmt=png&from=appmsg)

\* 详询平航官方技术团队

**如何获取工具？**

**1**

**申请“平航Link+取证管家”使用权限**

可联系区域销售申请。

**2**

**Link+工具箱 -> PTU工具**

**下载安装即可**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxX35BkNYk0zDfrNERKiahjibgWFgclnqJmYmN6u7YQExCqGQRwHiaOYYXiaMaq3jWR4SzJH3iboduuIGlvCeqRM4yo74sZicQPsu8rDU/640?wx_fmt=png&from=appmsg)

**产品试用与技术支持**

**联系平航区域销售或技术**

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxUiba3Jqwak3hK0uWjia6JCBhwB6ArLibzJpnaMLZY6bYp3fYjSqrzibiaVWoPAWQOia6s6ibcnrev2nzeHa3u74MdEibwJkIyOkSBnmsg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzI0OTEyMTk5OQ==&mid=2247496365&idx=1&sn=16a2c1debde7627c8ee252dad5c0c950&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxVJ8LsaPQ2cDplLcgLtLjNbGaOIAxZLwtnZcwAGIb1K1acjscQrWd05DVkfIBYhDTNvHKuqiaD9MUEG6vjlUOFoEVmRdiba3BvUI/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzI0OTEyMTk5OQ==&mid=2247497133&idx=1&sn=c6a58ec23b91f8582e3c72f95a040560&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxUeJ3LuiaAcmflQvexlyLs7agmNbFphnZvTZEkRVcTxdAmYtWfmiaUv0zKOibEfyh94B9ZQcF1ynCksSnMdecTgshu8NxkaQeStP8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzI0OTEyMTk5OQ==&mid=2247496993&idx=1&sn=2f7122632e16d1e7702d974cb229f9d5&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3dkZpcsMPxVrkjbJlRLmox9zD0pZ9nNmHAtsL63ibuPIxy4pukxKZKiaWzRIcndiciadcYD8W2t3CiaQRW4hrlEAlZTdgCvibQVfTxoSckDiaQibYhg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzI0OTEyMTk5OQ==&mid=2247496966&idx=1&sn=a72273f516de0c2e52b07dd16093110d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/3dkZpcsMPxXfsS4icvzpLgrYoNicWbdD4ovYMAguOpBUUHtlHgQ5WTPDFcrSDKe3vCJE8GvKcQxVNWMEvyicINHqb0cHF2vnpUEdC4hJ2ThTjg/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yt52qCDA2icoKhH0KibcqrWuKbnqic30HgfjgxTuNC0WebFgRsQCXhiaay6SL1chib77oKj7ePQV2h6wHm9t4ra6GgQ/0?wx_fmt=png)

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