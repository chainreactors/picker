---
title: AI 驱动的自动化渗透测试——技术现状、工程实践与演进方向
url: https://mp.weixin.qq.com/s/NpWAKjJH69rZFEseRAk04Q
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:08:37.915066
---

# AI 驱动的自动化渗透测试——技术现状、工程实践与演进方向

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Ukaia78jfYMJTPjLkEoG2JL7V9KQ5ia4GSLficfF0PAGAVZR1rgDQibDZJARbg0MOvehYWHj6iarcN812NMtmxcLFOEpFRnJ0DKibPgrCsoIFaNVc/0?wx_fmt=jpeg)

# AI 驱动的自动化渗透测试——技术现状、工程实践与演进方向

原创

l3yx
l3yx

淚笑的赛博日记-起零衍迹实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

这是我在 CSOP 2026 AI 安全大会分享的议题。内容包括对行业现状的分析，个人视角对国内优秀实践的总结，和对未来发展的判断。稿件写于一个半月以前，感觉在技术快速迭代发展下再不发布就会过时了。

然后在这一个多月里我也有很多新的想法和设计，会在后续的文章分享。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ukaia78jfYMK9XZaOTibVPgia1tFg7Kqiaqagib00D7n15l6qYH95K9EGLUBNoDjM4ehatXytFyqb0p9R2q90kd2hzI3As0wU5uCekcmYQogppQc/640?wx_fmt=jpeg&from=appmsg)

## AI 驱动的自动化渗透测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMKAmpyq9AAyjb60SgC2NSAmTTKz9pqmVSxJ9OPnsrvHmIQ3HNcJK9Sw3hcEYDkSiaR8CcrmQu3RHrrFSYoS7lD0TicFq5FSB2o6I/640?wx_fmt=png&from=appmsg)

### About me

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJqdDoEypvcQCuK3rzWmdJ7LaaqSfgqp7PibwVT5CxIYvYiapZGLutN40gWzp52HNSZKWxltcvuXSNFwyQrgicj2e70ZJkdOjx7kk/640?wx_fmt=png&from=appmsg)

### 目录

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYML87ibXxbk7PaObYiaBpvONF99yadeGv0j6InoeIUMKuHr82CAdUCPzYUl0nDzFxAyBqicXtGiccQAsaeuLB2jicvwiaVq7Ty27bV4hM/640?wx_fmt=png&from=appmsg)

## 背景

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMItno0q3hF0AafTFJsZEwNmqicckzIyxbrtW1tKwhuLLqRwJ0efsA1OKLbUmxp82v48y6ibRkicGjGcUgFDbaucYXjUvfLryM37Tk/640?wx_fmt=png&from=appmsg)

### 攻击侧态势

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMIYeZC31Ku8rZxSzL6iaStia4cRnNiaFdVpib5jjQMJgztHS6OX0rH5R3jOoXJLDxFADU5vRU8ZM4rRpVsomjN4KRn7iafyAT5MlvjI/640?wx_fmt=png&from=appmsg)

### 防御侧困境

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJwIOLEAxOTB5BbpPLORJzroT4yBEiafmPX58pib78sial1V2ahZcmF5NGzeENRZEgY6RGNTllexPXJjicc2GUZDtn2wY1BKE1mfsc/640?wx_fmt=png&from=appmsg)

### 行业应对

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMKL8iciassZjNwM9GQ9AWjAJOSoee6deMvIM3CW0fTZRopKGA7r6pg9JzNgKXJXOXsficcYz37RxVQd0ndQl68kCcSQkjicJcibe6bo/640?wx_fmt=png&from=appmsg)

### 为什么现在需要 AI 自动化渗透

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMJEbOoiaHbFiafv2tWJHY0ElPq6RlF9CVXyhNnQM2IIdF8nCUKRKSRwH3rKfzIdVxVl5v8mpPktvOXF4boRUiapvDxP0gWyeia46LQ/640?wx_fmt=png&from=appmsg)

## 技术现状

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMI7qL5eCgUHy7GRZRkP1IqtIPLmpmicPdsQ5fVlic0cL6QEW5L2VEvRiajDpSK1xnDFomKG2qLibrjE284wn4iaYpa9RLgH0iczTNI24/640?wx_fmt=png&from=appmsg)

### 自动化渗透测试的发展脉络

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMK9EgRwJl64lCxYvIyUAjdt8WHvh6ia3xiaIZrbiayVLW2DibyPV2GnNXcIKwP5cGU8u8oFqATbZPGrvLVERMhPF3DiaIbGLOU2tNmU/640?wx_fmt=png&from=appmsg)

### 真实世界里程碑：AI 自动化渗透与漏洞挖掘的当前产出

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMKvzpHD8j6ndLuowYnZdBJic1XXUmJYToJK89eb1BhCgjNsgldCnYFxv0vEeYbYGv90aukAunWENhtwIyCcWm90dhCabYlWzpO8/640?wx_fmt=png&from=appmsg)

### 一个特殊的观察样本：TCH·腾讯云黑客松智能渗透挑战赛

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMIW8m1yN4NuyVFnZTDNWlZozibQickYspPq7soenkbvc7uZDTs24cSyre3D1DWW1fRZ1hYde7E7qOhCSlwgLacuAzKOUmCicT7RiaI/640?wx_fmt=png&from=appmsg)

### 当前技术水位：已经到来，但尚未成熟

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMIl1a8zNEzSLQ5bd2XaXOf4G6b1ebE9PAicPoicZeRW0yA7vuGesZmrPcsGsP8gMfyqAibGmbIsDwZt21ViaVLMLBguBT8uHFr78bQ/640?wx_fmt=png&from=appmsg)

