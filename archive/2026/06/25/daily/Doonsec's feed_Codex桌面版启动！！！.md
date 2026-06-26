---
title: Codex桌面版启动！！！
url: https://mp.weixin.qq.com/s/pA4agRElZrx8XT2fLRc7xw
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:04:58.464911
---

# Codex桌面版启动！！！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b34oV9VTkcFhFt2RBf9nr4V2DpuRMBdwQXmzpUagNf2UO7mKia4hnfu8qaIjPcRianAlKOvQYx7yTiafgORFxWJ5u8dvibUmiaeShxmf5B4GA2J0/0?wx_fmt=jpeg)

# Codex桌面版启动！！！

原创

小谢
小谢

小谢取证

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字“小谢取证”一起玩耍

这篇文章教你零门槛安装 Codex，并通过 cc switch 把 Codex 接入 DeepSeek国产大模型并应用于电子数据取证的网络在线提取实战应用场景。
  重点是：使用 cc-switch 图形界面就能完成配置国产大模型，没有复杂的流程。完成大模型的配置后，可以使用codex使用chrome的mcp工具对网站进行固定提取。

先展示成果：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFHIlexk7TVXo6cWWeiaghr0rOuN0v6ribicfLs79QXQHxyIEPqDoZLuhgW6gqhM7Mxiae2frbgh4usVOE9mANdTa6HQHCsuOrib7NM/640?wx_fmt=png)

输入提示词：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEKM8icccUZz6lEkeJwLBGXjq21UJg0R000fZmJH2oATOjerH8DKyeaPoP00TqeShySaNcpjpcbLVXfsJ4FjvItVia1UXPqlCSpE/640?wx_fmt=png&from=appmsg)

截图文件：          ![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHB7yrkibHvU4FRrKfYrrRf2oUcX4keBa7xEHQB1jr8s12w1XFlFDnr2e16g6tPFfnsZ32PKf2HP2g1wrIa2eR0Nh7rblUaqjCA/640?wx_fmt=png)

表格数据文件：          ![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHsLONUQ0uIZ4HgqOwUNLf9Ibible6NzbozKiblmu2JQ1LWI7AUicQXicibwoQsFBia6V0R5YW7pQMBicVaETn5o3aYzXXaP6icPTto7zQ/640?wx_fmt=png)

本文目录：
1.codex是什么？
2.codex如何下载安装？
3.如何使用cc-switch配置国产大模型
4.codex应用于电子数据取证当中的网络在线提取

一、什么是codex?

  Codex是由OpenAI开发的AI智能体工具,是一个能理解自然语言需求并执行复杂任务的AI助手。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFnrIHE5ribyWJOht0SDNLAAZGGZiax3fESA6KLY3uiaOjqajWShk3RhIA0UWlwpBp9kSmRLicOQwCqBHxqMibCauOww8POzvZia03Oc/640?wx_fmt=png)

二、codex如何下载安装？

（1）获得方式：

方式一：科学上网打开：
https://chatgpt.com/zh-Hans-CN/codex/

点击下载windows版:

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFiccht9gSEeA6OkZtjKcNGgv0BjG2nqndSEaDichf8ibAcWDxe6UAPS028bGoSKNr5cRGb9QoXfzf8F1NW0roicykQKuAZEmZauLA/640?wx_fmt=png)

下载后运行安装包即可：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHKVia1bqiaq5NMR17Uv19GgXbv6Apg9TslmkQ92XKAtXZ5KCFHtTQGzs2yBITqicqVVF0XXa4rFdOibXGjE8cbK83QjTufAeIOKBs/640?wx_fmt=png&from=appmsg)

方式二：直接在微软的应用商店搜索codex进行下载

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcF62nrzrekAbAMQKoTLiaChVdpIbMiacF8bQ1XtYhguVHFcSicfDCntIOjlnys0ASAtCDBQ3EQgLXnbRqGFktzeFg0GiaEe9BCuQgQ/640?wx_fmt=png&from=appmsg)

方式三：但有可能你的应用商店下载安装不了会遇到以下问题：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGvY3e6F4x3LYULZs68gWeOCmrkn0UAnNQjzIgxtpYXRG8Uibq4UfHkN10eZRNibTeh0ibLUiafr945jfuoLb4e35yKxicqOe8vib4WU/640?wx_fmt=png&from=appmsg)

