---
title: 扣子 × SearchCLI：一个不会英语的卖家，靠一个 bot 卖到了日韩英多个市场
url: https://mp.weixin.qq.com/s/s2FFCkg2qH17wryFbnJYgA
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:59:55.534930
---

# 扣子 × SearchCLI：一个不会英语的卖家，靠一个 bot 卖到了日韩英多个市场

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FGB4hYw9Fef8fia2GzXdKvc4TO1XLqUo9qF0BJ07Gu47kxKUjhlY8AcrrQUPzPh6lwxx2tsKZ3nSGRibt7tNrAicia6rLg3S1N4sdAJIIcdenL4/0?wx_fmt=jpeg)

# 扣子 × SearchCLI：一个不会英语的卖家，靠一个 bot 卖到了日韩英多个市场

原创

Viking AI 搜索
Viking AI 搜索

字节跳动技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

做跨境的人，十有八九都在同一个地方栽过跟头——不是货不好，是语言这关过不去。

日本客户用一长串敬语礼貌地问尺码，韩国客户甩来几句口语化的短句砍价，英语客户上来就要精确到克重的面料成分。而且每新进一个国家，就等于要重新熟悉一拨新客群——他们说什么语言、习惯怎么问、在意什么，全得从头摸。

每多打一个市场，就意味着多养一套导购、多写一套话术。养一支多语言客服团队？小卖家根本扛不住。退一步用机翻顶上？又常常答非所问，客户问两句扭头就走。

**而这次的主角小 V，把这些坎全绕过去了。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedGSN5STm90cQCBtAicQlED09fQftvaO9YYgnqcb9HN2Ze3LcVUykD96ncxvuQQXQiaiaibeP04T7EWtSC5QhsvhPOiaB4AMnuI072M/640?wx_fmt=png&from=appmsg)

小 V 是个卖服饰的独立卖家，英语四级考了三次没过，日语韩语更是一窍不通，却想一口气把店开到日本、韩国和英语区。放以前，他的选择只有两个：要么放弃出海，要么砸钱堆人。

但他最后真正做的，其实只有两件事：**先用扣子搭起网页入口，再借助 Viking AI 搜索 CLI（下文统称 SearchCLI），在扣子里配置出一个会说日语、韩语、英语的智能客服 bot**。

💡**为什么是扣子 + Viking AI Search？**

扣子负责 "快"：自然语言描述需求就能生成完整网站，预览所见即所得，一键部署，不用自己配环境、调打包。

Viking AI Search 负责 "真"：纯大模型能聊天，但会瞎编商品、乱报价格；Viking 能把对话和真实商品库打通 —— 用户说什么，它就从两千多件 SKU 里检索、理解、推荐，给出去的每一件商品都有图有价有链接，点一下就能进详情页下单。

从此小 V 负责发货，bot 负责听懂全世界。下面就跟着他，把这套东西一步步搭起来。

**一、快速上手：几条命令，开启智能搜索之旅**

SearchCLI 的安装和配置极度精简，繁琐操作都能交给 扣子 在对话里自动完成。

**1、安装与授权**

小 V 的第一步很简单：打开扣子，让它自动下载和配置。

💡 **复制这句话发给扣子：**

“帮我下载这个 CLI：https://github.com/volcengine/SearchCLI ，并告诉我是否运行成功。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fee3A5qEhAJuOIH19nqMUtzVicmqIknicxMUkrD2vOG9sMAVoLxZM61R0tlQhDLk4YYLNXuOM5q5RXVYNDn9K7bBdZD9G9hMNcbOU/640?wx_fmt=png&from=appmsg)

扣子对话界面-安装 SearchCLI

装好之后，去火山引擎官网拿一组 AK/SK（鉴权凭据），按 Agent 的指示在终端里填进去，授权就自动配好了。整个过程不到 5 分钟，基本是零手动操作。

💡**如何获取 AK/SK：**

