---
title: Visual Basic文件浅析及算法分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458492111&idx=1&sn=184d481e59a05fb56bb1e26268219a6c&chksm=b18eac4586f925531f8203d64f6734e9d5541da6422d1561cecf8072f7b704cba5cd24142571&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-01-13
fetch_date: 2025-10-04T03:45:35.900884
---

# Visual Basic文件浅析及算法分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Epdc4ZGz62v7VsGcBOfibNJ5JTuaLNh99P6BOertPp4ibY52CRs9fKZ46o6ZaOoBYFDib1w3b3PPd8A/0?wx_fmt=jpeg)

# Visual Basic文件浅析及算法分析

顾忧

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HGXJIRb0n0OHImmLILKpctkdsz4Lo0pUEO8sjfvMkBcpC3ZLZlepQSk7ePFh4LiaNa4MRGoIFJxJg/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：顾忧

```
一

Visual Basic文件特征
```

**1.1、 VB专用引擎**

VB文件使用名为MSVBVM60.dll的VB专用引擎。举个VB引擎的例子，显示消息框时，VB代码中要调用MsgBox()函数。其实，VB编辑器真正调用的是MSVBVM60.dll里的rtcMsgBox()函数，在函数内部通过调用user32.dll里的MessageBox()函数来工作。

**1.2 、本地代码与伪代码**

根据使用的编译选项不同，VB文件可以编译为本地代码与伪代码。本地代码使用方便调试器解析的IA-32指令；而伪代码是一个解释器语言，它使用由VB引擎实现虚拟机并可自解析的指令。

**1.3 、事件处理程序**

VB主要用于编写GUI程序。因为VB程序采用Windows操作系统的事件驱动，所以用户代码存在于各个事件处理程序之中。

**1.4、未文档化的结构体**

VB使用的各种信息以结构体形式存在于文件内部。

```
二

查看serial值
```

运行OD，打开abex'crackme #2.exe。执行程序后，首先调用的VB引擎的主函数ThunRTMain()。

EP的地址为00401238。00401238地址处的PSUH指令用来把RT\_MainStruct结构体的地址(00401E14)压入栈。

然后40123D地址处的CALL 00401232指令来调用401232处的指令（跳转到主函数ThunRTMain()）前面压入栈的值作为主函数的参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FRSPuONJHg8OrVZpictUKRDOQOce71dYbzLGlbNjWpRPpfx4GibMzJR2g/640?wx_fmt=png)

先运行abex'crackme #2.exe看看具体体现。可以看到输入错误的数据，会提示Nope,this serial is wrong!这就有捷径了啊。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FqCC9cf9x8DHklqOOfIMt53haYBicNH3UptlcIlV8iaru0Yg3GaN6xfibw/640?wx_fmt=png)

这里本来想要查看字符串的方法需要定位到关键位置，但是我在使用OD下断点，然后运行之后就卡壳（不能进行任何操作，于是放弃这个方法，决定一步一步的调试到指定位置）。卡壳如下，有知道原因的师傅请指导一下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FI1yhD1ictDGuqFc2bDkuQ145jLADnibe0myTZwFibM3wcv0tjV8ZdxgPA/640?wx_fmt=png)

重新调试。直接F8执行00401238 push abexcrac.00401E14 ，可以看到数据已经被压入右下角栈窗口，不要问为什么不F7，因为F7直接进入函数内部，太繁琐了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FdKWCRic0rkAbndBgGphA4bJpXbd2NNnypFpg0W14DPIf0zGdv7rG13A/640?wx_fmt=png)

再F8执行0040123D处的指令，熟悉的窗口再次出现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FkkEgpy58ZZMVnyYnnHVhq6WkE6WhQSANsggdGZWkqlcN2dG0W66o9Q/640?wx_fmt=png)

随便输入一串数字，点击check。如果不下断点就会弹出上面的错误提醒。这里在00403324处下了一个断点，目的是让程序停留在这里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FbEBa3SfGkJmQKtlDxuxUD3uIpG98HiasIF6WhxrLfz41sMrGNiaMlXIQ/640?wx_fmt=png)

