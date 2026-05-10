---
title: 【SRC实战】985证书站实战案例，领证
url: https://mp.weixin.qq.com/s/w0Cwt_t0Tty8LCjxlMjMeg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:35:56.031108
---

# 【SRC实战】985证书站实战案例，领证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qghiaf9NMibp0egOtvHzTCZZN1GE4JQlhsMYOsyt60OsFPia5Hicia9LRohezmsKrscarhubFicrRblXNWZVwEKlTic7Q/0?wx_fmt=jpeg)

# 【SRC实战】985证书站实战案例，领证

原创

渗透测试安全日记
渗透测试安全日记

渗透测试安全日记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息、工具等资源而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任!

01 背景

分享一起985证书站实战案例，通过循序渐进的资产收集排查方法，挖到了漏洞，拿下证书。

通过此次的案例分享，给各位师傅打打鸡血，拿下985的证书站没有想象中那么难。具体过程见实战！

号外号外，免费的睿鉴安全知识库上线了。点击下发链接，福利直达！！

安全知识模块，主要放一些实战的案例，目前已更新五期内容，上新企业SRC专栏后续会持续更新。主要内容如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4deQYJ2dvHVt7hG5h2eJicnIrEwbqTiaFnuxLqx233m6HraTIS84epWKa2TXzRfECAzMykqTXpfFO5SiatCO9ZKkOvU8EVIxELnDoE/640?wx_fmt=png&from=appmsg)

资源中心模块，主要会放一些安全工具，给各位师傅提供一站式下载的渠道，目前已上线20+款工具，主要工具如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4de7hPL6uxWaRAery8Ae9Hb9rzChKPHibBpwD6yg7iaHRwggo1Hw5Bo0LT8eG37dBqYEsajDy1fzTib5iaXYAvSO428zICEjErNAD9c/640?wx_fmt=png&from=appmsg)

02 实战过程

在挖这个985站点的时候，一开始没有想象中那么顺利，因为打的人太多了，该出的证书洞也差不多挖完了，这个985的站点，作者反反复复摸了很多次。

说实话，通过这次的挖掘，作者再一次感受到，找别人找不到资产的重要性，看了这个漏洞，你会发现其实漏洞不难，难得是找资产。

开局一登录框，可以看到有一个注册和绑定账号功能，通过信息收集到的账号进行绑定。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4dfxkHpcTXq0GicHhGHr0QJdrhDOsRa1MCEGuK5E33zjm5Zr5C6b2vSribSbUZmOmoC0QzhYg89FGzofS8cNhzzicga3kmbKgvXRBE/640?wx_fmt=png&from=appmsg)

输完账号和随意输入的初始密码后，点击下一步，会进入接收验证码功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4ddnuUpo9oobiacjfoerRp0Y5nYrkDzzvGBZWB5ZHaec6JAfYDoictnIzlXKs41YOPNj17hCAb3AZ3gumfesLwOLTavWOcerCPNac/640?wx_fmt=png&from=appmsg)

触发短信验证码，在输入框中输入1111，点击下一步，使用burp抓下验证码校验的包。发送至intruder模块爆破。

可以看到验证码不对的时候会提示不正确，所有的提示都一样。后端并未对验证码的校验次数进行上限设置，可以进行爆破。