点击 火山 AI 搜索首月体验版（https://console.volcengine.com/aisearch），注册火山账号，获取 AK/SK 即可体验产品功能，**首月仅需 9.9 元** 🥰

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fecl68XBh2B3ccO1cIvs6IbqIInaGdF4ZX48icW1CFPBHShEPNdiaZRaAibdBeqib2OUGuJFxrqLUwlzcljyolKxWI1beY4RUicViaOYE/640?wx_fmt=png&from=appmsg)

获取 AK/SK

**2、数据入库**

权完成之后，小 V 要做的事情其实很简单：把商品数据交给 SearchCLI。

导入这一步完全不用亲自动手。SearchCLI 把这条链路拆成了三步：

1. 基于 vs item profile，扫描数据、识别字段结构，自动分析文件的 Schema

2. 执行 vs item plan，生成入库方案，规划字段映射和写入策略

3. 通过 vs item apply 执行上传入库，自动完成数据入库并构建底层索引

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedwSVDxOm6lT5NFk7IrDhwkq9I0Ez96ePrWagiba1zxCIPo9r3XaNjOx8arcOP8mcrdbL64eOq9ibpniaJIdCJqmmCicEiabqxduT4Y/640?wx_fmt=png&from=appmsg)

SearchCLI数据入库三步法

原本几天的活，被收成了一条能顺着跑完的链路。小 V 不用自己写脚本清洗、拆字段、调接口，商品数据就这样有了可直接拿来做搜推问的底座。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedcxNqePK4KjNaTpz34DQ2QjObVYYaFgWibziaoJ7iauK7UTDfZ1p0ePMn4RyLwsCBp8fxc5uTyX9qiagphkhnlxcajhEENNJ6KleI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fecejo8VvOtxxibyq0LH3JDxyHicXXO7rfaatxbjtPicWbxwC6W1ppJ3q1QuCXyO8vB7XOvsohs6zpVz6aGXCBhAQSvkpbgESiaztQI/640?wx_fmt=png&from=appmsg)

扣子对话界面-日语-上传数据

扣子对话界面-韩语-上传数据

**3、搜索、推荐、问答策略自动生成**

数据备齐之后，小 V 终于走到最关键的一步：**让这家店真正开始做日本、韩国和英语地区的生意**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedicXxgrd38PXL2HiclQn8MgLH5EQ1OcfD23reZjDYqlRlxM7bTCAUWCFnsOjwmKteLiaIiagptKOCib4haKqG0Bv7S3MOm6GvzzmeI/640?wx_fmt=png&from=appmsg)

但这一步并没有想象中那么折腾。**因为对 SearchCLI 来说，建多语种应用并不是重新开一条新链路，而是把已经跑顺的那套流程再复用一遍**。

商品怎么入库、搜推问怎么配置，这套流程一旦跑通，接下来建日语、韩语、英语应用时，基本照着再跑三遍就行。

于是，小 V 把这套 “建应用” 的流程照着跑了三遍，先后建出了日本、韩国、英语三个语种应用。没有额外的复杂开发，也不用为每个市场从头再搭一遍系统，三个市场就这样陆续跑了起来。

更妙的是，每个应用里搜推问一体的能力都是开箱即配，客户用什么语言进行问询，它就用什么语言回应。

**1.1 多语言搜索**

SearchCLI 内嵌了包含文本与图像的多模态检索配置，搜索能力即刻可用。

小 V 试着在扣子韩语应用的对话里搜了 "适合通勤的外套”—— **结果不再是靠关键词硬匹配，而是真正理解了他的意图**。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FefV1cGqgPQOicOKOibb2icHCQRxIS8W5KGN6FuuZ2z4kxOC9bjCOBKd7JYDy4ddLj2jqDP8eOz8uUAlAPapCugeT8lzsmrvm4MibYQ/640?wx_fmt=png&from=appmsg)

扣子对话界面-韩语-搜索效果

**1.2 个性化推荐**

搜索能用了，但电商客服不能只是"等人来问"。很多用户不是带着明确问题来的，而是边看边犹豫：这件衣服有没有更百搭的颜色，这双鞋有没有类似款，这条裙子还能搭什么。

