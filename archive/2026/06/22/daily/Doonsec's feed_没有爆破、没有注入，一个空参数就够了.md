---
title: 没有爆破、没有注入，一个空参数就够了
url: https://mp.weixin.qq.com/s/ybsn73FJbgATmE6mTUtuzg
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:24.199434
---

# 没有爆破、没有注入，一个空参数就够了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/72I8gAalpPVsoVS7DGjuMQwa84YRiateXicoKFup9KEEbNVbIp92znSLqkYicoAjRNdUI8mRC1c3CGKqNQVnYyIo8BWoFyVzchFAR7wsp7ydwc/0?wx_fmt=jpeg)

# 没有爆破、没有注入，一个空参数就够了

原创

pippybear
pippybear

安全无界

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

声明：请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

这是之前的一次授权安全渗透，目标是一个监管小程序，也是挺久没有测小程序了，话不多说，直接开始正文。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPUbvjETl8r4icicJo5QWPoVzMVpew9BZ6gyqJFNjuk4pgUVjribFJYibpIgWIHDC7pROGPr4xibXnUWWVAShZRXbhRC6Tvhz5XSaneU/640?wx_fmt=png&from=appmsg)

直接在微信中找到对应小程序，查看功能情况。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPW99W5ZUp7pICYeriaggf53avSTXP8bKnfbqKEHD44xfoWAzktbwlMGQ682258xULYm5BZicQxN82nMuBqgoiaYDKyWjQGsib4pRRw/640?wx_fmt=png&from=appmsg)

点击进入小程序，发现功能确实单一，似乎就一个反馈功能和反馈查询功能。这任务简单呀，很快就能搞定。就喜欢这种任务了，而且客户还没有那种必须出洞的要求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPXtfbGFF5EYlKnicPzfMO5Ee3FaVYemA9VEicKkHqn8l8U155icYeITLzduUx9kibicl4zbJjU6yb3hFtmu5NRafGjfRdIoyle3lfA4/640?wx_fmt=png&from=appmsg)

简单的在提交反馈功能处测试了一下文件上传和IDOR，似乎都没有，那就再简单看看反馈查询功能就可以打完收工啦。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPV0Qt7eicDMQOmZsG3P3I60JMCByyCnUjbkdfFo4cGaCwKyVca1ZTcUUCkgBGWmTzyqK5q8mt0yianmic1ekY38fFic4rgwEF5CzGE/640?wx_fmt=png&from=appmsg)

这里似乎只需要输入反馈时填写的手机号即可，也没有啥验证码之类的。不管了，先输入任意手机号抓包看看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPUVoicGcicIhiaMTg9tvCzzzzX6mxFmgs3Mia2Lcv6iaCweicgmUcF07jk3rblOjQZHsu1QZmW3GEqkib2gNVzhUq6SoodWQYv97bsQ8Y/640?wx_fmt=png&from=appmsg)

还真是简单呀，估计不出意外应该也没有啥频率限制，简单试了一下，果然～可遍历手机号（这个也不难，找到这个系统服务的核心城市区域的手机号段，然后就遍历个几位即可），这里就不做陈述。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPWiaHFUsJXbtt4BA3vPNRDwSFH3miccmkfnOaH1bQSx9oq9PaufKyIGq3PvZTCglA8KjL4z2gZiblZsfIvSibPQf8icicvFJZsp3AVgU/640?wx_fmt=png&from=appmsg)

最后看看置空手机号试试（每次这种场景都会稍微来一下，而且大部分情况都没有令我失望，大部分都只是前端做了一个空入参校验，后端则没有进行任何安全限制），结果还真是一如既往的，直接响应了系统所有的反馈内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPWTmssYLyiaWO6oKjnkJhLwsDUpC8ZCJZv0XqoP4AQ8Vr9WpR14txJRtzouZaYjSMo046D6k3L4xGdg34rG2PUicN5rEtxt667bg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVMcDwKpfcwOcHc6OufflQ2I9wIYY3ycVgMejoGnN0ibsdPXce3sF57T4n365uHS6XTiarOQg2gjzA8ck5cYddkWkKGM1IgCp95E/0?wx_fmt=png)

安全无界

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVMcDwKpfcwOcHc6OufflQ2I9wIYY3ycVgMejoGnN0ibsdPXce3sF57T4n365uHS6XTiarOQg2gjzA8ck5cYddkWkKGM1IgCp95E/0?wx_fmt=png)

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