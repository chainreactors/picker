---
title: 使用xdbg附加blobrunner进程分析shellcode-自动解密API哈希
url: https://forum.butian.net/share/3685
source: 奇安信攻防社区
date: 2024-08-28
fetch_date: 2025-10-06T18:02:29.852572
---

# 使用xdbg附加blobrunner进程分析shellcode-自动解密API哈希

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

### 使用xdbg附加blobrunner进程分析shellcode-自动解密API哈希

前言
在恶意软件分析过程中，恶意软件经常会在内存中注入一些恶意代码。这些恶意代码或shellcode有可能不是常规的PE文件，无法直接使用xdbg或ida进行分析。这种时候可以使用speakeasy来模拟确认...

前言
==
在恶意软件分析过程中，恶意软件经常会在内存中注入一些恶意代码。这些恶意代码或shellcode有可能不是常规的PE文件，无法直接使用xdbg或ida进行分析。这种时候可以使用speakeasy来模拟确认shellcode的功能，但是在学习过程中“自动化”并不是一个很好的办法，实际上，“自动化”的结果并不是很理想。这篇文章，深入学习一下如何对shellcode进行手动分析。
样本
==
![image-20240807143349556](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-f6374da58aee7673638d2f8f983ee0bbac2bcafc.png)
Malware bazaar 链接：<https://bazaar.abuse.ch/sample/26f9955137d96222533b01d3985c0b1943a7586c167eceeaa4be808373f7dd30/?ref=embeeresearch.io>
使用Ghidra分析
==========
载入shellcode
-----------
![image-20240807144241597](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0dcf07008defc3da7787506698be5af9b314d350.png)
相比于正常的PE文件，shellocde需要我们自己选择架构。
一般的Windows程序，编译器通常选择Visual Studio。但是对于shellcode，只需要确保是x86、32位和little就行了，编译器都可以。
反编译shellcode
------------
这是载入shellcode后的ghidra：
![image-20240807144820600](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8635f8c72dbd8a45a73dc19aa2f9c78469d3e767.png)
由于shellcode没有文件头，Ghidra默认不会反汇编它，我们需要手动进行反汇编。
对第一个字节按`D`或者鼠标右键：
![image-20240807144946844](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-ba3656eca52f83e03f288b0b16acfb074893a642.png)
反汇编之后右侧可能还是空白的，这个时候继续在第一个字节上按 `f` 即定义一个函数：
![image-20240807145243649](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0e877f9ccdbefa9f1c37114924bd605d07499eb3.png)
定位函数调用
------
在shellcode中，是没有函数名称的，因为函数调用都是通过API哈希进行的。
\*\*API哈希\*\*
- API哈希是恶意软件常用于规避检测的一种技术，用于混淆Windows API函数。它使用经过计算的哈希值替代函数名来调用API，从而避免直接暴露API的名字。
![image-20240807145938996](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b3825766070625831b7dffb2f9f13d54ce8f8d4b.png)
进入分析第一个 `FUN\_0000008f`:
![image-20240807150035430](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-08bee271a8fce2a92097e973214b5b87400ced00.png)
有俩个通过API哈希进行的函数调用。这里验证一下，复制下来到google 搜索：
![image-20240807150159024](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-ff5fd3ebeeb7a9e8099f865f2feedd371f2c182c.png)
0x726774c 对应的是`kernel32.dll` 中的`LoadLibraryA`函数
回到Ghidra,查看左侧的汇编代码:
![image-20240807150408103](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-9d430df8947ae57266a8e8c6dcda1de1491bf019.png)
发现了 PUSH + CALL 的组合。通过PUSH将哈希值压入栈中，然后CALL 的EBP负责解析刚刚的hash，从内存中查找与之对应的API函数地址。
这是一个标准的API哈希解析模式,也是\*\*Cobalt Strike 和 Metasploit\*\* 生成的 shellcode 常用的方法,因为它们需要尽可能的保证小而简洁的代码在受害者系统中实现复杂功能。
在API哈希调用的上方还有俩个类似哈希的十六进制数值得留意一下：
![image-20240807151602468](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-abd8d0fdb3d7852bd5f596f69dc0543b9ebf93ac.png)
将其复制下来，使用cyberchef解码：
![image-20240807151628445](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-6a0db9cc5a5b651f622d9f378427c8027ec7ff01.png)
可以发现它是要加载的库 `wininet`
对另一个API哈希也进行搜索
![image-20240807151937900](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-cb61b6c679f21dd36a23e83b9aa83f7d5dffed56.png)
这样，我们就知道了如何通过Ghidra手动解析API哈希了，可以在Ghidra中添加注释方便调试。
xdbg解析API哈希
===========
但是，我们不可能一直用Google搜索的方法来辨别API哈希，有点太蠢了。同时，面对一些定制的恶意软件以及哈希的特点，只需要略微的改动就可以使得Hash发生变化。因此我们应该通过定位寄存器的方式来解析API哈希。
API解析之后自然是要执行的。那么就定位到API解析最后的返回值：
![image-20240807153058129](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-697c01fd3eec2230c10392b328573fbdc129366d.png)
该shellcode的第一个函数`FUN\_00000000`前面大致内容都是解析API哈希的操作，解析的函数在最后执行。
通过图形视图，也可以发现该 JMP EAX是整个函数的结尾：
![image-20240807153426924](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-a9f945307243093fa5e12c046aef61e34800d2f0.png)
blobrunner工具下载
--------------
工具地址：<https://github.com/OALabs/BlobRunner>
BlobRunner 是一款简单的工具，可用于快速调试在恶意软件分析过程中提取的 shellcode。BlobRunner 会为目标文件分配内存，并跳转到分配内存的基址（或偏移量）。
![image-20240807153617882](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-7eab763faa93ce6557e603bf59ae2b5aefa41fac.png)
使用blobrunner加载shellcode
-----------------------
下载下来解压后，放到同一工作台内，打开cmd ：`blobrunner.exe shellcode.bin`
![image-20240807154049673](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-c46fc0668958ce4f181b013659c3c643f666b3b6.png)
可以看到shellcode已经被加载到基地址 0x00500000
接着再将该blobrunner.exe附加到xdbg上就可以了。
![image-20240807154314679](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-9c4b194614587c2baa60ebc16eb9adfe0538d1e2.png)
附加到blobrunner，添加一个断点 00500000
![image-20240807154351801](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b6162e20375bfcec383b084d3981e897f19dfe39.png)
之后可以回到blobrunner并按任何按键来执行代码：
![image-20240807154647442](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8e928bc9cf68ff440c6dd50da449a75d3a3a4ded.png)
![image-20240807154807236](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-20195fbac5269b3d1c7bd23cdd57add934035c2f.png)
如上图，在Ghidra中可以知道地址。所以可以`bp 0x00500000+0x86`
在xdbg中连续按俩次F7进入我们刚刚分析的第一个函数内：
![image-20240807155058269](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-287208678b84146115818ddcc5ea20a3ba984836.png)
在俩个call ebp上设置断点，运行到此处。查看右侧堆栈情况：
![image-20240807155345677](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-dbc5b57c9f7fb03ccaa9f5c17f3804856a928601.png)
可以发现刚刚call ebp的哈希值。
这里继续F9，直接断在了JMP EAX上，查看右侧窗口，发现eax的值被解析出来了：
![image-20240807162249794](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-15d3051b47a67c2bfff10a5af9bd365d5f49da9c.png)
（这里因为乱码换了个xdbg，blobrunner重新启动了，所以地址会有所不同）
继续F9，解析下一个API哈希。
![image-20240807162408562](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-5e8b39d478ac0e334db5c4d128e4cd27493d13cb.png)
`InternetConnectA` 函数为给定站点打开文件传输协议 (FTP) 或 HTTP 会话，因此它需要传入一个参数。再次F9，可以看到程序传入的参数，即C2:
![image-20240807162537951](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-f3966e104997f3eba5b6d18565ea6f88ad6803d5.png)
继续F9,可以解析到其它的API哈希,以及其传入的参数:
![image-20240807162920051](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-7407d07dff24935d47730493eabe520737545ed0.png)
利用条件断点自动解析API哈希
---------------
定位到解密API哈希函数的末尾,即执行函数调用的地方,就可以发现被解析的值。
![image-20240807165621705](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-cc2d1b7563c3fe44e78243b2ce375852f7a94699.png)
在本例中基地址是 0x00ff0000；
![image-20240807165742195](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-149379833a083c16b259cf2534f01a7344268be1.png)
这里CALL ebp可以跟进一下，发现解析API的函数地址就是 0x00ff0006
![image-20240807165848853](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0db0a84da30513eef2a5a513d831cfb6ca0b3196.png)
![image-20240807170028798](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-20920c36fe4fd85d6029f38759dcb7215dfddea1.png)
往下走可以发现包含散列API函数名称的确切位置；至于解析后的函数位置即之前的JMP EAX。
现在我们已知：
- API解析函数的起始地址 ： 0x00ff0006
- 包含散列API函数名称的确切位置 ：\[esp+4\]
- 解码后API函数名称的确切位置：0x00ff0006 + 0x86
需要设置俩个条件断点：
- 在API解析函数起始处 打印Hash值
- 在API解析函数后 打印API名称
如下图所示：
![image-20240807170316857](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-e1afe4fa9a202e94453a5c8aacd7d2e443cd077c.png)
![image-20240807170532815](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-fa91b79691844b2eab59a86680f2507accd5b072.png)
关于条件断点的编写，可以自行查阅。
之后F9运行，查看日志文件，可以发现如下图所示：
Hash：
API：
![image-20240807170507584](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-13877ae00ac6d...