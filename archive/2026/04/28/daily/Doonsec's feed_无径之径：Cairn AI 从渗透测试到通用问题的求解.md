---
title: 无径之径：Cairn AI 从渗透测试到通用问题的求解
url: https://mp.weixin.qq.com/s/nT7ojaMKFB1Qq2xjZx1vyw
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:07:43.751912
---

# 无径之径：Cairn AI 从渗透测试到通用问题的求解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ukaia78jfYMJ1zicyMhzJYNMWQeZoUgVbgAdguSqMbaMVpnpQutXdsToOWVdsWTr6ibk4KUOfLJZPtkKQgGzdzcca532oSITPJXfSftBCicC1Ns/0?wx_fmt=jpeg)

# 无径之径：Cairn AI 从渗透测试到通用问题的求解

天翁安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

向大佬学习！跳出了常规的角色型agent思维，与黑板架构相辅相成，给了渗透测试Agent一个新的思路。

以下文章来源于淚笑的赛博日记-起零衍迹实验室
，作者l3yx

![](http://wx.qlogo.cn/mmhead/KetjXWSVppuEjdTYBHeIgAe9C16gCftyLXB6I0F9gjEOoTiaACDdAHVtgeEI87hIoyuiby7a067JU/0)

**淚笑的赛博日记-起零衍迹实验室**

这是我在第二届 **TCH·腾讯云黑客松智能渗透挑战赛** 获得线上唯一 AK 成绩的线下决赛答辩 PPT，最终总成绩为**全国第三**。

"无径之径" 的含义是——我没有给系统预设任何固定路径、流程定义和角色分工，路径本身从黑板上涌现出来。我的 PPT 写的比较详细，基本交代了我整个设计理念和工程实现，本系统全部代码近期也会在起零衍迹开源，如果有任何问题欢迎在本公众号该文章评论区留言，或者加入「起零衍迹 AI 社区」微信群讨论，我本人会一一回答。

> 「**起零衍迹**」是我们专注于 AI 应用与 Agent 工程前沿探索的开源组织，我们致力于技术开源与社区共建。安全攻防是我们深耕的方向之一。

## 无径之径：Cairn AI 从渗透测试到通用问题的求解

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMKwqnFyOfy1xOtmLOl87IicniaWGw5IhFibPwDFXUxzh1F9csKyCXSfiaAP5bhwbbYdPJLGc9qN1jGxUcZLb1MPhZiaGg1ibytJaYBJY/640?wx_fmt=png&from=appmsg)

### About me ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMKx8AIhC5PzWQvPqnicaicDicd7GicCE1zfcoKYS2Vd1JmqAwVEciaPNAzsaLjbhd3XbWibBghLQPWnw2YEOWggZibd7vdtQRhGMuFeA0/640?wx_fmt=png&from=appmsg)

### 目录 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMLLDR4oOiaaN3JPmk5RtrFfcvQ14N6ODVHyzRiaVA9vgxIqWqcMwYM75KOzich3GJ2Yk9X1a4BmpibpwxRiaKNdMSWaEiaF0AicDre39E/640?wx_fmt=png&from=appmsg)

## 问题的本质

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMK7nkve8fxsKdBGia7TCB4JhH1Ep6MmjwRrtBBRncdTeGEGHOEJHLCY3eRz6L94hJY1RsfCZchZo7As67E7fXeib8OPHon0fNia7I/640?wx_fmt=png&from=appmsg)

### 开场 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMI2vAR2VEd6XoBllJzsqfA7o4ldQnXerng7gxI8D5NJaAHkkX4OMKoC33KiaLLgyVbYicW2YcY5jUl0y8OicicQXKD6BdxwD9IOc2A/640?wx_fmt=png&from=appmsg)

### 经典回答 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMIzJcZ8QugXpyXHV6tf4NXuj7OJOaOTFfM8viaeM5K1DbPp6PWUpvn5NviabVwkjJJN1aqXBWeRorFfyG5prKvK0oiadj5jHUzKw0/640?wx_fmt=png&from=appmsg)

### 状态空间搜索 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMJUoSQ8YSHdQLZxSCKmSpHh09rwOkicldoanciae5rrWdicVp3HnXBodC6RzuvQibQodspuRza6sVic3eGx65eiaCP4vcXOODofE3ags/640?wx_fmt=png&from=appmsg)

### 不只是渗透测试 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMIp5qQ1dgHydcWhxXJSzaibEkLBsLgh70IkIvxkOlA1aSl8L8LxNllIUbo45icdRQwOSagFUQfrYnX2mnDyFWckoXKOknh9XicGpU/640?wx_fmt=png&from=appmsg)

