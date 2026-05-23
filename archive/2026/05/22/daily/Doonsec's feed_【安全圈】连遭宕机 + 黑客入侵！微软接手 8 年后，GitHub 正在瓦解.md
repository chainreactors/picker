---
title: 【安全圈】连遭宕机 + 黑客入侵！微软接手 8 年后，GitHub 正在瓦解
url: https://mp.weixin.qq.com/s/tI6g0H8Qx3IEnylJfY_CNw
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:35:01.729620
---

# 【安全圈】连遭宕机 + 黑客入侵！微软接手 8 年后，GitHub 正在瓦解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGuhgHfwsibTJ8yQStF5lD0udbXVSmbvpzO3luMtDZPUIoZIzIg3xSkoMTiaXqFz2dauMy5MPJv4zTo4AROTpjlkgZrdCATnOCEc/0?wx_fmt=jpeg)

# 【安全圈】连遭宕机 + 黑客入侵！微软接手 8 年后，GitHub 正在瓦解

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

GitHub

微软斥资 75 亿美元收购 GitHub 近八年后，这一全球最大代码托管平台正陷入生存危机。频繁宕机、安全漏洞与核心人才流失三重压力叠加，AI 编程工具竞争格局的急速演变更使其战略地位岌岌可危。

过去数周内，GitHub 接连发生多次重大服务中断，并披露了一处严重远程代码执行漏洞；本周更有消息称，该公司 3800 个内部代码仓库遭到入侵，起因是一名员工安装了被植入恶意程序的 VS Code 插件。据 The Verge 采访的多名现任及前任 GitHub 员工，公司普遍陷入领导层真空、方向感全面丧失的困境。

动荡始于去年夏天前 CEO Thomas Dohmke 的离职。微软此后未安排继任者，GitHub 领导层被迫直接向微软 CoreAI 团队汇报。这一架构调整引发持续的人才流失—— Julia Liuson、Elizabeth Pemmerl、Jared Palmer 等高管相继宣布离职或转岗，**有员工直言 " 基本上已经没有 GitHub 这家公司了 "。**

GitHub 的困境正在被竞争对手视为入场机会。Cursor 和 Claude Code 已在蚕食 GitHub Copilot 的市场份额；据 The Information 报道，负责监管 GitHub 的微软 CoreAI 团队负责人 Jay Parikh 已私下警告同事，GitHub" 面临严峻威胁 "。与此同时，曾对微软收购持观望态度的开发者正以实际行动表达不满—— Ghostty 终端开发者 Mitchell Hashimoto 宣布将项目迁出 GitHub，称 "18 年了，不得不离开 "。

**领导层真空，人才加速出走**

GitHub 当前的困境，在很大程度上可追溯至去年夏天 Thomas Dohmke 的离职。微软随后将 GitHub 并入 CoreAI 团队管辖，该团队由微软 CEO Satya Nadella 亲自引进的前 Meta 工程主管 Jay Parikh 执掌。据媒体援引知情人士透露，Parikh 在微软内部口碑欠佳，不设新 CEO 亦是其本人的决定。

GitHub 员工长期以独立文化自豪，自称 "Hubbers"，如今却须直接向微软体系内的团队汇报，适应过程颇为艰难。随着营收职能并入微软 MCAPS（客户与合作伙伴解决方案）部门、产品工作拆分至开发者事业部，部分内部人士已感到公司已名存实亡。" 基本上已经没有 GitHub 这家公司了，" 一名员工上月告诉 The Verge：

" 一切都是微软，公司正在崩塌——无论是从严重损害公司声誉的宕机事故来看，还是从领导层的不断出走来看。"

高管离职潮持续扩大。拥有 34 年微软资历、此前负责监管 GitHub 营收与工程业务的 Julia Liuson 上月宣布离职。GitHub 前首席营收官 Elizabeth Pemmerl 同月递交辞呈，由微软 MCAPS 前负责人 Dan Stein 接任。今年去年 10 月才以高级副总裁身份加入 GitHub 的 Jared Palmer，已宣布转赴 Xbox 出任工程副总裁，并担任 Xbox CEO Asha Sharma 的技术顾问——值得关注的是，这位 Xbox 新掌门人已陆续招揽多名前微软 CoreAI 高管，外界普遍解读为相关人员急于脱离 Parikh 领导层的信号。

