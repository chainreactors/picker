---
title: 雷神众测漏洞周报2026.9.7-2026.9.13
url: https://mp.weixin.qq.com/s/PzQm7pYMyOaTKL6Fzh9vnQ
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:57:12.050812
---

# 雷神众测漏洞周报2026.9.7-2026.9.13

# 雷神众测漏洞周报2026.9.7-2026.9.13

原创

雷神众测
雷神众测

雷神众测

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

***摘要***

以下内容，均摘自于互联网，由于传播，利用此文所提供的信息而造成的任何直接或间接的后果和损失，均由使用者本人负责，雷神众测以及文章作者不承担任何责任。

雷神众测拥有该文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的副本，包括版权声明等全部内容。声明雷神众测允许，不得任意修改或增减此文章内容，不得以任何方式将其用于商业目的。

***目录***

**1.Google Chrome代码执行漏洞**

**2.D-Link DWR-M961命令注入漏洞**

**3.DELL Power Protect Cyber Recovery身份验证不当漏洞**

**4.Google Chrome信息泄露漏洞**

***漏洞详情***

**1.Google Chrome代码执行漏洞**

漏洞介绍：

Google Chrome是由谷歌公司开发的网页浏览器。

漏洞危害：

Google Chrome存在代码执行漏洞，该漏洞源于Aura组件在处理HTML页面时对对象生命周期的错误管理，导致内存错误引用。攻击者可利用该漏洞通过精心构造的HTML页面在沙箱外执行任意代码。

漏洞编号：

CVE-2026-79290

影响范围：

Google Chrome <152.0.7977.65

修复方案：

及时测试并升级到最新版本或升级版本

来源：CNVD

**2.D-Link DWR-M961命令注入漏洞**

漏洞介绍：

D-Link DWR-M961是友讯（D-Link）推出的一款4GLTEAC1200双频无线路由器。

漏洞危害：

D-Link DWR-M961存在命令注入漏洞，该漏洞源于/boafrm/formTracerouteDialogicRun接口未过滤host和ipVer字段中的命令分隔符。攻击者可利用该漏洞在未认证状态下注入恶意命令，并以root权限执行。

漏洞编号：

CVE-2026-71947

影响范围：

D-Link DWR-M961 <1.1.5\_C1\_202607071108

修复方案：

及时测试并升级到最新版本或升级版本

来源：CNVD

**3.DELL Power Protect Cyber Recovery身份验证不当漏洞**

漏洞介绍：

DELL Power Protect Cyber Recovery是戴尔科技集团推出的一款‌数据保护与网络恢复解决方案。

漏洞危害：

DELL Power Protect Cyber Recovery存在身份验证不当漏洞，该漏洞源于身份验证不当，攻击者可利用该漏洞通过远程访问进行未授权访问。

漏洞编号：

CVE-2026-79938

影响范围：

DELL PowerProtect Cyber Recovery <20.3

修复方案：

及时测试并升级到最新版本或升级版本

来源：CNVD

**4.Google Chrome信息泄露漏洞**

漏洞介绍：

Google Chrome是由谷歌公司开发的网页浏览器。

漏洞危害：

Google Chrome存在信息泄露漏洞，该漏洞源于CSS处理过程中未能正确处理特定样式数据，导致敏感信息被意外暴露，攻击者可利用该漏洞通过精心构造的HTML页面获取用户敏感信息。

漏洞编号：

CVE-2026-79291

影响范围：

Google Chrome <152.0.7977.65

修复方案：

及时测试并升级到最新版本或升级版本

来源：CNVD

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V2X9n7vzLP0kSjAg48gYqOuc84iaialYgD6omNO1jEV4MUxNlXOL6t1DEmiby1TOItnw2KWpTOyibZe3TAU1unFx1oANTs45NoAicoU6pTicKyMQ4/640?wx_fmt=jpeg&from=appmsg)

专注渗透测试技术

全球最新网络攻击技术

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/V2X9n7vzLP0hknZncYB6v1s9kIRF3icf49f1MT1hMkwm355CZmabiaA0icuNJxE41RyeRlibhGNh0ROYeRqyW2a60EhfaQKCqgnXuJxiaeV1DrHM/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JXR4T1FPu3xWeia88A3vf9jricoWSZL9S5lgnSdQiaibu0xaMXwojMqj62dlEG7DNkrNAbMu6quah2YLQ/0?wx_fmt=png)

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