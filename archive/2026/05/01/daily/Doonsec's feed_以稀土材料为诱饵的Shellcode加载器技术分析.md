---
title: 以稀土材料为诱饵的Shellcode加载器技术分析
url: https://mp.weixin.qq.com/s/kVn2dTLqUaLJ5nahcbrg-Q
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:59:23.786636
---

# 以稀土材料为诱饵的Shellcode加载器技术分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NksXHPG5CBOXicBVe34ox9w08hJCDaHK9R6s3BMPkSDfuYcftSDS5JjhvrRhXMeLePZ88lwJgtFOnegsdGiatdMVJbVoamzILL0/0?wx_fmt=jpeg)

# 以稀土材料为诱饵的Shellcode加载器技术分析

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于李白你好
，作者助力行业的

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM64s9gX2k0hsiazj2NHKBakVpZzzOAgJWEM9BndyEscXZg/0)

**李白你好**
.

综合性的技术交流与资源共享社区 专注于红蓝对抗、渗透攻防、威胁情报、安全资讯分享。网络安全情报攻防站社区：www.libaisec.com

## 概述

2025年11月21日，Malware Hunter Team披露了一个值得关注的样本。该样本从新加坡上传至VirusTotal，是一个名为 `China’s Governance of Rare Earths and its Global Implications.zip` 的压缩文件，解压后包含两个文件：一份带密码保护的PDF文档和可执行程序 `SecurityKey.exe`。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNUPCCu1oPRstWnGFF4ic6DLwGia8Exs18BITiaj67mPmLbksUn1iceM5QxWh4IotDOEbAKfl61nHRYVIkafMV6nAjltbLJeQWMUT58/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=0)![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNVZ7xeF7NmGibNAbgwZLccLQhhia9revohBLlTrYyB7H0W1NGkibj8SfchOgfDibzQFlmxqHkRU57QBrZQsu9oLsvJib8lAnCjPFicDQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

攻击者的意图很明确：受害者试图打开PDF文件时会被提示输入密码，从而被引导去运行配套的可执行程序来获取解锁密码。这一社会工程学手法直接、高效，配合稀土这一地缘政治热点话题，具有相当的欺骗性。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNVEQHP5vricUEnWOPJfbX4vhK5iaZictC9qFuqf8XuniaXmSIibrPyNBaiaPgfxzAjria518wO0UDricothibaQMPpJiblYr1ofUFLWjiaW4U/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

其攻击链可以概括为以下流程：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNXWHjibABAGWhR4OfK41tza39ZnfGerZCcnzcx4KZFRswCACTJWswZMPhKkGbibWvg7HiaMyib0wm7gUaicDbfdh5sqa9ibzicoB5Yg7U/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

## 诱饵分析：精准的地缘政治选题

使用密码 `202511` 解锁PDF后，可以看到一份2025年8月的论文，题为《China’s Governance of Rare Earths and its Global Implications》（《中国的稀土治理及其全球影响》），由S. Rajaratnam School of International Studies（RSIS）出版。RSIS是新加坡南洋理工大学下属的全球研究生院和智库，专注于战略研究与安全事务。

稀土材料在国际政治经济格局中具有极高的战略价值。作为全球最大的稀土生产国和储量国，中国在稀土供应链中占据主导地位。2025年，中国政府加强了对稀土出口的管制措施，引发国际社会广泛关注。RSIS作为新加坡权威智库，其发布的稀土治理研究报告对亚太地区的政策制定者和研究人员具有天然的吸引力，这一选题与样本从新加坡上传的来源地高度吻合。

从威胁情报角度看，将时事热点与学术研究成果捆绑作为恶意软件的载体，是一种成熟的社会工程学范式。攻击者对目标的专业背景和信息需求有着清晰的认知，这暗示其行动具有一定的定向性。

## 加载器机制：从密码提示到代码执行

`SecurityKey.exe` 本身的逻辑并不复杂。程序首先通过消息框展示PDF密码 `202511`，随后立即进入shellcode执行流程：分配一块具有 `PAGE_EXECUTE_READWRITE`（RWX）权限的内存，将嵌入在可执行文件 `.rdata` 节中的shellcode复制到新缓冲区，然后通过函数指针解引用的方式调用执行。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNVquPVvZUJS4mVYZjpGZibTLAHgRicBDfbKtFxxxy1iarOibBlf9JWGJJM7Vot8icXxCDjZnYYYNK6P7INDk1xia5k4VfUa11udvzgAA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNXbDibgXOnotKMBV0OM5kTJN3R8hwUFdS2tCJ8P7X34RcejK380icqbZr39K0IbyeG6n3aL8zmgwhAia0piaqVO866Ixq2iaDbTU0sg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

这种“弹窗—执行”的模式在用户视角下显得自然而无害：程序完成了它宣称的功能（提供密码），用户不会察觉到任何异常。但从技术视角看，内存中出现的RWX页面是一个明显的危险信号。通常正常的Windows应用程序极少同时申请可写可执行的内存区域，这使得RWX内存成为端点检测与响应（EDR）系统的常见启发式特征。近年来越来越多的加载器变种倾向于先以 `PAGE_READWRITE` 分配内存，写入shellcode后再通过 `VirtualProtect` 将权限改为 `PAGE_EXECUTE_READ`，以规避基于内存属性的检测。本样本仍使用直接的RWX分配方式，表明其在反检测方面并未投入过多精力，或许是攻击者认为诱饵本身的欺骗性足以使其绕过初步审查。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNXxhPuA5a5lc8nFePllTjkVTrxfeKia31WNslloawjWOEv7lyJgomUjK9Q8BAV9P6YfK73T3wXuI5pQrx2DJZhvo9RbyUHqlXvE/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6)

