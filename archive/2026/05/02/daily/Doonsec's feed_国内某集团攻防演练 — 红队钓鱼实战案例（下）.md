---
title: 国内某集团攻防演练 — 红队钓鱼实战案例（下）
url: https://mp.weixin.qq.com/s/oxqXSpqijvy14OYRtyIHsA
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:25:27.690851
---

# 国内某集团攻防演练 — 红队钓鱼实战案例（下）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cGhMn4Bj3bZlkQUicUMf44I6gH7RQsJfOxIZ3fMibv3fGRibhvpRp8Hs1VZ75xSyjCeA7FtMFNVibMvRIrI1O1t3lC8MBPibN6Bofsnt4d6q2T0k/0?wx_fmt=jpeg)

# 国内某集团攻防演练 — 红队钓鱼实战案例（下）

信益安研究院
信益安研究院

信益安信息安全研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 拿到权限后首先看看杀软，发现为金山毒霸

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bYVn125Fg2mhNB52IKlJUuur838jESSHOibherQuTsSia97uOs1cRTUtuHNHC2UmGPaaqtdicMfhxanv0ll0skoXtMJbzgcQ8XuGQ/640?wx_fmt=png&from=appmsg)

## 准备一个vshell的shellcode进程注入上线下vshell方便后续的我们屏幕监控：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3batSp9KxbDWdB8Fhs0qDViaxhOfuertRZhPS4hJ28qsBYkbRjic9tprvK9mqqMf7XwGxkGk6K6Afx02TOxkzBEAgMqbFhXNXQupM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bYM9ybT9ibibFSFjRHueI1rtE7lARWMia5jJNhNRpGwHJQAiazOMAEcNEPmsZu2BBWJRaO9s0IoeWg0lCATaxMufo3bYib2erJmjjF4/640?wx_fmt=png&from=appmsg "null")

### 成功上线vshell：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bZy5h7zPIEhtWibugjrXJxjMr029HnsOqnoamOFeJ0MfsK6fNgI6nozCSqNYIXRibtibNIlMkiba0rdGWj9tuuycHb8ladTuhgM7gM/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bbeibFTicQd73pX19NBWiaPibkSDFGadwYib4ZPIfEWiatSJdu6GRib2r3iagmnNulEWCia5icMQbQCVngtt8YB9pvJWyicYtQHBwrOVLayZs/640?wx_fmt=png&from=appmsg "null")

## 发现可以uac提权：

```
net localgroup administrators | findstr %username%     //能找到你的用户名 = 你是管理员，只是被 UAC 压到了 Medium IL。这种情况才能 bypass UAC 提权。

whoami /groups | findstr "S-1-16"
//- S-1-16-8192 = Medium IL（未提权）
//- S-1-16-12288 = High IL（已提权）
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bZ9Eaz7JqWumzYVgLImgfQy0xgdGcKcVmJbDGhoESOeYsGnOwhQ2Uiald2GoFzPDNngxMkX2auHs2U9NsbOISV0wSejbPCPh5Qc/640?wx_fmt=png&from=appmsg "null")

### 准备一个经过处理的免杀木马，直接bof执行uacbypass成功提到system：（管理员有sedebug权限了 就能impersonate system的token了）

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bawFic5hv0N3xoxw9SSyicZwAEOMTbnupW1sXnrsbwTlnztQiaJqRiaPujvs7QdHq3XXEGibRLnDCXBoVtp3wzByQBcyTHp4YeqUx54/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bbDQemTrKfQDd5mhv8Mh2DHbddhbaVTCFOBAqJcHgcrJrk8zqpDb0psicnorzmhrISIUXu0f78yM9uo6jK27jdL520qwbSUxc9c/640?wx_fmt=png&from=appmsg "null")

#### 因为提了权，就方便我们做权限维持了（略）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bYHibLPdn0MCI3Q7C4qeqvpLFI32vic2TZxeRIEeIiaHkmQlvGC7GdaDjviaRt7BKWXicMOW9OkZATAL4ibibxtrCzDibg9bhDalyzZgRE/640?wx_fmt=png&from=appmsg)

#### 以及去bof执行去dump凭据离线解密：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bbRg40fYic2zA7O4aPbdzByiaEzL3BJ7kJnYfWBQicTlUhhdu0SovgskMc2kOCrGgTeibdlqkSRn34r9du8m4XM3SlwNnjmmZ1n28M/640?wx_fmt=png&from=appmsg)

##### 成功解密

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZmjQSC9HK8Urm5vBicvF3u3SgoLMS0OE5A58phfUSApLd8IPtticSWuUDZtUcZcl6asbQeNXuDeu6mdDEOOLuHaz2dT5t0mW94c/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3ba9ZekbvbTZf9erH7PCGGFVIdicibwvqeIO8jgW3Q58sMibtmLHYQoPIuWtcq0YicHpk4uNzB8ibgmNyXSPl78XfBoHMMa1KoLOMRRM/640?wx_fmt=png&from=appmsg)

## 由于因为是钓鱼拿的权限，估计是个人pc，探测了下没啥别的内网，所以无法进行横向，把重心放到数据分这一块：

### 通过进程发现目标使用的edge浏览器，简单点，github找个脚本直接解密浏览器缓存凭据（因为自己虚拟机金山毒霸测试不杀，所以用的该脚本）：

```
https://github.com/The-Viper-One/Invoke-PowerChrome
```

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZAc9BanQlB3hjPtOiaAViaMyeJGaWLd7TibdtpFjah5nKN1FCg818Vb6UQHjQcZ4HmZEbvibNMejicibEFDCSzbyYsQMaYKCdtHKuAo/640?wx_fmt=png&from=appmsg)

#### 成功拿到目标浏览器缓存的凭据（至此成功进入5个后台并整理数据提交至裁判）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bZncDDHk23rHPqSwQ8iah9nYGnOF48ibF2IImV5e2DWqp4j0jk04Ghk7Sz2wLOGrOv0ib2U0zaUOe23XLAzhkx9a8icML7O24h0s58/640?wx_fmt=png&from=appmsg)

# 最后

🌟感谢您看到这里，您的支持与关注，是我们持续输出内容的最大动力

🌟欢迎加入我们的交流群

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cGhMn4Bj3bbPuuagKQt9cQFeG5bfxWsMY3g3RAV3Ie6PSsfnOqdEf7ibN9npMV0OxspSylRoFqY9gzibmSWGcVCibwFZd0tichyxf5CPwaWorGI/640?wx_fmt=png&from=appmsg)

####

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QuEg2icmqMJN031QmqC3zSSEqFE7RmUhmgcPTFGGHIofVlkhte6tRlku5hMKHfMWbOoeOSzfs9CcypicibwibvDGeQ/0?wx_fmt=png)

信益安信息安全研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QuEg2icmqMJN031QmqC3zSSEqFE7RmUhmgcPTFGGHIofVlkhte6tRlku5hMKHfMWbOoeOSzfs9CcypicibwibvDGeQ/0?wx_fmt=png)

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