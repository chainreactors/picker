---
title: FPGA中亚稳态的分析与解决 - potatso
url: https://www.cnblogs.com/potatso/p/18930974
source: 博客园 - potatso
date: 2025-06-17
fetch_date: 2025-10-06T22:54:01.528752
---

# FPGA中亚稳态的分析与解决 - potatso

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [FPGA中亚稳态的分析与解决](https://www.cnblogs.com/potatso/p/18930974 "发布于 2025-06-16 12:39")

在学习 FPGA 的新手入门项目中，**FIFO** 是一个不可错过的经典练手项目。与简单的地址加法器（Addr 加法器）不同，FIFO 更强调对 **FPGA 时序特性** 的深入理解，是学习跨时钟域设计的绝佳实例。

FIFO 的设计不仅能帮助新手掌握基本的硬件描述语言，还能引导我们深入探索 FPGA 中**时序约束**、**同步机制**等重要概念。尤其是在工程实践中，最大的挑战是如何正确解决 **亚稳态问题**，否则 FIFO 的数据传输就可能变得不稳定，导致整体设计失效。

通过实现 FIFO，初学者可以真正理解和应对 FPGA 开发中的时序问题，这对后续设计更复杂的项目有极大的帮助。

# 概念解析

对于很多软件出身的人来讲，认为数字电路中的状态不是3.3v，就是0v。在状态改变的过程中，电压立马从3.3v，跳变到0v。而实际并不是这样的，门电路由mos管组成。mos管的充放电都需要时间。在异步FIFO中，两个不同的时钟频率间互相传递数据，很容易出现采样不及时等情况。表现在电压信号中就是电压信号在0~3.3v中随机震荡很长一段时间，最终会明确信号。在震荡这部分时间，我们称之为亚稳态。顾名思义，就是不稳定状态。

![](https://img2024.cnblogs.com/blog/1916047/202506/1916047-20250616123911466-1621330285.png)

# 解决分析

在很多教科书中讲解，通过两极触发器即可解决亚稳态采样。在这里简单讲一下原因。

mos管的原理是通过形成电容，构建沟道，从而导通电路。在这里有两个重要参数，分别是Vg>Vs和阈值时间，也就是电容形成的时间。

电路进入亚稳态，此时电压信号很难驱动并打开mos管，也就是门电路。对于D触发器来讲值不会变动，依旧输出上一次明确的逻辑信号。解决了亚稳态采样问题。

可能这时候有同学提问，那只需要一个D触发器就可以，为什么还需要两个触发器呢？原因很简单，mos管的Vg>Vs，栅极电压并不会是明确的3.3v，很有可能1.5或2.0V。这时候亚稳态电路恰好达到mos管的阈值电压，并且阴差阳错地达到了mos管充电阈值。此时D触发器会因为亚稳态而采集到不正确的逻辑信号。如果只有一个D触发器，此时就会输出这个错误的逻辑信号，约等于继续传播这个错误的亚稳态，造成FPGA错误。

而如果存在两个D触发器，虽然第一个D触发器因为采集到亚稳态信号而变成错误的逻辑信号，这个时间周期可能已经超过了时钟上边沿的周期，因此第二个D触发器在非时钟上边沿是无法被写入的。这个错误的逻辑信号就会被存储在第一个D触发器中。

根据统计，一般亚稳态顶多在一个周期内就会结束。在下一个时钟上边沿到来之际，第一个D触发器会采样正确的逻辑信号，并修改存储的值，由因亚稳态而采集到的错误逻辑信号修改为正确的逻辑信号。第二个D触发器此时会先接收到这个错误的逻辑信号，紧接着第一个D触发器会把正确的值再传递给第二个D触发器。完成亚稳态的消除工作。如果你为了更保险，基于上面的原理，可以多增加几个触发器，串联即可。

![](https://img2024.cnblogs.com/blog/1916047/202506/1916047-20250616123940351-966466433.png)

posted @
2025-06-16 12:39
[potatso](https://www.cnblogs.com/potatso)
阅读(61)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)