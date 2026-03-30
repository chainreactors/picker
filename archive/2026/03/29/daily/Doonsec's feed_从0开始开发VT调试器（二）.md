---
title: 从0开始开发VT调试器（二）
url: https://mp.weixin.qq.com/s/tOxXZxIxMGzUEZoAPwV7FQ
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:44:05.119958
---

# 从0开始开发VT调试器（二）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1woCcbOsjVMibibrOSsUtzveEVPqLUfIcianbnOmcN0u6ibtibosKboYHmEDdrZazMib50zibzNZtBFacfF7rzUnq1gly9Tp4S0aMwickn1ggx9H7VQ/0?wx_fmt=jpeg)

# 从0开始开发VT调试器（二）

原创

CrazyHarb
CrazyHarb

冲鸭安全

![]()

在小说阅读器中沉浸阅读

从0开始开发VT调试器（二）

背景：

上一章中，我们完成了基础的VT环境搭建，我们已经可以从guest中拦截一些简单的指令跳转到host了，本期我们加快速度将对调试链路进行进一步编写

原理：

在Ring3层，我们经常会用到各种调试工具，例如vs、x64dbg等，他们的单步原理基本上就是两种异常——#DB、#BP，这两种异常在触发时（其实所有异常都会这么走），会触发IDT表中的1号中断和3号中断，中断触发后，会先触发调试器，也就是windbg、x64dbg等(First Chance); 如果调试器未处理，会自动分发到触发异常的进程的ntdll的RtlDispatchException，最后如果进程没有处理，会再次触发Ring3调试器

我们简单画一下异常处理的流程图，即：

