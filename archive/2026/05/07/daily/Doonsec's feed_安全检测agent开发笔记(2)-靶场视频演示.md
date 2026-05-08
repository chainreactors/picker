---
title: 安全检测agent开发笔记(2)-靶场视频演示
url: https://mp.weixin.qq.com/s/Lfy4dj1j0_qFkN4HSWXM_w
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:54:45.533114
---

# 安全检测agent开发笔记(2)-靶场视频演示

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kCaGE674k6MnavicUw4NMFET14YcG1860Jz3e8btV2jFF6piahexDl45D1seZT5CvvujCoP5jibw2cjoLsaHuhKQicKiaxelicqj5MXvFZGf3Bpgc/0?wx_fmt=jpeg)

# 安全检测agent开发笔记(2)-靶场视频演示

原创

鬼麦子
鬼麦子

鬼麦子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

注: 视频通过电脑显示器等大屏幕观看较佳，手机可能看不清文字。

facai安全工具的agent实战对目标进行渗透测试实践视频。

途中遇到的问题:

在使用线上模型时，模型幻觉、缓存命中，时常会出现，模型编故事编字符，甚至在一些情况，给你编一串又一串，就如视频所见，他还给我编了一个admin/ 路径，尤其是上下文长度越大，幻觉越严重。

我是早上用本地rtx5060ti-16g的qwen3.6-35b-a3b，在做测试，测试了有两个多小时，居然成功了，果然他妈的还是得相信科技，也是继续、继续、继续，就这样，但他是上传php文件whoami的，经过下午的线上模型实测，感觉本地模型的幻觉率很低，应该是本地模型没有他们线上模型的缓存命中，所以从体感上好很多，可惜太慢了，不适合演示视频，然后去阿里云找了些免费额度模型。

glm4.7 glm5 qwen3.5-397b-a17b 之类。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6OH0QevywgPicSQ02yBcZkj9mPFoY1iaYv7CT3Ntko3Sl3Weq7C0nIRwwnibTh4vGB5xLWCn4pJzX8o9g9Uiad6STOsPXP1Q3nPMh4/640?wx_fmt=png&from=appmsg)

他们真的是一堆又一堆缓存命中啊，对于agent来说，不是很有友好，还有就是，按道理线上模型的token size应该比我本地模型要大，但实测还是会时常 agents.exceptions.MaxTurnsExceeded: Max turns (10) exceeded

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6P0On28OZs76Lz8Qfwnquhf7yPApmFoib3icgIicvkby3WOVuEic0wOYXsbXr81RuIibria7CUciajtPIfY6Sn1Rh4ETDZNjmliccCrsnM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6MmtULKLVKNicRJUnQ24GXLXOk6RyGQsVrRS5icyXXTzzG5rbv1AwJ5LXt2bZ7syKUaCT8kkn8yib4y0O8YUOPw6DxaMSpuhDD2P4/640?wx_fmt=png&from=appmsg)

甚至在体感上，比我自己本地模型设置的上下文长度还要小的多，不知道是我代码问题，还是他们真的把单次上下文设置的比较小。

基本上在渗透测试和挖基础漏洞这块就这个样子了，再优化下流程，和多agent，必须得有个agent来验证需要真实交互的步骤执行是否为编造的... 还有就是上浏览器cdp控制，得动态控制网页，不能再只是curl了。

靶场相关

避免用现成的靶场，现成的靶场，模型都知道攻击路径，用来测试毫无意义，所以这个靶场是我vibe coding的，首先是让他做了个新闻管理php项目，然后我零星修改，再加了些漏洞，才开始当然测试的是xss之类，效果还不错，然后对整个测试流程做了修改，最终结果必须是以执行whoami为目标，得到whoami则流程终止，或者所有攻击面都已测试完流程终止，大概就是这样。

对facai的pro版感兴趣的，联系微信: guimaizi

未完待续...

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hMZ0ictzVvTt7jx7CZw4MSq5nEQtjICjeaVic6ibJpEw74Sls4kFials6YTebNIl4XBYcKHtzcvNtl0NUd3iaqib1TGA/0?wx_fmt=png)

鬼麦子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hMZ0ictzVvTt7jx7CZw4MSq5nEQtjICjeaVic6ibJpEw74Sls4kFials6YTebNIl4XBYcKHtzcvNtl0NUd3iaqib1TGA/0?wx_fmt=png)

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