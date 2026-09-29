---
title: 朝鲜IT工人团伙开始利用女性进行活动
url: https://mp.weixin.qq.com/s/EAr1kAOSYMb_QqvdZMjy_A
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:38:10.577229
---

# 朝鲜IT工人团伙开始利用女性进行活动

# 朝鲜IT工人团伙开始利用女性进行活动

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一个参与远程 IT 工作者项目的朝鲜组织开始利用女性员工来迷惑可能正在调查其男性工作者的西方公司。这些女性通常作为会议和面试的门面，而男性开发人员则在幕后进行工作。

这是一篇由独立安全研究员于 2026 年 9 月 23 日发布的调查报告，研究人员通过社工手段渗透进一个朝鲜 IT 工人小组的内部 Slack 工作区，完整记录了一名代号为 "Jasmine" 的女性新招募人员在入职前三周内的训练、人设搭建、账号批量生产、以及她首次直面客户 CEO 的面试全过程，并借此揭露了整个小组的运作架构、掩护公司与美国籍 facilitator（协调人 / 中间人）。

黑鸟按照往常一样，仅展示该调查涉及的相关手法，涉及部分情况不过多讨论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpojo60BiaXwBmPLzcvibUTyict6kxCgibb8bFLvbwubLTNC9MibNSt5muPNaxPOujh69uDDwdsmcd4krC8M2RYtO89sgiaT8C8UTcfQ/640?wx_fmt=png&from=appmsg)

2026年9月，一个自称Jasmine Bell的女人走进了一场视频面试。对面客户是美国一家做身份认证的咨询公司，要招一个懂Okta、Azure和VLAN配置的系统管理员。

Jasmine入职这家“美国公司”MageHire才三周。按她简历上的说法，她在新加坡国立大学读完计算机，先后在四家公司做过基础设施和系统工程师，最近才搬到佛罗里达。

可她其实一行代码都没写过。

她在小组里的正式头衔叫caller，翻成大白话就是“接电话的人”。在这个朝鲜秘密IT工人小组里，caller负责出面参加视频会议和面试，靠一口流利的英语口语撑场面。真正在键盘后面敲命令的，是躲在她背后的开发者。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqZWdBwGVibCU4KbicxDHFVIyqpfwNUkFBKrYbtQdmNx1QyiaRqkUT29f0iaueAJ4GzUndMGPJMg2A8EicibchsJuXD7pCZLyK4AaQxY/640?wx_fmt=png)

Jasmine在内部频道自我介绍“一个新来的女dev”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoYGTVKwEWHB7Yy8ENR1o4STia4h8w0n5yvEY8FuEQHtF9nouicFwMpylnCxffyCVFhacYvn3kaG9nBF9s3bCFvNswuHF79y7haw/640?wx_fmt=png)

她很快改口：自己是caller，不是developer

这不是临时起意的兼职。McKenzie通过social engineering混进了对方的两个Slack工作区，把Jasmine从入职第一天起的聊天记录全程跟了下来。他看到的是一条已经跑顺的流水线：批量生产假人设、批量注册邮箱和LinkedIn账号、用ChatGPT写好简历和五分钟开场白、再丢给一个叫MockWise的AI面试平台彩排一遍，最后把一个毫无技术背景的女孩推到镜头前。

这个小组用两个Slack工作区把里子和面子分得很开。一个叫mphteam，2023年6月建，里面全是朝鲜人，不放外国合作方。小组自己的任务目标、发薪deadline、培训资料、身份证号都丢在这里。另一个叫MageHire，2022年7月建，是对外的门面，美国facilitator（牵线人）也在里面。小组成员自己把这个工作区叫“我客户的slack”。

|  |  |  |
| --- | --- | --- |
| line-height:normal"><o:p> </o:p> | mphteam | MageHire |
| 用途 | 内部，只有小组成员 | 对外，和美国牵线人共用 |
| 创建时间 | 2023年6月9日 | 2022年7月16日 |
| 历史消息数 | 27002条 | 190583条 |
| 月活跃用户 | 8到15人 | 6到10人 |

数据截至2026年9月15日。

