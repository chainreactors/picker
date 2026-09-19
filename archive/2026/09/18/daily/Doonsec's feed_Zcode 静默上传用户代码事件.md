---
title: Zcode 静默上传用户代码事件
url: https://mp.weixin.qq.com/s/cp0WPx7cDChyJ7ubjJsN3g
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:51:59.490168
---

# Zcode 静默上传用户代码事件

# Zcode 静默上传用户代码事件

ChinaRan404
ChinaRan404

知攻善防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

最开始是这篇文章，我自己的环境：ZCode 桌面端 版本 3.12.3

https[:]//blog[.]ferstar[.]org/posts/zcode-silent-workspace-snapshot-upload/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a3etiafIAYXE5apChzqIGyNBHniazmfpTBEvgQ3Qk0DBoGRvgjuib0lvkiazgvtMPDFQxMbpUT4grtQNqmfHGcHNbTpiadRyj3Ux1NJaxicNnWj64/640?wx_fmt=png&from=appmsg)

那么众所又周知

简单描述一下上传了什么？

90% 是 git 仓库，而且是仓库自打创建以来的全部历史底裤：

目前防御方案

```
MacOS# 清空并锁定 checkpoints 目录rm -rf ~/.zcode/v2/checkpointsmkdir -p ~/.zcode/v2/checkpointschflags uchg ~/.zcode/v2/checkpoints
# 验证：应该输出 Operation not permittedtouch ~/.zcode/v2/checkpoints/test
```

```
Linux# 清空并锁定 checkpoints 目录rm -rf ~/.zcode/v2/checkpointsmkdir -p ~/.zcode/v2/checkpointssudo chattr +i ~/.zcode/v2/checkpoints# 验证：应该输出 Operation not permittedtouch ~/.zcode/v2/checkpoints/test
```

不过我估计现在没什么用了，先自己检查一下自己被上传了什么吧，特别是政企、涉密单位的师傅们，速速自测。

对于这件事，智谱是什么态度呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a3etiafIAYXGMtcFyH50ryRqtuRLpRbFqKTRiattYCapNW5hP6JN7uJIrZs3xabUFjWY51cu1hvrd8AaCE1iahrAn1CTL1vtNeAoeeWr8pjicS4/640?wx_fmt=jpeg&from=appmsg)

（图片来自网传）

大致意思就是，送你个周限重置卡（又把老用户当🐶了，老用户用不了周限卡），这就就别折腾了，我们只是上传云端做 wiki，信不信由你。

最后的最后的最后

政企用户、政企开发、涉密项目，一定要自查源代码是否被上传云端。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vpaa3t1HRmibZdUyUIV26B2MicC0Pdssk9I8XMhaLthiakFkJoPdL4fwjibWEOuTdXxu4VibxgqQ7yl6yg/0?wx_fmt=png)

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