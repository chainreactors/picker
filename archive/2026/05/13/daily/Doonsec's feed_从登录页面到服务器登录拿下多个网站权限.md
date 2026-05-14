---
title: 从登录页面到服务器登录拿下多个网站权限
url: https://mp.weixin.qq.com/s/gjr4EXjVLRl5_O8DE0MAtQ
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:43:04.717405
---

# 从登录页面到服务器登录拿下多个网站权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/16lHuWzRRdvkF7HZhmRkpKz22YWyvoUzSVhibJh6iaMEiaC71P1ZoCem2NFUazbm1kice5tNhORPR7WyiaNke6Cxrdj6kwuUIBDULktcZA3CZOeY/0?wx_fmt=jpeg)

# 从登录页面到服务器登录拿下多个网站权限

原创

private null
private null

轩公子谈技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

发个库存，保持流量费代言，赚个酱香饼钱

老早之前，领导姐姐甩我一个有意思的网站，于是我便来玩一玩。

打开是一个登录页面，朴素如花，白色点缀这绿色，乍一看就很安全的那种配色。

初次相遇

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsVsQYHXRvFY5cNHmbGVqgtlWn6cOgTe22CEgh1VhpKibqt29OfF0vQ6lHbX0G4nrSfic6cunLiaMEoxcKwiaqhIhdaFxK1YXLATfs/640?wx_fmt=png)

但是我来了，它就不安全了。因为它的强来了。

查看熊猫头，竟然就这几个接口，看不起谁呢，于是我用 dirsearch 狂扫，竟然没出东西，太可恶了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduASJ5B7DN6HR19BbFebdR2lWlRLAzON2icU2o4ofr4zQt5teha4jxIabibyDw61JVy43xIBVLhPAJPAg1iaibaqI1JWs8y173qYHM/640?wx_fmt=png)

刚好没的验证码，直接爆破一手，刚好弱口令进入后台

进入后台乍一看有个命令执行，这岂不是美滋滋，说不定又可以 rce 去群里装逼了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsGsyUA0RzJYfeaVYK3vAIE6ctiaEc5NltQanJmwxhFwLZdoNEITnzLa6QYcwTd214gdDYB1MIJBDicMCcCuSFqVnYpAXKpqEpMM/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdsYO6WIQEB3qTg3ezk9eTulEmeZmDr7KoeWV84O2UOaytapicAeicP6xHlSnY3ca88jG8mj5JM7w6vbRibsEookgvZHjsXcBmgDB8/640?wx_fmt=png)

很自信的点击新建，然后创建了 dnslog，看看是否能收到记录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdu9Ev4rTKAOkooRH3huAzYeTRib61qHSZHRKQee7OEHsZa8FZztIVABxLknia5icwCbAuKgEENg8Syz6DOTL9KMO1AyZBfgzpVkVk/640?wx_fmt=png)

等啊等，等啊等，等了半天，也没收到请求，我寻思会不会有什么隐藏的参数或者按钮，点击才能触发，然后我查看熊猫头，发现接口变多了，筛选命令相关的，只发现了新增和查看，没有触发的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtBIomAIpccPXiajlndZNe97V9yU1t9wXFq7ho1JfF1NxfyM5qQ27Bp4qlOM8Y70spCLY8TDUaIYqSaVIhRMgWjxHp2faTeia3F4/640?wx_fmt=png)

那这难搞啊，这个功能的作用干啥的啊，于是就查看源代码，看看 js

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdsDrp8NzVyuF01UsARvUPHp3zBhsLmjicsH7ibD4ZzhtSabznqkleibs4BIqLLGAWaaCStCQ3XYdMt5Znuh66GZU8w2OdqKKmsv9s/640?wx_fmt=png)

下载 js.map 还原代码

发现 js 里竟然也没有，翻到最后发现有上传接口和下载接口

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdteWlm8rXyeOU3QNTIc4WjibKfFmkTgFdYHfOZkzaibHvUFmOx5M2wD0S1xsAlVFuYI0LVAUjN30UYlwSqZublEqhwv8L0ezskZk/640?wx_fmt=png)

