---
title: 中国87亿条、国外240亿条信息泄露，业内人士称：泄露数十亿记录正成常态
url: https://mp.weixin.qq.com/s/K45uvStrmMg1kunDNdBt3A
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:46:28.525978
---

# 中国87亿条、国外240亿条信息泄露，业内人士称：泄露数十亿记录正成常态

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpedTVIzxDv5RjnWEPYdMro9bTlaicxS09QrWkBn5C04WLtBqmyeBYQoHSv0Hdp5Ovl13rLaiceqbbJZ9eian6RjfIoSMTsicMd7TmY/0?wx_fmt=jpeg)

# 中国87亿条、国外240亿条信息泄露，业内人士称：泄露数十亿记录正成常态

走狗是狗哥
走狗是狗哥

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

**[导读]**

近期网络安全研究团队曝光一起特大数据泄露事故，一家威胁情报企业因服务器迁移配置失误，致使存储 240 亿条、超 8.3TB 数据的检索集群全网公开。这批数据以窃密木马盗取的明文账号密码为主，源自 36 类非法渠道，涵盖勒索黑产电报群、历次泄露数据合集等。文中拆解数据构成、泄露成因，同步对比国内 87 亿条海量泄露案例，梳理近年同类特大泄露趋势，并面向普通用户给出账号防护实操办法，揭示海量用户数据裸奔、大规模凭证泄露已成行业常态化风险。

近日，Cybernews研究团队发现了一个公开暴露的数据库，内含240亿条记录，涵盖用户名、邮箱地址、明文密码以及登录网址。

数据来源复杂，主要包括窃密木马日志、受感染设备窃取的信息、Telegram渠道收集的内容、历次数据泄露汇编等。

**核心发现要点：**

**▶研究人员找到的是一个未做防护的Elasticsearch集群，总计包含240亿条记录，数据量超过8.3TB。**

**▶绝大多数记录属于窃密木马日志，内容为用户名、邮箱、密码和对应的登录地址。**

**▶全部数据来自36个不同源头，包括Telegram频道、历史泄露汇编、大型数据合集。**

**▶研究人员暂无法确认其中有多少重复记录，也无法统计受影响的独特用户数量。**

**▶目前该数据库已关闭公开访问，但用户如果复用密码，账号依然存在被盗风险。**

百万级数据泄露如今已屡见不鲜，但一次性泄露240亿条账号密码记录，依然远超常规水平。

也正因如此，研究团队在发现这8TB多的公开数据后，反复核验了三次才确认结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpfwGPEVIc3oLkMEPRIzUMs1ZANFhMiaDdIoz2dXGQ9lldfuC1ej4VGkxLTmv0QPOviaOyibcCjGsFljvyyBSWmHxBicgRTEaGiab7ko/640?wx_fmt=png&from=appmsg)

团队在6月12日发现了这批数据，它大概率是有史以来公开暴露的最大规模数据库之一。

其中绝大多数记录都是窃密木马日志，也就是被盗取的账号密码，以及这些凭证可登录的对应服务。

研究团队表示，这次凭证泄露的危险性，首先来自它极其庞大的体量。数据公开流出后，数十亿个账号都面临被接管的严重风险，没有开启多因素认证的账号尤其危险。

报道发布后，团队确认了数据集的归属：它属于一家威胁情报与泄露监测平台，用途是识别可能影响客户的安全风险。

数据暴露的原因，是平台在临时迁移过程中出现了配置错误。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpdSG05cFczlodqyiarbDoVxiapFb8W3rj0wcPUTLDpicrWXRfEmjwb0xVUuU3mE8Cheibn2KGJSSUCibrHD6g70DZXeJibIlIwO5Zsf0/640?wx_fmt=png&from=appmsg)

**泄露数据的具体构成**

所有记录都存储在一个公开可访问的Elasticsearch集群上，也就是一组互联的搜索服务器，总数据量超过8.3TB。

几乎所有暴露的记录都是窃密木马日志，也就是恶意软件窃取的敏感信息。日志里的登录凭证都是原始格式，每条信息单独保存，包括邮箱地址、用户名和明文密码。

除此之外，记录里还包含这些凭证可登录的网址，以及日志的来源渠道。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpfyibBS014XeMj7RBQTLCibLpSR6h7BLibmAl5KkvcgRrrZJ4dMyQrV6UBfDQNJCHfDY8zH06mKOHcSlEuhC4vs7GzicGhEkxInFVk/640?wx_fmt=png&from=appmsg)

这批泄露的凭证来自36个不同源头，范围很广：既有Telegram频道，也有历次数据泄露的整合合集，还有从目标服务器直接导出的数据集。

**涉及的Telegram数据泄露渠道**

其中约17亿条记录来自各类Telegram频道。

这些频道基本都和网络犯罪相关，核心内容就是分享被盗凭证和数据泄露资源。

36个数据来源里，有30多个都是Telegram频道，单频道的记录量从几千条到数亿条不等。

频道大多使用英文，也有一部分是俄语频道。

