---
title: 为啥有些网站Chrome记不住密码
url: https://mp.weixin.qq.com/s/7ryN_8H_lSucd2y23SuDRg
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:03:29.788587
---

# 为啥有些网站Chrome记不住密码

# 为啥有些网站Chrome记不住密码

原创

hyang0
hyang0

生有可恋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

大部分记不住密码的网站都是内网 https 网站，并且它们的 https 证书报错。

比如：

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7Peiauibv1VnWLAuX9xpES9Xw5pkMvWQLGUMQnvIMzBE8UibfcrficmGLibQ1txdQrjxqx4wiaSjxGJbQC4saAKl3DM7FgkKMuJLwPXSc/640?wx_fmt=png&from=appmsg)

这种网站即使你在 chrome 密码管理中将url+账号+密码都填进去了，它还是记不住密码。打开网站时，密码框死活弹不出不来密码代填。

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PeicyGLDEz20oeHyTHic98jlGialOgtgeiaB9gnH33DERoZsHr5F5CzwNB5AEv5aj9cxeWD9I1Kl4SFw0iaTMGBiaYH8mdJQ1PrARI8Y/640?wx_fmt=png&from=appmsg)

这是因为 Chrome 会对不合法的https证书站点收紧密码管理行为。如果证书告警，八成密码代填会失效。

有没有办法解决这个问题？一般使用第三方类似 keepass 这种密码代填工具或浏览器插件来实现密码代填。

还有一个办法可以从源头解决掉这个问题，就是把应用的证书替换成 mkcert 生成的自签证书。其中 mkcert 生成的 RootCA 证书文件只用导入一次，为服务器分配的应用证书不需要在客户导入。

这需要在服务器侧替换证书，在客户端侧导入 RootCA 证书。大部分应用无法做到更换证书，比如封闭系统、安全厂商提供的硬件盒子等。

这时可以使用 nginx 实现 TLS 终止，将原 ssl 证书卸载掉。然后再重新组装由 mkcert 生成的自签证书为站点提供 ssl 加解密服务。nginx 在其中充当的是 https 跳板，此时访问代理后 https 网站，证书不再报错。

示例：

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7Pf2t7jGTT7A7CkH2vRsMficXAHDvs8cuNTkIUibpPupcnjVsibxr2fvxO47VZgLyfdLPGVTbm4jOaSWvPiblUp2GUWSJJTibacTkrP0/640?wx_fmt=png&from=appmsg)

这是一张对照图，上半部分是原始https站点，提示证书错误；下半部分是通过 nginx 代理后的站点，https 不再报错。

虽然证书是有效的，但因为是自签证书，点开地址栏的叹号还是会有一个安全提示但在地址栏不再有红色告警。并且 chrome 也能正常记住中转后的网站的账号密码。

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7Peg6qkwgGqAtickS8YWy9Pl9ZPAaErEnczHWicwlrZPBibURhsoueibef5ibf1xNkibYial6ibYeicXKGKbuAnnCQ0UQiaNyibluI519uphvM/640?wx_fmt=png&from=appmsg)

给 nginx 做了一个前端管理界面，方便在界面上操作端口映射。

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7Pduf9fqxeYO3bx5xKTocTRa6IloklI1qjApbowaVYc2y8jCIicqNM8zpVvx5ZcGklYryqsOdnG7pcbur9hEaDwNOQF7YQwM35mI/640?wx_fmt=png&from=appmsg)

原始提示词：

使用 nginx stream 在本机搭建一个代理服务器,底层命令类似:`nginx -p $PWD -c nginx\_conf/stream.conf`。访问日志存到 nginx\_logs 目录,一个端口一个日志。使用 mkcert 创建本地证书,为 http、https 应用转为使用本地的证书。使用 node 开发一个 web 应用,提供简单的密码登录。在 web 应用中可以配置 nginx stream 端口映射,并可以实现 nginx reload、restart、stop 操作。可对端口实现 enable、disable 操作。可查看某个端口的访问日志。日志中含访问时间,客户端 IP,。提供统计功能,提供 24 小时访问次数、6 小时访问次数,每分钟访问次数等统计信息。按端口进行统计,按访问者 IP 进行统计。

全文完。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

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