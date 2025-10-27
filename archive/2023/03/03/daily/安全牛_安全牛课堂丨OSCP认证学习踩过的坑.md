---
title: 安全牛课堂丨OSCP认证学习踩过的坑
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651122441&idx=3&sn=301e66c90a3edd27710f940f9a04f10d&chksm=bd145bda8a63d2ccea0655837a581457e0a9342c1298c6fddd641a144edba665b903c9fe6036&scene=58&subscene=0#rd
source: 安全牛
date: 2023-03-03
fetch_date: 2025-10-04T08:32:57.173089
---

# 安全牛课堂丨OSCP认证学习踩过的坑

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkBFT9SQ5xeRajHYyU50XgZaXbtgRqEPS3ic89wEqN9H7CkicvzWBJ3ibrPQyDjuicx7sSdic4qXmSgYk6A/0?wx_fmt=jpeg)

# 安全牛课堂丨OSCP认证学习踩过的坑

安全牛

OSCP终于拿到证，感觉参加考试备考的日子才过去没有多久，想起了那几个月被“虐待”的日子，我想总结下在课程和考试中的犯的错误！

**计划**

我制定了一个学习计划，计划是学习、练习，然后再学习、练习一些，最后参加机构课程。在我完成课程后不久参加考试并通过。做完计划我就白天工作，晚上学习和练习，同时还要为家人腾出时间。本来想着大约3个半月内就能完成这些，因为我是一名渗透测试人员，我有一定的相关经验，以前我也通过了其他几项认证，可结果告诉我，我错了，太高估自己了。

首先，我的工作和个人生活能挤出学习的时间少之又少，在第4个月份的时候我重新调整了计划。此时我只完成了一些准备任务，还没开始实际的Kali Linux渗透测试课程。直到第6个月，我才支付材料费，所以……

**准备工作**

我很轻松读完了大部分的课程材料，因为我的基础还不错。此外，PWK课程只是一个开始，真正要做的是自己研究，并将其应用于课程所涉及的内容，课程还包括问题和练习。

![](https://mmbiz.qpic.cn/mmbiz_png/m6icpc8EwicOVXjesTorXZibPvJiaibhlwHLELgy4CT6zl4yjItKIUY8WBbwxvnxnYz1xQr9nDYI134NqUXY2WZ0yYg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

然而，我没有完成所有的练习就继续上课了。而且只花了60天的实验时间，不想把其中的一些时间浪费在“家庭作业”上。我想的是尽可能多的时间用在实验室里积累动手经验，为考试做准备。当时学习精力都用在这五台机器上，有任何问题随时求助于PWK论坛和IRC聊天。

在8月下旬，在找到27台实验室机器并只使用了一次Metasploit后，我安排了考试。因为我评估了自己的优势和劣势，并确定我需要在权限升级方面做得更好（尤其是在Linux中），但我已经做了足够的笔记，观看了足够的视频通过应该没问题。！

结果还是错了！

**我的问题**

1、没有对自己的能力和考试难度有清晰的认识，计划做的不符合自己的实际情况

2、总是在没完成上一项学习任务的时候，就匆忙进行下一个学习任务

3、即使发现问题，也没能及时修改学习计划

**考试**

我是工作了一天后进行的考试，下午5点左右开始考试。我在不到3个小时的时间内就完成了第一台靶机，30分钟后又完成了一台靶机，不到4小时得了35分。我稍作休息继续考试，可就从这里开始考试就没这么顺利了。

在接下来的8个小时里，我遇到许多问题弄得极度疲惫，结果我睡了一觉，而就这一觉我睡过头了，醒来时只剩下4个半小时，为了通过考试，我匆匆忙忙的开始操作。

在另一台机器上得到一个shell后，我很快又得到了10分，但我无法理解权限升级。此时还有大约3个小时，我无法在其中任何一台机器上取得任何进展。最后，在还剩一小时的时候，我在25分的机器上找到了突破口，只要提升我的特权………但在Linux机器上这是我最薄弱的地方，当时非常后悔，如果我做了练习并把它们写下来，我会得到62.5分。虽然还不到70分，但听说有人在写了只有60分的详细报告后仍然通过。

结果可想而知，我没通过考试。接下来反思了自己，以及如何在第二次尝试时确保获得及格分数。

![](https://mmbiz.qpic.cn/mmbiz_png/m6icpc8EwicOVXjesTorXZibPvJiaibhlwHLEdI6fh8Hs3422TZVQSr5cZzvloXQIUxuuVPdWr8f6OtBWJFJpTkSQSg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**新计划**

这一次，我没有给自己一个硬性的期限，开始踏下心学习基础知识，重新访问OvertheWire、Hackthisite、Practical Pentest Labs等网站。认真复习BASH脚本、Python和C编程语言等知识，这会在实验室和考试中节省更多的时间。还有我报名了机构的培训课程，跟着老师的节奏学习和复习。

我又从Vulnhub.com等网站下载了几台虚拟机，据说这些虚拟机与PWK实验室类似，接着我又使用Hack the Box，并支付进入VIP实验室的费用，VIP实验室也有几台类似OSCP实验室的机器。

![](https://mmbiz.qpic.cn/mmbiz_png/m6icpc8EwicOVXjesTorXZibPvJiaibhlwHLEVjf5ntWNmBLHqvFu2hdKiceBFI912FUORqJAGCLLFI2vSbFKX6VG3Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

完成了所有类似于PWK实验室机器的机器，我在PWK实验室购买了90天的访问权限，并完成以下操作：

1、完成所有练习并写下来

2、尝试根目录所有实验室机器

3、安排OSCP考试并通过

**学习资料分享：**

1、OSCP认证考试介绍、报告模板解读、关于实验报告解读

2、和你一起熟悉Kali Linux：启动Kali ；工具菜单；Kali 文档；熟悉 Kali；管理系统服务；软件包管理；

3、Linux基础命令学习：BASH环境 ；管道重定向；文本搜索与修改；文本编辑工具；比较文件；管理进程；下载文件 ；

4、常用工具使用方法：NETCAT；SOCAT；Powershell& Powercat；wireshark；tcpdump；

5、BASH脚本知识学习：变量 ；条件语句；布尔逻辑运算；循环语句；函数；练习；

![](https://mmbiz.qpic.cn/mmbiz_jpg/m6icpc8EwicOVXjesTorXZibPvJiaibhlwHLEKl9trcPvibVibOnhjia0swdic303fdAzOjGzwUYkRfFibJgoDauB401Jpeg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

识别上方二维码咨询领取相关资料

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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