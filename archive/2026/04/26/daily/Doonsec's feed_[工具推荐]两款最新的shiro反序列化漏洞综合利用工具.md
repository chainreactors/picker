---
title: [工具推荐]两款最新的shiro反序列化漏洞综合利用工具
url: https://mp.weixin.qq.com/s/GsZn0E8bW4_PS7-Q0niQ2Q
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:04:15.609789
---

# [工具推荐]两款最新的shiro反序列化漏洞综合利用工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQR4aW3Lyiaaxicfs0LSJo7M425260aljJeEcbK4QRZLicmDzYuAA99Fj7DRhic1ub18yuM657ET8ReFicGAfkspCMI9T0L2IibSSsaY/0?wx_fmt=jpeg)

# [工具推荐]两款最新的shiro反序列化漏洞综合利用工具

原创

陌笙
陌笙

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

工具一:ShiroAttack2

一款针对Shiro550漏洞进行快速漏洞利用

工具特点

```
JavaFX GUI，开箱即用处理没有第三方依赖的情况支持多版本 CommonsBeanutils gadget（1.8.3 / 1.9.2 / AttrCompare）支持内存马注入（Filter / Servlet 型，支持哥斯拉、蚁剑、冰蝎、NeoreGeorg、reGeorg）采用直接回显执行命令（Tomcat / Spring / DFS-AllEcho）支持修改 rememberMe 关键词支持直接爆破利用 gadget 和 key支持代理（HTTP/HTTPS，支持认证）支持修改 Shiro Key（内存马方式，可能导致业务异常）添加 DFS 算法回显（AllEcho）支持自定义请求头，格式：abc:123&&&test:123支持 POST 型 Shiro 探测与利用Key 生成器（随机生成 AES Key）
```

工具截图

工具首页

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRk5DVuibDdA1dCTXibWT8hO951CLkJ3JQ2xvLTZbicatFGxUt77p927FYfVXfYghpS0OiaT3icq8q0Xe28N8TfyPCELVrMDOibUWczI/640?wx_fmt=png&from=appmsg)

利用链

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTZLYMIl1UpJQ2BicnPfWzaAQCSQBzC0icnO5WfiaZqOUrJTlfne7EvZEuAibiaibOff5dE6Y5Uuic060fusnLsJbpBpZibtNOhBc5xSWk/640?wx_fmt=png&from=appmsg)

内存马注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS7bxhjAN0D1QVBf5n4Fah0rGwvkkVYhwby82KoKibkJkDYsiaen6Y27MB7HXiaa80kL9HzgXC6bqR6BJvqkJh7QdCfkt6uiaw5Er0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRShCk7KLefym0NrLowWyYm5L7wSHvvicicDPXmc9uXdt2oBTxm7lLXm4JZMTF2x9hxQhwTLmDO07UQ3t4WZiacXqUI9icGlCE1xHc/640?wx_fmt=png&from=appmsg)

shirokey修改

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ32Y6nf8IsicjLfMWY0ibvzFGDrMBsKDtfI9zXI024kpvDmGoakpVwrMOlrX51OYtpxDe3kLQqesyW5dtbxIcT1OlbnxT8WiaBLQ/640?wx_fmt=png&from=appmsg)

内存马生成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRx5JstetsvCh2H4JibgroyXQUKAF7P44jhibxKMVNkYQmdliac88wwsFq2Q4gVJrLqeicCXOH2WTDVib8XmeZqUhWH6ZjrvBLlZIIM/640?wx_fmt=png&from=appmsg)

其他功能不在一一截图

工具二:ShiroExploit

ShiroExploit,是一款Shiro反序列化漏洞一站式综合利用工具。

工具整体架构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSZah5dEvtEOicKe9sk9RWVmcUzGcEicKRr7YXoMrBDOqDibKYKze3G4lVsPVKYCtuM3JkU272E4exUNfRwC3Tze9WEG7vWWS2cnY/640?wx_fmt=png&from=appmsg)

基本概述如下：

