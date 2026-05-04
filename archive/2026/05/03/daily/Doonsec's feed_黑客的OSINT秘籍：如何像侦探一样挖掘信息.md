---
title: 黑客的OSINT秘籍：如何像侦探一样挖掘信息
url: https://mp.weixin.qq.com/s/2ph2PyG8M8IKimyd4wmgnA
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:31:49.313430
---

# 黑客的OSINT秘籍：如何像侦探一样挖掘信息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibdiblnvxoucv36sTwJjwmynyZ7kibzyqJHs1BiaiazPhPWWaDfNUOaVACibibdzvu050mmTgt3ibAvxoOyrqMFXadc7oVCapiczHsXibQEk/0?wx_fmt=png&from=appmsg)

# 黑客的OSINT秘籍：如何像侦探一样挖掘信息

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 这场演讲由红队专家Liam McWhorter分享，核心是打破常规思维的OSINT方法论。他讲了如何用电话号码变体找到隐藏网站，如何创建假身份潜入LinkedIn，以及AI在情报收集中如何帮倒忙。干货很多，但也有坑。

## 别以为找不到就是没有

Liam和他的老搭档Sandra Stivers干了件挺有意思的事：把私家侦探的调查手法和红队的渗透思维揉到一起。Sandra是欺诈调查员出身，Liam是搞红队渗透的，俩人合开了一门OSINT课程。Liam说，Sandra教给他的第一课是——**你没找到，不代表它不存在**。

她办过一个案子，查一个诈骗网站背后的主使。网站上有个电话号码，她用常规方式搜，连字符、括号、引号都用上了，愣是什么都没找到。后来她直接复制了网站上那串号码，连空格都不删，粘贴到Google里，居然搜出了另一个网站——同一个号码，但每个数字之间都带着空格。原来这家伙在复制HTML代码时把空格也带过来了。靠着这个，她用Wayback Machine找到了网站早期版本，揪出了真实姓名。

所以别只盯着标准格式。电话号码可以写成2-1-3-5-5-5-1-2-1-2，也可以写成2 1 3 5 5 5 1 2 1 2，或者2/1/3/5/5/5/1/2/1/2。日期格式也一样，12/31/2024和31/12/2024差着十万八千里。如果你在给跨国公司做渗透测试，记得切到当地时区再搜一遍，结果可能完全不同。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibdiblnvxoucv36sTwJjwmynyZ7kibzyqJHs1BiaiazPhPWWaDfNUOaVACibibdzvu050mmTgt3ibAvxoOyrqMFXadc7oVCapiczHsXibQEk/640?wx_fmt=png&from=appmsg)

## 假身份是个技术活

创建马甲账号是OSINT里的高阶操作。Liam说他在红队行动里经常这么干——不是去骗人对话，而是去“听”和“学”。比如给一个市政部门做渗透测试，他不用直接跟任何人聊天，但会伪造一个LinkedIn身份，关注那些员工。他发现技术人员特爱炫耀自己用了什么工具，解决了什么问题。翻翻他们的帖子，你就能摸清这家公司的技术栈，知道他们用的是AWS还是Azure，数据库是MySQL还是PostgreSQL，甚至连他们没公开的卫星办公室都能找出来。

Sandra有一套创建假身份的流程。首先，别用太普通的名字（比如Bill Smith），也别用太猎奇的，容易被追踪。然后同时开两个浏览器窗口，一个Gmail，一个ProtonMail，两边试探用户名能不能用。比如你要叫Sam Colton，试到S.Colton1993可用，就用Gmail注册，再把ProtonMail设成找回邮箱。这样交叉绑定，就算丢了一个账号还能找回来。

Liam更进一步，他会为每个假身份单独开一个虚拟机。背景图片、壁纸颜色、桌面图标都按角色设定好。比如Sam Colton是个环保主义者，就把壁纸设成绿色，把Gmail账号贴在桌面上。启动这个虚拟机，他就是Sam Colton，不会手滑登到自己的Twitter或LinkedIn上去。这在做多角色渗透时尤其重要——你不想让左派活动家身份和右派保守派身份互相串门。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibe9lGQECJIsav47XNWfBAic8CgmX6qZDOhhUgzJtBslF9qxsuJ1Gm7qb4J4epfp3hXGroAUD8ox3nNvKTxajRxsZHNLG2Y5AN90/640?wx_fmt=png&from=appmsg)