mphteam的#general频道挂着33个成员，按月活跃算下来实际干活的也就8到15个，剩下是休眠或退役账号。频道列表很说明问题：#english（11人）、#resume（6人）、#used-real-infos（7人），还有一个私有频道team4（4人），暗示这个小组历史上至少跑过四个项目组。

成员头像全是卡通图或者AI生成图，头衔自己瞎起，什么Senior Recruiter、SWE、Odd Eye。同一个人还开重复账号，叫Victor的有三个，叫Rakal的有两个。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoy43WAnPCDynHCQs4jlicFJMx7V7rWSUJGOQsKcvErTB7XTccF2ujsPOkZcMWNFCMx7u1ReUlllpJia81UictG5FABSzqR5nrc2U/640?wx_fmt=png)

工作区成员目录

小组组长MP转发过一份成员名单，说是给MageHire老板看过的版本。上面写得很直白：

某国某地：Joy/Joey、Eddie、Timon、Zack

某国某地：Leo、Kei、Lucas、Shiny、Shine

俄罗斯，已不活跃：Victor、Alex

对外履历里，他们的国籍写某国，其中一个叫Kei的写日本，还有两个写俄罗斯。

新人进来由老队员带。Scarlet自己熬了十个月才等到第一次真人面试，她告诉Jasmine“你已经很走运了”。学英语的素材是六本《老友记》剧本，2025年3月有人发到#english频道里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpGFLGQ28rSgBFqOpLw8OEekjDbnL1VXER1pQofebiczkLq7wKbqlezYUeuRbJuia0h5U1cur4LbdteicoicY6icicVK2alI2LzBHf7g/640?wx_fmt=png)

英语学习材料，《老友记》剧本

# 入职第一课：你什么都不用会

Jasmine的onboarding全在mphteam的team4频道里完成，带她的人是Dark。这个频道只聊朝鲜内部行动，不碰MageHire那边的事。她接手的培训材料包括：

怎么bid（批量投简历）和养LinkedIn要用的邮箱

人设搭建指南，要求一个人设在所有账号里保持一致

ChatGPT聊天记录，既用来写人设小传，也用来写面试台词

ixBrowser的安装和正确用法，这是个带代理的浏览器，账号都养在里面

SlyNumber怎么注册和配置，用来过手机验证

面试前的准备材料和面试后的复盘

怎么开加密货币钱包

Dark没指望她懂技术，聊天记录里写得很明白：照着指南做，不会就问，批量产账号就行。

Jasmine连自己的身份都不能随便挑，必须从MP给的名单里选。她选中“Jasmine Bell”这个名字之后，被要求把现有Gmail的显示名也改掉，因为那个邮箱前缀正好是jb开头，能顺着接上人设。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDolznps9J3uKERWOTtlzftlfwzgCicxibKAJ2GdVX4FebyzUQPFialfOHkcc4ohJrD7IH5IKqfozFwEthqiaxpeQP60jKD7wQKnOVQ/640?wx_fmt=png)

从组长给的名单里挑一个假名

# 人设是怎么批量生产的

Dark给她派的第一个活是做邮箱和LinkedIn资料，给以后投简历用。他承认这活无聊，但讲清了道理：一旦有队员拿到offer，手里得有一堆现成资料背调用，过验证才不慌。直接做美国LinkedIn账号太容易死，所以让她先集中做欧洲身份，养十五到二十天就能看到回报。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDr3t9J8sqRtF9wRoSR4Yt7k7sze8APuCBy9Bq1hOZw29UqZYHKyeLCsY0AzRzRgPRRjfxOyjQV2Wzeh8M2IGkrVuk5ibiarXP13c/640?wx_fmt=png)

第一份任务：做邮箱和LinkedIn

# 建号规则本身就是写给AI看的prompt

挑一个大城市，找一个真实住宅地址，拿来当人设住址

围绕这个都市圈做四段履历：大公司实习生、创业公司远程软件工程师、中型公司onsite高级工程师、小公司远程高级顾问

不准用美国公司

头衔统一写“Senior Full Stack AI Engineer”

加一所开了IT专业的大学

简历上写的每一项技术，必须在那个职位的时间点之前就已经存在

