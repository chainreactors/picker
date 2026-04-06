---
title: 汽车SOME/IP协议如何Fuzzing
url: https://mp.weixin.qq.com/s/rm_2yfWcQ8TS8ICe3PyB3w
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:40:04.418970
---

# 汽车SOME/IP协议如何Fuzzing

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD8QxFwHVV0Dd5hyReiaB5EpEe8Who8UicFFcNOMw6fpKnoWtvPHwsOsuJUufBDfGtVO25zJ3zqZYhWY334ibhsRdNBEiaUtKWC9W0/0?wx_fmt=jpeg)

# 汽车SOME/IP协议如何Fuzzing

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

**01**

**关于SOME/IP和Fuzzing**

近年来，汽车行业对于连接车辆的更多数据通信的需求不断增加。更高的数据交换量要求底层通信协议具备更高的带宽，这对车辆中广泛使用的现有通信协议如CAN、LIN、FlexRay等构成了挑战。现有协议的限制使得需要采用新的通信协议来支持汽车行业的新趋势，而汽车以太网则是其中有前途的解决方案之一。

SOME/IP是一种轻量级协议，用于简化进程/设备间的通信，支持过程调用和事件通知。由于其简单和高效的特点，SOME/IP被越来越多的汽车设备采用。随着SOME/IP的出现，SOME/IP应用程序的漏洞检测变得至关重要。

**02**

**SOME/IP协议概述**

汽车以太网上的众多上层协议中，SOME/IP 是一种专门针对汽车的协议，通过 UDP 协议栈提供基于服务的通信，使不同车辆组件之间进行基于服务的通信成为可能，例如在信息娱乐系统和发动机控制单元之间的通信。SOME/IP 的关键特点之一是其高效地使用单播和组播通信。这使得在组件之间发送控制消息时，网络不会被不必要的流量拥塞。除此之外，SOME/IP 协议还包括远程过程调用（RPC）、服务发现（SD）、服务事件的发布/订阅以及 UDP 消息的分段等功能 。这些功能是通过数据序列化实现的，其中 SOME/IP 消息头被预置到消息的有效载荷前面。消息头包含以下字段：

1. MessageID：标识应用层中的 RPC 调用或事件，其中包含 2 个子字段 ServiceID 和 MethodID；
2. Length：指示从 RequestID 到 SOME/IP 消息结尾的字节数；
3. RequestID：区分用于同一事件的并行使用的数据包，其中包含 2 个子字段 ClientID 和 SessionID；
4. Protocol Version：标识使用的 SOME/IP 头部格式；
5. Interface Version ：使用的 SOME/IP 协议的主要版本
6. Message Type ：用于区分 SOME/IP 协议中的不同消息类型
7. Return Code ：指示请求是否已成功处理。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibPwsd4Rc6xdEBHVXHjdnSuT73BDYpj9bicUagJmtcnJM6WOOzzj5WrNp55TLTlkH94XHUpTPBicF0w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

SOME/IP协议消息头格式 图1

**03**

**灰盒模糊测试**

在过去的十年中，模糊测试已经展示了在漏洞检测方面的潜力，并被用于发现开源和闭源软件中的数千个漏洞。此外，研究人员也提出了新的模糊测试技术来模糊不同的协议实现，如FTP或RTSP。然而，与常规以太网上运行的FTP或其他协议不同，汽车以太网上的SOME/IP和其他汽车以太网协议通常是简单直接的。这是因为运行这些协议的设备的计算能力通常是有限的。一方面，协议设计的简单性意味着模糊测试器不需要为协议维护状态机模型，如AFLnet。另一方面，计算能力的限制意味着我们需要寻求在并行运行多个模糊测试器以提高模糊测试效率。

灰盒模糊测试是一种广泛用于检测真实世界程序漏洞的方法。近年来，像AFL、libFuzzer等灰盒模糊测试工具已经帮助发现了数千个漏洞。灰盒模糊测试的基本思想是应用一些预定义的生成和变异策略来产生输入，然后通过观察受监视的执行过程中的安全问题来发现错误。

下面是一个典型的灰盒模糊测试工具的工作流程：

