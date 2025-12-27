---
title: 传统 GDB 多进程调试的缺陷与 Patch 方法的救赎
url: https://forum.butian.net/share/4667
source: 奇安信攻防社区
date: 2025-12-26
fetch_date: 2025-12-27T03:22:56.270206
---

# 传统 GDB 多进程调试的缺陷与 Patch 方法的救赎

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

### 传统 GDB 多进程调试的缺陷与 Patch 方法的救赎

* [硬件与物联网](https://forum.butian.net/topic/51)
* [CTF](https://forum.butian.net/topic/52)

在调试多进程程序（如 Web 服务器及其 CGI 子进程）时，gdb 虽提供 follow-fork-mode 与 detach-on-fork 用于跟踪父子进程，但在实际中因子进程生命周期短、fork 频繁及进程依赖复杂等因素，这些机制常难以捕获目标子进程，甚至影响服务运行。为此，本文介绍一种更稳定的方法：在目标程序入口 patch 一段机器码，使进程启动后进入无限循环等待 gdb --attach；完成附加后再恢复原始指令，从而在多进程环境中获得可控且可靠的调试条件。

引言
==
在使用gdb调试多进程时，通过设置`follow-fork-mode parent/child` ，`detach-on-fork on/off`可能也难以调试目标程序，该文章将介绍使用`patch`方式让被调试程序进入无限循环等待`gdb --attach`附加，附加后修复`patch`为后续调试多进程做准备。
在调试由多进程协同工作的程序（如 Web 服务器及其 CGI 子进程）时，gdb 提供的 `follow-fork-mode` 与 `detach-on-fork` 机制在理论上可用于跟踪父进程或子进程的执行。然而在实际环境中，由于进程生命周期极短、fork 次数频繁以及进程间相互依赖等因素，这些调试模式往往难以捕获目标子进程，甚至会导致服务无法正常运行，无法满足调试需求。
为解决这一问题，本文介绍一种更稳定且可控的方法：通过在目标程序入口 `patch`一段机器码，使其在启动后进入无限循环等待 `gdb --attach` 附加。完成附加后再恢复原始指令，从而为后续多进程环境下的深度调试创造可控条件。
GDB 多进程调试问题
===========
在该系统中，由 Lighttpd 作为父进程负责监听端口并提供 Web 服务。当访问不同的 CGI 接口时，Lighttpd 会派生子进程执行相应的处理程序。由于这些子进程生命周期极短，目标程序在运行后往往瞬间退出，导致难以通过常规方式进行调试。
笔者最初尝试编写一个监控脚本：实时监听进程列表，一旦发现目标 CGI 程序启动，立即使用 `gdb --attach` 进行附加。但实际测试结果表明，这种方式仍然无法达到调试目的——虽然能够成功附加到进程，但附加时子进程几乎已经执行完毕。此时在 gdb 中尝试 `ni` 或继续执行，都会提示程序已经退出。
```js
#!/bin/sh
# 监听进程，输出对应的pid。
while true
do
pid=$(pidof your\_process\_name)
[ -n "$pid" ] &amp;&amp; echo "$pid"
done &amp;
```
```js
/bin/gdbserver-mipsel-15.2 0.0.0.0:1234 /usr/sbin/lighttpd -f /etc/lighttpd/lighttpd.conf &amp;
gdb ./login\_cgi -x set\_gdb.sh
```
\*\*gdb server:\*\*
启动 gdbserver 之后，它会在指定端口进入监听状态，同时输出被调试程序的进程号。如下图所示，gdbserver 成功创建并附加到 `/usr/sbin/lighttpd`，其进程 PID 为 \*\*4694\*\*
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-f5675193ec8f1fbc98030e3d861a012b3b9bd943.png)
\*\*gdb client :\*\*
| | | |
|---|---|---|
| \*\*目标\*\* | \*\*GDB 设置\*\* | \*\*描述\*\* |
| \*\*只调试父进程\*\* | `\*\*set follow-fork-mode parent\*\*``\*\*set detach-on-fork on\*\*` | \*\*GDB 留在父进程，完全不管子进程，让子进程自己跑。\*\* |
| \*\*只调试子进程\*\* | `\*\*set follow-fork-mode child\*\*``\*\*set detach-on-fork on\*\*` | \*\*GDB 切换到子进程，父进程自己跑。标准用法。\*\* |
| \*\*同时调试父和子\\*\\*\*\*（高级）\\*\\* | `\*\*set detach-on-fork off\*\*`\*(\*`\*\*follow-fork-mode\*\*` \*决定哪个先活动)\* | \*\*GDB 控制住两个进程，它们都被暂停。你需要用\*\* `\*\*inferior\*\*` \*\*命令手动切换。\*\* |
```js
set architecture mips
set follow-fork-mode parent
set detach-on-fork off/on
target remote 192.168.88.11:1234
```
### `set follow-fork-mode parent` + `set detach-on-fork on`
如下图所示，在该配置下继续执行程序后，可以看到 Lighttpd 的父进程（PID 4694）很快退出，并立即拉起了一个新的进程（PID 4719）。与此同时，`gdbserver` 也随之退出。
按理说 gdbserver 应一直处于监听状态，但此模式下随着父进程退出而终止，因此在该环境下无法用于实际调试。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-ec70c811b63f9aa70baa28157db6157a77575b3e.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-56fdcd636a0e46b97108a6766f577b054f06e6e8.png)
### `set follow-fork-mode parent` + `set detach-on-fork off`
如下图所示，在这种配置下发生 fork 时，gdb 会捕获并手动切换 inferior。继续运行后，页面与接口服务均无法访问，因此也无法再触发 CGI 子进程。
这是因为 Lighttpd 本身会 fork 多个子进程，而 `detach-on-fork off` 会让 gdb 同时控制所有子进程，导致 Web 服务无法正常运转。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-ef11881a558ac165891df615ea0062550c7b8e58.png)
### `set follow-fork-mode child` + `set detach-on-fork on`
如下图所示，在这种配置下，并在目标 login\\_cgi 程序的入口设置断点后继续运行，gdb 会在 fork 出子进程时尝试跟随子进程，但由于 Lighttpd 在处理请求时会频繁 fork 多个进程，gdb 最终直接退出。
同样，此模式也无法满足在多进程环境中稳定调试子进程的需求。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-aa29f226bad7f24b11004d0a13addd54a6ea0ca3.png)
### `set follow-fork-mode child` + `set detach-on-fork off`
如下图所示，此模式会在 fork 后自动切换到子进程。我们希望能在切换后手动回到父进程，并执行 `c` 继续运行父进程，让 Web 服务恢复正常，再通过访问接口触发新的 `login\\_cgi` 子进程，从而在 `info inferiors` 中看到目标进程。
实际结果是继续执行后 Web 页面及接口依旧无法访问，也无法触发新的 CGI 进程，`info inferiors` 中也未出现我们期待的目标 `login\\_cgi` 程序。
原因是 `detach-on-fork off` 会让 gdb 持续控制所有 fork 出的进程，即使主进程恢复运行，其他被 gdb 停止的关键子进程也会阻塞整个服务流程，因此此方法同样无法使用。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-0878f8c5ba64529b3ca3e24a81641fa2ca55b068.png)
综上，Lighttpd 的 CGI 处理方式导致 fork 出的进程生命周期极短，加上 gdb 自身在 fork 处理上的限制，使得传统的 `follow-fork-mode` + `detach-on-fork` 组合在本场景中几乎无法稳定抓住目标子进程。
因此，有必要采用替代方法，下面便介绍\*\*在目标程序入口处打补丁（patch）让其进入“死循环”，再通过 gdb attach 来进行调试\*\*，以绕开 fork 调试局限。
Patch
=====
在多进程程序中，使用 `follow-fork-mode` 等方式调试子进程有时会比较困难。为了能够稳定地对目标进程进行调试，可以采用一种更“强制性”的方法：通过对可执行文件进行补丁（patch），让程序在入口处进入可控的暂停状态，从而便于使用 `gdb --attach` 进行附加调试，恢复后即可下断点进行调试。
具体做法如下：
1. 将目标程序（如 `login\_cgi`）反编译或反汇编，定位其入口函数，一般为 `\_start` 或对应的初始化函数；
2. 在入口处修改两条机器码，使程序一启动就进入一个无限循环（通常使用 `jmp .` 或 `b .` 这样的指令）；
3. 启动程序，此时它会在入口循环处挂起；
4. 使用 `gdb --attach` 附加到该进程，并在循环位置设置断点；
5. 恢复入口处被修改的原始机器码，让程序继续执行，从而实现对子进程的完整调试控制。
通过这种方式，即使在多进程、fork 派生频繁的场景下，也能稳定抓住子进程的执行现场，实现更精确的动态分析。
以`login\\_cgi`为例（改`0040101C`的原因是mips架构的流水线效应，跳转前下一条指令会优先执行）
将
`.text:00401018 21 80 80 00 .text:0040101C 12 00 40 14`
改为
`.text:00401018 FF FF 00 10 .text:0040101C 00 00 00 00`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-7d2773945520f3b18fc06458e279aca74777e36f.png)
修改机器码并保存后，重新打开可执行文件即可看到伪代码已成功变化为我们预期的无限循环逻辑。至此，就可以将原始程序替换为已完成 patch 的版本，并重新打包运行，用于后续的调试过程。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-7d8e255a16431c637ef83b5643aa3553a1a2c84e.png)
当通过 Web 接口触发对应的 CGI 子程序时，可以看到目标程序在后台按照我们逻辑无限循环，而不再立即退出。此时即可使用 `gdb --attach` 附加到该进程，从而开始对其进行后续调试。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-28f74a4d83d34f94d4eada39e9cf6b08acb90fd1.png)
```js
set architecture mips
set follow-fork-mode parent
set detach-on-fork on
target remote 192.168.88.11:1234
```
gdb连接后我们需要恢复`.text:00401018 .text:0040101C` 处的机器码
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-8d618d18a8642848f4b675b579ac632b87a51011.png)
```js
# 由于是mips小端，所以反着写就行。
set \*(int\*)0x00401018 = 0x00808021
set \*(int\*)0x0040101C = 0x14400012
```
恢复后与修改前做一下对比，能对上就没问题。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/11/attach-d29a61bc2d7cd846d1f5bd71a1fc21ce821b442a.png)
至此，我们已经成功附加到目标子进程，并恢复了被修改的指令。接下来只需在相应的执行位置设置断点，即可继续对该子进程进行正常的断点调试。

* 发表于 2025-12-26 09:43:49
* 阅读 ( 292 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

3 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![all](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/27243)

[all](https://forum.butian.net/people/27243)

3 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![all](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---