但是熊猫头里面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduXY8uhjwB5icFyfib2KibGjzlh1GL3sibxhIaFmfibjfIxJVkQjDDRiaaIB2D3God5pTRibH0Dnych3QczcZjGqd4Zabzzm30eUvqPf8/640?wx_fmt=png)

竟然没显示 file 相关的接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsBBG2x1icPQa1NvhvmIzC1vP0lWl736rsYmOMrBLbBY79oWngTQNZw9HDwGUjibduoulp2BIvNu5mR7icI8Qriadm1lUDCXU9PYsM/640?wx_fmt=png)

只有这两个，好奇怪，竟然没有获取到上传和下载接口。

上传接口可上传任意类型，但是没有返回路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtSmu5kk1NVbeXNb9Xr45GriayXRSOccOmzsv6Ll9UWLmJGtgwnEjmENPzbUnJLMBQ4s2wWSs5JYv5Ce1iaZjLAe80icedjJBV9vQ/640?wx_fmt=png)

站是 php 的，但是访问接口就变成了 springboot

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdvOPjxibsEvJuWOLJa3x0LplpjiadaB55k47qxBIxHD2eA9XicuKv2upLgibRyEIuFNSjmUP4IvX58Tq6IRG4yVB84OmaiaBnVdNCn8/640?wx_fmt=png)

放弃了，看看下载接口

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdu7fxXiaUYHFe9V5iac8NFJibD1Tu3gWWicaTcxWcdoBTkP9qdhOlsqrEC9weiagKwNnb407nUpStYNvBWKewLvnCDeAnT3w2AqAfPc/640?wx_fmt=png)

成了，那就尝试读取历史命令，看看有没有什么重要的信息

我发现了，既有 java 也有 php

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRduuulYkdT7h6rlnV5L0Qd36upfgTksticsLlhYoKbm8j1FMgx0unvf1D6KNYaDF6ibGQXBE3t2ibtD7aMgzxCT8vYUCIbur4CvZCg/640?wx_fmt=png)

嘿嘿嘿

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduhuquUJiaQSxaCnZVJHqvAtg3tctDM1ianEI2BRTHBw9EC7ibIE3oaWo1YgsVZH5Pm2HGjcaaAPKkLQSDKjBzp2yaE2xmP7ianwcg/640?wx_fmt=png)

没想到吧，我也没想到，真有账号密码

看我阴他一手

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtpPT3svrgiaibg6U8QCJpVnXLka0a2oibHAlx1VBicXaxuYpzPLm3icWvnVFFQAgVVU4KBcjGYBia6Lv9VcZDNw4useHz7NAguXBD1Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRduibT3ljiayr41kc751AfbWniaHw0dFylicNR8iaGdT9TiaVqHUQWpL1p4reKzOWniaS1CN63amhu3w1WZ1cS8cyic9X8T0aqljyvwQFRw/640?wx_fmt=png)

竟然是七个站

第二种则是获取 root 权限的账户信息

读取 ssh 配置信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsCQwXHaJzVnnpQZWJTUJK5zCypzVXEmooGI77nEWhsib0x2TBYSloBzRpiaPib2jpm2lPBOElCf4JL69YItzwOYkvkofT945sic8A/640?wx_fmt=png)

有密钥，直接读取私钥，免密登录

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdseGH1DK8vG1kUhjoUhNsYTvrAibCCjMKM5LVl3aZpR9b7rCJOlk6stxwJZ2tBIuW8n4UUU2dib8bN7Br4LcVviaOKXMY7WKTRSaw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRduN0qPblMjwf6pciajaN8iaAib6sn82RA3NrL8AMibaiczTxZ5mERd3qzqt44JQclveRictPZHQG0LGewA1d3kgXMypMxP1wUoayeXxQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/16lHuWzRRdtwIaAbgTBGQUN80usicQ0RRzlwpsib8HJgMEyOUlDclfGrmWsXF2JfVsZR8v7vP8hlUPZFrIdYzcib2sWD6tjzvEsauKzQSVzDP0/640?wx_fmt=jpeg)

美滋滋啊

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

轩公子谈技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

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