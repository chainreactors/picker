---
title: 1 + shell = 18 web
url: https://mp.weixin.qq.com/s/T0AXBB6i4Pzo__38aWeQCA
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:08:15.947381
---

# 1 + shell = 18 web

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/16lHuWzRRdsSr7XMQC75O9GhKJY17YlsflKUOYSujibPicCiaSazNj14qfO5C5GLonnvHXHaiaLBqGglcwQibeWx6LafIlUib8cF17FKgib9vkcAibQ/0?wx_fmt=jpeg)

# 1 + shell = 18 web

原创

private null
private null

轩公子谈技术

![]()

在小说阅读器中沉浸阅读

故事背景

接手某局的渗透测试任务，资产表上只写着一个平台名和一个孤零零的 IP。可当我满怀期待地访问这个 IP 时，迎接我的却是空白页面——打不开。目录扫描？依然毫无收获。那一刻，我仿佛在睡梦中摸索，四周一片漆黑。难道我要托梦给客户，告诉他：“渗透测试结束，系统非常安全”？别开玩笑了，这种报告交上去，怕不是要被当成“梦中渗透”……

常规的 Web 探测手段（IP 访问、目录扫描）全部失效，意味着目标可能将服务部署在了非标准端口上。为了打破僵局，也为了证明自己不是“水货”，我果断调整思路，对目标 IP 进行了全端口扫描。而这一决定，直接促成了后续文件上传漏洞的发现——18 个站点 getshell 的故事，正是从这里开始。

我通过 Goby 全端口扫描，辅以 Hunter 和 FOFA 的资产关联，实现了全方位探测，确保每个潜在站点都被覆盖，无一漏网。

探测的第一个页面，是魔改若依

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtVMS3wmNQXQ6fM2uIZMdNv4Wj3hS4xPzibXStzXFTExtiaGPcgMrkpiceKSQ1ibyhkDE8dicmovDIIPtdibutEZibTvfiaePkg7MUGBN8/640?wx_fmt=png&from=appmsg)

注册页面与注册接口双双 404，常规入口已封死。剩下的突破口只有两个：提取隐藏接口，或暴力扫描目录。然而经验告诉我，目录扫描大概率无功而返——必须把重心放在接口提取上。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRds9xt9qmghZjcHUbQqadEBriacldTlO2LFnzmmo9HzkSr6EC1HSDDtfQZTFHzscvBasNZe9ROTE8F47V6A8EfyIxSmvfCvemcQY/640?wx_fmt=png&from=appmsg)

事实证明，我对了

点击“导入”按钮，Burp Suite 抓包，意外捕获了一个前端 JS 中从未出现的上传接口。尝试上传图片，服务器竟直接返回了访问链接——这一刻，我终于摆脱了零产出的尴尬。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdvdcYKAldYiaUYqTkMWz4Vw8Z84T2J4XeH6e2tcONPBgLzKF0IM9V0vbMTN0XugO2rWMqHvmyUDSrGsnEs2IZodDswiakkwKhyW4/640?wx_fmt=png&from=appmsg)

尝试上传 JSP 文件，却被白名单无情拦截。不过，HTML 文件居然可以上传！虽然暂时拿不到 shell，但能植入恶意 HTML 页面，同样构成严重的安全隐患

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRduPbA5E0UPBiaStwAZKDwgevpsh9eVq7U6xicpoTYwhFOFEeV2xJFuiaicCyrnRWLq3rsrRftWpJaIJsbrhRRbol7UeicfEmxlibhyRY/640?wx_fmt=png&from=appmsg)

第二个页面访问 404，是 tomcat 中间件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsR1lUAJZNhYZmM0Lj9JcBZd3XnRJb0fSGLDbX2CiaqzJxTD9yvcuP0h2DoQ0iaVLnOcl7JZWwQbYJiazJcdW8xn8aPObcwiaznLhE/640?wx_fmt=png&from=appmsg)

针对于这种唯一的思路就是进行目录扫描

刚好发现了一个通用的 cms，乾润报表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdvjs6nial1pib4ic8wibKHgM492vM5zN3O68PcphjWaOmKlc84tHRsUJaoYIsZCAkOoWnnJUQVsYfEqYeBN68SP1WDYovsFMkeawDw/640?wx_fmt=png&from=appmsg)

既然系统存在历史漏洞记录，也就不费劲去审计了。

直接尝试访问 /servlet/dataSphereServlet?action=11

——果然，任意文件读取漏洞依然健在。

目标为 Windows 系统，默认站点在 D 盘，读取文件时稍微绕了点路，但最终还是成功将关键文件收入囊中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdvulXMibEQQTKnM4GVKeMH93Hzb5xQuIJYMrZoYwodp1WeWicKh1DncwiaWr0SwlpM7KptxnQQzibu9W4SIt49cYYX1libGuoC3Ml90/640?wx_fmt=png&from=appmsg)

文件上传直接 getshell，就是本文的重点了

servlet/dataSphereServlet?action=38 上传成功

InputServlet?action=12 上传失败

这个接口有点异议，如果像常规的上传包，只给一个参数，也可以正常上传，但是解析 jsp 失败，访问报 500

因为他这个路径不是常规的，所以 poc 这里就要把 path 值直接改成 /

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdtmciaBVWYRDyQuL7RcITS3f8CQt4fdj8Fibb0DoEuW3C3Wy87B27ibrbG9TaUc8qbrEbYxp40icZrPQcpV9m2TQ6qrFUxuMGziaKC0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduJ9VaBtz50lFCIkbicsyicOic3riavo5xcPgIeQJ0tS7Mqm1Y82eicNJlS5e3CvS6XfqsEsYqqe9UTRLibomHq4yLulNv9KU4D0qceA/640?wx_fmt=png&from=appmsg)

一句话小马报错，类什么不存在，这里需要加入

import java.io.\* 相当于完善 jsp 的语法，就可以解析成功

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdvaRhtlqic1ialia8msqK2jBFTc5GIkgthQESoqica4fboAqVQN4udxWRau3NMCApwq51v7T4y2Wrib4mCZqSzTMqfnv2Rw4yz2YtOM/640?wx_fmt=png&from=appmsg)

查看了端口链接情况，开放了很多端口，发现每一个开放的端口都在 Hunter 里一一对应，刚好是 18 条记录，也对应 18 个站点。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

轩公子谈技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

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