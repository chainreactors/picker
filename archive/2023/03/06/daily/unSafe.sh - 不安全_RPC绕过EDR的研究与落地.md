---
title: RPC绕过EDR的研究与落地
url: https://buaq.net/go-152036.html
source: unSafe.sh - 不安全
date: 2023-03-06
fetch_date: 2025-10-04T08:44:59.407506
---

# RPC绕过EDR的研究与落地

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/1e4778977955e83507c7fd33a5901097.jpg)

RPC绕过EDR的研究与落地

1、前言最近研究RPC在内网中的一些攻击面，主要是以红队视角来看，使用RPC协议有时候Bypass EDR等设备会有较好的效果，那么什么是RPC呢，RPC 代表“远
*2023-3-5 12:47:0
Author: [xz.aliyun.com(查看原文)](/jump-152036.htm)
阅读量:58
收藏*

---

## 1、前言

最近研究RPC在内网中的一些攻击面，主要是以红队视角来看，使用RPC协议有时候Bypass EDR等设备会有较好的效果，那么什么是RPC呢，RPC 代表“远程过程调用”，它不是 Windows 特定的概念。RPC 的第一个实现是在80年代在UNIX系统上实现的。这允许机器在网络上相互通信，它甚至被“用作网络文件系统（NFS）的基础”，其实简单的说就是它允许请求另一台计算机上的服务，本节内容主要是依靠[Microsoft官方文档](https://learn.microsoft.com/zh-cn/windows/win32/rpc/rpc-start-page "Microsoft官方文档")进行学习。

## 2、RPC结构相关概念

1、首先我们要理解RPC是如何进行通信的首先需要知道几个概念IDL文件，UUID，ACF文件

IDL文件：为了统一客户端与服务端不同平台处理不同的实现，于是有了IDL语言。IDL文件由一个或多个接口定义组成，每一个接口定义都有一个接口头和一个接口体，接口头包含了使用此接口的信息(UUID和接口版本)，接口体包含了接口函数的原型相关细节查看。

UUID：通常为一个16长度的标识符，具有唯一性，在Rpc通信模型中，UUID 提供对接口、管理器入口点向量或客户端对象等对象的唯一指定。

ACF：(ACF) 的应用程序配置文件有两个部分： 接口标头，类似于 IDL 文件中的接口标头，以及一个 正文，其中包含适用于 IDL 文件的接口正文中定义的类型和函数的配置属性。

2、调用过程

[RpcStringBindingCompose](https://learn.microsoft.com/zh-cn/windows/win2/api/rpcdce/nf-rpcdce-rpcstringbindingcompose "RpcStringBindingCompose")：需要先创建一个绑定句柄字符串。。

[RpcBindingFromStringBinding](https://learn.microsoft.com/zh-cn/windows/win32/api/rpcdce/nf-rpcdce-rpcstringbindingcompose "RpcBindingFromStringBinding")：通过绑定句柄字符串返回绑定句柄。

## 3、存根分配和释放内存

在编写RPC调用的时候，必须将函数MIDL\_user\_allocate和MIDL\_user\_free在项目的中定义。

## 4、相关攻击面

所有的Demo都在 <https://github.com/M0nster3/RpcsDemo> ，大家可参考。

### 1、IOXID Resolver探测内网多网卡主机

我们发送一个IOXID的传输包，这个发送方式有很多种，我这里用的K8师傅的工具，用Wireshark抓包。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123013-6c398b02-bb0e-1.png)

上图中TCP的三个包就不用看了，就是很常见的TCP的三次握手，后四个包中可以如图看，主要关注的是最后一个包，前三个都是固定的，就是交互中用来协商版本之类的参数。

1、先来构造第一个数据包，由于这个包是固定的可以直接Copy Wireshark中的，如下图

```
05000b03100000004800000001000000b810b810000000000100000000000100c4fefc9960521b10bbcb00aa0021347a00000000045d888aeb1cc9119fe808002b10486002000000
```

2、后续第二个是接受的数据包，直接将第三个包复制就可以

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123034-7894fabc-bb0e-1.png)

```
050000031000000018000000010000000000000000000500
```

3、主要就是看我们如何剖析最后一个包，将他接收过来并且进行一个分割输出，首先我们是想要枚举他的多网卡信息，和主机信息。我们对数据包进行一个分割。是从/0x07/0x00/进行分割。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123052-837de984-bb0e-1.png)

