---
title: 一个普通黑客通过 ARTEX AI 工具，两周打穿了 7 家韩国银行
url: https://mp.weixin.qq.com/s/qGSiQGNPewK4J4f-0GdN7Q
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:58:31.125105
---

# 一个普通黑客通过 ARTEX AI 工具，两周打穿了 7 家韩国银行

# 一个普通黑客通过 ARTEX AI 工具，两周打穿了 7 家韩国银行

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#AI安全#威胁情报#攻防演化#防御模型

> 本文技术事实主体来自 CrowdStrike Intelligence 官方博客《Unknown Threat Actor Uses AI-Driven ARTEX to Target South Korean Finance》（2026-10-07）。

！！！好家伙，还得是黑客们，直接干上了路透社

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNot6lWviaH94RNY5FXqbvx8zgqialJOOFQSnOC2jpHNTTfFCmPotwy9qU0nl8DvtmQN87GicdCCpwUo4oddWmHfKgATxrWOfALS8IQ/640?wx_fmt=png&from=appmsg)

事件发酵后原作者迅速删库跑路，发表声明

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PIWj1VguNovDwjFKK1VNQoQ4nd8NMKuFbIKIQA2VuYKicGBK9TQI4RRqK7lP6fFeMjRwvtrXwNNsDguAp2b77pqeoMezpW3GAUkD5oy5STUk/640?wx_fmt=jpeg&from=appmsg)

---

# 01 事件速览

2026 年 10 月 7 日，CrowdStrike 发通告：一个身份不明的行为者，用 AI 智能体渗透工具 ARTEX，在两周内打穿了多家韩国金融机构，数据外泄。按韩国媒体报道，受影响至少 7 家银行、两家大型教会，约 6.8 万人的信息流出，有些带着年收入和贷款额度。动静大到路透社都在跟进——还得是黑客，直接干上国际媒体了。

攻击者的全部行头，摊开就这么点：一个开源仓库的下载、两台服务器、几张大模型 API 的账单。个人量级的投入，打出机构量级的事件。

这个故事最要紧的地方，一句话讲：AI 把"打穿银行"的能力降到了个人下载的级别，防线不能再按"对手是专业团队"来画。

# 02 工具与打法：AI 把门槛降下来了

工具是 ARTEX，开源渗透框架，出自中国开发者之手，本意是红队演练。它跟传统框架最大的区别在干活的方式：不是一行行命令拼出来的脚本，而是一个 AI 智能体在跑——自己规划攻击路径、自己找漏洞、自己执行，接哪个大模型都行。

这次现场抓到的模型栈挺具体：

* 主后端 DeepSeek v4.1-flash，通过 API 转售站 xcai[.]pro 调的；
* 另备 GLM-5.3（智谱 AI）和 Grok 4.6，跑额外的会话。

三个模型一个意思：这个不答，换下一个。渗透方法写在 Claude Code 的上下文文件.claude/CLAUDE.md里，中文写死"模型应该怎么打"——整个方法论是配置化的：意图人定，活儿 AI 干。过去要十年经验、自研武器库才能撑起的节奏，现在变成几天的配置工作：下一份开源工具、充两个 API 额度、写一份提示词。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNouibIbNVGXRGXbIHghE1KtnTD6lV9jibepsCTichicLPhoGuQ0j9GqjsIS65k3QcAdcaIVziawJuotbI7Ggy3ywWFhGxmlUkgs87xes/640?wx_fmt=png&from=appmsg)

图1｜AI 代打的全部家当：一个智能体、三个模型、一个转售站

打法上也没挑重担。网银和手机银行是各家防御最重的地方，碰都不碰；被打的是贷款中介查询页、员工移动办公支持系统这类边缘系统——暴露面大、防护薄，也不在核心监控视野里。两周打穿 7 家，这个节奏靠人盯是盯不住的。

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNov7fTziaiaodXbBNRKakdVhEjIbL4aFnWKUHfzQvNvnVfYCCEdqRicxOgcT5oFlIacKJQibMnR6q0zwoKfG1rfxgliaqtr2ib8EBmTOQ/640?wx_fmt=png&from=appmsg)

图2｜防御最重的没碰，暴露面大的全中——AI 批量打的就是边缘

两件事值得记：一是整套技术栈公开可下载，没有自研武器库的个体，也能维持两周的高强度渗透；二是"对手手速等于人速"这条假设作废了，对手现在按机器速度跑。