小 V 继续让扣子把推荐场景配起来。即便一开始没有足够的用户行为数据，也没关系 —— 小 V 把店铺卖什么、用户大概是什么人群告诉 扣子，它就能先**生成一份冷启动用的模拟数据，让推荐系统跑起来**。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9FeejfpialPTLKc0vEnZrc4JvBnVIy4g87cosgNqfRFmQZWJ4nicskHrPbjKlWI9SLEibJpZZ7wx9cwYSteibT6iantDvKGbw1kRreJBg/640?wx_fmt=png&from=appmsg)

扣子对话界面-日语-生成模拟行为数据

SearchCLI 自动完成了事件类型映射，并成功创建了推荐物品的功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedaWPIYa4SwvA7nib9WwOO6mDm9XEVU76BI4aGTchwjNdhw3mekqSXt6vA80Bg4ouT8x1CHEXfQXTasV17IDMcHfjnG98dH14ibE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedquRbCm165Dxh4XUyKcKSZuicYzfUSiaYofygZDQ9AGGR6mgtVFicibfX4iaFELPmxiadCfhbVBaOIQblr204zo1a3GkZGwsGspibLoE/640?wx_fmt=png&from=appmsg)

扣子对话界面-日语-上传行为数据

扣子对话界面-

日语-配置推荐策略

**1.3 售前问答**

别小看这一步，真正临门一脚影响成交的，往往就是这些细碎但关键的问题。尺码怎么选、面料怎么洗、会不会缩水、穿上会不会显臃肿，客户不问清楚，很难放心下单。

以前这些问题得靠人工一条条回，现在用 SearchCLI 接上问答能力，其实就是一句话的事。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedAsolGfK4X68vQSZiaHcpvqPCp6lOVu0FBgSEKd804H1Vthiaib0Px8tic2DFgqibRXU47bcRqicibZQ5ico6TMFwoMen531VosmUUkGU/640?wx_fmt=png&from=appmsg)

扣子对话界面-日语-配置对话场景

接进去之后，bot 就能像个懂行的导购一样，不管面对日语、韩语还是英语客户，都直接用对方的母语把这些下单前的顾虑解释明白。

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Feew1ic4EY2pyIhZibze1boYQE9wthkeyzuhvhOjmI9Rbn4Wic0064fN8lY3FM5lJnBTiaoZd7HFN4vpejIueHjsGb7iaaGYPZunlVRw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefAicIKFicuvsrhS2prPicNqMicWlnWLGxbxtibTXzgMsPA44vgYw3licXlIKAc0xicXZYMiaPyVACbKIQEibh85q940yNia7zasAOFauBmY/640?wx_fmt=png&from=appmsg)

日语-问答效果示例

英语-问答效果示例

**4. 效果评测与自动化调优**

能跑起来只是及格线。小 V 心里还有个疙瘩：三个语种，到底答得准不准？要是搜不准，又该怎么调？

放以前，解决一个“搜不准”的问题，常常得靠算法专家盯着一堆 bad case 排查好几天。现在，SearchCLI 把这条路铺成了一套完全自动化的闭环：

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Feeuq4WicL8WuicIibb6e7HrV9vAYMqwfmp8ABswkickd5DThDicibyxdjmnWny3YbqlXSr4oN9YvUHRmlyBeq3s3Eicib00edmzyuj8HicY/640?wx_fmt=png&from=appmsg)

* vs search tune query-generate：小 V 没有现成的测试用例？没关系，SearchCLI 提供了**把 “构造评测集” 这件事直接简化成一个命令**：基于已入库的商品数据，为每个语种自动生成多种意图的评测 Query。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9Fefy9tILeHmvZVhuWFzXZBDy5niaUFldfe83Lh4ia3k9ZG84PabrW0L60PX18icEhtKyTF3YfzeKcq61uib55hvu2iaGAgAkNJWvfice0/640?wx_fmt=png&from=appmsg)

扣子对话界面-构建评测集

