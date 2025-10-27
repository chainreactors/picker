---
title: [原创]2023腾讯游戏安全竞赛决赛题解(安卓)
url: https://buaq.net/go-160018.html
source: unSafe.sh - 不安全
date: 2023-04-23
fetch_date: 2025-10-04T11:31:28.278907
---

# [原创]2023腾讯游戏安全竞赛决赛题解(安卓)

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

![](https://8aqnet.cdn.bcebos.com/730b8520d5c5994d16b4b99cf6fb7d8b.jpg)

[原创]2023腾讯游戏安全竞赛决赛题解(安卓)

决赛在 il2cpp 上的防护以及 anti-debug 上并没有增加难度,而是把重心放在了注册机算法上,所以决赛篇就不重复写 dump 和 anti-
*2023-4-22 20:53:29
Author: [bbs.pediy.com(查看原文)](/jump-160018.htm)
阅读量:36
收藏*

---

决赛在 il2cpp 上的防护以及 anti-debug 上并没有增加难度,而是把重心放在了注册机算法上,所以决赛篇就不重复写 dump 和 anti-debug 部分了

## getflag

在有 dump 的情况下拿 flag 就是洒洒水了,分析我都懒得贴了,上个代码意思一下

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | `function CheatFlag()`  `{`  `var g_libil2cpp_addr` `=` `Module.findBaseAddress(``"libil2cpp.so"``);`  `var coin_cmp` `=` `g_libil2cpp_addr.add(``0x4652ac``);`  `Memory.protect(coin_cmp,` `4``,` `"rwx"``);`  `Memory.writeInt(coin_cmp,` `0x7100001f``);`  `Memory.protect(coin_cmp,` `4``,` `"rx"``);`  `}CheatFlag();` |

## 注册机

il2cpp 中分析过程还是一样的,很容易可以找到验证点,稍微分析就可以知道这里的验证方法是低位与rand比较,高位为0

![](https://bbs.pediy.com/upload/attach/202304/888558_BJ679RQPRV23G76.png)

sec 的 so 里也同样有个加密函数

![](https://bbs.pediy.com/upload/attach/202304/888558_S8TN2PTSQMU9EYR.png)

这次调试出现了一个奇怪的问题(上次打的时候没这个问题,不知道是怎么触发的),跳转 libsec 会到一个只读的段,里面代码完全相同,所以断点下载这里面根本不会断下来

![](https://bbs.pediy.com/upload/attach/202304/888558_HEU675UJC5UHNHK.png)

把这个段删除就好了

![](https://bbs.pediy.com/upload/attach/202304/888558_PAFTZFCW8PD4HD7.png)

分析加密函数 0x94368,像这种函数还是好计算的,不过为了方便也可以直接调试

![](https://bbs.pediy.com/upload/attach/202304/888558_JC9C327SGJXHYFH.png)

可以看到 0x9E93C 函数的参数是输入& 0xFFFF00FFFFFF 的值,也就是拿了输入的这些位

同时下面那个函数 ida 也标出来了是 strcmp,观察参数可以理解 v8 是 0x9E93C 的输出

![](https://bbs.pediy.com/upload/attach/202304/888558_SVSFT7WJB5PZYK8.png)

而函数内第一个用到输入的函数是 0x9f4c4,这个函数很简单就是赋值,那么接下来就是需要针对 v10,也就是需要观察下一个函数 0x9f0a8

这个函数里面有一些混淆但不多,还是调试起来看好一点

![](https://bbs.pediy.com/upload/attach/202304/888558_PVBTZCSQPJNXV6K.png)

先看传进来的参数

![](https://bbs.pediy.com/upload/attach/202304/888558_8R24HNSAJSMFK2W.png)

第一个参数是输入&0xFFFF00FFFFFF,第二个 0x11 也就是 17,在 0x9E93C 中可以看到赋值 17,第三个参数是一串不知道干什么用的二进制,第四个是 0

第一个函数调用完也就是用了 a4 的那个函数,把 1 写到了 a4

第二个函数的参数 v15, ida 分析它是一个 char 数组,原本里面的东西应该是没有清空,执行完第二个函数之后就清空了并且 memcpy 了输入,第三个函数和第二个函数是一样的,所以结果就是把 17 存储到了 v14 的空间处

可以简单的把这俩个函数都归为 copy 的功能

至于后面的,就慢慢 F8,看它执行哪个分支

第一句是比较 (0x11 & 1) == 0,很显然结果是假

![](https://bbs.pediy.com/upload/attach/202304/888558_JTFCGBW9CN52D4G.png)

而后要执行的是这一块,把它暂且叫分支 1

![](https://bbs.pediy.com/upload/attach/202304/888558_RVYZM5AQ7TA8XRK.png)

这里的参数 a4 前面被赋值为1,v15 是 input 的复制,v13 前面还没有用到过

执行完以后 a4 和 v15 没有改变,而 v13 变成了 0x2b67,也就是 v15 的当前值

下一句用到了更改后的 v13,以及不知道用来做什么的二进制入参和没变过的 a4

执行完以后 v13 和 a3 都没有变化, a4 则变成了 0x2b67

似乎这就是复制来复制去,暂时猜不出有效信息

然后程序继续执行,跳到了这个分支,把它暂且叫分支 2

![](https://bbs.pediy.com/upload/attach/202304/888558_Z2789AUEDA4TJCN.png)

第一个函数执行完之后 v13 变成了8,v14 没有变化还是 0x11

第二个函数跟最开始的 copy 是一个函数,也就是把 v13 的 8 赋值给了 v14

第三个函数啥事没干,v14 进去什么样出来就什么样,不过出来的时候 x0 = 0,应该是用于判断走向的

后面又走到这了,把它暂且叫分支 3

![](https://bbs.pediy.com/upload/attach/202304/888558_TR3JPPJQJUHHX58.png)

实际上这个分支的函数就是第一次分支执行的,不过参数不一样,区别就在于 a4 换成了 v15, v15 目前还是 input 的复制

执行完以后 v13 从 8 变成了 0x75bc371,并且 v15 也被这个值覆盖了,看起来 v13 是一个 temp 值,只用于储存中间值

这之后又到 (8 & 1) == 0,这回的结果是真,会执行不同的分支

果然这一次直接执行到了分支 2,之前为假是执行到分支 1 的

![](https://bbs.pediy.com/upload/attach/202304/888558_RB72S5H4V2ZCTSS.png)

这个函数之前把 0x11 变成了 0x8,这回变成了 0x4,可以猜测是除 2,判断结果还是 0

不出意外又执行到了分支 3,这一次 0x75bc371 变成了 0x362594b58b57e1, 好像执行一次,长度就会涨一倍,符合这种运算的应该是平方

|  |  |
| --- | --- |
| 1  2  3  4 | `>>>` `hex``(``0x75bc371``*``0x75bc371``)`  `'0x362594b58b57e1'`  `>>>` `hex``(``0x2b67``*``0x2b67``)`  `'0x75bc371'` |

那这个意思应该明白了

先判断是不是单数次方,是单数就执行分支 1,分支 1 是用最开始赋值的 1 来乘

然后把次方数除 2,如果不为零就执行分支 3 继续乘,乘法的两边是自己,也就是平方

那么 off\_12EC00 是乘,off\_12EC10 是除,off\_12EC18 是判断

还剩下一个用到了入参的 off\_12EC08,猜测是取余,只是因为输入的数太小而没有显示出作用

尝试输入一个大的 input 比如 0xFFFF00FFFFFF

本来这次运算的结果应该是左边 hex 中的内容,执行后右边变小了

![](https://bbs.pediy.com/upload/attach/202304/888558_X2H79AEFDRW5DKF.png)

按照它的读法,a3 是0x28a831a5bf4b902e95318e50c2075259f91094d08d84409e1b76eadfa0865d1278acc90fa7c6cf6acb375,尝试一下

|  |  |
| --- | --- |
| 1  2 | `hex``(``0xfff8081bc7dca7d4e8c54ebc420e2cb73b9dbc3fdc7d4455b2f5b4ef598916bd20fc37f15870001bc8140007f8000001``%``0x28a831a5bf4b902e95318e50c2075259f91094d08d84409e1b76eadfa0865d1278acc90fa7c6cf6acb375``)`  `'0x228c023ea3485a0244b4820c12cc034e874a8afe26cfc87b997c23889da89ed6d7b038236b04f34dc353f'` |

发现结果是对应的

那么最开始所比较的应该是次方后的结果的字符串

果不其然

![](https://bbs.pediy.com/upload/attach/202304/888558_S84QBH5EGKEY4WQ.png)

所以只要知道哪个数的17次方取余这个大数等于另一个大数就可以了

这个问题实际上是 rsa 问题,可以用 yafu 把模数分解乘两个大质数相乘,当时我吃了不会用 yafu 的亏

yafu.ini 配置如下,特别注意 dir 相关配置,我这配置有问题执行不下去,后面快结束了我才回头整的 yafu

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | `B1pm1``=``100000`  `B1pp1``=``20000`  `B1ecm``=``11000`  `rhomax``=``1000`  `threads``=``16`  `pretest_ratio``=``0.25`  `%``ggnfs_dir``=``.\ggnfs``-``bin``\Win32\`  `ggnfs_dir``=``.\ggnfs``-``bin``\`  `%``ecm_path``=``.\gmp``-``ecm\``bin``\x64\Release\ecm.exe`  `%``ecm_path``=``.\ecm\current\ecm`  `tune_info``=`       `Intel(R) Xeon(R) CPU E5``-``4650` `0` `@` `2.70GHz``,LINUX64,``1.73786e``-``05``,``0.200412``,``0.400046``,``0.0987873``,``98.8355``,``2699.98` |

最后运算结果是

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | `NFS elapsed time` `=` `925.8149` `seconds.`  `Total factoring time` `=` `925.8163` `seconds`  `*``*``*``factors found``*``*``*`  `P51` `=` `555183147936225271626794036740589959032732535469347`  `P51` `=` `640704384372038524783151782406101498608483916642951`  `ans` `=` `1` |

顺手上传到 factordb 上了

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19 | `import` `gmpy2`  `q` `=` `640704384372038524783151782406101498608483916642951`  `p` `=` `555183147936225271626794036740589959032732535469347`  `n` `=` `0x28a831a5bf4b902e95318e50c2075259f91094d08d84409e1b76eadfa0865d1278acc90fa7c6cf6acb375`  `c` `=` `0x25f6b048b4f32e3ce9175bb64930f65101a706ae74988a4ec87b4d5ec7feb9223ab782bcf1ec9d7fee750`  `e` `=` `17`  `phi` `=` `(p` `-` `1``)` `*` `(q` `-` `1``)`  `d` `=` `gmpy2.invert(e, phi)`  `m` `=` `pow``(c, d, n)`  `print``(``hex``(m))` |

最终结果是 0x7be300df8b2c

就是说,0x7be300df8b2c 是 input % 0xFFFF00FFFFFF 的结果,还剩下 3 个 byte 在余下的运算之中

回到最初的解密 0x94368, strcmp 下面的是混淆看不懂结构了

我的做法是再每一处跳转做记号,并对被跳转地也做记号,这样就可以清晰看到路径

然后发现对照图来还比较方便

![](https://bbs.pediy.com/upload/attach/202304/888558_8VE7NQBM9KMWDSP.png)

可以看到是先比较 strcmp 的结果,再下一次运行就往 3 走了

4 这里我做了标记,参数是排列好的输入,并且执行完之后改变了输入

![](https://bbs.pediy.com/upload/attach/202304/888558_JUK322XVSSUE58A.png)

5 就是正常的程序自检然后退出

那么重点就在 4 调用的函数 0x99ef4 之中

0x99ef4 虽然后面做了混淆,不过经过调试可以知道到 0x98e50 这个函数就计算完了,后面没有再改变

![](https://bbs.pediy.com/upload/attach/202304/888558_WHGPF4ZECS3SZND.png)

不过这个函数里面混淆的很厉害,什么也看不见,经过调试,可以发现有一处用到了输入,并且更改了输入

![](https://bbs.pediy.com/upload/attach/202304/888558_ZRZR8765SYZ3RA9.png)

而这个函数内部不用说也是混淆的厉害,而且通过多次这个函数会发现这个函数不是一个固定的函数,就是说这里跳转的函数是从函数列表中拿出来的,与此同时 X8 似乎是个记录 index 的寄存器,观察汇编可以看出 X0 也是从内存列表中与 X8 相关取出的,于是乎可以拿到两个列表

另注意,ARM64架构处理器采用48位物理寻址机制,就是说开头 1 字节不要

![](https://bbs.pediy.com/upload/attach/202304/888558_NDDFSXWHQMRA9GP.png)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 | `0``:`  `0x7042D23DB4``,``0x7042D2327C``,``0x7042D10004``,``0x7042D22148``,``0x7042D11A88``,``0x7042D10004``,``0x7042D13AD0``,``0x7042D22148``,``0x7042D13AD0``,``0x7042D17158``,``0x7042D22148``,``0x7042D17E00``,``0x7042D12CC0``,``0x7042CFB1BC``,``0x7042CFB1BC``,``0x7042CFB1BC`  `10``:`  `0x7042CFB1BC``,``0x7042CFB1BC``,``0x7042D27BF4``,``0x7042D11A88``,``0x7042D22148``,``0x7042D10004``,``0x7042D10004``,``0x7042D24E18``,``0x7042D25C50``,``0x7042D2A564``,``0x7042D21BE8``,``0x7042D22148``,``0x7042D21BE8``,``0x7042D2075C``,``0x7042D19B64``,``0x7042D16A78`  `20``:`  `0x7042D11B2C``,``0x7042D2A564``,``0x7042D13420``,``0x7042D10AC...