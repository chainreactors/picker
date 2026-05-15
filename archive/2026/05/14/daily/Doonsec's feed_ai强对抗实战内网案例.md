---
title: ai强对抗实战内网案例
url: https://mp.weixin.qq.com/s/RyFKPVGTEoQLUrIyfEhFDw
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:47:40.226106
---

# ai强对抗实战内网案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibeRzWcLROATEtIXllyhgGjQ1b5UxZN5dibMhp62CVAGIgbibTtxjbXwILBxWicvYyenKna4Rf6gtWjdMVkPt5kQyC2swiar2KQsiaxV78wIEuiapI/0?wx_fmt=jpeg)

# ai强对抗实战内网案例

原创

mkbksec
mkbksec

水刃安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本次分享为实战ai强对抗实战内网案例和红队牛牛一起打的，所有截图均为虚拟机内复现脱敏，过程为实战案例过程。

入口：红队牛牛通过外网打点发现口子上线iis服务器权限极低

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeRzWcLROAQDNh1myPon1fTARxYBdHDRPPNK4f9ibibweEMMJL1YmrPpgLelSIiaH8rR56j01j6Sm7UiblhHC4icPofF3KU9Hmj3OfrEwBC6HNWQ/640?wx_fmt=png&from=appmsg)

过程中有蓝队在后台删我们的c2

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeRzWcLROAQkliaymvUnnNeblxEiaxF4yyHdjlLHBviaflE8Kz81siaNuwFYvZunjYuIeKyXtZNxGds5vbdCQfaFpEJjE3l5B0WsPyMPjtjBP4k/640?wx_fmt=png&from=appmsg)

牌没有问题，把进程信息打印出来，根据我们掌握的免杀技术开始针对df和云镜做免杀

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeRzWcLROAQc2kb2e7zBzl7icm8Qgl5vbJxPS0byB6HBrqIiajJica5BtczTKhXXBH0UMzRQyJa2qnj8XnWBZcEOTaya70MQibKmm1cyRUUaKU0/640?wx_fmt=png&from=appmsg)

常规流程systeminfo >1.txt直接看看补丁

![](https://mmbiz.qpic.cn/mmbiz_png/ibeRzWcLROAT2qA16Fejz0ybHb0DqfAxslA9joZ3OrpvlbVpvXRFn2HsdNjHm0W72C7Hsgbb0bWNKoY1dicPYy9vq2UD6e2lYjM98uXuc7TTk/640?wx_fmt=png&from=appmsg)

弄出来让ai分析用什么来提权

![](https://mmbiz.qpic.cn/mmbiz_png/ibeRzWcLROAT0K3WhOVYLTGibhLSnTlAbLHvIldYJ3GkiaSriaZdJAq8IBhu8W4Um54NLAiaDKxD2rPudicZTEP68BCbLc5icS4g0FZnHR7Y6xaLlM/640?wx_fmt=png&from=appmsg)

推荐土豆是吧，好杀好杀df发力了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeRzWcLROASkFg6WUZicp9xiaOzMD6nAmYGmzlCv3ugVk3qnIMSicqelpF4KnQomKwNic0iciajcjz68fiaKHicmO7yYhiaKzDWhJ7LrKNALRjGhUib9w/640?wx_fmt=png&from=appmsg)

这里针对采用的是api动态调用，直接syscall，ETW致盲还有点其他免杀技术

直接让ai写

![](https://mmbiz.qpic.cn/mmbiz_png/ibeRzWcLROARLQrFMxzwonSZrvMBJTCCzWvibMyibOnI6PbHISPBRribZyITOzX0nlo8385uHqV6gPeMveH4Jxo0y4MFDPrSnTKYfQCrCjJogCU/640?wx_fmt=png&from=appmsg)

上传不报警，免杀有一点过头了其实，360核晶动态也能过

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibeRzWcLROARFhuYT2MpZD3f0rpIs1YbY94nTpj2icepFzOtDdiavg4oaIs3PYewDRbiciakwV9rT2FqM1ibcT0FAIrzicLlFnUN41KRjVDX0N7icibE/640?wx_fmt=jpeg&from=appmsg)

然后发现提权失败了，排查了一下权限

没有SeImpersonatePrivilege权限所有土豆全部失效

![](https://mmbiz.qpic.cn/mmbiz_png/ibeRzWcLROAQ4WFGeyrOsemUINfdGJ7Qb1TK9xMKMb5B5KV0uj313mFxicpdnLiabaJrbNeV16GNz9H0HTsCRPnvUiaxdXt46njxDbT41bc0yyY/640?wx_fmt=png&from=appmsg)

靠了，然后通过wes.py查提权脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeRzWcLROASWeE6L9PicYuaxlDzh4hjgYxJuNamowcK5YAOMj1kjBJglicRaf022RK7Eic98PzIvqoficdm5Vsd54TAYnyW0qDqfm3ibk4VhoOlU/640?wx_fmt=png&from=appmsg)

找了一个打印机功能提权SpoolFool

又是一套免杀操作，然后红队牛牛说失败了

依旧排查问题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeRzWcLROARFWdhLdOO0aabkK5OW5uDjN71hlibVD27otZod7DImMq5SGibaOibz7u3icibQicHC4icp2B972DhISobVTrRicf4at4LUDefQ5ibRyVME/640?wx_fmt=png&from=appmsg)

