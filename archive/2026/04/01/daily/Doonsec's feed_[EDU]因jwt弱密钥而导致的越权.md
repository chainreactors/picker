---
title: [EDU]因jwt弱密钥而导致的越权
url: https://mp.weixin.qq.com/s/6IluTEuilr51g_5h8CNkMA
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:26:26.930498
---

# [EDU]因jwt弱密钥而导致的越权

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbBcibVekOYQMKxR6B7iaWXdkFXtMjMNibR7w607rg7Jiaicibdqib12uVJCYjb6lm3Vd6rAQnJqX78G97oAJ79piaC9ATYXYxiafxibAJ9oI/0?wx_fmt=jpeg)

# [EDU]因jwt弱密钥而导致的越权

原创

略懂安全的三秋
略懂安全的三秋

略懂安全的三秋

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbCEaCibzsUK7eCdLkvH9uqTj6LPKyMgibrB0Gw9jIoJibMcDGk8uVcuHlgibsfQo8rGxcOx25xO5Yf9gqm12ZcquRib53FP1pwQmFFI/640?wx_fmt=jpeg&from=appmsg)

开局二维码起手。

这里先扫个二维码![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_14@2x.png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbB4su6bBtUKIxh9ZrHcydGUAAdIxJ6IddR5437P9YcggLoUQz1q3MHnSNv5zlecAZzE0Z0B0PD49JaV3gl9B7OI6H2GlBrdejE/640?wx_fmt=jpeg&from=appmsg)

好的，我们已经弄好注册信息了，之后进入测试

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbCsjV69Aob8icKYOgxqkOgkBAOEznQWdIB6FqRAchsIwwYXDg61LOKn3y1gakwMqcvQ9ibbHSichQibOIibh53cB213HMsjKQhSIyicU/640?wx_fmt=jpeg&from=appmsg)

这时候就要抓包了，这里要抓报名的请求包

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbCpHvcRXNOGdjIX1euiaoLic5bQo1qIAzt2axvo2xb6dy7tjYQX5GRNLDNCMW7uZeW9LqkzsgbWbaTakulsiaDyV0bWKXI1RvgAVA/640?wx_fmt=jpeg&from=appmsg)

这里可以看到使用JWT认证的，所以我们解密和爆破看看，这里使用无影

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbAW8jwyhkkZ7ibiaZt9WyNn5MVxRynyv8g3VVGVBOv58Z96ib61YvU302ATVkpiaFGBZZ7tnr9fMyc3xtFuNtOyDJwysSr0kHNhoz0/640?wx_fmt=jpeg&from=appmsg)

爆破出来了密钥，我们可以改ID，在编码放到请求包中

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbC21jrwwpBaMDb9XatYqv7AGGfgJdI6SOwZEn8KHCTPHQrOphwj5EDfnic6vXNqQCHX5p0e5LjDPzfic7hVKM3oobGqZibKBu9d6M/640?wx_fmt=jpeg&from=appmsg)

这样就得到了别人的身份信息

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbBbrNwsIJ5x2hfpUicvXNsrQAOQicAuMUx2eY4pMILmCkBuHkU0IJyXyaKxGV3jJ9Ys9yV0m1V71axaQPicWaMW9PLMSpInJoqqK0/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbCwAYTiclpRB4d8UMS5G0NXicGflmaaXtNoDJ57elS5DgjA8ZJZFeZDibBVbueHY8MicUeUaVtzibgSIWCzy7mZDg4u2csb5UdBqNQI/640?wx_fmt=jpeg)

这里来的下一个小程序，是一个校友会

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbDXaK5KKoYibNAJvjhHaKd4jMQvcUwdcTynzke38yqrZ2Us2GwrEytGzKPKwAHfJvJKySG4jyqjuPHBQ0kNFMM7yXrKq22H245M/640?wx_fmt=jpeg)

点击头像并抓包

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbBgG0O35dNl1mzXC9boibpHsTuYI72rOqB0rZdqfZBIaPvkQkfxgfkFicf8bwLq8lpibGP51qJ7ahH0N9vbWeDqRmZby4icfX28x6I/640?wx_fmt=jpeg&from=appmsg)

这里有别人的一些信息和openid

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbCnnVCrqu2poY9KsFYXIWZUOOFTxRD3ulCdS6phY7tibXofwgKhOlMvS6JTRVgicicJrtvNickyOZJWZeT8uNEyYEYG9CXqPbKLOiaQ/640?wx_fmt=jpeg)

这里我们进入学籍认证

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbAqUXxZTXbicIpkWbVscWM9LhF9ksqyG3gegehdOLINibWj6yjw4Q6euOicYOl0eibKKYcHHWwtvILb1uzcm8tELLe3Mnhao77mvNU/640?wx_fmt=jpeg)

抓包并认证

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Qzel5kQIPbB5VhxP06eKo5TQoteqmOjgNguSKRcDKETwsHA4nDkoOIibPID0nyzlYcjj6Vicic3eowSCrnZkibhphh7L34icLmXUhkJKdV6jEq3k/640?wx_fmt=jpeg&from=appmsg)

会得到以上请求包，可他只会返回我们的信息，这里构造参数

![](https://mmbiz.qpic.cn/mmbiz_jpg/Qzel5kQIPbBqxm7sOohegj1f4iayfn0ToaCibtfBt7XFDTkWs83p8Iv2gmlSCQonrThtAd6SZ0ibLBYeVPDt9AJyL4I8AQxRky1vfuk7bewuzA/640?wx_fmt=jpeg&from=appmsg)

就可以得到全部的待审核人员的信息。

文章来自作者日常积累，未经许可严禁转载，转载需联系本人。文中内容仅限学习交流，严禁用于商业及非法用途，涉及网络安全相关未经授权不得测试，违规使用后果自负，与作者及本文无关 。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCLibpoeKyUIrykBCCd4Ix1Q2SVIyIsc7IGsL6y2kJktXuMpEpkOprEoL5TVjNdLBTeiaVESIo318WKeepXDXS0sfibQPxG3maGhU/0?wx_fmt=png)

略懂安全的三秋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Qzel5kQIPbCLibpoeKyUIrykBCCd4Ix1Q2SVIyIsc7IGsL6y2kJktXuMpEpkOprEoL5TVjNdLBTeiaVESIo318WKeepXDXS0sfibQPxG3maGhU/0?wx_fmt=png)

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