为避免变相推广这些非法渠道，报道没有公布具体频道名称。然而，大多数基于Telegram的记录据称是从与黑客相关频道获取的。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpc3wPE8RxsS7kUTHLdz1CWKkb3ibrYyT11kmaHEuzIyRrweSptNWfpw7tMZmQ2naLBTbRRIdvU2w2Hqf38oaOr4ZZDvwdibzSn6E/640?wx_fmt=png&from=appmsg)

除了账号凭证类频道，还有一类Telegram频道分享被盗的信用卡数据，其中有一个频道专门做这类内容。

值得注意的是，近2.6亿条记录来自名称带有“Darkside”的频道。

Darkside曾是全球最猖獗的勒索软件团伙之一，因攻击科洛尼尔管道运输公司、导致美国东海岸燃油供应中断而臭名昭著。

**占比最高的“数据合集”**

高达226亿条记录，被数据所有者归类为“合集”。

这些记录可能来自此前网上公开流出的各类窃密数据汇编，也可能是按照可非法访问的服务类型，整理分类后的凭证集合。

由于数据库很快就被关停，研究人员没有时间进一步追查这些“合集”数据的具体来源。

同样受时间限制，团队也没法精准判断这批数据涉及哪些服务提供商。但考虑到记录体量极其庞大，基本可以确定覆盖了大量用户基数极高的互联网服务。

研究人员还发现了一个标注为“本地数据库转储”的来源，包含1.5亿条记录。这类数据通常是从正在运行的目标服务器上直接导出的。

这部分数据有可能是服务器运营者自行上传到合集中的，也有可能是从其他渠道流转而来。

记录里还附带了数据导入时的源文件名，总计至少有195个不同的文件。

部分文件名显示，相关凭证来自AntiPublic合集，还标注了对应的账号类型。

AntiPublic是2016年首次出现的窃密日志合集，最初包含约6亿条记录。这次泄露里的相关数据，对合集做了进一步分类，比如单独整理成人内容服务、流媒体平台的登录账号。

另有1.46亿条记录来自“泄露汇编合集”来源，内容基本都是历次数据泄露流出的用户凭证。

攻击者非常喜欢利用历史泄露数据，因为用户普遍习惯复用密码，也很少主动修改。

所有来源里记录量最少的是“Redline窃密木马”，只有27条记录。

Redline是一款非常常见的窃密木马，以“恶意软件即服务”的模式运营，技术门槛很低的攻击者也能用来作案。

**数据所有者的特殊痕迹**

有意思的是，研究人员还发现了一小部分特殊记录，大约1.7万条，这类内容在普通数据泄露中非常少见。

其中有9500多份文档，包含通用漏洞披露（CVE）的编号、漏洞描述，以及对应的GitHub仓库链接，比如其中就包含ValhallGPU内核驱动的相关漏洞。

还有5200多份文档，是数据泄露相关的新闻报道日志，附带文章链接、正文内容和简短摘要。

最新的一篇报道发布于2026年2月，内容是针对Python包索引（PyPI）仓库的供应链攻击事件。

剩下2900条记录，是网络安全事件相关的社交媒体帖子，其中一条讨论了2021年Babuk勒索软件的运营细节。

所有这些信息都说明，数据所有者一直在持续跟踪全球网络安全动态，目的应该是不断把最新的泄露数据补充到自己的凭证库中。

**仍未明确的信息**

尽管可以确认泄露规模达到240亿条，但关于这个已经关停的Elasticsearch集群，还有很多信息无法核实。

首先是调查时间有限，研究团队没法深入分析“合集”分类下的具体数据类型。

其次是无法准确估算数据的重复率，因此受影响的独特用户数量没法给出精确数字。但可以确定，这么大体量的泄露，必然波及海量网络账号。

另外也没法精准判断数据的新旧程度。不过从里面包含2026年2月的新闻来看，数据所有者一直在定期更新集群内容。

报道发布初期，研究人员并不清楚数据所有者身份，后续才确认是一家威胁情报公司。

研究人员表示，企业收集这类数据，可以用来做泄露监测服务或者安全检测服务；而攻击者收集这类数据，则是为了寻找新的攻击切入点，辅助实施数据窃取。

团队认为，对于历史泄露数据来说，积累的体量越大价值越高。数据越全，分析结果就越精准，既能发现更多已泄露的账号，也能梳理出目标对象的潜在攻击路径。

**普通用户的防护建议**

想要保障个人账号安全，主动防范至关重要，几个简单操作就能大幅降低风险。

用户应尽快修改所有复用的密码，优先更换邮箱、社交媒体、云存储、网银等核心账号的密码。

尽可能开启多因素认证，使用密码管理器生成高强度的独立密码。

同时要警惕钓鱼信息，有些不法分子会打着“帮你查询是否泄露”的幌子，骗取用户的账号信息。

几个日常习惯，能有效防范窃密木马，大幅降低账号被盗的概率：

****▶********使用公共****Wi-Fi****时连接****VPN****，保障连接安全；****

****▶********不要随意点击陌生邮件、消息里的链接，不要下载可疑附件；****

****▶********及时更新设备的系统和应用，安全补丁通常会修复关键漏洞；****