* vs search tune run：对不同召回策略批量跑分，得出一份能直接对比优劣的评测结果，他什么都不用做，看着它跑完就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeeXbkqE5FjdRdCqU7icU3ibxceyc790BAHUTfVkrBkvNAsTJmC4Hay58ericObuF3CDYs3ENX05CIKRF2w0GCqBicpRqPXicrqvzHmg/640?wx_fmt=png&from=appmsg)

扣子对话界面-批量评测结果示例

* vs search tune report：不仅指出 “哪里有问题”，还会**直接列出实用的策略配置建议**。别的工具帮你看清问题，**SearchCLI 直接帮你定方向**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedZHwZCrG0wvoibcHccJicgPm7KfJ4hJaDrH5tksLZukbACiaWlg4AobCfO8RCghGyJ81NXMWhYVg3KfCgf2EGeWowWde5BiaXyeW8/640?wx_fmt=png&from=appmsg)

扣子对话界面-策略配置建议示例

* vs search tune apply：一改完再跑一轮评测，小 V 很快就能看到结果。推荐侧的重复率下降了 58%，Novelty 提升了 5.5%，**策略效果大大提升！**

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Fed8ibXGFIy4CTIkian8xovXDW8KdDzWUk6ZLib6MabaROGibhOFPvtUP61JyZjjg7rthWia9Ue4z7T0ZHgmemFrl65e67On8FZRO8sc/640?wx_fmt=png&from=appmsg)

扣子对话界面-不同策略效果对比示例

**二、走向交付：三步搭好一个能卖货的网站**

前面的工作，解决的是 “搜推问能力怎么配”；接下来要做的，就是把这套能力真正装进一个能面向客户使用的网站里。

**1、先把网站搭起来**

小 V 在扣子里把自己的需求说了一遍：跨境女装网站，首页、商品列表、详情页、购物车、结算页都要有，并且还要有能集成导购助手的悬浮机器人功能。

话说完，网站就跟着出来了，客户进来能逛、能看，悬浮 bot 也出来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FeeDpWpf8iapvia6PCcl9qXUPHlfEKIPK1Ps5kZIRRVOUwjWUKBvk7OicvdHFfEwh4qaLWUMFMSWbkW6snQmnTGBuQpS44R8PSOU2Y/640?wx_fmt=png&from=appmsg)

扣子对话界面-生成电商网站

![](https://mmbiz.qpic.cn/mmbiz_png/FGB4hYw9Feetqn83ricQj6tdTia58ME3xjq6tqGnZK1H5ypdXibvWA0lLFA23icvRZcRqrFAzeTRYcp23fGUwAPicbjXicicjFegEdhqiadUtMcBIia8/640?wx_fmt=png&from=appmsg)

电商网站-首页

**2、把导购能力接进来**

页面搭好之后，接下来的关键，就是把前面已经配好的 Viking AI 搜能力真正接进来。这样一来，这个 bot 就不只是 “能聊天”，而是真的能听懂客户想找什么、在问什么，再把商品搜出来、推出来，把尺码、面料、洗护这些下单前最容易卡住的问题讲清楚。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FefmtSrBeze9qXGIx6nOFld0yEKJRMAgW2Wo1hS1YR1JV8ribSzsfALK310aOKC1VacEFgeM1lNlExd0icFqB1V2VpNrXoMiapJMcA/640?wx_fmt=png&from=appmsg)

扣子对话界面-部署导购功能

这一步最省心的地方在于：对接的代码 扣子 已经帮你写好了。后端自动按 V4 签名直连 Viking 对话式检索 API，流式 SSE 打字机输出、商品卡片解析、会话 ID 管理、request\_id 透传，不用自己改一行代码。小 V 要做的事只有一件 —— 点右上角的「部署」，在部署面板里找到「生产环境变量」一栏，点「+ 新建变量」，把 Viking 控制台里拿到的四个值填进去：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FGB4hYw9FedldlrOFQkNf1tQvbRfMXqCO29mib54P4c1DJ5Mi...