---
title: Re·3-1— 以分析单机游戏作弊者的眼光去了解软件中的“内存”
url: https://mp.weixin.qq.com/s/G00OAiIBXB2thYLkouxdNQ
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:58:17.147568
---

# Re·3-1— 以分析单机游戏作弊者的眼光去了解软件中的“内存”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icfnkibn16VeiaxwD9ibsczA3ia9GmoPCnRIwyUP34zY9z2wQGQsvgFnJcS9Tibib1qZpBBsx6yVF6PpOR5UPwnj1wmJYOyBqlrLQTafdEKoHzAYDQ/0?wx_fmt=jpeg)

# Re·3-1— 以分析单机游戏作弊者的眼光去了解软件中的“内存”

原创

bl0ckdev
bl0ckdev

Esn技术社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Vehmupj0Caic1q63Q3yBE3HD7M0oLt42GU0XgWlRopU5C92OhACNN16X7wyp6QDsBk9a2RHicmuqH5BicRXgq2xuxLkCPlveiaotwE0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247493114&idx=1&sn=e792d898c8dddcaa91042edc082d6ce7&scene=21#wechat_redirect)

> 我没有选择录制视频或者是录制X教程的路线,社区整体选择的是图文+后期的问题解决。
>
> 图文可以节省很多时间,我需要把更多的时间放在我维持我生活的重心，然后在有限的四个小时逐步的拆解过程,同时在Disocrd服务器中持续性回复大家的问题。
>
> 如你有依赖视频输出的习惯,订阅星球是不理智的想法。
>
> Bl0ckdev

第四章目标已选定：

至于我们要开始的内存分析和编辑的游戏选定了,我临时选的是下方游戏,正在寻找FPS类的相关单击游戏,如果有推荐的也可以。[我的联系方式](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247493114&idx=1&sn=e792d898c8dddcaa91042edc082d6ce7&scene=21#wechat_redirect)

A·反恐精英1.5-1.6 仅限（单机）

B·等待推荐有什么比较适合解释的。  仅限（单机）

最后选定的是:[逆向工程第[3-4]部分的编辑内存和分析内存](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247493090&idx=1&sn=b53b501519d68520b7a642aa6b9d9ad9&scene=21#wechat_redirect)

* Mount & Blade: Warband
* 扫雷

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VejNibMibvcwVCGVngJKyw3ywFa7XWQricCiabf4yqic0buRls2ibENHSAQtWz37vHyGPsRMR7MOCgcOdIGMFCgjwOWpnuyHYIIXh2wcQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VejoBMY8icLw2bsTxXabBbibSQiaeWVaI0NN4txzOdicmeH2Z2xTicwX8Vnj3g8Qy6CibdYGg2kTCNWRuNbD5QXS8eUeyadcYblWmdtB8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Veia08A8Wt5n8sPX2aLcO5fTfBl5FMia5W7tz7VqcPqvJ8oOnsorfFw6L949AN1hJgPpdKXkqISSy9YbusVVS37tRXwvRbI1ImLlw/640?wx_fmt=png&from=appmsg)

文件大小4G,我将会重新压缩分段进行上传到—ESN社区云盘频道解压密码：

文件大小4G原,种子我将会上传到云盘大家使用相对于的工具可以下载：

Cheat Engine

Cheat Engine教程从入门的晋级都可以在网上寻找到对应的资料,这里其他类型的我就不在叙述了！我只单独的去写一个#CheatEngine 内存编辑和内存分析,方便后续对于内存的理解,因为在Cheat Engine研究和基础的时候会涉及到 汇编和C++,这也是强项。

关于本地和在线llm

我本地使用的是Gemma 4模型,在线选择的是Deepseek,你也可以配置Qwen3,因为我的图像模型使用的就是Qwen的多态模型,用来分析图片和修改图片。更多的问题可以在这里进行提问：https://t.zsxq.com/nun60  生成视频的话我现在的显卡不行，大多数模型支撑不了。,所以我暂时都是按小时租用GPU。( 主要是之前跑密码用习惯了.. )

今日星球—更新内容

* Cheat Engine 完整安装与中文  | https://t.zsxq.com/HaodR
* x64dbg  完整安装细节化  | https://t.zsxq.com/4ULbF
* 教程中配套的单击游戏和后期的源代码均储存在内。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VegbkCzlsmhQYszm7CDer8seXvFm30HmCscEfR7pdICoDzz3TcMvLrpzzJtKlSbYyX0GxmNCibTCMC9r9dMhhRMUXNfFISFPbiaW4/640?wx_fmt=png&from=appmsg)

整体的Cheat Engine 运行逻辑

* 1-启动游戏
* 2-初值扫描
* 3-地址搜索
* 4-修改内存
* 5-保存弊表
* 👇ESN技术社区附加项👇
* 1·从零开始C++写出来一个内存修改的程序

Esn技术社区

我们将会附加C++编程相关的操作,直接附带完整的演示,\*\*\*程序是如何编写的。

1. 非订阅用户可以直接使用Ai生成一个,然后让Ai慢慢解释即可。
2. 订阅用户将会直接使用Ai直接分析制定代码的进制和汇编。

下图[ 非订阅者故障发帖处 ]

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Vehd5Vpic1ZcyzialWr9iaf2IsyWOqFttxECI7fyBa8rsoKK1VAVZVOldRcxDMOgH4SnX1Gsz8oJDumcCBGiaibvaRK5OP8MNHAyAZHo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

https://discord[.]gg/KWFrnnqBQu

正文开始：

ESN技术社区—#逆向工程 所有内容均与图文清楚描述,主以解决订阅星球用户和非定于星球用户的进度问题。我们优选先回复订阅者,然后定期回复非订阅（故障处理）的帖子。

完整的九章实践版规划：

第二部分：

1. Cheat Engine= 如何修改内存
2. Cheat Engine x64dbg = 如何分析内存和修改内存
4. [游戏视觉/雷达/3D](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492171&idx=1&sn=ed9698bc0ad4ddf123319f6ce4473274&scene=21#wechat_redirect) — 实践版非理论版
5. VS C++ 手动创造一个自己喜欢的程序。集合前五
6. 编写一个程序后进行逆向自己编写的C++程序。完成对内存的认知！

整个阶段的细节会发布在 [订阅星球内](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247493114&idx=1&sn=e792d898c8dddcaa91042edc082d6ce7&scene=21#wechat_redirect)。可配合Agetn一键复现的会发布在公众号。

👇 点击阅读原文.订阅我的星球

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

Esn技术社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

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