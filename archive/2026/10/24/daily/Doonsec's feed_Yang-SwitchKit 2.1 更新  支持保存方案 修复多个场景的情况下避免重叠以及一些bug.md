---
title: Yang-SwitchKit 2.1 更新  支持保存方案 修复多个场景的情况下避免重叠以及一些bug
url: https://mp.weixin.qq.com/s/uYpclTzBWeMMtoiuQ9314g
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:05:25.704846
---

# Yang-SwitchKit 2.1 更新  支持保存方案 修复多个场景的情况下避免重叠以及一些bug

# Yang-SwitchKit 2.1 更新 支持保存方案 修复多个场景的情况下避免重叠以及一些bug

原创

小阳的赛博日记
小阳的赛博日记

小阳的赛博日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hU0Xy2EUic31LeyM9D4IVHGRTvzUMT2jEHG5Kxy0afwhMuWqn5xhib2gGibVqsI9WkCgM0krugnf1xLTw6dwFAcK6yFczyhvNGcftjlibTcXjq8/640?wx_fmt=png&from=appmsg)

Yang-SwitchKit 2.1 更新。原计划只做一件事：把参数存下来。做到一半发现后面还有三个坑，一起修了。

**一、参数能存了**

顶栏右上角多了「打开方案」和「保存方案」，在「深色」左边。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hU0Xy2EUic32pT3TicSCcTCfJqsCy4wtyTFNfwmLeVSibvI8tpFpib5PQqibXnibbanorECv3HYU6ym5DicXog7MeXicW4odV6JPvP0tlnc0JgZn7gM/640?wx_fmt=png&from=appmsg)

点保存，弹框选路径，存出来一个 .json。下次点「打开方案」选中它，参数全回来，之前生成过的场景也按原顺序重新跑一遍。

存完标题栏变成这样，后面那个 \* 表示还有改动没存：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hU0Xy2EUic31gAOdOEoNLglBHNezzq9srib50MzCZu6RlRgUL0oR1ibRNnhjev79XwGkq2nXlMdt2nJdO32Vkta02J5j9O02KicVvRxFmEdAFgY/640?wx_fmt=png&from=appmsg)

快捷键 Ctrl+S 保存、Ctrl+O 打开。存过之后再按 Ctrl+S 直接覆盖，不弹框；换位置用 Ctrl+Shift+S。

嫌点按钮麻烦还有两种法子：把 .json 拖进窗口松手就开；或者把文件拖到 YangSwitchKit.exe 图标上，Windows 会把路径当参数传给程序。命令行也行。

窗口内拖放 Tkinter 自己不支持，常见做法是装 TkDND，但那要额外带一个 DLL，跟「绿色单文件、不装依赖」的路子冲突。所以直接跟 Win32 打交道，把窗口过程换掉自己接消息。写不好会让窗口失去响应，所以每一步都包了异常保护，真挂不上也只是拖不进来。

双击直接打开那个没做。要注册文件关联把 .json 抢过来，可你电脑上的 json 多半已经归编辑器管了，抢过来之后所有 json 都会变成用这个工具开，不划算。

文件长这样，纯文本：

![](https://mmbiz.qpic.cn/mmbiz_png/hU0Xy2EUic33sXBzWFcx4oyfIp0Nr4nlC9TGMibEg81EqV1WI2ibCLqMG6xup431P84NvWonTblJP56DxYdLsaic7er0ekPTGQRutFOlrKSytmM/640?wx_fmt=png&from=appmsg)

填了参数但没点「生成脚本」的场景也会一起存。不然你填了 29 个场景只生成了 3 个，存一下只剩 3 个，剩下那些白填。

**二、多个场景不再堆成一坨**

这个是打开方案之后才暴露的。

每个场景单独看都是完整的一段：自己进系统视图、配好、退出、保存。只生成一个场景没问题，可三个场景拼在一起，脚本区就变成了这样：

system-view     ← 8 次

return          ← 3 次

save force      ← 3 次，等于保存三遍

粘到设备上存三次，看着就不专业。

现在合并时会自动整理：进入视图只留第一个，保存只留最后一次，同一条提示不会出现两遍。124 行里，system-view 一次，save force 一次。

![](https://mmbiz.qpic.cn/mmbiz_png/hU0Xy2EUic33HukITIGdYiaG7Xia7BxuZQU8H9g4JnZiatYvXgOCMUoLtOATG7zK9wkWEmhGaIBdhjIValUz1R4Kqyngj5C9Ybzyspj369p30mY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hU0Xy2EUic30N1TGMA9W9nCmgjicLUsymSDg4uKK2lpOZuvSBaQ1snAnFkk6HxVhldNYH85picKibyvVTay06a5k7oOJDkLibO6MGwmZDqDRsSpU/640?wx_fmt=png&from=appmsg)

有一处我特意没删，思科和锐捷的 configure terminal。

因为它们的 show 必须在特权模式。中间的 end 和 configure terminal 是成对的。删掉 configure terminal，后面的配置命令会落在特权模式里报错；删掉 end，后面的 show 又会跑到全局配置模式里报错。所以这两家只做了保存合并。

**三、修了个会让思科直接报错的坑**

这个跟上面那个合并没关系，是查合并的时候顺手翻出来的。

原来思科的核对块长这样：

configure terminal

show ip ospf neighbor

show ip route ospf

end

show 是特权模式命令，夹在 configure terminal 和 end 中间，等于在全局配置模式下敲 show。真机上会直接给你：

Router(config)# show ip ospf neighbor

                 ^

% Invalid input detected at '^' marker.

锐捷一样。而且不是只影响一两个场景。我写了个状态机把生成的脚本从头到尾走一遍、记着当前在哪个视图，扫出来 **58 个单场景里有 32 个存在这个问题**。不光是 show，write memory、copy 也是同类错误。

改法是把核对块里的 configure terminal 和 end 都去掉，只留查询命令本身；配置块该退出配置模式的补上 end。

这个错之前一直存在，只是单看每个块都像模像样，拼起来才露馅。现在 tools/view\_audit.py 会一直盯着这件事，改坏了会报出来。

**四、保存的反馈**

有朋友反馈「点保存方案没反应」。查下来不是坏了，是反馈太弱。已经打开过文件的时候，点保存是静默覆盖，不弹对话框；存完「未保存」状态被清掉，再点叉号自然也不弹确认。状态栏其实有提示，但那是灰色小字、贴在窗口最底部、五秒就没了。

现在改成这样：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hU0Xy2EUic33d8PapTgTsQT6XP2NAeEbDaV0Fnpz1LIVZnoLdrIIexz8XXiaz0bjt2GdTYnxLnibxlUWHDVOEmGEbB8060lfq6lAvlO5vm7LrE/640?wx_fmt=png&from=appmsg)

绿色，留 8 秒。没有改动的时候点保存，会明确告诉你「已是最新」，不再默默重写一遍文件。

**怎么升级**

去 GitHub 下 2.1.0 的包，覆盖旧的 exe 就行。或者后台私信“交换机”发您新版的网盘链接

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hU0Xy2EUic309LfD9glHpzuCKghBUR9uxnP62QJocSw1p94908xL8HiaFRD6kemfWrqB4prY544oyryPzQEIzo8v8Ve6p0e7HB1LGkoYDOJA0/0?wx_fmt=png)

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