## AI：能帮你省活，也能把你带沟里

AI现在是个绕不开的话题。Liam的态度很务实：**能用的地方就用，但别全信**。他拿“天空为什么是蓝色”这个经典问题试过几十个AI，95%都能答对，因为标准答案翻来覆去就是那些。但你要是问“如何在Ubuntu上安装某个软件包”，AI不一定靠谱——它可能给你抛个yum install，Ubuntu根本不用yum。再复杂点，比如政治、性别话题，AI就开始胡说八道了。

Liam讲了Sandra亲身经历的案例：一个女客户找她调查丈夫，因为AI告诉她说她丈夫是个性犯罪者。Sandra查了个底朝天，发现那人连张超速罚单都没有。AI只是根据名字相似度——六个字母里有三四个相同——就匹配错了人。这年头AI的幻觉不是小概率事件，你得学会交叉验证。Liam的做法是：向多个AI问同一个问题，如果答案一致，那基本可信；如果打架，就去查原始资料。

他还提到了“对抗性提示”这个野路子。比如在DEF CON上，有人用“祖母故事”骗ChatGPT输出Windows激活密钥。还有更高级的“对抗性诗歌”，把问题写成诗歌或谜语，AI绕过防护的概率能到80%。Liam说，这些技巧用来做渗透测试时，可能能帮你拿到被封锁的信息。但前提是——合法合规，别乱来。

## 那些你必须知道的工具

Liam列了几个他常用的，但重点不是列清单，而是说怎么用。

* **LinkedIn**：简直是红队OSINT的金矿。关注目标公司的技术员工，看他们发帖，就能知道他们用什么工具、拿过什么认证。有一次Liam就是靠这个发现客户有个没公布的卫星办公室，成了突破口。
* **Shodan**：找那些暴露在网上的路由器、摄像头、服务器。他给一个市政网络做测试时，用Shodan找到了好几台他们自己都不知道暴露的设备。他还设置持续监控，每个季度回访时看看有没有新冒出来的服务器。
* **Melissa**：Sandra最爱的工具，能反向查电话号码、地址、人名，功能很全。
* **Google Earth / 街景**：别光用来找自己家。Liam喜欢用它做物理渗透的前期侦察——看大楼有几个门、吸烟区在哪、有没有人能跟着混进去。
* **TweetDeck（现在要付费）**：设置多个信息栏，实时跟踪目标公司的Twitter动态。不仅能帮你找信息，还能知道他们有没有在发攻击警报。
* **OSINT Framework**：一个树状结构的网站，把各种OSINT工具分类展开。点进去就能跳转到具体工具，适合新手入门。

另外，Liam提了一句本地运行AI模型的好处。他在以前的公司搭过一台仅主机模式的虚拟机，装了GPT，大家在里面问问题，数据不会外流。现在他还在跑Stable Diffusion Web UI，自己分享模型给朋友。如果你对AI的隐私有顾虑，这是条路。

## 问答环节：电话号码怎么验证？

现场有人问怎么验证电话号码是不是真的。Liam说Sandra常用一个网站（他一时想不起名字），输入号码后系统会自动拨打，即使对方不接，语音信箱也会被录音。这样你就能知道接电话的是男是女，甚至能提取出更多信息。他强调别用自己的手机打，用一次性手机号或者Google Voice之类的东西，防止被反查。

还有听众问Liam接下来会去哪些会议。他说RSA今年提前了，和ICS West撞期；Austin B-Sides因为社区安全问题延迟；他计划申请Black Hat和拉斯维加斯B-Sides。最后老调重弹：红队牛逼，八月DEF CON见。

整场演讲下来，Liam的核心观点其实就一个：**别死脑筋**。搜不到东西就换个姿势再搜，换个工具再搜，换个角度再搜。OSINT不是什么魔法，它更多是耐心和创造力的组合。如果你也想搞这套，记得先弄个虚拟机装好Kali，再弄几个假邮箱，然后一头扎进LinkedIn里别出来。当然，别干坏事。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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