---
title: 抓包即可篡改实验成绩？高校虚拟仿真平台安全隐患曝光
url: https://mp.weixin.qq.com/s/-aF0UzZxLL3FIj8iCYRIyQ
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:35:21.738746
---

# 抓包即可篡改实验成绩？高校虚拟仿真平台安全隐患曝光

# 抓包即可篡改实验成绩？高校虚拟仿真平台安全隐患曝光

三垣网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGKsicia8QzAOah9mKaBhNGmpIkuVErKjibNp02STYUiclUVDib4e58MngaVHuV1GzFW8S3yMnxEIAXJIzSVD2tpBbuxibQ1XUw7OqYE8/640?wx_fmt=png&from=appmsg)

1、前言

高校虚拟仿真实验平台，现在已经成为线上教学重要组成部分，学生在线完成实验、测试，系统自动核算成绩，部分成绩还会参与校内排名统计。但如果后端没有做好参数校验，攻击者通过简单抓包修改请求字段，就能随意篡改考试、实验得分。本期我们就来看一处教育平台的逻辑漏洞：仅修改前端提交的 score、chengji 参数，即可绕过业务校验直接拿到满分，给教学考核公平性带来不小风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGIHrucG3R1HQPZrY42Rro451EfTicxGJZ8g7MrHT3fxU4Sp0o8G4jU7SPMOnT8XCPuZHNiaSAIlnlRoCCA8LjNntPUvyHnHw9QNU/640?wx_fmt=png&from=appmsg)

**2、漏洞复现**

1、进入该虚拟平台，找到专家登录，选择一个实验

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLib0CzhG8v6E1SyiaG3YT9T9OmiaCSc3ZVvs3drPFlpQ3B8NKNCBLItB7sa3kFGYMpXibp7zKP9xHxm0ibOcGEpE2szkBAf2zmSBics/640?wx_fmt=png&from=appmsg)

2、选择测试

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJQDXAeIRW3BiagVrBgQFu8OLYNHPicrKS9OYVRCNEXEicb0eYdia3eicXnPpm30prYHQKOVeyFsk4T2q9sDEibYu5sFiawsZXrgeZjAQ/640?wx_fmt=png&from=appmsg)

3、提交试卷抓包，把score字段改为100，放包

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SxoDJcKqQGL6Qv1MLkSokYtLGkeY6T0BAXGACDGrltvhyibv9xZy1VZ3v9dibmesyBzrxdxztfrLCLtj4uK1w8lAjZJPm4c1cWyCcLTt86k84/640?wx_fmt=jpeg&from=appmsg)

4、发现成绩变为100

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLvwwQQ2e54ZtuOL5vKJSDHd6sxRRQJd8Qsw7BM2cQQF4RpBJkzGgLFunuWl9kG6oXm1YZciaZwHCRyPatZajhLG1K25k8QfodY/640?wx_fmt=png&from=appmsg)

5、下一步在我完成抓包后

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLpm6VjWicgEkAAOAnRhacUEHY7zqocfQQ6rfSqKvj7YPibcqH8dmVrDoTzDhSmxeWmDEZzsRPsiaBl0QD6JnfTpu24g5dvZ5ul9Y/640?wx_fmt=png&from=appmsg)

6、把chengji参数改为100，放包

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGLVhPeHm0pZahLaJEeQiaWGLPMwzR5EHSRhzrn3pSicYPzv42Df4AdAexn7Vd6uhoET8oemp7XxibYJw3tPTxiaQNmYLMLOaibicR2b8/640?wx_fmt=jpeg&from=appmsg)

7、实验成绩也被改为100

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLCIvckVGuhDwYeiaQJ602rplOEgX2WXAiakwkCAYyaTX5ISBEbtNQ0oW5lHNutuhOUyPwQ8NIRCaMvpic0Kgwqic7YMdjRDs1iaRAA/640?wx_fmt=png&from=appmsg)

漏洞危害:可以任意修改成绩影响教学，成绩可以计入排行，影响其他用户成绩排行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLUmhrmcyucmaryuDvnLLTfIV7vhX0LEXBKUjJaTiaiaMXREicb8bIFIeXtCHQ5G4dUgBfJ6MBUn8iavT89ePicG3iaSCYJZAAlx9GqU/640?wx_fmt=png&from=appmsg)

**3、总结**

1、这类属于典型业务逻辑漏洞，根源在于平台过度信任前端传来的数据，没有在后端对成绩、分数做二次校验。前端参数可以被随意篡改，不能作为可信数据源。教育系统关乎考核公平，一旦漏洞被滥用，会直接破坏教学评价秩序。

        2、对于开发人员来说，所有关键业务数值务必在后端重新计算校验，不能直接采信客户端提交的参数；也提醒各位安全从业者，在做教育类系统渗透测试时，可以重点关注分数、成绩类接口。网络安全测试仅可在授权环境开展，请勿用于未授权系统。

#逻辑漏洞 #抓包渗透 #教育系统安全 #web安全

搜索三垣网安，学习更多网安技术

期待你的

分享

点赞

在看

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJaWOwicn7raXm5k4xXDlBia0Okyg0R9d4niakArWeAcFZe0mbIWPKXdgcJHv0mIY6picqR7UB0GmPPeMC70E9VFWMXDEdYOj8GS3o/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过