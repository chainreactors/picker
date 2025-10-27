---
title: Execute-Assembly攻守之道
url: https://www.secpulse.com/archives/198531.html
source: 安全脉搏
date: 2023-04-05
fetch_date: 2025-10-04T11:29:24.090841
---

# Execute-Assembly攻守之道

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# Execute-Assembly攻守之道

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-04-04

10,078

## 以下文章来源于红队蓝军 ，作者HaCky

## 0x01 Execute-Assembly 原理

        在《Cobalt Strike 原理分析》一文中，介绍了内存加载程序集(Assembly)的主要有四步：

> 1 加载CLR环境 2 获取程序域 3 装载程序集 4 执行程序集

        在odzhan的Shellcode: Loading .NET Assemblies From Memory所描述的那样，.Net Framework随着版本的更新，使用了不同的接口，.Net Framework V1.0 采用的是`ICorRuntimeHost接口`，支持v1.0.3705, v1.1.4322, v2.0.50727和v4.0.30319。到了.Net Framework v2.0，采用`ICLRRuntimeHost接口`，支持v2.0.50727和v4.0.30319。然后到了.Net Framework v4.0，则使用了`ICLRMetaHost接口`,但是可能不再兼容4.0以下的.Net Framework。所以使用`ICLRMetaHost接口`并不是一个非常合适的接口。

        我们可以使用多个函数进行接口的实例化，最常见的可能属`CoCreateInstance`或者`CLRCreateInstance`。

```
CoInitializeEx以及CoCreateInstance
CorBindToRuntime或者CorBindToRuntimeEx
CLRCreateInstance以及ICLRRuntimeInfo
```

        剩下的关于`获取程序域`,`装载程序集`,以及`执行程序集`在Execute-Assembly实现都有具体实现。完整代码如下。

```
#include <stdio.h>
#include <tchar.h>
#include <metahost.h>
//
#import "mscorlib.tlb" raw_interfaces_only
     high_property_prefixes("_get","_put","_putref")
     rename("ReportEvent", "InteropServices_ReportEvent")
 rename("or", "InteropServices_or")

using namespace mscorlib;
//
#pragma comment(lib, "MSCorEE.lib")
//
int _tmain(int argc, _TCHAR* argv[])
{
 HANDLE hFile = CreateFileA("CSharp.exe",
  GENERIC_READ | GENERIC_WRITE,
  FILE_SHARE_READ,
  NULL,
  OPEN_EXISTING,
  FILE_ATTRIBUTE_NORMAL,
  NULL);
 if (NULL == hFile)
 {
  return 0;
 }
 DWORD dwFileSize = GetFileSize(hFile, NULL);
 if (dwFileSize == 0)
 {
  return 0;
 }
 PVOID dotnetRaw = malloc(dwFileSize);
 memset(dotnetRaw, 0, dwFileSize);
 DWORD dwReturn = 0;
 if (ReadFile(hFile, dotnetRaw, dwFileSize, &dwReturn, NULL)==FALSE)
 {
  return 0;
 }
//
 ICLRMetaHost* iMetaHost = NULL;
 ICLRRuntimeInfo* iRuntimeInfo = NULL;
 ICorRuntimeHost* iRuntimeHost = NULL;
 IUnknownPtr pAppDomain = NULL;
 _AppDomainPtr pDefaultAppDomain = NULL;
 _AssemblyPtr pAssembly = NULL;
 _MethodInfoPtr pMethodInfo = NULL;
 SAFEARRAYBOUND saBound[1];
 void* pData = NULL;
 VARIANT vRet;
 VARIANT vObj;
 VARIANT vPsa;
 SAFEARRAY* args = NULL;
//
 //检测点1
 CLRCreateInstance(CLSID_CLRMetaHost, IID_ICLRMetaHost, (VOID**)&iMetaHost);
 iMetaHost->GetRuntime(L"v4.0.30319", IID_ICLRRuntimeInfo, (VOID**)&iRuntimeInfo);
 iRuntimeInfo->GetInterface(CLSID_CorRuntimeHost, IID_ICorRuntimeHost, (VOID**)&iRuntimeHost);
 iRuntimeHost->Start();
//
 iRuntimeHost->GetDefaultDomain(&pAppDomain);
 pAppDomain->QueryInterface(__uuidof(_AppDomain), (VOID**)&pDefaultAppDomain);
//
 saBound[0].cElements = dwFileSize;
 saBound[0].lLbound = 0;
 SAFEARRAY* pSafeArray = SafeArrayCreate(VT_UI1, 1, saBound);
//
 SafeArrayAccessData(pSafeArray, &pData);
 memcpy(pData, dotnetRaw, dwFileSize);
 //free(dotnetRaw);   //释放1
 SafeArrayUnaccessData(pSafeArray);
//
 //检测点2
 pDefaultAppDomain->Load_3(pSafeArray, &pAssembly);
 //free(pSafeArray->pvData);
 pAssembly->get_EntryPoint(&pMethodInfo);

 ZeroMemory(&vRet, sizeof(VARIANT));
 ZeroMemory(&vObj, sizeof(VARIANT));
 vObj.vt = VT_NULL;

 vPsa.vt = (VT_ARRAY | VT_BSTR);
 args = SafeArrayCreateVector(VT_VARIANT, 0, 1);

 if (argc > 1)
 {
  vPsa.parray = SafeArrayCreateVector(VT_BSTR, 0, argc);
  for (long i = 0; i < argc; i++)
  {
   SafeArrayPutElement(vPsa.parray, &i, SysAllocString((OLECHAR*)argv[i]));
  }

  long idx[1] = { 0 };
  SafeArrayPutElement(args, idx, &vPsa);
 }

 //检测点3
 HRESULT hr = pMethodInfo->Invoke_3(vObj, args, &vRet);
 pMethodInfo->Release();
 pAssembly->Release();
 pDefaultAppDomain->Release();
 iRuntimeInfo->Release();
 iMetaHost->Release();
 CoUninitialize();
 getchar();
 return 0;
};
```

