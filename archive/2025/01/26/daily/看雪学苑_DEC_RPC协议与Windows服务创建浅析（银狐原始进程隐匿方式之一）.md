---
title: DEC/RPC协议与Windows服务创建浅析（银狐原始进程隐匿方式之一）
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589259&idx=1&sn=2076280e4c58e4cd0d718047946ebe83&chksm=b18c28c186fba1d72857bb2f9ecd1cf60756243ffde6306a22d046402d7ef801dfff28547af8&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-26
fetch_date: 2025-10-06T20:10:10.271545
---

# DEC/RPC协议与Windows服务创建浅析（银狐原始进程隐匿方式之一）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXQWxT1FPBibfL2b3QhicbckeCfrib1E1zynuz26TibVOLLz7nLb8ENFTGmA/0?wx_fmt=jpeg)

# DEC/RPC协议与Windows服务创建浅析（银狐原始进程隐匿方式之一）

time.time

看雪学苑

该方法是在一个银狐家族的样本中发现的，通过构造RPC数据包并发送请求至对应的RPC服务，能够绕过多个终端安全软件对CreatServices、NrdClientCall3等3环函数的Hook，从而规避服务创建监控和限制，构建出全白的进程链，使进程可信，且与原始进程断链，提升隐匿性，降低查杀阈值。

常见的RPC程序调用构建好必要的数据后，最终通过NrdClientCall系列函数进行通信，而这个函数中调用的下层的函数其实就是对RPC bind和RPC Request等数据包的处理，主要由NtAlpcSendWaitReceivePort等一系列NtAlpc函数完成。因为CreatServices和NrdClientCall等api会被杀软进行Hook，所以该方法未使用这些敏感API进行服务创建，而是自己构建符合格式的RPC数据包进行发包通信来创建服务，因此可以绕过部分只对RPC系列函数和服务创建启动等相关函数进行hook检测而未对RPC协议进行解析的安全软件。

一个完整的RCP调用的过程可以粗略分为Rpc绑定(连接)、Rpc绑定响应、Rpc请求、Rpc请求响应。通过逆向Services.exe、本地抓包以及查阅文档资料的方式可以获取到相关结构体和数据包。

```
一

RPC数据包的构成与解析
```

##

RPC通信前需要先进行绑定，这个过程和TCP的握手有点类似，各自在本地维护一个内存结构，用于记录通信的状态，这里的内存结构称之为**RpcConnectionStruct**。此结构体维护Rpc通信的连接状态和数据输入输出的缓冲区，发送的RPC数据包由另外几个重要的数据结构和数据缓冲区构成：

◆**绑定过程数据包**：RpcBaseHeaderStruct、RpcBindRequestHeaderStruct、RpcBindResponseHeaderStruct、数据

◆**请求通信数据包**：RpcBaseHeaderStruct、RpcRequestHeaderStruct、RpcResponseHeaderStruct、数据

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXFnahX2AUXaKicmibbziaXHD0d3ib10P71kmVX7iaxwt3uOJ34ibbNhwlTribw/640?wx_fmt=other&from=appmsg)

**RPC数据包的解析大致是这样**：

RPC数据包发送(写入) 先写入RpcBase头，再写入RpcRequestHeader，最后跟上RpcConnectionStruct->bProcedureInputData（数据包）。

RPC数据包接受(读取) 先读取RpcBase头、判断Rpc通信的版本、数据包类型、数据包标记、数据帧长度是否等于实际读取长度。然后是**RpcResponseHeader**，最后是返回包的具体数据，这里面包含的是和指定RPC服务的数据。

下面我们具体了解一下这个通讯过程中需要用到的数据结构和相应的字段。

```
二

RpcConnectionStruct
```

##

这个结构体维护Rpc通信的连接状态和一些必要数据，和TCP通信一样，在本地维护一段连接状态的数据结构，是自定义构建RPC通信的重要结构体之一，其中最重要是的**hFile**字段，这是一个句柄类型。打开一个RPC服务创建的命名管道可以获得该句柄，通过此句柄可以连接到指定的rpc服务。与RPC服务通信的请求body和响应body也放在这个结构体中，每次的消息发送与接受都要处理这个数据结构。下面是用C语言定义的结构体类型：

```
struct RpcConnectionStruct {
    HANDLE hFile;                // 文件句柄，用于RPC通信的管道
    DWORD dwCallIndex;           // 调用索引，用于标识RPC请求
    DWORD dwInputError;          // 输入错误标志
    DWORD dwRequestInitialised;  // 请求初始化标志
    BYTE bProcedureInputData[MAX_PROCEDURE_DATA_LENGTH];  // 存储过程输入数据，后续通信的发送的数据都按格式排在这
    DWORD dwProcedureInputDataLength;  // 存储过程输入数据长度
    BYTE bProcedureOutputData[MAX_PROCEDURE_DATA_LENGTH]; // 存储过程输出数据
    DWORD dwProcedureOutputDataLength;  // 存储过程输出数据长度
};
```

