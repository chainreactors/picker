---
title: 我被诈骗了
url: https://mp.weixin.qq.com/s/EvuLYbWFixTqp6M8JBsp3A
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:48:31.799347
---

# 我被诈骗了

# 我被诈骗了

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于州弟学安全
，作者爱州

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM4k2aH4YiaCfWiaA255TBo8n28qZ4pVoM1BT1zZJaibWWCJQ/0)

**州弟学安全**
.

太极生两仪 非黑即白 正义之道，注重从基础理论到实战的每一步，小白-有经验只需要这些就够了。

**本篇文章共 7000字，完全阅读全篇约10分钟**

## 前言

**我就知道你是因为看到这个标题点进来的，首先给点进来的朋友，澄清一下：我没有被骗到钱。思来想去，还是用了这个标题，因为这大概是我离诈骗最近的一次，近到我能看清它的每一个环节是怎么运转的。**

事情发生在上周。当时我正在写文章，微信突然弹出消息，我被一位好友拉进了一个群。拉我的人叫宋某，是我以前租房时上门修过暖气的师傅。

也正因为我自己从事网络安全行业，接下来的几个小时里，我一边"配合"他们的剧本往下走，一边把这套骗局的话术、分工、软件、服务器拆了个遍。这篇文章就是把整个过程写出来：前半部分讲骗子的剧本和生意经，尽量让不接触技术的朋友也能看明白；后半部分是对诈骗软件的技术分析，供同行参考。

动笔之前，先作几点说明：

1. 本文为真实案例复盘，写作目的只有一个，就是反诈科普。文中对诈骗手法的还原仅作剖析与提醒，请大家不要模仿，更不要抱着"薅骗子羊毛"的心态去尝试，原因我会在文中详细解释；
2. 分析中示意图涉及到的金额均为举例，并非真实金额；
3. 文中对涉及的普通人信息做了必要的脱敏处理，诈骗团伙的服务器地址等威胁情报信息则按照安全行业的惯例予以保留，方便防守方封禁处置；
4. 天上不会掉馅饼，掉下来的往往是陷阱。如果这篇文章能让您和您身边的人多一分警惕，也烦请转发给亲朋好友看一看。

同时我也制作了视频讲解，感兴趣的各位可以移步观看，并转发给长辈家人：

## 一、骗局的开场

被拉进群后，宋某很快发出了话术和二维码：帮"好朋友"的影视推荐群做推广，进群保持安静，群主稍后会发放多个大额红包。

![](https://mmbiz.qpic.cn/mmbiz_png/mOj9kVLGEa1HdQYfGybmTLqbUXxVBuUl381rbkiak2ZTfcINwGfw471o5TkibeOVrrI5ic1Ic1Ltsmx3Uow6GRia5DjibibPRShiav7GBw4xtvsCMs/640?wx_fmt=png&from=appmsg)

宋某在群内发布的拉群话术，引导大家扫码进入所谓的影视推荐群

宋某就是那位修暖气的师傅，他突然拉群、突然发推广话术，我的第一反应只有两种可能：号被盗了，或者被人花钱雇了。结合以往的经验，以及和做反诈的朋友交流，我更倾向于后者：他在做"兼职"。

这类兼职的链条，大致是这样运转的：

1. 境外的诈骗盘口把拉人头的需求，通过一些境外聊天软件分发给国内的黑灰产头目，这是第一层，此时单价还很高；
2. 一层继续向下外包：需要多少人拉群、多少人发红包、多少人负责引导进诈骗软件，分别报价；
3. 层层转包之后，最末端的"业务员"找到了宋某这样的人：你只管拉好友进群，按照我们给的话术和二维码去发就行，有多少人成功进群，我们就给你结多少钱，我们是纯绿色平台，没有任何影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mOj9kVLGEa3E0FufmaQHE8CQ4gCekYPpSibq2z8Zj1RUZyIKewqMhS2y6prMicT8IldEhrlP3e172ibGv5LdRMqCRUKdbDpN2zNvZcVWzmf7rA/640?wx_fmt=png&from=appmsg)

从境外盘口到宋某的多级分包链条（示意图）

请大家留意这个话术的设计："我们是纯绿色平台，没有任何影响。"这句话不只是说给进群的人听的，更是说给宋某这样的兼职者听的。如果一个人清楚地知道自己是在给诈骗团伙拉人头，他大概率不会干；但如果他相信自己只是在做一份发广告的兼职，这点钱就赚得心安理得了。所以某种意义上说，宋某也是这场骗局的受害者，只是他自己未必知道。

至于诈骗团伙为什么不亲自下场拉群、发红包，原因也不复杂：自己干这些事，既要养号又浪费时间，还容易被平台风控和溯源；层层转包给兼职者之后，成本和风险都转移了出去，溯源的难度也成倍增加。他们只需要坐在最后面，等前面的人把"流量"引进自己的地盘。

