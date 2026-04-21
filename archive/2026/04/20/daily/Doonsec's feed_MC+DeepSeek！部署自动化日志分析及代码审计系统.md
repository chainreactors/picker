---
title: MC+DeepSeek！部署自动化日志分析及代码审计系统
url: https://mp.weixin.qq.com/s/P_uUGLFIz4O1tASFE3KbJg
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:49:18.575393
---

# MC+DeepSeek！部署自动化日志分析及代码审计系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CyYbk1vmHvbJniczJ0SBdXVXXq7ScFuXAUcskh6DdlWAO68ELTBokmEV1Ohrr0IvibeKQN3XM4p5WXcxqiajTffPnq14xPFF8iaAKTuqlEC1TMg/0?wx_fmt=jpeg)

# MC+DeepSeek！部署自动化日志分析及代码审计系统

原创

Flowers aq
Flowers aq

flower安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

项目介绍

在线地址：https://monkeycode-ai.com/

开源地址：https://github.com/chaitin/MonkeyCode

项目介绍：MonkeyCode支持不限额度免费使用，不需要连接本地开发机，也不需要先折腾复杂环境。你可以直接在平台里创建任务，让 AI 编码，在云端开发环境中使用终端、文件管理和预览，再把结果接回 Git 协作流程。

CyberSecurity

正文（代码生成）

MonkeyCode（以下简称MC）是国内公司开发的，免费开源的专为代码而生的大模型：

![MonkeyCode 任务执行界面](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvYVFI7NRpy769acQrGl6Zhxu6UeicSkLYmNoS0Dwt7gNKsgP5bdfXgxanAGabaJFP3NWQXTjPTmbIOiaJicFP7joZjux9oul1icg40/640?wx_fmt=png&from=appmsg)

MC的优点在于其和Git仓库的完美适配性和支持在线部署一键调试的便携性，并且其目前支持大量模型的调度，包括大名鼎鼎的Codex！

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvZG6KdIrC5L2jczzq4upaAicfDuVD66NqfQHGEmeHgbMvBK87cdf5ZcciakQICcWXr2928r0G5sMVTbIuoQhuZibxBISEyXjmmD0M/640?wx_fmt=png&from=appmsg)

我们以一个在线的日志分析系统为例，为其让我们开发部署一个简易系统，其功能要包括威胁展示、报告输入等两大方面：

首先为其提供需求

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvZ8JhwlXfgHRrfYhtqqLN7QM9dVIzuEEHs7AKryfCqibJd5BMQuP2KsORKeMlqwl6Ub0aFgjpc0y1uvVFg0wGrsAGlHQORDdSck/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvYiaficub5Kw8Wa2H7IITC9U618NibfEKJld4WPYZbYwExXLm15uHk9B791rSibLqoQ1WXhbejuXeRFbMCPnhvXYrBnzzClfQdHb88/640?wx_fmt=png&from=appmsg)

选择技能

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvY2ib3M4Ny2UsXRG8XjWemMT90g67eh6ZtmB5EVTib2JrIfvK7uhU8Zzx0FF1Dc4ictluicRWpgQ5HjHmpZxlaOYsZ9M3jDj0SK8oE/640?wx_fmt=png&from=appmsg)

随后其进入代码生成并自动调试阶段

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvadtmSbIhx2NMoERFzCR85h1rczS8rMSAHNTSB0O3XqpzAGHdkBLW8IjBWNEcK3Z2BXBkSo7W7c6qasSB34Hiak5S5YRictqOrk8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvZBUOic3mpump8T6pQJdsh3EOibtpLnMP23Qf62fg7CYEibcKHUOciaxDONKAvNG7qlUYKYbDeroPF9iaEASnbgkRqbMqNvkZc2Vnv4/640?wx_fmt=png&from=appmsg)

开发完毕后它会启动服务器自动部署供我们调试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CyYbk1vmHvaJIw3QK853xdia4dETRSGM6RAT1y41YgZCDYW3nkiakBGKFnG8qgqtwYkdic3got5BgGxRGIQTS373EFRzHLj4EGOAv5ib3ncCicZQ/640?wx_fmt=png&from=appmsg)

