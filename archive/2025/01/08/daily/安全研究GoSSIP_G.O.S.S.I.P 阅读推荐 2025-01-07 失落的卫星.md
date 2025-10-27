---
title: G.O.S.S.I.P 阅读推荐 2025-01-07 失落的卫星
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499572&idx=1&sn=51058d20ddd7d80dda3dde62f30cfe6b&chksm=c063d1edf71458fbe88bfb88241f777cf4f6d44761b2f18f8b106cabe53aa896de6a8ebe5a46&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-01-08
fetch_date: 2025-10-06T20:10:40.355250
---

# G.O.S.S.I.P 阅读推荐 2025-01-07 失落的卫星

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7xr7F5vD1fG3ibQDnFEUGAxMdVNzdyRRnbM7LlL8vibZXJndTSFGRnM6w/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2025-01-07 失落的卫星

原创

G.O.S.S.I.P

安全研究GoSSIP

今天我们不是来卖书的，虽然那本《失落的卫星》确实蛮好看。我们今天要给大家介绍的是刚刚过去的第38届Chaos Communication Congress上的一个有趣议题——*Hacking yourself a satellite*

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7xF88why7czkI3DP3rDy7fmhqCHtNjclOuAGoYicPcbuxA3WIRg8jN3A/640?wx_fmt=png&from=appmsg)

（注意到speaker头上戴的是什么了吗？）

这个报告的speaker是来自柏林工业大学（Technische Universität Berlin，TU Berlin）的`PistonMiner`（当然是id啦），他的报告内容是《重生之我如何远程控制了一颗真正的人造卫星》，之所以会去研究人造卫星，跟他的学校背景有关，因为柏林工大还蛮喜欢放卫星的（下图），还有一门课是专门教人造卫星操作的，`PistonMiner`在2022年选了这门课~~，为了学分苦苦挣扎~~，结果发现了一个非常有趣的事情：柏林工大2009年送上天的一颗微型人造卫星——BEESAT-1，在天上运行了两年（预期工作寿命是1年）后就持续发送无效信息而无法响应了，当时卫星控制团队启用了备份计算机，然后过了两年又出现了同样的问题，这时候已经是2013年了，感觉也赚回成本了，于是学校就懒得管了。但这种小卫星（体积约为10 × 10 × 10立方厘米）要过20年左右才可能重入大气层（烧毁），你可以想象一下你有一台在外太空的VPS（哇塞好酷，可以去跟朋友炫耀），结果ssh连不上去了（囧），但是放着这么个资源不用，好像有点浪费，这时候你该怎么办？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7d3oE3X8nFNJ3MMGuRAZfKPAZORKMJnDBiaxe4YzNY6eZsQU35f6keSw/640?wx_fmt=png&from=appmsg)

显然，要是能搞定这个问题，`PistonMiner`估计能拿到课程的高分，于是他就这么去做，而且成功了（为了通过数论课考试，我证明了哥德巴赫猜想）！首先他需要去学习这款卫星的技术细节，其他不说，光是通信速率只有4.8k bps（还是半双工）这种感人的上古数值就足以让人精神大振！当然，BEESAT-1卫星的硬件还行，至少不像阿波罗11号那么寒碜。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7YHZEVcNsHGKsKLNCWYKGdibOJ0EB9f3PNfXFEia5e1RTicNDxVLWrAQaw/640?wx_fmt=png&from=appmsg)

要跟这个酷炫的外太空VPS通信，有很多很多很多的困难，比如每天其实只有几个时间窗口（每次10-15分钟）可以通信。而且你还不敢轻易去尝试一些可能让本来就很脆弱的系统完全瘫痪的操作（目前卫星的状况好歹还能通信，只是一直在发送无效数据）。这时候就要考验大家的硬件知识了，比如“你懂不懂固态硬盘的工作原理”，`PistonMiner`大胆猜测，卫星有可能是在下图所示的状态，也就是flash memory的一个页正在被重写的过程中重启了，然后就只能读到全零的数据。我们亲爱的读者，你们了解这是为什么吗？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7oLg3xLTaq06slokwAibudgTHibv9YlsVicnSRs2LicxHr3969phkZAkLwA/640?wx_fmt=png&from=appmsg)

