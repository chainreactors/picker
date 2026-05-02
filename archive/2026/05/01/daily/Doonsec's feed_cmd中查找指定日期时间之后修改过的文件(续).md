---
title: cmd中查找指定日期时间之后修改过的文件(续)
url: https://mp.weixin.qq.com/s/BcLibEHnjhDJM5kQsYO3Cw
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:58:47.010944
---

# cmd中查找指定日期时间之后修改过的文件(续)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h56Z2h4w7Jl4Uy3aibesAnHrlT5cWbPeYYO0vAju68VZ0j9nRt31dvEC8kcnu71uib0VMnPicswSIbjMyjNCsrBJOm8zekSPXPTHJha7pibX6Po/0?wx_fmt=jpeg)

# cmd中查找指定日期时间之后修改过的文件(续)

原创

沈沉舟
沈沉舟

青衣十三楼飞花堂

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2.11 查找指定日期时间之后修改过的文件

```
https://scz.617.cn/windows/201607271351.txt
```

A: scz 2016-07-27 13:51

(之前的内容略，十年后在后面增补一段内容)

Q:

想在cmd中显示当前目录下修改时间精确等于"2026/1/19 13:49"的子目录(不要普通文件)名，不要遍历子目录树，只要这一级的。只要目录名，不要大小、时间戳信息。

A: scz 2026-04-30

forfiles干不了这个，它只能以天为单位，精确不到时、分。

方法1

```
for /f "tokens=4,*" %a in ('dir /ad /t:w /4 ^| findstr /c:"2026/01/19  13:49"') do @echo %a %b
```

---

```
for /f "tokens=1-3,*" %a in ('dir /ad /t:w /4 ^| findstr /c:"2026/01/19  13:49"') do @echo %d
```

/ad使得只显示子目录，不显示普通文件。/4用4位年份。^表示转义。findstr时注意日期与时间之间是2个空格，这与dir的输出强相关。

for的%a对应第一个token，后续自动赋给%b、%c等等。token之间用空白作分隔符。

方法2

```
powershell -Command "$t=[datetime]'2026-01-19 13:49'; Get-ChildItem -Directory | Where-Object { $_.LastWriteTime -ge $t -and $_.LastWriteTime -lt $t.AddMinutes(1) } | ForEach-Object { $_.Name }"
```

---

```
powershell -Command ^
"$t = [datetime]'2026-01-19 13:49'; ^
Get-ChildItem -Directory ^| Where-Object { $_.LastWriteTime -ge $t -and $_.LastWriteTime -lt $t.AddMinutes(1) } ^| ForEach-Object { $_.Name }"
```

有些^号用于续行，有些^号用于转义，勿搞混。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOa7YUszQ2zP2AFStE4UScicKMwhEqpde0j0FEheXVmbxSG8JFKDG3K8piaJjMHLjicL5zKemTibjvuQg/0?wx_fmt=png)

青衣十三楼飞花堂

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOa7YUszQ2zP2AFStE4UScicKMwhEqpde0j0FEheXVmbxSG8JFKDG3K8piaJjMHLjicL5zKemTibjvuQg/0?wx_fmt=png)

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