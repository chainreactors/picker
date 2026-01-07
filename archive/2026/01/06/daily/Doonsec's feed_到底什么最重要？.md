---
title: 到底什么最重要？
url: https://mp.weixin.qq.com/s/a1Xudbu8cxJ10xH9co-lLQ
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:27:59.242190
---

# 到底什么最重要？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TjmWAPibmuszXicrPeGM8tic2rT6oRlgpDVMdyytkRI5BFAdZ94a9FCw3FSIznVgoicIpc3bUqG0WWEOOKYjVrxxicQ/0?wx_fmt=jpeg)

# 到底什么最重要？

原创

heige

黑哥虾撩

![]()

在小说阅读器中沉浸阅读

这两天想统计下Chrome的2025年的在野利用漏洞情况，我首先想到的是通过https://chromereleases.googleblog.com/2025/01/ 去爬取，于是我让AiPy帮我去完成这个任务，写个个简单任务提示词：

> >>> https://chromereleases.googleblog.com/2025/01/ 这个是google chrome的升级log URL按月份生成对应的link，我需要你冲2025年01月到2025年12月的所有漏洞信息统计，注意你要通过语义理解去阅读页面内容，而不是通过正则等规则匹配，包括漏洞对应的CVE编号、报告者、报告日期、漏洞基本信息、是否存在在野利用等进行全面统计，结果按CVE编号去重保存到表单文件里，一定要注意要全面 如果访问错误请务必访问成功

测试了下跑出了106个漏洞，然后7个在野漏洞，但是最大的问题是没办法确定，于是我让AiPy随机抽查了几个月份：

> >>> 你帮我随机抽查下8月 6月的漏洞 是否对得上数据

结果提示漏掉好几个，然后我让他全部查一下在野漏洞的的情况，发现之前结果也有一些出入，后面分析后发现，主要是有一些数据的格式不统一导致的：

```
[$2000][384844003] Medium CVE-2025-0762:[N/A][460017370] High CVE-2025-13223[TBD][405143032] High CVE-2025-2783
```

而大模型处理数据习惯性的使用正则匹配，然后比如在野利用的描叙也有各种各有，比如：“in the wild” 、“in wild”等等，当然虽然在任务提示词里有要求 用“语义”理解，实际上大模型是直接无视的。于是我写了一个很长的“Skills” 并加上了一些例子说明，最后的效果看起来还不错，但是始终没办法确定数据是不是准确，抽查发现尤其在野数据老是不对，当然我也尝试了用ChatGPT来帮我执行这个任务，不过搞笑的是ChatGPT写了个脚本让我在本地跑 ... (本地跑那不直接AiPy啊！)

![](https://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmuszXicrPeGM8tic2rT6oRlgpDVIzBvFXicPR40GMmhm33N4VQLt3klHIPmzA0jiccKdG16uNaoCuMn3kJQ/640?wx_fmt=png&from=appmsg)

要命的是，最后我发现了一个问题：本身访问 https://chromereleases.googleblog.com/2025/01/ 这个页面的数据是不全的，里面有分页（相当于你爬取https://chromereleases.googleblog.com/2025/01/ 这个一月的数据，有一些一月公告的数据显示在下一页里）

这实际上从根本上否定了这个方法，于是我想着换一个思路：直接用搜索引擎的API来搜索

> >>> google api搜索chromereleases.googleblog.com上 2025年的标记在野利用的漏洞及相关信息

最后输出9个在野利用

![](https://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmuszXicrPeGM8tic2rT6oRlgpDV6c2IL84kT1xvLZKJmIhJFUjIK1olDdHJ1hDMSevBWkFLUE74qWkhgA/640?wx_fmt=png&from=appmsg)

那么这个结果准确不，于是我交叉了下GhatGPT的搜索结果，输出也是9个，对比了下

```
https://docs.google.com/spreadsheets/d/1lkNJ0uQwbeC1ZTRrxdtuPLCIl7mlUreoKfSIgajnSyY/view?gid=897725844
```

 Google P0 0day "In the Wild" 项目的数据 基本上对的上，只是在这个项目了有2个漏洞标注是webkit，这个其实也影响Chrome

所以问题来了：到底什么是最重要？MCP/Skills? 工具？产品？结果？认知？那么现阶段的用户到底是谁？LLM到底取代了什么？

在纠结那么多问题之前，先纠结下：你能正常访问 https://chromereleases.googleblog.com 这个网站吗？

对了 我上面用的模型是GLM-4.7

新年水一篇，要不然老是有人问我：这个公众号买不买 ...

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmusywYo8vMxicZG46g3fRCRKAPISGxUu21B296repWw7SQkcAUcXj2HNHOPmv4vtsuOvOykhEhwne6iag/0?wx_fmt=png)

黑哥虾撩

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TjmWAPibmusywYo8vMxicZG46g3fRCRKAPISGxUu21B296repWw7SQkcAUcXj2HNHOPmv4vtsuOvOykhEhwne6iag/0?wx_fmt=png)

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