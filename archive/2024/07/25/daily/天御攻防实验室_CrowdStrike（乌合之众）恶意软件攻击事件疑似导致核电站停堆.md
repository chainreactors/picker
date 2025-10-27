---
title: CrowdStrike（乌合之众）恶意软件攻击事件疑似导致核电站停堆
url: https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485941&idx=1&sn=61daa29038aaa69e2fcf17786b5fb18a&chksm=fb04ca9dcc73438b31e7216d5c7d57e53ce2955c53ddd4af14a8e56e950a8deb98be2922b517&scene=58&subscene=0#rd
source: 天御攻防实验室
date: 2024-07-25
fetch_date: 2025-10-06T17:43:43.703689
---

# CrowdStrike（乌合之众）恶意软件攻击事件疑似导致核电站停堆

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBDhnoKAEcUESV3zlGzzjWxiaC3nerpH9icg31JVTynR0EtJIOrwyhCHdkPXAj1yruhcFwvVnIteEfUw/0?wx_fmt=jpeg)

# CrowdStrike（乌合之众）恶意软件攻击事件疑似导致核电站停堆

天御

天御攻防实验室

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBB5BmsfdicqGCtt49YBib04HhpU7T1lptTIJLHJDeIQoE94MH7rJlP0BVMAIE55IW0DqCNHFC9VhMYA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**TLDR：**

*2024年7月19日，罗马尼亚切尔纳沃德核电站1号机组因厂区常规部分故障而自动与国家电网断开。有人推测这可能与同期发生的Crowdstrike（乌合之众）恶意软件攻击有关。*

*切尔纳沃德核电站采用加拿大CANDU 6反应堆设计，共有两台机组。两台机组虽有一定差异，但都采用了冗余和多样性设计以防范共因失效。此次事故似乎只影响了1号机组。*

*据报道，反应堆是在下午5点35分自动停堆的，这表明:*

*1. 这不是人工停堆，而是由于常规部分的故障触发了反应堆保护系统，导致受控停堆。*

*2. 停堆时间相对于"乌合之众"事件的高峰期似乎有些滞后。*

*基于现有信息，作者认为此次核电站事故可能与"乌合之众"攻击无关，但还需要更多细节来完全排除这种可能性。总的来说，在没有更多技术细节的情况下，很难下定论。但考虑到核电站对网络攻击的防范设计，二者应属巧合的可能性更大。*

全文：

恶意软件研究界的传奇人物康斯丁·拉伊乌在他的X账号上发布了这条消息，所以它立刻引起了我的注意。

关于此次事件的技术细节很少。基本上，所有文章都在提供基于罗马尼亚国有核能公司Nuclearelectrica发布的新闻稿的相同信息。有趣的是，显然核电站常规部分的故障自动导致了反应堆停堆:

"7月19日晚，由于核电站常规部分出现故障，切尔纳沃德核电站1号机组自动与国家电网断开。"

那么，什么是常规部分呢?基本上，除了"核岛"(即核蒸汽供应系统，包括反应堆堆芯、稳压器、蒸汽发生器等)之外，核电站与其他发电厂相似。一旦蒸汽流向汽轮机，我们就可以说是任何其他发电厂了。所以，如果我们要定义"核部分"和"常规部分"之间的界限，可以说是位于蒸汽发生器回路中的主蒸汽隔离阀(MSIV)。

我画了下面这个简图来可视化这个概念。

切尔纳沃德核电站基于CANDU 6设计，是欧洲唯一采用此设计的核电站。事发时，1号和2号机组都在满功率运行，但2号机组并未受到影响。这说明了什么吗?我认为这不能说明问题。

1号机组比2号机组老，尽管它们采用相同的参考设计(1997年)，但2号机组吸收了CANDU技术在1号机组建成后的所有改进。因此，两个机组在设计、安全性和可靠性方面存在一定差异。

我们还需要记住，核电站的设计是为了防范"乌合之众"式的事件，即最坏情况下的"共因失效"(Common Mode Failure)，这会使电站的不同部分因单点故障而无法使用。因此，核电站采用了冗余和多样性作为纵深防御策略的一部分。我们也可以在其他安全关键系统(如航空电子设备)中看到类似的方法。

报道提到，1号机组在17:35(GMT+3)时"自动"断开并停堆。这有几个原因值得关注:

1. 这说明这不是人工停堆。这看起来显而易见，但实际上相当重要。这意味着不知何故，核电站的"常规部分"出现故障，成功地向反应堆发出了跳闸信号，并由反应堆保护系统(RPS)妥善处理，导致受控停堆。导致这种情况的原因可能有很多，在没有进一步信息的情况下，我无法真正缩小瞬变事件的范围，但它肯定是严重的(例如，由于汽轮机问题可能导致的负荷脱扣情况)。因此，我们应该假设停堆不是操作员根据当时的情况(例如，计算机崩溃)做出的决定。例如，2007年在美国的布朗费里(Browns Ferry)核电站就发生了这种情况，当时一个有故障的设备产生了大量以太网流量，最终导致操作员决定启动人工可控停堆。

