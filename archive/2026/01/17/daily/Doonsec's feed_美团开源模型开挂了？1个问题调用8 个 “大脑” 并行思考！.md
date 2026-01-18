---
title: 美团开源模型开挂了？1个问题调用8 个 “大脑” 并行思考！
url: https://mp.weixin.qq.com/s/_XiH14-QIQ1SO30rovQvTA
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:33:16.721264
---

# 美团开源模型开挂了？1个问题调用8 个 “大脑” 并行思考！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHacrzKbqCu1eWcsiaSLYw4PZ4d0hbRibLJeSwxCB2eMn9ib7F9GS5icLMuCyw/0?wx_fmt=jpeg)

# 美团开源模型开挂了？1个问题调用8 个 “大脑” 并行思考！

原创

天欣
天欣

天欣AI

![]()

在小说阅读器中沉浸阅读

1 月 15 日，美团开源了最新一代大模型 LongCat-Flash-Thinking-2601。这是一款总参数规模高达 560B 的模型，其采用了 MoE（混合专家）架构，模型可以在大参数规模下依然兼顾了推理能力与推理效率。

![美团官媒.png](https://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHacZUBuwoNHDqBSIFyUztYwdTYW94tzGPEria8kCPBoePLYWRnJKp8d04w/640?from=appmsg)

LongCat-Flash-Thinking-2601 这款模型在工具调用、搜索推理等场景达到开源 SOTA，评分甚至超越了 Claude 的闭源模型。

![评分图片.png](https://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHachYEVNPZgBJic0rf0mhwGSZTPzt7wHScgo1ropyiaPickDnPbgXicoEnw6g/640?from=appmsg)

> 官方体验地址：
>
> https://longcat.chat/
>
> 魔搭社区：
>
> https://www.modelscope.cn/models/meituan-longcat/LongCat-Flash-Thinking-2601

最让我感兴趣的就是这款模型的并行思考的能力，我给大家演示一下，比如这里有一道数学逻辑推理题目（大家也可以试着做一做，这类考验逻辑的题目还是挺有意思的）：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHacicfHL0DWBolicdL3HTa6dic02b6ezcGZAicZ5iaXB7rgu4LdIt0gaIwb0CQ/640?from=appmsg)

我们打开上文中的官方体验地址，然后将问题发送给 AI 模型，你就可以看到AI模型同时调用了 8 个 thinker 来思考并分析这个问题，当我看到这个场景的时候，我都震惊了，没想到还能这么玩儿。

![8个thinker模型.gif](https://mmbiz.qpic.cn/mmbiz_gif/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHacvB3ZmQ0An675lhO2fzHMiat9KknTJNvh12Q18yd0liaHtedet7Stfe3A/640?from=appmsg)

最后 LongCat-Flash-Thinking-2601 模型会根据这 8 个 thinker 的分析结果，总结分析一个最终的答复。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHaczXibzxl6EhpZVDHpkN5z8DNlJurpoubsfCXX0QyJzLojOZuiacct36jw/640?from=appmsg)

其中有些 thinker 甚至会自动执行 Python 代码然后确保最后结果正确。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHacHRE2blnraXxM9CdMx5DJ8JjOoej94r7cufyQXicCaE7MBLibXspptLOA/640?from=appmsg)

最后 LongCat-Flash-Thinking-2601 也是成功的推理了这道题的正确结果：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHac27ic3mQOHvWTfAYIxD7qQbog2XHhhwOYJHiayhMTf0qJrvzxYbmnmz4g/640?from=appmsg)

接下来，我想测试一下 8 个 thinker 的数学题目推理能力，但是我发现在深度模式下，竟然无法上传图片。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHacV8Xmk8b9BnoUGbA2t69UbXz0ENJspeoZ6m8P1QNeW1ZWmHOia3pcJBg/640?from=appmsg)

所以我这里只能复制数学题目文本发送给AI了，最后经过对 8 个 thinker 的思考结果进行总结后，给出了正确的答案。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHacXFIaF3HBEEGuiaTGnQP0Mmcg0sRveNKCoF9TZiaEVbicTCxicYK03FCGtg/640?from=appmsg)

不过这里不得不提一句，深度思考模式下不能上传图片确实是挺可惜的。

下面我们再来看一个编程的测试案例，让 LongCat-Flash-Thinking-2601 生成一款经典的童年游戏——飞机大战。在我提交需求后，可以看到系统同时启动了 8 个 thinker 并行思考，然后分别给出各自的推理与回复。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHacPnZ1wWyUWeN4yCcCmKQfulicn24PfwanFeXWs3RBAs4hliarqS03dAzg/640?from=appmsg)

这时候我遇到了一个问题，在深度思考模式下，尽管这 8 个 thinker 在思考过程中得到了具体的代码内容，但最终也没有给我一个确定的代码结果，反倒是直接告诉我：出错了，请重试。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHac9cfwceLZy7WnuyyRTAtYCDbwtPQBS2fxrk7l4icbc4L2JSpa4Sibxs9A/640?from=appmsg)

所以我只能当这些 thinker 的处在思考过程中的时候，去随机选择一个thinker 的生成的代码结果来做为结果，最后这款“飞机大战”游戏的效果如下所示：

![飞机大战.gif](https://mmbiz.qpic.cn/mmbiz_gif/AyVFGmKalNyRDiavLkzHQB3HuM5sOeHacqG9nicTlMibORq3COzMn9wTicTEHbia9tB8MuRnhL5ClLTYQWa3gVqF2Hg/640?from=appmsg)

生成的结果没什么大问题，就是这个绿色的飞机实在是有些不美观啊![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_05.png)

总的来说，这种可感知的并行思考方式，已经足够让人眼前一亮，也让人对开源大模型未来能“怎么玩”有了更多期待。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNz2bAzZDNvNXR9yvPBwu4HyfdFk7GADDDIbK5DWYWHQDoyyiauJY36pVkQZ8sATZZDRMpbczyBWmJw/0?wx_fmt=png)

天欣AI

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNz2bAzZDNvNXR9yvPBwu4HyfdFk7GADDDIbK5DWYWHQDoyyiauJY36pVkQZ8sATZZDRMpbczyBWmJw/0?wx_fmt=png)

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