---
title: 一篇迟来的反思与分享
url: https://mp.weixin.qq.com/s/ehj10haHzDWxTV81fOi1Yg
source: Doonsec's feed
date: 2026-11-08
fetch_date: 2026-11-09T08:52:16.612812
---

# 一篇迟来的反思与分享

# 一篇迟来的反思与分享

满天星星的AI+红队梦

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

编者荐语：

很牛逼的师傅和工具，体验感不错，方便快捷成果满满我的推荐码：
6FC2M5WU

以下文章来源于青椒洗衣液
，作者青椒洗衣液

![](https://wx.qlogo.cn/mmhead/qd3u5IHSYTic9MVlf1xLV6Uxy47ib9UUfG9IP0YfdNYnClPiaHSib1gCPBHQuibhHuVgchfsgB5epvyw/0)

**青椒洗衣液**
.

越努力越幸运。

# 一篇迟来的反思与分享

大家好，我是青椒洗衣液，一名从事网络安全工作的普通大四学生，今天写下这篇文章，主要有几个目的，一是跟大家分享一下这几年来自己走过的路和感悟、二是向大家宣发一下我们这一群人最近正在做的工作、三是寻求一些机会和合作、四是希望能够给到一些同学们部分有效的启发。

# 一：自我介绍

诚如前文所说，本人是一名于贵州警察学院就读的大四学生，专业为信息安全，由大二开始，深入从事网络安全这一项工作，截止目前，已有两年出头的时间，奈何天资愚钝，只能靠着不断前行的韧性和努力，方才取得了一些微不足道的成绩，以下为本人的个人简介，每一项成绩，都有相关证书、报道、奖项所证实，欢迎各位同行随时考证,为不过渡占据篇幅，仅展示部分成果。

1. waic（世界人工智能大会）特邀演讲嘉宾。
2. 腾讯llmwaf挑战赛个人全球第一。
3. 阿里ai大模型攻防赛个人全球第四。
4. 腾讯清竞指令遵循挑战赛队长全国第十一。
5. 阿里ai产品赛个人全球第十八。
6. 公安个人三等功获得者。
7. 贵州省教育厅感谢信获得者。
8. 职业规划大赛高教组（ai安全攻防工程师）个人全国奖项获得者，获贵州日报相关报道。
9. 中关村智联联盟受聘Ai安全专家。
10. 某安全厂商Ai安全项目实施人，同时从事渗透测试/护网监测/竞赛支撑/安全培训等工作。
11. 数十次金融/影视/交通/公安行业Ai安全培训讲师。
12. 在各大厂商/官方平台/众测项目/日常工作中提交并审核通过数百个相关漏洞。
13. 作为核心队员+队长多次参与国护红队、省级攻防项目并获相关感谢信。
14. ……

![](https://mmbiz.qpic.cn/mmbiz_png/DbE8HYbjXuO4SP6u3hOqicibic4g0qV7qkGVyy1yfKcm94KBZa8yFzVDKUD97RXaaicL34jIbibL725oWbwN4CSc2ibaHw4FSfhy80iaTWNfO7MgUI/640?wx_fmt=png&from=appmsg)

两年以来，获得过一些成绩，也见到过形形色色的前辈或者同行的朋友，在这些还算饱满的经历当中，收获到最大的成长是这样一句话：“人，永远要记得谦卑，永远要记得自己的来时路和最开始的目标。”

大一的那一年因为坚持，坚持打比赛，坚持刷ctf赛题，坚持去各种平台上自学，所以有幸被网络安全社团的师兄们赏识，哪怕师兄们的能力并没有惊天彻地，可终归是给到了我一些方向、一些动力，哪怕那一年压根没进过一次线下的省级竞赛，唯一的一次获奖，也仅仅是社团内部考核的二等奖还是三等奖（连奖状都没有的那种获奖）。

因为没有能够快速到手的成绩，而很多时候网络安全相关类型的竞赛又在周末，所以常常出现找到同班同学组好队，真正到了比赛的时候，他们会因为各种朋友的邀约、想要放松一下、反正什么也不会的合理理由缺席竞赛，最后往往是我一个人面对着压根不会的题目坐牢一整天，然后继续循环往复，一个人继续锲而不舍的、孤独的坐着自己的冷板凳。

因为没有体系化专精化的训练，哪怕做了很多，也慢慢从0解到能够解出一大部分题目，但是依旧没有拿到什么大的结果，所以我一直说我是属于比较愚钝的那一类人，是有所依据的。

我想，我唯一可以依仗的、比别人更加突出的点在于，别人一个星期只愿意花几个小时或者半个小时来钻研，而我可以每个星期的每天都花几个小时在这项事业上面，哪怕一直是吊车尾，哪怕没有成绩……

让我没有放弃的理由，是我对这项事业感兴趣。

而另外的一个理由，或许是不想辜负社团师兄的期待，当时记得因为前期选拔面试，社团的一位唐师兄选择了将近十人的种子亲自带，而在那十人中，有之前就接触过的童子功，有几个互相就在一个班级能够交流学习，有脑袋灵光学什么东西都很快的……，而我恰恰是那一类最不起眼的，学得慢、忘得快。

唐师兄为了勉励我的愚钝，也生怕我会中途放弃，于是跟我说了这样一句话：“齐江，我希望你能走到他们的前面。”

然后我记住了，一直到现在。

不积跬步无以至千里，不积小流无以成江河，我想对一些还未入行的新人同学们说，如果你确认热爱这个行业，那么请不要放弃，寒冬终会过去，而见到春天的人，一定属于长期坚持下来的那一群“笨蛋”。

转机在大二的寒冬，由于在学校有过一些前期“网络安全社团”的坚持经验，哪怕没有拿到什么成绩，可还是被一位对我影响最为重大的刘师兄审核简历通过，去到了相关单位实习，说是实习，其实更像是刘师兄对于我们那一期四个学员的言传身教，我们每周学习六天，一天平均学习12小时+，而因为大二时期没有多余的金额用以支付房租的费用，我们就近免费住到了单位里面。

我记得分配给我的是一间大概30平米的阁楼，地板是木制的，房间因为堆积各种电器的包装纸箱占据了三分之一的位置，因为进入阁楼的空间狭小，并不方便放置新的床位，所以我只是买了厚厚的两床床垫，然后把那整整三十平的木地板当成了我的床板，就这样坚持了两个月的寒假实习，练就了扎实的渗透测试/环境搭建/传统漏洞/的知识，也总算是了解到了正统的网络安全方向，挖掘到了人生中的第一个漏洞。

地基打好之后，需要的就只是时间这位工匠不懈的堆砌，水滴石穿，纵使是顽石也逃不掉这样的宿命，那个冬天很寒冷也很温暖，天寒地冻，可刘师兄却自费为我们每人购置了一个小火炉并且全额承担水电费，这份温情我一直记得现在，从来不敢忘怀。

同样，在那一批被选中的四个学员里面，我的能力依旧不算突出，唯一的特点，在于经常因为学不懂、学不会，所以常常琢磨到凌晨三四点，直到后来重新回到校园，因为深刻知道自己的平凡和普通，所以开始在网络上给别人承接一些5/10块钱诸如帮忙搭建靶场，帮忙解决虚拟机问题，帮忙练习打靶场，帮忙解决实验实操等等基础问题的工作，并且开始长期在csdn、先知社区等平台撰写技术博客总结不足。

一直这样持续了几个月，从一开始一个问题需要几个小时甚至一天才能解决，转换到后面十几分钟就能流畅完成，现在我个人出去做技术培训的价格在2000-5000一天，低于这个价格我基本不会考虑，可在2025年，雇佣我一天的费用只需要5元钱，如果我没有成功解决那个问题，连这5元钱我也不会收取。

这当然是很苦逼的一段经历，为了接单，我常常会把电脑带到教室，在完成基础的教学任务后，开始苦哈哈的做着可怜的力工，常常因为转换教室，网络不畅，遇到过很多问题，可这些问题，终归都是可以解决的问题，可以解决的问题，就不算问题。

我的要价，也在一次次解决问题中，从几块，到几十块，几百块，以及到如今的几千块，每一个阶段我都在解决不同的问题，吸取不同的营养，只有我完全确保有拿下这件事情的能力，我才会去进行收费，所以做到如今，大大小小的单子做过几百上千，但没有一个差评。

到了大二下学期，我终于开始能够为我的学校，我的社团，我的师弟师妹们做一些事情，这一年我变成了大家推选的当之无愧的网络安全战队的学生总教官，也是在这个阶段，我拿下了诸如阿里ai大模型攻防赛全球第四/腾讯清竞指令遵循挑战赛全国第十一/阿里ai产品赛全球第十八/贵州省教育厅感谢信等等在如今看来还算尚可的成绩。

但此时的我，依旧满心惶恐，因为我其实是一个比较苛刻的人，我会反复的问自己，这些成绩对于自己而言是突发而不可持续的，还是只要自己想，就总归能够拿下的？在我看来，只有想拿就拿并且持续的拿，才是能力的体现。

于是，我又默默蛰伏了半年，成绩越来越多，从校级走向省级，从省级走向国家级，从优秀走到单人第一，我的国家级证书和获奖，慢慢多到一个书包都放不下，至于省级的已经不在计数范围之内，慢慢的有了一些省级媒体的报道，成为了学校的宣传对象，拿到了公安的个人三等功，承蒙前辈们赏识做了一些议题和分享，直到这个阶段，我那颗惴惴不安的心脏才算是落了地，因为无数次的实战证明，这些成绩，只要我想，我就能拿，这是我的底气，也是我的能力。

走到这里，我想对大家说，一定不要过于自满，因为人外有人天外有天，一些小小的成绩，并不足以自傲，相比起一些老前辈们长期做出的贡献和事业来说，我们这点成绩，不过是微不足道而已，故而了解我的朋友也知道，我的朋友圈更新频率其实不高，多做事，少宣扬，多反思，少张狂，这是能够一直进步，也一直有朋友愿意持续相处的根本原因。

到了大三，因为前期的一些成绩，进入到了某个国内还算知名的安全厂商进行实习，至今已有七个月的时间，在这半年里，我见识到了更多工程化的项目，撰写了数百份漏洞报告，从事渗透测试初测/复测；攻防竞赛；Ai安全培训/测试/竞赛等等项目，我在数个省市辗转，数十家单位里面从事相关的安全工作，这极大的夯实了我的工作落地能力以及团队协作能力，也正是这半年的时间，让我慢慢转变为一个成熟的安全工作者，不仅懂得技术，更懂得了项目的各个阶段，工作中的各个细节该如何把控，以及针对于不同级别的单位，不同需求的安全工作，应该具体怎么落地落实。

这半年以来，令我感触最深的是，当你带给客户足够高质量的工作，他们是真的会发自内心的认可你，犹记得一次Ai安全培训的项目，事后客户自发电话给了我们部门的相关领导，夸了我足足一个小时；也记得一次省级竞赛的培训，让一位客户学习到了比较先进的技术拿到了不错的名次，对方事后专程向我报喜……

慢慢的，自己开始有独立支撑一些项目，包括一些省级竞赛，一些难啃的渗透项目，一些各大单位的培训项目，这才算把能力真正全方位落足到了实战，成为了一个能够被大家信任的安全工作人员。

到这里，想跟大家分享的点在于，安全工作是一个很广泛的方向，不仅技术广泛，出路也同样广泛，不止有竞赛/SRC/培训/应急/销售/产品/卷实习等等出路，如果你的精力足够，或许可以都来尝试一番，当然，最好分清什么是主线，什么是支线，每个人有每个人要走的路，不必去复刻他人，只要坚定自己的内心，踏踏实实的做事，熬也总是能熬出头的。

# 二：我们最近在做的事-观星

一直到2026年8月份，总算是走到了大四的这样一个阶段，我和身边的朋友，终于将很早以前的一个想法落到了实处，简单来说，我们想让更多人拥有发现安全风险的能力，不管是初学者还是甲方的安全人员，因为一个人能做的事，跟一群人、一个行业的人比起来还是太过渺小，我们希望增加企业的安全自检能力，希望增加更多白帽子的安全风险发现能力，从而推动安全行业走向更加完善也更加稳固的阶段，发现风险-解决风险一直是我们在做的事，未来，我们希望更多人能够跟我们一起做这样的事。

于是，在老前辈也是好大哥-无法的带领下，我们自主研发了一款名为“观星”的自动化风险评估的产品，这款产品2026年10月投入内测，截止目前，已经成功挖掘到数千个漏洞，结合研发人员此前不录入内测阶段的数据，这个数量要超过三千，当然，在SRC上也累计挖掘到了数十万的赏金，在各大众测项目上，同样拿到了霸榜表现，在真实的省级攻防中，更是可以做到单人+观星拿下1.5万分的亮眼成果……

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DbE8HYbjXuPjeSc3NgPV86wZGBCo0yb56bMuTZvkQGG7XWXBl0vVPLBpSNP3bVRgFPQg35Womw57mnurO0j3wDaZYas6TqswObQYicqpDVx8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DbE8HYbjXuMXbBib4lzibzsuGEBmqd4o0EADrO5PKKbohfaS0gFO9etNWTSVhzTCHbQenTpPFb6Vlj4GZCfaiaXDeH04frw9L3Ue5u6osldM3k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DbE8HYbjXuPs2xwvX0rJAVR6Nhd9I73Ew2q2MHGC3W2bicnzF4By1iaBfK9jOyxKDCIptyzq1rtVSMfGtezrYmHLoxT6onLwBhSXkSdnq16ibw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DbE8HYbjXuMxzKcD01iba513LZF8KWlxsa6mhfpeRAzgHVbmDIfKrakqEJYlnqVFciaVrm2bqQOPzmodXGuxtnCmhzJDRmiaz12tyMDRey3St8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DbE8HYbjXuPFEwknefWBtMV5CIR5Pz109iafTaA30bsVxZPYL4X39DhlUsqX7PJZic8mliaFEktcnHJCsO2jvwuz332ZtZIFvUQlNKqlq8MuMQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DbE8HYbjXuNKiaOXu7CSPicibu95ibXLNnIiaV030ugYEictbSug4PTPD8yCLtojlViaZic5cibliaBksQESfDU689a88ItkYmrFTIgGhJicq0s1A8ibJCI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DbE8HYbjXuMlsRdjZIwMf0FUtIcGun6PQYod4Bicap4YMW1HNUj9qm9OSq1PZbSFlmoOSJk9TwY1bNzCd4kVo2L99fNvvwBW2LaY8icY0OhQg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DbE8HYbjXuMP0iabeU3GCtcMl03Se1jkCa8THOz6AdfSj00gaxOibAyY7553C1tuOpBibHmFhPaea0Y3o0shIqjpFFWjphMCsfGYcPJibqTYXKU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DbE8HYbjXuPlib4ziczn0sa5ehSiaaQItHhB2ozc77dVzP17yz8uODHtuhnSx8qQOK8qLutOvKAyXVENGhyDDVNic7zTUTa9n7oiczwnFMcicBCCc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DbE8HYbjXuMM5W1fRxSuWLVeVdvA41wvLiaTKs4OPJfrJGPA1EjrflFNnQCD9r2ibsWpZJMmbibPFbraJVHPyiazl9yUt95D8O4w3PaOSPF3H04/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DbE8HYbjXuN9pCmjNOe6dibbycK5VRZlhdsyicqHwaKAv2D0m3gZWOALPJFff5NFdrcZLurR74UcKYe8ibD5b2se0L2pTC68IJq4LbcvkhRCU8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DbE8HYbjXuMJgiaUpw6PaQUfkbTOXB5uxL4xx6IxdptXEkIicyqDIRHP8o9vme9LshCBaort3K8wIoNR3jamYc877za5L13AxLFGYfP7dgaNs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DbE8HYbjXuMTicMqj090Vx29HhgHc3TicGn7TficKns6llZFVialK4QnBkhiaIS8ibHu6xI2lWo3HoM9lsrC4YUIMIicLUv8eY2h4MczPWvn3NwNok/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DbE8HYbjXuNbq2l0W70J80Znw8NTxVgbCZEYULRASjBKTVGnhe4QwXJWrdlZpOsibDHLkNOpsIC0jphK8xVegCLIH7ylv6NKQP8UcYW429wo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DbE8HYbjXuN4YK41TKzYbbHh7XOx8JEqtDer8vqxb1ChppGx4icNwv9sXPfROtt00kdAAnGrbhdCspumibS3mBfSOCOyV143MWPszb3tibGLKc/640?wx_fmt=png&from=appmsg)

部分证明如上，不再一一展现……

当然，在如今的时代下拿到这样的成果不足以让大家感到震惊，可如果，我们把这种发现风险的能力转化成了小白都能上手的工具呢？

可以看到，我们做好了官网网页，并且将产品打包成了适配于windows的exe版本和mac的适用版本，这也就意味着，发现漏洞风险的能力，已经被打包到了一个普通的工具当中，理论上来说，你只要能够使用电脑上的wps，那么你就有能力，使用这款无脑的产品，发现风险，解决风险，从而提高网络安全性或者获得漏洞赏金及漏洞证书。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DbE8HYbjXuOKVNTRoCE2jHq2yiakfjgx5lbOJ60sGvYPVLESzYdvKLmXrQZ7GJHNiaE88GkvxDIMibUvybKp8ZoGKWVQsPdMhghmUvfnYs7Yq0/640?wx_fmt=png&from=appmsg)

以下是产品打开的详情页面，大家可以发现，异常简洁，这也就意味着不会有任何的使用难度，你只需要将模型key配置成功，然后导入合规授权的测试目标，即可发现安全风险，解决风险，目前，观星新版本支持web全板块测试以及小程序和app反编译包静态...