每条规则都对应一次以前踩过的坑。四段履历拼出一条可信的职业上升线，同一个都市圈保证地址不打架，真实住宅地址显得像真的。最扎眼的是“不准用美国公司”这一条，它直接制造了一段北美雇主在本国根本没法核实的工作经历。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrNkO0Rljds4Lb985ic09ujwL2DvfhTGUHjzXq8yqqqziboe9Q4nsPkCnzLAdxqyEH6KoDHZJpLwzUncoyCzsT1TQvuoYt6BKWfc/640?wx_fmt=png)

Dark贴出的建号规则

# 一个邮箱只养一个LinkedIn

人设的主邮箱特别金贵，因为2FA（两步验证）靠它，所有账号的找回也靠它。这种邮箱不会出现在求职申请里，一个邮箱只对应一个LinkedIn，LinkedIn一被封，这个邮箱也跟着报废。

Jasmine在一个Gmail后面挂了二十多个Outlook，直到微软开始强制要手机号为止。SlyNumber就是用来买和养手机号的服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqJ62MfqDXh2dIGeQd9zb2UJ8G4d2qCDegwicjtlYa67ILI70lAoeUNfQUsJw2v7JeQqtF9nmHXaibGD9v6LvNDD5RCZoJ5xz6NI/640?wx_fmt=png)

一个Gmail后面挂了一串Outlook

所有账号都养在ixBrowser里。这是一个anti-detect browser（反指纹浏览器），每个人设关在独立的浏览器profile里，后面还挂着各自按量计费的代理，这样一个平台封号不会连累其他账号。Dark叮嘱她每天看一眼流量余额，套餐一空，所有profile一起陪葬。同一条消息里他还说，SMS验证服务要充值的话走她邮箱。

这些服务主要用加密货币付款，但也有队员直接用偷来的信用卡和银行信息。工作区里贴过一整套卡信息，账单地址在路易斯安那州。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrTZpldeVptXQoqaw3vdAwZFBxXOSzlv4HWOCPRF1ALPLicyeOg6HibnYwuaeqafEvapfcMPicd5ianlm0OZiaEf1RWhmOib09Ck0KTw/640?wx_fmt=png)

Dark让她每天检查代理流量

两周下来，Jasmine做出来的东西摊在一张共享表格里：

|  |  |  |  |
| --- | --- | --- | --- |
|  | 备好人设数 | Outlook账号 | LinkedIn账号 |
| 芬兰 | 642 | 5 | 3 |
| 波兰 | 103 | 13 | 11 |
| 荷兰 | 100 | 10 | 0 |
| 英国 | 99 | 10 | 1 |
| 澳大利亚 | 88 | 1 | 0 |
| 爱沙尼亚 | 83 | 14 | 0 |
| 美国 | 61 | 2 | 0 |
| 日本 | 50 | 2 | 0 |
| 八个国家合计 | 1226 | 57 | 15 |
| US\_REAL | 3个真实身份 | 无 | 无 |

修改时间集中在9月7日，也就是她第一批profile被验收、然后发现全死的那天。

表格里有三个规律特别扎眼。

所有生日都卡在1995到1998年，算下来28到31岁，正好落在他们身份生命周期文档里写的28到35岁区间。八页国家里没有一个男性身份，每一行都是女人。日本那一页更讲究，给每个名字标了罗马音读音，配一个美式化的姓，比如佐藤结衣变成“Yui, Taylor”，还加了一列“Feeling”，写这个人给人的感觉应该是“优雅、聪慧”“专业、可靠”“经典日式感觉”。

US\_REAL那一页

第九页叫US\_REAL，里面存着三个真实美国女人的全套资料：出生日期、身份证号、家庭住址、电话、个人邮箱、雇主、职位、银行名、账号和routing number（银行路由号），还有信用分。两个住在佛罗里达，其中一个在杰克逊维尔，名字叫Jasmine，个人邮箱里带个“bell”。

这就是Jasmine Bell这个名字的来历。