1. 定义输入生成和变异策略：模糊测试工具应用一组预定义的输入生成和变异策略来生成输入，这些输入会被提供给目标程序。这些策略可以包括翻转、替换、添加/减去位、字节或块，或者基于输入结构生成输入。
2. 目标程序的插装：目标程序通常会插入特定的代码段，以在模糊测试期间提供覆盖反馈。这些反馈有助于根据特定文件输入评估程序执行。
3. 监控执行：模糊测试工具会监控执行过程，以确定是否观察到任何安全违规。可以使用AddressSanitizer、MemorySanitizer等工具来帮助识别这些违规。例如内存使用后释放、缓冲区溢出等安全违规通常表示实现缺陷，这可能会导致漏洞，如内存损坏、信息泄露等。
4. 发现漏洞：如果触发了违规，相应的文件输入将被用作漏洞的证明。
5. 增加覆盖率：如果模糊测试工具发现当前输入有助于增加覆盖率，则会用于后续变异。
6. fork-exec模型：由于执行会被重复多次且由模糊测试工具进行控制，因此可采用fork-exec模型来减少加载目标程序公共序言代码段的开销，并提高整体模糊测试性能。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibPwsd4Rc6xdEBHVXHjdnSugPsGZNzbnOP9Re1xD48SljiaiczhkH7NDUozkdjSgSk5SlJkWtWLAU2g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

灰盒模糊测试流程 图2

**04**

**如何有效Fuzzing SOME/IP**

在现有的方法中，每个模糊测试器实例将管理和运行唯一的测试目标实例。然而，如果测试目标需要某些独特的资源（例如端口，锁定文件等）才能执行，则测试目标只能在每个设备上运行一个实例。在SOME/IP中，服务器应用程序通常在每个设备上运行一个实例，这使得进行并行模糊测试变得具有挑战性。

针对这些挑战，我们介绍一个针对SOME/IP应用程序的灰盒模糊测试工具-Ori。Ori具有两个关键创新点：附加模糊测试模式和结构变异。附加模糊测试模式使Ori能够高效地测试服务器程序，而结构变异使Ori能够有效地生成有效的SOME/IP数据包以到达目标程序的深层路径。通过评估表明，Ori可以准确高效地检测SOME/IP应用程序中的漏洞。

**SOME/IP模糊测试的常规设计步骤**

1. 选择fuzz工具：根据需要，选择一个适合的fuzz工具进行SOME/IP模糊测试，如AFL、libFuzzer或Ori等。
2. 选择目标程序：选择需要进行SOME/IP模糊测试的目标程序，确保其符合SOME/IP协议规范，并且能够接受并处理来自模糊测试的数据包。
3. 准备seed文件：生成或准备一个符合SOME/IP协议规范的数据包作为初始化的样本文件。
4. 配置fuzz工具参数：根据需要，配置fuzz工具的参数，如超时时间、内存限制、CPU核心数等。
5. 启动模糊测试：将seed文件作为输入文件，启动fuzz工具进行模糊测试。fuzz工具将在seed文件的基础上生成大量随机变异的数据包，并将其发送到目标程序进行测试。
6. 分析测试结果：当模糊测试结束后，需要对测试结果进行分析，包括生成的数据包数量、覆盖率、崩溃数等指标。通过分析测试结果，可以发现目标程序的漏洞，从而进行修复。

**用Ori实现SOME/IP变异包方法**

Ori是一种基于变异的覆盖引导灰盒模糊测试的工具，它通过在目标程序中插入代码来收集执行反馈以帮助模糊测试。是否可借助Ori的两个关键特性进行SOME/IP协议的变异包实现？

**第一个特性是附加模式**

当我们使用Ori进行fuzzing时，fuzzer会附加到被测试的进程上。换句话说，我们首先启动被测试的进程，然后运行fuzzer与被测试的进程进行通信并执行fuzzing。这与以前的fuzzer情况不同，以前的fuzzer负责启动被测试的进程和管理被测试进程的生命周期。

整个过程可以分为两个步骤：fuzzing设置步骤和多附加fuzzing步骤。

1. 在fuzzing设置步骤中，仪表化的目标程序将在特定条件下分叉出一个fuzzing服务器。fuzzing服务器是从仪表化的原始进程分叉出来的，并将循环等待传入的fuzzing请求。
2. 成功设置后，我们可以运行一个或多个前端fuzzer。前端fuzzer将与fuzzing服务器通信，并发送附加请求。一旦fuzzing服务器接收到请求，它将分叉出一个fuzzing目标进程，该进程与前端fuzzer一起执行所有剩余的fuzzing流程。

