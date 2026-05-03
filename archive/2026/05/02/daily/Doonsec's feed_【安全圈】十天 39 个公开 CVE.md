---
title: 【安全圈】十天 39 个公开 CVE
url: https://mp.weixin.qq.com/s/A-5JWYhoCbWczQjwL_b3Qg
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:23:34.843312
---

# 【安全圈】十天 39 个公开 CVE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyG3YvFUftRdCR1tS9WoNUic9gjRia4cyM54Np5mhBSCJn7lCctIu4iatsjic6RjO4lstuAMQKibOVR7sCDGKSmmqRsVF5PtEVEdrKfA/0?wx_fmt=jpeg)

# 【安全圈】十天 39 个公开 CVE

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

AI漏洞挖掘

**写在前面**

2026 年 4 月 22 日到 5 月 1 日，**10 天**。

CVE 公开数据库里多了 **39 条** 致谢 Innora.ai 的记录。

CVE-2026-37555、CVE-2026-6857、CVE-2026-40858、CVE-2026-42482⋯⋯一个一个查 CVE Services API，全是 PUBLISHED。

把这 39 条记录摊开看，比"AI 找到了一个高危洞"更值得圈内关注的是：

它们**不在同一种产品里**，**不靠同一个 fuzzing 模板**，**不挂在同一种语言上**。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **#** | **类别** | **项目** | **数量** | **典型风险** |
| 1 | 基础音频库 | libsndfile 1.2.2 | 1 | IMA-ADPCM 整数溢出（不完整修复变体） |
| 2 | 企业中间件 | Apache Camel / Red Hat Camel | 2 | camel-infinispan 不安全反序列化 (CWE-502) |
| 3 | 安全工具 | hashcat v7.1.2 | 3 | 规则/Kerberos/PKZIP 解析中的栈与堆溢出 |
| 4 | 车端嵌入式 | Open-SAE-J1939 / isotp-c / uds-c / socketcand / cannelloni / OpenAMP / OVMS3 / AGL / Vanetza | 18 | CAN/UDS/ISO-TP/J1939/V2X/ELF loader 边界失控 |
| 5 | PHP 框架 | MixPHP 2.x | 6 | TCP unserialize / Redis-File handler / SQL 拼接 |
| 6 | Web 管理面 | V2Board 1.7.4 | 3 | XSS / token 暴露 / orderBy 列名注入 |
| 7 | CAD/CAE 解析 | Open CASCADE Technology V8\_0\_0\_rc5 | 6 | STL/OBJ/VRML/IGES/STEP 越界读、递归 |

另有**6 个待核验编号**：CVE-2026-37562、37566、37567、37568、37569、37572。

CVE Services API 当前对它们返回 404，本文不计入"已公开"，也不展开技术归因。

数字之外，更值得读者多看几眼的是分布。

C/C++ 边界错误、Java 反序列化、PHP 不可信数据流、Web 模板未转义、3D 文件解析——任何一种语言、一类输入、一种部署形态，都不是这套流程的天花板。

**跨语言、跨形态、跨场景。** 这件事单靠人或单靠工具都做不出来。

它必须是把研究员的判断、模型的归纳、动态的验证、披露的纪律拧在一起的产物。

**一、不是炫技，是三个工程命题**

39 个 PUBLISHED CVE 摊开看，有三条线特别清晰。

**命题一：同构变体扫描**

一个补丁修了 AIFF 路径，但 WAV 路径和 close 路径没修。

一个边界检查出现在 A 文件，没出现在 B 文件。

一个长度字段被校验，另一个同源字段被信任。

漏洞研究里，最贵的不是发现第一个 bug。

**最贵的是发现它的家族。**

**命题二：信任边界检视**

Infinispan 缓存里的一段数据，为什么能进 ObjectInputStream？

bind 在 127.0.0.1 的 TCP 服务，为什么可以 unserialize 后 call\_user\_func？

abstract Unix socket 上的 supervision 调用，为什么在凭证被置 NULL 之后还继续转发命令？

很多漏洞不在算法里。

