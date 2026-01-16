---
title: 水一篇某米OA任意文件读取
url: https://mp.weixin.qq.com/s/EzTTiDPa2-cEZseF-byZxw
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:27:04.131298
---

# 水一篇某米OA任意文件读取

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kSsBcTbgnEGBFE00Q6eCTpvfmd1VDdfZx6pic0GrwyHFtr3JJ9VNd7PoqoibibeuecYDqpqEb7NyniaREb907OlSWQ/0?wx_fmt=jpeg)

# 水一篇某米OA任意文件读取

原创

SharkSec
SharkSec

SharkSec

![]()

在小说阅读器中沉浸阅读

🔔 **温馨提示**：为了防止走散，不错过每一篇干货内容，请记得将公众号设置为**星标**！🌟

![图片](https://mmbiz.qpic.cn/mmbiz_png/cr9YyS063QrVstianyX9gPA4EZicfkbyKdBQyPtQHPwSLJePicuZmXcBiaLaRSTWrY6UibPpAaeNxLjOSiaeHaSvdHMg/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=other&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/CGEwnc7DGPkXwCkjLX8HzCgjKO1KuxPTWw8L9BNNTM3b8WVfHQxV3vIibDycqksck67KWnnVu75ctUZFfpde2kw/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=gif&tp=webp#imgIndex=1)

【声明】本文所有POC仅用于合法安全测试，严禁在未获得明确授权的情况下对任何系统进行测试。擅自测试所引发的一切后果，由操作者自行承担全部法律责任，作者及团队不承担任何连带责任。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/gFxQW0ZLIfNepCJZUicnBrw4fE1YN4dWcVLTlk9Sg3Z7GQQB6NicXCzc7r99xcmBQNKzF0GFFnd0kUuibbGSnABnw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)

引     言

一米OA是一款基于Spring Boot + Vue3技术栈构建的企业级低代码协同办公系统，支持MySQL、Oracle等多数据库适配，并可进行本地化私有部署。近期通过代审，又发现一个漏洞，给大家分享一下，仅供安全研究与学习参考。

fofa语法：

```
app="一米OA"
```

利用条件

```
无需登录直接利用就行
```

利用：

![](https://mmbiz.qpic.cn/mmbiz_png/kSsBcTbgnEGBFE00Q6eCTpvfmd1VDdfZ1Jm01j47tNoOHtuJsibvrp1my4TwonSUk6Yu5xFcABEAcvQoDpu8jRw/640?wx_fmt=png&from=appmsg)

关于本次漏洞分析，后续将整理上传至纷传上，感兴趣的师傅，可以直接在纷传中获取。

如果大家对我们的文章技术有什么建议或者工具使用上的反馈，都欢迎大家在评论区留言交流。对我们分享的文章感兴趣，想要深入探讨、交流并学习更多相关内容，也欢迎各位师傅加入官方技术交流群!!!（关注公众号，点击菜单栏：联系我们->技术交流群，添加管理员微信，备注【加群】，拉您进群）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/66Px0lScLmhsSQ81eCsVKJ3rdZkSvWiajhKcPGVl5T8wjtDrfJwp0JOA6IpdLIBVawKV3q1zsXaOP95lR6Gm0zg/640?from=appmsg&wxfrom=5&wx_lazy=1&wx_fmt=other&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/IEccNBf01KhlXSXZveRicx71HjXRoxf4N3auzMP8luVj3eupK7xS0R7jcBiaWXicawKPpLiamx4icOURtlgUdGjaVSQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

加入圈子，一起进阶！

我们圈子已平稳运营一段时间啦，后续也会持续为大家输送高质量的实战资源：有一线团队的一手攻防经验、私有工具源码（包括咱们公众号发的工具，圈子里能直接拿源码 + 持续迭代），还有漏洞挖掘的 POC/EXP、每月不定期 0day 分享，hw实战攻防遇见高频oa/设备源码都能在这拿到。

对了，圈子里还有些「刚需资源」：FOFA 的 Key 长期能用，Cursor Pro 共享账号登了就能用； 企业 SRC 案例、红队实战经验也会拆解着讲。

现在圈子**现价 119 / 人**，等满 100 人就涨到 129 了 —— 入了圈子还能进专属内部群，比咱们公开交流群的资源更新更实时、讨论也更深度。

纷传和知识星球内容是同步的，后期主要运营纷传，所以想进圈子的朋友直接扫描下方二维码就可以啦~

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/kSsBcTbgnEF69LhajNRxlDnK1VhAvG40BicZGeEp0SSffeeQtuiaibmkslPLWofJeWMia09iasDnTDdO9icRxYficM5bA/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

结束

👉 点击关注不迷路，一起潜入深水区，突破边界，共同精进！🚀

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kSsBcTbgnEEp9Bic1ajub6AAicIRCoc1GRlnsE7b1wz0MOfXibDJm0CKICT2vMqcmdELjlsyK7W0hS9Ck2JyNabyw/0?wx_fmt=png)

SharkSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kSsBcTbgnEEp9Bic1ajub6AAicIRCoc1GRlnsE7b1wz0MOfXibDJm0CKICT2vMqcmdELjlsyK7W0hS9Ck2JyNabyw/0?wx_fmt=png)

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