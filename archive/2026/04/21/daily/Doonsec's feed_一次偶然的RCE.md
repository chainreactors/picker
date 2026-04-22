---
title: 一次偶然的RCE
url: https://mp.weixin.qq.com/s/21t2qeAnAaWbidwusbWYSg
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:39:50.217917
---

# 一次偶然的RCE

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/16lHuWzRRdvRwhphJhxl2pdnEo3H8qL7LhHafvyvrpoA8s2UGSQhZ9InPoe6AnyS2XrueH1bKzyWYibDwaFfLJBo0V2aybgv56peUgcAySj0/0?wx_fmt=jpeg)

# 一次偶然的RCE

原创

private null
private null

轩公子谈技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近没什么新颖的素材，没有素材就不能赚流量费，没有流量费，就不能吃饱饭，吃不饱饭，就不能更新文章了

同事在项目上遇到有一个有意思的洞，RCE 漏洞。于是就给我这个素材，进行分享一下。看看这个洞是如何发现的，跟我走吧。

资产是一个小程序

手机号登录默认注册，于是先反编译小程序

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRduwXZt8yFJyKpanDcWujdRBuHstDD35BP9X1yfJDAM9IC376YTxS8ED2AAykaWPN4IAia8veIo552MHlQL9jhLwP7nkoocFwoVo/640?wx_fmt=png)

方便读取 js 内容，进行格式化操作

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRduHiatxGWAsD7IyEIMyNyEVjYcicJHdUjEtqjC8qRdlOKrwkymaDKUz0NgnncKrIXHm3sLTZCz2bhx9vA3qiaicf3aictvOPiadKHsm4/640?wx_fmt=png)

直接让格式化后的 js 拖动到浏览器里，使用插件提取里面的信息

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdt06oKwKN8cTszFuYs8G2Ltuv4jia1ibNVV9IagORFSmgVYX483Oic3bEyktrgT5dpQG3QQibZyLneDg91IphwjVa1ickr3yvjjTia7A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdseNrpoP5I6iagokpEMGIYLbcXP4bedHOUz3HA1Joeq0tpx6La0HP61xzVvN5yLSje7yBcUcT20AIHzZUQKB4kicFUSoFnrcpfrY/640?wx_fmt=png)

大部分接口都是无效的，只有少部分能够使用，筛选之后有效接口为 76行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduKgs71fbWR5zXCURWpkklbHZkTZXz7vJtQLnkF2ulFtJ0oIdYzLQichftSw42J0RDEJxDYXibfw000PhGhWKkIvptm03UCIqE9M/640?wx_fmt=png)

先对接口进行未授权测试，放到 bp 爆破模块，在进行接口过滤，去除删除接口，等存在风险的接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRds18NicFTAAQMQjTkwuUKPBGVJ2eF1rS95JrBicMFaNXJB8gzYNNOj0hjLJKKDS9vYy8dCrnicK0iaSkoHwgaWo2mLzXKLFgmVHZss/640?wx_fmt=png)

不存在此等危险接口，那么直接开始跑接口

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdv4SHt39XZffV3BibcVHefZkf199aRmBGUPmVib5hK16jhmqk3Vcw3vHkIFJhaficibrMGR9UoXzUWUEu5HyPcjLIicT1h84W2L2hW4/640?wx_fmt=png)

一半是GET 接口，可请求静态数据

一半是POST 接口，需要参数

instance/executeData 这个接口，乍一看就很亲切

熟悉 java 反射的师傅们应该不会陌生，instance 通常指代对象的实例化过程或实例本身

小程序的系统，为什么会出现这种接口呢，我们带着疑惑去 js 看一看

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdt3cCUezliaics8hMYylhYgoQiaSibibI05KSVOwvA4xgMfJMJPetzJQ5Yfpiboxpb6HCB0phkygxcrCibqtE9QUfvYVicsZMXqMRQvRzI/640?wx_fmt=png)