那么为什么是停留在这里呢，我们在这个地址后面可以看见一个Yep，this key is right!，再往下面看可以看见，

可以看见Nope，this serial is wrong!。那么可以推断这两个就是输入数据之后弹出的提醒。那么要想二选一，在它们的前面必然会有一个判断语句。向上面看，可以发现两个push指令，可以猜测这就是我们输入的数据。这也是在00403324下断点的原因。接下来执行这两条push指令，执行之前先记录一下右上角寄存器窗口的数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FZHOSeeTFMpnCtzBvpqoyYhU5kcs08EIzBia8a0zJrsYQZ49NjXYLaibQ/640?wx_fmt=png)

然后依次执行两条push指令。

```
push edx
push eax
```

执行之后，从栈窗口可以看见两个熟悉的值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0Fh5AQH6on1qibsicNPxqcBK5MuxkxvgyZlWM7ZqR6L4Jx7tda590K2gZg/640?wx_fmt=png)

执行完后，选中push edx右击选择follow in dump->Implicit stack address。可以看到下方的数据窗口有变化，但是为乱码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FgwHcWnkew2GayuaOzgg156FgFcp2IoR7F3yo9RzN7XvO7nWial71I1A/640?wx_fmt=png)

在数据窗口右击选择Long->Address with ASCII dump转换数据窗口的查看形式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FnNXhR0b8yySCyDrW9FWKDm00RPoibf1h4ibIuZdjSj0Nib5WibyrNEsLeg/640?wx_fmt=png)

然后在数据窗口跳转到EDX的地址处，可以看到两个值，一个是我们前面输入，那另一个就是正确的序列值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FyAGuvicJG8KI3gNy2NzLkjfiatb9lCUR0qEMRCU1opKqOSDjDcF3xp4w/640?wx_fmt=png)

输入D6C9DAC9验证，成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FZRUHGVDmP93mHLs1Qpo33s23VhVb0wL4eRXaNsibgNILvrucDEHicJibA/640?wx_fmt=png)

但是当name的值发送改变后，验证就无法通过。说明serial是以name的值为基础进行变化的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FnbiaQEvX7yr0gtVibLoclfBaE9vhpWqJH1DoeNKH4y4Ffvib7Lj1AuLyQ/640?wx_fmt=png)

```
三

分析生成serial的算法
```

既然输入正确的serial值会弹出Yep，this key is right!字符串提示，那么在字符串出现之前会有一个条件判断语句来决定如何进一下操作。那么可以在Yep，this key is right!字符串的上方代码区域里寻找条件转移的语句。

如图，在403332地址处发现转移语句。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0Fh4s7bqtpYEdp5XMLBgLVJib7tgAP7266ib50ZD4DZvICHPp0PPNv1ywQ/640?wx_fmt=png)

那么可以推测上图中的条件转移代码属于某个函数。这个函数大概就是check按钮的事件处理程序。原因在于点击check按钮后，该函数就会被调用，并且在这个过程中会出现成功/失败的消息框。

接下来，在条件语句的上面继续查看，会发现图中所示的代码。在402ED0处的命令是一个典型的栈帧代码，在开始执行函数时就会形成栈帧。由此得出此处就是函数开始部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0Fd3j1yvNULv8OFr4Iib7VWfrNPYbl7GEmtxUZESJt2fCBiaIep3NubPaA/640?wx_fmt=png)

同时在402ED0上面有一段区域存在着nop指令（00402EC5-00402ECF）。这个区域为VB文件的特性——函数之间存在nop指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FMaSCicaFy1kDL9n1vbZWZfjnicydjKdtg0TRZEgfWIThOkRLeapbKKibA/640?wx_fmt=png)

生成序列码的方法有以下的特点：

1、读取Name字符串

2、启动循环，对字符串进行加密（xor，add，sub等）

在402ED0处下断点进行调试，当调试完00402F98处的call之后，可以看到存储在EBP-0X88（0012F488）处的reverse字符串。

注意：