结束的是在0x09/0x00/0xff这一块结束的,把我们接受的数据进行一个分割。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123101-88632a90-bb0e-1.png)

相关代码：<https://github.com/M0nster3/RpcsDemo/blob/main/OXIDINterka_network_card/OXID.go>

效果图

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123111-8ebfc0ba-bb0e-1.png)

### 2、RPC SMB

RPC还可以通过不同的协议进行一个访问，例如通过SMB协议传输的RPC服务就可以通过管道进行访问，加入在做项目的时候又有个域凭证就可以进行一写RPC借口的一个调用，比较好用的一个工具是rpcclient，它是执行客户端 MS-RPC 功能的工具。 相关命令的一些总结我发在了[https://github.com/M0nster3/RpcsDemo/blob/main/RPC%20over%20SMB/MS-RPC.md中，大家有需要可以去提取。](https://github.com/M0nster3/RpcsDemo/blob/main/RPC%20over%20SMB/MS-RPC.md%E4%B8%AD%EF%BC%8C%E5%A4%A7%E5%AE%B6%E6%9C%89%E9%9C%80%E8%A6%81%E5%8F%AF%E4%BB%A5%E5%8E%BB%E6%8F%90%E5%8F%96%E3%80%82)

### 3、MS-SAMR的那些事

该协议支持包含用户和组的帐户存储或目录的管理功能，简单来说就是该协议主要是对Windows用户以及用户组的一些相应操作，例如添加用户，用户组等操作。[官方参考.](https://learn.microsoft.com/zh-cn/openspecs/windows_protocols/ms-samr/4df07fab-1bbc-452f-8e92-7853a3c7e380 "官方参考.")

1）添加本地用户

```
long SamrCreateUser2InDomain(
   [in] SAMPR_HANDLE DomainHandle,
   [in] PRPC_UNICODE_STRING Name,
   [in] unsigned long AccountType,
   [in] unsigned long DesiredAccess,
   [out] SAMPR_HANDLE* UserHandle,
   [out] unsigned long* GrantedAccess,
   [out] unsigned long* RelativeId
 );
```

在创建用户的时候通过分档来看，不能直接创建到内置域（Builtin）中，需要先创建到账户域（账户）中，如下图。

关于内置域和账户域的相关内容可以参考[官方链接](https://learn.microsoft.com/zh-cn/windows/win32/secmgmt/built-in-and-account-domains "官方链接").

其实简单来说就是，账户域内的用户只能访问该账户所在计算机的资源，而内置域中的账户可以访问域的资源。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123230-bd8759b2-bb0e-1.png)

由于使用SamrCreateUser2InDomain创建的账户存在禁用标识位，我们先需要为它Set一个属性，来清除禁用标识位。然后才可以将其加入到所在的内置域中。

使用SamrSetInformationUser() 这个API为它设置。

```
long SamrSetInformationUser(
   [in] SAMPR_HANDLE UserHandle,
   [in] USER_INFORMATION_CLASS UserInformationClass,
   [in, switch_is(UserInformationClass)]
     PSAMPR_USER_INFO_BUFFER Buffer
 );
```

编写脚本有两种方式一种是直接调用MS-SAMR协议去直接创建一个用户，微软官方给了[IDL](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/1cd138b9-cc1b-4706-b115-49e53189e32e "IDL")，将其编译，然后构造，这种方式调用起来比较麻烦，另一种是使用神器mimikatz打包好的包，samlib来进行调用，调用的时候将前面的samr改成sam就可以.

参考微软给的[官方例子](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/3d8e23d8-d9df-481f-83b3-9175f980294c "官方例子").

可以按照这个例子依次构造

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123321-dc0477c6-bb0e-1.png)

首先先求出来账户域Account和内置域的Builts的SID为后续添加账户以及加入到内置域中做准备。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123330-e15294b0-bb0e-1.png)

