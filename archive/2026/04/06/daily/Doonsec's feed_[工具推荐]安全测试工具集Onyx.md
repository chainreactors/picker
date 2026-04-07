---
title: [工具推荐]安全测试工具集Onyx
url: https://mp.weixin.qq.com/s/oijf5BILBPxaQpotBNZvNw
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:27:41.295947
---

# [工具推荐]安全测试工具集Onyx

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboSUYm8GCHutFzkDXIMShOlsSiadOzibDDialWPL5icNt5JI5iaCOK4faDXPHlOEKgZse0zttZfxSwrEm2DkNibyAnuLZDyem1a4vuncc/0?wx_fmt=jpeg)

# [工具推荐]安全测试工具集Onyx

Mstce
Mstce

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

项目简介

**Onyx** 是一款安全测试工具集，集合多种渗透测试常用的功能和工具，赋能攻防、渗透等场景。整合空间测绘、漏洞扫描、主机探测、信息收集等能力，提供一站式的渗透测试工作台，告别需要到处切换工具、网站的麻烦。

| 模块 | 说明 |
| --- | --- |
| **空间测绘** | 集成 **Fofa**、**Hunter**、**Quake** 三大测绘引擎，支持批量资产导出 |
| **漏洞扫描** | 基于 **Nuclei** 引擎，支持 POC 管理、批量扫描、请求包可视化、一键生成验证图片 |
| **辅助工具** | 内置 **CyberChef**、JWT 密钥爆破、编码转换、Fscan 结果处理、攻防批量截图 |
| **应用加解密** | 提供 **FinalShell**、**Navicat**、**蓝凌**、**致远**、**帆软**、**Druid**、**JBoss** 等常见应用/中间件的加解密工具 |
| **小程序分析** | 支持微信小程序自动识别、反编译 (`.wxapkg`)、敏感信息正则提取 |
| **企业信息** | 支持 IP 归属地查询、ICP 备案信息查询、企业与股权结构分析 |
| **信息探测** | 包含端口扫描、杀软识别、指纹识别、敏感信息采集 (JS 分析) |

## 提示

macos打不开请运行： sudo xattr -d com.apple.quarantine Onyx.app

## 功能

### 快速启动工具箱

渗透测试工具快速启动

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSr0lzy7Gw3v3CIRkp5o2ibREIacQtdgGu27axg2icN1hqoe5u8bjw4OKYWeDc6iaiauhOpDQSC2S4iaatY8XNPVWp8TqKibJnvg6pKU/640?wx_fmt=png&from=appmsg)

### 空间测绘

支持多种网络空间测绘引擎

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQvrQH3KF3zctymwZKhO9EWFujqSoRBv7hccfHg9wn41Kqb5158ULMkdxXq3hTXdWBGUqk2PPSKrwJC1SgQjySF6JYSxSzNudE/640?wx_fmt=png&from=appmsg)

### 漏洞扫描

* **Nuclei** - POC兼容Nuclei模板格式
* **POC 编辑器** - Monaco 编辑器，支持语法高亮
* **请求重放** - 支持自定义 HTTP 请求

**漏洞管理：**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSn01icSIpD0G4dYScrSdJADptVibqLzGqJmuQ6LyqfibkFgvTEpaaj2bGpH3KQdzsC7cn1BW19ylCrWEWoS25FBjicKPb9T0DFBA4/640?wx_fmt=png&from=appmsg)

****自定义POC：****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS038e8AvAWZbXUz5QKPiaEwGAE11nicWpv29HxR2XL6WUgUhmKxegv7G06eoCzXgqicRkjkJ5wnO0Hdkje1LHdy9qtUBFJOZNPqI/640?wx_fmt=png&from=appmsg)

-- 支持AI助力生成POC

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQN1ibB85NeTyPCLpUjM6dOqhIh9MOOdiaRUyKL1ibTSichPxJovf6EgmibzbIEFBLXicBiam8OcCCjeB1icAb7gcSjvlYcN6OoE8aDrRs/640?wx_fmt=png&from=appmsg)

#### 请求重放

* 自定义 HTTP 请求
* 支持各种请求方法
* 实时查看请求和响应

#### 示例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSc2FzdaU7c7H292K3SrpaJ5Re5FEiaId2yUic63dSn6ZOJ4bGO7IRHQ88ANK8TGoRzM3SEfzZB28A24sUWbpr0REBFNkKRKibGcE/640?wx_fmt=png&from=appmsg)

### 信息搜集

* 通过域名查询相关企业信息
* 股权结构分析
* 资产收集与关联分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRCWEia17tV4cr4rcHTnJcJDTNzjr6M0BKmSDnQJNeoA9LBZgibpgrSzUU2yN0KThIVxak66l19iaUPYA1G3pdLUyibhzBwyPV3iaTY/640?wx_fmt=png&from=appmsg)

### 攻防赋能

#### FScan 结果处理

