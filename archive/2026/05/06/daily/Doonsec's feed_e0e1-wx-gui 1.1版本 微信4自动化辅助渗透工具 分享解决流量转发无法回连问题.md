---
title: e0e1-wx-gui 1.1版本 微信4自动化辅助渗透工具 分享解决流量转发无法回连问题
url: https://mp.weixin.qq.com/s/0Soj0Rnxgeo0aqc_a0PZrw
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:31:11.556869
---

# e0e1-wx-gui 1.1版本 微信4自动化辅助渗透工具 分享解决流量转发无法回连问题

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3zcPYCnV3Shq4AMxFdpQkN4zL73baHQcVuTDKjxNfbCIEbP4wCs8aibou7qmSGtys9icyFTNyJPI7IFZctngYepZMrY5eAYFRZ11KWC1blrSM/0?wx_fmt=jpeg)

# e0e1-wx-gui 1.1版本 微信4自动化辅助渗透工具 分享解决流量转发无法回连问题

原创

深潜sec安全团队
深潜sec安全团队

深潜sec安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明：文中所有涉及的内容均不针对任何厂商或个人，同时由于传播、利用文中所发布的技术或工具造成的任何直接或者间接的后果及损失，均由使用者本人承担。

关注公众号，输入“学习交流”加入交流群

觉得不错的话，可以多点赞、分享、关注

```
e0e1-wx-gui 1.1 更新日志
1.关于反编译html等文件显示16进制的问题2.关于高版本微信，小程序加密文件换位置问题的优化，同时检测3个 用户指定、低版本微信默认、高版本微信默认的文件夹链接3.添加小程序调试开关功能4.优化反编译功能，添加全局搜索附带正则搜索5.优化反编译功能，添加文件局部搜索6.优化反编译功能的代码搜索加粗功能7.添加解决关于小程序转发流量后无法回连问题
```

> 下载地址：https://github.com/eeeeeeeeee-code/e0e1-wx[1]

## 关于小程序转发流量后无法回连问题

这里以Proxifier举例子，因为工具devtools连接会走ws协议，所以会被转发，导致小程序无法回连，所以需要设立两种规则，如下

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SjljCFf8jqpD1zfH5ZBCIH7h69SHcib2wWYfEq6hjOAltWSewY0I9GsTdenLC8YVMglKWIDTwMKFkdGjLuRwYQHjNibbzG27NS1E/640?wx_fmt=png&from=appmsg "null")
新抓包配置如下，第二个你自己的抓包配置

```
应用程序：WeChatApp.exe; WechatBrowser.exe; WeChatAppEx.exe
目标主机：127.0.0.1;localhost;::1
动作：Direct
```

## 功能使用详细介绍（建议看完）

### 监控功能

程序会监控小程序的生成，并且形成卡片，并且时刻检测存活状态，包括分包也会进行检测

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SgKnPlicmeciauXjHmFBsyXYyP4qPdJxsPa29fLKOJQTVyibHk8JlFXxjyl98ZSU8FgpJbleRM201FHEnicID6kibmME3CrCTnvv9Zw/640?wx_fmt=png&from=appmsg "null")

### 小程序反编译功能

第一个按钮代表开启自动化反编译，第二个按钮是对反编译的文件进行格式化

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SgTIWco3Mz3nO5JyiaoVOLibVYQEtdEXAfftIaPqRiaw5UkowZThXblncd3DrCZlB8jyKORaN59ngVibsEf5lrxXdN293r9l49lg60/640?wx_fmt=png&from=appmsg "null")

格式优化完成的内容如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3SiaHFvUZraic9DTWhSd8SKtVmTT3EtQOUhTkxelNMHVff0GSmx1tAbC6PvgfQpwj0sCsQ2e4M3cWyxwhk5FvkKfBTPJYDTJ5BdOw/640?wx_fmt=png&from=appmsg "null")

ctrl+f可以开启文件内搜索，并且加亮输出

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3ShdYbClAYPW55QGGuJVhh7zPiapaPo9CzXUwMxLebzNiaZ1XiblWnGwMt7iaia8OtUwyibwhUbYLpXV6wbjScjRPEQAdbcibLEzuPqW4M/640?wx_fmt=png&from=appmsg "null")

自动进行正则匹配

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SgbxwHXuE9DYIYug500ibHyoTZFvXuN66gjVkIMgWB5V5UmXdLKswjgyhLUtiasTDHibBxubgdJK6cfjNxOibWtH2HNJftXEAv8cfk/640?wx_fmt=png&from=appmsg "null")