然后获取域对象的句柄，然后为域对象添加用户,并且清除禁用标识位，关键代码。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123337-e582e170-bb0e-1.png)

到这里创建用户的准备工作就结束了，接下来，就是将用户添加到组里面，用到[SamAddMemberToAlias](https://www.t00ls.com/Ihttps%3A//learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/9a5d2c35-e84b-4e59-b7b0-96c6fa0fc8d7 "SamAddMemberToAlias").

```
long SamrAddMemberToAlias(
   [in] SAMPR_HANDLE AliasHandle,
   [in] PRPC_SID MemberId
 );
```

相应的Demo：<https://github.com/M0nster3/RpcsDemo/blob/main/MS-SAMR/AddUser/AddUser/main.c>

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123406-f6b3c676-bb0e-1.png)

2) Change Ntlm
调用的关键API在[SamrChangePasswordUser](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/9699d8ca-e1a4-433c-a8c3-d7bebeb01476 "SamrChangePasswordUser") .

当我们获取到了用户名，以及密码NTLMhash，则可以是用这个API将用户的密码修改了。

```
long SamrChangePasswordUser(
   [in] SAMPR_HANDLE UserHandle,
   [in] unsigned char LmPresent,
   [in, unique] PENCRYPTED_LM_OWF_PASSWORD OldLmEncryptedWithNewLm,
   [in, unique] PENCRYPTED_LM_OWF_PASSWORD NewLmEncryptedWithOldLm,
   [in] unsigned char NtPresent,
   [in, unique] PENCRYPTED_NT_OWF_PASSWORD OldNtEncryptedWithNewNt,
   [in, unique] PENCRYPTED_NT_OWF_PASSWORD NewNtEncryptedWithOldNt,
   [in] unsigned char NtCrossEncryptionPresent,
   [in, unique] PENCRYPTED_NT_OWF_PASSWORD NewNtEncryptedWithNewLm,
   [in] unsigned char LmCrossEncryptionPresent,
   [in, unique] PENCRYPTED_LM_OWF_PASSWORD NewLmEncryptedWithNewNt
 );
```

这这里遇到了一个坑，就是只用旧的Ntlm就行修改而不对LmCrossEncryptionPresent和NewLmEncryptedWithNewNt进行传参，则会输出一个C000017F的错误，如下图。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123514-1f496f32-bb0f-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123521-238cdb6a-bb0f-1.png)

我去查看一下这个错误发现是客户端使用当前密码LM hash作为加密密钥请求返回，不清楚为什么不能用当前的密码LM hash，就改了一个其他的LM hash,关键代码。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123547-32f7f10c-bb0f-1.png)

接下来就是编写POC，我在这里使用微软官方的提供的[IDL](https://www.t00ls.com/%20https%3A//learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/1cd138b9-cc1b-4706-b115-49e53189e32e "IDL")进行编译，提供了我们需要的所有包，在我们编译好，生成exe的时候会有很多错误，直接将其都注释就好。

根据RPC的调用过程首先需要进行RPC的绑定

```
RPC_STATUS RpcStringBindingComposeW(
  RPC_WSTR ObjUuid,
  RPC_WSTR ProtSeq,
  RPC_WSTR NetworkAddr,
  RPC_WSTR Endpoint,
  RPC_WSTR Options,
  RPC_WSTR *StringBinding
);
```

其中的ObjUuid可以直接在提供的IDL中找到，如下图，但是发现这个例子有没有这个都可以，[最主要的必须定义一个命名管道端点 \PIPE\samr](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wkst/13e9ee5d-4125-4492-bcc7-9a0061f2bbe7 "最主要的必须定义一个命名管道端点 \PIPE\samr")。 关键代码

![](https://xzfile.aliyuncs.com/media/upload/picture/20230305123733-7233f37a-bb0f-1.png)

绑定了之后接下来就是构造SamrChangePasswordUser,如果我们不熟悉MS-SAMR我们可以倒着堆整个调用流程。

```
long SamrChangePasswordUser(
   [in] SAMPR_HANDLE UserHandle,
   [in] unsigned char LmPresent,
   [in, unique] PEN...