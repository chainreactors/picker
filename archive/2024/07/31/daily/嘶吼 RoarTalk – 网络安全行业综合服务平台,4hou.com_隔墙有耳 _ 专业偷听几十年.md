---
title: 隔墙有耳 | 专业偷听几十年
url: https://www.4hou.com/posts/MX85
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-31
fetch_date: 2025-10-06T17:41:06.934679
---

# 隔墙有耳 | 专业偷听几十年

隔墙有耳 | 专业偷听几十年 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 隔墙有耳 | 专业偷听几十年

RC2反窃密实验室
[技术](https://www.4hou.com/category/technology)
2024-07-30 17:47:45

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)126477

收藏

导语：关于“隔墙听”的一些事: 专业设备、早期原型

![1.1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411320894016.jpg "1720406174129081.jpg")

**声明：********以下内容符合********OSINT国际开源情报搜集标准********，不涉及任何非法行为，仅供交流与参考。******

********0x01 先聊聊酒店的墙壁********

咳咳，行有行规，先说点正经的。

按照国内酒店装修必须遵循的行业标准**《旅馆建筑设计规范》****JGJ62-2014**中规定，旅馆建筑的隔声减噪设计应符合现行国家标准**《民用建筑隔声设计规范》GB 50118-2010**的规定。

如下图所示，可以看到，墙壁厚度还真是和酒店级别有一定关系的。

********![1.2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411321696467.jpg "1720406282192824.jpg")********

![1.3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411321123236.jpg "1720406305117107.jpg")

不过在装修的行话里，老师傅们一般会更通俗地用“**一砖墙**”的说法。所谓“**一砖墙**”，顾名思义就是厚度为一块标准砖的墙，类似地，就有了“**半砖、1砖、1砖半、2砖**”墙的说法。

说到这儿，顺便调查下，这些年大家住过的酒店，你认为客房墙壁有多厚？

********PS：********更多关于墙壁厚度的定义，大家可以在评论区里回复********“一砖墙”**，******就能看到。

那么，按照装修标准，是不是说五星级酒店客房就一定安全呢？

**这个嘛，真不好说。**

**0x02 一般人如何偷听隔壁**

**经常出差的人应该都有过这样的体验，尤其是苦逼出差的IT工程师们，撰写项目文档或做编程测试不知不觉到半夜，突然被隔壁莫名的声音惊扰。**

**除此之外，明显对内部会议、私下聊天的偷听会更有意义。于是乎，什么听诊器、杯子等都被人用来做偷听道具。**

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411321157759.jpg "1720406474150759.jpg")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411322541783.jpg "1720406480155331.jpg")

****百度知道上，甚至还有人专门回答了用杯子偷听的心得，也是醉了。****

****![1.6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411322903055.png "1720406746209098.png")****

****嗯，肯定有老司机觉得这些都太基础了，根本不值一提，也是，接下来说说专业的做法。****

******0x03 专业隔墙偷听几十年******

从原理上讲，专业偷听设备的确类似于听诊器，不过区别是，专业设备加入了电子降噪及放大的能力，所以也被称为：**室内物理音频放大设备****。**

**即行业里常说的：“**隔墙听**”。**

嗯，这个知识点刚好和上一期的**“**[****远程室外物理音频放大器****](http://mp.weixin.qq.com/s?__biz=MzIzMzE2OTQyNA==&mid=2648949651&idx=1&sn=cddc9b6870d66d2a41587697a7cba5ac&chksm=f09ed4ecc7e95dfadb0a382512caf7bf16bd4d919a28d65e3029d51a1e9f1ea3f958629dd457&scene=21#wechat_redirect)**”**互为补充。当然，和室外设备不同，**“**隔墙听**”**主要被用于对办公室、内部会议、私下聚会等室内环境的监听。

“**隔墙听**”设备，通常包括一个高灵敏度电子降噪放大器，一个包裹在金属外壳中的柱状超灵敏麦克风，一副监听耳机以及发射天线。

![1.7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411323432332.jpg "1720406809299719.jpg")

在使用的时候，要将柱状探头(麦克风)紧贴在目标墙壁上，理论上，只需要通过调整降噪模式，就能听到隔壁的声音。

******![1.8.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411323630416.jpg "1720406837186254.jpg")******

不过实际上，几百元至一两千元的民用低端产品，与上万元的专业高性能“**隔墙听**”设备之间，效果差距是非常大的。

呵呵，一般而言，民用款遇到“**一砖墙**”基本就没啥用了，个别甚至“**半砖墙**”就完全失效。

![1.9.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411323138328.gif "1720406880142855.gif")

下图是一款军用级“**隔墙听**”，可以轻松实现“**一****砖墙**”以上厚度的监听。啧啧，就是真心不便宜啊。

![1.10.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411324209641.jpg "1720406905188589.jpg")

******韩国电影《**特工**》（又名**北风/北寒谍战**）里描述的是中国改革开放初期，来自南韩和北朝鲜的间谍们在中国北京及朝鲜平壤间展开的一系列骚操作。******

******![1.11.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411324209136.jpg "1720406933640270.jpg")******

其中有一个片段，南韩间谍使用了专业“**隔墙听**”透过天花板的预制水泥板，来偷听上层会客室内几位大佬的聊天内容。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411324191603.jpg "1720406974173785.jpg")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411325125876.jpg "1720406980871306.jpg")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411325477521.jpg "1720406986881592.jpg")

