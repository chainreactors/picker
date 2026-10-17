---
title: 打不过就加入？微步在线近期布局，意欲何为
url: https://mp.weixin.qq.com/s/JzEvzjwuxVMYssBFHI0emw
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:25:06.200417
---

# 打不过就加入？微步在线近期布局，意欲何为

# 打不过就加入？微步在线近期布局，意欲何为

原创

AI安全迪哥
AI安全迪哥

AI安全迪哥

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

手机没抢到，算了写个公众号吧..

近期微步一系列动作，布局了大量的开源产品的速成整合，今天迪哥应粉丝要求，写一些解读，部分参考公开信息，具体口径仍以官方为准。

一、 开源AI运营平台Flocks，快速缝合出品，收情报的钱

我把它整个仓库文件树拉下来数了一遍：技能库 5012 个文件，4891 个来自同一个社区包。

![](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczOgrZCzgzod2eT4tkAnzhyHE1pRamWpV1ZPEw0wtva1riak4VhyrX3pFU8jzITIBo2rv11Bh9ZAic876MfaUSmLsMsF00CELf6W0/640?wx_fmt=png&from=appmsg)

先看外壳。工具侧有 bash、文件操作、代码搜索、LSP，模型侧接 Anthropic、OpenAI、Google，会话和上下文自己管。安装是 curl 一行脚本，README 里专门给大陆用户写了镜像加速那条路。

这套骨架眼熟。微步对外说 Flocks 的逻辑和架构基于开源框架 OpenCode 开发、代码用 Python 重写了一遍。OpenCode 文档里内置 agent 的名字正是 build、plan、general，Flocks 介绍协同方式时用的也是这三个词。

![](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczNSTHR5D002T08q9g1E5zqibQ5w4AaYq7icUqM1V2m30ezaziam4ia1AIkc9svUyz8mJrGOlmHteNyvD9dFxToibcCtZ0C81A8bwxfM/640?wx_fmt=png&from=appmsg)

挣钱方法一句话就能说完：客户端不要钱，token 按量走，额度按天给。Flocks 是同一个形状——跑在你内网的那部分 Apache-2.0 随便二开，微步收的是在 X 情报社区的 Key 的钱。

二、CyberStrikeAI：收甲方安全治理的钱

9月7日，迪哥对CyberStrikeAI进行了工程化harness改造，引起了很大反响。

[CyberStrikeAI全流程改造教程，36步端到端自主渗透打造超级AI红队](https://mp.weixin.qq.com/s?__biz=Mzk4ODQ0NDMyNg==&mid=2247484265&idx=1&sn=2cb32d38bab4a6543b29c72da238d072&scene=21#wechat_redirect)

无独有偶，9月16日，微步宣布完成对开源 AI 渗透工具 CyberStrikeAI 的收购。它的技术路和 Flocks 完全不同：Go 写的，编排框架用字节开源的 Eino。

个人免费用，微步收的是甲方「安全治理」的钱。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczPbp0SbqcLb57ZCUJJ1pEXP0GWBqEhicJRf8EhBXzbO0MFcibQlpsPVTnGXQZ31moj4eymiaBgR0sY7vl93MKG9gq4JMnibSOJ8Frg/640?wx_fmt=png&from=appmsg)

三、OneSOC：AI原生运营平台，但并非全栈，且聚焦单域

One SOC并非开源产品，但是它是明显区分于外挂类AI的产品，架构如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczOtX0gUJOG2pVRkpMWW1tchD8NdhWs8zmraI4PBUU5CmUlQyC29PWlycorukoSjN1EchdItoX6BNddiahMy6z0fyae3A7Ago7NM/640?wx_fmt=png&from=appmsg)

收费三个维度：1）日均告警量 2）接入设备数量 3）开启场景数

产品功能设计架构与产品接入旅程：

