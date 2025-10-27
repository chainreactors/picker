---
title: 开源发布 Slax Reader？
url: https://mp.weixin.qq.com/s?__biz=Mzg5NDY4ODM1MA==&mid=2247485184&idx=1&sn=5631150794f13f2af1509777b8340a76&chksm=c01a8a31f76d032737ce1151b4b5293e420adca18276fe745d55c96b334b6a287e25f73bfccf&scene=58&subscene=0#rd
source: 吴鲁加
date: 2025-02-09
fetch_date: 2025-10-06T20:37:39.055211
---

# 开源发布 Slax Reader？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sQicKibM7wlr9DcQUdSAFSnZqKz2iaPUFZMgAAK4ISqkQKglpgaxnZ4s8P97wwMcib3M17Ho0WCfaU6xDCE7OdMAMw/0?wx_fmt=jpeg)

# 开源发布 Slax Reader？

原创

wulujia

吴鲁加

先说一下，Slax Reader 是个结合了 AI 能力的稍后阅读产品，可以免费使用，同时具备付费功能（毕竟要 AI 算力），只允许 Gmail 账号登录。

地址：https://r.slax.com，欢迎试试，也欢迎付费 ;)

开源了，也还是会收费的。

以下是正文：

--

前几天，我在群里发了一条：

>讨论：如果 Reader 索性开源发布，大家会喜欢，还是担忧？为什么？

同事们的回复普遍比较积极。

Zhiqiang：

>两者都有。

>- 喜欢是没试过开源一整个项目，有机会尝试了。

>- 担忧是光开源代码不够、还需要支撑，比如文档、issue 的处理、PR 管理这些。事情多了起来。咱开源除了表达一种态度，还希望能提供价值，仅代码的价值比较有限，支撑性的工作是蛮重要的一环。

>总体上，喜欢 > 担忧。

Senwei：

>总体来说我赞成开源

>- 有部分用户是喜欢自己部署的，开源能吸引他们（omnivore 停服的时候看到了一些这样的用户）

>- 开源大部分功能，一部分功能闭源（dify、lobechat 的策略）

>- 开源让用户自己接模型，如果用得多可能是付费更省钱，如用 cursor 的开源替代，自己接模型比 cursor 月付费要贵  （cline 多聊几轮就 1 美元了，可能还没把功能改好，cursor 月费 20 刀）

Huanan：

>喜欢 > 担忧 +1。

>我再补充个担忧的点，市面上整个项目开源的产品也不少，部署难度（特指后端）会直接决定我们能够吸引多少小白用户，但是碰巧，我们选择的依赖 Cloudflare 的 Serverless 以及后端依赖项目过多，我们的部署难度其实挺高的。需要用户绑定 VISA 信用卡、开通各种各样的服务配置才能使用~

Junchang：

>我这边的想法跟 Huanan 后面补充的差不多，就是目前项目如果要开源的话还是有点难度的，除了 serverless 那套我们还有个自己手动维护的 readability

我也记录我的想法，跟大伙儿讨论。

为什么开源

- 实践开源 。此前我们一直是嘴上说说，没有实际入局，现在有些精力和资源，有坑或者有利，我们不妨都尽力试试。

- 吸引社区贡献者和爱好者 。建设开源社区很有趣，我一直想试试。让我们有核心团队和松散的贡献者。

- 让产品有更好的灵活度 。能有机会接收到来自全球开发者的需求、代码。

- 倒逼我们的产品思考与迭代 。就得把 roadmap 公开，得能做得更优秀，才能挡得住竞争和抄袭。

- 作为新入局者增强透明度，建立品牌，抢老用户市场的方式 。

- Slax Reader 我觉得值得长期做，开源是对世界的贡献 。

第一步的考虑

- 不用特别在意目前的代码质量和文档水平，在行进中迭代 。

- 不用特别在意目前是否方便用户自行部署，可以先有文档说明 。

- 不用特别在意商业上能不能成功，我们部署一个实例，能成功最好 。

- 目标反而应该定义为 start、PR 等跟开源社区活跃度有关的。

长期看

- 用户能越简单地参与越好 ，所以文档、接口要慢慢完善。

- 用户能越简单地部署越好（docker?）

- 产品可以多一些与第三方的交互、整合，比如如果有插件机制，一个 url，有事实核查插件，有扩展深度思考插件，就可以带动大家的创造。

--

欢迎你加入我的[知识星球](http://mp.weixin.qq.com/s?__biz=Mzg5NDY4ODM1MA==&mid=2247483765&idx=1&sn=081af2bcd6c4247546b6f0178714510f&chksm=c01a8c44f76d05522990865187ff7152ae26d431fd1045259c8a1d873c9764cbc3b4617d8679&scene=21#wechat_redirect)，我们一起聊聊创业、产品、运营、阅读。微信识别二维码，付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款。——>[星球创业笔记传送门](http://mp.weixin.qq.com/s?__biz=Mzg5NDY4ODM1MA==&mid=2247483765&idx=1&sn=081af2bcd6c4247546b6f0178714510f&chksm=c01a8c44f76d05522990865187ff7152ae26d431fd1045259c8a1d873c9764cbc3b4617d8679&scene=21#wechat_redirect)。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sQicKibM7wlribpCmjeDrEKlMXO5L194xOpIvwEqHQN69e1QGT78V0nLoeaEs7B3g6OZA2RfjddUiaY49xgkC3WhBQ/0?wx_fmt=png)

吴鲁加

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sQicKibM7wlribpCmjeDrEKlMXO5L194xOpIvwEqHQN69e1QGT78V0nLoeaEs7B3g6OZA2RfjddUiaY49xgkC3WhBQ/0?wx_fmt=png)

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