```
1、区分ShiroAttack2，采用分块传输内存马，每块大小不超过4000。2、可打JDK高版本的shiro，确保有key、有gadget就能rce。3、依托JavaChains动态生成gadget，实现多条利用链，如CB、CC、Fastjson、Jackson。4、通过魔改MemshellParty的内存马模板，使其回显马通信加密，去除一些典型的特征。5、借助JMG的注入器，加以魔改，实现无侵入性，同一个容器可同时兼容多种类型的内存马。6、对内存马和注入器类名进行随机化和Lambda化处理，规避内存马主动扫描设备的检测。7、可以更改目标配置，如改Key、改TomcatHeaderMaxSize。8、采用URLDNS链和反序列化炸弹的方式来探测指定类实现利用链的探测。9、缺点是流量相对大一些。
```

功能演示

JDK18场景下实现命令执行和打入多种内存马。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRiayTWwI94hhialUicTYYuNBP8PRYsBO7K7v9OC7KMQ5O8MDJdN8LxPhkLtAD8fNqm1jdtGx3icOatibLv1YUlSXRel45FS8Vf0iaXo/640?wx_fmt=png&from=appmsg)

爆破key

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTLnICHV7fWk48X7MmkZmt1sMoY0Jz3nl8LyCic62me97RXJ0jwLJPZpYkWJa1rsIysfGSmwZWgDJ2nvKOJXLdgX6QiaibUnoeXJs/640?wx_fmt=png&from=appmsg)

探测利用链

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRUKtPicDOV7IL6ssXGgoibYLXtcvdQiaJHe77Cdrtv1FQY0v4DjV93RSXeU82sNeugc1ibclJ7PwzKvBPHQTcUSYbyVyuTvuU15x4/640?wx_fmt=png&from=appmsg)

命令执行

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQKY74QpmLxJCSeOyjPc7y6kXia4PTdq8B0vD0NCuPESwUYVQicFxvicglFJZzeVkKkcfSNevZGoicz9Eq8DYqj0vKCTKwNx3CLXOs/640?wx_fmt=png&from=appmsg)

打入Godzilla内存马（支持Behinder内存马）

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTQyba4eRZOpScGL4VmqCrGL7yo1Xyy92mOFEoayiajW9VrSrYdrgW64IibjRzS5oLsHe12E4IkXABibjzngiaiahW587JkdqcdFum8/640?wx_fmt=png&from=appmsg)

打入SUO5V2内存马

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSfIK4icYichdOUuLv7pI9lQicZ0ibFVrUAdQfxVNic9aTbAJz1FjP80801iasOVX6Cl4BMAPUFCEojaGlwx2WxhicV2FkK1gUcGLNbng/640?wx_fmt=png&from=appmsg)

支持Tomcat10及以上的内存马

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQUriaQ4tbgd8m86Rm6xUfzxj3xKicB7iaLlrgckt4QQ2xibicickIW0hKnzkbFKsHiaKqpolzia11ey23ZBOH16VRMHUVCv6iayxicniahtU/640?wx_fmt=png&from=appmsg)

其他页面不在一一截图

工具地址

```
 https://github.com/SummerSec/ShiroAttack2 https://github.com/FightingLzn9/ShiroExploit
```

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中）**

```
信息收集(会永久提供fofa-key助力)弱口令漏洞任意文件读取&删除&下载漏洞sql注入漏洞url重定向漏洞未授权访问漏洞挖掘XSS漏洞挖掘等等常见漏洞EDUSRC证书站挖掘案例分享SRC挖掘实战针对各种常见功能总结的常见测试思路等经典常见Nday漏洞复现等各模块不在一一介绍
```

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSWarKnFiaUicnq701hWQaiaA94FmgLNE8SVmrJiaJwluiavCE2VRvDV3ZYnwhib2pSNEpPp3Qp3beicPIAsVs3dS4A2MoYQXcsticwlqQ/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRD8gJdgFicMTaYcSMHydxPNJvagOaOrNbrM6S2tDPEcmjyECKacjmNJBCtwGAKMNdMes7tztJfWZGqjKxC7tkg99v4uDXDTpSE/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRPAemLYYSWRsc2cHYkwwxQicDQNf46MY8wUetFibPmetZdkicr4BNvPF0cBibqyS9emwayFf6njw9kjvBvWLoFDQJY5JQDMSUqh4E/640?wx_fmt=png&from=appmsg)

