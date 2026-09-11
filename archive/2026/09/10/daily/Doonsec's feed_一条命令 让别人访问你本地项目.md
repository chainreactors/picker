---
title: 一条命令 让别人访问你本地项目
url: https://mp.weixin.qq.com/s/3PyXAsiCgKCM-jutY0phwg
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:50:04.034652
---

# 一条命令 让别人访问你本地项目

# 一条命令 让别人访问你本地项目

原创

大表哥吆
大表哥吆

kali笔记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 在日常工作中，我们会遇到将本地开发的项目放到公网，为他人演示或者测试。如何让别人能快速的访问你的项目呢？让我们一起来看看吧！

# ![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorfgSXVeOM7EvJ0KEEiag7ENKTjLibYEdQLuxwruWk8YFWib89z1dlL0uDopXtLGWmml0OcMfLx5ZApibJictdaz5GJoAmUnRiaeZDbAc/640?wx_fmt=gif&from=appmsg)原理分析![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBord1h7CnvhKunaBXfuZNianAhEokqwxkWquRqeAYdRpgtqezxLIb5PnLibKjWmibIUCB4C7hkiaOaEicSXBNNXl9aZgvg1aRxpBKD96o/640?wx_fmt=gif&from=appmsg)

你的电脑/服务器在局域网或 NAT 后面，外面的人访问不到。"临时隧道"= 一个中间服务器（如 localhost.run / cloudflare）帮你开一个公网地址，再把这个地址的流量反向转发到你本机刚才启动的 HTTP 服务上。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcpFa89ocnMjbYa41Vq4wM1udWA0F0PtVLtNcXqACmibyHoh9D1g4h4DdzgEw2rn3QsYrVw0RN5Le7BTEyd97xOHNjgRJ58CQx0/640?wx_fmt=png&from=appmsg)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBord8Uz8oWfEVeic5bdVx5ULYbahRFZccyib2Kiby9LQvwZ95ek8LgtdSR8JZtZJa43icRpIZOztLBLstZ3qJdZomiaeyk3xqEQuiafI3M/640?wx_fmt=gif&from=appmsg)只需一步![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBorf5ID5LJ6gj22g4Yt57Xtsrj4icePaHH5Ut76Qpia0RMnAa4Lx5Y68UsEMJsdc8ZDHx7c1ia3oID0MlMNgiaDn1b0iaADc1zu0icicviaM/640?wx_fmt=gif&from=appmsg)

无需注册、无需装软件，Linux/Mac/Win10+ 自带的 ssh 就能用。
命令如下：

```
ssh -R 80:127.0.0.1:8123 nokey@localhost.run
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBord15SFphUBYKFiaiaKg87vicPteddv0QwZibhfA0j9xicTZFRgbgDlrRD3JqRgqMXO0YqJfj6RQlkRdcBbgoX9tAnUbaqSFyqd4EbB8/640?wx_fmt=png&from=appmsg)

要点：

* • 第一次连会提示确认主机指纹，输入 yes
* • 连上后终端会打印出你的公网地址.
* • 保持这个 ssh 进程别关，隧道就一直有效；`Ctrl+C` 即可关闭隧道

如上，我们便轻松的将本地的`3000`端口映射到了公网。通过随机URL进行访问。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordSiaLgnnr92Elx7eI7Er8lK0NaCbO3rIuLx0sDdLD3CWJpFgibj9sXMasumJFX2o3jQibD3cJBOIBpGrdMqzDmEUTOpxUcpooTtE/640?wx_fmt=png&from=appmsg)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBordcSlS1hWd3qJttsvnxvD2NBJgPb0ojicT0tOSrC7Z9r5ibwLoFT3IvFIkdweb8cficEJTw1O1JAibicnpY2Q9cVjftcfTYzNXPkIvU/640?wx_fmt=gif&from=appmsg)总结![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorftgdkXWDHlib1PAL3UzjGr06IssuiaibvNZ265TdP0lbx0uHFQaEtrU9HtuvVKVpiaXZNDqwvaYbWjyhp1EyON3TBjRIQEzUJbgEE/640?wx_fmt=gif&from=appmsg)

只需一条命令，我们便能轻快的将本地端口进行映射。但需要注意的是，给出的url是临时的访问链接，如果需要长期链接，需要扫码注册，完成绑定！

更多精彩文章  欢迎关注我们

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

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