## 0x02 Execute-Assembly检测思路

根据上述的Execute-Assembly的实现原理，可以预测到Execute-Assembly主要有3个检测点。第一个检测点是加载CLR环境，第二个检测点是加载程序集，第三个检测点在于执行入口点的地方。在我看来，第一第二个检测点是比较好实现的。

### 0x2.1 ETW使用前置知识

根据XPN在他的博文Hiding your .NET - ETW一文中指出利用ETW(Event Trace for Windows)检测CLR的加载。而ProcessHacker或者ProcessExplorer这两款工具都能从进程角度查看进程是否加载了CLR环境。![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198531-1680572089.png)

        使用`logman query providers`命令查看所有的提供者。如图，执行结果的第一项是提供者名称，第二项是提供者对应的GUID。![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198531-1680572090.png)

        也可以通过设置指定得`provider name`或者`GUID`来获取具体的提供者的详细信息。即使用`logman query providers <provider name>`或者`logman query providers <GUID>`。

        通过执行`logman query providers ".NET Common Language Runtime"`语句返回的结果如下。除了具有第一部分提供程序的名称和GUID之外，第二部分是一些关键字的信息，也就是筛选事件的标志。通过设置这些标志来筛选我们所需要的事件。第三部分是安全级别，而第四部分对应的是事件对应的进程ID和进程路径。

```
PS C:Users14349> logman query providers ".NET Common Language Runtime"

提供程序                                 GUID
-------------------------------------------------------------------------------
.NET Common Language Runtime             {E13C0D23-CCBC-4E12-931B-D9CC2EEE27E4}

值                   关键字                  描述
-------------------------------------------------------------------------------
0x0000000000000001  GCKeyword            GC
0x0000000000000002  GCHandleKeyword      GCHandle
0x0000000000000004  FusionKeyword        Binder
0x0000000000000008  LoaderKeyword        Loader
0x0000000000000010  JitKeyword           Jit
0x0000000000000020  NGenKeyword          NGen
0x0000000000000040  StartEnumerationKeyword StartEnumeration
0x0000000000000080  EndEnumerationKeyword StopEnumeration
0x0000000000000400  SecurityKeyword      Security
0x0000000000000800  AppDomainResourceManagementKeyword AppDomainResourceManagement
0x0000000000001000  JitTracingKeyword    JitTracing
0x0000000000002000  InteropKeyword       Interop
0x0000000000004000  ContentionKeyword    Contention
0x0000000000008000  ExceptionKeyword ...