## 下载器Shellcode：PEB遍历与API哈希

`SecurityKey.exe` 加载的shellcode本质上是一个下载器，负责获取更高阶段的载荷。这段shellcode是位置无关代码，不能够依赖Windows加载器提供的重定位等服务，必须自行完成函数地址的动态解析。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNUlX900vwSxx9SB0ttdHWIYGKQbdAFMNrhnLAjzAnf74jSLINhnOhicwB4dVVlHKnePGPDmTFuU2fPxjXBpXyDiaNcc3eySE0ebE/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=7)

图片

首先，shellcode通过遍历进程环境块来获取 `ntdll.dll` 的基址。Windows在x64架构下通过GS段寄存器指向PEB，PEB中维护着已加载模块的链表。遍历PEB获取 `ntdll.dll` 基址是shellcode开发中的经典技术，其核心优势在于无需调用 `GetModuleHandle` 等容易被挂钩监控的API。研究显示，许多商业化和开源C2框架的shellcode都依赖这一方法来解析 `kernel32.dll` 和 `ntdll.dll` 地址。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNVqINclBE1n9luDON1awQb9wnPMzyQm6mWcoyx7dyoIS4z896QIQ7BBGWE9A6285jlbX78sMryO2vzNDh1hwLkOYj1OVvuhMT4/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=8)

定位到 `ntdll.dll` 基址后，shellcode采用API哈希技术来解析所需函数。具体做法是：预计算目标API名称的哈希值，然后遍历DLL导出表中每个函数名，计算其哈希值并与目标值比对，匹配成功后即可获取函数地址。这种方法的优势在于shellcode中无需存储明文的API名称字符串，既能减小体积，也增加了静态分析的难度。

## 修改版FNV-1a哈希算法

本样本采用的哈希算法是Fowler–Noll–Vo（FNV）算法的一个修改版本，具体为FNV-1a 32-bit变体。FNV是一种非加密哈希函数，设计目标是速度快、碰撞率低，广泛用于哈希表查找、数据完整性校验等场景。其高度分散的特性使其特别适合哈希URL、主机名、文件路径等相似字符串。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNXUiaY2Clmp3gu0Mj43r6vtEqsGoC5cRtNCcflOdgomNgMsrBdPnV7RHfn696KpS0Vuia4XYnSJicaPBsljutor0HoksicKkUPibWpY/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=9)

FNV-1a与FNV-1的唯一区别在于异或与乘法操作的顺序：FNV-1先乘后异或，而FNV-1a先异或后乘。标准的32位FNV-1a参数为：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNXW69nYFapLqCX8OEAJgAsfxcAtnncpQ39goqYZGkGZD5icRRtgo6F7TZDXEYaE2MF5CBK6N0pHib4ycjMaHNJLfNnonmdkHm3kg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=10)

* 偏移基数（offset basis）：`2166136261`（即 `0x811C9DC5`）
* 质数（FNV prime）：`16777619`（即 `0x01000193`）

攻击者对此进行了修改：

* 修改后的偏移量：`3126136263`（即 `0xBA52D5C7`）
* 修改后的质数：`16737619`（即 `0xFF6E53`）