最近热映的韩国电影《**南山的部长们**》，以韩国中央情报部(KCIA)的部长们(副总理级)与他们所主导的政治阴谋为素材，讲述了1979年被称为第二掌权者的中央情报部部长在韩国总统暗杀事件发生前40天间的故事。

![1.15.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411326161094.jpg "1720407201195209.jpg")

********影片中展现的国安级设备也非常专业，**在电影中，韩国中央情报局局长，就使用了专业“**隔墙听**”，来偷听总统谈话。******

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411326194668.jpg "1720407377101464.jpg")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411326917176.jpg "1720407382293863.jpg")

是不是觉得这简直是居家旅游升官发财覆手为雨防不胜防的必备杀器？在**L2隐私保护课程**中，学员们也会学习这类器材的防御方式，这里就不再重复。

下图是两年前，杨叔代表**R****C²****反窃密实验室**和“**全日本综合调查业协会**”交流商业调查员器材，其中就有商业级“**隔墙听**”。

![1.18.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411327161146.jpg "1720410644166330.jpg")

********0x04 再加深些了解********

杨叔和一些所谓的“反窃密行业”的人交流过，很无语地发现除了真正的科班出身，其实大部分人都对包括“**隔墙听**”在内的很多器材一知半解，仍停留在“满嘴跑火车为了卖设备瞎吹嘘”的阶段。

比如，“**隔墙听**”的早期原型，压根不是用于墙壁及其他介质监听的。它最早不过是汽车工程师的一种工具，通过对发动机内部声音的分析，协助判断可能的故障。

********![1.19.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411327113949.jpg "1720410738149525.jpg")![1.19.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411327113937.jpg "1720410767210304.jpg")********

慢慢地，这个概念引申出一系列可以通过墙壁、地面、隔板和其他介质的声音放大设备。比如在早期的情报界，专业的“**隔墙听**”设备基本上都通过探针式麦克风来完成，这一点和原型非常相似。

杨叔翻看了很多公开/半公开的情报资源库，找出了这款在1980年代后期制造的国安级专业“**隔墙听**”套装，如下图所示。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411328175694.jpg "1720410895179706.jpg")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411328785578.jpg "1720410900941092.jpg")

该“**隔墙听**”套装包括一个具有宽动态范围的高灵敏度放大器，一个包裹在金属外壳中的超灵敏探针式麦克风，以及一副超保真耳机。

![1.22.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411328169928.jpg "1720411013169018.jpg")

那个时候的监听人员，只需要将连接麦克风的探针插入墙壁上的小孔，就可以监听隔壁房间中的任何声音。

![1.23.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411329930638.jpg "1720411063997669.jpg")

同样地，也可以通过钥匙孔监听隔壁房间中的对话。

![1.24.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411329185467.jpg "1720411150475592.jpg")

如果没有现成的孔洞，监视人员会使用特殊的钻孔工具，在墙上钻一个小孔，却不会在另一侧留下任何痕迹。所以为了应对墙壁、天花板等不同厚度介质，这款专业套装里也提供了四个不同长度的探针。

![1.25.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240708/1720411329128228.jpg "1720411259125055.jpg")

当年，**CIA**甚至专为这个套装额外配备了最早用于秘密监听的动态麦克风和专门设计的电子探针。

What？多少钱？在哪儿买？嗯，不好意思，信号不好听不清楚，专业内容到此为止，不再深入讨论。

**0x05 如何防御？**

很遗憾，由于默认情况下，“**隔墙听**”设备自身不会发射任何无线信号，所以没有办法通过对无线信号的监测来发现（**PS：**虽然“**隔墙听**”设备支持将语音无线发射，但一般都不使用这个模块）。

这就是为什么每次有朋友询问有什么“**反窃密**”的随身设备，杨叔都会先确认具体场景和需求，因为没有什么设备是一劳永逸的，完全取决于实际需求环境和使用场景。

和我们常说的酒店隐私保护要求一样，一般来说，**加大环境噪音**是个很取巧的防御方法，其它一些方法杨叔已经在上篇科普文里提过了，来回复制粘贴也没意思，要不大家再抽空温习下？

[**“远距离语音监听 ▪ 来自网店的解决方案”**](http://mp.weixin.qq.com/s?__biz=MzIzMzE2OTQyNA==&mid=2648949651&idx=1&sn=cddc9b6870d66d2a41587697a7cba5ac&chksm=f09ed4ecc7e95dfadb0a382512caf7bf16bd4d919a28d65e3029d51a1e9f1ea3f958629dd457&scene=21#wechat_redirect)

**----**END**-----**

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!
...