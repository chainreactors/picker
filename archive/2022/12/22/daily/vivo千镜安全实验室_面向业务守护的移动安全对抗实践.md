---
title: 面向业务守护的移动安全对抗实践
url: https://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247490597&idx=1&sn=01fa0ab5199c773850b3d33cb33a4642&chksm=e9b93a49deceb35f24ccd02b41c92c16494c2be7e8dcadcd26060a094c5dad0c9bf07d592dfa&scene=58&subscene=0#rd
source: vivo千镜安全实验室
date: 2022-12-22
fetch_date: 2025-10-04T02:14:19.982442
---

# 面向业务守护的移动安全对抗实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpDtVDWmHvSIicGKeDIa2xEvicvuK28poK9JtNpwKHG6c71riaKMWpmsynXRIpK6vRHLBZcdjbfX5DUrw/0?wx_fmt=jpeg)

# 面向业务守护的移动安全对抗实践

FTXP

vivo千镜

**一、游戏平台的广告安全对抗**

**1.1**

**背景介绍**

本文中指代的游戏平台，主要是指小游戏，它不同于我们平时玩的手机游戏，它是由前端技术栈进行开发的轻量级游戏，主要特点在于无需下载、即点即玩；集成于操作系统；基于快应用框架。

小游戏生态作为新兴的游戏生态，变现能力和激励政策好，发展迅速， 生态逐步完善，商业规模在持续增长。在开发者竟相投入的环境下，还是存在少量开发者的小游戏存在乱推广告的情况，影响了用户体验。

**1.2**

**广告问题展示**

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQa81oDsWwOCjRkegfQcYSlKSI4h2YTN2buzZE1hd478yNEuJ92Pt0rA/640?wx_fmt=png)

用户体验不好，用户量会下降，也会损害厂商的口碑，这样是一种恶性循环。

下面是几种平台侧获取到的广告违规行为：

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpAZyIsZyMRuPiaTUnGl77ZxVia4XehBibDz68iaLTOF2LibFNiakS4uukSxETr5d7l1QSibYEz9jg4EuputQ/640?wx_fmt=png)

从整个行业来看，平台需要对这部分广告问题进行管控和治理，提升小游戏质量，塑造一个良好的生态。

**1.3**

**案例分析**

平台通过对存在用户反馈以及后台数据异常的小游戏进行解包，然后进行代码分析。

分析小游戏可以从**云控文件，静态代码**两个方面入手。

案例1：Cp通过这些云控参数，在上架的时候规避平台的人工审查。![](https://mmbiz.qpic.cn/mmbiz_gif/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQujlWzvEKBjwQVf7ldGIPn54S5odmJBGbhhdvu47NibqNUjic8U7UBfHA/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQtlRao1IBeaUqAt3b3l5rGyYCictIv1jBlY2Y9JAcBI0oTsDOVn0QWXg/640?wx_fmt=png)

案例2：通过ip定位城市信息，在那个城市屏蔽列表里面的城市就没有广告。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQC6raCAJ03jSMluUHNYCvcAicFibu4wbTeuUC4504GLP7rtFmN5qLxV3g/640?wx_fmt=png)

针对案例的分析，提取出大量的特征，这些特征可以是静态代码特征也可以是动态云控特征，有了特征，就可以做自动化的检测了。

**1.4**

**治理措施：检测与落地**

将**数据异常的小游戏从动态和静态**两个方面进行检测：

**静态检测：**先扫描游戏对应包名列表，然后爬取下载小游戏，在服务器端解压rpk并遍历js，然后针对js文件进行规则的正则匹配，输出违规小游戏列表。同时根据检测的反馈，扩充规则库与优化静态特征。

**动态检测：**扫描游戏对应列表，在端侧拉起小游戏，通过对流量的过滤和抓取，对流量内容进行云控参数的匹配，将匹配结果输出为违规小游戏列表。同时根据动态的反馈，扩大流量特征库与优化云控参数特征。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQ8eBgrOicXKKF8OWffrV1Pfy1Wt1vL32OYY97icC0vwI4D8fPk9sRzxIQ/640?wx_fmt=png)

输出违规小游戏列表，交由业务进行冻结和下架等处理。

从行业侧来说，小游戏的动态广告触发相对容易受到外界因素的干预，所以应更加着重于源码与数据传输层面的违规检测。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQ0Fw5BspFUkTNM8TMqLP0KA6phibgwYjj6pZPDjVY6EkRmlAumdibkCgQ/640?wx_fmt=png)

有了游戏平台的检测环节，那这个环节要从哪儿开始落地呢？

两个方面：**巡检 ；上架**。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQnY051EnQhZNsWOCz2sMpjTeqBzIDn17oTicLBRibDOb18hun8XC8Puxw/640?wx_fmt=png)

