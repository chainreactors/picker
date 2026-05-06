---
title: 五一炸场！老外做的DeepSeek版Claude Code开源爆火
url: https://mp.weixin.qq.com/s/rOWwQPmLi5QC6k_l25xIBA
source: Doonsec's feed
date: 2026-05-05
fetch_date: 2026-05-06T05:07:20.730294
---

# 五一炸场！老外做的DeepSeek版Claude Code开源爆火

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKwWSfmT2gT3wlC5I7o882IYAIAUulMvTkdjQcd8gQonh0LKm5bwETUzib2MkT7GHotWVwQIlOwBY500KPNC9CVFt4qNeviaxkMs/0?wx_fmt=jpeg)

# 五一炸场！老外做的DeepSeek版Claude Code开源爆火

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

这个五一，AI圈被一个跨洋开源项目彻底点燃。

一位美国独立开发者，凭一己之力做出DeepSeek版Claude Code，开源即封神，两天冲上GitHub热榜，星标狂飙2.7k+，还特意用中文喊话：

鲸鱼兄弟们，谢谢你们 。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKbpkefvmojDicjXibBgs9YIDS7ydQgicGAnmc9EDaEts8W9q6Va0Yudl8zQR2u8BBic7m2sOHy7T9c2DTcT4Kb2naJnGuBNUCzEOc/640?wx_fmt=jpeg)

他叫Hunter Bown，不是DeepSeek员工，却做出了让无数中国开发者直呼“终于平替Claude Code”的神仙工具——DeepSeek-TUI 。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKAIntaDoCDzqagpAo9CRLW7mSqlicnWFl80e9gw2ibkLeEib3j1hsD6nziaibA152vVz84EAgiaR5azUpibiazORgeXxlae5CeKIPpapI/640?wx_fmt=jpeg)

01、到底是什么神仙项目？

简单说：Claude Code的体验，DeepSeek的内核，完全开源免费 。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJ4TCagMOa6uq9IanwUyDmroKxwm1WmD2O3HLYkvWQwBtxIHYLNmhGiat8nnvFKr0eqqLxhS6WUZpJ6lOx5rDLJqRpyTkWibkS8c/640?wx_fmt=jpeg)

这是一个用Rust编写、跑在终端里的编程Agent，底层搭载DeepSeek V4，Claude Code有的核心能力它全复刻：

 文件操作、shell执行、git管理、网页搜索

 子智能体调度、MCP服务器兼容、SKILL.md技能机制

 三档操作模式：

Plan只读探索、Agent分步确认、YOLO全自动

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicILOMz42HDWvZRPllsYf2RFjyxMwMEqXmDwhd80qHTThgXpCn45JjN3UTkOuFWRSBTBNovGKGHE2HCtQwZianIAoJgaKUZ2GKys/640?wx_fmt=jpeg)

 工作区Git快照兜底，误操作可回滚，安全不翻车

更绝的是把DeepSeek特性拉满：

 思维链流式输出：终端实时看AI思考写代码

 默认1M token上下文：长任务不中断

 RLM并发设计：1主模型+16个Flash子任务并行，成本直降，效率拉满

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJsy2Jvleg0OX7eoR3Ipiaevg8KYAZxfhSKkE5rOUicnTJk9pGICicCTpWhk4ID5WrtJVumcibeeUS03ke0hibrEVLXCDKDBrapicZoA/640?wx_fmt=jpeg)

安装一行命令搞定，全平台兼容，预编译二进制直接用：

plaintext

npm install -g deepseek-tui

贡献者列表里甚至有Claude、Gemini、Qwen等，堪称AI辅助编程的梦幻联动 。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIvay71hHbwB5icTnggiafCvttlvovra3RpPuy6cmRtQW0iao1cVBT2qFn6l7WIAicdIDkteibsjiaFIvJlE2Pcia3ko6ZgBichsicAP5W4/640?wx_fmt=jpeg)