2. 根据"乌合之众"攻击事件的发展过程，反应堆跳闸的时间似乎比其他干扰晚了一点。

基于目前掌握的信息，我认为"乌合之众"恶意软件攻击可能不是此次核事故的背后原因，但我们需要等待进一步的细节才能完全排除它作为根本原因的可能性。

备注:

- Crowdstrike:"乌合之众"，一家网络安全技术公司，此处指代该公司同名的一起恶意软件攻击事件。

- Cernavodă:切尔纳沃德，罗马尼亚东南部城市，著名的切尔纳沃德核电站坐落于此。

- Nuclearelectrica:罗马尼亚国有核能公司。

- CANDU:加拿大重水铀(CANada Deuterium Uranium)反应堆，加拿大开发的一种核反应堆。

- Browns Ferry:布朗费里核电站，位于美国阿拉巴马州。

相关报道：

微软(Microsoft)声称，上周五与Crowdstrike（乌合之众）相关的大规模故障只影响了"不到1%"的Windows机器，**这种说法试图淡化一个仍在全球经济中引起反响的事件**，是一种透明的企业文过饰非。恢复工作比写一篇博客文章要困难得多。

在"乌合之众"Falcon平台的一次软件更新出错时，受到影响的850万个系统并非随机分布的Windows机器。这些机器被规模较大、资金较充足的组织用于需要"乌合之众"所承诺的那种保护的敏感功能，正如医疗、银行和金融、交通运输和公共安全等关键领域所遭受的破坏所证明的那样。

"这850万台设备所在的大型组织，其威胁和风险状况意味着它们有能力投资'乌合之众'的解决方案，"位于都柏林的网络安全咨询公司BH Consulting负责人布赖恩·霍南(Brian Honan)说。

英国网络安全专家凯文·博蒙特(Kevin Beaumont)在周一发布于社交平台Mastodon的帖子中表示，在有问题的更新发布三天后，清理工作仍在"进行中"。

受影响的系统陷入了无休止的崩溃循环:蓝屏死机、重启、加载有问题的"乌合之众"文件，然后再次崩溃。由于"乌合之众"直接访问操作系统内核，微软没有内置防御措施。修复受影响的系统需要删除该文件。微软已经发布了一个可以提供帮助的工具，或者受影响的用户可以进行擦除和恢复(参见:\*"乌合之众"和微软的故障暴露了重大的恢复能力问题\*)。

"我知道有不少组织还不到修复工作的三分之一，"博蒙特说。

在航空公司中，达美航空(Delta)继续受到特别严重的打击，导致公司层面和客户层面的业务中断。据航班跟踪网站FlightAware称，在周一上午美国时间10点左右，达美航空已经取消了当天19%即700个航班，这使得自周五以来取消的航班超过5000个。据路透社报道，大量航班取消和广泛延误使许多旅客滞留，达美航空尚未给出恢复正常运营的时间表。

微软周日发布了一个与"乌合之众"联合开发的工具，使管理员能够从受影响的系统中删除有问题的更新，尽管有一些注意事项。

任何使用微软BitLocker或类似产品进行全盘加密的系统(这在某些行业是监管要求)都必须先由管理员输入恢复密钥进行解锁。

一些组织集中存储BitLocker密钥，但许多组织只对关键服务器而非每一台台式机或笔记本电脑这样做。因此，他们可能需要让最终用户参与恢复过程。

另一个注意事项是:微软的工具需要从可启动的U盘运行，因此使用该工具需要物理接触系统。"你的生活将是从一个地点驱车到另一个地点，应用修复程序，然后继续前进。别想睡在自己的床上，或者吃一顿不是从快餐店买来的饭，"IT人士埃德·齐特隆(Ed Zitron)在一篇赞美系统管理员的文章中写道。

霍南说，需要亲自处理无法工作的设备将延长恢复时间，特别是"对于有许多远程工作或混合工作方式员工的组织而言，""这些员工需要到当地或中心办公室修复设备，或者IT人员需要到员工和设备所在的地方。"

参考资料：

https://www.linkedin.com/pulse/did-crowdstrike-fiasco-cause-romanias-npp-cernavod%C4%83-1-santamarta-witff

https://www.databreachtoday.com/blogs/crowdstrike-disruption-restoration-taking-time-p-3673

**推荐阅读**

**闲谈**