这一修改有两个层面的意义。在技术层面，它确保通用的FNV哈希识别工具或规则无法直接匹配该shellcode的API解析行为，相当于一种轻量级的代码混淆。在安全产品层面，许多威胁检测引擎内置了对标准FNV-1a哈希常量的特征匹配，修改参数可以有效绕过这类静态检测。从修改幅度来看，偏移量增加了约9.6亿，质数减少了约4万，改动虽不大，但足以破坏基于常量值的检测规则。

## 载荷下载与基础设施仿冒

完成API解析后，shellcode利用 `wininet.dll` 中的网络函数，从 `www.global-reia[.]com/image-directory/da.mp3` 下载后续阶段的shellcode。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNXpbqIhGw1eib61hB80UN13PxupsHBFeTC71dMceQWXIa6IQ61YibLeLibspeAcTYLX0gZaPokaiahwxzbArTK9bpRZD8voJT2lF5c/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=11)

该C2域名的命名值得特别关注：它仿冒了合法域名 `global-reia.org`。`global-reia.org` 隶属于稀土工业协会（Rare Earth Industry Association，简称REIA），这是一家总部位于布鲁塞尔的国际非营利组织，代表全球稀土元素产业的价值链利益。REIA成立于2019年6月，旨在为稀土价值链中的利益相关方提供交流平台，并促进可持续供应链的发展。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNU9EvxUwW9guAwgwvic1ZicQTmuyje7iafmZDZl3rlzU8j4eIVUJxdJc16ZndicGkCZflrZs19bicbrROWeibJcNvu3h6UMwZt1oGYBU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=12)

攻击者使用 `.com` 而非 `.org` 顶级域来仿冒REIA域名，同时将载荷路径伪装为 `/image-directory/da.mp3`，看起来就像一张普通的MP3图片目录文件。这种域名仿冒（typosquatting）与资源路径伪装相结合的技俩表明攻击者对稀土领域有相当的了解，知道REIA在行业内的权威地位，因而选择其作为基础设施伪装的对象。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNUOCW2JX2TibZaGDszM7pSNIJiayfS7y3CbQZsqB6MTsVt2cd2nXlxXxaDTicPPUvTLHFVYMrhGufL07ZFydyrnyXZxiccO8PESTz4/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=13)

该域名 `global-reia[.]com` 解析到IP地址 `45.93.8[.]97`。遗憾的是，DomainTools、Shodan等公开威胁情报平台对该IP在2025年11月前后的标记信息有限，目前能够确认的是该IP确实托管了恶意载荷，但尚未发现其与已知APT组织的明确关联。分析时，从该域名下载的下一阶段shellcode已经不可获取，服务器的后续行为无法进一步追踪。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNXkFM3suH2HZedsrSLTTU4509utgVwQRofTF6uibKVJjZP8WasfsYYM7e3uZfDLsyDIrbl2LibOAdbCypasMpBoVF0MahmPC6ByU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=14)![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNXQkRV61icUImNoqePDnWWGIWMNZHY8eUKoBAHjzPV62ib24hlQ2lvzJ9e1lZm1FGDmc3grT00RkzuiaFnX2iadK9A3XFsq1gBHSIA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=15)

## 纤程执行：一种非常规的Shellcode调度方式

下载完成后，shellcode再次分配具有RWX权限的内存，将载荷放入其中。执行方式并非传统的 `CreateThread`、函数指针调用或APC注入，而是使用Windows纤程机制。

Windows纤程是一种必须在用户态手动调度的执行单元。与线程不同，纤程对内核调度器完全不可见，其调度完全在 `kernel32.dll` 的用户态层面实现。一个线程可以包含多个纤程，但同一时刻只有一个纤程在执行，只有当前纤程主动调用 `SwitchToFiber` 切换到另一个纤程时，上下文才会发生切换。

利用纤程执行shellcode需要调用四个基本API：`VirtualAlloc` 分配内存、`ConvertThreadToFiber` 将当前线程转换为纤程、`CreateFiber` 创建指向shellcode的新纤程、`SwitchToFiber` 将执行权切换到shellcode所在的纤程。这一技术的核心优势在于规避检测：大多数EDR系统会重点监控线程创建相关API（如 `CreateThread`、`NtCreateThreadEx`、`CreateRemoteThread` 等），而纤程的创建和切换发生在用户态，不需要系统调用，从内核的视角来看没有任何新线程产生。

已有多起威胁案例采用类似技术。例如，Trend Micro曾报告TESDAT加载器同样使用 `SwitchToFiber` API来执行解码后的shellcode，研究者认为这正是为了规避检测。Ghos...