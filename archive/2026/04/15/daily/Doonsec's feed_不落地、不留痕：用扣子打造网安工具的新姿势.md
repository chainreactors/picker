---
title: 不落地、不留痕：用扣子打造网安工具的新姿势
url: https://mp.weixin.qq.com/s/sHxKAyq3VTRpy59aD4n9og
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:49:38.782544
---

# 不落地、不留痕：用扣子打造网安工具的新姿势

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/I8PshYBGmQ7ia6xdkDeO1o1zj5YXmVA7T6AuEU5Cu791NKspSTMM5lW1N1HEvPyLEzBic99Pib5g7kqCibCRHRAboibohmccaPHMnknTcuCbic0S4/0?wx_fmt=jpeg)

# 不落地、不留痕：用扣子打造网安工具的新姿势

原创

跟着斯叔唠安全
跟着斯叔唠安全

跟着斯叔唠安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

1

Start

最近在折腾扣子（Coze，https://www.coze.cn/），尝试把一些常用的网安工具做了“云端化”改造，逐步搭了一套属于自己的工具库。实践下来，有几个体验非常直观：

```
不落地执行：工具运行在云端，本地几乎不留痕迹资源解放：不再吃本机CPU/内存，老电脑也能轻松打随用随取：不用再到处翻工具、配环境，一个入口统一调用隐蔽性更强：执行链路与本机隔离，降低被反向分析与溯源的风险
```

    相比传统“本地工具堆叠”的方式，这种模式更像是在搭建一个自己的网安工具中台，你不再只是“使用工具的人”，而是开始管理、编排、甚至自动化你的工具链。

2

Action

以ICP查询工具为例，通常情况下，我习惯于使用tscan配置镜芯API然后进行批量资产查询

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I8PshYBGmQ7VZ9cjmO7HVabQZQsTyBQQIcwq4xr8q2ic6bI9PkZPglr4TWTwRvOlMVmK3pYjudtgB5IxqVgyZesVV7NOU3VyUricbfjhUJvv4/640?wx_fmt=png&from=appmsg)

    不过查询资产较大的话，如果本地还在并行做一些其他的测试工作，本地网络波动对查询结果影响还是蛮大的。但如果在云端扣子打造自己的工具库的话便无需担心这样的问题。

    并且咱们平时用的那些工具本身也就是发一发http请求，基本涉及不到ai交互，工作流搭建之后也不会有token消耗相关的烦恼。这里是实现了一个输入公司名称，输出其公司备案的小程序资产的效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I8PshYBGmQ565jTYedibeZqMicvnONwejgn4eRree4LoF6IGoz9qeMt9DNZ7xf7sMC07YMPgM8TSx8MjNM9qDSYPJyGrFRu7NgYsBb0dFD8G8/640?wx_fmt=png&from=appmsg)

       工作流的搭建逻辑也很简单，碰到使用扣子提供的模版搞不定的操作，例如文本处理之类的，可以使用typescript代码代替。什么？不会写typescript代码？问AI！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/I8PshYBGmQ4qUPKhCbtnVoicQNrqJpE57aBMChLnCHQLqbtceL924ianUkaxGk5EW2BJhulS9EXvz2RsAEXibff2fxVbrhhmIe0ibwZv1S88eBs/640?wx_fmt=png&from=appmsg)

这里也只是以icp查询为例，抛砖引玉。熟悉扣子工作流的搭建方式之后完全可以打造属于自己的工具中台。

3

End

🚀 **新圈子上线 | 高质量安全内容持续更新中！**

我最近在纷传上建立了一个全新的安全技术圈子，主要聚焦于 **WEB安全、APP安全、代码审计**、漏洞分享**** 等核心方向。目前圈子刚刚建立，内容还不算多，但会**持续高频更新**，只分享真正有价值、有深度的干货文章。

📚 圈子中包含：

* 高质量原创或精选的安全技术文章
* 公众号历史付费内容免费查看（如：小程序RPC、APP抓包解决方案）
* 一些只在圈子内分享的独家思路和实战经验
* 不定期分享0/1day

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UaQw8cfe5zo87XFXicicayuia9gvdmBnX6lOnSygn4NFJlzqeyxyes0uIYicDwGwh3rbAYicdwYFhK3Ang/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UZMvCajj3cxavCh3fUEdiaFHUic5nqZ0ibvAD9CcCfWUb95icfUs84yQDGbbicPNeYjVwyvcvmcP0LWEtg/0?wx_fmt=png)

跟着斯叔唠安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UZMvCajj3cxavCh3fUEdiaFHUic5nqZ0ibvAD9CcCfWUb95icfUs84yQDGbbicPNeYjVwyvcvmcP0LWEtg/0?wx_fmt=png)

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