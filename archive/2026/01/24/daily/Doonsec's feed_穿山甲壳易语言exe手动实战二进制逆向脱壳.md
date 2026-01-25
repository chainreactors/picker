---
title: 穿山甲壳易语言exe手动实战二进制逆向脱壳
url: https://mp.weixin.qq.com/s/67rohiB5JeEttblZRobf3w
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:54:35.311363
---

# 穿山甲壳易语言exe手动实战二进制逆向脱壳

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLhjYdArSUUJDgfQa41MKicqU8CxINOowC5InHb6v9Q7AyzSlicsffvEvg/0?wx_fmt=jpeg)

# 穿山甲壳易语言exe手动实战二进制逆向脱壳

原创

secureyang
secureyang

secureyang

![]()

在小说阅读器中沉浸阅读

穿山甲壳易语言exe手动实战二进制逆向脱壳一、确定程序OEP（原始入口点）二、实现Fix-Dump脱壳三、Ghidra反编译

# 穿山甲壳易语言exe手动实战二进制逆向脱壳

去这里下载练习程序GitHub - Maijin/radare2-workshop-2015

我演示的这个程序就不给了哈

## 一、确定程序OEP（原始入口点）

使用OD打开 断肠人exe

![image-20260121142912026](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLpHnrjV3Lkc8ibsK9D1cMOKP8lC7lpWcJrdbdfrp1uzj2ibaChfnO80Tg/640?wx_fmt=png&from=appmsg)

![image-20260121142936020](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLwzXxkLzssNry1qgiaVYv7YuwV7yickjIlcvVrP3q0s6agn36niaJsiavUQ/640?wx_fmt=png&from=appmsg)

此时按下 F8 ，我理解的是相当于初步开始调用 exe 程序

![image-20260121143041271](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLFouOuyzN8IibXITVWlvLohcr7MptglMybPSANib4AruBobH9vlBUnQlA/640?wx_fmt=png&from=appmsg)

我们可以看到寄存器里面上半部分只有 ESP 变成了红色

此时在这里选中ESP之后右键选择在数据窗口中跟随

![image-20260121143152168](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLAYmVPfHS3RciaA62PCREFgSlnDoia2ic345AzOM8DUarBJz65laIgJSPg/640?wx_fmt=png&from=appmsg)

在左下角选择 HEX

![image-20260121143257569](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtL91eNxQJWJkDVLRf3U2uhnwlKWULjVOAF96icI7Hz3U5qhiabvKtvADOQ/640?wx_fmt=png&from=appmsg)

我们可以看到在HEX数据中有好几行，每一行开头第一个就是我们要的 DWORD 字段

> ### 🔍 什么是 DWORD
>
> DWORD 是 **4 个连续字节**组成的 32 位数据，在小端序（x86 平台）下，字节的存储顺序是反向的。
>
> 简单来说，在这个十六进制窗口里，每一行的**前 4 个连续字节**就构成一个 DWORD，你可以按这个规律依次找到所有 DWORD。

然后选中第一个DWORD字段，右键设置硬件访问断点

![image-20260121143512589](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLf8rZfEjZSPfIvK9UO5QpQ7ITySkURQiasWPTGawOmz812EOh7Zqp67Q/640?wx_fmt=png&from=appmsg)

此时断点设置好了之后，直接按下 F9 让程序跑起来，它会自动停在断点的位置

![image-20260121143558882](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLoRwlFa6cn0HbtGGZUqmTuo7ShicEB5wks6EwzXrw32FeX0zgojxlU5Q/640?wx_fmt=png&from=appmsg)

然后一直按 F8 让地址一点一点往下走

> ### OllyDbg 常用调试快捷键（类比 VS Code）
>
> | OllyDbg 快捷键 | 功能描述 | VS Code 对应操作 |
> | --- | --- | --- |
> | **F7** | 单步进入（Step Into），会进入函数内部 | 单步进入（F11） |
> | **F8** | 单步跳过（Step Over），不进入函数，直接执行完当前行 | 单步跳过（F10） |
> | **F9** | 运行 / 继续（Run/Continue），让程序一直跑直到遇到断点 | 继续运行（F5） |
> | **Shift+F7** | 单步跳出（Step Out），从当前函数返回到调用它的地方 | 单步跳出（Shift+F11） |
> | **Alt+F9** | 运行到用户代码，直接跳过系统 DLL 和壳的代码，回到程序自己的代码 | 无直接对应，但效果类似 “运行到光标处” |
> | **Ctrl+F9** | 运行到返回，执行到当前函数的 `ret` 指令处暂停 | 无直接对应 |

