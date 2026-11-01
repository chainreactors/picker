---
title: 仿冒 CCleaner 投递 GhostDesk 木马
url: https://mp.weixin.qq.com/s/k671VHF4cB4YmTvf1dxcmQ
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:19:45.767246
---

# 仿冒 CCleaner 投递 GhostDesk 木马

# 仿冒 CCleaner 投递 GhostDesk 木马

ZyOrca
ZyOrca

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

近期有威胁情报检测到伪装成知名系统清理工具 CCleaner 的恶意软件。攻击者搭建了仿冒的官方网站（ccleanerwind[.]top ），诱导受害者下载伪造的安装程序 CCleaner.exe 。该程序安装运行后，会进行 DLL 侧加载、无文件内存加载、用户态 Rootkit 等操作，并最终以 Chrome 浏览器的恶意扩展落地，目的在于监控和窃取受害者的敏感信息，包括加密货币钱包地址。（下文记录了多次调试，可能存在PID、内存地址前后不一致的地方，见谅）

# 1. DLL 侧加载和持久化

CCleaner.exe 安装运行后，向 %APPDATA%\Microsoft\Vault 路径写入三个文件

* cscript.exe（微软的脚本运行工具，白文件）
* version.dll（恶意加载器，会读取AppxState.dat）
* AppxState.dat（加密的 Payload）

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0hFibtVO8ZdaLr4Gf6zNzvLV74gnK4ftyyicfV276zAJnrscqY9Dh8FVPht2Fl724n1bgpIC2TXCkUyQnpsgANsUN24o15mCfx4/640?wx_fmt=png&from=appmsg)

接着 CCleaner.exe 会创建进程，运行 cscript.exe。 cscript.exe 进程被拉起后，加载 version.dll ，立即扫描同目录下的 .dat 文件，找到 AppxState.dat 后读取。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2QXINQGdnXZO513Ytyw1l6H9wmw829UwILt9icYYx7icNia9ts1TJwA9A6eqwTpKcxga917PxHPgMg9lEIiafckn1oJk4icbdXdEbM/640?wx_fmt=png&from=appmsg)

cscript.exe 读取 AppxState.dat 后，会将注册表 Environment\UserInitMprLogonScript 的键值设置为 cscript.exe 所在路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1AkwTXBARjOrDfW70HP9eLGtekbA9MH2IuzhUiaibEgibqwVsiaV2JDYOFy155KrvmwibmPQEwtBpmB2siaayMsZYdibnpibfFIaWsXRk/640?wx_fmt=png&from=appmsg)

当用户登录 Windows 时，进程 winlogon.exe 会启动 userinit.exe 初始化用户环境。userinit.exe 会自动检测 HKCU\Environment 下是否存在 UserInitMprLogonScript。若存在该项，userinit.exe 会以后台方式静默启动该项中指定的程序或脚本（如 .bat、.vbs、.ps1 或恶意 exe/cscript.exe 等）。与Run 键设置相比，这种方式更为隐蔽地实现了恶意程序的开机自启动

# 2. version.dll 侧加载

## 2.1 获取函数地址：TpAllocWork 和 TpPostWork

IDA 查看 version.dll，看到开始部分有函数 DisableThreadLibraryCalls，这个是 kernel32.dll 的导出函数； x64dbg 调试cscript.exe，程序加载 version.dll 后，先在这个函数下个断点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K01H7BMxLHiaYWPBNcJe4UUiaHdGeyb1pRZTN2qLuUGJ0QwicFd8YBKA3FMFmQMAIuqCSU8DNrbPdtXTOsZbWex3kWoXpSMIk1axw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2vGDyTTyCRm7UibGYg8OHBqGv8N5TAdsubHLYd1lZnWAEWqoTiaFDPkuD439LGJ7DOjTqUdSp7n6MmKFyeZRXcQmHbiaopL2s3F0/640?wx_fmt=png&from=appmsg)

成功断了下来，接着往下单步运行，可以看到函数 GetModuleHandleW()
获取 ntdll.dll 句柄后，可以看到接下来应该是解密某个函数名称，再通过 GetProcAddress 获取这个函数地址。

再往下运行，验证了猜想。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3cefbsokZ1Sa02Usjmb23dic466Z12Asoic4ibTm9fwWXKyRXtw4qKtHXxB7Z3XBVNmhXjdYmWWL2S3Aj57lWUmFOmd8Ta3AEwOg/640?wx_fmt=png&from=appmsg)

先是获取了 ntdll!TpAllocWork 和 ntdll!TpPostWork 的函数地址并保存在 rsi 和 rdi 这两个寄存器当中，然后调用了这两个函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3HquibFON3QfibGTZHKoibHqqibFZMniaMSSv5FXmX66Noicp0w8G878noOIon0xVmRMVicPJpJAKk0ibKh5JTm61SJE3iaWa7bQX4DbxQ/640?wx_fmt=png&from=appmsg)