总的来说，附加模式消除了加载特定SOME/IP实现的前导代码段的多余执行。通过这个特性，Ori通过专注于实际协议逻辑来提高整体性能，并提供了调用多个fuzzing实例进行并行fuzzing的能力。

**第二个特性是Ori支持种子输入的两个变异级别**

SOME/IP协议的数据包包含两个部分：正文和头部。相应地，Ori使用不同的变异算子来处理不同的部分。通过变异数据包的正文部分，Ori可以测试SOME/IP服务器的核心逻辑。通过变异数据包的头部部分，Ori可以测试SOME/IP协议的实现。

对于数据包的正文部分，Ori使用类似于AFL的朴素随机变异算子，如位/字节翻转、替换/添加/删除随机块等。对于数据包的头部部分，Ori首先识别头部的不同字段，然后根据字段的类型应用变异。值得注意的是，Ori不会变异ServiceID、ClientID、Protocol Version和Interface Version字段。这是因为变异这些字段不会有助于覆盖测试目标的关键逻辑。例如，如果突变数据包的ServiceID字段，并且无法匹配测试目标提供的服务，则数据包将立即被拒绝，测试目标的更深层逻辑将不会被执行。了解此特点之后，Ori可以生成可以到达目标程序的深层逻辑的数据包，并且可以同时测试协议框架和应用程序。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibPwsd4Rc6xdEBHVXHjdnSuNKEMpyMw0WfNvzGjmEJvQcxm0HJ1PoAQRHx1dOse3Ex9ksibcORIohg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

Ori的架构图3

**05**

**Fuzzing SOME/IP的流程设计**

Ori包括一个前端fuzzer和后端目标，两者之间详细的fuzz流程如图4所示，其中包含两个阶段：准备阶段和测试阶段。

**1）准备阶段**

在进行SOME/IP模糊测试之前，我们需要进行准备阶段，以确保测试目标的可用性和测试环境的稳定性。以下是详细的步骤：

1. 启动目标服务器程序并进入forkserver状态：首先，我们需要启动目标服务器程序，并将其设置为forkserver模式。这样，目标程序可以与fuzzer进行通信，并接收来自fuzzer的测试数据。
2. 启动fuzzer：接下来，我们需要启动fuzzer，以准备开始模糊测试。在启动fuzzer之前，我们需要设置fuzzing环境，如共享内存、输出目录等。
3. 检查目标程序的forkserver状态：fuzzer将尝试联系目标程序，以检查其是否已准备好与fuzzer通信。如果目标程序已经处于forkserver状态，则它将通知fuzzer，并准备接收来自fuzzer的测试数据。
4. 启动主fuzzing循环：如果目标程序已准备好与fuzzer通信，则fuzzer将启动主fuzzing循环。在主循环中，fuzzer将生成大量随机变异的数据包，并将其发送到目标程序进行测试。如果目标程序崩溃或产生其他异常行为，则表明存在漏洞，需要进行修复。
5. 结束fuzzing：当fuzzing循环结束时，fuzzer将生成测试报告，包括生成的数据包数量、覆盖率、崩溃数等指标。通过分析测试结果，我们可以发现目标程序的漏洞，并进行修复。

**2）测试阶段**

Fuzzer将生成数据包来测试目标服务器并处理测试结果。首先，fuzzer将向forkserver发送一个请求，要求它fork一个新实例进行测试。这个测试实例从forkserver逻辑被插入的点开始执行，因此测试实例可以跳过与测试无关的逻辑执行。测试实例开始执行后，它会通知fuzzer继续执行。然后，fuzzer将使用结构变异生成一个新的SOME/IP数据包，并将其发送到测试实例。变异的数据包头部有助于测试数据包解析组件，而变异的数据包主体有助于测试服务器的业务逻辑。在测试实例执行完成后，forkserver将收集其退出状态和执行覆盖信息，并将收集到的数据向fuzzer报告。

在处理测试结果时，Ori与其他基于覆盖率的灰盒fuzzer类似。如果数据包导致测试实例崩溃，fuzzer将保留它以供将来分析。如果数据包可以增加代码覆盖率，fuzzer将保留它作为生成新测试用例的种子。这标志着一轮测试的结束。如果用户不停止fuzzer或目标服务器，则整个过程将继续进行下一轮测试。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibPwsd4Rc6xdEBHVXHjdnSuKxibYICHoQ1B0iaJdpH5P0RTt3OFXlQ0Lz7yCRDS4hUyrwAjmYecSSaw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

