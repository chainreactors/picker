---
title: 公平CFS调度类:SCHED_NORMAL、SCHED_BATCH和SCHED_IDLE
url: https://blog.csdn.net/21cnbao/article/details/144645649
source: 宋宝华
date: 2024-12-23
fetch_date: 2025-10-06T19:36:01.699337
---

# 公平CFS调度类:SCHED_NORMAL、SCHED_BATCH和SCHED_IDLE

# 公平CFS调度类:SCHED\_NORMAL、SCHED\_BATCH和SCHED\_IDLE

原创
已于 2024-12-22 15:38:21 修改
·
2k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

18

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

18
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#linux](https://so.csdn.net/so/search/s.do?q=linux&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#操作系统](https://so.csdn.net/so/search/s.do?q=%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#进程调度](https://so.csdn.net/so/search/s.do?q=%E8%BF%9B%E7%A8%8B%E8%B0%83%E5%BA%A6&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#CFS](https://so.csdn.net/so/search/s.do?q=CFS&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-22 13:47:20 首次发布

公平类的调度算法强调的是一个公平，比如有5个任务，则每个人分享20%的CPU。这是一种人人平等的理想情况，实际情况下，nice值会决定任务的权重，nice值位于[-20, 19]之间，nice越低，权重越高，应该获得更多的CPU。nice意味着与人为善，比如坐地铁看到老人或者儿童就让座，这样就是nice，显然nice值越高，自己能坐到座位的机会越低（优先级越低）；nice值越低，优先级越高。

在内核的Documentation/scheduler/sched-nice-design.rst中实际画了这样一幅图，在Linux内核早期的O(1)算法里，nice值实际改变了任务能获取的时间片的大小：