在VB文件中，字符串使用字符串对象，在OD的默认查看模式下，很难认出实际字符串。要想实现下图的效果需要将OD的Dump窗口更改为Long-Address with ASCII dump模式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0F6XcutjxPdh5RBgib9ylVQmmFiadic7IDNVQR9Mba547BicIsnOB2OnyGRw/640?wx_fmt=png)

加密循环（00403197-004032A0）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FbqAKP5h1B7tBiaIE2GEYecLJK9YWP7onWNjPuibMhvUNa9eGZJfKqKuA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FIQFUOQ5nvgftEwAib24DSgtQ2cHfMsPcC8no7ZyMySqagDWmenbkqnw/640?wx_fmt=png)

加密方法

输入的Name字符串为“reverse”

当执行到004031F6处，从name字符串中获取第一个字符r

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FYmU9ZwKu4KIGPptJQicZFrRhcVKfayBDcdWNj8E7FLEq6xHuA6fwjlw/640?wx_fmt=png)

从004031F0调试到0040323D之后，查看一下栈。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FFpMTMhvzwG74abLbrGLM1rdpbIwflkVEwG2ssAuS0zXW1XKXmp9f7Q/640?wx_fmt=png)

再查看ECX的内存地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FpAd2IEGibEpcVhPzicp3bdgyWtNIqXpicoIv5f4vACpngIkialhy6LnFOw/640?wx_fmt=png)

查看EDX的内存地址，发现name字符串的首字符ASCII值R（十六进制值72转换成十进制值为114，对应的ascii值为r）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FLm8ialpRy68ic6r8ibMSb7ibC0rYmg61X6PsfpqXHcLMaVuESlnWjKpaxQ/640?wx_fmt=png)

执行如下函数，将加密后的值存储到ECX寄存器所指的缓冲区。

```
00403243   .  FF15 AC104000 call dword ptr ds:[<&MSVBVM60.__vbaVarAd>;  msvbvm60.__vbaVarAdd
```

此时的栈内存地址如下。计算结果D6是原值72（"r"）加上密钥64生成的值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FrdjgnwWQfqlWickSiax0zW7zpVgAg4uicGaWkQTiaFPMtuhhhfGtgiavVdQ/640?wx_fmt=png)

下面的框中的代码将数字D6转换成字符串D6。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FSEF1pydDt1ayVw73lt2NIAaWbXVIPtncicOiaFuJJ1Gr4EVfpsM0y2QQ/640?wx_fmt=png)

下面代码将生成的字符串连接起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0F1Zd6mMA16L1HeNcFAWlBxGS4zhh5tpgUIiaS5aUnRgZE6DenibNoZsxQ/640?wx_fmt=png)

循环，生成最终的序列号。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FsRwNy6ZRgavP9jgc5VO88RqpzC4ATvyUpCicwnnAzq3ibic1a6ShhSjbA/640?wx_fmt=png)

```
四

整理加密方法以及脚本实现
```

加密方法整理如下：

1、从输入的name字符串中读取前四个字符。

2、将读取的字符一一转换成数字。

3、变换后的数字加64。

4、再将与密钥64相加的数字转换成字符。

5、连接变换的字符。

java脚本如下：

```
public class Decrypt {    public static void main(String[] args){        String str = "orange";        for(int i = 0;i<4;i++){             int s = str.charAt(i)-0;            s = s+100;            String hex_str = Integer.toHexString(s);            hex_str = hex_str.toUpperCase();            System.out.println(hex_str);        }    }
```

结果为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FiajIKZ3TiaTJDPqmEDwXG0eDUJiaKbhMFRGeLh8yEL0IWIiaJGnnFt8ndQ/640?wx_fmt=png)

验证成功：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0F5GMzuyEg2m7R3icBU9VgaEgelFGquvs0DLcNAfGua78pJRhcaz42osA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EmAdI8xmmSRTFCE74vicZ0FMcX3h3nEYkDrA6DrzY1a8iapjGq7dhDicmF5B46HLYWQpfclk1IR906A/640?wx_fmt=jpeg)

**看雪ID：顾忧**

https://bbs.kanxue.com/user-home-890008.htm

\*本文由看雪论坛 顾忧 原创，转载请注明来自看雪社区

[!...