## 二、一场精心编排的群体表演

进群之后，果然是老套路开场：先发红包，让大家过过瘾。

![](https://mmbiz.qpic.cn/mmbiz_png/mOj9kVLGEa2DJN1eia59sRbuPBx121gsnr9PTAuZcGUfqPMvt5xRWqYdRKictibgVseGHdtkcIfUqgmQl5ViamvLqXicxBUmsbYolBUeTIRc2ToQ/640?wx_fmt=png&from=appmsg)

进群后的第一轮红包

发红包的人叫 KK。这里多说一句，KK 和宋某一样，也不是诈骗团伙的核心成员，而是另一个"兼职"：他的任务就是发红包。可能是找到宋某的人也找到了 KK，也可能是同一层级的其他人招来的人，总之每个人只承担链条上的一个环节，彼此之间甚至未必认识。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mOj9kVLGEa0hoPQ0T8WcyuPkBlB1xsr1se2Jb5apDu8Db1pJjoXlxxvicnxUHtA6ebRyBvXMNY0F52faadE7y0tMpfDiaL4rudKgrvht1YnzI/640?wx_fmt=png&from=appmsg)

发红包环节由兼职人员 KK 负责（示意图）

红包发完一两个，剧本进入正题：有人开始以"影视短剧推广"的名头发布任务。发话术的人叫怡，同样是兼职，只是分工不同。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mOj9kVLGEa16ia9O9ORGVWiaP5TURG9I9oxL5jtKOA6n2UHXrYt9Q0TpPr8ECKSibc2y5usZiczicl3QJTEDpV4P69eRkic0qLRFEELDm9NlcP0Wg/640?wx_fmt=png&from=appmsg)

怡开始以影视短剧推广为名发布话术

![](https://mmbiz.qpic.cn/mmbiz_png/mOj9kVLGEa0iawibn5Oiaf37JnmlSdIGw7Rqr2sanEQIXibiaQDE6MWsA29yicTyHOFdtnsBWldqrvHmco2hV5jgTuUppr0hH8l3NRSVd2T46vpn0/640?wx_fmt=png&from=appmsg)

发话术环节由兼职人员怡负责（示意图）

可能有人会好奇，拉群给钱、发话术给钱、发红包也给钱，为什么发红包的佣金反而更高？这一点我专门请教过做打击黑灰产的朋友。原因出在账号代价上：短时间内频繁给大量陌生人发红包，极易触发支付平台的风控，号可能直接废掉。对骗子来说，与其自己养号冒险，不如花点钱让兼职者来承担这个成本。久而久之，愿意干这个活的人少了，价格自然被抬了上去。看明白这一层就会发现，这条产业链上的每一分钱，都被精确计算过。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mOj9kVLGEa0jTSnVicp8vG6RpdzMoT35XVcwHAibfibzGsVnUI29ex4Km4u7jXtUbNCtIpp8RRLd42zr8BvvYrRGBNXibdXGPRYRDyaBraibooeY/640?wx_fmt=png&from=appmsg)

所谓的任务：浏览几秒截图发回群里，即可领取几元钱

没过多久，群里陆续有人晒出到账截图，六块钱、二十五块钱，一张接一张，群里开始齐刷刷地刷"666"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mOj9kVLGEa3YqDhrK76lmQh9lj0rA8rWKD0blic8OSaKNJZYqbUfMjORWRpKpqCSVO2ze0xt2jJECic0oUjnVibROFN6f1DU64BolGUyZf6fe8/640?wx_fmt=png&from=appmsg)

群里陆续有人晒出到账截图，气氛被烘托起来

到这里，这场戏的第一个钩子已经放下了。心理学上有个概念叫互惠原理：人一旦接受了别人的好处，就会不自觉地产生回报的心理，警惕心也随之下降。这几块钱的红包，就是骗子买入场券的钱。

还有一个不太让人舒服的真相要告诉大家：这个群有一百四十多号人，除了被拉进来的目标，相当比例是骗子自己安排的"托"。你看到的踊跃晒单和满屏的"666"，未必是真实反应，而是被设计出来的氛围。心理学上管这个叫社会证明：当我们判断不了一件事的真假时，会下意识地参考周围人的做法。当"周围的人都在赚钱"时，怀疑反而成了一件需要勇气的事。

我照着流程做了几次任务，前后领了三十来块钱。这里必须诚实地说一句：钱是真实到账的。这正是这类骗局最迷惑人的地方，它不是一上来就骗你，而是先让你赚到钱。

## 三、四十分钟，从微信群大转移到他们自己的地盘