9月7日Jasmine交了四个做完的LinkedIn等验收，Dark回来说全被封了。他处理这事的语气跟处理日常差不多：平台封号比他们建号快，唯一的解法就是接着建。这种没完没了重建账号的劲头，小组内部有个专门的词叫“injogogi spirit”。Injogogi（豆皮）是朝鲜饥荒年代用豆渣压出来的菜。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqkt25FeCN5m6iaP1yhQPZHF1FV1aJLXP9IuhEjUBmFzC0fiaRpZc0UVeCmMHhFcR4Rgmv27GSSEcrjMINx9RG3ypvS7s6HHO95Y/640?wx_fmt=png)

小组内部把这种死磕叫“injogogi spirit”

# 怎么找一个“sil-In”

同一段对话里Jasmine问，怎么才能弄到一个“sil-In”，大致意思是一个真正的外国牵线人。Dark的回答是，找一个她感兴趣的男人，主动搭话，然后“把他迷得神魂颠倒”。McKenzie之前的报道里把这种心甘情愿帮忙的美国人叫“real guy”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDr6MlwiaKzf8lKXPyuL6UAwktn7yVBbe2ugJryPjUryRcFGObggKibiaWvVxicGHoaDzFiashxfWuHicYeVROJlbibg7z9CglmUaOkvvI/640?wx_fmt=png)

Dark教她怎么“发展”一个真外国人

# MageHire：那间美国“猎头公司”

MageHire工作区2022年7月建，累计19万条消息，月活6到10人。这里存着职位profile、面试排期和人员安置，也是小组成员和美国牵线人唯一的交集点。

它对外的样子和普通staffing agency（人力资源公司）没区别：一个团队负责人、几个高级和staff软件工程师，还有一个头衔写着“CEO-SALES-MARKETING”的CEO。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpiaQr9cp6QmhZEtoMMg8ByFqAjx1GGwqf2FN3Bn1XSZdZWiaerN1KyL3S5WCDXo8ypLI7sibHehwpRoPArWwwTibLKn9sNpEB9Rjk/640?wx_fmt=png)

MageHire工作区成员目录

CEO叫Schmid Payen，住在纽约的美国公民。他在几十个网站上都有职业痕迹，每个网站上的工作经历版本还不一样。工作区里不止一个Payen，还有个叫Rodrigue的，频道里叫@Rio。

2025年7月Payen当了爸爸，他在MageHire工作区里把这事告诉了所有队员，还发了条语音让大家都请假庆祝。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqMJ20ib6r0upwMWOEicaWSJAUjjqS1VZGkiajnD753O4EjyuQV4kLKAXQVlalicD37kibCgDib38mWK4m0lnU0nr67tia9xVvoibRAm38/640?wx_fmt=png)

Payen在Slack上的个人资料

# 每天早上的standup

每天早上开场是check-in。队员把自己当天要陪的客户会议发出来，其他人就知道谁在哪场会上，CEO据此安排。CEO在频道里抱怨说，早上八九点之前收不到这些日程，他就没法接新客户，他想把客户电话全排在周一到周五，其他事包括沟通都甩给团队。团队负责人同意，提议每天8:40站会。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpTBzcib6iaoSnsVs6zW98sHpXK68QqOwBsLPEvOibWnicgm2MT9xJZwpMaRGRlULnq5ia7pasoKx7gicn5WvO5S72ucULqy49Ytb1QY/640?wx_fmt=png)

早上的check-in日程

check-in还能看出他们怎么互相补位。有个队员把第二天三个客户的会议全列出来，标注自己上午可能不在，然后把每场会分别交给指定的同事，其中一个还说“如果我开会迟到，我会在xxx频道里发消息”。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrxx0MzUfzmr51gK4mGvIK2kH5NN7peD00iaWaSJAVXhNcKpzOJ2BZWm55sE6xk77lQJj4DKG1BhbcNChSB8DIMFgGwPnV2PZLo/640?wx_fmt=png)

把会议分头交给同事代打

这些日程并排看才能感觉出这条线跑得有多深。早上帖子里出现的客户名是好几个并行项目，一个人没空，会议就在几个人之间倒手。

# 按客户记工时

队员按月做表，记录每个客户的计费工时。下面是一个开发者某几个月的情况：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 月份 | 客户A | 客户B | 客户C | 客户D | 合计 |
| 2026年6月 | 5.5 | 4 | 0.5 | 无 | 10 |
|...