**它们在一句默认假设里：这里应该是可信的。**

**命题三：解析器作为攻击面**

WAV、PKZIP、Kerberos、STL、OBJ、VRML、IGES、STEP、PCAP、CAN 数据流，全是解析器的战场。

解析器做的事很普通：读字段、算长度、搬内存、递归展开、转换结构。

**也正因为太普通，它们常常被低估。**

攻击面不是从"危险函数"开始的。

是从"外部输入被解释为内部结构"的那一刻开始的。

**二、案例一：libsndfile，补丁旁边的漏洞**

**CVE-2026-37555**

技术上，这是一个 32 位整数乘法溢出。看起来没有任何"性感"的地方。

但它最适合解释：为什么 AI 在漏洞研究里有结构性价值。

CVE 官方描述里写得很清楚：早年的 CVE-2022-33065 修复了 IMA-ADPCM 编解码中的 AIFF 路径——src/ima\_adpcm.c 的**第 241 行** 给乘法套上了(sf\_count\_t) 强制转换。

第 235 行的 WAV 路径，没改。

>

第 167 行的 close 路径，也没改。

只要samplesperblock × blocks 在 32 位空间溢出，这个错误的乘积就会被赋值给 64 位的 sf.frames——一个被精心构造的 WAV 文件，足以让后续基于错误帧数的内存分配崩塌。

这种 bug 不靠灵感。靠**结构化追问**：

·WAV 分支有没有同样的乘法？

·关闭路径有没有读这同一个长度？

·读取阶段和释放阶段是否共享同一个不可信值？

·一处用了更宽的类型，另一处是不是还停留在 32 位？

模型擅长的事，恰好就是这种**机械级的同构搜索**。它把一个已修复点拆成模式：变量来源、算术表达式、类型宽度、边界检查、相邻格式分支、错误路径、清理路径——然后扫整个仓库。

研究员该做什么？做收敛。把候选清单压成"这里和已修补路径结构一致，但缺少同等约束"，再用 ASAN 跑出可重复的崩溃。

好的 AI 漏洞挖掘，不是输出"这里可能有洞"。

它应该输出：**"这里和补丁同构，但缺少补丁的约束。"**

这才是工程化。

**三、案例二：Apache Camel，缓存不是信任边界的终点**

**CVE-2026-6857 / CVE-2026-40858**

Apache 官方公告写得很坦率：camel-infinispan 组件中，基于 ProtoStream 的远程聚合仓库，**用 `java.io.ObjectInputStream` 反序列化从 Infinispan 缓存里读到的对象，且没有配置任何 `ObjectInputFilter`**。

CWE-502，老牌反序列化坑位。

值得讲的不是"反序列化危险"——这个结论已经讲了十几年。

值得讲的是：在现代企业系统里，**反序列化入口越来越不像入口**。

它不是 HTTP body。

不是 RPC 参数。

不是用户上传文件。

它可能是一条缓存记录。一段消息队列内容。一个连接器在内部传递的对象表示。

当数据进入 Infinispan，它看起来已经"进了系统内部"。但从攻击面建模的角度看，**只要攻击者能写入这个缓存，这里就是输入边界**。

ObjectInputStream 不会因为调用栈看起来内部就自动变安全。

ObjectInputFilter 也不会因为组件名里带个 ProtoStream 就可以省掉。

这类漏洞对 CTO 真正重要的地方在：企业里最难盘清楚的，不是"公网接口有几个"，而是**"内部可信假设有多少层"**。

服务网格、缓存、队列、连接器、插件、低代码扩展，把数据搬来搬去。每一层都可能把上一层的"已验证"误读成自己的"可信任"。

AI 在这里能做的，不是简单 grep ObjectInputStream。

grep 只能告诉你哪里用了危险 API。

工程化的做法是顺着数据流追：谁能写入？经过哪些格式转换？有没有过滤器？有没有类型白名单？异常路径是否会降级到通用反序列化？调用点是否跨越安全域？

**不是看函数名危险不危险。是看一段数据从哪里来、被谁相信、最终被哪个解释器执行。**

