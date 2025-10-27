---
title: 实战 | 某OJ渗透测试记录
url: https://buaq.net/go-141567.html
source: unSafe.sh - 不安全
date: 2022-12-28
fetch_date: 2025-10-04T02:34:50.009738
---

# 实战 | 某OJ渗透测试记录

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/2f66da386d0d10974fcd314326088002.jpg)

实战 | 某OJ渗透测试记录

并没有什么技术含量，纯粹就是玩个黑盒的过程。挺有意思的，所以就写下来了。群里说，他们那有个 OJ 是用 windows 的当然二话不说上来看看咯。开整之前大致想出流程，判
*2022-12-27 16:58:45
Author: [www.secpulse.com(查看原文)](/jump-141567.htm)
阅读量:56
收藏*

---

并没有什么技术含量，纯粹就是玩个黑盒的过程。挺有意思的，所以就写下来了。

群里说，他们那有个 OJ 是用 windows 的

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129318.png)

当然二话不说上来看看咯。

开整之前大致想出流程，

* 判断是否容器
* 判断是否出网

第一因为是用 windows 所以有点希望，就来验证第二个看看。

先找个时间长点的题目

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129319.png)上去提交代码。能用的有 C/C++/G++/JAVA/C# 以及 PASCAL

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129324.png)

试了一下，C/C++ 没有 windows.h，基本的 system 等函数就直接 reset 了。

估计有一些防火墙。

运气好，发现 C# 能执行 api？？？

这下好说了，shellcode 走起。

直接参考这个

> C# 加载 shellcode
>
> https://blog.csdn.net/Jailman/article/details/77574019

提交，运行，之后 cs 上线了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129324.jpeg)

但是 10s 一过就被 k 了。

原本是想找个能自动复制的 shellcode，或者是干脆直接 exe2shellcode 然后编码到代码里提交上去写出

结果提交代码有长度限制，最多 6kb，只能继续在 shellcode 上整活了。

那么继续，我们换个思路。

我们把自己复制一个，然后用 api 把自己运行不就行了？

经过测试之后，发现，CreateProcess 这个 api 可以用，shellExecute 这些倒是被 reset 了。

那么接下来就简单了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-16721293241.png)测试之后发现，只有本体线程上线了。。。复制之后的那个没上线？这就很尴尬。

现在有 3 个猜测

* Temp 文件夹没权限
* CreateProcess 并不能运行
* 本体不是 exe 而是某种动态执行的东西，所以复制本体出去压根不是正确的 PE 文件

总体来说就这三种情况，那么我们该怎么排查呢？

oj 也不是完全黑盒，oj 也是有返回结果的

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129325.png)其中我们只需要关注 `Judge Status`，`Exe.Time`,`Exe.Memory` 这些就行

前两个我们是可以手动控制结果，后面一个 Memory 是判断我们程序是否正确运行。

那么接下来就简单了。我们可以手动一个选择支 (if)，达成某种目标，就给出正确答案，或者超时等等。

我们先判断程序是否复制到了 Temp 文件夹下面，如果复制到了那么就直接 Sleep 到超时。

```
 (File.Exists())
                {
                    System.Threading.Thread.Sleep();
                    ;
                }{;}
```

经过测试之后发现，文件不存在。程序并没有超时，直接 return 了。

继续判断扩展名

```
 filename = System.IO.Path.GetFileName(szPath);
(Path.GetExtension(fileName)==){System.Threading.Thread.Sleep();}
```

发现超时，说明文件确实被编译成 exe 了。

那么既然 temp 目录没有权限，那么我们就直接复制到本地目录不就行了嘛。

经过修改代码之后，提交运行。这次倒是上线了两个。

但是依旧是过了 10s，这两个程序同时掉线了。预测是被 k 了。

这就很奇怪了。

难道 TMD 学 360 还能判断进程链？还是说有什么组策略？

既然这样，我们就换个方法，既然它会 k 进程链，那么我们就注入到不是我们创建的进程不就行了嘛？