铺垫做足之后，话术变了：后续的"长期任务"不在微信群里发了，需要下载一个他们自己的"影视 APP"，在 APP 里接单。

![](https://mmbiz.qpic.cn/mmbiz_png/mOj9kVLGEa0rcE5LQ05n82XC7MYc1C6iadNSWVcUdgtjmxSAH6o11yiaj8pibictibkBkwsLMa90Lkfsvibgz7uUNB4cjCvsDG0RRsUHnGkACVpHc/640?wx_fmt=png&from=appmsg)

话术转向：后续任务需要下载他们自己的 APP

![](https://mmbiz.qpic.cn/mmbiz_png/mOj9kVLGEa2kxnJoMITkp6M5O3plia1IKtBucBQemwM4W8QicrtaFusApBA2aP052F3lhXZE1OOWzd5ZmicDGxcdTSGwYSHib2XK8KLZoViaSED8/640?wx_fmt=png&from=appmsg)

群内发布的安装指引笔记，内含多条下载地址

与此同步，我下载了安装包，顺手做了反编译，结合 AI 辅助开始对这套软件进行逆向分析。

群里的托继续烘托气氛，有人晒出下载 APP 后领到的几十元到账截图，越来越多的人开始"争先恐后"地跟进去。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mOj9kVLGEa16FibfQNIZKvxe8aXrEjtDsUsNPN6k8TPicwBp4gN0R5DdtLAetuACmoibCFTDWeD1SXHBtRLDUAibH6Gp3wlDbwPoXJarIicdVAZA/640?wx_fmt=png&from=appmsg)

托在群里晒出下载 APP 后的到账截图，带动大家跟进

从我被拉进群，到大部队被引导进诈骗 APP，全程大约四十分钟，非常迅速。这就是一条标准的流水线：微信群只负责获客和初步筛选，真正"动刀子"的地方是他们自己掌控的 APP。到了 APP 里，和受害者对话的就是实实在在的诈骗人员了，行话叫"狗推"。整个链条到这里形成闭环：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mOj9kVLGEa2ic5dZa29KoYFCHFA1UvWbiaIIvMdR8X0vFrRqRUKSOXq738WtOFIepDqxVuhsXmQ6CZqSaIAiaZic7uphqACqePgEfyWQhbuA8jQ/640?wx_fmt=png&from=appmsg)

从微信群到诈骗 APP 的完整闭环（示意图）

这里给不懂技术的朋友解释一下，为什么非要换地方不可。微信不是法外之地，诈骗话术随时可能被平台识别，账号随时可能被封，所以他们要以最快的速度把人转移到自己的地盘上。在那个 APP 里，他们是管理员，拥有绝对的控制权，微信的风控规则管不到那里。这个细节，后面还会起到关键作用。

## 四、甜头与收网

进入 APP 后，剧本还是熟悉的配方："助理"主动加我为好友，继续派任务、发佣金，甜头继续给。

