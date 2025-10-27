---
title: 我的OSCE3之路——OSED
url: https://red-team.tips/post/oxqLv6NzK/
source: 白袍的小行星
date: 2024-03-14
fetch_date: 2025-10-04T12:07:31.105668
---

# 我的OSCE3之路——OSED

[![](https://red-team.tips/images/avatar.png?v=1754980891100)](https://red-team.tips)

# 白袍的小行星

**Once a hacker, always a hacker!**

[首页](/)
[归档](/archives)
[标签](/tags)
[关于](/post/about)
[友链](/post/friends)

## 我的OSCE3之路——OSED

2024-03-13

8 min read
[# OffSec](https://red-team.tips/tag/omhFdQrox/)

# 前言

`OSED`对应的课程为`EXP-301(Windows User Mode Exploit Development)`，从名字就可以看出，这是一门Windows平台漏洞利用的课程，简单来说就是Windows Pwn.

`EXP-301`的主要内容是Windows下32位的漏洞利用，很多人认为在现在的环境下还教32位有点过时，但这门课并不是进阶课程，而是Pwn的入门课程，所以用32位其实没什么不妥，真正高阶的`Exploit Development`课程应该看`EXP-401`.

官方给的前置技能要求包括：

* 熟悉调试器
* 熟悉32位漏洞利用的基本概念
* 能够熟练编写Python3代码
* 能够基本阅读和理解C代码
* 能够基本阅读和理解基础的汇编代码

# 考试规则

`OSED`考试同样为48小时，同样需要监考和提交报告。考试总共会出现3道题目，其中两道为30分，一道为40分，获得60分即可通过。

考试中不能使用商业工具、AI聊天机器人（chatgpt类），并且必须使用`IDA Free`和`WinDBG`完成逆向调试，不能使用其他的调试或者反编译工具，比如`Ghidra`、`IDA Pro`、`x32dbg`等。这一点很多人不喜欢，因为WinDBG的指令确实反人类，OffSec官方说这样要求是为了保证评分流程的流畅。

可以使用WinDBG的插件或者扩展，但需要在报告里说明其用途；可以使用漏洞利用编写框架，例如`pwntools`、`mona`等。

考试所写的脚本必须是`Python3`的，可以使用`Metasploit`社区版作为辅助。

另外要注意的是，`OSED`考试所需报告的要求也是有变化的，脚本需要单独作为文件而不是放在PDF中。

只要完成其中两个题目就可以通过考试，必须完全解决才能得分，不会给步骤分。

和`OSWE`类似，`OSED`考试同样严禁下载考试文件到本地。除非考试说明特别要求，即使这样也需要在考试结束时删除该文件。

# 备考

`EXP-301`的课程板块相对来说没那么多，主要就是这些：

* WinDbg使用介绍
* 基础堆栈溢出
* SEH溢出
* Egghunters
* Custom Shellcode
* DEP绕过
* ASLR绕过
* 格式化字符串

看了其他人的review以及考试说明，提到题目一般是3个类型：

* 给Crash PoC的DEP Bypass，ROP必须多练，一定掌握熟
* Custome Shellcode，会指定你需要通过哪个函数达成什么效果
* 对逆向能力要求高的压轴题

压轴题都说很难，做出来的人不多，因为不做也能通过考试。

因为就剩最后一门了，所以有点松懈，加上备考中间遇到了春节，最终学习时间其实很少。

输人不输阵，还是约了3月8号的考试，要这么急匆匆考的原因还是，剩下的时间还想再学个OSMR（macOS上的本地提权及绕过操作系统防御机制）或者OSDA（安全分析师路径）的，必须狠狠榨取剩余价值。

根据剩余时间和考试内容的综合考虑，我选择放弃最后的压轴题，目标就是把前两个类型掌握熟练。

`EXP-301`总共有三个challenge，第二个主要考察DEP绕过+ROP，第一个和第三个都需要一些逆向工作。因为时间和工作原因，没来得及做challenge，只能把课程材料多熟悉了几遍。

收集了一些有用的资源，包括review和工具：

* https://red.0xbad53c.com/training-reviews/offensive-security/osed
* https://darkwing.moe/2022/10/07/OSED%E5%8F%97%E9%A8%93%E8%A8%98/
* https://github.com/epi052/osed-scripts
* https://github.com/0xbad53c/osed-tools
* https://github.com/nop-tech/OSED
* https://github.com/nop-tech/code\_caver

还有一些额外的自制小练习，来自`@y4ng`师傅：

**自定义shellcode：**

* CreateProcess执行calc.exe
* WinExec执行calc.exe
* CreateServiceA创建一个服务
* GetUserNameA + MessageboxA 弹出"Hello 用户名"
* GetUserNameW + MessageboxW 弹出"主机名 用户名"

**ROP:**

* github.com/xct/vulnbins
* exploits/50472 10-Strike Network Inventory Explorer
* exploits/17665 D.R. Software Audio Converter 8.1
* exploits/44522 exploits/47411 Easy File Sharing Web Server 7.2
* exploits/46269 Faleemi Desktop Software 1.8
* exploits/50650 vuplayer 2.49
* exploits/43156 VX Search 10.2.14

# 考试

毫不夸张地说，OSED是我目前遇到的最难的OffSec考试。

当天还出现个状况，进入监考平台后我没法看到监考员发的信息，我也发不出去信息，最后靠挂全局代理解决了。

题目要求写的很清楚，要求必须用什么以及不能用什么，另外就是记得提交时每道题只能交一个脚本，如果你有多个脚本就需要合并起来。

第一道是DEP Bypass+ROP题，期间踩坑无数，很多东西现查现学，不断冒出想放弃的念头。还好慢慢进入了状态，最终在考试开始后近30小时解决了它，而第二道自定义shellcode要相对简单一些，大概花了6个小时，做完就开始写报告，也写了5个多小时。

这次的报告也是最长的，写了近70页，把每个步骤和环节都尽量写的详细，然后提前6个小时结束考试并提交了报告，当时已经是凌晨五点，将近20个小时没休息，倒头就睡了。

对于考试，还有一些经验：

* ROP非常重要，练得越多，你的ROP就越熟练，遇到一些限制环境也能找到另外的构造思路
* 常见汇编指令要熟悉，不然想要实现某个功能却不知道用什么指令，那真是没地方哭
* 每种题目要针对性地多练练，常见的坑就能提前踩好
* 做好文档和脚本的管理，考试中我因为用混了没改的脚本导致浪费好长时间
* 有时候仅能用的gadget会有副作用，比如让你的堆栈产生各种变化，要学会怎么消除它们

又是无比漫长的等待，这次等待的感觉已经接近于OSCP的那回，因为看到频道里很多人都是交报告24小时内就结果，整个人就是急急急。

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20240313201643OITgKl1662521809258362.jpg)

还好这次速度也很快，大概在交完报告的第二天晚上就出了结果。当时的我正在和朋友聊天，手机突然传来叮的一声，这是推送软件的声音提醒，只有当考试结果通过时才会响起。

我愣了一下，才反应过来我已经通过了OSED，也就完成了获得OSCE3的最后一项认证。

近10个月的不断学习，我终于获得了`OffSec Certified Expert 3 (OSCE3)`，这一刻真有种如释重负的感觉。突然就想起来刚开始学习OffSec证书时，在某个人的OSCP review里看到的一句话：**这不是短跑，而是一场马拉松。**

# 小结

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/202403132017223wehbQimage.png)

拿到OSCE3的电子证书后，还有一封邮件，是需要确认邮寄纸质证书及纪念币的地址，比较坑的是邮件里的链接点开就302，需要发邮件给他们的order部门处理下。

地址先填英文版的，等到了国内之后再改为中文版方便派送。证书会通过DHL寄送，基本是一批一批发的，最长需要两个月左右的时间，就慢慢等吧。

我的LU订阅还有两个月到期，争取把OSDA和OSMR也拿下，那这次的钱就花的太值辣😁

* [前言](#%E5%89%8D%E8%A8%80)
* [考试规则](#%E8%80%83%E8%AF%95%E8%A7%84%E5%88%99)
* [备考](#%E5%A4%87%E8%80%83)
* [考试](#%E8%80%83%E8%AF%95)
* [小结](#%E5%B0%8F%E7%BB%93)

下一篇

[### 2023年终总结](https://red-team.tips/post/2mrt_3sfo/)

[RSS](https://red-team.tips/atom.xml)