![](https://mmbiz.qpic.cn/mmbiz_jpg/1woCcbOsjVOPUU44ick5v8kibHnN6XE7DGniacggrxnrvocp4Obr6oCSsyibfXpsmGyewYjibYbicJmHWadoib4UWt63icTgHpHrCJj2Lyg4byAZsJo/640?wx_fmt=jpeg)

VT下的异常流程:

通过原理已知在Ring3进程触发异常时，首先会通过触发#DB #BP，然后借助IDT进入windows内核，这便是我们可以触发VT调试的点，即，当触发#DB #BP时，VT host会接管异常，并分发到我们自己的调试器，当调试器处理完成后，VT负责注入异常或者继续执行

![](https://mmbiz.qpic.cn/mmbiz_jpg/1woCcbOsjVNuyrN3ThWJhWaQ5eGdQGwCEeic0YPSwbBHudwg4ejMsqNVBhlnjfWE7wdFlbJpsqdf4LticN7lMiajV7r7aomrW6t85MXZYicUsEA/640?wx_fmt=jpeg)

代码修改：

1. Exception map

首先，我们找到setup\_vmcs中的针对\_vt\_vmcs\_exceptionbitmap的写入值，这个字段主要的作用是它记录的值中如果某一位为1，那么当idt触发对应的中断时，会进入vt host，例如当#DB触发时，如果\_vt\_vmcs\_exceptionbitmap的值为 1 << 1，那么#DB会进入VT的host的代码中，这里我们把exception\_map的值改为 1 << 1

|  |
| --- |
| C++                   uintptr\_t exception\_bitmap = 1 << 1;                    nerror |= \_\_vmx\_vmwrite((size\_t)\_vt\_vmcs\_field::\_vt\_vmcs\_exceptionbitmap, exception\_bitmap); |

2. VT处理异常代码

我们在代码中需要对\_vt\_exitreason\_exceptionornmi进行处理，即vt\_vmm\_handleexception函数，在该函数中，我们需要对#DB进行判断，并打印一条日志，并按原属性进行注入事件，在我们修改的代码中可以看到，判断了type(Hardware)和vector(#DB)，这个type和vector是一一对应的，具体值需要参考intel的手册，这里就不再展开了

|  |
| --- |
| C++                   void vt\_vmm\_handleexception(\_vt\_vmhandle\_guestcontext\* guest\_context) {                        size\_t exit\_exception\_value = 0;                       \_\_vmx\_vmread((size\_t)\_vt\_vmcs\_field::\_vt\_vmcs\_vmexitintrinfo, &exit\_exception\_value);                       const \_vt\_vmexit\_interruptioninformationfield exception = { exit\_exception\_value };                        const \_vt\_interruption\_type interruption\_type = (\_vt\_interruption\_type)(exception.fields.interruption\_type);                       const \_vt\_interruption\_vector vector = (\_vt\_interruption\_vector)(exception.fields.vector);                        ULONG\_PTR guest\_inst\_length;                       \_\_vmx\_vmread((ULONG\_PTR)\_vt\_vmcs\_field::\_vt\_vmcs\_vmexitinstructionlen, &guest\_inst\_length);                        ULONG\_PTR error\_code = 0;                       \_\_vmx\_vmread((ULONG32)\_vt\_vmcs\_field::\_vt\_vmcs\_vmexitintrerrorcode, &error\_code);                        if (interruption\_type == \_vt\_interruption\_type::\_vt\_interruption\_hardwareexception) {                           // Hardware exception                           if (vector == \_vt\_interruption\_vector::\_vt\_intteruptionvec\_debugexception)                           {                               DbgPrintEx(DPFLTR\_IHVDRIVER\_ID, DPFLTR\_ERROR\_LEVEL, "GetInt1 %p\n", PsGetCurrentProcessId());                               vt\_vmm\_injectinterruption(\_vt\_interruption\_type::\_vt\_interruption\_hardwareexception, vector, exception.fields.error\_code\_valid, error\_code);                               \_\_vmx\_vmwrite((ULONG32)\_vt\_vmcs\_field::\_vt\_vmcs\_vmentryinstructionlen, guest\_inst\_length);                           }                           else {                               vt\_vmm\_injectinterruption(interruption\_type, vector, exception.fields.error\_code\_valid, error\_code);                                \_\_vmx\_vmwrite((ULONG32)\_vt\_vmcs\_field::\_vt\_vmcs\_vmentryinstructionlen, guest\_inst\_length);                           }                       }                       else {                           vt\_vmm\_injectinterruption(interruption\_type, vector, exception.fields.error\_code\_valid, error\_code);                            \_\_vmx\_vmwrite((ULONG32)\_vt\_vmcs\_field::\_vt\_vmcs\_vmentryinstructionlen, guest\_inst\_length);                       }                   } |

3. 代码测试

我们将驱动在测试环境中加载起来，此时我们需要触发#DB，才能在驱动的输出中看是否拦截到了，所以，在这里需要打开调试器对文件进行单步，笔者使用了x64dbg对一个exe进行调试，可以看到，笔者单步两次后，debug中是可以打印出对应的日志的，证明此时host拦截到正确的数据了

![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVNY9fiajLzdMnIhia1b6ztwZBHs9TaUCENtEfB3bU4IN9FlDafUK2bXprO74C7tz7qG34gRKdgAGzC2iciapiaTSVtyTuN250CtmRBY/640?wx_fmt=png)

Guest代码转向

现在，我们开始编写guest代码，guest的流程主要为，host注入guest转向，guest代码跳转到我们自己的stub上，stub最后触发host处理，最后host恢复环境，然后ring3继续执行，这里触发host处理，我们用vmcall指令即可

首先，我们在汇编中添加：

|  |
| --- |
| C++                   asm\_dbg\_entry proc                       mov rcx, 1340h                           vmcall                           int 3 ;不该执行到这里                   asm\_dbg\_entry endp |

其次，我们在#DB中添加注入RIP的代码

|  |
| --- |
| C++                   ....                      if (interruption\_type == \_vt\_interruption\_type::\_vt\_interruption\_hardwareexception) {                        // Hardware exception                        if (vector == \_vt\_interruption\_vector::\_vt\_intteruptionvec\_debugexception)                        {                            DbgPrintEx(DPFLTR\_IHVDRIVER\_ID, DPFLTR\_ERROR\_LEVEL, "GetInt1 %p\n", PsGetCurrentProcessId());                            \_\_vmx\_vmwrite((ULONG32)\_vt\_vmcs\_field::\_vt\_vmcs\_guestrip, (ULONG\_PTR)&asm\_dbg\_entry);                        }                        else {                            vt\_vmm\_injectinterruption(interruption\_type, vector, exception.fields.error\_code\_valid, error\_code);                             \_\_vmx\_vmwrite((ULONG32)\_vt\_vmcs\_field::\_vt\_vmcs\_vmentryinstructionlen, guest\_inst\_length);                        } |

KVA功能的影响

在注入代码后，我们需要考虑的一个问题，就是KVA的问题，如果windows启动了KVA，那么我们还需要更改cr3到kernel态下的CR3，毕竟shadow Cr3只有当前进程的ring3地址，以及ntkernel中的.KVSCode段的地址，我们的驱动不在这个段中，所以需要切CR3；如果没有开启，那么就不需要切了，可以用下面的ps脚本进行判断

|  |
| --- |
| C++                   Install-Module SpeculationControl -Force                   Import-Module SpeculationControl                   Get-SpeculationControlSettings |

笔者的电脑，执行后发现没有开启KVA，查阅相关资料发现在最新的CPU上，已经修复了这个漏洞，所以，windows不再开启了

![](https://mmbiz.qpic.cn/mmbiz_png/1woCcbOsjVOBOmCS0K6ttvPZQvr8pv7eibw6COmzS1iafQibZ1rkJEZqff8Rjv9KENgkY1lAxq9Bfp3gucjL1nDXBjYL2iac65crCOB316uV3GQ/640?wx_fmt=png)

需要保留的寄存器：

以上的代码展示了核心部分，但不是完整流程，因为在vmcall后，host需要恢复现场内容，所以需要将现场数据进行保存

1. eflags寄存器

该寄存器必然会被修改，因为至少tf位会被置为0，否则当注入guest后，会再次触发#DB，最后走入异常状态，我们根据Intel手册中对eflags的描述，我们将Eflags置为2，原始值保存

2. DR寄存器

和eflags的理由相同，当启动Dr时，如果地址被ring3精心构造，那么我们会在stub的某个地方触发#DB异常，导致异常状态，我们把Dr7改为0x400，屏蔽掉其他的Dr寄存器，避免触发

3. Guest context寄存器

包含cs和ss、rip、rsp、rcx，为了在vmcall的时候直接恢复，所以这几个段需要保存，这里可能会有读者有些疑问，为什么rcx也需要保存呢？因为我们在再次进入host时，用的vmcall，为了判断编号，所以用的时rcx，所以这个rcx是需要保存的

4. guest\_exceptionreason、error\_code、指令长度等

这些都和guest注入异常有关系，所以也需要进行保存，这样可以避免后续未处理时，注入错了异常

我们总结一下整体的结构

|  |
| --- |
| C++                   struct DBG\_Stack {                       ULONG\_PTR Dr7;                       ULONG\_PTR guest\_inst\_length;                       ULONG\_PTR exception\_type;                       ULONG\_PTR exception\_vector;                       ULONG\_PTR csbase;                       ULONG\_PTR cslimit;                       ULONG\_PTR csselector;                       ULONG\_PTR ssselector;                       ULONG\_PTR csarbytes;                       ULONG\_PTR ssbase;                       ULONG\_PTR sslimit;                       ULONG\_PTR ssarbytes;                       ULONG\_PTR ip;                       ULONG\_PTR eflags;                       ULONG\_PTR sp;                       ULONG\_PTR original\_rcx;                   }; |

申请并填充栈

为了保存我们需要的数据，我们需要将我们的数据保存在栈上，并为了避免返回Ring3的时候，Ring3找到相关的数据，所以我们需要自己申请一块地址，保存context

|  |
| --- |
| C++                   PHYSICAL\_ADDRESS phys = { 0 };                   phys.QuadPart = ~0ULL;                   auto stack = (ULONG\_PTR)MmAllocat...