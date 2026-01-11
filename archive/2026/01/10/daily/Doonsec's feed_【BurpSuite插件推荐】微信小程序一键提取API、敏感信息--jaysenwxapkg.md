---
title: 【BurpSuite插件推荐】微信小程序一键提取API、敏感信息--jaysenwxapkg
url: https://mp.weixin.qq.com/s/6Fm-7zKQJbe_1mnY-5GqOA
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:38:51.307530
---

# 【BurpSuite插件推荐】微信小程序一键提取API、敏感信息--jaysenwxapkg

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iawfFicgO3G9fezbrebEJU7x7czVE9lic0YCJNHk8ibROcKHByqJvhcZlKQ/0?wx_fmt=jpeg)

# 【BurpSuite插件推荐】微信小程序一键提取API、敏感信息--jaysenwxapkg

秋刀鱼

塔罗安全学苑

![]()

在小说阅读器中沉浸阅读

# 0x00 插件介绍

以前老版本的微信很多师傅都登不上了，目前市面上也好像没有针对微信新版本的小程序反编译解包并提取敏感信息的插件，**jaysenwxapkg** 就是一款基于burp api 2025.8开发的插件

**项目地址：**Jaysen13/jaysenwxapkg： 自动解包微信小程序并提取敏感信息和api接口

觉得好用的师傅辛苦点点start✨

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iaDiahzFSF7D91dV1EXIlyfQy0GibcMlsqvEiaDaXemclxB5MCv45f89hZQ/640?wx_fmt=png&from=appmsg)

## 0x01 插件使用

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5ianPXH8CG1wRqWZGVEqAuDuc61fnIEiaJgJySUSq9LbicqXMAw5JOUHAeA/640?wx_fmt=png&from=appmsg)

image-20251229103047907

访问项目链接，下载jar包，然后直接导入jar包即可

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iaoJG91syRribjHGZ3kTt8AcTPdQmIVJyNMZrg7iaPcMFGK1pytWIpAxEQ/640?wx_fmt=png&from=appmsg)

image-20251229103133824

加载成功如上所示

可以查看我目前是微信最新版本：4.1.6.14

找到微信的小程序包生成路径，默认是

```
C:\Users\你的用户名\AppData\Roaming\Tencent\xwechat\radium\Applet\packages\
```

找不到的可以全局findsomething搜索一下packages

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iab7uib12icsRS7naIm3DeiarcGga81EQL0icfnyS2PPV7zlibw2vHiaRIJWRg/640?wx_fmt=png&from=appmsg)

image-20251229093124896

以下图是一个小程序生成的主包和子包

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iartRweg19h31DDgW6z8myaO2Kp8ic2ldolczoU4f3WR2ab307zudwvRg/640?wx_fmt=png&from=appmsg)

image-20251229093139954

这里会有很多包，每一个包代表一个小程序，部分包还存在多个wxapkg文件，由于不知道哪个包是哪个小程序，先全部删除

打开需要提取信息的小程序后，在插件选择小程序的文件

默认首先打开以下路径：

```
C:\Users\你的用户名\AppData\Roaming\Tencent\xwechat\radium\Applet\packages\
```

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iaHYwnB58ibWRSKlbia5XzqlJBGp9oIes2dDXCibyHiagsTBiaFvbg1otkquA/640?wx_fmt=png&from=appmsg)

image-20251229093308773

点击【批量解析所有wxapkg包】即可解密该小程序的所有主包和子包，并提取信息

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iaBhQCG1A8xSKOg6HGc09ofiacSBCJ0afYjv1nQQVBQHgcvCXxNliaBjug/640?wx_fmt=png&from=appmsg)

image-20260110154754166

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iartRweg19h31DDgW6z8myaO2Kp8ic2ldolczoU4f3WR2ab307zudwvRg/640?wx_fmt=png&from=appmsg)

image-20251229103624954

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iazyUekQpFYsU6Rr2TNyEbkia44BWxB3toPvPlDoMQDQwU5gHee54cg7w/640?wx_fmt=png&from=appmsg)

image-20251229103747459

点击\*\*【打开文件浏览器】\*\*

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iaUwduODGc2ypUP4pP8ODDic2N5BhLBecUleY4jhbed6zEJSXjQ12VpSg/640?wx_fmt=png&from=appmsg)

image-20260110154954334

![](https://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHKmwwNb5toztAreb2B2QO5iaWMWOalPFzibXOBqAtjkaJvEC6oz0YJbzmLa2KyrUhzIF0q4IbVQaP8g/640?wx_fmt=png&from=appmsg)

image-20260110155041313

可以直接全局搜索信息，已便快速定位真实的敏感信息泄露位置，不需要再去缓存处用编译器打开

## 0x02 插件配置示例

**敏感信息正则示例**

```
手机号:1[3-9]\d{9}
车牌:^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$
AppSecret 泄露:(?i)\b\w*secret\b
IP地址:^(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$
微信小程序 session_key 泄露:(?i)\bsession_key\b
身份证号:\b\d{17}([0-9]|X|x)\b
邮箱地址:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}
```

**API接口提取正则示例**

```
(?:"|')(((?:[a-zA-Z]{1,10}://|//)[^"'/]{1,}\.([a-zA-Z]{2,})[^"']{0,})|((?:/|\.\./|\./)[^"'><,;| *()(%%$^/\\\[\]][^"'><,;|()]{1,})|([a-zA-Z0-9_\-/]{1,}/[a-zA-Z0-9_\-/]{1,}\.(?:[a-zA-Z]{1,4}|action)(?:[\?|/][^"|']{0,}|))|([a-zA-Z0-9_\-]{1,}\.(?:php|asp|aspx|jsp|json|action|html|js|txt|xml)(?:\?[^"|']{0,}|)))(?:"|')
```

**前缀/后缀黑名单示例**

* 前缀黑名单：`/pages/,/components/,/static/,/uni_modules/,uview-ui/`
* 后缀黑名单：`jpg,gif,svg,wxss,wxml,png,js,jpeg`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHJLT0krIpLicq1SDppPicWtD9WT2vqMxfSPoDTel0zk7r49TmrRBTiaBickOiaUTrjNdD4YoIzFibCLVu1g/0?wx_fmt=png)

塔罗安全学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uhzNxvrVaHJLT0krIpLicq1SDppPicWtD9WT2vqMxfSPoDTel0zk7r49TmrRBTiaBickOiaUTrjNdD4YoIzFibCLVu1g/0?wx_fmt=png)

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