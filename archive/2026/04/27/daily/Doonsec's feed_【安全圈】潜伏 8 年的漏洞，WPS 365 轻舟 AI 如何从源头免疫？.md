---
title: 【安全圈】潜伏 8 年的漏洞，WPS 365 轻舟 AI 如何从源头免疫？
url: https://mp.weixin.qq.com/s/HMx0Y-GakKYxFrQk_wi6cA
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:26:07.494800
---

# 【安全圈】潜伏 8 年的漏洞，WPS 365 轻舟 AI 如何从源头免疫？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGKdUEhPgSE8ZmATSJ7IOPAia2bBHZNZjLOBqYFsibmy2htOpvdH4qYM8UYw1uJQ0LibN6yYTdCxhSpGo0BdCQgEGPazr8l5nORLA/0?wx_fmt=jpeg)

# 【安全圈】潜伏 8 年的漏洞，WPS 365 轻舟 AI 如何从源头免疫？

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

AI

近期 ，360集团公开披露了一个让人不安的事实：一个潜伏长达8年的Office远程代码执行漏洞，被评定为Critical（最高危）级别，影响全球超10亿用戶。简单说，你打开一份Word文档，电脑就可能被远程控制。这不是科幻电影，而是正在发生的安全危机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyGdbW1g6neQ1N3yoX8UvGPg9nIO3jx4dz3D2Y5YNEicoYdYbc7ao7capM0ez1aX64wiaic4RhwZnm8QmQK2XZlYeP5OOGtnfrRkZs/640?wx_fmt=png&from=appmsg)

360 创始人周鸿祎的判断很直白："一个人就能操控上百个黑客智能体  ,  网络安全正从 人与人对抗 进入 机器与机器对抗 。 "过去 8 年 ，这个漏洞为什么没被发现？ 因为传统安全逻辑是"发现问题→打补丁→等下一个问题"。但当 AI让漏洞发现能力可以被训练和复制，打补丁的速度已经追不上攻击的速度。问题的根源在于宏机制一它允许文档内嵌可执行代码，本质上是给攻击者留了一扇门。2025年，国安部通报境外人员伪装成"学生"向高校专家发送内置木马的Word简历；2026年1月，工信部紧急提示攻击者把恶意代码藏在DOC和PDF文件里。办公文档，正在成为网络攻击的高频入口。

当传统防御全面失效 ，企业需要的不是更好的补丁，而是从架构层面解决安全问题。这正是WPS 365轻舟AI 已经解决的问题。金山办公选择这条路径，是因为判断：当AI让攻击能力可以被规模化复制，安全将从"可选项"变为"必选项"。而传统SaaS模怯的数据外溢风险，让政企客戶 "想用 AI但不敢用"。轻舟AI要解决的，正是这个行业困境。

轻舟 AI 的技术路径是：将 AI 能力压缩到单台普通 CPU 服务器即可运行 ，企业无需采购昂贵的 GPU 集群 ，也无需改造现有IT 架构。这意味着 ，过去需要千万级投入的 AI 私有化部署 ，现在可以降低到百万级甚至更低。

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyFK2VxlPJiarzUbYk89xUwvJjF91yz5HCNoL0mrwAwsqIfK2siaMIF0cUjYQ4AY0ic9wDlzRN7f9Obzc2exGpkxXWThpyic9mbCwI0/640?wx_fmt=png&from=appmsg)

图为轻舟 AI 发布现场

轻舟 AI 是金山办公发布的协同办公行业首个私有化 AI 办公解决方案 ，针对私有化部署的安全需求做了专门设计。其核心安全逻辑是：数据不出域 ，安全由企业自己掌控。

具体来看 ，轻舟AI提供了三个关键安全能力：第一，完整安全治理闭环一满足数据不出域的核心安全要求，形成从权限管控、操作留痕到内容审核的全流程安全管理，满足政企、金融等行业的监管规范；第二，全链路可控一企业可自主调整业务参数、优化提⽰词，将内部私域数据转化为AI可直接调用的知识，全程可控可追溯，避免黑盒模型不可解释带来的安全风险；第三，轻量化原生架构降低部署风险一同等功能下，传统方案需10 台服务器+8 张高端显卡，轻舟AI仅需1 台普通CPU服务器即可，资源占用降低超95%，可直接复用企业已有算力，无需额外采购硬件降低供应链风险。

更重要的是 ，轻舟AI不是纸上谈兵。已有数十家大型客户处于投产或POC 阶段，涵盖工商银行、华为、华润、vivo、上海机场、美的等知名企业。其中一家头部科技企业将轻舟AI应用于法务评审，针对评审类型超400种、业务规则超2万条的复杂业务挑战，将人工邮件评审升级为线上智能评审，AI智能定位风险项，单份文档的评审耗时从140分钟缩短至40分钟，效率提升超3倍。年研发投入20.95亿元、服务超90家央企、在互联网周刊2025信创办公软件排行榜中位居榜首一这些数字背后，是金山办公38年的安全积累。

对于正在推进国产化替代的政企客户而言 ，这次漏洞事件提供了一个清晰的决策信号：办公软件的安全选择 ，不仅是效率问题 ，更是国家安全问题。 当 AI 让攻击能力可以被规模化复制 ，安全已经不是选择题 ，而是必答题。轻舟 AI 给出的答案是：让企业既能享受 AI 带来的效率提升 ，又不必把数据交给别人保管。这或许就是未来十年政企数字化的底层逻辑。

***END***

阅读推荐

[【安全圈】89TB数据灰飞烟灭！北京一科技公司工程师“删库”获刑5年](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076007&idx=1&sn=6a6eff1e09bd7d67b20d20ee06a2fd39&scene=21#wechat_redirect)

[【安全圈】男子利用公安内部系统卖个人信息 非法获利被判刑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076007&idx=2&sn=09ae1d9ef07438cdb39cedb748421211&scene=21#wechat_redirect)

[【安全圈】装机必备的GPU-Z出事了！曝出严重安全漏洞：黑客可获取系统最高权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076007&idx=3&sn=7b7cd810015615c15d6232964cb06d5f&scene=21#wechat_redirect)

[【安全圈】美国家庭安防巨头 ADT 被黑客勒索，大量客户数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075996&idx=1&sn=421380f14f3ee130f56c4f1cbcca9e6c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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