双击输出匹配结果，可以自动跳转到对应的文件内容

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3Sjh6nVGEia6MEib8oxfSjC7Jjef4Ptdu1ZSdIxGocsfSxgOLbRKLSd2cTPwvibulHM7pKzuOWaDwE8ibLXtfWhUIQ6g21TuW8zgbHA/640?wx_fmt=png&from=appmsg "null")

全局搜索，同时也支持正则，同样也可以双击跳转过去

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3Sia2qkuf4uUcPZUh7ue0e2yriaRQHbLiaSryrYC0sbSECfk3tO9Dia9moO4jAsQTKBZTQbpI5cvsqnPySHRxSgWxhYC8qjxITcZU94/640?wx_fmt=png&from=appmsg "null")

### 小程序devtools-cdp功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3ShA6ep4NvBIkiaewH6ZTicwTNSpJA5kYJiawYw3UHFvvbFficFDENIJxJNKxibBZt9BndZfqicDqicblo54vRTQBtvudSwiaAvHe5ibkttg/640?wx_fmt=png&from=appmsg "null")

点击开始调试，小程序重启一下既可回连，复制链接到浏览器里面就行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3ShAULAuuR8TPWtbnozxoh7VYXVda7KvS5q2CBQsD7lLyUN13zy3GSGvJfibKUrKWOeu8jqibpRrTPZlzhj5BNaMsHQVyJUJrPzAU/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3Sia9lsicXgxnJ5RRMJIPOUXialXIMSNQCxDMjKgJARHkBKQFrJPOXngXajahvQibb34nHBmmWsBjRH18Khx8AgYWicnOcIGv316xAos/640?wx_fmt=png&from=appmsg "null")

### 小程序路由功能

接管路由，选择对应的路由，点击打开新的页面，可以直接让小程序跳转到对应的页面中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3SheKnAT0wNs3wJLs4lIHyb4IloYUMspPqJlJsNOIibbcPoiaTerdQ9KVUJ8DLqHd4bBDhdp5UZzeAaUkq8m8licYPGV5xvHrn9SAo/640?wx_fmt=png&from=appmsg "null")

### 小程序云函数功能

可以静态扫描和动态捕获云函数，双击对应的云函数，点击手动调用，既可进行调用

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3Sjp9lPOMPv2wHqOVLgUVF4yPiaXczXsl94Ribj3z5zsEOkibzcsFm78Rib33HvhYVlrwDJc0UmvUPDR775hH1Tq4RKEWiaHKtbIB4lk/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SiaINufoqJNO9wgnsaPBhlmIec8qqYpC0BKicXZ83hyKgRo6L5kTCdw1G3KIArh34vqUiaRj3y8MsK3ibE8tn2icU2pjk28ibrvePlia4/640?wx_fmt=png&from=appmsg "null")

### 小程序调试开关

点击开始调试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3SgpXYor7c66aymJsaCSZrVMUDVLa841Rvic5mUpQrLXsTPyh4k1obEufkDO149BcYAU4XnrdVZEjCMWsFVMp6HHh6ibrnDkIJibYw/640?wx_fmt=png&from=appmsg "null")

关闭小程序，从小程序页面再次打开

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3SjDib4bPKnYeaREcpH8Ku7lFPfMial6ZUibzqgJRwNqs5ibdzmMENAQUNzibEml4TGcFFIVdujDOjRAsXO3PL0QgXSqdOksl8uiaFlvo/640?wx_fmt=png&from=appmsg "null")

既可出现vConsole

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3Sj4PDrNj7u3Rc8xmIebrDArxCRic99uV6aWuQCoyARobx17LKmZsPTIX2E0ibUBiawd9sadbe1sGfzyBFtgJBqxibXgIic4yKdENbnU/640?wx_fmt=png&from=appmsg "null")

可以通过这里关闭

![](https://mmbiz.qpic.cn/mmbiz_png/3zcPYCnV3SjM9RM1sHPXsAYr0dshBfMlGWiam1k8fliaGP6CBwibWqj2GC4E37D7h2G9ScBJGahbt11ALogCqPU5tYffEjtjqoSHcqyiapOW114/640?wx_fmt=png&from=appmsg "null")

或者这里也可以进行关闭

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3zcPYCnV3Siah0LYRWhdfbVJbrzl8Iicw7vq4T58Ribd1WHVXKF0ujJaGLvyR0knicgd9Whm7VWXhG84T7Xia9dcM19Wl2PXAxDB4QhTEZeXcFfc/640?wx_fmt=png&from=appmsg "null")

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