这时可以用绿色免安装版：
在用绿色免安装版之前，我们当前的安装环境需要有node.js环境：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHWd2vTuVOAIsCnPhWSSLnq9Azp9qpSNsEpuc4oyfFXuILr8ydFwqibk5aGADsLV7UJ9fDG9arTFOWaRbLQgrhCtZEc6pHdanAo/640?wx_fmt=png)双击运行。
运行之后直接双击运行，就可以直接运行。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFwo3ExmhKQju2ow7s04INZRxc68cSwffJtyC7C4mK6O6Fn3UmOwlEht1EkByiay37o0LPuUYg7pkJ4oUlmSBeibia88J25Q2rJw4/640?wx_fmt=png)

三、如何适用cc-switch配置国产大模型?

（1）在codex应用程序运行前，接下来我们要解决的是怎么在codex当中接入自定义的大模型：
先访问https://github.com/farion1231/cc-switch/releases/tag/v3.16.1地址进行下载cc-switch
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcE4pfHicfRCZrwdrglUk5PeibyYlXb7ibMmrkvE8otduDwYSxRd5Bkyag0ZkHtpTQRWhYPJyolMH65pmY1NADFzfiasBtCwkpyHuCA/640?wx_fmt=png)（2）接下来就是安装确认：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcH3Ex6OoKFGsxbiaxiaoAxVsicFr5sKRsWfeE2kFuyCq8qnUbqyzPY6PSooVaiaTJdCAC4EPDH9JtibXySSZ7Uo1icxL2icYAaQkibUC7c/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHibHMuE0ictyEdKPf4hjst6WxCzZDJYhnic6uiadLAflKA2UIwBnamKOLJb1smcEctiaKYc4u6be59vb0ozov3eQT2paRyBnahCmXc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFQsBIyWBXxzsJWtxxLLqarHE2ZVqLQnD4GzVibGkxt9Wkpdr0OF3NMFu1d8IIksyrxOdU9b85HkjhoD3LecJtg9F3vbvVG1wicQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcG44t5jpubfMYB0gYO6UPL50Cic7Qj1mLALp5Wiafniaz9IQ2G1IjP8BcZwxNxd2MXYflcqf2W6pgKdW48bdKvp3MMlg65xyvQ1Cw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcG7YNjko0mdWgJMAh2p47XegB1tenNUmia7tcBsgNb9ibmXWrdsSkIsZBibWHHDKFiciaCc8VBNxs86kibHRJJLDa3PW9iceMiak3xx27M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHaqnCJ4FadicA19rZmQ2C4IxJLOf6JWMIO2FHjRZoW3Ruu7RQ9JlgrpYibibmuvaI4XDvd1r9EoDAKpkR2w4D3HYOib0fMhTiaVCwc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGoiaDXMkBiaj19KNvw3ib9rrobLAhwibAficoxKQS6n0ew1ianW57nqxnoDgUnAfia8JNB3sKWvY2sLtHZvnVOUP9OrqklQhlLScMo2c/640?wx_fmt=png&from=appmsg)

（3）在cc-switch软件的界面点击OpenAI的图标再点击“+”号：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEQ18sYapkyaB5aPRkZtwkDAwaLSM7LgeqB3ETia2HjwRA464p0nd49FpvFibRjbgRM6iaeABWRfftibwib3svvbal1HXjpX4f9YLvI/640?wx_fmt=png&from=appmsg)

选择添加DeepSeek

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFS1iaOibtSNPdSgsDgs1z2VFZU0rfz0YgWs06umNJCmYbHPKWqtRgBdeBTn7AtNon4hznAnrJQl51dKVKw2w3vfBeicCWEkHbUu8/640?wx_fmt=png&from=appmsg)

（4）这里需要填写DeepSeek的API key，可以到deepseek.com的官网进行生成，或者可查看文章：[让Trae帮你全自动安装Claude Code并接入自定义大模型进行实战和打比赛！！](https://mp.weixin.qq.com/s?__biz=Mzg4MTcyMTc5Nw==&mid=2247491531&idx=1&sn=c8fd202a56be2fea1c666cc2fb075b59&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHDvAKJQHCaha3snl3Mnw6bTxaAdUxwFhvBdZTjp9R3ufibLrnFBbCCKLhZTCm0KlZrDiaG8T4uLR2WEZr2icDox7iabgBibb4s5BGg/640?wx_fmt=png&from=appmsg)

填写完成后点击添加

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHVeLTSsTYY1rWD2xjOqV9DdP0jXkSFSTBxMZTTqxYruyCj58iaCbTmTJE4INYbJ0pNh4GgzOPA3jX3FaHZhJ8t0YL5HfeCQtH0/640?wx_fmt=png&from=appmsg)