自动解析和格式化 FScan 扫描结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTfUEpPofyn8sdCENwbMicEDyMvQYia0XFwMwXkgGaBLPXdXvl2dNDmsBPMZV43seXCGUNiaic1ibLWSL9Y4uVto2ThpiaGsoC5xHQcY/640?wx_fmt=png&from=appmsg)

#### 快速截图

结果批量截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKGK4PqvwTqQqHNyfziaxRhibMlnNBrTAOSna4ljCbrxMFmRAzrhibETbDHtpNbeMU3bWlpZoNUAjwCveib8VRfwX5N6mkIWgkEyo/640?wx_fmt=png&from=appmsg)

#### 微信利用

支持公众号、小程序、企业微信的 AK、SK 利用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSquOpCZQRasic4k39066jwYY5cEgTYn0lkElTHL2eMBs2IKdPg7ibfEbsVM5F3hOzHy1jnnbMhibb6ZD4kaC4xfZx7BIufkibmVYU/640?wx_fmt=png&from=appmsg)

#### 常见资产密文加解密

渗透测试常见高危资产密文加解密

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTJ2VuUUHA7WhOHSuebwvJKEbCwicMeZ5ibz6zug1c9nqXQWt5mheDA2wn5tFIrN53wKkpD5GjarWGgMsbRh3fumEoHY1coWD5xU/640?wx_fmt=png&from=appmsg)

### 微信小程序

* **自动扫描** - 自动扫描微信小程序
* **小程序反编译** - 微信小程序反编译与代码分析
* **小程序敏感信息搜集** - 自动提取小程序中的敏感信息
* **自定义正则表达式** - 支持自定义正则表达式进行信息匹配

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSNDh8OoFvf54bcQAoCNn3QZJQtSYvQOn5Va2ib7MY7NaibBNQsMxwKXRjWViblhccQEG5kOb1wRobiapdvzsxib7ZnrzYia8YSRS3dY/640?wx_fmt=png&from=appmsg)

工具链接

```
https://github.com/Mstce/Onyx?tab=readme-ov-file
```

**交流群**

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboTonoAcMicu8KdPtTq6Dqe4oozEuCAFOxTicicIb4lqMibY2NorTrxcNRn0Vx4H4BwicltOjxIfHVPPFgWlJAkO79JXPg5Y6yXdMPrs/640?wx_fmt=jpeg&from=appmsg)

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS2XK1iaGNrmliaogCnNn8Odkhrgib6bZsCHbib3drrWtIxs6voRiccXdHb1dic2GVBqLw8PZhOqEOSPT85Ur2aAsHqRAvs3IQUX32Ys/640?wx_fmt=png&from=appmsg)

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSxdcm5nYOYib6RQ9icEbL24CEdgW8picdlKScbf20oibpwVYewMyuhgZz1RMv7Vib8kr73PvErOKEm3MSEcVslJNUFEJ3OcDHXibKKw/640?wx_fmt=png&from=appmsg)

**陌笙****纷传****圈子介****绍**

```
1、src挖掘思维导图，信息收集思维导图，edusrc挖掘思维导图，以及后续的红队&面试思维导图&自己网安笔记等持续更新2、2025-2026的edusrc实战报告包含证书站和非证书站以及2025之前的各种优质报思路分享3、各种src报告思路分享（内部&外部）4、分享各种src挖掘&edusrc挖掘培训资料&视频5、不定期分享通杀、0day6、有圈子群可以技术交流以及不定期抽取证书&免费rank7.分享各种护网资料各家安全厂商讲解视频&精选实战面试题目8、各种框架漏洞技巧分享9、各种源码分享（泛微、正方系统、用友等）10、漏洞挖掘工具&信息收集工具&内网渗透免杀等网安工具分享11、各种ctf资料以及题目分享12、cnvd挖掘技巧&CNVD资产&src资产分享&补天1权重资产分享&fofakey共用13、免杀、逆向、红队攻内网防渗透等课程分享14、漏洞库&字典以各种内容不在一一说明15、cisp-pte/pts&nisp一级&nisp二级&edusrc证书内部价格15、如果有漏洞挖掘问题或者工具资料需求可以找群主(尽量满足)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSY2pbvbP3qGAlW8O43bRvAISCxZm4UDTRsaMVbJKTsjfTMTDlq6qNBcVs4tkl4UzgqGz5ag81baU1rusKE09J9T6cMVliaibibwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTrLRQpTicOR7bzyNiajiapVJgyMiaYlEDBVU87YXMnanOFWsCYN3cCVGsKkibzV9dMryvbFXBb4Z3472ib27RJ1Xq1HnKJIp5u49GYQ/640?wx_fmt=jpeg&from=appmsg)

**目前620多条内容，扫码查看详情，持续更新中。。**

**如果觉得合适可以加入，价格不定期会根据圈子内容和圈子人数进行上调。。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT0iaBwm4aD4ER0ncNHUj8Bh7PMD2W4nfxvVhT5O9wRwM5emREABQBPRVM042tq4megNhwJypRsjPExQtlbib1YWVxdoWyNQ55cg/640?wx_fmt=png&from=appmsg)

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