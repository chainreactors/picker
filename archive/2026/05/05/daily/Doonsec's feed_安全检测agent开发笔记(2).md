---
title: 安全检测agent开发笔记(2)
url: https://mp.weixin.qq.com/s/pfjJhR2eevIv5dC0M79luQ
source: Doonsec's feed
date: 2026-05-05
fetch_date: 2026-05-06T05:07:01.585449
---

# 安全检测agent开发笔记(2)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kCaGE674k6MngOQUzNDj8Wjlc2reqUG8APuF6GTEGVqPK1kVUwzibw7NgVz5a472dQ8dyiasqhEuHjgepVfsY8GuN9mt7iaP8V8lkKBDIj24z8/0?wx_fmt=jpeg)

# 安全检测agent开发笔记(2)

原创

鬼麦子
鬼麦子

鬼麦子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

真他妈的逆天啊，可以改行了....

如果笔记1所说，其实我就给agent了一个操作ubuntu功能，里面声明了些安全工具。

[安全检测agent开发笔记(1)](https://mp.weixin.qq.com/s?__biz=Mzg4MzY3MTgyMw==&mid=2247484254&idx=1&sn=e574a009a1d031065ea754c873319ca6&scene=21#wechat_redirect)

然后这是扫127本地的结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kCaGE674k6MuCho0KYq6icz9atf0RHldmwcUTNicdWpiaeNqRgO3otaAGHXK54lgV11DibwytAy6E9UkeicNm5TP87Sv1icJeIQUseibH7kiaVYicmAs/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kCaGE674k6MM1kicFknyF1lpcOZIxuP2yJjBT6xibNOPyu5axLDzoupaO5PkFQm1PZvU0fjiaqLrb7bpB1MbkpBsXerZzvrIpoa9Fery8Gk7oo/640?wx_fmt=jpeg)

这是扫我外网vps的结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kCaGE674k6N5AH3ZNROtHU1f0Ro1xoT9DfUjBXXG60AhicwxBIP8iaBib8NkYcWpfeEtRCnVzujg19g6uQCVNnof6uxXZPIC07f1vkekdmPxc4/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kCaGE674k6PtEORuj0GKkFia8ibVzf7hbJJkkap4f6aia7eibibzFT6yqjmTqPzglNDcNIJiaaF3Cf3L3CicMpwpgInGhKPzFMSicOWicu1vSuAjQUDc/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kCaGE674k6MibynXPbfACIPKI0w0OCZLrZicETMzBfxYQrw1g6A8FZvRnBpQTnbf2EicG2jDmibe4ucqjnMce4ccAkSnqdLPH9rjLMGDLtqdwicY/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kCaGE674k6PNIpzeiaOrj2icWHWgt2cu6GZQFTfTKUGvCVdI6wNicibdI5TU43y4VQaBpABeiaIiayz6z1698lQLZKgdQZ6fiaCqRz4aibFYTz1Tuib0/640?wx_fmt=jpeg)

我用的gemma4 27b a4b啊，本地5060ti 16g 32g ddr5，能做到这种地步... 调用多个工具，自行决定扫描方式，直接扫描还是后台挂起扫描。

甚至因为我访问bak确实存在，但是文件是空的，明明我web目录不存在这些东西，他还能给我回答原因。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kCaGE674k6OfJbqnhZZzkww3PgaBxc4J64jhfzvWMGlBfDh7KHT7ZSzdE9x9Lhp4ibBx0j1cQg8RcicHMUxykbNkJpVwZw835pGiaxWEQ4oWYc/640?wx_fmt=jpeg)

如图，就是因为我vps是阿里云的，给的假反馈...

回归正题，今天给模型加了记忆功能，曾经考虑过RAG或者openclaw的markdown那种，搜了很多文章资料，问了很多ai最终选择Mem0。

https://github.com/mem0ai/mem0

github 5.4万star

![](https://mmbiz.qpic.cn/mmbiz_jpg/kCaGE674k6NxCn3hWJtH5gEwoGSht4ibyJqicU14vWJC3ruicC78csgJpe1Ajxm6RvgZl3A9fcT724YObic1GJ7qt8LzPMbMNbxo8AFS01xes2I/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kCaGE674k6PYqrzghRbmEickECnUff6kLtvP5H4z6Bq4eZHXDG6kZxjtC7ObHPR6Ddl4eTRZM91Tgf80LLDaiaX6errQzXNWhlvFqqK2GQHMg/640?wx_fmt=jpeg)

然后vibe coding给挖了很多坑，我一般vb的时候会选择一个差点的模型把架子搭起来，便于我理解后，再选glm5.1开始搭，才开始模型给我选择的记忆保存方式是Chroma，这是个比较标准的向量数据库，然后运行起来，也能用，但是因为每次对话结束，mem0都会保存会话记忆，会额外的进行一次llm处理，这样速度是比平常慢许多，略感不适，我就搜有没有什么优化方式，就发现了更标准的做法FAISS，Meta开源的向量检索库，实测体感上，可能略微快一点点。

然后vibe垃圾模型用老的方法使用mem0:

"history\_tracking": True,  # 追踪记忆历史
"auto\_update": True,        # 自动更新旧记忆（不是追加）
"auto\_merge": True,         # 自动合并相似记忆
"dedup": True               # 自动去重

然后报错了一堆，在较新版的mem0这些功能无需修改，都是默认开启的，glm5.1搞定后，简单测试了下，这个记忆功能还是可以的，因为只是刚装上，类似chatgpt Gemini他们的记忆功能，才开始的惊艳，后续感觉并不是那么好使，具体还得看我后续使用感受...

对facai的pro版感兴趣的，联系微信: guimaizi

未完待续....

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