一直到看到我们要的 OEP（原始入口点）

![image-20260121143852230](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLDVTJgdLzlicjztZuAbm7rD1ViaOEVuZvsEh3Gaiae8ehllkDAmMfRic5uw/640?wx_fmt=png&from=appmsg)

但此时，其实我们的 EIP 还没有走到这里，怎么快速跳转到 OEP 这里呢？

![image-20260121143946682](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtL150Fre0NCB7MQlm89FWiaHUic6DsHaTYZ6auPRK75rK2icLUmRribB8m8Q/640?wx_fmt=png&from=appmsg)

直接选中，然后右键，点击此处为新 EIP

终于到这里了，选中它，右键选择用 OllyDump 脱壳调试进程

![image-20260121144037274](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLPtH3zlCbib2CQAsBRO1Whd9ZMKUF1AC1ic7h3ibkHEZW7ce4zT8AAG7AQ/640?wx_fmt=png&from=appmsg)

![image-20260121144136980](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLY73JqibJ47dxtrvfpwFqPibGK6VNZiaW02Hh9gCzWcmxRUrF66DrlrQSw/640?wx_fmt=png&from=appmsg)

然后设置一个文件名称就好了。

![image-20260121144223405](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtL6VabAZcSIaHagzBI2wQwSm8l1UVvlicG4GiaVZyX8qmLvJIszS17rgZQ/640?wx_fmt=png&from=appmsg)

这个时候我们就可以看到我们脱下壳之后的exe程序了

![image-20260121144307607](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLBW6DBAxnsfICK0K1I6mkOtL42aF5VY1pqps8N5FHibKRRqhBbH07WgA/640?wx_fmt=png&from=appmsg)

77428801

但是此时打开我们会发现，报错了

![image-20260121144828052](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLpcvaasPz7ESeu4hHQbouw0GhuEsuH2icYt2xeG5SNPLicIfrOsVM77eg/640?wx_fmt=png&from=appmsg)

> 这个报错很常见，说明你脱壳后的程序在导入表修复环节出了问题。
>
> ### 🧐 报错原因
>
> `无法定位程序输入点 NtDllWindowProc_A` 表示：
>
> * 程序在调用系统 API 时找不到正确的入口地址。
> * 这通常是因为 **ImportREC 修复导入表时，错误地保留了 Armadillo 壳的虚假 API 导入**，或者遗漏了原始程序的真实导入表。

## 二、实现Fix-Dump脱壳

所以现在我们需要重新定位 OEP 地址

按下 Alt+M 打开 内存窗口

![image-20260121144947923](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtL3bwTj2DtFXXaZlUH3o9qycac4PTCgPaJlc411ia4ncckI1enTvYicepQ/640?wx_fmt=png&from=appmsg)

找到 属主为程序名称，且区段为 .text 的这个位置，选择 在访问上设置中断

此时前面的地址会变成红色

![image-20260121145121983](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLFAaHvN5ic95G7OU468OFROnKTAnnJGriab59etHK3xiaQqn2zlqC8NTGQ/640?wx_fmt=png&from=appmsg)

此时我们直接按下 F9 让程序跑起来，让它停在这个断点的位置

![image-20260121145218206](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLP9msJbialKuAiaexoHgzMZrtChesbAksxibeV86KrsZFezVgSa9eAFz0w/640?wx_fmt=png&from=appmsg)

看，直接停在了 push ebp mov ebp,esp 的位置，在这个位置重复上面的操作，重新 dump 脱壳

但是发现，此时报了新的错误

![image-20260121151157283](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtL5XcuKjQPQOMtsPeM6VhgGyWnyzo81mibD05Azl7LSqd0GJm4WUichL2Q/640?wx_fmt=png&from=appmsg)