## 工程实践

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMIjuwlGoDFycj8C5ZNaEntic2nrQITWnAWNtqAZ0OaYsV4kUQxp1WKrtRt5ticMeJicYueLicCKxGtsTIDv5fEibzojqbLucUFmNlCo/640?wx_fmt=png&from=appmsg)

### 工程实践的表象

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMIzX43FvkHuMG9AAqG8rKiaMTk4rPdyibIfST0uicjmKlibVU8M6O8vibm6qyDzPDjHYmyHnzC3h3W9Lnico0KEydEcwnPRYt1qnn8Bc/640?wx_fmt=png&from=appmsg)

### 工程实践的本质：控制与结构

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJrXu5M02Ajur7iaDOKKICP7lV8zsuE5M9RN0e7zeL4maDa4AUbGgrqAHj70BOiacPaM9jPYI5Al2ZGib2Y4QJdoGOlHaCGfyks8g/640?wx_fmt=png&from=appmsg)

### 放入同一张工程坐标系

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMKgSCPHWClAibRp4q44iafvddCkibG27XQozoTQv9aFxoU7fKSIXspFkQJQLKBXsk0rSe31r2QzRVK5kqyUIEt8cTyp6aibvBiacf7c/640?wx_fmt=png&from=appmsg)

### 两届 TCH 折射出的三端工程转变

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMICTKutZjlTB3UXqKnfHHYKFR5jU7Gxr8qNia6CTuUica8P8s44vocFAnfyzkFP314C5uxeCWLgU0zRd1dn6ibYAkibNUq9eHicM3h4/640?wx_fmt=png&from=appmsg)

### Cairn 的设计起点：渗透测试是无限状态空间中的有向搜索

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMLg3b3wGMqtZVWqGVIgrvnTiaIFKicYgdcGRJYB5jicCoSbxSWVHy7POIjJMOgMdPK3yFLtEn5aZRuNkjeQHrsAglbNHUyXaJH5dg/640?wx_fmt=png&from=appmsg)

### Cairn：一张事实图驱动的自动化渗透系统

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJCibsVQ3esmMcAWmCffuRuNwcdmjpIyGxeaQbwR6GDBjibkHdR4icBRy2tP6It9ZhyDiaGcatrCq0iaTvgxqiaWRic4FFlUiciaHIh4CYQ/640?wx_fmt=png&from=appmsg)

### 把 Cairn 拆回三端工程

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMLvI73urYnDKHiaVVqHmTZ4TpODqjxO6FPCFsl9Uiaic851PET898LviaMkF5APYC7ibs31jzlESbxDJx08NEU8DF58ZN4FJHKzrg2o/640?wx_fmt=png&from=appmsg)

### 工程判断一：多 Agent 不只是角色分工

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMJ2eZmffJJG6ofDxc5lJdHzUcNlq8cKN48fVyYZ5Uia4j6wlhpnMk1y3PnlYHia2rurKeTuAHNYN44S3Sm2nC5P4qWj3J2LCIAgw/640?wx_fmt=png&from=appmsg)

### 工程判断二：工程要释放模型能力，而不是压低模型上限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMI5y81vHZvPOAeepU0SIaE8FKAdibXasgDJLEXoQHicDa1pRfCgXP0d8IJWmxAIyB3RhGxKGbwmNUTXMEzAIbjo0pnqBDKgjNNp8/640?wx_fmt=png&from=appmsg)

### 工程判断三：Workflow 会与动态探索共存

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMLiavGCPibicbdLeXkqsG7lNYOvicXAzygy0ITibCy69hJstbMr3Sbl23ab5acdkR5AfqNLur9bqIJMwr7ksjaEznn9gMTcprtgD3Xk/640?wx_fmt=png&from=appmsg)

## 演进方向

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMJjjV0SMTLElRFxDA5SKIwy4AW0XO1bQntukNjzr05sAsK8CS75wSBoe71bddRWlKsDQVdToh5Ih9nZCvaYQSbNgWhzcy95dsE/640?wx_fmt=png&from=appmsg)

### 用一把尺子判断工程的长期价值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMJQxYbukKvKzBK2x4uQAtrxp4uM9jpQdbEdKpPqsFKeouAOglibPjCU0s9IUTicfia7NibgkrysEHfJwBo9KunmISfBfLAASaePwPI/640?wx_fmt=png&from=appmsg)

### 会消失的工程，与会沉淀的工程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMLY7dovnqEPR5pibmzTtiank2YGUia6KrQRjaXR0tBXXgcdcha3LGQsCiazkaoCnMFKljBsLibdLg3WR0l6XguEQDzhzazT5lYcCUUE/640?wx_fmt=png&from=appmsg)

### 从自动化渗透，到持续验证能力

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJBRIGJ16S7KP1MMSO5Wicc8vaEREazM9giar0QetaJCGzvuoyF7kvdxuAexO6pGCMmMOqa0XTpH4RDlBkCTC9YqD4z9GH5nMUE0/640?wx_fmt=png&from=appmsg)

## 附

### 开源项目

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMJqPBIw3IcZb5d2pheiaIcPoIiaMryrGqjGVMveh3UwXDU24eEDN9mmMfNw3PibRVPL0w05rXxgoibP5X6PGLjQH9tctzGssBsqN7Q/640?wx_fmt=png&from=appmsg)

### THANKS

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMKunZ9ujmK3zuyY0GCX4yV1he8veWJAU184DN9GbXrlgVuTvr4tJaeYwRLKCjuqUicH9L1vg2cs1SAVm9p6edxhgI5Ps2S2ecH4/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/CWdFC7ibFjyTiceBWekJMdgtvc2rx4L9AwibYGEhytXwD5uia712MlXklaVlzPKiaZZQLAhQBUcxjtB00eBUaqlUAsg/0?wx_fmt=png)

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