好好好依旧不用打印机是吧

感觉我依旧被对面看穿了，然后ai让我找了一下可写路径打dll劫持提权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeRzWcLROARicjkzyxjXUFOUPwTKibhbdvUqugM2CrARBbGm0jQpPwjkpicI3FWC3sDrdFIOPB2I8niaoTyM7gbX0ylVPTZxeotVSu66G0Np6zY/640?wx_fmt=png&from=appmsg)

考虑到在生产环境不能重启服务怕有问题就没采用这个方法

然后ai分析服务让我们打sqlserver

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeRzWcLROAT1wPt5h21UoqbKzFaujccqTpvW7ON0PIUAsWrhia96fn6Bfoialv8zGACTGXSLXk0iaqA3jefWWJg1H67zcCbFg5QK7ULteCgCAw/640?wx_fmt=png&from=appmsg)

当然他那个命令没有生效，但是红队牛牛发力了，找到了配置文件我就不放出来了

然后就常规xpcmdshell的打法了，权限稍微提升了一点，直接我写的免杀土豆家族

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeRzWcLROASV5u2EpaSJPje1bxkiaCKavicbYBtMeSPAflBXU9iaWiaSHy2pllsjjbf73pakaanZb2PAuAaoHriaY0RldNsZ21gECARfDq8D9gJI/640?wx_fmt=png&from=appmsg)

rdp直接上去到这里就结束了

![](https://mmbiz.qpic.cn/mmbiz_png/ibeRzWcLROATXIN7lVtQKZOtCv9Hzib6ISq3UPpvz7shMEJzagblCia6d9Njjic7kMFaADwQJbZmC1PE2fE78PBItqGJaYmUXMlKJ2U2qkrsLoE/640?wx_fmt=png&from=appmsg)

总结提效没什么问题，确实省了我很多查资料的时间

但是ai老是想做风险操作的方法这一点要注意判断，我们思考ai接入c2我们给他很大的权限，是不是风险操作就不可控了，我还是觉得人要作为最后一关把控所有风险操作，这就是本次ai实战案例分享了，只做过程分享，具体情况因为保密不能放真实截图，非常抱歉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeRzWcLROAS6UmgdeiaC8qBSsAMaI94fJskx904lVR8ZSrL3Zua3OO6CnNQVnjbbfEfqafybl1bOic5nObXlpUVQS3oTicibCXiafq3l9qlibQS8Y/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pibfvTmETc8jWDjLturOjgAn2E1GQ9p5OBYEbceMkp44Ia0ibgjh1js1kLpibIaK7gM6icibgazcb5up3q1Yn0SG8xg/0?wx_fmt=png)

水刃安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pibfvTmETc8jWDjLturOjgAn2E1GQ9p5OBYEbceMkp44Ia0ibgjh1js1kLpibIaK7gM6icibgazcb5up3q1Yn0SG8xg/0?wx_fmt=png)

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