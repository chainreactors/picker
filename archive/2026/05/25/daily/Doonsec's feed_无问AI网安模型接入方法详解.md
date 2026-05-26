---
title: 无问AI网安模型接入方法详解
url: https://mp.weixin.qq.com/s/Sst8Lfqae9zrspmBU4MzrA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:02:39.517428
---

# 无问AI网安模型接入方法详解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DupJg3UCeKLWGTgDqqicibrLibBYN00abDl5ddSSur4HKJ18CrPwSKATFBiak7WDmsAle5Nanhg4fL8nNrE8aWQ70OocAwtVB2iapHYWZXawdHac/0?wx_fmt=jpeg)

# 无问AI网安模型接入方法详解

原创

无问社区
无问社区

白帽子社区团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

自无问AI模型API服务升级后，收到了数十位用户咨询API接入问题。

在本文中将更详细讲解无问AI接入流程。本次会以当前咨询最多的Trae做演示，同时也会加上claude code的配置和使用说明。

除了通过API调用无问AI网安模型，也可以在线访问和使用，无需任何额外配置，直接即可使用。

**https://www.wwlib.cn/index.php/ai**

**如果需要更多的Tokens资源也可以前往此处了解Tokens折扣方案**

https://www.wwlib.cn/index.php/api-service/sale

1.TRAE接入指南

将无问AI接入TRAE需要先从下方链接下载并安装TRAE

https://www.trae.ai/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DupJg3UCeKJ4cZynicu9l3dYtIhWcp9pjhFfjNG2d3Rr8dic27qaGm8gpVYlAVkiaTvCJIocsWeNAPwdh30B65ytQ0bNlKr8alrP0y8x9lTuro/640?wx_fmt=png&from=appmsg)

安装后打开后需要在右下角优先进行登录，登录后即为图中的效果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DupJg3UCeKKRn1GsePnCFGBsq0Qic5L2fu8IPYxicULw2dgJ0MujbibCn2pRPHPGgxcCxgYoicFGl3ibicfepy61htiaj4BuW98ZGibU0t0skKbwx4s/640?wx_fmt=png&from=appmsg)

点击左下角的设置- > 模型 这里我选择OpenAI接口，当然也可以选择Anthropic，目前对于这两个接口都已经兼容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DupJg3UCeKLnrqkqEy7PGvoOYnCRRib15sPFwGDCvGI1dpkNGSZfXW7Loe9RHgLh5w3bUSugiadcj0qla6kE8IQjKY6KNvU7XXHkcHN6HDhvY/640?wx_fmt=png&from=appmsg)

弹出的窗口选择自定义模型，并填入模型名称与API KYE 还有接口地址

接口地址：

**https://www.wwlib.cn/index.php/v1/chat/completions**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DupJg3UCeKIaK9TFFGDRThwQt7kiadwjW9ciaLsbvzrRwD5zjGwC26BDVDt6jib6oB4bX5k9KbNj4AInZm4FW6ttkYHJxD81h9yZ16OvlElgwc/640?wx_fmt=png&from=appmsg)

右下角切换至添加的模型即可开始使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DupJg3UCeKKrzLSmJRHtU9UvqpMTibMGgt3KpowYd06zvqj7iaxVHlwKficLLaoPBe0Rq9R9sO2xZJIM6x1rSENfJvucibeQu1tHmqEhW1ZLfno/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DupJg3UCeKLNylsibibqkw5ndMXbwHubpZpFicmg2D2NSYMe4Ku5ecvjjgz3A855c61IT8pZEd2pZnF1lKiabAQNTkF4DdZdKO69lnUrTAialcy8/640?wx_fmt=png&from=appmsg)

2.Claude Code接入指南

在安装Claude code之前需要确保自己已经安装了Node.js V18.0以上的版本

![](https://mmbiz.qpic.cn/mmbiz_png/DupJg3UCeKKNt5jb5iaJ8LOSyM4VJyYCt29b0XnNFiavvcgiboIzOdYoEeadgMbeYrJoEnDCZUql84ILickd51I6hVOZibxsG9BMoszXXpHTIOkU/640?wx_fmt=png&from=appmsg)

安装方式分两种

irm https://claude.ai/install.ps1 | iex

或者

npm install -g @anthropic-ai/claude-code

打开用户目录下当前登录用户的目录，找到.claude.json

![](https://mmbiz.qpic.cn/mmbiz_png/DupJg3UCeKJZoib8OyERsvVibuMzBtSEuYq2qzrwdhtQQdT5UWmicviac6sWAd45oLNFTk8Muoic4FVISIVrPcHXy2uT1TPNDK2O8GM3kyJ8qJ5s/640?wx_fmt=png&from=appmsg)

在其中写入

"hasCompletedOnboarding": true,

![](https://mmbiz.qpic.cn/mmbiz_png/DupJg3UCeKKXDBibrHYb4GAJmticCwyBnpsGH9RpgIZITcB3tVIGxQGiaDETZEgtj1PLFDJDGdicYLn4tyKHIuyjXfv8VD3Y75mwwCiapicMgCHUM/640?wx_fmt=png&from=appmsg)

打开powershell

输入：

$env:ANTHROPIC\_BASE\_URL="https://www.wwlib.cn/index.php/"

$env:ANTHROPIC\_API\_KEY="XXXXX"

$env:ANTHROPIC\_MODEL="N1PROMAX"

需要注意，其中的ANTHROPIC\_API\_KEY需要输入自己的API KEY

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DupJg3UCeKIsCHpYW5Mxqj7EsjtXo9Xqiaxxs0ic9IhciclqWU9tP3609dZjpUxkwRqmsF3IdiacFPGCcsLbeF0ia3GEwq3ibibeAoRRibURaOVDRC8/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/DK5OZOOglM6D8CODmqVX5pENgZsribK6KXeXxbic9BOTDC2oiapGqAhbC1p11TrLTC5YfoLeFOUdkhIYfbtnlD6Cw/0?wx_fmt=png)

白帽子社区团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DK5OZOOglM6D8CODmqVX5pENgZsribK6KXeXxbic9BOTDC2oiapGqAhbC1p11TrLTC5YfoLeFOUdkhIYfbtnlD6Cw/0?wx_fmt=png)

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