****▶********所有支********持的账号都开启双因素认证，多加一层防护；****

****▶********只从官方应用商店或可信网站下载软件，避免下载到带毒的篡改版本。****

**十亿级泄露正成为常态**

遗憾的是，数十亿条记录规模的数据库公开暴露事件，正变得越来越常见。

今年早些时候，研究团队就发现过另一个暴露的Elasticsearch集群，包含160多个索引、87亿条以中文为主的记录，涵盖公民身份证号、各类商业数据等。

去年12月，团队发现过一个43亿条记录的数据库，部分数据来自领英，总量达16TB，包含邮箱、照片、工作经历等个人信息。仅其中一个合集就有7.32亿条带照片的记录。

2025年7月，Cybernews研究人员曾发现史上最大规模数据泄露之一：多组登录凭证合集总计160亿条记录，共30个公开数据集，单组记录量从数千万到35亿不等。

而能和这次240亿条规模相比的，是2024年发现的一次超大规模泄露。那次泄露整合了多次历史泄露数据，总量达12TB，包含超过260亿条记录。

原文链接：https://cybernews.com/security/24-billion-credentials-data-leak/

**安在企业（用户）会员服务**

**助力全生命周期安全意识提升**

“安在企业（用户）会员服务”，为所有企业提供一站式的网络安全支援服务，包括意识宣传、培训教育、效果检验、专业圈子、知识社区、专业培训、参选评奖等多个板块，助力网安从业者高效履职，实现个人与企业安全能力同步升级。

**[小投入大防护！安在推出企业（用户）会员服务](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)，点击标题阅读详情。**

深度贴合企业不同规模、安全水平投入以及员工安全意识的不同发展阶段，特设5级安全意识培训服务体系，为企业用户量身匹配适配的安全意识解决方案。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpfxauQUKv5E2gfFrpMBAz1Um7FAY4ontydFQQ1ZKtH1AnXs3kfYxtOYX55xrRBM2pFYicz2sqACyjd4u1CO2iaAFCYLIbgMGS58M/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpevFQuuGbgqzRQXxpZt2NQG9gkeSfhrKIBL6NVagjD9IYhtko4pjEdkrmiaAFfGAYPQN06Cs2MSLG4HGqExqL1OJ9n0ZSmibwO9Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

本文展示所有类型素材，均包含在企业（用户）会员服务中，如有意向，欢迎垂询。

**加入诸子云知识星球**

获取更多“安全意识资料”和“网络安全报告”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpevtB5U1iad3jHVWSBznd4wGSnt15KjDpDvdDAzWfLewNRoKHVyCNTCEIVkuJAZOyUvKSibQZJfe43xQsofxEKuB4xuj2gzBG4EM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfphwUVRfsnQ4tHXQicImFKOyric81wyOR6UtibaU9W2nPpF2bIflBltg8S0vJMmYEDrEkWN30lpxicg5YUyLDu0fAlCgX3ibJBX8Ys/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcHLAPdhJaKhut2fLyfnDD0ofblclhTxwQtdjZ9Wnsgw7qtANaolbmpYLhf9mCW9ib2vDial19qZnEibibEZkAcOVPZVTA9QsD5EeY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcaBf7luDbkibnkcG6SFanyicuIePMSYCXyZ4dpRTDOuRkj4IwafHmia3a61q1QmasWkERH6vhD4eicgePFZCERRib6zAefEHxWz3cY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcoibvzpu3KUfibMYf9yTU7VWPXP10LBBkle2fQKqqdVk7zLYiaoh0bHWxmovw4aqY0icMXYfqY2TW0LibL3W2NVG5u6ibA9aDyzsF8I/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpfHuRbxczmKK36HLRfSVxysIgBAQMVFSdVGCDascdwN2jmE6LickWQ9nyK1k0fVcibLIYwaseCvT2VtXEoVubWyMLdmf9jRo59JY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpd5O3toB6xb2AkuS2RcTBYTLu0nY8LibtS5iaZCyjdwbYYvsFA52ib67sdZdjG5Irwcs962K5KttO7qbKW4eEBYNtKkJUKBfHGI0s/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpd8PSnWIlP6x8ytDuhBpQc307z6BWzOD6flZLjlIYYXXU1NKpN5gXPjeq2mAPqgJm6Bd82h2IOL1rNSU0REl8Z7LOmpoU1NjS4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcGyRCee3d61E6ibYFh5VeHPicnicIloE3Iia6Bvud9Ok8cJOYYu0s4aIIXNltmfiagic87u2yvKdIDY6Px4iaaFwOh1h0B17rs0nibSlo/640?wx_fmt=jpeg&from=appmsg)

**<**

**滑动查看下一张图片**

**>**

******END****

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AAfIzicyojXwPTCxD0QGZHhyRcRicJAHhUv382sYFibICoxjzktlJwEEPag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibILU2vpTY8kPMvg2uyDyibiaFibHCDibF1vCIjn2tNAKdNicq3Y45vuYuWNUDICSF8dZ206dy1Kzrehug/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)](https://mp.weixin.qq.com/s?__biz=MzU5ODg...