Ori详细fuzz流程 图4

**06**

**Fuzzing SOME/IP的具体实现与评估结果**

**1. 实现逻辑**

Ori是一个工具，由两个主要组件组成：代码仪器和模糊器。代码仪器构建在AFL的LLVM模式之上，使用定制的LLVM传递对目标程序进行仪器化。尽管仪器化继承了afl-clang-fast的逻辑来收集代码覆盖信息，但其forkserver注入部分被修改以适应模糊的额外模式逻辑。这个修改涉及约200行C++代码。Ori的模糊器使用约400行Python代码实现，并依赖于Scapy库来执行结构变异。

**2. 验证评估**

1）评估目标

目前，唯一的开源SOME/IP协议框架是GENIVI/vsomeip 。

> GENIVI/vsomeip是一个基于C++语言的开源SOME/IP协议实现框架，主要用于汽车电子领域的通信。SOME/IP是一种轻量级的通信协议，可以在汽车电子中实现多种通信方式，如消息传递、远程过程调用和发布/订阅等。该框架实现了SOME/IP协议的所有特性，包括服务注册、发现、发布、订阅和取消订阅等。它提供了一个高度可扩展和易于使用的API，可帮助开发人员轻松实现复杂的汽车电子应用程序。GENIVI/vsomeip框架还包括一组工具，如vsomeip-sd、vsomeip-jsonconfig和vsomeip-log等，用于简化SOME/IP应用程序的开发和测试。此外，GENIVI/vsomeip框架也可以与其他GENIVI项目进行集成，如DBus和CommonAPI等。

因此，以下描述的测试目标基于GENIVI/vsomeip示例程序的修改版本，所有当前的实验都基于该程序。该程序是一个SOME/IP服务器，接受客户端的消息并发送回"Hello "加上消息内容作为反馈。我们在示例程序中添加了一个崩溃点，以便如果客户端发送以小写字母'a'开头的消息，程序将崩溃。示例程序的修改如图5所示，代码行6-14。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibPwsd4Rc6xdEBHVXHjdnSuuLQuPu4fCZfaNNT3zrFJLJUJ6NG0f2SOckjiaziaQVMKH5H30M9ntZ4w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

GENIVI/vsomeip修改程序示例 图5

2）可附加模式模糊测试

附加模式模糊测试允许多个模糊器实例并行模糊测试，而不会受到端口占用的限制。此外，Ori在初始化主要上下文后插入forkserver逻辑，从而允许测试实例跳过服务器设置过程，显著提高了测试速度。实验结果表明，Ori比现有工具具有更快的执行速度，每个测试用例只需要1-2秒，而没有延迟forkserver插入的AFL至少需要4秒。这些结果表明，Ori是一个高效、灵活和可扩展的模糊测试工具。

Ori相比于现有的工具，具有更快的执行速度和更高的有效性。结构变异的应用使得Ori可以在复杂的协议中生成正确的有效载荷和报头，并显著提高了Ori的有效性。Ori是一个非常有用的工具，可以在软件开发中提高测试的效率和质量。

3）结构变异有效性高

结构变异可以帮助Ori在生成复杂数据包头时，提高其有效性，使其可以测试目标服务器。通过比较，我们可以看出AFL几乎无法生成像SOME/IP数据包头这样复杂的结构，因此即使它可以生成正确的有效载荷，也无法成功将数据包传递到测试目标，这限制了AFL在这种场景下的有效性。而Ori使用结构变异的方法可以生成符合SOME/IP协议要求的数据包头，提高了其有效性和可用性。

这种实验结果可以启示我们，在实际应用中，如果需要对复杂的数据结构进行测试，可以考虑使用结构变异的方法来生成测试用例，以提高测试的有效性。此外，结构变异的应用范围不仅限于模糊测试，还可以用于其他领域，例如软件漏洞挖掘和恶意软件分析等。因此，结构变异作为一种有效的技术手段，可以在软件测试和安全领域中发挥重要作用。

参考文献:

1. A Greybox Fuzzer for SOME/IP Protocols in Automotive Ether...