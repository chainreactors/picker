---
title: 【安全圈】Windows 11 24H2剪贴板历史记录无法正常使用 但有方法可以临时解决
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065331&idx=3&sn=b1347862642950fd691835800661fa2b&chksm=f36e6273c419eb6501b6ef498d734836143bff084e25da364d07410fa621c965d3d276f7e909&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-19
fetch_date: 2025-10-06T18:53:38.911728
---

# 【安全圈】Windows 11 24H2剪贴板历史记录无法正常使用 但有方法可以临时解决

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg3icicroLnsrzY1UNibfRPm923gAvnuoupserDofdj25tBCNu1MibqI7dIzeRTEJVCPIXvhPQPyL1Rvg/0?wx_fmt=jpeg)

# 【安全圈】Windows 11 24H2剪贴板历史记录无法正常使用 但有方法可以临时解决

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Windows系统

本月初微软发布 Windows 11 24H2 RTM 版，不过该版本目前已经被发现存在多个问题，按理说这些问题应该在测试期间就被发现并解决才对。

已知问题包括西部数据 SN580/SN770 升级到 24H2 后蓝屏死机、SFC 命令始终显示系统存在错误需要修复以及有 8.63GB 的更新缓存无法清理等 (但这是个显示错误)。

最新被发现的问题是 Windows 11 24H2 启用剪贴板历史记录后，复制任何内容都无法在历史记录里正常显示，这个功能异常影响部分依赖此功能的用户。

剪贴板历史记录是微软在 Windows 10 Version 1809 中推出的新功能，该功能默认被禁用，在启用后复制的内容会被记录下来，这样用户也可以通过 Win+V 找到之前复制的内容，但如果重启系统则未固定的内容会被清除。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylg3icicroLnsrzY1UNibfRPm92bx8pkE4afZ4KQMA15WwzEPeADSKHyqxu7ia4ZQ2tSLXgMtYAf1m46QA/640?wx_fmt=png&from=appmsg)

在 Windows 11 Feedback 反馈中心里，三个月前就有用户发现了这个异常并提交了反馈，但和大多数反馈一样这并没有引起微软注意，于是这个错误抵达了 RTM 版。

值得注意的是经过测试，剪贴板历史记录无法工作可能与某些特定的模式有关，通过修改设置似乎可以恢复使用，因此如果你遇到了这个问题可以尝试以下操作。

**下面是临时解决方法：**

1. 打开设置、系统、剪切板、开启剪贴板历史记录
2. 如果「建议操作」是开启状态则将其关闭
3. 不需要执行其他操作，此时复制任意内容并打开剪贴板历史记录进行测试
4. 如果依然无法正常显示，则尝试关闭历史记录后再开启
5. 接着你可以根据需要选择是否开启或关闭建议操作

来源：Windows 11 24H2剪贴板历史记录无法正常使用 但有方法可以临时解决 – 蓝点网 (landiannews.com)

***END***

阅读推荐

[【安全圈】高调的后果：频繁发起DDoS的苏丹匿名者两名黑客被逮捕并被美国起诉](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065297&idx=1&sn=fa2a4aa36abffd67179e9e7c2f8fa045&chksm=f36e6251c419eb479544d109a9bff01089e47a68f2a93205c5a8b24617186c76629c9768e469&scene=21#wechat_redirect)

[【安全圈】X/Twitter最新使用条款强制用户同意授予内容训练AI 如果不同意则无法使用X](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065297&idx=2&sn=bcc275e3432942ddac41ebc9be889312&chksm=f36e6251c419eb478594055e38af33f40ade65f17b7b77b1ed41b08141cd7943a3c989955e45&scene=21#wechat_redirect)

[【安全圈】SolarWinds Web Help Desk曝出严重漏洞，已遭攻击者利用](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065297&idx=3&sn=763d27a5148619b21d8a21de71663c4c&chksm=f36e6251c419eb47fce614b9c2353cfdc1ca30e5dc890827e6e25466db25669bd30f6e9ca3b3&scene=21#wechat_redirect)

[【安全圈】谷歌：2023年被利用的漏洞70%是0Day](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065297&idx=4&sn=6553ac6cf6c694af3a1a0522d91e551e&chksm=f36e6251c419eb47d1871be661931a6925259b6104043a45226869c6771428e3a794d49dd5c3&scene=21#wechat_redirect)

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