（5）开启路由：
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEcu6MHxGsGE2KOaGrC0YbGaWgV2j99t62r3Svyns6YU8pNtdBUREgaZ5Ohsicscs212Wx9ASyLjfTrEERWPNks4ibiavcP1ZiccRg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGjDtTmjnY3vZSAcSz969ogibhcCqgOoWhbCEzIgCsmkRzCg2z3viaLAzlrSEXTOgXfsHWvEs0JSD7W8jhrCfPsaoXcmk17eCHD8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGajUDyq09mgNOJcNRYssOUFibibwd4hcQgebiaIicGro8yLYU8MHpa4HfiaZwJEibbiae359ibetcszJEZcG4PyJlb8V99ASp13Xq3vyM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEQjdPFF7SKxibgGcJdy7icgzs5n9Cmp9ibWOkaORAZbgursOPRGgCtia1ADBEvIGIqBibDeymfv0mSq46jp76qKV4E3a2GC9vmJHFU/640?wx_fmt=png&from=appmsg)

（6）之前有安装claude的报错，现在可以通过这种方式解决![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGWt2ib9mYAFAYfw0BpiaQWPn40PYTrAfrXQPk9XylTWPddvPUlJeuGnOJ3VomHbibe2py32uOtgfRrLJsJnswyn72sPMGuugDrbQ/640?wx_fmt=png)

也可以同时开启，直接让codex可用
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEpRGHGIRHJbUzmVfHl4XWLeSdzWyxFmUWibC12MNCSSLPMFwrDmwlnLRrLrcQrN7krhnYNSTsiabukiamv8kOPjjVYGtCkv6eNfA/640?wx_fmt=png)

返回上一级可以看到正在使用当中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFoTo4Uqj8apibiby16fwx1SHzpkV8xvJiapQX5VlgC90Sb6zJmnZfP1GXialUD9ukrZmYYopRS4haLiahib6YUYo48S1Tu9KPVPYZIQ/640?wx_fmt=png)

同时cc-switch也提供claude登录的绕过，之前的文章大家反馈说claude的桌面版使用不了的问题，可以使用此进行解决。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEBAXH5U1fLqmPrnboQEbc5JQibnCqxaX6f9l5OwYCalqITN8x0OygwhXHXH0ONjM4Yl6JtFMvaYiaPWkqrg7Oq82hFiaB7QFzTDA/640?wx_fmt=png)（7）配置完成后可以启动codex进行验证，这里我们启动绿色免安装版本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHkm763RwPWZYo5OIu2mjNgvuVVMZLEkSGBUNyHSZBibEsZfcTe4oeMvgAATkpDhEhdyxKxc5jpiaiaIpurh4ZLDxSZeMALnoQV3g/640?wx_fmt=png)（8）但在在运行Codex.exe前先重新启动cc switch，这样配置的大模型才能生效。

验证：小谢取证公众号是谁

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFBC8jPHKrlSbBbAdJt4MctJOd2xjBgiaSbpeMYDKVMlW3htcx4ISXvKjmPIGy7ibYlRKg1LDK0NUHhJlNah9dA6icKfic23BW2HJ4/640?wx_fmt=png)

（9）但你会发现每次需要进行命令的调用或者操作需要跟你确认权限。
所以我们可以设为最高的权限给他。

选择完全访问权限：
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGvNfBjfFIqoNKHxufGic9KbpqPK0tib3aHib1pvBv2fbMkb6chHT5Ehz5vLDHcCsNib8krltQ8ObwrsWPrx16H3WLkTuyBOtQpxSQ/640?wx_fmt=png)

选择是
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcG0B2FrfpNgAmJicjPrsE5HladJOJZWbSwNodjDMZa8BnTSdibzr7fW8EhjibqpbrfFuCNIicRibJ8BNQFWhj5SD79KkZTXQC7IgP9E/640?wx_fmt=png)

生效：![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHRibKVdsicluticOp9yU3AsfKIUMTTuYLicrkI036bKqicJS2wA7X7fn1YkmWnwibFe2s3UkrtXgAiccQKP58ZG1KBUT4gkE4soXTO4M/640?wx_fmt=png)

授权成功后停止对话再重新问一遍：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHCz3AKNSMxss6ib8kT9VHRX2Au5J79CgodJ0YKu3fVggmpb5Obwv9SpZT7R3BQVEvic9ibUXnRe...