---
title: 利用pua+ctf-skills组合解决CTF中的逆向类题目
url: https://mp.weixin.qq.com/s/01vE6HMevVCmvuEh9HcMwQ
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:57:14.126677
---

# 利用pua+ctf-skills组合解决CTF中的逆向类题目

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xY9ZTT0gDw6rTZw7L2h1HTl92uZEWlR3QTVic1VEdRs23FiaJYfER2myLlPAQsAhMvgCcmxpFex4qgOf73px72Ns97zKFwskVaQW3DlnbznwI/0?wx_fmt=jpeg)

# 利用pua+ctf-skills组合解决CTF中的逆向类题目

原创

huan666
huan666

huan666

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、前言

随着大语言模型（AI）在代码分析领域的应用深化，以及ctf-skills等模块化逆向工具链的成熟，将 AI 辅助分析与工具化流程结合，成为提升逆向解题效率的有效路径。本文将介绍如何通过AI 辅助分析（PUA）+ ctf-skills 工具集的组合，构建一套高效的逆向解题流程，覆盖从初步特征识别、脱壳反混淆，到关键逻辑定位、Flag 提取的全流程，为 CTF 逆向题目提供可复用的解题思路与实践方案。

二、工具清单

```
pua：https://github.com/tanweai/pua/ctf-skills：https://github.com/ljagiello/ctf-skillstrae：https://www.trae.cn/
```

三、skills介绍

pua skills：

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw7JweJib3CeWBgyiapvO7BtbFiafqC4XdnuzlaK92l380koxTHelsZNRlqKF8lDjK07AjK9wQuJH06uJ37ePxUOQSgqtG0T6F30sQ/640?wx_fmt=png&from=appmsg)

ctf-skills：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5BfInicupLIRDBsOgtM9o5Xv9tHyKo0DXcSG3jUfSkFMPvCpEYuwPaeibORhZNh04oHuIAMicRkxLBY1Kn0bM4Rn7jDIqoJiacTF0/640?wx_fmt=png&from=appmsg)

四、工具配置

[基于Trae的AI自动化安全测试实战总结](https://mp.weixin.qq.com/s?__biz=MzkzMjk5MDU3Nw==&mid=2247484740&idx=1&sn=3a62e0cc4905d77278ea557791c2c20e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw47sY1DiahPehnmUUmsAHVBmdSETgYTqibrdy3pMJ2MPTVEg1rUrMxDTVNdjKK9YkNcdz0OvE2OoVKS17kw5cBWSzEBWhuwKnf8w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw63lgKGB5Emn61LQ2V3PBqNJf6I6Gne2rebU0WnS8fYyOc16NJehqh4GEc4L3H6sstoBcicK7Yqe9rwJwHknVfHw2ibFYhqcLMiaI/640?wx_fmt=png&from=appmsg)

五、案例演示

|  |  |
| --- | --- |
| prompt | /p10 /ctf-reverse 帮我解一道ctf Reverse类题目，题目附件是：luck\_guy。  注意：解题过程中，不要给物理机安装任何exe程序！ |

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw7zLTiaDSZPSkEzibGHcB2cH83AGdOia1uuk5uSM0rrPd3Ju9Vic3PfvOHpo2ibgEVa0ZCmcUlnhzvCh7kZyBdlo3TWvT5owY3OibgwE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw4edWSLYAtx26Hwcia2lEFDkQ9pwTUFaBMI9W1gOju6PBbxxonwK0u7vib6icDnveRiblSSdCuBQEbAytP2WnY6uCp9vX9RqjOPBCM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw7N92LxpRrZFcRS2MjMlZTX2cl2uYZhZPPfLucthysAT7aq7KicdJZe6tHACAQ7gPcOltibn1bm8dkWibDlhvtO8ibILC7cqvESdnQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw4NFfatGEIEXhLQGMFM9qxicp33icZvDaRLG6tz5VbzvhoTOHib1udNyGgo7U5KsjJWCib5VjHeFWlCvRWp1ZJt9zu9icxPibNxnOT5k/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

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