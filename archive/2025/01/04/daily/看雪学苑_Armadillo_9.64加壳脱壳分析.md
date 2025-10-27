---
title: Armadillo_9.64加壳脱壳分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588040&idx=1&sn=c401466ae78ba69aa089efcce6117344&chksm=b18c230286fbaa14cee6fc3ae311a6df0915e382932ad14ada113e6aeb3cb07f71303ddd1562&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-04
fetch_date: 2025-10-06T20:10:53.547570
---

# Armadillo_9.64加壳脱壳分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5tm8KF97jJib8p3Z4CBDia5uWAGIta8bXO53MMLhHP5BQOWfvjZf2ZZQg/0?wx_fmt=jpeg)

# Armadillo\_9.64加壳脱壳分析

舒默哦

看雪学苑

```
一

缘由
```

写此帖的原因在于，许多论坛关于 Armadillo 脱壳的讨论往往只讲解脱壳步骤，而不涉及原理。即使有些帖子提到原理，内容也常常遵循安全人员的脱壳经验，这对初学者并不友好。Armadillo 壳属于强壳，但它是一款较老的壳，似乎已经很久没有更新了。之前只找到 9.64 的汉化版，而没有找到更高版本，因此我将分析这个版本。对于初学者，建议准备一个没有任何插件的 x32dbg，先尝试自己进行分析，然后再参考下面的分析过程。

```
二

分析 Armadillo
```

Armadillo\_9.64版本的汉化版界面如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5gwnSsBiaDGHusCUSoNOadYV2oJjNIGvyFicHnicqLnMOTTZ9fOYaBksug/640?wx_fmt=png&from=appmsg)

---

##

## 01 最低保护（最兼容）

### ① IAT表加密

最低保护，只对IAT表进行了加密。可以与源文件对比，找到IAT表的首地址，下硬件写入断点。壳程序会在断点位置写入两次，第二次才是真正填写IAT表的地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5MswXdgBQYgw82q4vCexyaMvEbEkwURzXt3OSb0DZ6pQBNLNga1srBw/640?wx_fmt=png&from=appmsg)

接下来收集IAT表的信息，需要三个要素：

1.函数名称。

2.函数所在的dll地址（也可以称dll句柄）。

3.最后需要回填的地址。

经过多次调试，可以在**add edx,4**这条指令处下断，以收集IAT的信息。当断点停在这里时，eax寄存器中储存的就是IAT地址，函数名称位于堆栈的[esp-8]位置，而DLL句柄则储存在局部变量[ebp-0x2948]中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5xuArE4etUpdEIT6WCmHicbwS3qJW23TNWkTCQGprv6JyXmqk2mse3bQ/640?wx_fmt=png&from=appmsg)

其中，定位dll的地址，需要往前面看，dll地址的关键信息，在以下位置：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5Eo7WicKlNib4YlawaR9VV7kVibXYCFOPVaTjxArqFG15QIeutoTsAX15Q/640?wx_fmt=png&from=appmsg)

### ② 确定OEP入口

通过和源文件对比，来确定OEP的入口，然后在堆栈窗口往回溯，找到转跳到OEP的CALL（如下图），记录下图所选择的特征码(`8B 55 F4 2B 55 DC FF D2 89 45 FC EB 48`)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5Ubp7jFDjYldmU2IxlkLHumTekHK98Iol1tJTdRoW9UBfnqFQp81pzg/640?wx_fmt=png&from=appmsg)

搜索的时机是在`VirtualAlloc`函数下断，当遇到申请大小为**0x200000**时，返回到用户代码并运行到**0x43F756**这个位置。在**0x3EA0000**地址（即刚刚申请的**0x200000**大小的区域）中搜索 OEP 入口的特征码，就能够找到。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5CpW1wXJNo6H17RlTQ535NCltFyMCFx0NmmSG488N1ibb4icibn3J8bibSg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5pwoyGMYKwBhLDFoicJnMbudBWhn4zgyBBTiaEbhrUbXxNHLMJicrBiaRqQ/640?wx_fmt=png&from=appmsg)

### ③ 修复IAT表

IAT表信息的收集，可以写插件来自动完成，通过插件来跟踪和保存收集到的IAT信息，然后运行到OEP后，再回填到IAT表，以完成修复。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5uK294ic9hGGMuYtBL4BJCZeAhqiaRcU3cNFtn2v7MlqeEEjdynOOKeQg/640?wx_fmt=png&from=appmsg)

因为是断点事件，所以插件的回调函数，其类型为断点回调(CB\_BREAKPOINT)。开启跟踪后，收集的IAT信息会被存放到申请的缓存中，程序最终会停在OEP处。此时，查看IAT表，可以看到些地址加密了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5T0Dv6EIppOrgI4RickwP1bscj27UgodLDQqxQHXY2XF48ZfLzbDh35A/640?wx_fmt=png&from=appmsg)

再点击回填IAT，以完成修复：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5CkgnBjKcEyvButukhXFwpIVYC3CNTcIEBOsv6ccLLVciaueC5ibx6pBA/640?wx_fmt=png&from=appmsg)

### ④ 脱壳

此时，可以使用x32dbg自带的插件**Scylla**来完成脱壳。需要注意的是，有些导入表地址是无效的，通过和源文件对比，这些地址是多余的，直接cut掉即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF530ia913XNxYeAMvDrsXibeSKUv90s3iazFvdjsuib0V7f2WltR4lg7vcNQ/640?wx_fmt=png&from=appmsg)

---

##

## 02 仅标准保护

勾选仅标准保护，调试的时候，会依次产生如下异常：

1.0xC0000005异常