人才流失还衍生出直接的竞争威胁。Thomas Dohmke 离职后创办了新开发者平台 Entire，该公司现有 30 名员工中，至少 11 人曾供职于 GitHub，其产品方向与 GitHub 直接竞争。

**宕机频发，CTO 公开道歉**

服务稳定性问题在过去一年尤为突出，以至于 GitHub CTO Vladimir Fedorov 上月不得不就最新一系列事故公开致歉。Fedorov 承认，拉取请求、代码提交及新建仓库数量的激增，给 GitHub 基础设施带来了沉重压力。" 我们的优先级很明确：首先是可用性，其次是容量，然后才是新功能，" 他表示，" 我们正在减少不必要的工作，改善缓存，隔离关键服务，消除单点故障，并将对性能敏感的路径迁移至专为此类工作负载设计的系统。"

Fedorov 于去年加入 GitHub，此前曾在微软任职近八年、在 Facebook 工作逾 12 年。他入职后不久即启动了将 GitHub 迁移至 Azure 服务器的项目，以应对数据中心容量瓶颈，但 GitHub 所管理的复杂 MySQL 集群，使迁移过程中的宕机风险始终难以消除。

频繁宕机令外部开发者的耐心消磨殆尽。Ghostty 终端开发者 Mitchell Hashimoto 上月在公开信中写道："GitHub 每天都在辜负我，这让我感到很切身……我想继续写代码，但我无法再在 GitHub 上写代码了。18 年后，我不得不离开。"Ghostty 随即宣布迁出 GitHub。

**服务稳定性之外，安全问题同样令 GitHub 承压。**今年 3 月，安全公司 Wiz Research 借助 AI 模型发现了 GitHub 内部 git 基础设施中的一处严重漏洞，攻击者一旦利用该漏洞，可访问数以百万计的公私代码仓库。GitHub 在不到六小时内紧急完成修复。

本周曝光的安全事件更为严重：GitHub 共有 3800 个内部代码仓库遭到入侵，起因是一名员工安装了一款被恶意篡改的 VS Code 插件。一名微软员工指出，VS Code 频繁向用户推送插件安装提示，此前已有安装量达数十万次的插件在被发现植入加密货币挖矿程序后，从 VS Code 应用市场下架。

**Copilot 竞争力滑坡，计费改革引发反弹**

GitHub Copilot 曾在 AI 编程助手领域占据先发优势，但过去一年已明显落后于竞争对手。据 The Information 报道，Parikh 已就此发出内部警告。微软近期据报曾考虑收购 Cursor 以弥补差距，并已取消大量 Claude Code 内部许可证，意在推动自家开发者转用 GitHub Copilot，以帮助加快产品改进。

与此同时，GitHub 即将推行基于用量的 Copilot 计费方式，引发开发者新一轮抵触。新方案下，每个订阅计划将包含月度 AI 积分配额，超额使用须另行付费；不同于现行方案中超限后自动降级至低能力模型的做法，新系统将直接断供，付费门槛的提高令部分开发者感到不满。

**在微软内忧不断之际，竞争对手正加速围猎 GitHub 的开发者生态。**Entire、Cursor 和 Claude Code 均在强化产品能力，将 GitHub 的困境视为重塑市场格局的窗口期。

对于微软而言，GitHub 的战略意义远超一款产品本身。正是长达数十年对开发者生态的深耕，奠定了微软作为软件巨头的根基。若 CoreAI 团队无法有效扭转当前颓势，微软或将持续流失这一赋予其核心竞争力的关键群体。

***END***

阅读推荐

[【安全圈】间谍利用路由器窃密！快自查你的设备是否安全](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076710&idx=1&sn=8486b45483e17417ac95a396764113cb&scene=21#wechat_redirect)

[【安全圈】黑客团伙公开叫卖GitHub核心代码，3800个内部仓库遭窃取，事件细节曝光！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076710&idx=2&sn=61f1c86aba0ca609e6ed58d71c15f47c&scene=21#wechat_redirect)

[【安全圈】美组织要求 FTC 对 Roblox 展开调查：是否强迫未成年人过度充钱](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076710&idx=3&sn=781e1ea679e99b5bbb21f65b1598510c&scene=21#wechat_redirect)

[【安全圈】撞库黑产牟利倒卖十万条账号密码，男子获刑三年六个月](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076684&idx=1&sn=64c91617442881ffc89ce114c525797f&scene=21#wechat_redirect)

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