1. [中国网络安全行业出了什么问题？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485457&idx=1&sn=d45cc35242cdc83e98b124531ea7c093&chksm=fb04cb79cc73426f21801f35912b626bf515dc2b9d85b3da578f8087d0a2960396ef1e6347bc&scene=21#wechat_redirect)
2. [国内威胁情报行业的五大“悲哀”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484999&idx=1&sn=485863f4e66a62f55aa69334c787e6f3&chksm=fb04c52fcc734c3919fc28c61a9b13488b89efe4c1ba5cb16f8f00f0c6e996c7f1df47984463&scene=21#wechat_redirect)
3. [安全产品的终局](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484846&idx=1&sn=35bab89f917f5043919e40893268d576&chksm=fb04c6c6cc734fd05c0423dc971a0578eb8b951ef1764be0a99e2bdd1c26b736d64cf61b6d77&scene=21#wechat_redirect)

**威胁情报**

1.[威胁情报 - 最危险的网络安全工作](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485331&idx=1&sn=0857185a1bc7ed04c2d1edc60cb93a34&chksm=fb04c4fbcc734dede0fd243984c30250ff7859f68a265b1a278ac72a5761ac0ccaf0038537ec&scene=21#wechat_redirect)
2.[威胁情报专栏 | 威胁情报这十年（前传）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484880&idx=1&sn=c2b5730f2a7011959096526ff775c8ac&chksm=fb04c6b8cc734fae9f6d2e0693cecd5fd594a01694d8e38bd95926cb88a0f627c3d5b2f36ea2&scene=21#wechat_redirect)
3.[网络威胁情报的未来](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485003&idx=1&sn=76253d23e51dde8dbf4d675b79ab43cf&chksm=fb04c523cc734c352490ca37f55f1c3a989d55807298cb308aa3c126e24816d6fda11a8766f1&scene=21#wechat_redirect)
4.[情报内生？| 利用威胁情报平台落地网空杀伤链的七种方法](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485042&idx=1&sn=afd1212b585f30bccdece8471fadd31d&chksm=fb04c51acc734c0c9fd0d1d388b7672defbe5ce17a10af58d3a5d336ba21fa21398b4ad860e2&scene=21#wechat_redirect)
5.[威胁情报专栏 | 特别策划 - 网空杀伤链](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484709&idx=1&sn=649a27516ca01baab49ce750e3502cc3&chksm=fb04c64dcc734f5becd252686228f6c3c2bd00bff52041e9dae6fde2008e1a43057989b9d16f&scene=21#wechat_redirect)
 **APT**

1. [XZ计划中的后门手法 - “NOBUS”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485524&idx=1&sn=aa2b7b0d57b250e5cc101e5dcbebbca6&chksm=fb04cb3ccc73422a9fe22937b801eceb205ceaf8bf3b76a92143d575d55e5fd2eef5adfacb36&scene=21#wechat_redirect)
2. [十个常见的归因偏见（上）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484868&idx=1&sn=3d65e81115c967b165fa16021a211967&chksm=fb04c6accc734fba7c760fd14caaaf9a2d7991acc2557ee340e772ccbb805b30f1a46c793e8a&scene=21#wechat_redirect)
3. [抓APT的一点故事](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485237&idx=1&sn=9152fcb5f5b1f884e6da97ba9b04f69a&chksm=fb04c45dcc734d4bd8fbede2ae93dc52feeaaa11e215a3240bca32f3d43444a2c909e01a2814&scene=21#wechat_redirect)
4. [揭秘三角行动（Operation Triangulation）一](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485278&idx=1&sn=9def52d0d9063e86acb16533be2a52e8&chksm=fb04c436cc734d20b8c67348f7db21fa10921ad3826b37c713e847b73972f50de82b6c1f1e6b&scene=21#wechat_redirect)
5. [闲话APT报告生产与消费](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485325&idx=1&sn=d0219cfe811afe5e8fc8729c603de2bc&chksm=fb04c4e5cc734df3a8ad433a992172c1a9a0f236fd69550c72eb499e1202d23b81f32b379259&scene=21#wechat_redirect)
6. [一名TAO黑客的网络安全之旅](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485451&idx=1&sn=5f794deaaccf45e7d81958eba82cd556&chksm=fb04cb63cc73427538546f24b1be7cd78375a9017498efb3fd2da46de5c38c0d4599c2e01100&scene=21#wechat_redirect)
7. [NSA TAO负责人警告私营部门不要搞“黑回去”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485250&idx=1&sn=a35def8b58f86f8a149e335f3df3a1c9&chksm=fb04c42acc734d3cdfd1e8f2ae852731c3569533ab8fa83bd0126b788ea20673a2f912cdf011&scene=21#wechat_redirect)

**入侵分析与红队攻防**

1. [入侵分析与痛苦金字塔](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485464&idx=1&sn=f05718bec99d4506a8fe1c49dc2bf337&chksm=fb04cb70cc734266a436d4225d4eb0486becaed5f0258748e6ff3de46a22caaa01b0da1b0e4f&scene=21#wechat_redirect)
2. [资深红队专家谈EDR的工作原理与规避](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485494&idx=1&sn=f45125e76dd412a291cfa3bccd5943c5&chksm=fb04cb5ecc734248332218f7df17be9a31d4b09777b8cd846b69821248a5e75b44baa6bfbfe4&scene=21#wechat_redirect)

**天御智库**

1. [独家研判：五眼情报机构黑客纷纷浮出水面](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485100&idx=1&sn=b88f8864594b76d4e1412db7cf204f77&chksm=fb04c5c4cc734cd2f5440ee760377afce1745a3abade998a40b9fe3752acb3be14574e6e6f9a&scene=21#wechat_redirect)
2. [美军前出狩...