经过测试，Process 这个关键字没被拦截，那么 `Process[] processes = Process.GetProcessesByName(processName);` 这个方法应该也不会被拦截，试了一下果不其然。

这 oj 真的有做过滤嘛 emmm，不过能调用 api 本来也就很奇怪了吧。

依旧同样的方法，判断 explorer.exe 是否存在，然后找到它的 pid。

这里要注意点，可能找到的不一定是 guest 用户的 explorer 也许是其他用户的，我们不一定有权限注入。

所以是循环查找。

然后就是远程线程注入。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129328.png)

很好，自信满满，提交运行。

结果：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129329.png)

？？？？

换了 x64/x32 的 shellcode 都不行，msf 的也试过了。全 TMD 都不行。

我本地测试一下也奇怪的奔溃了。但是用 C++ 写的那份却可以运行。怪事。

不得已，只能上 CPP 了，还是 CPP 用的顺手。

不过在此之前只能祈祷这上面能用内联汇编
提交了个

```
#<stdio.h>  main(){__asm{NOP;} ;}
```

上去，发现编译通过了！！！

不就是不能用 `windows.h` 嘛，小事。

之前想过，不能用 windows.h 最大的问题是什么？不能调用 winapi 嘛。

然而懂计算机的都知道，我们只需要知道函数的地址，然后手动 call 不就能调用了嘛。

和这种情况类似的有什么呢？对，就是 shellcode。直接 PEB 或者 SEH 查找 k32.dll 的地址然后再找到 LoadLibrary 和 GetProcAddress 的地址，那么 winapi 不就是随便用了吗？

因为仅仅是不能用 `windows.h`，和我另外一篇 自己动手打造一份熊猫烧香 ，还是有点区别的，至少 strcat 这些简单函数都能用，其他的都好说了。

为了节约代码长度，这次不用上一篇文章的那个方法整结构体了。直接参考

> [Windows 下 Shellcode 编写详解]
> https://xz.aliyun.com/t/2108

中的内联汇编代码，抄出来稍微改改就行

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-16721293291.png)

然后就是定义 api 然后调用

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129332.png)

代码很长后面我就不截图了。有了 API 原理就和 C# 版本的一模一样

一样的注入 explorer.exe，提交，运行。

感天动地，终于上线了。过了一分钟也没被 k。

现在就是判断系统版本，先判断系统版本，systeminfo 是不能用的，tasklist 也不行。因为是 guest 权限不是那些 IIS 权限，所以前段时间我用的很爽的各种土豆都用不了，这土豆是真滴好用。啊废话有点多。

用 C# 随便写一个判断系统版本的丢上去。

这时候确实是 C# 比较舒服。.net 库还是全的，如果是 CPP 整 winapi 还得弄一堆七七八八。

最后结果是 win7。虽然结果是这么写的，但是也有可能是 08 之类的东西。因为上传 shellcode 没被杀，所以确认是没有杀软，直接提交 exp 吧。

有了这个就很简单了，随便找个 1458 丢上去，运气好提权成功。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129333.png)

用 1458 的时候还出了点小意外，详情可以看我博客里面有个 tgchannal。过于丢人就不说了，总之还是换了 8639，提权成功。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129336.png)接下来就是横向了，不过我只是为了日 OJ 而来，剩下的就索然无味了，横向还是日 tw 的 edu 好玩。又没有法律风险，难度也不是很高，他们的 web 一个个都可以是梦回 2008 年代的画风。但是意外的洞却不多，所以又简单的同时也有难度，啊又跑题了。

总之第一步随手看个 `netstat -an`，以及 `arp -a`，查看其他资产，有 mysql 连接，这种主机肯定存在 MySQL 配置，可以用来横向。

第二步当然是我们最爱的 ms17010 啦。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-16721293361.png)emmmm，这管理员真的有在管学校嘛。

剩下的没意思，溜了溜了

**![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194134-1672129339.png)**

**本文作者：[HACK\_Learn](https://www.secpulse.com/archives/newpage/author?author_id=8971)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/194134.html**](https://www.secpulse.com/archives/194134.html)

文章来源: https://www.secpulse.com/archives/194134.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)