```
    push ebp
    mov ebp,esp
    push ecx
    mov dword ptr ss:[ebp-4],0
    mov eax,dword ptr ss:[ebp-4]
    mov byte ptr ds:[eax],0		; eax值为0，执行到这里会造成0xC0000005异常
    mov esp,ebp
    pop ebp
    ret
```

2.0xC0000096异常

```
    push ebp
    mov ebp,esp
    push ecx
    push ebx
    mov byte ptr ss:[ebp-1],0
    mov eax,564D5868
    mov ebx,0
    mov ecx,A
    mov edx,5658
    in eax,dx				;in指令是特权指令，只能在0环使用。执行到这里会造成0xC0000096异常
    cmp ebx,564D5868
    jne 58BD6AA
    mov byte ptr ss:[ebp-1],1
    mov al,byte ptr ss:[ebp-1]
    pop ebx
    mov esp,ebp
    pop ebp
    ret
```

3.0xc000001d异常

```
004667F0 | 55                    | push ebp                                            |
004667F1 | 8BEC                  | mov ebp,esp                                         |
004667F3 | 53                    | push ebx                                            |
004667F4 | B8 2D684600           | mov eax,huffmancoding.46682D                        |
004667F9 | 68 2D684600           | push huffmancoding.46682D                           |
004667FE | 64:FF35 00000000      | push dword ptr fs:[0]                               |
00466805 | 64:8925 00000000      | mov dword ptr fs:[0],esp                            |
0046680C | BB 00000000           | mov ebx,0                                           |
00466811 | B8 01000000           | mov eax,1                                           |
00466816 | 0F                    | ???                                                 |;未知指令，造成了0xc000001d异常
00466817 | 3F                    | aas                                                 |
00466818 | 07                    | pop es                                              |
00466819 | 0B36                  | or esi,dword ptr ds:[esi]                           |
0046681B | 8B0424                | mov eax,dword ptr ss:[esp]                          |
0046681E | 64:A3 00000000        | mov dword ptr fs:[0],eax                            |
00466824 | 83C4 08               | add esp,8                                           |
00466827 | 85DB                  | test ebx,ebx                                        |
00466829 | 74 1A                 | je huffmancoding.466845                             |
0046682B | EB 1C                 | jmp huffmancoding.466849                            |
0046682D | 8B4C24 0C             | mov ecx,dword ptr ss:[esp+C]                        |
00466831 | C781 A4000000 FFFFFFF | mov dword ptr ds:[ecx+A4],FFFFFFFF                  |
0046683B | 8381 B8000000 04      | add dword ptr ds:[ecx+B8],4                         |
00466842 | 33C0                  | xor eax,eax                                         |
00466844 | C3                    | ret                                                 |
```

直接nop掉产生第一个异常的指令（如下图），然后脱壳步骤和最低保护一样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5Oicvcg51X5cVJNAKSyCoIoeM2CIOd9Gf6xvIvicbxSeYsXmGMD8APLag/640?wx_fmt=png&from=appmsg)

---

## 03 标准保护+检测调试器

标准保护加检测调试器，实际上是开启了双进程保护的。可以把仅标准保护的文件和此文件对比着一起调试，很容易发现关键指令**je huffmancoding.44056F**，跳过去就不会执行双进程策略。因此，在跳过去后，其脱壳步骤和仅标准保护一样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5Z5PbU31JVg1pdW5Oibd8poicg9fot0ZOnKRHCr5tlNUuSBbXMBQ4UpDQ/640?wx_fmt=png&from=appmsg)

关于检测调试器，有两个地方进行了相关检查：一个是直接调用**`IsDebuggerPresent`**，另一个是通过**`FS`**寄存器来判断是否存在调试器。然而，调试器的检测也包含在双进程保护策略中。如果前面的检查已经跳过，则无需再进行处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF5pMErK6Q0AsVnS8Fkueic65gy39VQJdGNxK8p0zQ6AHtXLHK9TlVtgKg/640?wx_fmt=png&from=appmsg)

---

## 04 双进程+检测调试器（最高保护）

### ① 分析方法

根据上一节的方法，直接跳过**je huffmancoding.44056F**，无法有效阻止双进程保护的策略，后面会造成异常，导致程序崩溃。通过条件判断的来源，可以确认**0x004F4838**是一个全局变量，似乎是一个用于启用各种保护策略的结构体地址。值得注意的是，这些保护策略的启用或禁用并非简单的true或false，而是经过特定算法处理的开关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF56EjTraFMXRxCNmUyDQkf6tQ4MpKGTbDEoOwW8BUU5Z0YXjb0icgJJsQ/640?wx_fmt=png&from=appmsg)

正确的做法是不要跳过，而是直接分析创建子进程后的调试流程。因为被保护程序的代码是在子进程中运行的。可以逐步调试并跟踪，或在**WaitForDebugEvent**函数处下断，以找到关键函数**sub\_426A50**。该函数可以通过 IDA 进行查看，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HqoESibexDGWPrtDd2WnUF53I0FVKorF7Dt3mFunlNxUacq5AStEta4YC8vO0WBjiblFKicibVptlAsA/640?wx_fmt=png&from=appmsg)

```
sub_426A50函数执行的主要流程：

while(...)
{
    if(WaitForDebugEvent(...)) // 等待调试事件
    {
        EnterCriticalSection(...);	//进入临界区

        switch(...)
        {
            case 1:	// 处理异常事件
            {
                if(异常码 == 0x80000001)
                {
                    ...
                    sub_428370(...) // 代码解密的关键函数
                    ...
                }
                else if(异常码 == 0xC0000005)
                {
                    ...
                }
                else if(异常码 == 0x80000003)
                {
                    ...
                }else{
             ...