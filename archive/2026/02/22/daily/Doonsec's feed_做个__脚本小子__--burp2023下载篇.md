---
title: 做个\"脚本小子\"--burp2023下载篇
url: https://mp.weixin.qq.com/s/lCPk5VPugRf4z3XX3UhVvw
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:16:21.670203
---

# 做个\"脚本小子\"--burp2023下载篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KvrEnQiahoiaBQEpuzNScUAWPRB7NaUM4IiclhHKiaPwESPbOubYZWH3mGAhlgSO0f8XhyZu0Uiaouic19xsxObzlUaJDOvlPbrJfYd4KSphBaYj4/0?wx_fmt=jpeg)

# 做个"脚本小子"--burp2023下载篇

原创

lawliet
lawliet

kingman安全

![]()

在小说阅读器中沉浸阅读

声明:

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。同时所有相关行为均已取得授权，未经作者同意禁止转载

# 前言

用来用去我还是喜欢23版的burp，首先是界面，不像远古版本的丑到爆

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaA06R8r0Dj0qlcTibRwhJ5m2dep1aicgJbzXOoatOme92ou4oKakK2yniaxbackFIWjIV0TcyYoCIGVKVjJhEHjeDWKQ5XzopqKzM/640?wx_fmt=png&from=appmsg)

2023 全年burp更新得无比勤劳，虽然往后的版本激活方式从没改变，但就稳定性来说，经常用就知道，bug都不知道从哪来的，明明我也就用proxy，intruder，repeater这几个，其他是压根不用看的，但就是莫名其妙的使用错误。

# 安装步骤

一句话就是复制粘贴

当然前提你需要保证自己有java

推荐是安装java≥17的版本

官网随便挑

```
https://www.oracle.com/java/technologies/downloads/
```

双击BurpLoaderKeygen.jar

![](https://mmbiz.qpic.cn/mmbiz_png/KvrEnQiahoiaD0icwljalXHodPXBk2FrzzlQO82Stxdy1apNzS3gIf46EdabiaxXQMibKdGpBxp8Vvrib43HR5Sltiagj3n9sfOfrjWUeiaeicGYhASo/640?wx_fmt=png&from=appmsg)

点击run启动

![图形用户界面, 文本, 应用程序, 电子邮件  <p>AI 生成的内容可能不正确。" wxw-img" data-ratio="0.6130030959752322" data-type="png" data-w="969" height="339" width="554" data-imgfileid="100000298" data-aistatus="1"></section></p> <section data-layout-id=](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KvrEnQiahoiaDwMRz8v8WMJ3JH55wBzTHL70fZibRZd5y8ibvGre1GABGOl7oISsATibH59EI3bzI7toSpyibySRfl4WJbhOVOWdCicY2kodbT8Fgs/640?wx_fmt=jpeg&from=appmsg)

下一步

![图形用户界面, 文本, 应用程序, 电子邮件  <p>AI 生成的内容可能不正确。" wxw-img" data-ratio="0.8835051546391752" data-type="png" data-w="970" height="490" width="554" data-imgfileid="100000299" data-aistatus="1"></section></p> <section data-layout-id=](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KvrEnQiahoiaBhg45rlWEIlaH6lDypst2c2ulLfrQayYA8rZkGCIVxTYwfC6iccOSic1u0CdPgUnE5nwib2msb48p8jXZY3uEmkf36ERZJmnbWq8/640?wx_fmt=jpeg&from=appmsg)复制粘贴，然后下一步

![图形用户界面, 应用程序  <p>AI 生成的内容可能不正确。" wxw-img" data-ratio="0.3987603305785124" data-type="png" data-w="968" height="221" width="553" data-imgfileid="100000297" data-aistatus="1"></section></p> <section data-layout-id=](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KvrEnQiahoiaCh3b9J5UXn97aFBrDKDGBBcZ0hPefdtnsLJWzUosTZBdSKx3LnTZibhh0HHCq9Gvfr7yITRicVJY02GxNyPWHo7XNGZj7Xiay4ibQ/640?wx_fmt=jpeg&from=appmsg)点击手动激活

![图形用户界面, 文本, 应用程序, 电子邮件  <p>AI 生成的内容可能不正确。" wxw-img" data-ratio="0.8649484536082475" data-type="png" data-w="970" height="479" width="554" data-imgfileid="100000296" data-aistatus="1"></section></p> <section data-layout-id=](https://mmbiz.qpic.cn/mmbiz_jpg/KvrEnQiahoiaDr9NMYcaOeHAJRIcz3gxD54hx8skibuJKVHkFKypTGY5ibqYSuWFqucItcPPlxX4ABEeicMt1Rs046dwxTOickO2f8U5TWIKr2N4M/640?wx_fmt=jpeg&from=appmsg)粘过去，又粘回来

![图片包含 日历  <p>AI 生成的内容可能不正确。" wxw-img" data-ratio="0.35810113519091846" data-type="png" data-w="969" height="198" width="554" data-imgfileid="100000300" data-aistatus="1"></section></p> <section data-layout-id=](https://mmbiz.qpic.cn/mmbiz_jpg/KvrEnQiahoiaBlMQQ2uc5icrVK5OeCxYKBckpQZrFJv4EOy4x3FLPGIMYM1vphf4FiaApicUIGnWc4kn6YXrGXTvLSUCl8Ge0WkaesfnMI6Tb1t8/640?wx_fmt=jpeg&from=appmsg)好了，完成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaBCCXUZwKChibDQezQ8dZX9MNibM52Zc9j3MBFup1JzVuYoZSjhB1yRyWTQIUfEUhdiaPzvyiboh6RicAWibYu6vcxH9X9wRU5xxvk2s/640?wx_fmt=png&from=appmsg)

下次直接双击bat即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaAnic9XiaqaYCgWQoc8ATD5KxPt9S5yeFFMtibafyAvRdzwiaAwU1ulA26icfYArAGbhNiaoCviafKuNG2I3BDQTxULm3r6icNSefunutw/640?wx_fmt=png&from=appmsg)

获取

公众号回复burp2023获取软件

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

kingman安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

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