---
title: 微软副总裁亲自出马，把 Mac 的功能「搬」到 Windows！
url: https://mp.weixin.qq.com/s/0an7pAKYeTxknjgE-Sn-Qg
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:45:44.342802
---

# 微软副总裁亲自出马，把 Mac 的功能「搬」到 Windows！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ib4HLZ26hYAruB6RMkMApW9SiaGKtKFkRNK5UfEgicc7n6BkQetFiamSobiaWxxCzBHNT79RFSMDbziaGglc2dXB7Gr9V3icQytd4lO2ubXWJ9BjS8/0?wx_fmt=jpeg)

# 微软副总裁亲自出马，把 Mac 的功能「搬」到 Windows！

网络空间信息安全学习

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于数码荔枝
，作者正版软件

![](http://wx.qlogo.cn/mmhead/ibkKkoaQFco6z2PEeGeqENwjhkKsvrOOYWBU9icn6SvIXSBibCEfSGnozOicPsAzpYWuaMo8BVlrOAk/0)

**数码荔枝**
.

数码荔枝 (lizhi.shop) 官方公众号 —— 分享实用软件 & 技巧干货

Windows 用户有羡慕过 macOS 上这个操作吗？ —— 轻点桌面壁纸空白处，所有窗口瞬间隐藏，露出整洁桌面；再点一下，一切恢复原位。

![](https://mmbiz.qpic.cn/mmbiz_gif/ib4HLZ26hYArIcE58H66OrRQsFzVpzqdWJwVjDE6b9nQu13h6QBcbicZoBdFzZpazzEf1WHYtNnBWCloeFdkGnMs45wvxWYEibr5dhquJfkyjQ/640?wx_fmt=gif&from=appmsg)

▲ 在 Mac 上点击壁纸，显示桌面

现在，Windows 也能做到了！

把它带来的人不是别人，正是微软开发者部门副总裁 Scott Hanselman。

这位在全球技术圈影响力极大的资深工程师、作家和播客主，致力于推广 .NET、Azure 以及开源技术。

他在两天前开源了一款小工具 PeekDesktop，把 macOS 的「点击壁纸显示桌面」功能，带到了 Windows 10 / 11 上。

![普通隐藏.gif](https://mmbiz.qpic.cn/sz_mmbiz_gif/ib4HLZ26hYAoEWpicn14MrDe0cNQoMBbh0ArTDgl8QXRdOhNxnn6BpbJEsVCmd2Lv3st8ebDxy1jb29QKNFDw6973cOb2rh8EdlA3o4Wtpf5Q/640?wx_fmt=gif&from=appmsg)

▲ 在 Win 上点击壁纸，显示桌面

![标题图标](https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0u4CHiaMhAdl8MT33E9ByxnhpYuMGja3h82BzeYpzJQ90iaTxpsibR2Qlg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)告别「针尖按钮」

Windows 用户想显示桌面，要么按 Win + D，要么去点任务栏最右侧那个细到让人怀疑人生的按钮。

![CleanShot 2026-04-15 at 20.27.29@2x.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ib4HLZ26hYAq5biay6APUlsibiaNaBW05pWSmbgLWxwqmJUqSV7UhOfOlJ3Q2djNVaMskuZmia7nicZFjTPKfbEMyetS3gkmQMzbFzPE3GHFPpdg4/640?wx_fmt=png&from=appmsg)

PeekDesktop 的逻辑更符合直觉：整个壁纸就是按钮。

点击空白处，窗口隐藏；点击任意窗口、任务栏或再次点击壁纸，窗口精准回到原位。

不用担心误触。工具通过底层 API 精确区分「点击空白壁纸」和「操作桌面图标」，我们可以在桌面如常进行拖拽、右键、双击图标等操作。

他还做了个对比表，来展示 PeekDesktop 方案，相比 macOS 的优势。

![CleanShot 2026-04-15 at 21.00.38@2x.png](https://mmbiz.qpic.cn/mmbiz_png/ib4HLZ26hYApqdVgGga7qU4JZZnTpeQvPgBGib6VUFIfiaRc3G37lwoX2m7uVOJ4vyNickyyE7rvb8x3LOgwCiaCS13LGicf5Tf8mcVAIWXojjz0w/640?wx_fmt=png&from=appmsg)

▲ macOS 不支持系统托盘！赢了 ![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)

![标题图标](https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0xU9Fvm3ILCw745js1LmpsibFNyvia4QsicUbKwqeibUyrYvx0N4CN2trBw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1) 不只是模仿，还有新花样

在默认模式下，会直接调用 Windows 原生的「显示桌面」机制，稳定可靠。

此外还有多种模式可从系统托盘实时切换：

* 经典最小化 —— 逐个最小化窗口；
* 飞散动画 —— 窗口「飞出」屏幕；
* 虚拟桌面 —— 荔枝君实测时，没有这个选项。

![飞散隐藏.gif](https://mmbiz.qpic.cn/mmbiz_gif/ib4HLZ26hYArlNBG6JeOoU4fIXfryGRmtvBvpb66elmKGf1eqYib0bUlHuQkOt35q98zthsEz3FiceNcIiaZn0Z5Hrr3zDSPma4RBcuu8Q907v8/640?wx_fmt=gif&from=appmsg)

▲ 飞散动画模式

软件无需安装，解压运行即可，常驻托盘，文件体积不到 3 MB，内存占用不到 5MB，支持开机自启和多显示器。

![CleanShot 2026-04-15 at 20.44.06@2x.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ib4HLZ26hYApIXfgKyR2LNPqE3bXDloiamnC2IL8vfLrHia3RR8rdw2zDG3gicibOyVSbwBB3tuAc34yQP8ajjlvfPh8JuAnibPkdvoLnURECQXyA/640?wx_fmt=png&from=appmsg)

▲ 可设置为双击触发

![标题图标](https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0WZZD2XSfTRL4qMsKuHfseqVcjBRM0E29GIiatsL7vdPItywyXqHibNEQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1) 下载方式

最新版 v0.6.2 已在 GitHub 开源发布，提供 x64 和 ARM64 版本，采用 MIT 协议，完全免费。

![CleanShot 2026-04-15 at 21.03.10@2x.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ib4HLZ26hYAr6fich7MChKgztBuXIbjPf0VKa3uA3icicRHuA5a2YaNIBBjd86BpKSbSNsmeRShB1g7tYRHSibJibj5FIbfHiak7PibiasyI9omkSu2c/640?wx_fmt=png&from=appmsg)

有需要的朋友，可以前往开源地址了解更多信息或下载使用。

开源地址：github.com/shanselman/PeekDesktop

![标题图标](https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JBKwShvcSd8gIJqox7aK7I0f9nmMMDAvNIxXBVYXiadGiar3ovYA7wm63icczibatTnaQbZAdPrIXfeSw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1) 写在最后

说实话，荔枝君的主力机正是 Mac，但这么多年下来，「点击壁纸显示桌面」这个功能用过的次数一只手数得过来。

桌面上的项目、小组件、台前调度，统统都被我全部关掉了 —— 干净的壁纸，对我来说就是最好的桌面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib4HLZ26hYAr1sgn5v5bKG39gp3JBdCLW1Cw8or36RRsGDbnSZtO2Dy7B0licesh6cuqyfdDZkA0lGIEAWyOvxu1QbXfEMIxHwj8hdDiahX33c/640?wx_fmt=png&from=appmsg)

真要隐藏所有窗口，我更习惯用 Wins 自定义的快捷键，一步到位。

所以 PeekDesktop 这个功能，对部分 Mac 用户而言可能「不过如此」，但对 Windows 用户来说，多一种更直觉的选择，总归是好事。

毕竟，功能用不用是一回事，有没有是另一回事。

点击**阅读原文**，前往**数码荔枝**买买买！

---

![底部配图](https://mmbiz.qpic.cn/mmbiz_png/aFXaQ2oY6JA9PRiaUibW3XyibONLPibefw2jwwLBic4uoBlZp4WiaLQfqZr9n5tJkPyic2B8I5jUE4gRdnUMrepCiaO9Qg/640?wx_fmt=png)

点「♡」，了解更多好玩小工具！

![底部GIF](https://mmbiz.qpic.cn/mmbiz_gif/aFXaQ2oY6JAbmS3wc8fxt3Lemribiaz5FbJWN9K3GTB1OeJtBE3au0xdUsQTVVVyOuERx44KVcl1kDXgbEvib2TtQ/640?wx_fmt=gif)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/gfUJ2iaQ0nODk9TISbtm1uMud9k1tC7dE472rEkXzZqiaJqFJ15ls93vreGft27DTUIjDxiaI8TTBqheJRoBqn93g/0?wx_fmt=png)

网络空间信息安全学习

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gfUJ2iaQ0nODk9TISbtm1uMud9k1tC7dE472rEkXzZqiaJqFJ15ls93vreGft27DTUIjDxiaI8TTBqheJRoBqn93g/0?wx_fmt=png)

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