**陌笙安全漏洞库介绍**

```
1day&0day分享EDU学校相关漏洞Web应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSajCclDhuRpaLic9Ld915CHU7RqSC1LCrPGfNZiavdPEVeDedDWOPBhtMLCicTp3RNd1lT0Pmfo3mx5B0hUxbQg3ic6Via90NMtZVk/640?wx_fmt=png&from=appmsg)

**陌笙安全面试库**

```
渗透测试基本问题一汇总渗透测试基本问题二汇总渗透测试基本问题三汇总微步护网面试题目长亭科技面试深信服护网面试启明星辰渗透测试面试题目安恒面试题目360面试奇安信护网面试运维面试题目运维面试题库网安面试相关文档大全相关面试文章推荐等等
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSoLqEzH0a3A4LQrvTIkGx81Sh5pf6fCoEQJhYg715vrJicSkfBuCoAmV2Kp4uOMe5jcUZutPwicibFibtJ1ZmyiaAibCg0XicWnsNcicE/640?wx_fmt=png&from=appmsg)

**陌笙****纷传****圈子介****绍**

```
1、src挖掘思维导图，信息收集思维导图，edusrc挖掘思维导图，以及后续的红队&面试思维导图&自己网安笔记等持续更新2、2025-2026的edusrc实战报告包含证书站和非证书站以及2025之前的各种优质报思路分享3、各种src报告思路分享（内部&外部）4、分享各种src挖掘&edusrc挖掘培训资料&视频5、不定期分享通杀、0day6、有圈子群可以技术交流以及不定期抽取证书&免费rank7.分享各种护网资料各家安全厂商讲解视频&精选实战面试题目8、各种框架漏洞技巧分享9、各种源码分享（泛微、正方系统、用友等）10、漏洞挖掘工具&信息收集工具&内网渗透免杀等网安工具分享11、各种ctf资料以及题目分享12、cnvd挖掘技巧&CNVD资产&src资产分享&补天1权重资产分享&fofakey共用13、免杀、逆向、红队攻内网防渗透等课程分享14、漏洞库&字典以各种内容不在一一说明15、cisp-pte/pts&nisp一级&nisp二级&edusrc证书内部价格15、如果有漏洞挖掘问题或者工具资料需求可以找群主(尽量满足)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSY2pbvbP3qGAlW8O43bRvAISCxZm4UDTRsaMVbJKTsjfTMTDlq6qNBcVs4tkl4UzgqGz5ag81baU1rusKE09J9T6cMVliaibibwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTrLRQpTicOR7bzyNiajiapVJgyMiaYlEDBVU87YXMnanOFWsCYN3cCVGsKkibzV9dMryvbFXBb4Z3472ib27RJ1Xq1HnKJIp5u49GYQ/640?wx_fmt=jpeg&from=appmsg)

**目前650多条内容，扫码查看详情，持续更新中。。**

**如果觉得合适可以加入，价格不定期会根据圈子内容和圈子人数进行上调。。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTf4cCVdicO19OlMKjUqicUpTREyLiawUiaVBe7TXVa9fLcvT0mqkAEfcGwAcfNWxnUlaFBYLEvdU2wVjToBO4X0TfexQ2gecibiastw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQcC04k4SdMxslAAnsXQalzfUWyCs1AkITJOPWZtae9oKL9bs4QTHPmhfv1jbZTmHLS6HAeLysibzKyeicico7Jg923RDiaKp7rnTs/0?wx_fmt=png)

陌笙不太懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQcC04k4SdMxslAAnsXQalzfUWyCs1AkITJOPWZtae9oKL9bs4QTHPmhfv1jbZTmHLS6HAeLysibzKyeicico7Jg923RDiaKp7rnTs/0?wx_fmt=png)

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