## 系统设计 — 黑板、蚁群、和涌现

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMLTkGkPUPXtAict0U7ORWw52h10YCz0eia3rfqYiaDGVs6t0qOmz3mKJxrURyxhwJq7qOvpgia7rkmmUl56sLpbsvl2P6KDN7uljow/640?wx_fmt=png&from=appmsg)

### 一个画面 —— 侦探破案 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMKAy7NA7KZYjHKu8vGNXLd8wSQKq7BMiaPKfQnAGFIRgaPHmvxic4WKtYdeoicZZKBc9Va1OJ676HRHZE8IT3StmnjKHDInn9yBqI/640?wx_fmt=png&from=appmsg)

### 我设计出来，才发现它有名字 —— 黑板架构 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJpwk2WdmJ1lQEYJrh0lp5HgMkUnFicBia2WEWhI2zTH4Sha3kPVxupdbvzQeoekwxHE6iaBNTQWQl6VscmzZ851nZBCFC4MEOhUY/640?wx_fmt=png&from=appmsg)

### Cairn 的黑板 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMKgDFqI6KpwTAHQ48lOj4cweRO1CornmSSZcXv8vfU8nEEwgAQcO8O89FvaTticJ0dW2qFkm6Bn5axKOAdsgL4cYFiadFEvibZAAM/640?wx_fmt=png&from=appmsg)

### Agent 的工作循环 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMLRduQXoK5RoSJqD2iaZBtnyktibZ69qAf2VWcibuvGcQPoonyuQT1e57OGQjfu6BSnevfwDYRXHCSXeTfQ8j8TWPqacdBSpts33c/640?wx_fmt=png&from=appmsg)

### 一道题的完整生命周期 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJtfZzVPyrH3jAozt7Oyy0CUQ4lYphDQJosJR5WTvIcbhibY23y82xBChxCpHWCFzvHQKstMWz4uYVEZia5Vbjz3Qxkt30ZCwrLs/640?wx_fmt=png&from=appmsg)

### 设定起点 Origin ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMKd1KQhjB8Jh2B0QMMEjVEoGx6zIlm41naiajjXdS1YlsRmpc6eKa5cWpvIWibr6knlscoyicibdSP8Wwdg82ibeOO53Mts9c0VQzds/640?wx_fmt=png&from=appmsg)

### 设定终点 Goal ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMKAd6VibbVlodXKYtfH3SPvAqE18YOAUXVj2wQVx3MhSjic3YyHDC1SUH3al7XLmGyGiabjK5LxrR0CTZpiaG4DdGDPCRgNicjGCM1Q/640?wx_fmt=png&from=appmsg)

### 系统初始时要求直接完成 Goal ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMK8vyASibic5b3tvX95aDCK8XKMPsJ3tibicicpJBvSPv1vKL08cYOSpAevS4E5szlUD7FFmUHrKRdCXMheBbtClxE9NM1ArZIBe3Ts/640?wx_fmt=png&from=appmsg)

### Worker 尝试直接从 Origin 到达 Goal（Bootstrap） ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMLcC0VrJAHia855P2pfY4W8XuOCSzT6nUckial7IaP5ERI78xlUSiaethDAYcyiahU8v1sNJQxyMTfkjQfIfoYOoewb36AKibN7Wz0A/640?wx_fmt=png&from=appmsg)

### 没有在指定时间内到达 Goal，但也写下了结论 Fact ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMIGw1lOthSGSupI6bgArZ7SQfxX92wwf1pzBp4bo5nibribc3cTuwficzLXRstEXpNSBgbRHt70EsOfGnCtO9BaadczL9lR73RoJs/640?wx_fmt=png&from=appmsg)

### Worker 开始思考下一步应该做什么（Reason） ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMKNkrYO4khP4wFhJWubtvpgFWSJk021FT1q2aea3fPickbkt8gia17CDIF2sLGtt2DGpdSGwUY0m4g7icS7cqXDUTglCLttf1I5r8/640?wx_fmt=png&from=appmsg)

### Worker 写下下一步 Intent ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMLNpkV0cBM72LhfOc8riaZAI7YjTTQfiasT5E0b22yp6HlEMGKtXOolshckPqlnwEjE2ZlLricO8IkeWCehhCQN5O3Niaia06JHcqbI/640?wx_fmt=png&from=appmsg)

### Worker 执行指定 Intent（Explore） ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMIKE1IdzHKN9uNuY9CVwJIDBHicRW4riaxuPBhQCBN3AucvrWdJahiaUWibm5vib2TkwAAaXFgFa79vQgLdiclAicxDHfiaVl5uib41MuYk/640?wx_fmt=png&from=appmsg)

