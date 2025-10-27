---
title: stack canary泄露方法
url: https://blog.csdn.net/winsunxu/article/details/128897046
source: 深度技术安全
date: 2023-02-07
fetch_date: 2025-10-04T05:49:25.146582
---

# stack canary泄露方法

# stack canary泄露方法

最新推荐文章于 2025-03-18 23:25:40 发布

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
最新推荐文章于 2025-03-18 23:25:40 发布
·
682 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

0

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

1
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-NC-SA](http://creativecommons.org/licenses/by-nc-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#漏洞利用](https://so.csdn.net/so/search/s.do?q=%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#pwn](https://so.csdn.net/so/search/s.do?q=pwn&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#canary](https://so.csdn.net/so/search/s.do?q=canary&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文详细介绍了栈 Canary 的概念，一种用于防止栈溢出的安全机制。通过分析漏洞程序 `vuln.c`，揭示了 Canary 保护如何在函数调用期间启用，并探讨了两种绕过 Canary 保护的方案，特别是利用 `printf` 函数泄露 Canary 值的方法。文章还讨论了 canary 的偏移计算和其在函数栈地址空间的位置。

## 什么是canary

security cookies，Assume that at the beginning of a function call (e.g. during its [prologue](https://en.wikipedia.org/wiki/Function_prologue_and_epilogue#:~:text=In%20assembly%20language%20programming%2C%20the,for%20use%20within%20the%20function.)) we are saving a value in the function’s stack frame, we would expect (! if everything went well !) to read the same value just before the function exits or namely at its epilogue. If the value has changed, then the execution of the program will be terminated and an error message will be displayed. [1]

Obviously, this protection mechanism is added by the compiler during the compilation process. For the

GNU Compiler Collection (gcc), it is implemented via the StackGuard extension which was added to gcc 2.7.2.2 [1]

[Bypass stack canary](https://artik.blue/reversing-radare-23)

## 漏洞程序 vuln.c

![](https://csdnimg.cn/release/blogv2/dist/pc/img/lock.png)最低0.47元/天 解锁文章

200万优质内容无限畅学

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newBlack.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/f8402e4ea45942fba4bc0eb4a51c8d70_winsunxu.jpg!1)

winsunxu](https://blog.csdn.net/winsunxu)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-dark.png)

  0

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-dark.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-dark.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  1

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseBlack.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment-dark.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share-dark.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![打赏](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/reward-dark.png)
  打赏

  打赏
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more-dark.png)

  ![打赏](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/reward-dark.png)
  打赏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report-dark.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report-dark.png)
  举报

专栏目录

[*stack* *canary*绕过思路](https://blog.csdn.net/sea_time/article/details/103317323)

[sea\_time的博客](https://blog.csdn.net/sea_time)

11-29
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountBlack.png)
2182

[*canary*
简介：
我们知道，通常栈溢出的*利用*方式是通过溢出存在于栈上的局部变量，从而让多出来的数据覆盖ebp、eip等，从而达到劫持控制流的目的。然而*stack* *canary*这一技术的应用使得这种*利用*手段变得难以实现。*canary*的意思是金丝雀，来源于英国矿井工人用来探查井下气体是否有毒的金丝雀笼子。工人们每次下井都会带上一只金丝雀如果井下的气体有毒，金丝雀由于对毒性敏感就会停止鸣叫甚至死亡，...](https://blog.csdn.net/sea_time/article/details/103317323)

[DEP、*Stack* *Canary*介绍

最新发布](https://blog.csdn.net/zppzzl/article/details/149228427)

07-09
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountBlack.png)
786

[简单介绍DEP *Stack* *Canary*](https://blog.csdn.net/zppzzl/article/details/149228427)

参与评论
您还未登录，请先
登录
后发表或查看评论

[Leak*Canary*直面项目中的内存*泄露*](https://donkor.blog.csdn.net/article/details/54095110)

[Sahara\_Savage](https://blog.csdn.net/donkor_)

01-05
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountBlack.png)
3856

[转载请标明出处：http://blog.csdn.net/donkor\_/article/details/54095110
前言：
Leak*Canary*一个直白的展示Android中内存*泄露*的工具。它是Square公司开源出来的内存*泄露*自动探测神器，能够在程序发生内存泄漏的时候在通知栏提示通知，而且学习成本巨低。通过学习本文，了解和如何使用Leak*Canary*工具，同时了解和解决实际开发中出现...](https://donkor.blog.csdn.net/article/details/54095110)

[*Canary*学习（*泄露**Canary*）](https://devpress.csdn.net/v1/article/detail/104115114)

[至臻求学，胸怀云月](https://blog.csdn.net/AcSuccess)

01-30
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountBlack.png)
6320

[*canary*
原理
通常栈溢出的*利用*方式是通过溢出存在于栈上的局部变量，从而让多出来的数据覆盖ebp，eip等，从而达到劫持控制流的目的。栈溢出保护是一种缓冲区溢出攻击缓解手段，当函数存在缓冲区溢出攻击*漏洞*时，攻击者可以覆盖栈上的返回地址让shellcode执行。
当启用栈保护时，函数开始执行的时候会先往栈底插入cookie信息，如果不合法就停止程序运行（栈溢出发生）。攻击者在覆盖返回地址的时候...](https://devpress.csdn.net/v1/article/detail/104115114)

[*Canary*机制及绕过策略-格式化字符串*漏洞**泄露**Canary*](https://download.csdn.net/download/weixin_38650842/14942022)

01-27

[*Canary*主要用于防护栈溢出攻击。我们知道，在32位系统上，对于栈溢出*漏洞*，攻击者通常是通过溢出栈缓冲区，覆盖栈上保存的函数返回地址来达到劫持程序执行流的目的。
*Stack**canary*保护机制在刚进入函数时，在栈上放置一个标志*canary*，然后在函数结束时，判断该标志是否被改变，如果被改变，则表示有攻击行为发生。
一，实验源码
文件名：*Canary*.c
命令](https://download.csdn.net/download/weixin_38650842/14942022)

[绕过*Canary*与*Canary*的*泄露*](https://blog.csdn.net/ConlinderFeng/article/details/111626012)

[Sakura给爷pwn全场](https://blog.csdn.net/ConlinderFeng)

12-24
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountBlack.png)
343

[*Canary*学习（*泄露**Canary*）：
https://blog.csdn.net/acsuccess/article/details/104115114
*泄露**canary*：
https://blog.csdn.net/qq\_38204481/article/details/81076850](https://blog.csdn.net/ConlinderFeng/article/details/111626012)

[*泄露**Canary*的正确姿势](https://blog.csdn.net/ConlinderFeng/article/details/113006228)

[Sakura给爷pwn全场](https://blog.csdn.net/ConlinderFeng)

01-22
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountBlack.png)
367

[*Canary*学习（*泄露**Canary*）：https://www.icode9.com/content-4-626619.html](https://blog.csdn.net/ConlinderFeng/article/details/113006228)

[栈溢出之*canary**泄露*与绕过“新*方法*” .pdf](https://download.csdn.net/download/testvaevv/21951159)

09-05

[*Canary*，又称为*Stack* Guard或*Stack* Smashing Protector，是一种防止栈溢出攻击的技术。当启用*Canary*时，系统会在函数调用的栈帧中插入一个随机生成的Cookie（或称*Canary* Value），这个值在函数执行期间会被保存。在...](https://download.csdn.net/download/testvaevv/21951159)

[*PWN*——格式化字符串*泄露**canary*](https://blog.csdn.net/djhtdjdywgjc/article/details/127936870)

[djhtdjdywgjc的博客](https://blog.csdn.net/djhtdjdywgjc)

11-19
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountBlack.png)
2027

[格式化字符串*泄露**canary*](https://blog.csdn.net/djhtdjdywgjc/article/details/127936870)

[反思：*泄露**canary*之后一定要记得处理掉多余的东西————[2021 鹤城杯]littleof](https://blog.csdn.net/m0_73858054/article/details/136354942)

[m0\_73858054的博客](https://blog.csdn.net/m0_73858054)

02-28
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountBlack.png)
892

[这是一道libc类型的题目，应该是不难的，月余之前遇到。当时思路什么的都理清楚了，脚...