这是什么原因呢？

> 这个报错 `无法定位程序输入点 NtDllWindowProc_A` 很典型，根源是**导入表没有清理干净**。
>
> 我帮你拆解一下原因和解决方法：
>
> ---
>
> ### 🧐 为什么会出现这个错误
>
> * `NtDllWindowProc_A` 不是 Windows 系统的标准 API，它是 **Armadillo 壳留下的虚假导入表项**。
> * 你用 OllyDump 生成的文件里，还残留了壳的导入信息，导致系统加载时找不到这个不存在的函数。
> * 简单来说：脱壳只完成了 “内存转存”，但导入表还没被精准修复。

所以此时需要我们，去清理一下导入表，把脱壳留下的壳的表，清理出去，并修复dump下来

我们需要下载这个工具：Releases · NtQuery/Scylla

我在这里重新使用OD载入并用Alt+M的方法找到OEP地址后，记住这个地址，千万不要关闭OD

![image-20260121151428465](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLgpWnXHribLOkjkmoCLphggdt8cj4HmiaHIiaGiaRara91ftVH3qq9k2zhA/640?wx_fmt=png&from=appmsg)

下载好，我们需要确认，脱下壳的程序的版本，是 64 还是 32，用 exeinfope

![image-20260121151527886](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLEWRmWSkZbQvCg6mCr23kNM0tuouZfgqIQwTa4VBia2apEygA99TdN1g/640?wx_fmt=png&from=appmsg)

这个位置的说明就是：镜像是一个32位bit的可执行程序

所以我们选用 32 位的 Scylla，注意，使用管理员运行程序，否则很多进程他是检索不到的

![image-20260121151643339](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLibicStgTrXBzxX9JTEOmxFibKsQ96bQVjib1WbibMNvdBBNrNlVmpWmvfZA/640?wx_fmt=png&from=appmsg)

点击下拉框，找到OD中正在运行的这个程序

![image-20260121151732415](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtL4pGGTe8JFcLELIOjFEW1qWFAMkzr3zCJ9F8hdvibaNibX87lsOG136wQ/640?wx_fmt=png&from=appmsg)

此时他会自动解析出已经运行到的OEP，

![image-20260121151833035](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLCa82yX9G7xNsSagIDq8xwFOgFgFibnPGLDZkM4ZNWVxhglnyJqN5OIA/640?wx_fmt=png&from=appmsg)

点击 IAT Autosearch

![image-20260121151927445](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLicEI0hu5w2sj9f1RzYicflSh7rowzzljpZwkOsoibicdPTfWzh6FbTLGWg/640?wx_fmt=png&from=appmsg)

它会自动计算出 VA 和 Size 的值，点击确定

![image-20260121151958509](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLjMTm0ywmLXvsrxjYXrWuZNxQC6S3ylSdwVyiclqOEbUv7yoRv2X8loQ/640?wx_fmt=png&from=appmsg)

接下来点击 Get Imports

![image-20260121153127407](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLZb7Va0t17tp1fV18eSzjib2H0jrOnUfoVo99BlbFcEYjOeibM2ol2xjg/640?wx_fmt=png&from=appmsg)

可以看到这里面有这些红色的导入表，这些就是我们需要清理掉的

![image-20260121153207875](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtL4ibt0RWm32IEeOFej6F2stBn9SPYB6fQk4hZQWwrevD1cQcVN8Kpygw/640?wx_fmt=png&from=appmsg)

分别选中，右键 Delete tree node 即可

清理完毕之后，点击Dump，给Dump下来的文件重新命名一下

![image-20260121153242597](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLibibKMweGJFfA95dstJ6NDic1gBqxAzPSS4vUecYkLbDY2PcicF0NlFqgw/640?wx_fmt=png&from=appmsg)

然后再点击 Fix Dump，选择刚刚保存的这个文件

![image-20260121153323162](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLqmJh39VmNibS0T8r3gM5oACnIxMTehCQvrETgAVgSun2mUsUmwWP24Q/640?wx_fmt=png&from=appmsg)

此时，Fix Dump 之后会生成一个新的 SCY 的exe

> Scylla 在执行 `Fix Dump` 时，会自动在原文...