## 2.2 线程池注入

ntdll!TpAllocWork 和 ntdll!TpPostWork 函数的调用是很明显的线程池注入特征。使用 CreateThread 太容易引发 安全软件的告警，攻击者选择利用线程池机制，更隐蔽一点。

```
NTSTATUS NTAPI TpAllocWork(
    PTP_WORK*            WorkReturn,        // RCX：返回创建好的work对象指针
    PTP_WORK_CALLBACK    Callback,          // RDX：当 work 激活时，要调用的函数地址
    PVOID                Context,           // R8 ：传给 Callback 的参数
    PTP_CALLBACK_ENVIRON CallbackEnviron    // R9 ：环境控制
);
```

TpPostWork 执行后，操作系统内置线程池中一个已存在的休眠 Worker 线程被唤醒，读取回调函数地址（即 sub\_1800035C0，动态调试界面中 RDX 保存的地址 0x00007FFF6C3035C0）并直接跳转执行。

这个线程的入口是合法的线程池调度器，引发告警的可能性要小一点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2iaJKNsdQYBqZAITkbXOxAly0LhRY2VQRGfoPSpu04WlsKcRKD28VS0nfhibNIlAVWyQiaqmeiay9Cb0nA43GclnqkvshVk5atXU4/640?wx_fmt=png&from=appmsg)

## 2.3 执行恶意回调函数

在 0x00007FFF6C3035C0下断点，成功断了下来

调用 Sleep(0x64)（100毫秒）
调用 GetCurrentProcessId() 获取宿主（cscript.exe）的 PID
调用 EnumWindows(EnumFunc, CurrentProcessId)

EnumFunc 遍历所有顶级窗口，找到属于当前 PID 的窗口后，调用 ShowWindow(hwnd, SW\_HIDE)，将 cscript.exe 的黑框控制台窗口隐藏（这个可以在桌面观察到）

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1GT37BkMSiag3XT7dOny7xTbbpVQg0Na3YmZ93bTNK1c0db81xKz8nowUiaicwqNrovphCibCvjsqlBUGYaAiaKVkFqsFvj3Y8De8Y/640?wx_fmt=png&from=appmsg)

## 2.4 读取 Payload，内存加载恶意 dll

接下来获取文件所在路径，找到后缀为.dat 的文件，调用 readfile() 函数读取文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K245fWLZx2WHzIm5DWiaB0QrYEy9IDfdVAAibTH4ICSBTCHYg60eg3VcsaQGDhCePJJ7DM85DLkhhSicIKDFQMct3XB2zytZXmAD0/640?wx_fmt=png&from=appmsg)

然后调用 Windows 的 BCrypt 密码学库，对文件进行哈希校验和解密

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K12FSh4k5GbGfjSFxbc91MKjBfEKrtl4eWhzgeV7HMST3x9OdS1UKD8qon8pSYwgGjxwWcy4YD1tcImwH0XDNicXBMnPJtAYxE8/640?wx_fmt=png&from=appmsg)

最后通过修改内存属性（VirtualProtect）并冲刷指令缓存（FlushInstructionCache），直接在内存中执行dll

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3roZUV8qicqycicraWBNLxicBjdBlzhukXyMK31rRDM0gml0HJnJDfql9cQld4gEmcCnNteswDSBrLQc6licoylwC5YMmoBoSh01U/640?wx_fmt=png&from=appmsg)

sub\_1800010F 函数实现在内存中加载恶意 PE 文件

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1rGwV8j3tv2epQoe8wb8Wic2V2c9s32rrfSLeXFy5zEpzQr4F6RCNicHtxd5ICcmdxokRynpicWo3PiaEf4zwM5KqSdjEjFY7BSg8/640?wx_fmt=png&from=appmsg)

调试时，可以看到内存地址 0x24C0000 有解密后的 PE 文件

# 3. 内存加载的 dll

## 3.1 dll 执行入口

将内存中加载的 dump 下来，是一个dll 文件，IDA 看一下，导出函数名为SynTPEnhService\_1()。

> `SynTPEnhService` 是 Synaptics 触控板服务的 API 名称，攻击者将载荷导出为同名函数，可能会骗过一些安全软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0cu53wefkdjlYMNtVFN7RIWcEosM6SqsGnia2XrDyGcCOWKEg42Zmlf3qho3I4FoDaoYlN0NPdv0GXFVU2gnic5Qh6ZNV16RnnY/640?wx_fmt=png&from=appmsg)

