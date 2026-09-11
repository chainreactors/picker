---
title: 卫星什么时候能拍？不用等厂商反馈，一句话查询卫星过境情况
url: https://mp.weixin.qq.com/s/c4xemnUztyNJMeEKybdTsw
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:49:43.080911
---

# 卫星什么时候能拍？不用等厂商反馈，一句话查询卫星过境情况

# 卫星什么时候能拍？不用等厂商反馈，一句话查询卫星过境情况

原创

mapxiaotu
mapxiaotu

空天感知

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

这是一则有关自主完成卫星过境分析的成果预告。阅读约 4 分钟。

涉及卫星遥感影像的获取，不管是用户还是乙方，大概都经历过这种对话：

-「明天这块区域，有没有星能拍?」

                                              「先把坐标和时间窗发我，我去问厂商。」

                                               「回了再说，可能要等半天。」

-  [那等等.......]

从用户角度,你其实永远不知道三件事：**卫星什么时候过这里、怎么安排拍摄、要不要拍。**

答案不在自己手里，而在厂商值班表、销售微信、或者某份过几天才能回的 Excel 里。

来回拉扯是常态，效率低；真遇上应急，更显得脆弱——**窗口稍纵即逝，人却还在排队问。**

从「问人」，到「可计算」

我们想把这件事，先从「问人」变成**「可计算」**。

于是做了一套**卫星过境分析算法服务：**

只要卫星公开了 TLE 轨道根数，就可以对任意目标点或区域做**窗口预测、几何评估**。

理论上，**凡是公开了 TLE 的卫星，都可以纳入同一套过境分析**——不必每换一家厂商，就重新经历一轮人工沟通。

![在地图上圈选 AOI](https://mmbiz.qpic.cn/sz_mmbiz_png/cemuAg1hRPvvbXq00EJl9zTpqRH7JpOhzSFwBSBibFa2bBWBiaEiczhYeHzHv6ceOqDj5gVVVxHvuCMicTa05mOKhqJx4pay0IZic4vRYsC7qZGU/640?from=appmsg)

*在地图上圈选目标区域,查看覆盖与任务机会*

算法好看，更要经得起对照

在大模型智能如此涌现的时刻，你告诉AI按照轨道根数等去做个过境分析算法，可能也就是半小时的事。

但是，没有经过任何检验的这半小时产出的算法，往往是一堆问题。我们自己在coding过程中发现，大模型前五轮产出的算法，包含着各种Bug。

我们获取了 **Umbra** 与 **Planet的过境数据做验证，与本地基于公开 TLE 的推演交叉比对，结果高度一致；**

同时也联系了国内一些厂商，利用其**官方过境分析做了同口径对比。**

同口径对照结果

厂商官方分析 **12** 条,与本地 TLE 独立推演 **11** 条达到**秒级到分钟级**对齐。

公开轨道可用时，独立推演已经能逼近厂商侧预报，而不是只能「听人说」。

一句话，查过境

在此之上，我们还做了一层**类似自然语言交互：**

你可以直接问：

「未来几天，杭州市有哪些卫星过境」

「明天，北京市有XX卫星能拍吗」

…

诸如此类，自然语言交互也可以进一步拓展至日常操作：

「帮我调取杭州市近一个月的存档影像」

…

时髦的团队会给起个名字叫Agent    😄

也想吐槽下，我觉得，尤其是卫星厂商内部，应该全面拥抱AI，先拿AI改造改造自己的业务系统，再对外提什么大模型遥感解译，现在的生产模式还是过于原始了。

这样一来，系统返回**窗口与可拍性判断，**而不是先填一堆参数、再等人工回微信。

目标明确——**把多的人工交互变成可复现的流程化过程，把决策前置到沟通之前。**

**下图是我们参考skyfi平台做好的自然语言的验证：**

![自然语言查询过境窗口](https://mmbiz.qpic.cn/mmbiz_png/cemuAg1hRPvETQicdDExWhu38libl6dJsIs62IIL42sGjdicvqibApwBONy5AOwQ4uIvzw6xeUePEFicAJkMiagdlVJkUVZcXdhR0HlYwJFBXXh8c/640?from=appmsg)

*自然语言 + MCP:一句话查询过境窗口;右侧结果来自真实可行性查询与本地交叉验证口径。*

预告

这是正式成果发布前的一则预告。

能力还在打磨，但方向已经清楚:

**让「卫星什么时候过」对用户可见、可算、可复用。**

这个场景，你觉得最该先落在哪里?应急快响、常态排期、多源采购前的机会窗比选，还是给业务同学一个「先问清楚再找销售」的前置工具?

也欢迎有意向的同行交流合作——一起把黑盒对话，变成可计算的基础设施。

有想法，留言或私信，我们聊聊。

`往期推荐：`

[让AI“读懂”12000+景SAR影像：开源SAR平台重大更新，接入大模型你也可以实现以文搜图](https://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247488734&idx=1&sn=d045ef3e00551d2562e24413dab1bfe2&scene=21#wechat_redirect)

[也说遥感共性产品，行业需要什么样的遥感产品？](https://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486926&idx=1&sn=66ad7dc53a491a5c9068e6b4684cbb03&scene=21#wechat_redirect)

[看水利部水利遥感星座战略布局，机遇与挑战并存](http://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486470&idx=1&sn=8cac97764abc7e9245f86848dd08e2ca&chksm=ea6d9db9dd1a14af59370e49bcf8ee8e5ba2da77d1b5658589b68c6d649ff302627d446d071e&scene=21#wechat_redirect)

[Umbra开源雷达影像下载工具开发实践](https://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486877&idx=1&sn=15bb7e1fa63a69c07bf78df5e668758a&scene=21#wechat_redirect)

[NASA与微软联合推出“Earth Copilot”，“智能助手“或成为行业产品标配](http://mp.weixin.qq.com/s?__biz=MzI2MDIyOTMyOA==&mid=2247486590&idx=1&sn=869ed4f61721ebc13009dd121b105b90&chksm=ea6d9dc1dd1a14d7146f6faee440b3c3e6526d673c10f990d3f7d633b45350eec0f51aae7e4f&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWjdEW9c30onjJcgk6LHVj8znEw3pAFsRY0RgWLfXfGOVGNfqjsgmQxVALISuFh3ovbrUZbOEyX49Q/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

笔者长期从事人工智能、遥感、大模型等业务

欢迎添加微信交流

（微信号：mapxiaotu）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ObyhaySm97WZNjpySwibqk7H5ntMHKzv68D9ES1ajKEoa99iaKyw0UHfrzyqxcAe0RgoS61lwXicia92djIK593Atg/0?wx_fmt=png)

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