由巡检去掉存量的违规小游戏存量，由上架审查去掉增量，这样才能更好地维护小游戏环境，优化用户的游戏体验，从而实现正向循环。

**二、移动应用广告安全对抗**

本文的第二个介绍主题，就是移动应用广告的治理问题，对于这个问题，消费者都深恶痛绝。类似下面两张图，图1中用户正在桌面正常使用手机，突然弹出清理弹窗广告，然后更是弹出了视频广告，大大影响了用户的正常使用体验；图2则是锁屏界面下的广告，这种广告形式也给用户的正常解锁带来困扰。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQrwPibTg08SslbHZ7Wh6J75wjosI3tHaEghGnbtQdwYhrLuKOSQv4erw/640?wx_fmt=png)

**2.1**

**产业链分析**

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQH5Ls4hkDibPQibJN9N3ib2QyGyulKMP0ibu10TAiaPAruEnORibhYq9ibpyCg/640?wx_fmt=png)

流氓广告开发者会注册一堆空壳公司、利用那些公司的名称，进行马甲应用投放；流氓广告cp会通过应用商店上架，三方平台和头部媒体的买量进行投放，触达到用户侧。并且他们自身也会推送同公司，同品类的应用到用户这里。这就常常出现有的老年用户偶然下载了某个这种应用，在应用推送的广告中又点击下载了其他同类应用，以此循环，最后就下载了一屏幕的广告应用。

流氓广告cp不仅仅满足于投放应用后应用内广告的正常收入，因为用户平时也不会总是去打开它们，在不被打开的情况下，还能实现广告推送曝光增长？那就是通过各种方式去进行应用外的弹窗广告，这样即使用户不打开这些应用，他们也能获取到广告的曝光收入。

总之是使用短留策略，获得用户后通过野蛮广告变现实现商业收益闭环

具体的弹窗流程如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQRCMKC0aereF2Q8W3EaS5iafibr2LrQUia5hW4Pib7EnrPwfKMM6VwribFcQ/640?wx_fmt=png)

这种高价值的变现也伴随了大量的对抗因素在里面。其中，**保活**以及**防御绕过**是对抗的重点。

**2.2**

**保活**

常见保活方式分析是需要保活，这是一切体外广告的前提，下图列举了几个常用的保活、拉活手段。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQGZ5MEz1CqPDq3zLQ7OTDkXkp8VqDFMNwzKtDSgb4X406x64iaAEtaeA/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQNjiaRbLgq9lIibCQLL5vMZN9nxCpP2XLkerUkARiaIFHKl8lzrB4d7icZg/640?wx_fmt=png)

在流氓广告应用使用上述手段并不能有效保活后，有开发者另辟蹊径，根据双进程守护的原理加以改进，使用两个进程互相锁住了对方的文件，其中一方的进程死亡会解除自己持有的锁，另一方会立即感知到，这时立刻拉起对方，详细步骤如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQfwGknIPjK6Snf2Xlyhic2icViarNBiaaIXMby5CWXD5PqzHm9t8AguW4Lw/640?wx_fmt=png)

**2.3**

**缺陷利用与防御绕过**

在保活成功以后，下一个容易被攻击的点是系统的防御策略，android系统对于后台的拉起是做了限制的，那么如何绕过这些防御呢？是利用系统缺陷。

### **2.3.1 伪造包名启动**

Android 11 以下，在调用方 Activity 中覆写 getBasePackageName 方法，返回系统白名单包名，则可以通过伪造包名拉起activity；

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQJflXtiaVSNsUDQokQ74gRcNEYr9baRlGrrRQiaz7csGem1IFNRpy78ug/640?wx_fmt=png)

也可以使用Hook Application 中的baseContext将包名伪造从而进行拉起。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQOVvbqM4uIBNbNO0ETLicKMzVjcXFibhl19ceNOic3gMH4ZicMDibjoHrF9A/640?wx_fmt=png)

### **2.3.2 moveTaskToFront启动**

movetask：这种方式不算是直接从后台启动 Activity，而是换了一个思路，在后台启动目标 Activity 之前先将应用切换到前台，然后再启动目标 Activity，如果有必要的话，还可以通过 Activity.moveTaskToBack 方法将之前切换到前台的 Activity 重新移入后台(需要声明android.permission.REORDER\_TASKS 权限)。

启动目标 Activity 之前先判断一下应用是否在后台，判断方法可以借助 ActivityManager.getRunningAppProcesses 方法或者 Application.ActivityLifecycleCallbacks 来监听前后台。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQpnDCWQmx7Rao4tLoIiaVwiaJIF04uWibWORthBLVmVQopGDo7MICDmUaw/640?wx_fmt=png)

### **2.3.3 全屏通知启动**