![图片](https://i-blog.csdnimg.cn/img_convert/4e3274819dcfee9a634e91773173c546.png)

现在Linux的CFS调度类采用的是权重影响任务运行的vruntime虚拟运行时间的概率。

![图片](https://i-blog.csdnimg.cn/img_convert/0e213064751da0b9e358a8c1536342a8.png)

负载权重基准，就是nice=0的任务对应的权重 1024，任务权重的计算公式为：

![图片](https://i-blog.csdnimg.cn/img_convert/2b2e60cd42cd2bf5cc99fedf4eadbaa3.png)

从而得到如下权重表（位于kernel/sched/core.c）：

![图片](https://i-blog.csdnimg.cn/img_convert/f32679f5387d39e0a4007517c93cfe22.png)

CFS采用红黑树（RBTREE）组织调度实体，追求vruntime的公平，每次都跑vruntime最小的调度实体。

下面一个程序创建2个线程，包括主线程在内，3个线程都跑while(1)。

![图片](https://i-blog.csdnimg.cn/img_convert/5fee2e7cf931d53d760034458fa758a2.png)

为了屏蔽负载均衡的影响，我们用taskset把它绑定在CPU0上面跑。

![图片](https://i-blog.csdnimg.cn/img_convert/9a74ddde7aeda85bc43d02deca57c586.png)

用top -H命令看他们的CPU利用率分布，大概是均等的33%：

![图片](https://i-blog.csdnimg.cn/img_convert/3172f0d77c4713c34eee77314d3df7ef.png)

默认情况下，nice都是0。下面我们把4606 线程renice为-1， 把4608线程 renice为1。

![图片](https://i-blog.csdnimg.cn/img_convert/b3dbd055297e9094f35abf8589863e22.png)

特别留意其中renice -1时候的sudo和renice 1的时候没有sudo，这说明想提升优先级（更多索取）是要权限的，想降低优先级（更多自我奉献）是比较随意的。

重新看CPU利用率的情况，基本上4607的CPU利用率没有变，4606由于提升了权重，CPU利用率变成约为4607的1.25倍；而4608则变地更少，4607约是4608的1.25倍。

![图片](https://i-blog.csdnimg.cn/img_convert/cf65be643a03c2d34dd893c259798c5f.png)

CFS的实现依赖于红黑树，试想如果我们用链表而不是红黑树来实现vruntime的排序，插入的开销可能就是O(N)而不是对数复杂度O(log n)。

![图片](https://i-blog.csdnimg.cn/img_convert/311efb538726dbbdc5dce5fc602ae422.png)

CFS内部有3种调度策略：SCHED\_NORMAL、SCHED\_BATCH和SCHED\_IDLE

* SCHED\_NORMAL：常规任务；
* SCHED\_BATCH：非交互的批处理任务；
* SCHED\_IDLE：低优先级任务

那么它们是需要3个分开的红黑树，还是1个红黑树上面放入所有的3种策略的任务呢？答案实际是后者。

为了实现SCHED\_IDLE的所谓“低优先级”，实际上它只要一个很低的权重就可以了，比如：WEIGHT\_IDLEPRIO = 3。

在fair这个sched\_class类的wakeup\_preempt() callback中，SCHED\_IDLE的任务可以被非idle的抢占：

![图片](https://i-blog.csdnimg.cn/img_convert/2b709385cbfb95b8256d265599686f47.png)

另外，check\_preempt\_wakeup\_fair()也进一步阻止了batch和idle任务去抢占normal任务（也并阻止了batch内部多个任务、idle内部多个任务的互相抢占）：

![图片](https://i-blog.csdnimg.cn/img_convert/de786fe4a5ece6fc15925f70bba4e2e5.png)

下面的代码，main里面创建2个线程，加上主线程在内，3个线程都while(1)执行死循环。

三个线程的调度策略和nice值如下：

![图片](https://i-blog.csdnimg.cn/img_convert/52b1c099fe874cc89ab71b9eddbd493b.png)

nice值19的权重等于15，是来自于前面的sched\_prio\_to\_weight表。

![图片](https://i-blog.csdnimg.cn/img_convert/371e3badaf0a6d4bd9339ad9bffffea0.png)

![图片](https://i-blog.csdnimg.cn/img_convert/8659993d823cecbc3ff1afc575d5222c.png)

编译并执行（绑定在一个CPU0上面跑）：

![图片](https://i-blog.csdnimg.cn/img_convert/8a0ddf1631496154eb9a581ba176d5ca.png)

top -H看看3个线程的CPU利用率：

![图片](https://i-blog.csdnimg.cn/img_convert/2af4a1da3812146423382cae68fcbc30.png)

这里明显可以看出，SCHED\_NORMAL并不会阻止SCHED\_BATCH和SCHED\_IDLE的运行，而且由于11697和11698都是权重15，它们的CPU利用率相同（尽管他们的调度策略分别是SCHED\_NORMAL和SCHED\_BATCH），它们的CPU利用率都是权重为3的SCHED\_IDLE策略的11699的5倍。它们这3者主要的区别，主要还是任务醒来时候谁可以抢占谁的问题上（本例中3个线程都是无睡眠的）；其他的，还是按照CFS的权重来跑的。我们也可以用chrt来验证一下3个线程的调度策略：

![图片](https://i-blog.csdnimg.cn/img_convert/62fe2bfbcd7bc108d57a4821e722288c.png)

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/default.jpg!1)

宋宝华](https://blog.csdn.net/21cnbao)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  18

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  18

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  1](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![打赏](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/reward.png)
  打赏

  打赏
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![打赏](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/reward.png)
  打赏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

[*Linux**:* *sched**:* *SCHED*\_*IDLE*](https://mzhan017.blog.csdn.net/article/details/148330919)

[mzhan017的博客](https://blog.csdn.net/qq_36428903)

07-17
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
78

[摘要：*SCHED*\_*IDLE*是*Linux*引入的一种*调度*策略，用于只在系统空闲时运行低优先级任务。它比nice 19的优先级更低，确保任务不会干扰正常系统运行，但仍会适当*调度*以避免死锁。与其他策略（如*SCHED*\_*NORMAL*、*SCHED*\_*BATCH*）相比，*SCHED*\_*IDLE*专为后台任务设计，适合病毒扫描、数据导入等场景。通过chrt或*sched*\_set*sched*uler可设置该策略，其实现避免了优先级反转问题，平衡了系统响应*和*后台任务执行。](https://mzhan017.blog.csdn.net/article/details/148330919)

[*进程*管理(二十二)—*CFS**调度*器](https://blog.csdn.net/u012489236/article/details/122399231)

[奇小葩](https://blog.csdn.net/u012489236)

01-16
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2581

[*进程*管理(十八)—*CFS**调度*器
*CFS*是内核使用的一种*调度*器或*调度类*，它主要负责处理三种*调度*策略：*SCHED*\_*NORMAL*、*SCHED*\_*BATCH**和**SCHED*\_*IDLE*。*调度*器的核心在挑选下一个运行的*进程*时有可能会遍历所有的*调度类*别。实际上系统大多数*进程*通常都是*CFS**调度类*负责处理的，因此为了优化下一个*进程*的挑选*调度*器核心会先判断当前*进程*是否采用了*CFS**调度*策略，若是，则直接调用*CFS*代码来挑选下一个*进程*，若不是或*CFS*代码未能挑选到一个合适的*进程*，则会调用各个*调度类*的挑选函数来寻找一个合适的*进程*。若*CFS*](https://blog.csdn.net/u012489236/article/details/122399231)

1 条评论
您还未登录，请先
登录
后发表或查看评论

[*Linux* *调度*策略 *SCHED*\_OTHER *SCHED*\_FIFO *SCHED*\_RR *SCHED*\_*BATCH* *SCHED*\_*IDLE*](https://devpress.csdn.net/v1/article/detail/114329765)

[luopandeng的专栏](https://blog.csdn.net/luopandeng)

03-03
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3675

[*Linux* *调度*策略的类型大致可以分为 TSS (分时系统）*和*实时系统这两种。一方面．一般的*进程*是通过分时运行的。也就是说．使用 CPU 的时间达到分配给*进程*的时间（时间片）时，就会切换到其他*进程*。这种分时运行的*调度*策略称为 TSS 。另一方面，在实时制约较严格且要求保证实时的处理中，就需要指定静态的执行优先级．并严格按照执行优先级进行*调度*。对这种对应答性有要求的*进程*，可以使用实时*调度*策略。另外，与 TSS *调度*策略的*进程*相比． CPU将优先分配给使用用实时*调度*策略的*进程*。
在 *Linux*中，*进程*..](https://devpress.csdn.net/v1/article/detail/1...