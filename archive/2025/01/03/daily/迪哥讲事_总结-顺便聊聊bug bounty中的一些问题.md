---
title: 总结-顺便聊聊bug bounty中的一些问题
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496729&idx=2&sn=14d09002327955c31cc61230268f434c&chksm=e8a5fe7adfd2776c35dfd955b243f48b78b5d57f3ce451d693c1eca3eab197cb058c458b65cb&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-01-03
fetch_date: 2025-10-06T20:10:18.947800
---

# 总结-顺便聊聊bug bounty中的一些问题

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7viaS9lTiazlyibfM5Ra69e0mausyDlM0IHE151BNiaOuvLq9dx7VYvjSnSvvkaydrtkxGj8ITf7EKvQ/0?wx_fmt=jpeg)

# 总结-顺便聊聊bug bounty中的一些问题

原创

richardo1o1

迪哥讲事

总结-顺便聊聊bug bounty中的一些问题

## 正文

一眨眼功夫,2024年过去了,时间飞逝,近几年越来越感受到时间走的越来越快,现在对时间也越发珍惜.

回到正题,整体来说,2024年和以前相比有了一定程度的进步,挖到了一些漏洞(尤其ssrf和和一些越权等逻辑漏洞)

当然在这过程中遇到了很多的问题和困难,也都一一解决了

有些同学也问过我一些问题,有些问题比较典型,我也为之比较苦恼,现在来分享一下,并讲讲相关解决思路

## 几个典型问题

**1.一些公开的项目,尤其是大型厂商,这些厂商是被很多人测试过的,我还有没必要去测?**

答案是有必要,为什么这么说,有以下几个原因:

1.1:每个人擅长的点不一样,有的人擅长a类型的漏洞测试,有些人则擅长b类型的漏洞测试,即使主要范围已经被测试过,仍然可能存在未被发现的漏洞或问题;

1.2:厂商的业务是持续更新的,尤其是一些大厂;

1.3:有些业务很显然是大概率测试不出问题的,但是你依然要去测，还有一个非常重要的原因,就是你要去熟悉业务,什么意思?这次你没有测出来,你下次再次看到的时候,你心里就有底了:这个点位我上次来测试过xx漏洞的,没有问题,这次我就暂时不看,那这里我就看看有没其他的什么新的功能点,或者说后面某个时间点我学习到了一个新姿势,正好想起来某个点位可以测试,那我就来这里尝试一下

**2.怎么样才能找到一个适合我们自己的厂商?**

这是一个非常典型的问题,其实我也陷入到过这样的一个困惑:不知道选择哪(几)个项目作为我的目标?不知道怎么入手?

最近我发现了一些可落地来解决这个问题的方法,这里我就来分享一下

首先分析一下原因:

为什么我们很多人很难选一(几)个作为长期目标?

* 心猿意马:我们有时候在专注某目标a的时候,有时候某个群里面或者社交媒体里面经常有人分享我在某某厂商那里拿到了多少多少赏金,然后下面一堆跪舔的,也不分享技术,然后我们很多时候也会去看看这个人所挖掘的厂商是不是也"很容易",久而久之我们把我们自己原本的目标给“抛弃”了,也就是说今天搞搞a目标,明天搞搞b目标,大后天搞搞c目标,总是三心二意,心猿意马,总觉得别人的"目标"更香
* 心里层面的障碍,我觉得a目标很难,要不换成b,看了几天以后,发现b也很难,如此反复,最后啥目标也没深入,被所谓的难度吓到了
* 完美主义者,我要找到那个“完美”的厂商项目,我想要一击即中,不想浪费一丁点时间在不适合我的项目上面,不想走任何弯路,其实这类人在我们生活里面有很多,具体表现出来就是做事不想走弯路,想要一步到位。

**1.为什么总是觉得别人的“目标”更香?**

从本质上来讲,凡是公开的有赏金的项目,对大多数人来讲,没有一个是非常容易的,如果有容易的,每个人都会抢着去做,谁不喜欢轻松赚钱呢?即使它们真的有,也很难轮得到你,从心理学层面来讲,看到别人赚到钱,尤其是赏金很高的时候,会产生一种错觉,什么错觉呢?好像赚钱很容易,咦,别人赚到很多钱了,我应该也能马上就能赚到,其实这是一种错觉,你所看到的是别人拿到赏金的那一刻的高光点,别人为了拿到这个赏金的背后所付出的努力你是看不到的,之前我看到一个白帽子记录了从0基础开始到拿到第一笔赏金所付出的努力:光纯测试的时间就达到100+小时,学习的时间达到200+小时.也就是说你很多时候看到的只是人家拿到赏金的那一刻,但是这背后的几百小时的努力你是没有注意到的!

解决方案是什么?

自己定义一个"好"的目标的标准,比方说,对于国内的厂商,一个中等危害的漏洞的赏金要达到500元以上,对于国外的厂商,一个中等危害的漏洞的赏金要达到500美元,厂商响应效率要达到90%以上

**2.为什么做事不想走弯路,想要一步到位的思路是有问题的**

这里我想借用伟人的一句话:错误常常是正确的先导.

扯远点说,一百多年前,中国处于一片混乱的状态,无数仁人志士也是尝试了各种方法去拯救中国,什么洋务运动,戊戌变法,三民主义,最后才试出马克思主义去拯救中国

雷军在《小米创业思考》里面也传达了一种思想:不要妄想一步到位就能做出一个完美的产品,而是要先做出一个雏形,和用户保持沟通,根据用户的反馈和吐槽,对产品进行迭代,不断完善。

历史告诉我们,想要一步到位,不走弯路,不"浪费"时间,是不切实际的,除非你是天才,其实生活里面大多数人都是普通人

**3.如何克服心里层面的障碍**

这里我给出一个大致的应对策略,给自己设置时间限制,这里举个例子,比方说我要尝试a目标,我会设置90小时的限制,就是说我会在这个目标上面尝试测试的时间至少要有90小时(不包含信息收集以及学习的时间),如果90小时以后仍然一无所获,我会切换到下一个目标

详细版本的操作策略我会在星球里面给出,后面我也会在星球里面定时周期性的分享我实时测试的进度(这个好像目前国内没有人这么做),以及我的一些思考

最后打一波广告:元旦了,发一波优惠券

以往的评价:

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5HWxQHfYQJbcAIvIpgr0n3horhcqB3Wia0rAgzZiaEHXFwUdLMaRQZEvSUX2h95sXJ3s79JicokkkzQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5HWxQHfYQJbcAIvIpgr0n3Xs7KmMCp4mWNY8APZ5LyfPeqDcsWFeZKa2KJ1d52XwwNM3dUZ1gPibw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7viaS9lTiazlyibfM5Ra69e0mWYaPbgticKXaCuq0N09ZrohKzPogb7gnZMC6u9tbFMumn0l5fBbHSxw/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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