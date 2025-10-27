---
title: 初遇内嵌WebShell的pdf文件
url: https://mp.weixin.qq.com/s?__biz=MzUyMTUwMzI3Ng==&mid=2247485429&idx=1&sn=77740905ff8e89d5fd6b6e5a569cce5c&chksm=f9db50b6ceacd9a0930e4541ced04b622dd5d109b2507acced8f52bafac99226c36614989ee2&scene=58&subscene=0#rd
source: OnionSec
date: 2024-05-01
fetch_date: 2025-10-06T17:20:35.882396
---

# 初遇内嵌WebShell的pdf文件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dib9GLOoSY0hS255rVo4VaI4KP8IqeXhlz6K4F6CUFdUdhBXia68FqI5shEWQE1Wc0gibKHUn3iaHTGNHhqDg8vB6Q/0?wx_fmt=jpeg)

# 初遇内嵌WebShell的pdf文件

原创

jishuzhain

OnionSec

回顾一下接触安全工作的过程，也是很纠结迷茫的时期。第一份工作是接触Web安全内容，当时是审核漏洞。然后觉得没有发展空间了便自学病毒分析后就转向了恶意代码分析方向，后来APT火热起来后就又从事了两年多的APT追踪与挖掘方向，发现该方向不太顺利后如今在接触恶意代码自动化检测和沙箱优化方向。整体来说接触恶意代码分析所占的时间要远远多于Web安全方向投入的时间，昨天遇到了一个未知文件判定的事情便勾起了自己对Web安全相关的基础知识的回顾。

事情起源昨天上午其他同事反馈给我一个聊天记录汇总，事情经过是XXX告警WebShell事件，但是相关处理人从告警信息拿到对应的可疑文件后，对方简单分析了下发现找不到这个pdf文件存在恶意的痕迹，但我们给出的该文件的信誉恶意的，于是对方内心对这个告警的信任度产生了怀疑。当需要判定未知文件的信誉时，遇到恶意文件判定的事情便转发给了我。

首先这个文件是一个pdf格式文件，根据以往的经验，pdf文件存在恶意的情况有三种：

1、内嵌了恶意代码

2、存在漏洞利用

3、MalDoc in PDF（内嵌了恶意word文档）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dib9GLOoSY0hS255rVo4VaI4KP8IqeXhlrRdm2vMvUdYdIJFpl6QhBRBOKEYKpA49yIFZTM3DWR2YLDHu2HZC2g/640?wx_fmt=png&from=appmsg)

很显然，最终发现只是内嵌了WebShell。

分析未知的pdf文件，首先是需要了解该类文件的格式与文件结构（摸清套路），最后是利用相关已有的分析工具（提效）。这里是需要证明我们给出的信誉不是误报，因此可以快速给出结论，不必输出比较正式的分析报告，证明该文件是恶意的即可。

当分析人员拿到这个文件，如果是以快速判断该文件是否为恶意文件的角度出发，第一步可能就是查看文件名，比如银狐类木马总是喜欢使用很明显比较异常的文件名来伪装文件，但是文件名是可以被修改的，在这里其实可以作为判断依据的作用不大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dib9GLOoSY0hS255rVo4VaI4KP8IqeXhlnrnWSe44RV4WNEFL4xabhsEqia5a8TSp2kibK1KdGeY3ziaFlsaNVuRwQ/640?wx_fmt=png&from=appmsg)

第二步是直接打开该文件（虚拟机环境，避免影响真实系统），如果该文件存在正常的内容或者异常的内容，那么可疑度会发生变化。在这个样例中，该文件打开后全部为空白页面，且只有1页。此时可疑度变高了，排除掉测试情况外这是比较奇怪的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dib9GLOoSY0hS255rVo4VaI4KP8IqeXhlXneIibLoqbz3x2Dverm2fNMF5WGC7Sw1l3BiaN1IEfJO3sniaYd4iat4xw/640?wx_fmt=png&from=appmsg)

第三步也就是最后一步需要快速找到能证明该文件是恶意文件的证据，我们大部分情况关注的是恶意代码或痕迹。这里可以使用PdfStreamDumper工具，工具打开该文件后如下，可以发现存在5个对象，1个额外的Stream和JS代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dib9GLOoSY0hS255rVo4VaI4KP8IqeXhlib8CqChkveXN14iaxaKDGVbLlC2zzsYhvVJG65EgbzrpjPNGnMHMT4VA/640?wx_fmt=png&from=appmsg)

优先点击查询该工具标红的对象数据，如下是JS代码，不过阅读代码后发现并非是恶意代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dib9GLOoSY0hS255rVo4VaI4KP8IqeXhlkWGQpGWpC3Zb04V8hBic68fM78hTwybfURXttNqj4XyAyyBwTQybS0g/640?wx_fmt=png&from=appmsg)

接着只能一个个对解析的对象手工查看右侧窗口对应的【Text】内容，最终在最末尾的Stream中找到了冰蝎ASP代码WebShell痕迹，到这里其实就可以证明该文件的信誉了。 这里的困难点在于如何快速找到恶意代码，一般是需要根据以往的经验，或者是通过搜索关键字的方式去全局搜索。在找到恶意代码的过程中统计时间只花了1分钟，可能是该样例比较简单的缘故。实际的攻防场景中多数WebShell或者内存马往往会采用加密或混淆的方式避免被静态特征扫描检测出来，因此搜索关键字的方式会变得较为困难，需要随机应对。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dib9GLOoSY0hS255rVo4VaI4KP8IqeXhlZ3Ke2l0gmHKUrTKcE8ObBArJHv7sMJJBJCZBQ1PQjls5hkFiaSxwNpQ/640?wx_fmt=png&from=appmsg)

乱码的原因是数据内容使用了UTF-8编码，因此改用UTF-8编码后可以正常显示如下内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dib9GLOoSY0hS255rVo4VaI4KP8IqeXhlY5dbenMnEtSiaZ7c8IaWzWbyGULcAibJmh73icVrmM2dhTumNibea3jukQ/640?wx_fmt=png&from=appmsg)

上面的截图就是非常明显的冰蝎WebShell特征，如果是冰蝎WebShell，那么它的来源大概率就是文件上传手法会使用的动作。攻击者找到能上传文件的功能，然后上传内嵌了WebShell的pdf文件，之后实现读取执行（这里需要服务端有这个功能或者利用其它漏洞实现）内嵌的WebShell实现远控。

这是一个非常简单的样例，好久没有接触Web安全了，仅仅记录下笔记。

预览时标签不可点

个人观点，仅供参考

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dib9GLOoSY0jc47rhCN51nXyDLzG2t0Ed2M9ZXiaicayfuPAlbxTSDkgDFjPrEt10tb2gT9hLYG1kL0ZMCicKHvZTw/0?wx_fmt=png)

OnionSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dib9GLOoSY0jc47rhCN51nXyDLzG2t0Ed2M9ZXiaicayfuPAlbxTSDkgDFjPrEt10tb2gT9hLYG1kL0ZMCicKHvZTw/0?wx_fmt=png)

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