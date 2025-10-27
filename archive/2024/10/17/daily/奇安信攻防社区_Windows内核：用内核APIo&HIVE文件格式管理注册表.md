---
title: Windows内核：用内核APIo&HIVE文件格式管理注册表
url: https://forum.butian.net/share/3810
source: 奇安信攻防社区
date: 2024-10-17
fetch_date: 2025-10-06T18:50:44.595391
---

# Windows内核：用内核APIo&HIVE文件格式管理注册表

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

### Windows内核：用内核APIo&HIVE文件格式管理注册表

前言
注册表（Registry）是Windows操作系统中的一个重要数据库，用于存储系统和应用程序的配置和设置信息。注册表包括多个层次结构的键（Key）和值（Value），通过这些键和值，操作系统和应用程...

前言
==
注册表（Registry）是Windows操作系统中的一个重要数据库，用于存储系统和应用程序的配置和设置信息。注册表包括多个层次结构的键（Key）和值（Value），通过这些键和值，操作系统和应用程序可以管理各种设置，如硬件配置、用户偏好和系统服务等。
病毒木马可以操作注册表实现注入、开机自启动、驱动加载等恶意行为。病毒木马可以通过直接调用导出的内核API函数操作注册表，但由于内核API操作比较容易检测和监控（例如，hook api），所以也可以通过注册表更底层的HIVE文件操作注册表。HIVE文件是注册表中很底层的文件形式，所以更难被检测和监控。
注册表
===
注册表是一个层次结构的数据库，有五个一级分支（也成为根键，root key）。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-b1c34d108a0f999230f5ce627974c84a98dcd230.png)
注册表存储的内容对于用户来说都相当重要，这也是为什么越来越多的恶意软件将攻击对象转向了注册表。
病毒和木马常常利用注册表进行下列操作：
- 持久化操作：通过在注册表中添加自启动项，恶意软件可以在系统启动时自动运行。
- HKEY\\_LOCAL\\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run
- HKEY\\_CURRENT\\_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run
- 隐藏自身：修改注册表的一些设置，以隐藏自身的文件或进程。例如，通过修改Explorer的设置来隐藏自身。
- 修改系统配置：破坏系统的正常允许。例如禁用任务管理器、Windows安全中心等等。
- 劫持应用程序：通过修改与特定文件类型关联的程序，恶意软件可以劫持系统中的某些应用程序的启动。如修改`.exe`文件的关联，使所有可执行文件都由恶意软件启动。
- 收集信息：一些病毒木马会在注册表中窃取敏感信息，如用户凭据、系统配置或其它机密数据。
内核API
=====
函数介绍
----
用户层和内核层中各有一组注册表API函数，这俩者的函数命名、使用方式和实现功能都类似。这里只讲述基于内核API函数实现的注册表管理。
### 创建注册表项
`ZwCreateKey`函数用于创建一个新的注册表项或打开一个现有的注册表项。`ZwOpenKey`也可以用于打开注册表项。
函数原型：
```c
NTSTATUS ZwCreateKey(
PHANDLE KeyHandle, //指向接收注册表项句柄的变量。
ACCESS\_MASK DesiredAccess,
POBJECT\_ATTRIBUTES ObjectAttributes,
ULONG TitleIndex,
PUNICODE\_STRING Class,
ULONG CreateOptions,
PULONG Disposition
);
```
主要代码：
```c
HANDLE hKey;
UNICODE\_STRING regPath;
RtlInitUnicodeString(&regPath, L"\\Registry\\Machine\\Software\\MyKey");
OBJECT\_ATTRIBUTES objAttr;
InitializeObjectAttributes(&objAttr, &regPath, OBJ\_CASE\_INSENSITIVE, NULL, NULL);
NTSTATUS status = ZwCreateKey(
&hKey,
KEY\_ALL\_ACCESS,
&objAttr,
0,
NULL,
0,
NULL
);
if (NT\_SUCCESS(status)) {
// 成功创建或打开注册表项，接下来可以进行其他操作
}
```
### 删除注册表键与键值
使用`ZwDeleteKey`函数删除注册表键，利用`ZwDeleteValueKey`删除键值。
这俩个函数的函数原型类似，前者只接收一个参数`KeyHandle`后者多接收一个`ValueName`。
使用：
```c
NTSTATUS status = ZwDeleteKey(hKey);
if (NT\_SUCCESS(status)) {
// 成功删除注册表项
}
UNICODE\_STRING valueName;
RtlInitUnicodeString(&valueName, L"MyValue");
NTSTATUS status = ZwDeleteValueKey(hKey, &valueName);
if (NT\_SUCCESS(status)) {
// 成功删除键值
}
```
### 添加或修改注册表键值
通过`ZwSetValueKey`函数实现注册表键值的添加或者修改功能。
函数原型：
```c
NTSTATUS ZwSetValueKey(
HANDLE KeyHandle,
PUNICODE\_STRING ValueName,
ULONG TitleIndex,
ULONG Type,
PVOID Data,
ULONG DataSize
);
```
`KeyHandle`是注册表句柄，由`ZwCreateKey`或`ZwOpenKey`返回。`ValueName`是要设置的值名称。由`Data`指向要写入的数据，`DataSize`表示数据的字节大小。
```c
UNICODE\_STRING valueName;
RtlInitUnicodeString(&valueName, L"MyValue");
DWORD data = 1;
NTSTATUS status = ZwSetValueKey(
hKey, // 之前创建或打开的注册表项句柄
&valueName,
0,
REG\_DWORD,
&data,
sizeof(data)
);
if (NT\_SUCCESS(status)) {
// 成功设置键值
}
```
### 查询注册表键值
`ZwQueryValueKey`函数可以查询注册表键值，获取键值的数据和类型。
函数原型：
```c
NTSTATUS ZwQueryValueKey(
HANDLE KeyHandle,
PUNICODE\_STRING ValueName,
KEY\_VALUE\_INFORMATION\_CLASS KeyValueInformationClass,
PVOID KeyValueInformation,
ULONG Length,
PULONG ResultLength
);
```
`KeyValueInformationClass`指定查询的信息类型，例如KeyValueBasicInformation。
实操
--
### 实现注册表持久化操作
实现这个操作的核心是利用 `ZwSetValueKey` 函数，在`Run`键下添加一个指向应用程序路径的值，实现持久化。
关键步骤：
1. \*\*打开注册表 `Run` 键\*\*：通过 `ZwOpenKey` 打开 `HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run` 键。
2. \*\*设置自启动项\*\*：使用 `ZwSetValueKey` 将应用程序的路径写入到 `Run` 键下，这样在系统启动时，指定的应用程序就会自动运行。
3. \*\*关闭句柄\*\*：操作完成后，关闭注册表句柄。
代码如下：
```c
#include <ntddk.h>
VOID ShowError(PUCHAR pszText, NTSTATUS ntStatus)
{
DbgPrint("%s Error[0x%X]\n", pszText, ntStatus);
}
// 注册表持久化操作：在 Run 键中添加自启动项
BOOLEAN SetRegistryAutoRun(PUNICODE\_STRING ustrExecutablePath)
{
HANDLE hKey = NULL;
OBJECT\_ATTRIBUTES objectAttributes;
UNICODE\_STRING ustrKeyPath, ustrValueName;
NTSTATUS status;
// 定义注册表的 Run 键路径
RtlInitUnicodeString(&ustrKeyPath, L"\\Registry\\Machine\\Software\\Microsoft\\Windows\\CurrentVersion\\Run");
// 初始化 OBJECT\_ATTRIBUTES 结构体
InitializeObjectAttributes(&objectAttributes, &ustrKeyPath, OBJ\_CASE\_INSENSITIVE, NULL, NULL);
// 打开 Run 键
status = ZwOpenKey(&hKey, KEY\_ALL\_ACCESS, &objectAttributes);
if (!NT\_SUCCESS(status)) {
ShowError("ZwOpenKey", status);
return FALSE;
}
// 定义注册表键值的名称（自定义名称）
RtlInitUnicodeString(&ustrValueName, L"MyPersistentApp");
// 设置自启动项，写入可执行文件的路径
status = ZwSetValueKey(hKey, &ustrValueName, 0, REG\_SZ, ustrExecutablePath->Buffer, ustrExecutablePath->Length);
if (!NT\_SUCCESS(status)) {
ZwClose(hKey);
ShowError("ZwSetValueKey", status);
return FALSE;
}
// 关闭注册表键句柄
ZwClose(hKey);
DbgPrint("Successfully set auto-run entry.\n");
return TRUE;
}
// DriverEntry：示例驱动入口函数
NTSTATUS DriverEntry(PDRIVER\_OBJECT pDriverObject, PUNICODE\_STRING pRegistryPath)
{
UNICODE\_STRING ustrExecutablePath;
// 指定要持久化的可执行文件路径
RtlInitUnicodeString(&ustrExecutablePath, L"C:\\Path\\To\\YourApp.exe");
// 设置自启动项
SetRegistryAutoRun(&ustrExecutablePath);
return STATUS\_SUCCESS;
}
```
HIVE文件解析
========
在学习文件管理技术的时候，我们知道计算机上所有的信息都是以文件的形式存储在磁盘上的。注册表当然也算，我们看到的注册表是一个层次结构，它是经过注册表编辑器读取之后呈现给我们的，其磁盘形式是一组称为HIVE的单独文件形式。
HIVE与其它文件形式不同，每个HIVE文件都可以理解为一颗单独的注册表树，就像Windows 的 PE 格式一样，它也有自己的组织形式。
HIVE文件概念
--------
简单理解，HIVE文件格式就是Windows操作系统用来存储注册表数据的一种二进制文件格式。
一个注册表 HIVE 文件是由一个 Header 以及多个 HBIN 记录所组成的。而每一个 HBIN 记录又是由 Cell 记录和 List 记录等所组成的。其中，Cell 记录包含 nk、vk 以及 sk记录;List 记录包括lf、lh、li、ri 以及 db 记录。
HIVE文件一般位于`%SystemRoot%\System32\Config`:
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-2d41d106f583374bf5b46ec808ef274b5d753236.png)
HIVE文件通常不能使用文本编辑器打开，可以通过regedit.exe导出HIVE文件，再使用WinHex进行分析。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-dde3896df38c352ee928c4050d489a78a0f552ea.png)
记得导出的时候要导成注册表配置单元文件，而不是reg后缀的注册文件。
HIVE文件格式结构
----------
HIVE的格式结构较为复杂，下列结构分析以导出的SOFTWARE HIVE文件为例。
### Header
每个HIVE文件都有一个头部，包含文件的基本信息，如签名、版本、序列号等。这个数据结构在整个HIVE文件格式中处于顶层，并且包含了一些关键的字段，用于标识和管理HIVE文件。HIVE的大小通常为4096（0x1000）个字节大小，即4kb。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-e39a4c6cefbeada372cd6744ac71bfe08602686c.png)
如上图所示：
- Signature（0x0）：HIVE文件的标识符，通常为字符串`regf`，用于标识它是一个HIVE文件。
- 主序列号（0x4）：用于校验完整性。
- 次序列号（0x8）：同上。
- 最后写入事件（0xC）：这个占8个字节，表示HIVE文件的最后写入事件，通常是Windows文件时间格式。如图是0x1DAEF8B3B87FBA9，转换为十进制表示为133682520239111081个100纳秒，即13368252023--&gt;423年，然后加上Windows文件起始时间1601.1.1，即可得到最后写入时间2024
- 主版本号（0x14）：表示HIVE的主要版本。
- 次版本号（0x18）：表示HIVE的次版本。
- Type文件类型（0x1C）：表示HIVE的文件类型，如0x0为标准类型，0x1为事务日志方式存储的HIVE文件。
- 格式标志（0x20）：表示HIVE文件的格式类型。
- 根键的偏移量（0x24）：它表示RootCell的相对偏移位置，注意在HIVE中所有的偏移量都是相对于第一个HBIN块的。Header大小占4096字节，其后紧跟HBIN，也就是0x1000处为HBIN。这个键表示第一个HBIN块的第一个cell位置在0x1020处。
- 文件长度（0x28）：记录整个HIVE文件的字节数。从图中可知0x86C9000--&gt;141332480--&gt;138020kb，这实际上比我们导出的要小：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-92ea3bea1778c0274104499d1a37e7b3f5e4eea5.png)
这是因为这一数值并不包含注册表头的大小，也不包含注册表 HIVE结尾处的一些附加数据。
- 文件名（0x30）：存储HIVE文件的名称信息，通常是配置单元的路径或名称。以0x00为结尾的Unicode字符串。这里我也不知道为啥我的没显示，换了好几个HIVE文件了也是空白。
### HBIN
第一个HBIN块位于Header后面，即0x1000处：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-aa17d8e911ddb6040885809202a471a895545646.png)
HBIN的典型大小为4096字节，也可以是多个4096字节的倍数。HBIN块是HIVE文件中的数据存储单元，包含多个“单元”（Cell），每个单元可以是键、值、或子键等信息。每个HBIN块开头有一个头结构，包含块的大小和偏移量。HBIN块中的数据按顺序存储，形成注册表树结构。
重点字段：
- Signature（0x0）：通常为ASCII的hbin。
- 文件偏移（0x4）：表示相对于第一个HBIN块的偏移。
这里用第二个HBIN块查看：
![image.png](https://cdn-yg-zzbm.y...