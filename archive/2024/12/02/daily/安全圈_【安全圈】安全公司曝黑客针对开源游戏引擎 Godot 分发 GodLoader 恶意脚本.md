---
title: 【安全圈】安全公司曝黑客针对开源游戏引擎 Godot 分发 GodLoader 恶意脚本
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066356&idx=3&sn=e3124c5e2c25a853da32a4cb281ef63c&chksm=f36e7e74c419f762eaec38852c8283a5dd82c75032528035ce338cde3cb06409efdcafbc33d4&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-02
fetch_date: 2025-10-06T19:37:11.943232
---

# 【安全圈】安全公司曝黑客针对开源游戏引擎 Godot 分发 GodLoader 恶意脚本

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgDWGm44ZJhb7wjWibCgG7WNlWsiccfsy8owDYu0cFfDZ4FOpxfexasicwxgLSVnwhuFCIrsxvk3x4Bg/0?wx_fmt=jpeg)

# 【安全圈】安全公司曝黑客针对开源游戏引擎 Godot 分发 GodLoader 恶意脚本

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

安全公司 Check Point 发布报告称有黑客利用开源游戏引擎 Godot 分发名为 GodLoader 的 GDScript 恶意脚本，继而在受害者的设备上加载恶意木马，据称目前已有 1.7 万台设备遭到感染，而许多安全软件实际上无法检测到这些恶意脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgDWGm44ZJhb7wjWibCgG7WNq5f4tn7a6RNP2nickEow6LlAazibPmhDgFFyY6QhIvZqLnQicibdM0Hia3A/640?wx_fmt=jpeg&from=appmsg)

据悉，Godot 引擎核心使用类似 Python 的 GDScript 脚本语言，方便开发者创建游戏，而黑客们主要在 GitHub 等平台新建各种山寨游戏代码仓库，诱骗不知情的开发者下载暗含恶意脚本的 PCK 文件，目前安全公司已发现约 200 个仓库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgDWGm44ZJhb7wjWibCgG7WNHHrcb9u30wMwjSTDMlgzLtgmXW4hRRXFflbzfCVicQa4zZNRf8ZwayA/640?wx_fmt=jpeg&from=appmsg)

由于 Godot 是一个跨平台的引擎，**因此黑客的这种攻击手法同样具有跨平台攻击的能力**，能够影响 Windows、Linux、macOS 平台，安全公司称任何使用 Godot 引擎开发游戏的用户都可能遭受黑客攻击，相关恶意脚本至少波及 120 万名潜在用户。

对此，IT 之家注意到，Godot 游戏引擎的维护团队及安全团队成员 R é mi Verschelde 回应称 "**他们已注意到相关恶意脚本，不过这一脚本影响有限**"，这是因为黑客不仅需要提供内含恶意脚本的游戏代码，还需欺骗用户下载经过修改后的 Godot 运行库文件，之后将相关运行库文件和 PCK 文件放置在同一文件夹中并启动，才能感染受害者的设备。考虑到相关过程冗杂繁琐，Verschelde 认为，这种方式并非黑客的首选路径。

***END***

阅读推荐

[【安全圈】重庆一学校因网络安全失职被处罚，电脑遭境外黑客远控植入木马](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066343&idx=1&sn=dac289849aa3002172d66bc0a7027e09&scene=21#wechat_redirect)

[【安全圈】“插件变‘木马’，上海信息科技公司因流量劫持行为遭判刑罚](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066343&idx=2&sn=efea10af979662c9eb148230f5e61f53&scene=21#wechat_redirect)

[【安全圈】“黑客”侵入计算机，为获利终获刑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066343&idx=3&sn=019baa0ef97c0636f6d9165d1a1443bc&scene=21#wechat_redirect)

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