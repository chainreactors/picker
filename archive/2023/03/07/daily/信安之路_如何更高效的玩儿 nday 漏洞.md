---
title: 如何更高效的玩儿 nday 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI5MDQ2NjExOQ==&mid=2247498498&idx=1&sn=b08147f28191d9099028907736055d18&chksm=ec1dcb2adb6a423c4857fdcc2e76c8c8d8c6f819864ea680f3c90d9262e563e810f48110d5d0&scene=58&subscene=0#rd
source: 信安之路
date: 2023-03-07
fetch_date: 2025-10-04T08:49:24.068009
---

# 如何更高效的玩儿 nday 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAfeMn6t58gEqgoH7SmyUmJocqEGZLPImAhlarJ4lbpm9baPicrIrhpxqYwp3LtLgEfzmj92aggosOfg/0?wx_fmt=jpeg)

# 如何更高效的玩儿 nday 漏洞

原创

myh0st

信安之路

最近又重新收集了一波 src 的信息，整理了上百万的网站资产，主要步骤：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfeMn6t58gEqgoH7SmyUmJocJm9gHT72p3dW80vvAjb5M6ZYmRm0rxYY3q1TDSU1libfp2OvAVXlpmA/640?wx_fmt=png)

可能大家都知道互联网上存在的漏洞中，nday 漏洞占比很可观，那么针对上百万的网站如何更快，更有效的从中挖掘 nday 漏洞呢？

有的人可能会说，poc 工具一把梭就可以了，比如 nuclei、xray、goby 等一键扫描，这种是最直接，最方便的打法，但是如果针对的是单个网站，或者几个网站，一把梭下来也要不了多久，但是针对上百万的资产，这么操作下来估计得个一年半载。

又有人说了，时间长，你不会采用分布式的打法吗？一台扫描器需要一年，你用十二台不就之需要一个月了吗？这种方式对于实现目标而言当然是可以的，但是对于服务器的操作和管理成本比较，服务器的租用成本与上一种一样，但是我很穷，有没有时间更短，服务器成本更低的方法？

poc 越多，对于单个网站的测试时间越长，比如 xray 高级版自带近 800 个 POC，nuclei 有三千个，上百万的网站，这么测试下来，以 xray 为例，需要 800 个一百万，以每秒 100 次的请求计算，大概需要三个月，如果测试的速度再慢点，时间会更长。

在这个测试中，其实有大量的测试是无效的，因为 poc 测试之有针对对应的系统才有效果，如果系统类型不对，则测试的过程无效，那么我们可以基于要测试的系统进行指纹识别，然后针对要测试的 POC 进行分类，这样精细化的测试，可以大大节约测试的时间，效果上面也不会太差。

### 0x01 基于 POC 定制指纹库

我的第一个操作是，基于 poc 所对应的系统进行整理，并提取相关指纹，然后获取这百万网站的 header、首页内容作为基础数据，然后进行指纹识别，找出那些 poc 所针对的系统目标。

对于以上操作，需要解决两个难点：

#### 1、指纹提取

我的做法是，首先去 fofa（指纹识别能力还不错） 上搜索，找到一个在线案例，然后通过观察其 header 信息、body 内容、标题等关键点，提取与该系统相关的信息作为其识别的特征，比如：

以标题为特征：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfeMn6t58gEqgoH7SmyUmJocddVDFC3WlrJ9eUJocicVz0dtQ5M1W1hibAu6jrFzBe7ONPqq5NBRWz7Q/640?wx_fmt=png)

以 header 为特征：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfeMn6t58gEqgoH7SmyUmJoc1Trmx2dhbsQ8iaYrH91NwKGZRlqj8Hy9c5Z1jTJPYOmPxB6ZsZianh7g/640?wx_fmt=png)

以 body 内容关键词为特征：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfeMn6t58gEqgoH7SmyUmJocrVc22g6KPXmPbatdia3Lem52ycSI5NQ7Rd5UT4adjcF4gx3rdanjCrA/640?wx_fmt=png)

基于以上三个部分的特征可以识别大部分的系统，这种系统主要为商业、开源的系统，客户不做二次开发，直接拿来用的，除了这些系统，还有大量框架、组建、服务器之类的，无法很好的进行指纹识别，这类 poc，我会将其作为通用 poc，针对全部系统进行测试，以免因为指纹识别结果漏报而无法全面发现漏洞。

#### 2、指纹规则与 poc 命名联动

编写指纹规则时，我们想要让规则识别出的系统与其对应的 POC 联动，那么就需要在命名上与 poc 的命名保持一致，比如 xray 中关于 wordpree 的 poc 命名如下：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfeMn6t58gEqgoH7SmyUmJocdibKspH3thwQTE1GWRFiabx0OKGkutt3gU4ewKicGDcQ3l2CJ8Zy0xpibg/640?wx_fmt=png)

那么我们就需要编写一个可以产品名为 wordpress 的指纹规则，如图：

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfeMn6t58gEqgoH7SmyUmJocRg0A7cPu1vwRXtvLgm4sK4cLc3hycDynuibuUd7eopdM6G6ZBmVE5CQ/640?wx_fmt=png)

那么在指纹识别结束后，就能知道那些系统是使用 wordpress 系统搭建，这个时候就可以使用其对应的 poc 列表进行测试。

### 0x02 基于指纹识别结果进行 POC 测试

经过第一步的操作，基于 xray 提供的 poc 列表，定制了一份包含 247 个系统的指纹库，对于那些针对开发框架、服务器、通用组件测试的 POC 提取出来，大概 99 个，这些 poc 将作为后续，针对每一个系统测试的 poc 列表。

其余 POC 将基于指纹识别的结果进行针对性的测试，共计 713 个，经过以下两个步骤，针对百万网站做了指纹识别：

1、获取百万网站的首页内容（响应码、header、body内容）

2、基于指纹库识别通用系统类型（7 万左右目标，识别出的系统类型 166 个）

从实战结果来看，整体测试下来相比全部测试，时间上至少提高 8 倍，原本需要三个月测试完成的目标，使用这种方式仅需要十来天即可完成。

有了这些基础数据，漏洞测试就是一条命令的事儿，相信用过 xray 的都知道怎么用，这里就不多说了。‍‍‍‍‍

### 0x03 总结

当你拥有开发能力之后，一切想法都可以形成脚本或者工具来帮助你提高效率，解放人力，自动化挖漏洞是一件非常有意思的事情，写工具写脚本也会给自己带来成就感，如果你对上面的内容感兴趣，欢迎加入信安之路与我们一起交流。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAfctHSYBwchiaKgp7icmkPcUuXLoXw2e0x1LRxK2jcOvnAAExok3ricOFogCLqAXicAOhQYgzy4bmEkOfw/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

信安之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

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