肉眼可看到，需要添加两个参数executeDataParam 和executeDataScript

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdv6kw5YkXqXYxWYflfhB9ksPNg1Sic7ibfWQrRqYriaANw8MIUxricTpk2IicibudYFYeaYC02oJKTj2tSqDsPwoRyibSE7qQoDp2KSEE/640?wx_fmt=png)

bp 构造发送并没有什么问题

代码给豆包问一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdvfC4ROHibnwUlRyibG4oqDjxI71d0DNP3GgwlpLykoDqgJZOBtibcreapOjGKooicgKOru8j0pHdvo6IZxgicxHBx0GTDI2oWkI2kg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdvkv6sDtPgriaicSibCKbKjn2GwQ5RPRzicQKCNpY0HMbXZB701cswib1rOSkTCcKPqbV7PIgtI3CHzG2ibGu3tXXeJ9gvEnNHRAND6Y/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtyNzqrbolhAf7REsf9857kN15ZFEJd0LQ1Gn5UgqrTMbpd7XHa1lia7j1Qa7RvNbbKVX7PBl07Eo4qfhpeIibAZ2OwB71Fowicvc/640?wx_fmt=png)

复制豆包给的参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsrTbj85PwQqtpHVyzbxOnbHFYLHCVkMicmbYWDwtDrcJgdsp1GPHicJ0EC3icw6OQg8om5jV0FyibOhrroH5rvW9VJamY5QvuhZNk/640?wx_fmt=png)

想到 js 代码中存在 return，那返回一个 hello 试试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsII5vriaUq10mPRiaY75CmUcRoltPrC3o4iaTicssI7ouJS3EAJaTblpUTLbK5Yb2LrqDTXSo0eFHKJ4gP4iag6uEG73tLUZERZcD0/640?wx_fmt=png)

成了，说明是存在问题，总感觉很像模版引擎注入

那么让他执行 id 试试，豆包在这方面还是不如 DeepSeek

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtdV88lnHibY9KOMuCINVTyN4MQyT6aaZfNRnsKgxVicZJwHBvl4YXtACWq48jpD4K9EyMgswUjWYicGwrpiajMpgPwP2We8JeUZOA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtWnJIABp3bjHZnOvDXnM0xWibygWQHuzvT5tr3mibQpR69yMC0JWzy0dK6VDOXHmoVDy5GxwmlBmFeyIcqZkqKlO16MlFaBeqvs/640?wx_fmt=png)

需要手动添加 return，才能返回结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsBSapyB9r5ibicicFH68FPwbddb6FTXI7KnUTRPCqBpjXSF1yYuNqBK2gfgCiarRMomHA7Y7rkLF00c0lsr361HjmgRpBOkSx0V38/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdtyoJVyGIR2rR4ibPLllOgiavtRQ0XL7BSeq174KngF9Vv43oxcxobaiaq2a9BI0VKHUhO9ybicU9fdspylibFRicrEllUdnvLsMrYyM/640?wx_fmt=png)

豆包给的则是

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdvhdV6Yf2eUNoHDG2hXqBKe94tCVmOJQpJfJhWuctmGYNTmGksTic8wRCbJKxN3kN2q9IStlKj9MsNaiaNbmIOiaSjDJDj2AzRuibM/640?wx_fmt=png)

两处的不同则是 DeepSeek 用的是 var 当做变量关键字，豆包用的 jdk 的变量关键字，语法不支持所有无法执行成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduInyQE6CvUhrfYXXfHQbUxLjgTSJcE6gCuoHxycpWWLEzfib9QqYtjiajHbxibF3LfibKGjj7FFlbvdedUmFvr2I3fyQA2MwXuULE/640?wx_fmt=png)

执行了ls -lh 发现竟然是 xxl-job，不过总感觉怪怪的，应该是二开的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRds0sANPXp29dseSLibMW6icKJYn1F6QfXVlDLibgQkEzfVzRqibsibMlmCL9hxqPSJVDaKJEp3cSzwFujzIicCfkWch7mLZp3iao1WPrM/640?wx_fmt=png)

到此结束.

预览时标签不可点

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