讲到这里，`PistonMiner`接下来就介绍了他使用一条远程控制指令（telecommand，TC）去修改内存（SRAM），然后下图这个已经10年读不出来的卫星数据就变了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad72192HzF3XRAf1w5sLtyibbQ6bS4RU13lebuCicPUPX4gQJD3vkJTNL2Q/640?wx_fmt=png&from=appmsg)

变成了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7fHD9y6j7dicIwxviaUZGTjHvUwHJaPVaYhtQ74YrHV8xPEjDiccYvDDgQ/640?wx_fmt=png&from=appmsg)

这时候全场响起了热烈的掌声，我们的speaker脸上露出了得意的笑容~ 但是得到黑客的认可容易，通过课程的考试难，`PistonMiner`接下来要面临的挑战很大：他找到一条TC指令读出了所有flash数据，发现有一个存储控制参数的区域的数据都丢失了，这时候就得想办法修复，但是总不能每天就坐在柏林等卫星经过的那短短10分钟吧？我们航空航天专业的同学肯定要嘲笑我们“连数字孪生都不懂”，在阿波罗登月计划时代，大家都知道送上天的设备要造一个一模一样的复制品，方便在地面上调试（嗯，阿波罗13号的时候还可以在地面上模拟灾难救援）。

所以呢，`PistonMiner`就去找BEESAT-1卫星的开发团队，想要看看有没有备用件，结果呢，不光没备用硬件，连团队的很多人都不在柏林工大了，当然大家还是很积极的回复邮件，把当时的软件（包括C++代码和固件）都发过来，给`PistonMiner`出了一个1000分的`RE`的题目，通过视频截图我们可以看出`PistonMiner`用的是BinaryNinja（这个广告费不知道给了多少）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7w81U2QEet4GDiamomsU8p3B21YVNXWNzxStIXfmibiavbGibzib2ibZvibSkg/640?wx_fmt=png&from=appmsg)

结果，你猜怎么回事，这个1000分的`RE`题目突然变成了1000分的`PWN`题目，为什么呢？因为BEESAT-1卫星没有什么固件升级的协议接口，只有一个很不好用的`CMD_WRTE_DWORD`命令，只能有限地修改数据，完全没法去更新flash memory的整页数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7pBFWzCQ4v9SqXaHjwBf4csc4ibIL8AgSgTE8ibVXJBwdh7AZMwzBjpYQ/640?wx_fmt=png&from=appmsg)

而且实际上整个卫星上可以临时使用的数据空间只有2K（本来应该是8K，结果BEESAT-1卫星开发组连续两次草台班子，导致可用空间缩水两次变成了2K）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7EOCic5geOhBfPocxEvhjh8SyjT7ibawlopac5Lzn8BCjNOShL2G71ViaA/640?wx_fmt=png&from=appmsg)

作为一名CTF选手（我们不知道他是逆向选手还是pwn选手），`PistonMiner`最后总算是发挥了特长，通过劫持固件代码的C++代码虚表指针（他专门感谢BEESAT-1卫星开发组这么喜欢用C++的继承）来劫持控制流，继而能够控制代码执行那个2K临时数据区里面的代码，实现flash memory的重写功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7TCYDjd7wfUw28KQ0P0ChO6ecULiaLg64bSOcYmic1s5ibr9XwP7vmLWGQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7aWqvIwHib7GiaibdWicrcic3Y9gXzvbXHEGG7ewmAlX2VMnI1JBpCBFf6wg/640?wx_fmt=png&from=appmsg)

做完了CTF题目，接下来回到课程设置的难题，要修复卫星的固件（大约300K），最理想也要两个星期：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7ytWWicC0450MEv3bBvRBm9ELOic3wLYFibPhOIbCFfIIxhnH1LUEskAKA/640?wx_fmt=png&from=appmsg)

同时还要考虑到有可能修复没做好，反而把卫星的flash memory彻底搞崩了，于是`PistonMiner`制定了如下的逐步修复计划，需要大约发送600次TC指令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7Cqev544XXb7qLVA9kUPTdgKFpqZFE6kPPUEA2Y7uINFOBXPu7R8nXQ/640?wx_fmt=png&from=appmsg)

