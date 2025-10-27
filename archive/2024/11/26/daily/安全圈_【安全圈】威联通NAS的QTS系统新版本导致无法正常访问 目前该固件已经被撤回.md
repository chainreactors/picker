---
title: 【安全圈】威联通NAS的QTS系统新版本导致无法正常访问 目前该固件已经被撤回
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066218&idx=1&sn=a4d403fd36bee9add5a2da4f1ca2462c&chksm=f36e7deac419f4fcda3b9182ef4c8b2f7899fb1d107b5c81e213e7e79e62ae9a1b71b65a3114&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-26
fetch_date: 2025-10-06T19:20:39.529918
---

# 【安全圈】威联通NAS的QTS系统新版本导致无法正常访问 目前该固件已经被撤回

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj1onmGQXCMYucl4PTjFia23DgDuibUF0cvBkYnV98oh0g1RcugUPpPfUZl0nIibHq9KcRbnDktC30Rg/0?wx_fmt=jpeg)

# 【安全圈】威联通NAS的QTS系统新版本导致无法正常访问 目前该固件已经被撤回

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

NAS

NAS 设备制造商威联通日前撤回了 QTS 系统新版本 v5.2.2.2950 build 20241114 版，该版本在更新后可能导致设备出现无法正常访问的情况。

据已经升级的用户反馈，升级此版本并在重启后无法连接，即便重置系统后仍然显示登录凭据不正确或账户不再有效的提示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylj1onmGQXCMYucl4PTjFia23Q7tiaWZgddH35pvibpRfJhmGtcOTpZXCpb2ALoDiauS3mJV5sHtX81EuQ/640?wx_fmt=png&from=appmsg)

部分用户还会看到：启动系统时检测到未经授权的更改，如果能成功登录并在启动应用程序时则会提示未安装 Python2 的错误提示，实际上已经安装，并且多个核心应用程序例如文件和资源监视器都无法启动。

还有些用户更新后发现 SMB 共享驱动器也无法正常连接，这些用户只能选择临时回滚到旧版本恢复各种功能的正常使用。

目前威联通并未就此事发布详细说明，不过有支持工程师回复用户咨询时确认新版本存在某些问题，同时这些工程师透露这个新版本已经从下载页面删除。

威联通工程师表示：我们在某些 NAS 设备上遇到了与 DOM 二级分区相关的 5.2.2 更新问题，开发团队的建议是通过 Qfinder Pro 工具将系统降级到 5.2.1 版。

所以如果你也使用威联通 NAS 那暂时最好不要升级到新版本固件，以免升级后也出现各种问题影响使用到时候还需要重新降级到旧版本。

来源：https://www.landiannews.com/archives/106781.html

***END***

阅读推荐

[【安全圈】太空技术巨头 Maxar 证实攻击者获取了员工数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=1&sn=81e535202f431485c12dac88cf705ffe&chksm=f36e7ddbc419f4cdfa6b93222991880723ead5b1224f5aea3c430d89ee2ad3f9ea5556553fc9&scene=21#wechat_redirect)

[【安全圈】微软公司推出 “Windows 恢复能力计划”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=2&sn=6d88527a3838dd59d8bbccb332540518&chksm=f36e7ddbc419f4cd51a855d822237f84592f66ad951174261234f7641e5c6bb1e6cd2cfcacca&scene=21#wechat_redirect)

[【安全圈】苹果解决了两个被积极利用的零日漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=3&sn=98b7c0046c725ff8299a89a706c8ee43&chksm=f36e7ddbc419f4cdfd1a5b1325eeaa6a76fad3e86c3a04d39a3c93255a412bb3e8ee77745d9d&scene=21#wechat_redirect)

[【安全圈】微软已通过更新修复Windows 10安装商店应用时出现发生错误无法安装问题](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066203&idx=4&sn=fa5c5885a0aa428e589410762dd813ac&chksm=f36e7ddbc419f4cdd12380c085a00117007aeacb6e8ac0816c71f80f4a0aa82a15a7f149aff5&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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