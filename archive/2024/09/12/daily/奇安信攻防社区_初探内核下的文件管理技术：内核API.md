---
title: 初探内核下的文件管理技术：内核API
url: https://forum.butian.net/share/3714
source: 奇安信攻防社区
date: 2024-09-12
fetch_date: 2025-10-06T18:23:30.096938
---

# 初探内核下的文件管理技术：内核API

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

### 初探内核下的文件管理技术：内核API

前言
Windows内核下的Rootkit开发技术学习。
用户数据都以文件的形式存储在本地磁盘上，Rootkit等恶意软件想要获取用户的隐私数据就需要有操作文件的功能，包括但不限于增、删、查、改。一般有...

前言
==
Windows内核下的Rootkit开发技术学习。
用户数据都以文件的形式存储在本地磁盘上，Rootkit等恶意软件想要获取用户的隐私数据就需要有操作文件的功能，包括但不限于增、删、查、改。一般有三种文件管理的方式，一是基于导出的内核API直接操作文件，二是通过程序直接构造输入输出请求包（I/O Request Package,IRP)并发送IRP来操作文件，三是根据文件系统格式（New Technology File System,NTFS)来解析硬盘上的二进制数据。本文先从相对简单的内核API实现开始学习，内核API和用户模式中的WIN32 API有一定的类似。
编程环境：
- 主机 Win11 Visual Studio2019，SDK和WDK 10.0.19041.685
- 虚拟机 Win10测试模式
前置
==
内核API
-----
内核API是一组从内核组件中输出的函数，大多数函数在内核本身模块（NtOskrnl.exe）中实现，少部分在其它模块中（如hal.dll)。内核API是大量C函数的集合，其中大多数名称含有一个前缀，这个前缀指示了实现该函数的模块。
常见的一些内核API前缀：
- Ex：通用执行体函数 `ExAllocatePool`
- Ke：通用内核函数 `KeAcquireSpinLock`
- Io：I/O管理器 `IoCompleteRequest`
- Zw：原生API包装 `ZwCreateFile`
Zw前缀的内核API是原生API包装的，原生API指的是前缀为Nt的一系列函数。Nt系列函数（如`NtCreateFile`）是Windows内核提供的原生API，它们直接与内核模式交互。但应用程序调用WIN32API时，这些API最终会转换成对应的Nt函数，执行实际的操作。
所谓的包装意味着Zw系列和Nt系列在实现上几乎相同，但它们通过不同的入口点进入系统。当内核模式调用Nt系列函数时，函数会检查调用上下文，以确定调用来自内核模式还是用户模式，如果来自用户模式，函数可能会进行一些安全检查或模式转换。而调用Zw系列函数，系统假设调用已经在内核模式下了，即直接将PreviousMode设置成 KernelMode（0）。
OBJECT\\_ATTRIBUTES 结构
---------------------
`OBJECT\_ATTRIBUTES`是Windows内核编程中用于描述操作系统对象（如文件、设备、事件、互斥体等）属性的结构体。该结构体通常在创建或打开内核对象时被使用，传递给如`ZwCreateFile`、`ZwOpenKey`等内核API。
```c
typedef struct \_OBJECT\_ATTRIBUTES {
ULONG Length; // 结构体的大小，以字节为单位。
HANDLE RootDirectory; //表示对象名称的根目录句柄。
PUNICODE\_STRING ObjectName; //指向UNICODE\_STRING结构体的指针，表示对象的名称。
ULONG Attributes; //指定对象的属性。
PSECURITY\_DESCRIPTOR SecurityDescriptor; //指向安全描述符的指针。常设NULL。
PSECURITY\_QUALITY\_OF\_SERVICE SecurityQualityOfService; //用于指定对象的安全服务质量属性,常设NULL。
} OBJECT\_ATTRIBUTES, \*POBJECT\_ATTRIBUTES;
```
上述字段中，如果`RootDirectory`为NULL，则`ObjectName`必须是一个完整的绝对路径名。否则，`ObjectName`是相对与`RootDirectory`目录的路径名。
`Attributes`常见的属性标志：
- `OBJ\_CASE\_INSENSITIVE`：表示对象名称比较不区分大小写。
- `OBJ\_KERNEL\_HANDLE`：指示句柄只能在内核模式下访问。
- `OBJ\_OPENIF`：如果对象存在，则打开它，而不是失败。
- `OBJ\_PERMANENT`：创建一个永久对象，不会自动删除。
InitializeObjectAttributes 宏
----------------------------
`InitializeObjectAttributes` 宏用于初始化 `OBJECT\_ATTRIBUTES` 结构体，这俩者都同属于`ntdef.h`。
宏定义如下：
```c
#define InitializeObjectAttributes(p, n, a, r, s) { \
(p)-&gt;Length = sizeof(OBJECT\_ATTRIBUTES); \
(p)-&gt;RootDirectory = r; \
(p)-&gt;Attributes = a; \
(p)-&gt;ObjectName = n; \
(p)-&gt;SecurityDescriptor = s; \
(p)-&gt;SecurityQualityOfService = NULL; \
}
```
p 指向 `OBJECT\_ATTRIBUTES`结构体的指针，字段如上述一样。
文件的创建和删除
========
ZwCreateFile
------------
在内核层中的病毒木马要想创建或者释放植入程序，最先的是创建一个文件。`ZwCreateFile`函数用于创建或打开文件对象，它是内核模式下访问文件系统的关键API。该函数同样可以用于创建或打开目录。
函数原型如下：
```c
NTSTATUS ZwCreateFile(
PHANDLE FileHandle, //指向接收文件句柄的指针。
ACCESS\_MASK DesiredAccess, //指定文件访问的类型，例如读、写、执行等。
POBJECT\_ATTRIBUTES ObjectAttributes,//指向已经初始化的OBJECT\_ATTRIBUTES结构体.
PIO\_STATUS\_BLOCK IoStatusBlock, //指向IO\_STATUS\_BLOCK结构的指针
PLARGE\_INTEGER AllocationSize, //指定文件的分配大小。
ULONG FileAttributes, //指定了创建或覆盖文件时的属性
ULONG ShareAccess, //指定文件的共享模式。
ULONG CreateDisposition, //指定文件的创建方式，如文件已存在时应如何处理。
ULONG CreateOptions, //指定文件的创建方式，如文件已存在时应如何处理。
PVOID EaBuffer, //指向扩展属性（EA，Extended Attributes）缓冲区的指针，通常用于网络文件系统。
ULONG EaLength //EaBuffer的长度
);
```
`ZwCreateFile`在使用时取决于字段`CreateOptions`，如果该字段设置了FILE\\_DIRECTORY\\_FILE标志，表明这是创建一个目录。
在内核模式下创建文件的步骤：
- 初始化`UNICODE\_STRING`结构，这是文件路径的表达形式。
- 设置`OBJECT\_ATTRIBUTES`结构体，调用宏初始化。
- 调用`ZwCreateFile`函数。
- 在执行完相应操作后使用`ZwClose`关闭文件句柄，释放资源。
### 具体代码：
```c
#include
void CreateFileTest()
{
NTSTATUS status;
HANDLE hFile;
OBJECT\_ATTRIBUTES objAttr;
IO\_STATUS\_BLOCK ioStatusBlock;
UNICODE\_STRING fileName;
//初始化UNICODE\_STRING
RtlInitUnicodeString(&amp;fileName, L"\\??\\C:\\Users\\example\\Desktop\\syswork\\MyFile.txt");
//初始化OBJECT\_ATTRIBUTES
InitializeObjectAttributes(&amp;objAttr, &amp;fileName, OBJ\_CASE\_INSENSITIVE | OBJ\_KERNEL\_HANDLE, NULL, NULL);
//调用ZwCreateFile
status = ZwCreateFile(&amp;hFile, GENERIC\_WRITE | GENERIC\_READ, &amp;objAttr, &amp;ioStatusBlock, NULL, FILE\_ATTRIBUTE\_NORMAL, 0, FILE\_OPEN\_IF, FILE\_SYNCHRONOUS\_IO\_NONALERT, NULL, 0);
//检查
if (NT\_SUCCESS(status)) {
DbgPrint("File created or opened successfully.\n");
}
else {
DbgPrint("Failed to create or open file.Status: 0x%X\n", status);
}
//关闭文件句柄
if (hFile) {
ZwClose(hFile);
}
}
NTSTATUS DriverEntry(PDRIVER\_OBJECT DriverObject, PUNICODE\_STRING RegistryPath)
{
UNREFERENCED\_PARAMETER(DriverObject);
UNREFERENCED\_PARAMETER(RegistryPath);
CreateFileTest();
return STATUS\_SUCCESS;
}
```
需要注意的地方，初始化`UNICODE\_STRING`时：文件路径要包含`\\??\\`,这是Windows内核中的一个符号链接，用于将内核模式的文件路径映射到用户模式的路径。
`ZwCreateFile`的`FILE\_OPEN\_IF`标志告诉内核，如果文件已经存在则打开它，如果文件不存在则创建它。
### 驱动加载：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-153ecd290e3b62a733680ce87b14d33e4ee87f89.png)
在虚拟机上加载驱动程序，要打开测试模式。还有visual studio生成解决方案时要用x64生成，使用x86生成的sys在win10上可能会报签名错误。
ZwDeleteFile
------------
删除指定文件。函数声明如下：
```c
NTSTATUS ZwDeleteFile(
\_In\_ POBJECT\_ATTRIBUTES ObjectAttributes
);
```
唯一的参数，指向一个 `OBJECT\_ATTRIBUTES` 结构的指针。
如果要单独写一个删除文件的sys，步骤和`ZwCreateFile`是相同的，先初始化文件路径和`OBJECT\_ATTRIBUTES`结构体，然后调用就好。这里演示，直接将ZwDeleteFile加到上述代码中。
### 部分代码：
```c
status = ZwDeleteFile(&amp;objAttr);
if (NT\\_SUCCESS(status)) {
DbgPrint("File deleted successfully.\\n");
} else {
DbgPrint("Failed to delete file. Status: 0x%X\\n", status);
}
```
报未找到`ZwDeleteFile`的错误，可以添加一个`#include`，注意要放在ntddk前面。
### 驱动加载：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-2689631d79c449ed42fb985caaeea51e4ea50e8a.png)
获取文件大小
======
ZwQueryInformationFile
----------------------
要对文件进行操作免不了要获取文件的大小，以便申请数据缓冲区。在用户层中，通过`GetFileSize`函数获取文件大小；在内核模式下，要获取文件的大小，可以通过调用 `ZwQueryInformationFile` 函数，配合 `FILE\_STANDARD\_INFORMATION` 结构来完成。`ZwQueryInformationFile` 函数允许我们查询文件的各种属性，其中 `FILE\_STANDARD\_INFORMATION` 结构包含了文件的大小信息。
函数定义：
```c
NTSYSAPI NTSTATUS ZwQueryInformationFile(
[in] HANDLE FileHandle, //文件或设备的句柄。
[out] PIO\_STATUS\_BLOCK IoStatusBlock, //指向一个 IO\_STATUS\_BLOCK 结构的指针，用于接收请求的状态信息和实际传输的字节数。
[out] PVOID FileInformation, //指向接收所请求信息的缓冲区。
[in] ULONG Length, //指定FileInformation缓冲区的大小（以字节为单位）。
[in] FILE\_INFORMATION\_CLASS FileInformationClass //一个枚举类型，指定要检索的文件信息类型。
);
```
其中字段`FileInformationClass`常用的类型包括：
- `FileBasicInformation`: 基本文件信息，例如创建时间、上次访问时间。
- `FileStandardInformation`: 标准文件信息，包括文件大小、分配大小、文件是否为目录等。
- `FilePositionInformation`: 当前文件指针的位置。
`ZwQueryInformationFile`函数的返回值是一个`NTSTATUS`代码，表示操作的成功与否。
FILE\\_STANDARD\\_INFORMATION 结构
------------------------------
`FILE\_STANDARD\_INFORMATION` 结构用于存储与文件或目录相关的标准信息。它是内核API`ZwQueryInformationFile`常使用的一个信息结构，当该函数的`FileInformationClass`参数设置为`FileStandarInformation`时，这个结构会返回标准文件信息，包括文件大小、分配大小等。
结构定义：
```c
typedef struct \_FILE\_STANDARD\_INFORMATION {
LARGE\_INTEGER AllocationSize; // 文件的分配大小
LARGE\_INTEGER EndOfFile; // 实际大小
ULONG NumberOfLinks; // 指向文件的硬链接数
BOOLEAN DeletePending; // 文件是否已标记为删除
BOOLEAN Directory; // 是否是目录
} FILE\_STANDARD\_INFORMATION, \*PFILE\_STANDARD\_INFORMATION;
```
部分代码实现：
-------
`ZwQueryInformationFile`的第一个参数是文件句柄，该句柄需要由`ZwCreateFile`或其它函数提供。因此同删除文件类似，可以对第一个具体代码进行修改，在创建或打开文件后，获取文件的大小。
变量要添加一行`FILE\_STANDARD\_INFORMATION fileInfo;`
```c
if (NT\_SUCCESS(status)) {
DbgPrint("File opened successfully.\\n");
// 查询文件信息以获取文件大小
status = ZwQueryInformationFile(hFile, &amp;ioStatusBlock, &amp;fileInfo, sizeof(fileInfo), FileStandardInformation);
if (NT\_SUCCESS(status)) {
// 输出文件大小信息
DbgPrint("File size: %llu bytes\\n", fileInfo.EndOfFile....