![](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczPVCAEoqKMyyDKBHtD0OsNFgr0iaCFa2Dl8eibibPYficF4iac5H7roNtMpuhbONnjaNSMsPiaTr9ibq1LcEfqF517cQib048EDMOHOXk0/640?wx_fmt=png&from=appmsg)

实施部署步骤：

01企业邮箱开测试账号

准备 1 台主机部署 Broker

02设备告警逐条经 Broker 接入

支持 Syslog、Kafka、API

03导入资产并用 API 对接 NDR、HIDS、EDR、WAF、防火墙

补上工单与登录管理

04AI 引擎做初始研判

自动积累两套知识库，持续 3-5 天

05进入正式运营

同类告警降噪更快、相似事件研判更准

06用户反馈写回知识库

修正特定业务场景下的误报

这套形态微步自己的说法「保留四肢，只换大脑」——旧设备变成新方案的眼睛和耳朵，这个利旧的思路，充分戳中了当前安全运营的甲方痛点。

退订时甲方会失去什么

三类付费订阅都是甲方融合的东西，这是收费粘性的构建点。至于「升级不额外收费」——退订失去的不止一次服务，是能力生成、沉淀、转换的那条通道。

实际效果怎么样？

实际效果怎么样，要用过才知道，不要迷信厂商的说法。

四、RedAgents：一个AI红队的整合产品

这一步我原本想跳过的，一个平台页而已。看完产品页我改了主意，因为微步把同行做成了自己的功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczPCEOVKB2Ap13AjRtXJoUtkw0g0M87icM83EwBLZkSFoVnGP8Jl3VLnACQ4bWiaSjUM9SVvFUwVdcsnmp0lr4wlO1AEtMqtN8YRg/640?wx_fmt=png&from=appmsg)

VirusTotal 那个类比是微步自己写进产品页的。图上四个能力，前三个是别人家的商业产品，第四个是刚收进来的，但是完成了跟CyberstrikeAI的打通。

微步一再强调这叫「不必被单一厂商的路线图绑住」。这话技术上成立，商业上还有后半句没说：绑住的是甲方自己的建设路线。

五、四步合起来：能力是借的，组件是自己的

Flocks

拿走开源的 agent 分层和社区技能库，留下 X 情报社区的 Key。按 token 天配额和情报查询次数计量

CyberStrikeAI

拿走一个跑通 Eino 编排、铺满杀伤链的 Go 项目，留下「受控」这道墙。按授权范围内的任务量计量

RedAgents

拿走三家同行的攻击引擎，留下授权、编排、去重、复测。按并行红队次数计量

OneSOC

拿走你不想自建 GPU 的那笔预算，留下全量遥测归一化。按日均告警量、设备数、场景数三根轴计量

每一步拿走的都是别人做好的能力，每一步留在自己手里的都是能按量发放的位置。

微步做订阅不需要学。2022 到 2023 年的公开报道里，它的订阅约占总收入八成、SaaS 客户续约率接近 95%，这个口径之后没再更新，但是这几次的开源项目整合，几乎全部是SaaS化能力的绑定，通过快捷可起步的平台，批量化卖情报、卖组件，构建ARR收入。

六、留给用户的问题

用户其实不关心背后的布局，但是以下两个点是关注的

第一，对云端的接受度

以甲方的数据为例，如果把提取的AI语义数据发送到云端，很多甲方不接受。

第二，用户担心会不会未来出现一堆「开源产品缝合怪」

用开源产品做改造，是AI时代的「捷径」，但是整合改造的力度效果，取决于厂商实际的综合实力，当下网络安全产业萎靡，基本亏本的情况下，仍需谨慎。

预览时标签不可点

修改于

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczMFkIZFVysicQLgtKK5XzzLA5ZKFpKH3DVr5xYezuQr0bODOmhTKLR6vO27yRBf8rIJ625r4TqusibRY9Y9fdLiaEeVv9CXTbIGbg/0?wx_fmt=png)

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