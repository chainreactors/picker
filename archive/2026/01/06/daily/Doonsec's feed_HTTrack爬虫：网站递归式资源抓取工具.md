---
title: HTTrack爬虫：网站递归式资源抓取工具
url: https://mp.weixin.qq.com/s/ttE_JuGyCmUqcValbvSLIg
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:27:08.406965
---

# HTTrack爬虫：网站递归式资源抓取工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwYQP6f9lXRicEC34Eb6GGIFyME3B90G2KIYyOOTzvHB2WicsibErD65Sdw/0?wx_fmt=jpeg)

# HTTrack爬虫：网站递归式资源抓取工具

原创

网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·["手机版的kali"黑客工具：Tool-X使用和安装指南](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485663&idx=1&sn=95cbaadb12dcf74077ec6e0bf8448c11&scene=21#wechat_redirect)

·[pentmenu:黑客必备实战流量攻击工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485644&idx=1&sn=ef9b011a20e30cea78592357736ca177&scene=21#wechat_redirect)

·[钓鱼工具分享：I-SEE-YOU获取受害者地理位置，实现物理”开盒“](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485643&idx=1&sn=2b298e43ac23c9b7ded4c9cddd5c1d0b&scene=21#wechat_redirect)

·[CTF-FlaskSession的cookie密码快速爆破工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485611&idx=1&sn=ad4273b85b9685bb4c94beb2fb350701&scene=21#wechat_redirect)

·[ZipCracker: CTF-MISC必备之zip伪加密破解和密码爆破工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485610&idx=1&sn=c6b44903980d6cc5c81df5c1e5e00644&scene=21#wechat_redirect)

·[Ds\_store\_exp工具一键挖掘备份文件泄露-CTF文件泄露-漏洞信息挖掘](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485591&idx=1&sn=25034db5fbc182de0d40bc971912ac08&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**背景分析**

![How To Use HTTrack Website Copier Tool](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwaFXdq5Vu37XIEBP5j8eSp1fCvJDlJoeYocrUS53MXibLFt7ZYe4duoA/640?wx_fmt=png&from=appmsg)

      HTTrack 是一款基于增量式镜像爬虫技术的开源网页离线下载工具，支持 GUI 图形界面与 CLI 命令行双模式操作，核心功能是对目标网站进行递归式资源抓取，可自动解析 HTML 文档中的超链接、CSS 样式表、JavaScript 脚本、图片及多媒体文件等关联资源，并按照原网站的目录结构与相对链接关系在本地构建完整的离线镜像。该工具内置断点续传机制与智能更新算法，能够记录已下载资源的校验信息，重启任务时仅对新增或修改的内容进行增量抓取，同时支持通过正则表达式配置资源过滤规则，可精准排除视频、压缩包等非必要大文件，有效降低本地存储占用与下载耗时。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**安装**

登录官方网站：

```
https://www.httrack.com/page/2/en/index.html#google_vignette
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVw06BZ1XPKUCKJPAgjWOaajz4552BKS5YzwN1duO5fgJJmelm5P5fg5g/640?wx_fmt=png&from=appmsg)

选中框中的推荐版本并下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwn6mibyXiavTP0Ut93OiaVUbY0uPyLPyRsafHicUe1EqvibrFZXRKvWNBGPg/640?wx_fmt=png&from=appmsg)

点击安装

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwrcMEEy5HyHd7355eA01HFGM6WVbgISG2G8m4OWFKdD34uszBLBCewg/640?wx_fmt=png&from=appmsg)

接受

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwzktneohfWfAxeJeKwyn8t0EgqB9GcLBuhEvnicvzlJZkhXPr3dY7APA/640?wx_fmt=png&from=appmsg)

默认选项

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVw4A0A0LevBG178I7T0UxD6yRpHreAaibFjqPJqgKvH2S8XkPLecVQRdg/640?wx_fmt=png&from=appmsg)

下载即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwXvYowRCtrw7fR8jSJlN2Ph6EBEvFyfbgmyMymibFo9JK3nPzZsazPpA/640?wx_fmt=png&from=appmsg)

这里选一下语言

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVw1YMoOANHhD3qfO3z7DOfiaIVib89D5hiay3ujWp5kOmZR39ZToWQ5BDWA/640?wx_fmt=png&from=appmsg)

这里创建一个保存克隆下来的文件的文件夹，后面会用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**使用演示**

打开

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwczhVUATibBk291ibBoOfZribzPkHx9B5GwGlAq1uOfYSgyA3nQ9wfV7Ow/640?wx_fmt=png&from=appmsg)

这里可以开一个新的工程或者继续执行以前的镜像

直接下一页开始新的克隆

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwPRQr91N3RTTSEAgCsTiatF2R2Me7qxXiacbptykWc7xWABjhhCHIDSCg/640?wx_fmt=png&from=appmsg)

设置好名称和位置，这里的位置建议用前面创建的文件夹

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwphheaJqYsFfEF0fRGOAHSnC8L7ibvjSPmxEkjgNWw9nICwyApz6rg5g/640?wx_fmt=png&from=appmsg)

设置好操作以后添加URL

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwlOdQJIN51vn7pdwbOaIFIvA9UUWk6b4DVlyuUIbC5fWqfQFjhhhoQA/640?wx_fmt=png&from=appmsg)

这一步一般默认就好

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwKvnIJaCXp0Pibce7Adia3gePl6uiaL2iasP5dZIInLNvWAtA63JElMOjeA/640?wx_fmt=png&from=appmsg)

开始下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwGUjDGibNq2pHmtJmNoTtg8DfUic2Sat9nxwfO4kziapvXiajcowkFFLfog/640?wx_fmt=png&from=appmsg)

完成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwibia155dkIkOAXTibzM1G5nbw7iaezKq5FGsKG9SDYKFmJR0auRiaSERictw/640?wx_fmt=png&from=appmsg)

之后找到前面下载的文件夹，找到index.html，注意这里不是http里的index.html而是http/1的index.html。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj2tZ0ibc8QCeIyFn0UmzhVwjSiaL2LVGeNqw85M9dQryD1ROibPvWQqKMGtR13tKy7NAWiamqzVohRvw/640?wx_fmt=png&from=appmsg)

点击打开即可

官网地址

```
https://www.httrack.com/page/2/en/index.html#google_vignette
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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