我们上传日志文件查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CyYbk1vmHvY07se6AUJlHUlibGYj6753Jic2CjBUubnHSiaWZ4aqOpSGiaviclQgOcLia7WpzvD4yE1vLKRkEfPtIdDB5J3jqGbCMMHeCEHqfG3tE/640?wx_fmt=png&from=appmsg)

我们再次返回到MC为其提供我们的改进意见，让其增加输出PDF，MarkDown文档和让分析更详细的功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CyYbk1vmHvZhnAUP5QuZL82ov0ZmOicWoEu1ZH6iakvDOdzXnhNk5ialYnIF9Yy1ollpibguCpHvca66E9o9gwSTTLs6qx6v6mrO5DWbK1MpMhE/640?wx_fmt=png&from=appmsg)

改进后的系统

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvZRESbH4vicUibVoic7QKyzONT06PwNXMC2wrHtNk5cjTMP4qcQ0dYARPfVv1WUfwvd5bCCDmrFEiacN2Y88OQlXebUs1HEdIDnOwE/640?wx_fmt=png&from=appmsg)

报告

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CyYbk1vmHvbmyibA6frxL9pJhfwQb7aAciaKibeicx4GRkCVHGXzJuAxFUrAtgvRYRXtmlnSDibqVc8eqnKq5SOIav2Q5XHoC6omV6daia3FYNsyk/640?wx_fmt=png&from=appmsg)

CyberSecurity

正文（审计功能）

接下来我们看看MC的审计功能，MC有专门的审计功能，可上传压缩包或直接粘贴GitHub地址它就会自动下载审计。

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvYnEaEcpIfdKx4fFwZFLA4BaW9GcDhbaQnPrvnQo29hdoofxPFNphqhKVYpScB4lpQMquZdkyRia17guy7874fpG2pggHITiaCQA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvbLhGdbjiabyK2W3D8UKogfmfTiaHJPGmMkLC2SMvNsKvfgEe7YcOrLLiaKwI8YfAGRKvgY06p9liaAP6borngBsPjNlFljb6jcduU/640?wx_fmt=png&from=appmsg)

提供需求

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvYYhGrMUIHP1WDDyKmia63IPt7ficpkLKHxpOmA7dztNm5Jp2N0VR5Z0QafxocudwRnVEkSdrZyzemSB8Ow4TiaMRLL3mZh6wChIE/640?wx_fmt=png&from=appmsg)

开始审计

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CyYbk1vmHvbuGFl6aITzicmfD8U1Gj3Qibbz3TCray43qLLRQHpjJaF0GxicGAxv8gUyXRfQicoP6aQtxJQ3jn2rCtz6HdMXmPKBQPC9l8icOs8U/640?wx_fmt=png&from=appmsg)

审计结果

![](https://mmbiz.qpic.cn/mmbiz_png/CyYbk1vmHvZiajOOnPD95Q2L531RCUdfpQctiaLpW33LqjomvyhbczMibzliaZ94ZgBNv2UIHv1Vfp0vNQllFjtxX1QMVCsZKYGMjPw5l2TicDuQ/640?wx_fmt=png&from=appmsg)

更多MonkeyCode的玩法几交流欢迎各位添加群聊！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CyYbk1vmHvawBicNqXSANcfPqWlzNGLicqbSzoLm2wlkIJ2c0m1xGPslXuW5zQROZlhsAQL0ZdiaQglIyeViaUOWovCrUQSyzrP3DibpeuAYn2Kk/640?wx_fmt=jpeg)

CyberSecurity

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/licEEwv67W2Z6JEIDPP2iagdV37qTM3quCUoWVYv0tAkhg9rL1WTgCSqpT8ZPoM2ZeE3CGmKZ9zMlIEibTShq9hEQ/0?wx_fmt=png)

flower安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/licEEwv67W2Z6JEIDPP2iagdV37qTM3quCUoWVYv0tAkhg9rL1WTgCSqpT8ZPoM2ZeE3CGmKZ9zMlIEibTShq9hEQ/0?wx_fmt=png)

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