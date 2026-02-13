---
title: 记一次渗透色敲网站
url: https://mp.weixin.qq.com/s/LcSfd1Nhym_WquiHGygrpQ
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:14:30.230856
---

# 记一次渗透色敲网站

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xTZfvDhkzLvwBsgDibIRUAabevuspJCiaKDznbJhyqmLkYTTicdT5GXR54ZMOduzNCGCB41AFjtMWRr2tCL2FtxroCibbACiaibmzpfiauJxomwM8U/0?wx_fmt=jpeg)

# 记一次渗透色敲网站

努力学渗透ing
努力学渗透ing

努力学渗透ing

![]()

在小说阅读器中沉浸阅读

距上次更新已经一百多天了，寒假终于想起来我有一个公众号可以更新一下，刚好今天打了一个站，更一下文章（技术文笔都差，求大佬轻喷）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xTZfvDhkzLt8XLwPM1l09PMFo4Iutz1GLF1opDGTnpH88wKtJjJLHodddCgFMy3kxIqaFHCJ0SW4Ilh7iaUqN3xo5HzNHIcy4DMGQelguJ74/640?wx_fmt=jpeg)

窃取数据前台有了，先抓包看看被窃取数据被发到哪

![](https://mmbiz.qpic.cn/mmbiz_jpg/xTZfvDhkzLtWfb3UCPR6g4nkKgEsTSFRrUpS4gIzhzNl7JqupJH70jrM3dEllMTN4r1kkPEicuKDHAuhZBSg7ic6dBIFSSm38GVMwPjbTLYFs/640?wx_fmt=jpeg)

URL中带有api字段，大概率后台放在子域名中，先看看api域名用dirsearch，发现啥都没有，访问一下看看

![](https://mmbiz.qpic.cn/mmbiz_png/xTZfvDhkzLtwWBqg7HNq8LOaWKD04adfOeWib5Lc9TgXVFz8AGuBicJrMCh4ryWicicvxDiaOMTGtJIqJ128PHjUHDhIKwgsmXHibNL9gbnQtibRaw/640?wx_fmt=png&from=appmsg)

app-token是不可能去找的，主打的懒，用nmap扫一下看看ssl能不能找到后台子域名

![](https://mmbiz.qpic.cn/mmbiz_jpg/xTZfvDhkzLscR0Abgia0YMsv69l3u2hl7mmUG4ibRESqDSZDe22ZrX2h8Shh4hB1AwwHK2nvK8kQHuibvCZcySSGbjkM48yVaS7ZibvjoxfLON4/640?wx_fmt=jpeg&from=appmsg)

没扫到的话就用fofa的domain语法查询一下

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xTZfvDhkzLtIslGoZ4VsJv7kZA1hQjn53hsTYbVzo2DNhSAQmHgKfotMWibddYZZIoibvo2DnawofDyTslC9f8LJBI1tjQm2pvPfBHknPvxX0/640?wx_fmt=jpeg&from=appmsg)

触发大保底找到子域名，并且网站标题明显带有admin字段，基本上就已经找到后台了，一般扫个目录就能找到登录入口了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xTZfvDhkzLvvy9IWT3c9ryu439iceJ2V7653YpQicbWPa8deKVVfkr6QaibKqmUJLUuDNa7xBtJOwywhdic4kryDEIvdXRDJv5icpFg4fvhB24Uk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xTZfvDhkzLuz8USHAlic7BeMX96pFpcu5aibXM28eMO954ianzpXAKYPM2LyQVxXfB5wEmAQ8Ezeic2o3DGAHz66ibuOoiacEaVMOnTIicAeX0e5aw/640?wx_fmt=png&from=appmsg)

一个200响应都没有吗，按剧本来说这种站/admin就有了，那就从js入手看看吧

![](https://mmbiz.qpic.cn/mmbiz_jpg/xTZfvDhkzLug1L1WyIk3oIsePZm0IlXgkPcxiatRTFVETibIhOsyRoaM5NFpuTtz4hmp0GauRPme0p0exth6Oo7iazYVzlF7eOdug7KpxXz3lM/640?wx_fmt=jpeg&from=appmsg)

都有vue的提示了还说啥，antidebug启动！（过路由守卫这个插件蛮好用的）这样攻击面就大多了，可以直接测后台接口了

![](https://mmbiz.qpic.cn/mmbiz_jpg/xTZfvDhkzLuyOvXNd4boyRqic3GnNTEjIrF8vuO82CfWcyZ4ibW8baclXTOpXGnXicSnW7WnKmbsl8kurMpyFT0tXem6pictvRaCxELc3zsNUy4/640?wx_fmt=jpeg&from=appmsg)

用户管理处每一个用户都有个id，虽然表面来看做了鉴权，但是查询或者将id置空仍可读取数据（敏感内容打厚码）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xTZfvDhkzLt3UfxwyKosEhnoDXGibSRkg74hxIyyA06tI1ZdonFq6s4O2YtrBU0NRoiaD4vIG54AQM9S2S2EOWu6pFNkodvCHgSnF0dpiaL1Ug/640?wx_fmt=jpeg&from=appmsg)

至此任务完成，三角洲 启动！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uC3aSPibticibFCu251CaHlT8k0UcNLtTK2GicCmre4ePPxovKNe5sHvDxuZ7rDneicgvzL6xOrgJdWr3xDP7GD1O2g/0?wx_fmt=png)

努力学渗透ing

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uC3aSPibticibFCu251CaHlT8k0UcNLtTK2GicCmre4ePPxovKNe5sHvDxuZ7rDneicgvzL6xOrgJdWr3xDP7GD1O2g/0?wx_fmt=png)

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