# 03 情报怎么来的：攻击者把作战手册留在了网上

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNotUOibMcawy1CZSoyX8iaDyUOKgk4fUUubIzOicRpbmBAGCSYVU17G7AGQTiaodgBLVG9F7tQCPicVMc0GxibicGKyawlxH8qF0rLLUAM/640?wx_fmt=png&from=appmsg)

CrowdStrike 能把这次攻击拆得这么细，因为攻击者自己的开放目录里躺着一切。从托管 ARTEX 实例的服务器上先捞到.claude/CLAUDE.md和中文提示词；顺着文档里露出的香港 IP，又翻到更多开放目录：Claude Code 会话历史、ARTEX 配置、Claude 记忆文件，一应俱全。

双服务器架构：香港 IP 是主控，38.244.50[.]120 跑 ARTEX 执行攻击。连 ARTEX 的实例端口都露在外面——它上面开着http[:]//38.244.50[.]120:18899/.claude/CLAUDE.md，目录直接可读。代理 IP 一共 9 个，按原报告格式照录：

* 101.53.80[.]20
* 205.214.59[.]31
* 124.155.252[.]63
* 154.201.79[.]246
* 23.248.249[.]90
* 23.158.220[.]98
* 103.248.148[.]84
* 203.160.133[.]172
* 209.209.85[.]38

销赃计划也没落下——会话里他直接问 Claude：韩国泄露的数据一般去哪卖？怎么找 Telegram 的数据群？全部摊在明面上。

后来，ARTEX 的维护者也发了声明，表示与这起事件无关，并把项目转成了闭源。声明和操作都是真的，但作用有限——工具早扩散出去了，删库删不掉副本，闭源也闭不住能力。

对攻击者这是灾难，对防守方反而是教材：对手的配置残留，往往比任何告警日志都值钱。溯源这边，警方查了金融监督院给的 28 个源 IP，全过 VPN，分布在约 12 个国家，没锁定嫌疑人；CrowdStrike 的画像也就停在中文使用者、经济动机（中等置信度）。IP 被 VPN 抹平了，但行为指纹抹不掉——提示词语言、工具栈、配置残留，这些东西 VPN 带不走。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNotyqLqnjMeIo27mgNxUBeTP6tQYGGNwIZYeibHbQOcpeQHRWfIuicQg8L7ibwm1KUhoIcROI5W0O8CRAIYlIGHLDFHnEKuLU1HBNM/640?wx_fmt=png&from=appmsg)

图3｜IP 在迷雾里，行为指纹在阳光下——配置残留抹不掉

# 04 三个变化与启示

事件的意义不在韩国，在三个变化，每个后面都跟着一条启示。

门槛降了。从前能维持两周、跨机构、机器节奏渗透的，是装备精良的专业团队；现在一份开源工具加几个 API 额度就够。启示很直接：你的对手不再只是已知的团伙，可能只是任何一个能下载的人。

危害大了。这次流出去的年收入、贷款额度，是能直接变现的字段，几万人起步。工具不挑组织，挑暴露面。启示是：一条没人管的边缘系统，也可能造成几万人级别的泄露。

影响放大。处置从一家安全公司的通告，滚成韩国总统内阁过问、金融监督院追查，国际媒体跟进（上了路透社），网络安全概念股一度涨了约三成。启示是：一次失守不再是内部事故，是舆论和股价层面的事。

落到企业，警戒一句话：下一个被扫到的未必是银行，但大概率是某个"边缘系统没收敛"的组织。防御侧五条，按优先级排：

暴露面收敛，优先于对核心的加固。把外部可达的业务边缘当第一类资产盘：对外联系统、经纪人/中介入口、移动办公平台、任何不在主监控里的入口。收敛速度要快过它的扫描速度。

检测与响应按机器节奏重排。重叠 IP、同款工具栈特征流量、异常批量出向，做联动告警；响应自动化衔接，别等人上班。

情报不止 IOC，要收"配置残留"。工具偏好、提示词语音、LLM 调用模式、代理供应商，都是画像和预警材料。

别把安全押在"模型自觉"上。对手已经用多模型冗余规避拒答，守方也一样：要求得在系统层做强制——命令拦截、出向白名单、最小权限。

红队用例里加"AI 打点"。自己人先模拟批量渗透边缘系统，固定进测试用例库常态化回归。模拟不出来的打法，别指望防线扛得住。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNotK7vmR2icAzRVMAhuYUqXKPP8cH84ic9nRBETk7o5iaCciaU7H2Q8k1IFEILMibDMIuhCbO0snW1GNXeLJgySJm10DpMoPLZpFnQ14/640?wx_fmt=png&from=appmsg)

图4｜五条防御对应三个变化：收敛暴露面、检测提速、别赌模型自觉

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

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