以银狐样本的中用到的SVCCTL服务为例，services.exe在主程序函数SvcctrlMain中注册了SVCCTL服务接口，其定义了一个命名管道符：**\pip\ntsvcs**和两种RPC底层通信协议序列：ncacn\_np（命名管道协议序列）、 ncalrpcs（本地进程间通信协议序列）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX3qYdcbXnUA4HiawAdbX9TKibibSGkmLKMlRyhlwNSicjUMJCGkHES6NhyA/640?wx_fmt=other&from=appmsg)

一个RPC服务可以绑定多种协议序列，也可以只绑定某一种协议序列，这是实现相关的，没有定式。某接口绑定N种协议序列，就意味着有N条途径可以访问该接口。WIndows的DCE/MS RPC框架使用的下层协议序列有很多：

```
               +-- ncacn_ip_tcp(动态TCP口)
            |
DCE/MS RPC--+-- ncadg_ip_udp(动态UDP口)
            |
            +-- ncacn_np(固定的139、445/TCP口)
            |
            +-- ... ...(其它协议序列)
```

对于**命名管道**(ncacn\_np)的通信方式，一般使用CteateFile函数打开对应管道符获取返回值句柄，后面会将管道句柄填充到RpcConnectionStruct的hFile字段，用于维护RPC客户端的连接状态。

```
HANDLE hFile = NULL;
char szPipePath[512];
RpcConnectionStruct RpcConnection;

// set pipe path
memset(szPipePath, 0, sizeof(szPipePath));
_snprintf(szPipePath, sizeof(szPipePath) - 1, "\\\\.\\pipe\\%s", pPipeName);

// open rpc pipe
hFile = CreateFileA(szPipePath, GENERIC_READ | GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, NULL);
memset((void*)&RpcConnection, 0, sizeof(RpcConnection));
RpcConnection.hFile = hFile;
```

对于RPC服务来说，实现具体功能的是其不同**接口**下面的**方法**，因此想要远程调用指定服务功能除了需要管道句柄，还需要绑定对应功能接口、数据序列化与反序列化接口以及调用号。这些接口数据的定义在微软的官方文档、RPC服务程序的反编译、RPC通信抓包中可以找到部分。下面详解一下上面提到的另外几个关键结构体*:RpcBaseHeaderStruct、RpcBindRequestHeaderStruct、RpcBindResponseHeaderStruct、RpcRequestHeaderStruct、RpcResponseHeaderStruct。*

#

```
三

RpcBaseHeaderStruct
```

##

# rpc基础头，包含rpc的版本，包类型，rpc包长度等字段。在rpc初次连接绑定阶段时，包长度就等于rpc基础头+rpc请求头的结构体大小，Bind包一般大小固定72，Bind\_Ack包一般大小固定60。

```
struct RpcBaseHeaderStruct
{
    WORD wVersion;                // 版本号5
    BYTE bPacketType;             // 包类型，Bind 11,响应Bind_ack 12，13代表失败  发送其他请求时为0 返回包该字段为2代表成功
    BYTE bPacketFlags;            // 包标志3
    DWORD dwDataRepresentation;   // 数据表示0x10
    WORD wFragLength;             // 片段长度(Base头+BindRequest头+RPC连接中的InputDataLengt)
    WORD wAuthLength;             // 认证长度0
    DWORD dwCallIndex;            // 调用索引从0递增1，每个包都要自增，由RPC连接结构体维护并重新给base头
};
```

**wVersion**字段目前在DECRPC包中能看到的基本都是v5，较早的windows2000系统中有v4的版本，所以后续可以认为是一个固定值5。

**bPacketType**字段在初次发送绑定连接包时应设置为11(bind包)，类似于TCP的ＳＹＮ包，且当接受绑定返回包时需要校验bPacketType的值是否等于12(bind\_ack)，类似于TCP协议的ＡＣＫ包，否则证明连接失败，此时的值一般是１３。

其他字段的含义部分在注释中注明，详细信息可自行查找文档研究。

```
四

RpcBindRequestHeaderStruct
```

##

rpc绑定请求头，包含需要绑定接口的GUID、接口版本、通信协议、协议版本等信息。

以SVCCTL服务为例，services.exe在程序中使用**RpcServerRegisterIf3**函数注册了其接口信息，接口信息由一个名为RPC\_SERVER\_INTERFACE的结构体构成，详细的结构体信息会在后面补充信息中贴出，这里只关注该结构体中的两个重要字段：**InterfaceId**和**TransferSyntax**。这两个字段就是服务接口的GUID和序列化接口的GUID，我们拿到这两个GUID后填充到绑定请求头中。

