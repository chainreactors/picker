---
title: 一文搞懂windows UAC机制逻辑及提权原理
url: https://forum.butian.net/share/3710
source: 奇安信攻防社区
date: 2024-09-07
fetch_date: 2025-10-06T18:20:01.161148
---

# 一文搞懂windows UAC机制逻辑及提权原理

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 一文搞懂windows UAC机制逻辑及提权原理

* [漏洞分析](https://forum.butian.net/topic/48)

核心内容："一文讲清楚windows UAC核心机制逻辑，总结历史上常见UAC提权方式是如何利用这些逻辑的漏洞来实现提权的，并提出检测思路"

0x01 前言
=======
本文主要内容：
> 1、windows uac机制的流程及原理
>
> 2、windows uac逻辑代码逆向调试分析
>
> 3、windows bypassuac 构造原理以及实践
>
> 4、常见uacme里面bypass方法及检测方式
之前分析一个黑产样本里面内置了一堆Bypasss UAC提权的操作，分析完之后测试发现一些杀软这个行为检测不到，于是准备从windows uac机制底层详细分析下Bypass UAC提权的原理和产生的行为有哪些，以及如何针对这种Bypass UAC 提权行为产生的特征进行关联从而落下来一个检测思路；
0x02 UAC流程
==========
一、判断流程
------
UAC的流程，微软有说明文档，用文字和图大致说了UAC的提权过程中的一些影响因素，我们可以先简单了解下：
参考：`https://learn.microsoft.com/zh-cn/windows/security/application-security/application-control/user-account-control/how-it-works`
运行一个可执行文件之前，调用CreatePrcess之前的相关判断流程图如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-fa65c8a484bb5251939ec57210ff1fa6d4b4dd58.png)
这里面有几个判断点：
### 1、第一个判断点：ActiveX是否安装
简单查了下ActiveX这个东西是一个windows下的用户交互组件，之前基本都是和IE联动是实现一些功能，但是这个东西现在的电脑上基本都没有了，具体分界可以大致参考，微软弃用ie，转Microsoft Edge的时候；引入Microsoft Edge之后windows在默认情况下不再内置ActiveX；所以这里我们默认都是no就行；
### 2、第二个判断点：检查UAC滑块设置
cmd运行msconfig，工具里面有个更改AC设置，这里就是这个UAC滑块，如下图，我们可以看到其分为四个档次；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8f4d2bbd51141f30783ffeb9199e269bd247284d.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-c8ef53bf83c88425ac921ac1c65d6a486acd1d2e.png)
对于四个级别的定义：
```php
始终通知 将：
当程序尝试安装软件或对计算机进行更改时，通知你。
更改 Windows 设置时通知你。
冻结其他任务，直到你做出响应。
如果你经常安装新软件或访问不熟悉的网站，建议这样做。
​
​
仅当程序尝试对我的计算机进行更改时，才会通知我 ：
当程序尝试安装软件或对计算机进行更改时，通知你。
对 Windows 设置进行更改时，不会通知你。
冻结其他任务，直到你做出响应。
如果你不经常安装应用或访问不熟悉的网站，建议这样做。
​
​
仅当程序尝试对我的计算机进行更改时通知我 (不调暗我的桌面) 会：
当程序尝试安装软件或对计算机进行更改时，通知你。
对 Windows 设置进行更改时，不会通知你。
在响应之前，不会冻结其他任务。
不建议这样做。 仅当需要很长时间来调暗计算机上的桌面时，才选择此选项。
​
​
从不通知 (禁用 UAC 提示) 将：
当程序尝试安装软件或更改计算机时，不会通知你。
对 Windows 设置进行更改时，不会通知你。
在响应之前，不会冻结其他任务。
出于安全考虑，不建议这样做。
​
```
我理解其实就是分了三个档，对应图上就是高中低，中等级占了两个，有点区别，选择中高的时候，系统会打开安全桌面，选择中低的时候不会；
如下图是选择中里面的第一个偏高模式的时候，系统打开安全桌面：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-225f5654693c3c59362a55621f0dc1f1a9bc24ed.png)
如下是选择中里面的第二个偏低模式的时候，系统关闭安全桌面：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-593fe90e5e24e10d96ad858f55d2eeda47e61704.png)
从流程中可以看到，低就会直接创建；中的话会去校验一些东西，比如可执行文件的签名、过文件清单、注册表等，就是类似白名单的东西，只不过这个表现形式不一样，如果符合白名单就要可以直接创建，不符合就去下一个判断节点；高就是不会直接创建，都会来到下一个节点判断安全桌面开没；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-00364d20a2606e3f8dea70d658914b48a6d1ce3e.png)
### 3、第三个判断点：安全桌面
这个安全桌面本身就会受UAC滑片影响，除非是特定的修改；直观的用户体验就是，uac弹窗时背景是否时灰色的，灰色就是开始，白色就是没开；
如下图，左边时开了，右边时没开：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-ca70a47c4906e013407afce50714b5c51acd0911.png)
到这我们就了解这个uac的工作机制了，但是不清楚具体过程是怎么个调用实现的，接着我们来看下这个调用过程；
二、UAC进程逆向分析
-----------
调试环境：windows10 19045
笔者之前学习fakePPID技术的时候，接触过一点uac提权的知识，通过fakePPID技术我们可以实现父进程伪造；并且uac就是利用的这一过程，手动设置被提权运行的进程的父进程；
我们不妨想想，平常我们右击已管理员运行某个程序的时候，最后运行完他的父进程都是explorer.exe，他的父进程真的是explorer.exe吗；
如下图，通过process explorer，我们可以看到explorer.exe进程使隶属于g0用户，并且没什么特殊权限，显然不是system权限；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-093b287bbb7b30234546f2a8194bf808dbd75553.png)
然后我们再看下通过右击运行的进程的权限，如下图，我们可以看到相关其相关特权权限已经变成system的了：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-c358cb1a6bdfee9a8ad4d95545f737d70e733753.png)
一个不是system权限，没有对应权限令牌token的进程，凭什么可以创建一个system权限的进程呢，这显然和windows安全权限管控相悖；\*\*所以，当我们以管理员权限运行的时候，这里真正创建对应的应用程序的进程不是explorer.exe，当时学习的时候了解到的是consent.exe这个进程做的\*\*；
\*\*真的是这个进程做的吗，所以这次我们深入的来剖析下；\*\*
这里我们可以先看下现象，sysmon全开，手动右击以管理员身份运行任意可执行文件，查看日志；
如下图（去除模块加载、注册表操作后）：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b61cf1f2a9a8b473b78539054470e4d069e7f23d.png)
按时间顺序我们简单看下；
第一条如下图，就是我们熟悉的consent.exe进程的创建，这里我们注意看其父进程；可以看到父进程是一个通过svchost启动，在netsvcs组的，一个叫Appinfo的服务；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-eb422231f9e46ef83f672f52c6cbc2dcee914b3e.png)
然后就是consent.exe结束：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-115a0428e9c6796a4f8dceb446255153759c95c9.png)
最后应用程序被创建，可以看到父进程换成成explorer.exe；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-4504f627a94810c26482b0e83a39905079d6c517.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8b2f02b468f034469a4aa9e4dfb141187bd1bd42.png)
接着往下，
### 搞清楚两个问题：
第一个问题，谁去创建要提权的进程；
第二个问题，如何去创建要提权的进程；
其实就是流程图中这两部分在哪完成的，如下图
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-52e8986422f38bd7e611a9e2665a279bcc98f78b.png)
#### 1、谁去创建要提权的进程
这里我们直接使用windbg调试explorer.exe，不管怎么说，右击管理员运行这个过程，肯定是先走的replorer.exe 的逻辑，所以在 explorer.exe！`kernelbase!CreateProcessW/A`下个断，以管理员权限运行应用程序（当前uac等级是中等偏上）：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-70bf9e9bdd52b7a3829d624ae1a320958bafe579.png)
直接运行成功，没有断点，说明不是explorer.exe 里面调用CreateProcess来创建被提权的进程；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-ca5c22e935fb8b7ca47fd87b2818f62e46010e60.png)
普通双击运行，断下来了，此时堆栈如下图，这里我们需要往回找，根据栈回溯，肯定有相关判断逻辑，类似判断这个操作是正常运行，还是要提权运行的，也就是createprocess之前是从哪来的；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-1face83013da6d3b5fa656f5e44227c7bcfdc29c.png)
可以看到，最近的是来自一个`windows\_storeage!CinvokeCreateProcessVerb::CallCreateProcess`;
使用ida简单看下windows.storage.dll这个函数：
应该是从这来的：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b5800cc75886cffbd800cb4b6bc0562f5c833f54.png)
看下伪代码逻辑，可以看到调用这个createprocessw之前，是有个判断的，通过SHTestTokenMembership判断之前检查进程的令牌是否是域中管理员组里成员的(这个是uac的一个判断条件，用户在管理员组，提升权限的时候，会起uac)，所以这里我们回到windbg，在这个函数下断点；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-064504e70e59ec6f4593805084df2e11469bc442.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-fd0815d44d6f092c954c4ca1b272fd03715cc6c0.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-181f729b54199ec936a850d1756d9b672bf3f7c0.png)
explorer.exe里面下断点：`windows\_storage!cinvokecreateprocessverb::callcreateprocess`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-23934aeba64e7c6a52b2e02dd19af4795bb03ef7.png)
再以管理员权限运行，这次果然断下来了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-4409a42a01fcaa347f5139e869f86180b3defac0.png)
堆栈和上面一致，
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-86b350dd76adf623f1a61ea7dbbc4bd92698b3ce.png)
进入调试跟踪分析，我们来看下，这个在要uac提权的情况下，这个函数如何走向：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-e13424fb5cd65ec5726bb57971e744612cc38d1b.png)
调试发现，提权运行最后都会来到如下函数AicLaunchAdminProcess，顾名思义启动管理进程；
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8f579addb849c01903bc4880776ef5dce3b62c89.png)
这个函数里面，调用了rpc函数`AicpCreateBindingHandle`，这里有一个uuid，我们可以大致判断，这里可能是尝试通过这个uuid和com组件进行通信,`201ef99a-7fa0-444c-9399-19ba84f12a1a`;
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-e1c8fcc3970d6306aaca7936ce0592df2529e260.png)
通过rpcview，我们看到这个请求的uuid对应的接口是来自svchost的Appinfo服务，就是上面我们找到的那个服务
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b7180a8ba75e7016f40962de38f0c2005ee27ba1.png)
#### 2、如何去创建要提权的进程；
Appinfo这个服务，通过查注册表服...