**四、案例三：OCCT，工业 CAD 文件就是攻击面**

**CVE-2026-42476 ~ CVE-2026-42481**

Open CASCADE Technology (OCCT) 是工业 3D 内核，被广泛集成进 CAD、CAE、仿真和供应链协同系统。

这一组 6 个 CVE，覆盖了 STL、OBJ、VRML（三个）、IGES + STEP（B-spline）五大文件格式。

CVE 公告里几个原文细节足以说明问题：

·RWStl\_Reader::ReadAscii 和RWObj\_Reader::read 在调用Standard\_ReadLineBuffer::ReadLine() 之后，**没有对返回 buffer 的长度做校验**，就直接调用strncasecmp 或按字节读取（CVE-2026-42476/42477）。

·VrmlData\_Scene::ReadLine 在处理转义字符时用了ptr[++anOffset]，**走出了固定大小栈缓冲区的边界**（CVE-2026-42480）。

·VrmlData\_IndexedLineSet::TShape 把外部文件的coordIndex 直接当成数组下标用，**没有对照坐标数组的实际长度**（CVE-2026-42479）。

·VrmlData\_IndexedFaceSet::TShape 在 shape 构造期间解引用了未校验的指针（CVE-2026-42478）。

·IGES B-spline 曲线评估和 STEP B-spline 构造里，存在**越界读** + **无限递归**（CVE-2026-42481）。

工程结论很直接：**只要一个系统支持导入文件，它就在接受攻击者提供的结构化输入**。

3D / CAD / 工程格式解析器常常被当成"业务能力"，不是"安全边界"。但它们出现在桌面软件、云端转换服务、缩略图预览、供应链协同平台、工业仿真平台——任何一个集成了 OCCT 内核的产品，都在执行这条解析链。

解析器漏洞挖掘的核心不是撞运气。

是把"输入字段如何变成内存行为"这条链路压出来：

·长度字段有没有和实际 buffer 绑定？

·递归结构有没有深度限制？

·字符串比较有没有越过实际行缓冲？

·几何参数有没有进入数组索引？

·错误恢复路径会不会继续消费未校验数据？

这些问题没法用一个 prompt 一次答完。

它们是**多轮交叉、数据流追踪、动态验证**叠在一起的工程问题。

**五、车端 18 个 CVE：协议栈才是真正的攻击面**

如果说 libsndfile 和 OCCT 是低调的工程提醒，**车端这 18 个 CVE 才是这批结果里最有传播价值的一组**。

目标覆盖 9 个项目：

Open-SAE-J1939、isotp-c、uds-c、socketcand、cannelloni、OpenAMP、OVMS3、AGL、Vanetza。

涉及的协议层：

CAN、CAN FD、UDS、ISO-TP、J1939、V2X、嵌入式 ELF loader、车载应用框架。

CVE 描述里给出的细节非常具体，没有任何渲染：

**Open-SAE-J1939（CVE-2026-37534 / 37537 / 42467）**

传输协议处理器中：uint8\_t index = data[0] - 1。

当 CAN 帧首字节为 0，index 下溢成 255。

后续写入tp\_dt->data[255\*7 + i - 1]——抵达偏移 1791，远超 MAX\_TP\_DT\_SIZE，越界写。

**uds-c / agl-service-can-low-level（CVE-2026-37536 / 37530 / 42485）**

send\_diagnostic\_request 用**6 字节栈缓冲区** 接收**7 字节**，再叠加1 + pid\_length 偏移。payload\_length 是uint8\_t，**没有上界校验**。

栈被 1-4 字节的攻击者可控数据覆盖。

**OVMS3 3.3.005（CVE-2026-37541 / 42468 / 42469）**

开源车辆监控系统：

canformat\_gvret.cpp 的 GVRET length、canformat\_pcap.cpp 的phdr.len、canformat\_canswitch.cpp 的 CANswitch DLC——**三个长度字段全部未校验**。

**AGL afb-daemon（CVE-2026-37525 / 37526）**

抽象 Unix socket @urn:AGL:afs:supervision:socket 上：

