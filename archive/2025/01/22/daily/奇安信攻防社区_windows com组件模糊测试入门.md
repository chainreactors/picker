---
title: windows com组件模糊测试入门
url: https://forum.butian.net/share/4060
source: 奇安信攻防社区
date: 2025-01-22
fetch_date: 2025-10-06T20:04:34.547416
---

# windows com组件模糊测试入门

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

### windows com组件模糊测试入门

windows com组件模糊测试入门
什么是windows com组件
com全称是Component Object Model，即组件对象模型。按照微软官方的说法，COM 是一个平台无关的、分布式的、面向对象的系统，用于创建可交...

windows com组件模糊测试入门
===================
### 什么是windows com组件
com全称是\*\*Component Object Model，即组件对象模型。\*\*按照微软官方的说法，COM 是一个平台无关的、分布式的、面向对象的系统，用于创建可交互的二进制软件组件。COM 是微软 OLE（复合文档）和 ActiveX（互联网组件）技术的基础技术。
Windows COM（Component Object Model，组件对象模型）的历史可以追溯到1993年，当时它被引入以支持对象链接和嵌入（OLE）2.0。COM最初是为了实现不同应用程序间的对象重用和交互而设计的，它定义了一套二进制接口标准，允许不同编程语言编写的软件组件在运行时进行交互。COM 是 Windows 系统中的核心技术，被广泛应用于操作系统、应用程序、脚本引擎、系统服务等多个方面。
### windows com组件的应用
com组件在整个windows系统的应用非常广泛，包括但不限于如下：
1. Microsoft Office 系列
Office 应用（如 Word、Excel、PowerPoint）提供了丰富的 COM 接口，允许第三方程序进行自动化操作，例如通过 VBA（Visual Basic for Applications）脚本控制 Office 应用
2. Internet Explorer (IE) 和 ActiveX 控件
ActiveX 控件 是一种基于 COM 的组件技术，主要用于浏览器插件、嵌入网页内容等，例如，IE 浏览器中用于视频播放、数据可视化的插件往往是基于 ActiveX 实现的。
3. 多媒体应用 DirectX（Microsoft 的多媒体图形 API）是基于 COM 设计的，特别是 DirectShow 和 Direct3D。DirectShow 通过 COM 接口处理音频、视频流，例如视频解码和播放。
### windows com组件的激活方式
com组件 提供了多种激活模型以适应不同的应用场景。根据 COM 组件的部署和运行位置，激活方式分为以下三种类型
1. local local 激活是指 com组件作为独立的可执行文件exe运行。客户端与组件通过本地进程间通信即IPC的方式进行交互。比如office上的公式编辑器组件就是local方式激活的。
2. remote
Remote 激活是指 COM 组件在远程计算机的进程中运行，客户端通过网络与远程组件进行交互，Remote COM 使用 DCOM（Distributed COM）实现跨网络的对象激活和通信。
3. in-process In-Process 激活是指 COM 组件作为动态链接库（DLL）加载到调用方客户端进程的地址空间中运行，客户端进程和 COM 组件共享相同的内存空间，调用时可以直接通过内存指针访问对象方法。比如浏览器加载的 ActiveX 控件通常是 In-Process COM 组件。
### windows com模糊测试工具
当前主流的com模糊测试工具有[ComRaider](http://sandsprite.com/iDef/COMRaider/index.html)、[axman](https://github.com/hdm/axman)、[dranzer](https://github.com/CERTCC/dranzer)等，由于ComRaider以及axman都需要人工操作，为了方便进行自动化测试，这里使用dranzer作为com模糊测试工具。
### windows com应用开发
为了确认dranzer这款工具对普通的com应用程序是否有效，这里笔者自己编写了一个简单的存在漏洞的com应用，利用vs studio的ATL模板可以较快的开发com程序。代码目录如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-e313fe34bd3e0c7b56a297cd69177e23eacc358e.png)
在temp.h头文件种实现了Ctemp类
```php
class ATL\_NO\_VTABLE Ctemp :
public CComObjectRootEx<CComSingleThreadModel>,
public CComCoClass<Ctemp, &CLSID\_temp>,
public IDispatchImpl<Itemp, &IID\_Itemp, &LIBID\_atl1Lib, /\*wMajor =\*/ 1, /\*wMinor =\*/ 0>
{
public:
STDMETHODIMP Number(LONG num, LONG\* result);
Ctemp()
{
}
DECLARE\_REGISTRY\_RESOURCEID(106)
BEGIN\_COM\_MAP(Ctemp)
COM\_INTERFACE\_ENTRY(Itemp)
COM\_INTERFACE\_ENTRY(IDispatch)
END\_COM\_MAP()
DECLARE\_PROTECT\_FINAL\_CONSTRUCT()
HRESULT FinalConstruct()
{
return S\_OK;
}
void FinalRelease()
{
}
public:
};
```
其中创建了一个Number成员函数，该成员函数一旦被调用即可触发程序崩溃，函数实现如下：
```php
#include "pch.h"
#include "temp.h"
STDMETHODIMP Ctemp::Number(LONG num, LONG\* result)
{
\*(result-0x3000) = num + 1;
return S\_OK;
}
```
同时配置好对应的idl和rgs文件，即可将目标项目编译为一个dll。
```php
HKCR
{
atl1.temp.1 = s 'temp class'
{
CLSID = s '{f2207b67-b76a-4a7a-842a-e86bce5f8802}'
}
atl1.temp = s 'temp class'
{
CurVer = s 'atl1.temp.1'
}
NoRemove CLSID
{
ForceRemove {f2207b67-b76a-4a7a-842a-e86bce5f8802} = s 'com object test'
{
ProgID = s 'atl1.temp.1'
VersionIndependentProgID = s 'atl1.temp'
ForceRemove Programmable
InprocServer32 = s '%MODULE%'
{
val ThreadingModel = s 'Apartment'
}
TypeLib = s '{6fa318af-3697-456f-8fef-c5018359865b}'
Version = s '1.0'
}
}
}
```
```php
import "oaidl.idl";
import "ocidl.idl";
[
object,
uuid(f1fa2254-8654-4746-8afd-544b71000e26),
dual,
nonextensible,
pointer\_default(unique)
]
interface Itemp : IDispatch
{
[id(1)] HRESULT Number([in] LONG num, [out, retval] LONG\* result);
};
[
uuid(6fa318af-3697-456f-8fef-c5018359865b),
version(1.0),
]
library atl1Lib
{
importlib("stdole2.tlb");
[
uuid(f2207b67-b76a-4a7a-842a-e86bce5f8802)
]
coclass temp
{
[default] interface Itemp;
};
};
import "shobjidl.idl";
```
编译成功后还需要对该dll进行注册，在管理员权限下，使用`regsvr32.exe atl1.dll`即可进行注册
注册成功后可以在注册表下观察到对应的CLSID项：
![image 1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-5e75239cff23bdae1c75b8c1a45ff9abc330f66e.png)
这样就可以通过CLSID来对该com应用进行加载，利用dranzer的遍历当前可测试的com组件的功能，也可以找到该com应用。
![image 2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0975f29de732c71cee26ec2cf2266231595bbea6.png)
### Dranzer测试
查看下dranzer的参数如下：
-o &lt;outputfile&gt; - Output Filename
-i &lt;inputfile&gt; - Use input file CLSID list
-d &lt;notestfile&gt; - Use don't test CLSID List
-g - Generate base COM list
-k - Generate Kill Bit COM list
-l - Generate Interface Listings
-b - Load In Browser (IE)
-t - Test Interfaces Properties and Methods
-p - Test PARAMS (PropertyBag) in Internet Explorer
-s - Test PARAMS (Binary Scan) in Internet Explorer
-n - Print COM object information
-v - Print out version information
-r - Generate Kill Bit registry files
这里我们主要用到-t参数，该参数意味着对目标com应用测试其属性和方法。将可测试的CLSID列表保存为一个文件，利用`dranzer -t -i clsids.txt` 命令让dranzer对该文件内的com组件进行模糊测试。为了能够尽快发现atl1.dll中的漏洞，这里准备了下面的文件作为测试目标：
![image 3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-437ac15a321845f40cb6b831c4a899a86747d523.png)
但是经过测试发现此时的dranzer并不能对笔者开发的com应用直接进行fuzz，原因未知，接下来需要对dranzer的代码进行分析来寻找fuzz失败的原因。
### Dranzer分析
对dranzer的代码进行分析，经过初步的参数解析以及一些初始化工作后，创建了一个线程用于后续fuzz，
![image 4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-037df42b227166f31da6d349b5c66abf0510efae.png)
当前我们传递了待fuzzing的com组件文件，`COM\_TestThreadProcInputFile` 函数会读取每行的CLSID值，并根据该值来获取对应com组件的信息，
![image 5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-7da4d55966ff15cb50d7f34652fc3908e75a2daa.png)
后续会根据`ExecutionMode`这个变量的值来决定执行后续的代码分支，由于我们传递的参数为-t，因此此时ExecutionMode的值为TEST\\_INTERFACES，如下：
![image 6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-984d8fb8abadc1c29a25424e42e41a0f34a97a27.png)
此时会进入到`TestCOMObject` 这个函数中，该函数主要调用了另一个项目TestAndReport中的二进制程序，如下：
![image 7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9e3f0854188aa31b3b7c20b41d5922302ce09082.png)
分析到这里可以发现dranzer起到一个转发的作用，真正对目标com组件进行测试的功能位于`TestAndReport` 项目中，在t\\_main函数中，对com库进行了初始化，如下：
```php
CoInitialize(NULL);
sprintf(TempTextBuffer,"\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\r\n");
WriteText(hLogFile,TempTextBuffer);
if (ExecutionMode==TEST\_CONTROL)
{
sprintf(TempTextBuffer,"Testing COM Object - %s %s\r\n",CLSID\_String,CLSID\_Description);
}
else if (ExecutionMode==IE\_LOAD)
{
sprintf(TempTextBuffer,"Loading COM Object in to IE - %s %s\r\n",CLSID\_String,CLSID\_Description);
}
```
在TestAndReport程序中，当前的ExecutionMode为TEST\\_CONTROL，此时会调用`TestCOM\_Object` 函数，发现dranzer会检测当前com组件的IObjectSafety接口，如果该com组件没有实现对应的IObjectSafety接口，即跳过对当前com组件的fuzzing。
![image 8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-d8d761f3c9e338e62316b1731d32fc8dd31e559e.png)
`IObjectSafety` 接口是微软定义的一个标准接口，用于控制和查询 COM 组件的安全性设置。它主要用于 ActiveX 控件和其他 COM 组件，以确保这些组件在不同的环境中如 Web 浏览器能够安全运行。如果pIObjectSafety为空，则认为该组件不是activex组件，因此会跳过对该组件的fuzzing过程。为了让dranzer能对普通的com组件也可以fuzz，修改这部分逻辑即可。修改后发现可以针对普通的com组件进行fuzzing，fuzzing时的输出如下：
![image 9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-ac60f43edff329dc6584d5926344b5d68ca91149.png)
在对atl1.dll进行简单的测试后就发现了问题，输出如下：
![image 10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-bc4ac12ad2d0f7e6c103def28f4be4fbed8a6059.png)
从上图可以看出出现问题的目标文件以及具体的调用函数，可以尽快帮我们定位漏洞。
### 结束
经过初步的测试，目前dranzer作为一个简单的com组件fuzzing工具是合...