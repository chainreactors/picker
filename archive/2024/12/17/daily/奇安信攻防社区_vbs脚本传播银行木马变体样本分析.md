---
title: vbs脚本传播银行木马变体样本分析
url: https://forum.butian.net/share/3937
source: 奇安信攻防社区
date: 2024-12-17
fetch_date: 2025-10-06T19:36:06.409552
---

# vbs脚本传播银行木马变体样本分析

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

### vbs脚本传播银行木马变体样本分析

样本分析
VBS 第一阶段
第一阶段是一个高度混淆的独立vbs脚本，它会将包括恶意样本在内的其他有效负载下载到系统上。
vbs脚本前面定义了三个变量，之后重新构造变量，重新组合后，NbCTQqd的值...

样本分析
====
VBS 第一阶段
--------
第一阶段是一个高度混淆的独立vbs脚本，它会将包括恶意样本在内的其他有效负载下载到系统上。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-3ee1a78a9ae1c9992ec38cb662e2b48b3895b784.png)
vbs脚本前面定义了三个变量，之后重新构造变量，重新组合后，`NbCTQqd`的值为：
```vbs
wscrilqpt.exe //E:vbscript
```
之后通过`CreateObject("Scripting.FileSystemObject")`创建文件系统对象。
接着做了一个路径生成，最终生成的路径是`"C:\Users\[User]\AppData\Local\Temp\tmp123454321pmt.txt"`，往下`CreateTextFile` 创建一个新文本文件。
接着下面全是混淆，借助vs解混淆可以得到完整的内容：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a61517fdba29087c8d7d1a70f4669cd7ef64c10a.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-79a7df5f2922c8d756f5b28704975314c00db817.png)
脚本从提供的URL中下载 pyaloads，并使用 rundll32.exe 执行下一阶段恶意软件，即恶意样本的主体。
Emotet DLL
----------
DIE检查它是一个32位的DLL文件。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-29a340082e9080e5b95d2168cb82e42469c0c093.png)
这里调试使用“rundll32.exe”进行加载。`Parameters`选项用于指定指定程序在启动或调试时所需要的命令行参数，这里使用参数`Control\_RunDLL`。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7cf30afe411980568175287df5a790bb752edb07.png)
一旦该恶意样本文件被“rundll32.exe”加载，它的入口点函数就会被首次调用。然后，它会调用 DllMain() 函数，从“资源”中加载并解密 32 位 Dll 到其内存中。解密的 Dll 是这个恶意样本的核心，由于其中包含一个硬编码的常量字符串，因此在本分析中将其称为“X.dll”。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9154f068328cb19a9f4cb83f28f977002f568865.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7d6b433561ed5059c8f893a80d6715f22e17c656.png)
通过System informer可以找到该进程内存的x.dll。
"X.dll"检查命令行参数中的导出函数名称是否为"Control\\_RunDLL"。如果不是,它会再次使用"Control\\_RunDLL"而不是其他导出函数(如"C:\\Windows\\syswow64\\rundll32.exe emotet.dll,Control\\_RunDLL")运行命令行。然后,它会调用ExitProcess()退出第一个"rundll32.exe"。如果初始DLL尚未加载ControL\\_RunDLL,它会使用API CreateProcessW()运行新命令。
可以借助内存转储工具将X.dll dump出来。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f99ee123ce1ce2ec21cb34a48be05006b477e5bd.png)
X.dll
-----
我们可以进一步使用转储的 x.dll，并根据当前正在调试的程序重新设置程序，并将导出映射到正在调用的函数。例如，调用 eax 跳转到 x.dll 中的 Export Contro\\_RunDLL，该 DLL 映射如下图所示：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-cd2cfbeb174ac9966603e48ec5e38605b6b1d048.png)
从x.dll的`Contro\_RunDLL`开始,为了方便这里将其重命名为`Contro\_RunDLl\_xdll`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-38a6073e9e371dd6eadfe8451664953a0f510e35.png)
在函数`sub\_1001FCD8`的图形视图中可以发现,下。x.dll使用了控制流平坦化的操作,将代码进行了高度混淆。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e6e6ec4d87fd2c6ee46b28358b38805af4af1d63.png)
可以通过给指定函数内的所有调用指令（`call`）添加断点。
idapython代码如下：
```python
import idautils
import idaapi
import idc
def add\_breakpoints\_on\_calls(func\_name):
# Get the function address by name
func\_ea = idc.get\_name\_ea\_simple(func\_name)
if func\_ea == idc.BADADDR:
print(f"Function {func\_name} not found!")
return
# Get the function's end address
func = idaapi.get\_func(func\_ea)
if not func:
print(f"Function {func\_name} not found!")
return
# Iterate through the instructions in the function
for head in idautils.Heads(func.start\_ea, func.end\_ea):
# Check if it's a call instruction
if idc.print\_insn\_mnem(head) == "call":
# Add a breakpoint at the call instruction
idc.add\_bpt(head)
print(f"Breakpoint added at 0x{head:x}")
print(f"Breakpoints added on all call instructions in function: {func\_name}")
# Example: specify the function name where you want to add breakpoints
add\_breakpoints\_on\_calls("Flatten\_func") #Flatten\_func is the "code flow flatenning function that i renamed"
```
给函数`sub\_1001FCD8`重命名为`Flatten\_func`，可以得到：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-003a2ef9f61c39a9a49d7393406d6faad42e5c51.png)
### 字符串混淆
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-146cc5d50be0fa948f5cbe6594ef9391f154b868.png)
所有字符串均在x.dll中加密，并在运行时解密。它会解密恶意软件中加载的所有附加库的名称。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-bd9942fea86fbed30bb1ee5df68edfe76cac9196.png)
### API解析
所有 API 都是动态加载的，以避免在静态分析中被检测到。在上面的例子中，我们看到“advapi32.dll”的字符串被解密。在此函数中，它将使用 API `LoadLibraryW`加载并执行。函数`resolve\_func`负责解析 API 哈希并在比较哈希后返回 API 地址。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-42e930f716b603b6f1f21453ed4c98c3db943b99.png)
从这里开始，所有 API 都使用 API 哈希解析并执行。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-26afa8b6927d2881b0ad14e53866505a6612f4b5.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9ca112eb71f7a5528bbb4acb5f111704f5a23600.png)
它首先检查的是命令行参数，以查看 dll 是否已使用`Control\_RunDLL`参数执行以及执行路径。如果恶意软件不是从%AppData%执行的，那么它会将自身移动到 Appdata 中的安全位置。
它涉及下列windows api
- SHGetFolderPathW 获取 `%Appdata%` 的路径。
- GetCommandLineW 检查命令行参数和路径。
- CreateFileW 获取自身的文件句柄。
- GetFileInformationByHandleEx 获取自身的文件信息。
- GetTickCount 生成随机名称。
- SHFileOperationW 复制文件。
- DeleteFileW 删除复制文件的 Zone 标识符。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a92eec9d6aff975fe42f1415e00d8c8e5fdca9ec.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8dd801f448c4b8e214f181478b58b7a1201c97ab.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c8f73381c0253c71498bfecc33e0b85be7024ae8.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e167fbf2496f32e5864491ce914fda439bb41579.png)
当恶意软件被转移到其他位置后，它会再次使用 rundll32.exe 执行自身，从而删除原始文件。再次执行自身所使用的 API 如下：
- CreateProcessW 该表情符号再次使用 rundll32 在 %appdata% 中新保存的 dll 执行
- ExitProcess 退出第一个进程
x.dll的行为会根据执行位置而改变。如果从 %Appdata% 执行，它会继续执行；但如果从其他路径执行，它会更改位置并重新加载。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8db7630e0c1a53087e8b27567cb487a7016e1343.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1e065939d3fbc263eb0fa98cb1cf28101e17168f.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9c683a93532083f6831570977bb3537413f6c1e5.png)
### 信息收集
最后一个阶段的恶意软件将 x.dll 复制到 %appdata% 本地文件夹中，文件夹名称和文件名均为随机的，并添加了 `.xnj` 扩展名。在此阶段，我将再次使用带有参数 `Control\_RunDLL` 的 `rundll32` 执行 dll，并进一步调试其行为。
它首先对 kernel32 和 ntdll 位置进行常规 PEB 遍历，然后查找 `LoadLibraryW` 和 `GetProcAddress` 的地址。然后，它加载所需的所有模块，并首先检查执行文件路径和模块名称。如果一切正确，它会收集系统信息以制作请求并将机器人注册到 c2 服务器。
- GetComputerNameA 获取受害系统的名称
- GetWindowsDirectoryW 获取安装系统文件的 Windows 目录
- GetVolumeInformationW 获取音量信息
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e73297dad5383194917c407b54023079744d34e3.png)
### 文件删除
当恶意样本尝试删除 %AppData% 中主目录中存在的所有额外文件时，我们发现它有独特的行为。除了主 emotet dll 之外，它还会删除目录中的所有其他文件。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-bc3eab1699ea1fb2732a15efbe84a7fa64e9e9d6.png)
如上图所示，它正在尝试删除名为 cdomcinc.xnj.id0 的 ida 文件。
### 加密密钥
样本使用椭圆曲线密码 ECDH 密钥来建立加密密钥。生成的 ECDH 私钥和嵌入的 ECDH 公钥与 `BCryptSecretAgreement` 函数一起使用，在恶意软件和 C2 之间生成共享密钥。使用 `BCryptDeriveKey` 函数从共享密钥中派生出 AES 密钥。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b71889eccb0ff2584c366b851f604a805060575c.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2089d21e3496dc619f...