on\_supervision\_call 调用afb\_context\_change\_cred(&xreq->context, NULL) 把凭证置 NULL，然后继续 xapi->itf->call(xapi->closure, xreq) 转发命令。

8 个 supervision 命令（Exit、Do、Sclose、Config、Trace、Debug、Token、slist）**没有任何认证**就能被本地任意进程调用。

**AGL widget（CVE-2026-37531）**

Zip Slip + TOCTOU 双重缺陷：

is\_valid\_filename 阻止了绝对路径，**没有阻止 dot notation 目录穿越**。

zread 用openat(workdirfd, ...) 提取文件，**存在 check 与 use 的双重竞态**。

**Vanetza V2X v26.02（CVE-2026-37554）**

GeoNetworking 报文管线里，OpenSSL ECC 点验证抛出的异常（无效压缩点、点不在曲线上），Router::indicate() 调用链没有捕获。

未处理的std::runtime\_error 直接崩 daemon。

这些不是"AI 玄学"。它们是**朴素到刺眼的工程检查**：

·长度字段是否受控？

·整数会不会下溢？

·固定栈缓冲区是否匹配协议长度？

·异常会不会跨过边界无人处理？

·协议帧字段会不会直接变成内存偏移？

车端代码有它的特点：长期服务于资源受限环境，C/C++ 历史包袱重，协议状态机复杂，测试样本经常偏正常流量。

正常流量测不出边界。

**攻击者只关心边界。**

车端安全长期被讲成"T-Box、APP、云 API"。

这 18 个 CVE 是一次提醒：**真正的攻击面，在协议栈本身。**

在 CAN 帧解析的那一行 data[0] - 1。

在 UDS 诊断请求的那个 6 字节栈缓冲区。

在 abstract Unix socket 上的 change\_cred(NULL)。

OEM、Tier-1、车载安全团队，需要把这些位置加进自己的代码审查清单。**不是某个白皮书清单，是真正的源码行号清单。**

**六、hashcat：安全工具自己也要被审计**

**CVE-2026-42482 / 42483 / 42484**

hashcat v7.1.2，全球安全行业最常用的密码恢复工具。

三个 CVE 全部命中**它自己处理外部输入的解析路径**：

·mangle\_to\_hex\_lower() 和mangle\_to\_hex\_upper() 在src/rp\_cpu.c 里有一个**栈溢出**：边界检查没考虑 hex 转换的 2 倍膨胀。规则文件配合 -j / -k 选项，加上 128 字符以上的密码候选，就能触发。

·Kerberos 哈希解析里，account\_info\_len 由不可信的分隔符位置算出，**没有上界校验就 memcpy** ——堆溢出。

·PKZIP 哈希解析的 hex\_to\_binary 里，攻击者控制的 hex 数据被解码进**固定大小 buffer**，没有长度检查。影响 modules 17200、17210、17220、17225、17230。

这一组的反讽在于：**安全工具本身也在处理不可信输入**。

规则文件、hash 文本、压缩包派生数据、Kerberos 结构、密码候选——它们都来自外部样本或批量任务。

"这是安全人员用的工具"不构成安全边界。

恰恰相反，hashcat 这类工具常常运行在**高权限机器、自动化流水线、SOC 取证环境、CTF 集群**里。把外部样本喂进去，是它的本职工作。

它们应该被当作高价值解析器审计——而且要假定**输入永远是恶意的**。

**七、MixPHP / V2Board：老问题的新位置**

**MixPHP 2.x（CVE-2026-37552 / 42471 / 42472 / 42473 / 42474 / 42475）**

公开描述给的位置非常具体：

·Server.php:87 里，sync-invoke TCP 服务从 socket 拿数据，**直接喂给 `Opis\Closure\unserialize()`**，再call\_user\_func() 执行结果。bind 在 127.0.0.1 上，**没有任何认证或签名**。能访问本机端口的进程，等于 RCE。

·Connection.php:76 上，sync-invoke 客户端对服务器响应也调 unserialize()——连到一个恶意服务器就能反向 RCE。

·Redis handle...