![](https://mmbiz.qpic.cn/mmbiz_png/Euxpicz6k4ddhWcNKMtcia6DJMWpWhrqH47pFzy93S8a1QsQDs1micffcth5RRGz10Q0TTPD6kFvibNFeT5mrT1ug6M4zfXGpcQ6dkTahTeibHV4/640?wx_fmt=png&from=appmsg)

最终爆破出正确的验证码时提示手机号不存在。因为是作者本人账号，确实在系统中不存在。

![](https://mmbiz.qpic.cn/mmbiz_png/Euxpicz6k4dc5p8RR7UdaRbia7x4kIoFfgxWLhh2YPZVLR1jYqrRiatb14TaSsnAYfSXKobIjcS0iaJVLEJavmv67z2mgnCFruo5y8Aeqm22OUA/640?wx_fmt=png&from=appmsg)

可以看到手机上收到的验证码跟爆破出来的是一致的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4dcib3eavVr9iaPpYOiaWfCQXBxZ826uXMfttnnUCJ2iaMoNAv9wvnVT7hs47EkdOjicoMQOV7zib32GbUkQGlvFSSZ0qF7OLj6qoFAwc/640?wx_fmt=png&from=appmsg)

点到为止，提交SRC。拿下证书。

往期好文

[网络安全人员的金牌证书：为你铺就高薪职业之路](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484847&idx=1&sn=62fefecfbed336486f417e60bdf5fdd2&scene=21#wechat_redirect)

[【SRC实战】一文玩转Minio存储桶漏洞挖掘](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247486079&idx=1&sn=ffb3843bb61c5a75a3da2e9869b932cd&scene=21#wechat_redirect)

[【SRC实战】IOT漏洞挖掘实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247486150&idx=1&sn=d0cf99fbe2508b3625f4f9168491b3b7&scene=21#wechat_redirect)

[【SRC实战】实名验证接口滥用漏洞](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247486026&idx=1&sn=20ed1a66f58940fa83cc88252e740ddf&scene=21#wechat_redirect)

[【SRC实战】支付漏洞实战案例](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247486000&idx=1&sn=61c32e9a555e7aa6e5a53f96cb895308&scene=21#wechat_redirect)

[【SRC实战】通过报错拿下高危漏洞](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247486158&idx=1&sn=70a37b791039d75b287d5f150072e627&scene=21#wechat_redirect)

[【SRC实战】简单FUZZ拿下高危漏洞](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485405&idx=1&sn=669a4286abd1103b050059efdb3da268&scene=21#wechat_redirect)

[【SRC实战】RedirectUrl劫持实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485901&idx=1&sn=dc9931b8afe21cca270f80e71fda1e20&scene=21#wechat_redirect)

[AI大模型“越狱”实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485551&idx=1&sn=5e2accbd716bf890c37a9fb7be4c06b7&scene=21#wechat_redirect)

[企业 SRC 低投入，高收益漏洞总结](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485784&idx=1&sn=d53f6491bccec7fdcd8eca356c04f0d8&scene=21#wechat_redirect)

[【SRC实战】任意用户密码重置实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485484&idx=1&sn=e3ccb64ef54194ae4216c1d43606b651&scene=21#wechat_redirect)

[【SRC实战】记一次越权测试实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485379&idx=1&sn=37985dd7e56a66b2d023548eabd845ea&scene=21#wechat_redirect)

[免密登录某后台管理系统实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485024&idx=1&sn=71c596dd36800993e18f1f05b9d37547&scene=21#wechat_redirect)

[安服人应急“薅洞”指南](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485381&idx=1&sn=d0195d62adf45f6d614c785886d04e92&scene=21#wechat_redirect)

[推荐一款资产筛选工具](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484744&idx=1&sn=7d205189f4a95c2a0cce1b6e99014c64&scene=21#wechat_redirect)

[【SRC实战】SRC常用的信息收集方法TOP 10](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485754&idx=1&sn=da396a3501b1346d7becdc4201299a2a&scene=21#wechat_redirect)

[【SRC实战】一次“链式”渗透，从站点A打到站点B](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484164&idx=1&sn=9c2db3fc19000f60785499f2c4ad1f6f&scene=21#wechat_redirect)

[用户账号接管实战，洞穿开发者逻辑](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247483991&idx=1&sn=c1f6e65233cf18ade53b6e566fa4b3af&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/qghiaf9NMibp2kbLoABFUAuAETmd9qZeaeqrnHLRAfCnibBuK9tfeENbn9wuXVcJC5TLaTtJt6tibLMfILKCiaibMMiaw/0?wx_fmt=png)

渗透测试安全日记

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/qghiaf9NMibp2kbLoABFUAuAETmd9qZeaeqrnHLRAfCnibBuK9tfeENbn9wuXVcJC5TLaTtJt6tibLMfILKCiaibMMiaw/0?wx_fmt=png)

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