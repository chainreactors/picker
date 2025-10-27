---
title: FPGA锁存器与寄存器的笔记 - potatso
url: https://www.cnblogs.com/potatso/p/18987406
source: 博客园 - potatso
date: 2025-07-17
fetch_date: 2025-10-06T23:27:33.330162
---

# FPGA锁存器与寄存器的笔记 - potatso

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

# [FPGA锁存器与寄存器的笔记](https://www.cnblogs.com/potatso/p/18987406 "发布于 2025-07-16 13:58")

# FPGA锁存器与寄存器的笔记

fpga初学者总是搞不清楚锁存器与寄存器，以及延迟赋值的原理。基础原理搞不懂，在编写fpga时候效率会十分低下。在这里我们使用触发器的物理结构去辅助我们理解这几个最常见的概念。

# 触发器的门电路设计

最简单的可以存储1位数据的门电路如图

![image](https://img2024.cnblogs.com/blog/1916047/202507/1916047-20250716135703111-851677299.png)

* 设置data为1后，data信号就可以撤销了。信号在经过第一个A门后变为0。此时Q采样为0。然后该信号再经过B门后又变为1。相当于自身又产生了一个Data信号。这个机制被称为自激机制。
* 同理，设置data为0，那么上面的门电路也会保存该数据。上面的门电路被称为双稳态电路，即可以稳定的存储1，也可以稳定的存储0.

但是上面的电路有一个最大的问题是，在初始化存储数据后是无法修改的。为了解决这个问题，我们可以在Data中插入或门，如下图所示。

![image 1](https://img2024.cnblogs.com/blog/1916047/202507/1916047-20250716135723078-1799274159.png)

此时存储的数据被分为两个信号，分别是Data1和Data2。他们是反向的关系。Or门有一个特性，就是只要结果有1，那么输出就为1。下面我们仿真分析

* Data1为1，data2为0。过程如下
  + A永远都会输出为0。Q采样为0。b or门两个输入都为0，那么b永远都会输出1。
* data1为0，data2为1
  + not b永远都会输出0，nota永远都会输出1。

假如修改数据，从第一种情况修改为第二种情况

* data2被修改为1，not b会输出0，我们发现情况开始变得和第一种情况相反，这样成功修改数据。

如果我们想锁存数据，只需要设置data1和data2都为0即可。

但是切记一点是，两根data信号线不可同时设置为1，否则会陷入亚稳态。所以最终触发器门电路如下图

![image 2](https://img2024.cnblogs.com/blog/1916047/202507/1916047-20250716135734133-469057879.png)

data数据先通过一根非门连接，这样确保了不会同时设置为1。但是这样也有问题，两根信号线又不可能被同时设置为0进入锁存状态。所以在两根信号线中串入两个and门。只要设置enable信号线为0，那么输出均为0，实现锁存状态。在需要修改数据的时候只需要enable设置为1即可。

上面的图被称为带有使能的D触发器。在fpga中推测出的锁存器就是上面的结构。

在FPGA中，大多数都是时钟上边沿触发。那又是如何从锁存器推导到寄存器呢？结构如下图

![image 3](https://img2024.cnblogs.com/blog/1916047/202507/1916047-20250716135742429-23143247.png)

整个数据流向，从锁存器A采样数据，到锁存器B输出数据。在时钟信号中，我们知道先下边沿，再上边沿。

在下边沿中，锁存器A的enable信号为高，此时锁存器A采样数据并输出到锁存器B。但是此时锁存器B的enable信号为低，无法采样。

## 延迟赋值

在时钟边沿时刻，锁存器A的enable信号为0，停止采样。锁存器B的enable信号为高，采样从锁存器A输出的信号。我们可以很自然的联想到，即使设置值，也要等到时钟边沿才能赋值，这其实就是fpga延迟赋值。例如我们在本次时钟周期设置寄存器的值，根据物理结构，需要在下次时钟边沿才能采样。

虽然下次时钟边沿才会采样，但是丝毫不耽误下次时钟边沿的逻辑判断。因为下次时钟边沿期间在设置值的同时，寄存器已经输出我们设置的新值了

# 锁存器与寄存器的要点

在FPGA中，时钟周期可以认为是理想的，不会出现毛刺等现象。但是其他信号FPGA是不保证毛刺现象的。

## 值初始化的原因

例如以在fpga常见的组合信号为例

```
if (sel)
	a = b + c;
```

假如sel信号出现毛刺，也就是因为干扰突然变成1。那么a就会立刻重新采样。这事我们不希望出现的。所以在fpga设计中尽量不要出现锁存器。

在上面的代码中，如果sel不满足，那么下面的a信号就会保持上一次的状态。**在FPGA中，如果未初始化，那么值就要保持上次的状态**。如果a默认有信号，那么该语句会推算出LUT查找表。但是如果没有默认初始化值，那就要使用锁存器保存上次的值。

如果开发者再粗心的使用上一次锁存器的值，会造成很多困扰。

## 组合逻辑与时序逻辑的赋值

为什么system verilog中要是用always\_ff与always\_comb来区分两种？最主要的原因是降低风险，方便编译器去推算。在两段式状态机中，为什么在组合逻辑中使用next\_state，而在时序逻辑中，要使用`state ≤ next_state`

在了解了寄存器的物理结构中我们可以得知，只有在时钟边沿才可以写入数据，否则不可写入。而在组合逻辑电路中没有时钟信号，所以无法写入。

我们告诉编译器，哪个是组合逻辑，哪个是时序逻辑，可以更好分析出存在违反设计规范的情况。

posted @
2025-07-16 13:58
[potatso](https://www.cnblogs.com/potatso)
阅读(57)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)