```
struct RpcBindRequestContextEntryStruct
{
    WORD wContextID;               // 上下文ID，用于标识特定的接口或对象。0
    WORD wTransItemCount;          // 传输项目计数，通常用于指定传输语法的数量。1
    BYTE bInterfaceUUID[16];       // 接口的全局唯一标识符（UUID），用于唯一标识一个接口。如367abb81-9844-35f1-ad32-98f038001003
    DWORD dwInterfaceVersion;      // 接口版本号，用于指定请求的接口版本。2
    BYTE bTransferSyntaxUUID[16];  // 传输语法的UUID，用于指定数据传输时使用的协议格式。如8a885d04-1ceb-11c9-9fe8-08002b104860
    DWORD dwTransferSyntaxVersion;// 传输语法版本号，用于指定传输语法的具体版本。2
};

struct RpcBindRequestHeaderStruct
{
    WORD wMaxSendFrag;           // 最大发送片段大小 默认4096
    WORD wMaxRecvFrag;           // 最大接收片段大小 默认4096
    DWORD dwAssocGroup;         // 关联组标识绑定包 0 返回包0x00012bee
    BYTE bContextCount;          // 上下文数量
    BYTE bAlign[3];              // 对齐填充
    RpcBindRequestContextEntryStruct Context; // 上下文条目
};
```

这个绑定请求头由两个结构体构成，其中绑定请求上下文结构体存在4字节对齐，因此大小会有变化。部分字段的意义已在上面进行了注释，除了wContextID字段是双方在自增后存在RpcConnectionStruct头中维护外，其他字段都需要具体服务具体分析。

在前面对services.exe的反编译过程中已发现其他注册接口的接口体，其中就包含他的接口版本以及接口GUID：367abb81-9844-35f1-ad32-98f038001003以及序列化协议GUID:8a885d04-1ceb-11c9-9fe8-08002b104860，直接填充到RpcBindRequestContextEntryStruct结构体的字段中。

下面看绑定响应头的数据结构：RpcBindResponseHeaderStruct

```
五

RpcBindResponseHeaderStruct
```

##

这个结构体其实分为三段，由RpcBindResponseHeader1Struct+SecondaryAddrHeaderBlock+RpcBindResponseHeader2Struct构成。

结构体如下:

```
struct RpcBindResponseHeader1Struct
{
    WORD wMaxSendFrag;
    WORD wMaxRecvFrag;
    DWORD dwAssocGroup;
};
struct SecondaryAddrHeaderBlock
{
    WORD ScndryAddrLen;
    BYTE ScndryAddr;
    BYTE bAlign[3];// 4字节对齐填充
};
struct RpcBindResponseContextEntryStruct
{
    WORD wResult;//返回值不为0代表bind失败，在解析时必须判断该项
    WORD wAlign; //Ack reason
    BYTE bTransferSyntax[16];//在wResult不为0时该字段表示序列化的协议
    DWORD dwTransferSyntaxVersion;
};

struct RpcBindResponseHeader2Struct
{
    DWORD dwContextResultCount;//返回值为1代表存在上下文
    RpcBindResponseContextEntryStruct Context;
};
```

Bind\_ack包如下:

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXXlL6ksBOCfiaGSL2PmicMXiba3po5ex9X0Ih1JVUP7N9N7q3uiaGC0ib5Xw/640?wx_fmt=other&from=appmsg)

**ScndryAddr**字段的长度不确定，存在0-65535这样２到6个字节的变化，需要4字节对齐。

**wResult**字段在绑定成功时返回值为0，其他值参考如下：

◆**Acceptance (0)**：这是一个成功的响应，表明服务器端接受了客户端的RPC调用请求，并成功执行了相应的操作。

◆**User rejection (1)**：这个响应表示用户拒绝了RPC调用请求，可能是因为权限不足或用户拒绝执行该操作。

◆**Provider rejection (2)**：表示服务提供者拒绝了客户端的绑定请求，通常是因为服务接口不受支持。

◆**Reject (3)**：这是一个通用的拒绝响应，表明服务提供者因为某些原因拒绝了RPC调用请求，但具体原因未指定。

◆**Other rejection (4)**：这个响应表示服务提供者因为其他未在前几个响应类型中列出的原因拒绝了RPC调用请求。

当**wResult**字段不为0时，另外的三个字段就有了意义，**wAlign字段**会提供更详细的失败原因，具体代表什么含义可自行查相关文档。

而**bTransferSyntax**字段会在**wResult**字段等于2，**wAlign字段**等1时提供包含服务提供者支持的传输语法UUID，用于告知客户端服务端支持的传输语法。

关于RPC接口绑定相关的数据结构和对构建数据包比较重要的字段已做了详细解释，其他部分也做了简单的注释，了解这些已经就可以做简单的PRC绑定包构造了，如果遇到其他未知的信息可以在调试时结合相关文档具体分析。当接口绑定成功后，就可以发送指定接口的函数调用号用于执行我们想要执行的功能了，比如打开服务控制器、创建服务、开启服务等。

```
六

RpcRequestHeaderStruct
```

##

这个结构体中关注一个字段wProcedureNumber，这里存放接口函数的调用号，用于确定远程调用方法。

结构体如下:

```
struct RpcRequestHeaderStruct
{
    DWORD dwAllocHint;          // 分配提示，用于服务器分配内存以存储回应
    WORD wContextID;            // 上下文...