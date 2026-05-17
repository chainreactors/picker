---
title: 记一次对某211大学敏感信息泄露
url: https://mp.weixin.qq.com/s/Bh_Di66OwgaszjI26b8mZA
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:44:28.352486
---

# 记一次对某211大学敏感信息泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DC4TgvRKhOumnlVkEs0clKhW98h1SutRe4mrolt8jxVibfIia1vUF7pHb7UZKrwRqiaJJcHtiauWJAJtcSWxMvIdUdL8M1GbZb8EXCuAdl1jMow/0?wx_fmt=jpeg)

# 记一次对某211大学敏感信息泄露

锅盖
锅盖

OnePanda-Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**OnePanada-Sec 招新啦**

**招新要求**

* 热爱网络安全，喜欢 CTF；
* 拥有 CTF 比赛经验，有较好比赛成绩的；
* 乐于奉献、热爱分享，愿意提升自己同时帮助他人；
* 时间允许参加各类赛事，服从战队管理与安排；
* 各类比赛获奖者、能力出众者视情况考量；
* 未参与其他高校联队；
* 大一同学视情况放宽资历要求。

**联系方式**

请将个人简历发送至以下邮箱：

简历邮箱：2638726415@qq.com

#

# 信息泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOvZgMu94yS9GhTicmzX0wrMr3Iia3fJLYQNZT5yjEhCDqDZfuwJ5uqgYkhtTfuGtuQW96pyP1rG9A1CNiaQjyvmy8Ft2z2BkZMXTU/640?wx_fmt=png&from=appmsg)

账号密码: xxxxxxxxxxxx/xxxxxxxxxxxxxx

开局登录框 但是已经收集到一个账号 开测
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOtWEGkuMR7A1QWvawqhNssic0w5NczibicpVaSAhdxaZzgWzTXdLZbTJBXBMsib8V32UzIaqPMBMBGD8LiaJCVy4hGW1DZ3m3a4qsicU/640?wx_fmt=png&from=appmsg)

开局就是一个信息泄露 然后继续测别的api

### 越权

后面又发现一个未授权

接口能未授权查询token

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOsCmibHtrLNUxncn7OCoLXoqOKGcDZLoTJACsGAHYXjGCADTjCZkFDN04ic07mD8Po8bibxmzGicqCGv2gg97BCvCIWQcbb5FlNWfo/640?wx_fmt=png&from=appmsg)

可以看到能直接返回token

替换Hsnt-Auth

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOvot6Vf3x1jSbJZRcbQaab7PKgm1Fw0eEHcN5icB57EImQCMPqLptoYRn8LibSCysKL1Oe2MnNgeqJfOvoBlATsVqvyqF1IooU4I/640?wx_fmt=png&from=appmsg)

此为账号A的token查询 因为此账号无审批记录 所以查询信息数据包不显示 我们替换其他账号试试

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuiafhzvFHwLNs8ll17vPVMhpAcsovu7UGTyFdfUwNGVgCMrD868kwX2vomxMs1x0DllJIEtNLJPTpCib2reianNTrpiaUoEZJ3xf4/640?wx_fmt=png&from=appmsg)

查询到一个admin的账号

再把token替换过去看看

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuOicD9ibW5CMlSpia1gc27t5DhVnqG2ksEd5198mJVJ7SiblguojwVDFyfTs8n9ZVP0lnhCubFzr7MkD3bWHJBbMY6SNg6DBQUeVc/640?wx_fmt=png&from=appmsg)

替换 能查询到大量信息

这里师傅们看的有点乱是因为 开局我们收集到的就是这个admin账号 后面发现api能够查询到其他账号token 然后再用的普通USER去测试的越权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vkibCXbGicB8N9xk73iamtLplTt37OUxp77DcYIOQb0QLJ8oQnEfTEUsTql1OFoKOz54qPSlOKu4BS7J6iaGlhaVcDzrZsbGzIIFGblGy5uY1S0/640?wx_fmt=png&from=appmsg)

**PART 03**

**微信QQ交流群**

欢迎大家加入[ OnePanda-Sec ] 群聊一起交流 ^ ^

![](https://mmbiz.qpic.cn/mmbiz_png/vkibCXbGicB8Nj9sRGKmdpcnZnxUKQ7OWqDaCxXibArvnnHh8P8ib0WeFOZ9d5lw2BgRhJxNYfyD1GBGMbYSQYA2a0N81sqnLYkOAGDecsZEShc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/DC4TgvRKhOubIZGuDibMkWwSJH1d2tMgvxAnbPsGcWgAfpZpnl9TPKdxN8Gic91fHXeW4VZfcUQChbBoZg6zLfAUBXhEdmZ6Uiaia3BbmlaQjZ0/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vkibCXbGicB8MCfibmV6DB7iaJFWqyQ1jyozX9v37ya1x8ORmvoL4QxiblEzzFVHicfF1cpuabWoDZ5p4YRJQRBFsmso8eSFEj0PyW9Kia0ibhlkGg4/640?wx_fmt=jpeg&from=appmsg)

**END**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZMrhibgToc4EOxfpGXh5oqt7kqWwkiaT7ZtI2x5f0yJMIKia0sLpQz7RKnGtPbhv0BqXKQV90C7hZj4Pvm7EJskcQ/0?wx_fmt=png)

OnePanda-Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZMrhibgToc4EOxfpGXh5oqt7kqWwkiaT7ZtI2x5f0yJMIKia0sLpQz7RKnGtPbhv0BqXKQV90C7hZj4Pvm7EJskcQ/0?wx_fmt=png)

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