在逐步更新image的过程中，`PistonMiner`还找到了一个原来代码的bug，并且在演讲的时候问大家“快看快看，你找到了吗？”，同时脸上再次露出了那种得意洋洋的笑容 技术直男果然只有在这个时候最兴奋。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7k8icW3G7gwMPCMay3DPULNCoj7ElKM4LGibib8QFrDg8iaPkWNf4TibcmiaA/640?wx_fmt=png&from=appmsg)

这个bug（少了个`break`）导致每次执行`TMS_GET_FLASH_DATA`操作的时候，卫星都会顺带拍张照（哈哈哈，给地球消毒），然而卫星的那个拍照软件代码是坏的……不但拍不出来照片，还费时费电。

反正就是一顿操作猛如虎之后，修复成功了！这时候`PistonMiner`再次收获了猛烈的掌声，以及第三次露出了得意洋洋的笑容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7kAial5eTpOibC5CQyrQzExaMFj8W4OM85YTJpd7lk55VbanGN9lz3KWQ/640?wx_fmt=png&from=appmsg)

> 别急，还没完。

刚刚不是说到那个拍照功能吗，那个camera似乎还没完全坏，能够拍一张非常低清的（只有9480字节）的照片：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7mM9UwdRxf5q96FEmX9qr3yvwahKKUwym6ibP3dqRI4y3dGlnUPphdgg/640?wx_fmt=png&from=appmsg)

但这也是来自太空的照片吖！`PistonMiner`第三次收获热烈的掌声，并第四次得意洋洋地微笑：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7qzJQNLCOLxJH5KQLWubrJxv7uibZXYpyO1Rrfl8b3jD9jqhQgcSfSfw/640?wx_fmt=png&from=appmsg)

然后他还想办法让摄像头在路过欧洲的很多地方的时候拍照片（还顺便解释了为什么没拍会议举办地汉堡，因为这地方上个月一直有云），以及第四、五次收获热烈的掌声+第五、六次得意洋洋地微笑：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7So2Of98xdaiaSkfl0e5KiawnVdDSBxopHC6T09icL0oDaPDrBNUwY5akw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7Fq9aHcySq3QXic1v7icfRsMNJeHhZMSed6BlNbOIpqcbT2HSBnrXEbww/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7X0xxu9AyjSMv4Xzv9YAg5z4JArcsKfpBtheqyFePPqKb2ibHUXSYR8g/640?wx_fmt=png&from=appmsg)

最后，`PistonMiner`通过分析BEESAT-1卫星数据，严谨地指出了他这个报告的最重要的科学结论——地球是圆的（收获掌声及洋洋得意微笑++）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7iadaftAQLEdibJ2KgwQYKWRoeicDrVibqXuicT0oTXCr22c0SWIutTv1srw/640?wx_fmt=png&from=appmsg)

---

最后插播一则2021年的旧闻：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7UeUd4ictjClzOSD4ichQiaa9jCf0ClSkS5icx2YPcuEaGV6Syg36GJLxRw/640?wx_fmt=png&from=appmsg)

> 只有3.7公斤重，80%的单机由学生自主研发；整星设计突破立方星能源限制，卫星可靠性显著提升；不仅能在太空中自动识别水面船舶信息，而且将在空间开展星间自组织通信新技术验证——这就是上海交通大学第一颗由学生自主研发并主导载荷设计的卫星——SSS-2A卫星。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7XzWEVv9tBJbibrMaDmr1kjnMetsviaeNG0aibAlibt1ZKWPtOBUZCTx2MA/640?wx_fmt=png&from=appmsg)

下一个硬核安全成果会出自哪所大学，不言自明了吧~

---

> 原视频：https://media.ccc.de/v/38c3-hacking-yourself-a-satellite-recovering-beesat-1

感谢`PistonMiner`也感谢（虽然有一丁点草台班子的）BEESAT-1卫星团队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GB5Z5y6UU8UMVFQyyicmad7rWoUQkicX81ZRSCI6xlt7mcV07zia73ut9At8RYWGKIeiczowB4Tqxwfw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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