![](https://mmbiz.qpic.cn/mmbiz_png/mOj9kVLGEa2ZL6gxfXVE5mumHjJEicakRHls4Mj989aIia7XoPw6AyKwx7jDPPukdznkyjIwAPg1fREbrvkgvQLIUQ1tnZl5hYwqg44CEKuA8/640?wx_fmt=png&from=appmsg)

APP 内的"助理"继续派单，搜索指定服务号截图即可领钱

与此同时，我在手机上架好代理，开始抓这个 APP 的通信数据。结果让我有点意外：这个软件的通信没有加密，也没有任何代理检测，数据包一览无余。以我的经验看，即便在同类诈骗软件里，这也算做得相当糙的。这也从侧面说明，这类套壳软件追求的是批量复制、快速上线，安全根本不在他们的考虑范围内。

数据包里有一个接口引起了我的注意：`getSensitiveWordsList`，从名字就能看出，它拉取的是一份敏感词黑名单。点开内容一看，黑名单里的是"骗子""马扁""骗"这类词。也就是说，只要有受害者在群里醒悟过来、喊出"**你们这群骗子**""**他们是骗子**""**他们是马扁**"这些话，这条消息就会被系统直接吞掉，群里的其他人根本看不到。

![](https://mmbiz.qpic.cn/mmbiz_png/mOj9kVLGEa3e5cUej8HEHlHN56fX1ww2sj5bBBQ8uhZxmu9r1M2bH5eGRQy9RxXSzALgtXMrWradaKsIrueA10qPPsIzhjY8icvHT2MibNbBQ/640?wx_fmt=png&from=appmsg)

抓包发现敏感词黑名单接口，"骗子"等词会被系统直接屏蔽

大家可以设想一下：在那个群里，你环顾四周，看到的是热火朝天的晒单和感谢，没有一个人提出质疑。你以为是自己多心了，但真相可能是，醒悟的人并不少，只是他们说的话，别人永远看不到。骗子不光写好了剧本，还提前制造了"沉默"，这确实让人心酸。

顺着抓包拿到的服务器 IP，我又去威胁情报平台做了检索。结果显示，这批服务器部署在中国香港，以集群的方式成段开通、轮换着使用。

![](https://mmbiz.qpic.cn/mmbiz_png/mOj9kVLGEa3h9p201ickQjic3H78ZFmqzjcX0BMGsiam57cEYaUgG4SHDlgxw2yonM5O93ia9rt2IbRxPb6SmRRKYjrl2ZedtzTWZr3SOMyyZcM/640?wx_fmt=png&from=appmsg)

威胁情报显示该团伙服务器部署在中国香港

回到 APP 的群里，甜头已经发得差不多了，大部分人累计"赚"了一百元上下。就在这时，剧本翻页了：助理开始发布"电影票房预售"活动，名义是帮影视公司做票房销量，方案从几十元到一千多元分成几档，标注收益百分之三十，先付钱认购，完成后连本带酬一起返还。群也悄悄开启了全员禁言。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mOj9kVLGEa2wVa5cXIz1RvnA1tHgr0JUqklaV7HzaFFlXqveNkmPIWpLrnVZSVN0GiaEyUibspBHBy9jsN8Y4QibMQHUFZAEAXvibxnvkD6yzsY/640?wx_fmt=png&from=appmsg)

收网阶段的预售方案，金额从几十元一路抬到上千元，群已开启全员禁言

这里需要特别说明：话术中出现的公司名义均为骗子冒用，请大家不要对号入座，正规企业绝不会以这种方式做推广。

接下来就是这类骗局最经典、也最狠的部分。当受害者第一次投入小额资金时，骗子大概率会爽快返钱，本金加佣金一分不少。这一步一石二鸟：既证明了自己的"诚信"，也完成了筛选，连小额都敢投的人，才有资格被放进长线。等受害者鼓起勇气投入大额，话术立刻变脸：系统提示"资金被风控冻结"，需要再充值一笔钱才能"解冻"。很多人卡在这一刻想的是，我已经投了这么多，不充钱解冻，之前的就全没了。心理学上这叫损失厌恶：失去带来的痛苦，远大于同等得到带来的快乐。骗子赌的就是这个。

于是就有人会问了：既然前期真能领到钱，我见好就收、薅完就跑，骗子不就亏了吗？

我在群里的时候也算过这笔账。假设骗子给 10 个人每人发一百元甜头，成本一千元；这 10 个人里只要有 1 个人上钩，被"解冻"话术榨出来的就是几千甚至上万元。这不是赌，这是一门稳赚不赔的概率生意，骗子根本不在意支出多少，只要最后是盈利的就行。你觉得自己能全身而退，是因为你此刻正冷静地坐在屏幕前读这篇文章；可真到了那个被话术、被氛围、被自己的损失感层层包裹的场景里，能果断抽身的人远比想象中少。所以也借这里再次说明：我写这篇文章绝不是教大家去赚骗子的钱。你盯着的是他的甜头，他盯着的是你的本金。

到了这里，我没有再继续做任务，把注意力转向了这个软件本身：它的背后，到底还藏着什么。

## 五、拆开这个 APP

交代一句背景：我平时的工作是网络安全，逆向分析和渗透测试是日常吃饭的手艺。结合Ai辅助的情况，接下来的部分会涉及一些技术细节，我会尽量写得通俗，不接触技术的读者看结论就好。

反编译打开这个 APP，业务代码一览无余。在一个名为 `Host.java` 的文件里，集中定义了上百个服务器接口，前面提到的敏感词黑名单接口就在其中；钱包、红包、实名认证、群聊等功能一应俱全，是一套完整的仿微信资金盘框架。

![](https://mmbiz.qpic.cn/mmbiz_png/mOj9kVLGEa2mCVfRLTNAK3K9ia7wQa7XnMZoSnczibaib9uTEY94acgiag0osvYam6ewmwPmoUaO5e6AuvDSOnmeTbRATCCkujGTyU1rN5VIABA/640?wx_fmt=png&from=appmsg)

Host.java 中的接口定义，红框处即敏感词黑名单接口

这个文件里还硬编码了 5 个"线路分发地址"（`api.sdmurv.cn/api/nodes`、`42.193.214.104`、`43.103.43.237`、`43.154.251.80/upload.php`），作用是旧服务器被封之后，给 APP 下发新的服务器地址。其中有一条比较特殊：它寄生在某正规公司的公共云存储上。那家公司纯属被冒用，与诈骗无关，这里就不写了。也算顺便提醒做云服务的同行一句，公共存储桶的权限和内容审计，值得...