暂且命名为 SynTPHelper.dll，然后继续动态调试；搜索内存加载 dll 关键函数结尾的部分，看到 call rax ，version.dll 的基址+0x149A，像是比较明显的 Payload 执行入口。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1XjQ5hIYnNTLFa2c58rzus9dA6a9wz3jV0LN4SVKaY1DH0MUDyW5TITJ35quVlYSh329rW36gkd10ibTWPQvnk2vCiaia5vAQpKg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0UoRagturdH9CicvuQTFr6Z9ffUmLRsvKEFywAdvtDwDw3V1v7ULMjD4cia3tGD9d2pawlltwrjyzJUIP3oKpnt2kb0c9FwMM70/640?wx_fmt=png&from=appmsg)

```
mov eax, dword ptr ds:[rbx+28] ; 1. 取出入口点相对偏移 (RVA)
xor r8d, r8d                    ; 2. 第 3 个参数 R8 = 0 (lpReserved)
mov rcx, qword ptr ss:[rbp+40]  ; 3. 第 1 个参数 RCX = 新模块基址 (ImageBase)
mov edx, r14d                   ; 4. 第 2 个参数 RDX = 1 (DLL_PROCESS_ATTACH)
add rax, rcx                    ; 5. RAX = 新模块基址 + 入口点偏移 (计算出真正的入口地址)
call rax                        ; 6. 核心：正式调用解密后木马的 DllMain
```

## 3.2 创建文件 runtimebroker.dll 和runtimebroker.cfg

然后步进，在函数LoadLibraryW 设置硬件断点，在加载 runtimebroker.dll 断下来

```
bphws kernel32.LoadLibraryW, "x"
```

payload 运行后，可以观察到，实现了持久化机制，创建了文件 runtimebroker.dll 和runtimebroker.cfg

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2TfDIlmchVibt9Sj6q44yEUnJIl2a4eiavYkXzKiabqxTEjqm2xGmcxaCckH43ic5os9dZbLHbAse9QrQicQaLJ7wIxnzhibEG2tPL0/640?wx_fmt=png&from=appmsg)

runtimebroker.cfg 其中的内容为

```
7788
syntphelper
syntpmonitor
onedrivesync
```

# 4. 用户态 Rootkit

## 4.1 创建多个线程

解密后的核心载荷一经 call rax 启动，在 14:25:07 这一秒钟内，突然暴增了十几个相同堆地址入口的线程，负责剪贴板文本监控、网络监听等功能

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K28ia3q6ASwtVcRaPu8SpnlAKyM7GxqFse1xbOVTI7eTqRkbhRP0zBcnD5HWCcDyoE0HgOvVyIdmeyZfu1iaCORpCUaIVaIJ2GcM/640?wx_fmt=png&from=appmsg)

## 4.2 加载 runtimebroker.dll

接着运行，来到了runtimebroker.dll 的入口处

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K19W8B9Euh87xCRoKFicPT8h9mqS9wHfKTiaFvy7MAicocERYeMNcQjmsfvYKFw1ic4zNCQX7C6PyAM7tMvByaf8P14ic2icCLCQx5icw/640?wx_fmt=png&from=appmsg)

下硬件断点

```
bphws user32.GetLastInputInfo, "x"
```

### 4.2.1 API hook

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2ic8yo9Qef8JxIyTe7OmlSoicBfWo2Zoeeib467VFyibPUfdJ7b9CZiaMN1qIvQL6m0G9MGgDcH8mmIGqO6c04KVhicFHWVCTckt2JI/640?wx_fmt=png&from=appmsg)

以下是 hook 的 API

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K04e2JaiaJ8EHB5dCmoFbOtYk9dTgdxF6eFEBiakBSibsx6XUnE7Via1X2zfLGgbG3WmuTttjpqFn0sRP7alcQibBRHU5pGNAOk3qXY/640?wx_fmt=png&from=appmsg)

断下来之后，查看NtQueryDirectoryFile 处的指令，最开头的 5 个字节不再是原本的 mov r10, rcx / mov eax, 32h，而是被强制覆写成了一条跳转指令 jmp 7FFF36A10238，这是比较明显的钩子特征。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3mcsLd46KqT84ATnUaf9peMWqbE35426wY9tjUNgZNBg0WSxNBU2sal9to4PbzdwSnfHnXPKyKuCB2dVicXiaCf2ghibvemwPQ5g/640?wx_fmt=png&from=appmsg)

```
GetCurrentThreadId() 检查是否在安装线程
GetThreadContext(thread, &Context) 获取所有活跃线程 RIP
检查 RIP 是否在目标函数 ±96 字节范围内，防止打断正在执行该函数的线程
VirtualProtect(PAGE_EXECUTE_READWRITE)，使代码页可写
写 E9 JMP 补丁 / 清空原指令为 0xCC ，安装钩子
VirtualProtect 恢复原保护属性
FlushInstructionCache() 清空 CPU 指令缓存
Resum...