### Worker 执行指定 Intent 完成后写下结论 Fact ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMKG1kX37oPmz5c3ZmgbicFXc0GJFwOYbdOoV899UCSeIK0xdIoFPYycTZscMWllxEW0vvLAaexb8d4mLBbpBMZcM5LXYQ1B9OOY/640?wx_fmt=png&from=appmsg)

### 态势变化，Worker 重新思考下一步做什么（Reason） ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMKyLYKeMPDeYrojONDQrVg1DLLMFnqKsfb3e4oxc9MY2oF10vnjaTR9iaOAat9tY7HEjBXX00bYAt2Y7Hiardp0TdaQR2nib8y2VE/640?wx_fmt=png&from=appmsg)

### Worker 写下下一步 Intent ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMIetSFNmUibmDQPFMQR2aHibX9YqfFiahHyUW96bzAibZCkrkcyj2h5o6St1tZrF85TuibWCAY9djStDR00mibibl1GCWe0lnsoFHMTXI/640?wx_fmt=png&from=appmsg)

### Worker 执行指定 Intent（Explore） ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMKsCNSUoC993jBWGl8ibziazVum7cicQBia7LUpHicjx6t0InQ7S6Er2PPW7oj6L2zXChjZQc0WPSA5icAxloYAmXVo6QIXtzicibElqIY/640?wx_fmt=png&from=appmsg)

### Worker 判定完成，连接到 Goal，项目结束 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMIib9bVwcF3zRNwwq7574Ms1VP9AtfHjE3B15NVQSj0q1Uu8rVoD8zC1nVOmibJ4TZK2xSBRouaOQYcqFH09fcicaP5fhicqSRI8Ko/640?wx_fmt=png&from=appmsg)

### 一个更复杂的案例 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMLiaSHrib296RoyFrZ0WasMKKTWZQVyziaZ6yavHsqeiaPicJHYusKcZtTtJ3jgDxvTcTRXY8gwOMibB3WsQSX96yicwI6ibibuiaEtKGoYs/640?wx_fmt=png&from=appmsg)

### 我从来没有限制他怎么做渗透测试 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJjFoo9YBKxm8nxrrakFtGGgbVKKib36zz3lgqWCIteReAhNCeQnticFxoAKvd7SldiawRb5z3mJngVAPcCDupTz8heMxtkMyjEXA/640?wx_fmt=png&from=appmsg)

## 系统架构

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMLVBabQsgJxowHib7wIibQmmgPaxNYvx1MYwGQiblFontfL1vuVqD61UYIxCdxUksRbBjibTU0f1WTVTaIIjic18azYvAt4lQD5XC9g/640?wx_fmt=png&from=appmsg)

### 平等的 Worker，动态的任务 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJ1a4Ke93jJY1U6krwJXGO4orzibKdXoLZvV0C9jC2mQQdFSZDPtWcFicvmKqthDcicrYH3WlF5lIFLicEEYZovF55p4FPia193trrI/640?wx_fmt=png&from=appmsg)

### Agent 之间如何协调 ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMKDXqicjia1Ly2cII0cpib2aE2um4uPw60UicD8h7bGCbILlEUXFPQ2AVSL53ia40ZeLQL6JWRKp0AnNGKaHM64vSVkv6ATAicJviaLxE/640?wx_fmt=png&from=appmsg)

### Agent 角色分工是人类局限的投影 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMIFMXlo5eWiamic2ic1O5eceVIy9mHFltbTiaibzZ9gQ9ibhZiaIhHAHicxrJ3ic87WW4IcU6dib2icAvfPqBdCq6NW3alXXS4vIChcBohUPo/640?wx_fmt=png&from=appmsg)

### 传统多 Agent 架构的角色分工是人类局限的投影 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ukaia78jfYMKhEl8fy3kmCW2LRahOjY5maia6q7rAJVEic8Y659R2QicOB1DqeBXEWA23BRG4ibVXpCpribXMfcAbrNpw2qiaG7ibnskQ3WJLnOia0s8/640?wx_fmt=png&from=appmsg)

### Less Is More ![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJv9AL9xJ4S2QeRWOfYibKY7osicNicF8Yvx5Mb2HbVg2FdYjyib2ItGIeBxC6J2RdkXPAOvBzQc1ibAITg3ZianCfH2nhNtAPFExk3c/640?wx_fmt=png&from=appmsg)

## 总结

![](https://mmbiz.qpic.cn/mmbiz_png/Ukaia78jfYMJf185fyb4qlJSx3CpjfRicnoajLZL7GHlwIuMagebKXvBthh37QcVautibxBicOC7ApdragIibJuRMOSqdBPjc4Z9cn9Usmk5X9C0/640?wx_fmt=png&from=...