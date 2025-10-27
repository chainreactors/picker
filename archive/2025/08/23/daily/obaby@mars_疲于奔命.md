---
title: 疲于奔命
url: https://h4ck.org.cn/2025/08/21382
source: obaby@mars
date: 2025-08-23
fetch_date: 2025-10-07T00:18:29.023113
---

# 疲于奔命

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 疲于奔命

2025年8月22日
[64 条评论](https://h4ck.org.cn/2025/08/21382#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250822105109_58.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250822105109_58.jpg)

最近这几天，的确是没什么时间来写点东西，每天都在与代码拼命抗争。另外就是之前处理的服务器被入侵貌似远没结束，还有一些乱七八糟的东西需要处理。

上周对象把博越送去保养，汽修厂的说减震没有问题，不过刹车片、火花塞需要换了。于是保养完又换了这两项，加起来又一千多。这乱七八糟的钱真的是不禁花。每天都有这些乱七八糟的事情，最近粉皮的保险也快到期了，月初各种电话，反而是这几天真的快到期反而消停了，也不知道到底是什么逻辑。

前几天  **[陈沩亮博客](https://www.chenweiliang.com/) 提示说我的友联检测不到：**

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250822-105821.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250822-105821.jpg)

然而，自己看了一下没什么问题。但是他却一致纠结这件事情。其实不想管这事，主要还是最近太忙了。项目用的国产时序数据库，数据写入和查询一直有问题，让 cursor 给修复，结果这小众的玩意儿她也很无奈，甚至一度直接给干废了。

[<https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250820-185721-HD.mp4>](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250820-185721-HD.mp4?_=1)

对于这种结果也是真的无奈了。但是还是要继续啊。既然有人坚持，那就去看下到底什么问题吧，结果不看不知道，一看吓一跳。真的 tmd 全部的链接在百度爬虫访问的时候都变成了 moban 什么狗屁玩意儿：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250822-110244.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250822-110244.jpg)

这 tmd 就很艹了。直接搜索moban 最后在 class-wp 中找到了这个东西：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250822-110413.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250822-110413.jpg)

真 tm 防不胜防，直接下载 wp 的原始安装包，替换这个文件一切恢复正常。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250822-110511.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250822-110511.jpg)

感谢这哥们的坚持。

昨天中午，实在不知道吃什么想着汤姆家的牛排还有余额，于是跑去万达吃牛排。结果回来的时候，一 jio 油门下去发动机故障灯亮了：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250822105305_60.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250822105305_60.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250822105305_61-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250822105305_61.jpg)

下午开去四儿子店，一个小时的检测之后告知氧传感器坏了，给索赔了一个，让等电话，到了之后过去换。问在哪里加的油，感觉油品有问题。

既然油品有问题，那就去中石化吧，问怎么加油优惠，说买优惠券。看了一下感觉不合适，就放弃了。让那个大哥直接加。

刚来的时候就说了加 95，结果那个傻屌直接用 92 的油枪就开始加，好在自己看了一眼，问不是该加 95 吗？！

那大哥都懵逼了，我当时 tm 脸都绿了肯定。这 tm 脑子是装了些屎吗？艹！

重新给换到 95 继续加，说不好意思，给送了瓶玻璃水。我拿了东西也没搭理他，真 tm智障。好在 tm 就加了 200。

最后也没注意92 是加了 3 升还是 5 升，艹！开到公司后，总感觉不对劲，于是跑到中石油重新加满了 98，算是标号能够中和一下。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250822105305_59.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250822105305_59.jpg)

不过这 98 是真 tm 贵。

最近晚上休息也休息不好，做梦都 tm 在改代码。半夜热醒了，忽然想到对象说的，加油站那么多的 666,888 去加油应该没问题。于是翻了下加油记录，发现最后实在老家的壳牌加的。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250822105305_62-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250822105305_62.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/微信图片_20250822105305_63-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250822105305_63.jpg)

这忽然又有种似曾相识的感觉，最开始开小六子回老家去小加油站加的油，回来就让维修发动机。从此再也没去过路边的小加油站，这次传感器坏了，这尼玛壳牌的 95 也不能加了？

对象说，肯定是忽悠你呢，本来就是要坏，非得说油不行。对于这个问题，我是没办法求证的，我也不知道是不是他最终要坏啊。坑爹！

不过不得不说，这破 java 真是写的够够的，太 tm 麻烦了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250822-111838-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250822-111838.jpg)

题外话，这几天还遇到一个大哥也 tm 神奇：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/4FF68B45CE410283FF6D899FDA8D68B9-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/4FF68B45CE410283FF6D899FDA8D68B9.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/5C3A03FDC4746970E5E394D4009E3A8F.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/5C3A03FDC4746970E5E394D4009E3A8F.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/D69C3E70188E194A2DADE2511DFF2653.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/D69C3E70188E194A2DADE2511DFF2653.jpg)

这尼玛想屁吃呢？CSB！！

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《疲于奔命》](https://h4ck.org.cn/2025/08/21382)
\* 本文链接：<https://h4ck.org.cn/2025/08/21382>
\* 短链接：<https://oba.by/?p=21382>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[cursor](https://h4ck.org.cn/tags/cursor)[Java](https://h4ck.org.cn/tags/java)[传感器](https://h4ck.org.cn/tags/%E4%BC%A0%E6%84%9F%E5%99%A8)[修车](https://h4ck.org.cn/tags/%E4%BF%AE%E8%BD%A6)

[Previous Post](https://h4ck.org.cn/2025/08/21408)
[Next Post](https://h4ck.org.cn/2025/08/21364)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2024年12月2日

#### [双城记](https://h4ck.org.cn/2024/12/18679)

2024年12月20日

#### [紧箍咒](https://h4ck.org.cn/2024/12/18838)

2023年11月14日

#### [双 11](https://h4ck.org.cn/2023/11/14268)

### 64 comments

1. ![](https://gg.lang.bi/avatar/604cb20b7fcb11384bfabc696c53425c9bb9f2c261657f6667bfd4e889ed0bee?s=64&d=identicon&r=r) **[云晓晨](https://blog.kaiqi.wang)**说道：

   [2025年8月22日 12:25](https://h4ck.org.cn/2025/08/21382#comment-128056)

   ![Level 2](https://badgen.net/badge/亲密度/Level 2/cyan?icon=codebeat)

   ![Microsoft Edge 139](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 139") Microsoft Edge 139 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   林子大了什么鸟都有，有些人真的无法理解。我们小县城这边95才5.8左右

   [回复](#comment-128056)

   1. ![](https://gg.lang.bi/avatar/b8988a975c704d67b3fe29316a8314fd33d3581287414b9c43e56c34f9d79d1e?s=64&d=identicon&r=r)

      [2025年8月22日 15:20](https://h4ck.org.cn/2025/08/21382#comment-128066)

      ![Level 1](https://badgen.net/badge/亲密度/Level 1/gray?icon=codebeat)

      ![Microsoft Edge 139](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 139") Microsoft Edge 139 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      你别说话，太拉仇恨🤣

      [回复](#comment-128066)

      1. ![](https://gg.lang.bi/avatar/604cb20b7fcb11384bfabc696c53425c9bb9f2c261657f6667bfd4e889ed0bee?s=64&d=identicon&r=r)

         [2025年8月22日 15:26](https://h4ck.org.cn/2025/08/21382#comment-128067)

         ![Level 2](https://badgen.net/badge/亲密度/Level 2/cyan?icon=codebeat)

         ![Microsoft Edge 139](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 139") Microsoft Edge 139 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         哈哈哈哈哈

         [回复](#comment-128067)
      2. ![](https://gg.la...