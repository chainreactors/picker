---
title: e0e1-wx重构gui大更新
url: https://mp.weixin.qq.com/s/we-HFC7-HSiMESIvvZQtvw
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:59:23.882437
---

# e0e1-wx重构gui大更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3zcPYCnV3ShKZoENowqL8icM2abfIyRCE61XQh04ddn44ibf1VwFFTaNu95wNS2H7GshGjnCvicahoybLyAZQX2TrndKhmFVibWuCGZ7HFgntqo/0?wx_fmt=jpeg)

# e0e1-wx重构gui大更新

原创

深潜sec安全团队
深潜sec安全团队

深潜sec安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 免责声明

免责声明：文中所有涉及的内容均不针对任何厂商或个人，同时由于传播、利用文中所发布的技术或工具造成的任何直接或者间接的后果及损失，均由使用者本人承担。

关注公众号，输入“学习交流”加入交流群

觉得不错的话，可以多点赞、分享、关注

因为很久一段时间，关于比赛和一些考试，所以没有更新，现在微信4也出来这么久了，现在也参考了First的功能点，直接重构了e0e1-wx，直接采取gui的形式了，不使用cli形式了。

> 下载地址：https://github.com/eeeeeeeeee-code/e0e1-wx

首先是可以自动检测小程序存活形成卡片，会记录小程序的源代码加密包，包括分包也会记录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3Sjuefianl2Wj5k2ZU9MEvIDg7pZgtq0DFD4andrZ5yrsXkV5pIYoXDeiaVx6DSdEpovVmZFUXm1KHqlzZLokJBMicvicavpD0AwJZs/640?wx_fmt=png&from=appmsg "null")

功能一：自动化反编译源代码

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SglRt6B8Mt2kJxibtcvNJQGDatFeyzBZIwhJrniaXMYYWXvLjiaXYDQTFnSn2VrR5bohdCgMl6GCRV2gia3mGiaUGpEQpBqHNwHAmmE/640?wx_fmt=png&from=appmsg "null")

功能二：正则匹配

可以自动化正则匹配，且双击对应的内容，可以直接跳到对应的字段

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3SgiaMPFAGby4ntpR7VFMrQE1Pa3AlJCtjebRTicnkLb7hnaFFqHsMMlBFD29ZLmkQ23kBtbX9lVCgYYia2BNz6XXWadgWCuR1IibJ0/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SiaseYESk3ibqrRrsbfSXXicpPVtiaygC3iabGH6ar0u7NZHwPvrgCdBqZBdoPic0cyMP1nEhkBwk3piciaNIH2CG58Kf6xd3gUCTnibt48/640?wx_fmt=png&from=appmsg "null")

可以通过正则规则来配置正则

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3Sjnz7f1pjyZsE4seCmBsybaDCia2CcYdmT7HSwd1kTJibdjC2icGbT9BmOhQndxibBGS1ws9iaFmV2HPBdibo33b4rvVOlz0iaDdH41u4/640?wx_fmt=png&from=appmsg "null")

功能3：代码优化

开启优化代码，可以在后台试试优化，小程序反编译出来的代码

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SiaXFFqzIIw2ZX2uwL7G9U32EXOssTyEYTFEsXgkHicoM8W0b4Gic5h1VXGXOwGckOqcg5Sv5191gGtkRUkkBjtNNKsbpqUChepsk/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SiaXKjroS4RFjRT2z35gQDsEnpXRnbUOhMGJLZsqKtJxjjDficR0HUWCTmGsZKgSANwiaCQMW2ic4uGF1fTpdscKULS8icd6QeVMCUA/640?wx_fmt=png&from=appmsg "null")

功能4：devtools\_cdp功能

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3Sgc4GibhyOtUmEjzibqdKYLhBmsre6N1tAAVVaxvKgqplAxK0OYYw26ByiciazibZl1licuAFB0KWwp9GBKS9ficEeRTw1tWOrD0IiaX7I/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3SgugyYiajiaFSVACc1CjweOYeziaibuIvul53ibmXtaEDacfzB8orQZpLXEfq1mnUKZHCp3UmV7OVwMEujmDMyR9gypDcOibnSg8uZdY/640?wx_fmt=png&from=appmsg "null")

功能5：路由功能

可以直接跳转到对应的路径上面

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SiaaNuvJv2hJKf2D9CJwX1KDac1mneFNIAwj61LpJz3NdwmU5TYWOAtMA0Q6KPpIeNT6QgSeMM9Tvyehh7pCs6RaKLrCXu7WPbg/640?wx_fmt=png&from=appmsg)

功能6：云函数功能

可以进行静态扫描，双击对应的云函数，可以选择调用对应的云函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3ShS9esib88ibj6NQbLMEHj2qjUsT8TdaibJ6tSb7icra1ms18cOmJgMVAgl7KiccNrP86s8ZgTK2nWrGKEzLSaic1dgfPHz5ibN3icVeIU/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SiaBjXJzkNliaTOcuGiamhbiamzUKn4ZzaRlQScaPZ7nujwklreuY8X9CibsoyretdbiaGibh0gs3rEGtLiaatx9Z1FCheuupwSv9cnGIs/640?wx_fmt=png&from=appmsg "null")

功能7：加密解密功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3SjY9b7oZRQTbSSlbLNLhLmE3y4Zx802sXibJ1jC6XqyVU8nJ9D0L4mIQ3kKCXWK2yBTEy3zlJDbhjmsX9G16z7k57lthYIplXxg/640?wx_fmt=png&from=appmsg "null")

### References

`[1]`: *https://github.com/eeeeeeeeee-code/e0e1-wx*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/bfMXBp6Qpdyx3ibsfYx4KAb6ZkRcGUwsl5NZRx1O9nvAwT60Fl6WjldPszmZKicF50WfVsyV1LNqVsggPsJdXjCA/0?wx_fmt=png)

深潜sec安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/bfMXBp6Qpdyx3ibsfYx4KAb6ZkRcGUwsl5NZRx1O9nvAwT60Fl6WjldPszmZKicF50WfVsyV1LNqVsggPsJdXjCA/0?wx_fmt=png)

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