02、破防了！老外把中国开发者宠上天

最戳人的不是技术，是Hunter的用心。

他明明不在中国，却精准拿捏国内开发者痛点：

 发布包托管在阿里云OSS+腾讯云COS，告别GitHub下载慢

 用DeepSeek把宣传推文翻译成中文

 专门写中文版README，降低国内用户使用门槛

国内号主“Datawhale”发文介绍时，他还会留言感谢：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKVWCsG17uEp3yFn2GzlyA9VrtwK4KabPmlczA1lOXL5Zuic8Sm2HzPFZibbnPZIohHBk0cF4ic30jrSibTDvB2uOeGKB91qia24bqY/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKeHDE6Gyc8BbqvMzMXlLa7bkY7VtIQeVQpAaV9DjBhtm3BnpCKlibSdltDrMCZzdB4yJpco10yzLKSHjU4ye5KJyl4uZlW475A/640?wx_fmt=jpeg)

他在推特感慨：

这是我人生最疯狂的两天，一句“鲸鱼兄弟们，谢谢你们”，破防无数中国开发者 。

网友用后体验：

我今晚用了一下，感觉有点慢。不知道是不是我的错觉

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKlaVic2Ks7e6wz30atLvfk5qCJtykY7VzLcia5EGZhlicZjtl3oVN5sdVaumAs98qicIL6oKflCoyE1zsWXHtvx4aYWWsGib9W2oFY/640?wx_fmt=jpeg)

03、更离谱的是：作者根本不是程序员！

你敢信？做出硬核编程工具的Hunter，没学过计算机。

他的履历堪称跨界传奇：

 本科+硕士：音乐教育专业，当过3年乐队指挥

 后来读MBA，又去法学院专攻专利法

 写代码是半路出家，他说这不是转行，是人生轨迹交汇

跨界buff还藏着家族传承：曾祖父是贝尔实验室研究副总裁、无线电先驱，科学家爱音乐；百年后，他是音乐家，痴迷科学 。

04、为什么这个项目值得所有开发者关注？

1. Claude Code平替自由：不用再眼馋，免费开源平替到手

2. DeepSeek生态爆发：国产大模型被海外开发者认可，反向赋能社区

3. 跨界编程启示：非科班也能做出顶级AI工具，打破技术壁垒

4. 开源无国界：一句“鲸鱼兄弟”，见证全球开发者的温暖连接

最后

一个音乐出身的老外，用Rust+DeepSeek，做出火遍中国的终端编程Agent；一群中国开发者，用星标和热情，回应这份跨洋诚意。

这就是开源的魅力：技术无国界，热爱可跨洋。

项目地址：https://github.com/Hmbown/DeepSeek-TUI

快去试试这款免费、开源、专为中国开发者优化的DeepSeek编程Agent

作者：hacking。前北漂程序员，现在做安全。

文章数据来自网络，大模型优化，侵权删。

**往期****相关****回顾**

[突发！意大利批准：美国引渡中国工程师徐泽伟](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554552&idx=1&sn=3ea39c208a37b34e033420ee8e4fa096&scene=21#wechat_redirect)

[DeepSeek现在我是你爹了](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554708&idx=1&sn=fbdf1504f70e6d8f7ba33aa96e881189&scene=21#wechat_redirect)

[苹果突发“社死”现场！一个文件忘删，4万亿AI家底全曝光](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554704&idx=1&sn=7b352ba2101a82abd1369f9cf4655995&scene=21#wechat_redirect)

[体制内vs大厂：当初选“稳”的人，现在后悔了吗？](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554700&idx=1&sn=90b851bc9acd516f42f7afdeae8dfc35&scene=21#wechat_redirect)

[炸场！2026年4月GitHub爆火11个开源项目，第3个Hermes封神](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554685&idx=1&sn=4ece1c43e225372e6e6625c22cdca38c&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

Hacking黑白红

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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