cp针对滥用谷歌全屏通知能拉起activity的机制进行后台弹窗。具体方式为构造一个调起外弹页的intent，并传入PendingIntent，构造通知，并通过setFullScreenIntent传入PendingIntent ，通过这样的方式来拉起activity，需要权限 android.permission.USE\_FULL\_SCREEN\_INTENT。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQeUowPPyIy5CUBj3KxbUFFHnzfKxG5gHicvbYtzLZHnB5maXOuO0HjEQ/640?wx_fmt=png)

### **2.3.4 伪造输入法拉起**

第一步找到系统默认输入法，模拟拉起的广告页面同样声明输入法设置的intent-filter；

第二步，将输入法的intent包装成PendingIntent,在通过intent.setData(Uri.parse(getPackageName() +"://start"));的方式将原始的intent替换掉；

第三步，发送PendingIntent,因为PendingIntent对象是从输入法获取的，此时恶意app实际上是以输入法的权限和身份发送了这个intent,就可以把FloatActivity拉起来了。问题的原因是PendingIntent中的intent被替换成了拉起广告Activity的intent。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQMdWR43cNwxJWgnr85iaOwLLQQueBsfzMYD48bOonvOAAO0l6jFMSWag/640?wx_fmt=png)

**2.4**

**动态对抗**

既然有缺陷利用，那么利用缺陷进行外弹广告的行为，肯定是厂商需要重点治理的行为，但是常常出现这样的一个情况，在消费者手里的那些弹广告应用，到了厂商的分析人员手里就不弹了，这是怎么回事呢？那涉及新的对抗方向：**动态对抗**。

那些应用为了规避上架审查，自身对于一些特定机制做了检测，检测范围以及对应的识别思路如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQjiaA17squLyrY2tAe6qdXJXGKJGrZj8XY65ic2ibgyn6bu0oSBZa5Kcfw/640?wx_fmt=png)

**2.5**

**对抗能力提升与工具建设**

针对上述的行为，首先从分析人员的分析对抗能力提升做起，主要分为3个方面，如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQDQX5haKTgzuvXCFBYvOH1eBmmy5OCH38XOvkiaY4qoKCENX5UlVnPkw/640?wx_fmt=png)

上面讲到了第三方的分析工具，但需要针对不同的对抗场景，进行工具建设。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQ4AHlhaFpClpeGu1MkohajYSXKTf09DwjedmtOHyecNSXvWlS9fdmYQ/640?wx_fmt=png)

解决了对抗工具问题，就解决了人工分析中对抗的一大重难点。

**2.6**

**建设自动化检测能力**

在人工分析完流氓广告应用后，应当将人工的分析成果赋能到用户体验的保障和商店环境净化，其中的过程就是自动化检测能力的建设。

自动化检测能力的核心，是业务方将可疑的应用通过任务队列批量上传，后端将检测文件反编译java代码，然后将人工分析中的特定特征进行静态引擎检测，然后输出广告的检测结果。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQjXVkicCMhX9sCyKOVB6FLwHGoqrJNfQW8mKhh2h19niaAqdaib3m9N1Vw/640?wx_fmt=png)

通过这样的方式，自动化识别流氓广告应用，从而来净化商店环境，以及对第三方分发的应用进行制约。

**三、总结与趋势**

针对于上述的对抗措施，进行对抗思路总结，如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQKPQLmFAyY7ricQtJoicWHz8AW108QicUsSrd50EIWZZHFB9BGhicHTI2HA/640?wx_fmt=png)

针对流氓广告应用未来的对抗的对抗策略展望如下图：![](https://mmbiz.qpic.cn/mmbiz_gif/n5WtWCY9vpBfWia0eBXvSmtQcrcPJZrbQujlWzvEKBjwQVf7ldGIPn54S5odmJBGbhhdvu47NibqNUjic8U7UBfHA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpAZyIsZyMRuPiaTUnGl77ZxVlV1Zc4yd7vCOiblQydSryN7cPqkNiaK3bbicbkYLDqYnAnnHRdibP5nCMQ/640?wx_fmt=png)

总体来说，伴随着厂商治理力度的加大，对抗趋势是将从事后的对抗转移到事前的对抗，这是一个长期的对抗路程，需要行业内的安全团队提升系统防御，加强风险识别、建设对抗工具，赋能检测能力以及产品机制，从而保障用户体验。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpDtVDWmHvSIicGKeDIa2xEviciaM1W7xRJ6q2SMyPFticNmZ9GHyAJ3yVvbgsslzsdubib6Dh7Y2LWO7Og/640?wx_fmt=png)

**往期回顾**

[iQOO11 国内安卓首发背景音过滤，人声更突显，通话更隐私](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247490534&idx=1&sn=8d8d38e4edd4c86a626c14086628b9a4&chksm=e9b93d8adeceb49c55d88fb40a6e820d2eb426233b993280dd9e52cc8e9888f6295a608a8c25&scene=21#wechat_redirect)

[vivo发布安全白皮书，首次披露完整安全隐私保护体系](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ...