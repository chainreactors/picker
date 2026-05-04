---
title: 【漏洞】RedSun复现
url: https://mp.weixin.qq.com/s/orGyVntLp8aM1_BH-R2eug
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:26:47.516131
---

# 【漏洞】RedSun复现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bz5OjA3RpuicrSAWVKoNhDkIdEf7XhbMOHl7mre5B9qtiavE7S6eodYFMyPsU4NxflFIUS4vu8exOUq9Wosv08Cn7M8xHQuEFDNaAc0U9vYcg/0?wx_fmt=jpeg)

# 【漏洞】RedSun复现

原创

joe1sn
joe1sn

不止Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> CVE-2026-33825又名RedSun，Microsoft Defender 中访问控制粒度不足，允许获授权的攻击者在本地提升权限。[1]

> 当 Windows Defender 识别出某个恶意文件带有“云标签”时，出于某种极其愚蠢且荒谬的原因，这款本该负责防护的杀毒软件竟然会自作聪明地决定：把刚刚发现的这个文件原封不动地重写回其原始位置。而这个 PoC 正是利用了这一反常行为，通过覆盖系统文件来获取管理员权限。[2]

![image-20260502145007748](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3Rpu8EhdaoOzFbM28UWGH5s6DdvPElKzdNCyahGrib9Jn50f2loACzJwXKEGX1SMsbrMd2ibcoWFRU9lNNVibk4G8TbkMXDViaicQznzDE/640?wx_fmt=png&from=appmsg)

**PoC地址**

* 原始PoC[1]: https://github.com/Nightmare-Eclipse/RedSun/
* cmake的自制PoC:  https://github.com/Joe1sn/CVE-2026-33825

# 前置知识

## Windows 对象管理器

Windows 内核维护一个全局的**分层命名空间**，管理所有内核对象（设备、文件、事件、信号量等）。结构类似于文件系统：

```
\ (根)
├── \Device          ← 设备对象（磁盘、VSS卷、键盘等）
├── \BaseNamedObjects ← 事件/互斥量/信号量
├── \GLOBAL??         ← DOS设备映射 (C:, D:)
├── \Callback         ← 回调对象
├── \KernelObjects    ← 内核同步对象
└── ...
```

这个命名空间存在于内核内存中，普通的 `CreateFile`/`FindFirstFile`**完全访问不到**。必须通过 `NtOpenDirectoryObject` / `NtQueryDirectoryObject` 这些原生 API 才能查询。

```
static std::vector<std::pair<std::wstring, std::wstring>> enum_directory(const std::wstring& path){    std::vector<std::pair<std::wstring, std::wstring>> entries;
    UNICODE_STRING dirName;    RtlInitUnicodeString(&dirName, path.c_str());
    OBJECT_ATTRIBUTES oa;    InitializeObjectAttributes(&oa, &dirName, OBJ_CASE_INSENSITIVE, nullptr, nullptr);
    HANDLE hDir = nullptr;    NTSTATUS status = g_NtOpenDirectoryObject(&hDir, DIRECTORY_QUERY, &oa);    if (status != 0) {        std::cerr << "[-] Failed to open \\" << wstr_to_utf8(path.substr(1)) << ": 0x" << std::hex << status << std::dec << "\n";        return entries;    }
    BYTE buffer[sizeof(OBJECT_DIRECTORY_INFORMATION) + 512];    ULONG context = 0;    BOOLEAN restart = TRUE;
    for (;;) {        ULONG returnLen = 0;        status = g_NtQueryDirectoryObject(            hDir, buffer, sizeof(buffer), TRUE, restart, &context, &returnLen);
        if (status == STATUS_NO_MORE_ENTRIES)            break;
        if (!NT_SUCCESS(status) && status != STATUS_MORE_ENTRIES) {            std::cerr << "[-] NtQueryDirectoryObject failed: 0x" << std::hex << status << std::dec << "\n";            break;        }
        restart = FALSE;        auto info = reinterpret_cast<POBJECT_DIRECTORY_INFORMATION>(buffer);
        entries.emplace_back(            std::wstring(info->Name.Buffer, info->Name.Length / sizeof(WCHAR)),            std::wstring(info->TypeName.Buffer, info->TypeName.Length / sizeof(WCHAR)));    }
    CloseHandle(hDir);    return entries;}
```

![image-20260502204121740](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3RpuibfnKOmDgxXu0KuibG1VGBT2EM1kpC2M2f3GpBXcuRnJrnoa7AIeTdIdvL0r9WicEsgUdWWaJdT1cicgT2SNsAmRTOsXkD9KUFiaD0/640?wx_fmt=png&from=appmsg)

## Volume Shadow Copy Service (Windows VSS)

> Volume Shadow Copy Service（简称 VSS）是 Microsoft Windows 操作系统内置的数据备份框架，用于在应用程序运行时创建一致性的磁盘卷快照（shadow copy）。它支撑了系统还原、文件历史版本及多种备份软件，是 Windows 数据保护机制的核心组成部分。[3]

在这里的利用就是首先就是windows defender检测到恶意文件的时候首先不会将其删除，而是会通过卷影副本进行隔离/备份操作。使用`vssadmin`可以操作。启用后会在对象管理器的`Device`下创建`HarddiskVolumeShadowCopyN`

```
#include <windows.h>#include <iostream>#include <fstream>#include <string>#include <vector>#include <filesystem>
namespace fs = std::filesystem;
static std::string exec(const char* cmd){    char buffer[4096];    std::string result;    FILE* pipe = _popen(cmd, "r");    if (!pipe) return "[_popen failed]";
    while (fgets(buffer, sizeof(buffer), pipe))        result += buffer;
    _pclose(pipe);    return result;}
static std::string extract_wmic_device_path(const std::string& output){    // Try multiple known paths and return the last one (newest)    std::vector<std::string> paths;    std::string marker = "\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy";    size_t pos = 0;
    while ((pos = output.find(marker, pos)) != std::string::npos) {        // Scan back to find start of line (after '=' or start)        size_t start = output.rfind('=', pos);        if (start == std::string::npos) start = pos;        else start = start + 1;
        size_t end = output.find_first_of("\r\n", start);        std::string path = output.substr(start, end - start);
        // Trim trailing backslash        while (!path.empty() && path.back() == '\\')            path.pop_back();
        paths.push_back(path);        pos = end;    }
    if (paths.empty()) return {};    return paths.back(); // newest}
int main(){    fs::create_directories("C:\\test");
    const std::string targetFile = "C:\\test\\demo.txt";    const std::string restoreFile = "C:\\test\\restored.txt";
    // 1. 使用wmi创建原始文件的VSS影子副本    std::string output = exec("wmic shadowcopy call create Volume=\"C:\\\"");    std::cout << "[+] Creating shadow copy via WMI: " << output << "\n";
    std::string shadowPath = extract_wmic_device_path(output);    if (shadowPath.empty()) {        std::cout << "[-] WMIC method failed.\n";        std::cout << "===== Raw WMIC output =====\n" << output << "=====\n";
        // Fallback: try to list existing shadow copies        std::cout << "[*] Trying to list existing shadow copies...\n";        std::string listOutput = exec("wmic shadowcopy get DeviceObject /format:list 2>&1");        shadowPath = extract_wmic_device_path(listOutput);        if (shadowPath.empty()) {            std::cout << "===== Existing shadow copies =====\n" << listOutput << "=====\n";            std::cout << "[-] Cannot create or find any shadow copy.\n";            return 1;        }        std::cout << "[+] Using existing shadow copy: " << shadowPath << "\n";    }    else {        std::cout << "[+] Shadow Copy created: " << shadowPath << "\n";    }
    // 2. 修改原始文件    {        std::ofstream ofs(targetFile);        ofs << "MODIFIED DATA: This version is AFTER the shadow copy was taken.\n";        ofs.close();        std::cout << "[+] Original file modified (after snapshot).\n";    }
    // 3. 从影子副本中恢复原始文件    {        std::string shadowFile = shadowPath + "\\test\\demo.txt";        std::cout << "[+] Reading from snapshot: " << shadowFile << "\n";
        std::ifstream ifs(shadowFile, std::ios::binary);        if (!ifs) {            std::cerr << "[-] Cannot open file in shadow copy!\n";            return 1;        }
        std::ofstream ofs(restoreFile, std::ios::binary);        ofs << ifs.rdbuf();        ifs.close();        ofs.close();        std::cout << "[+] File restored to: " << restoreFile << "\n";    }
    return 0;}
```

`首先在``C://test/`中只存在`demo.txt`

![image-20260502214442388](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuibyBY6sxnTTFztYsPggib3UHFgjrDo64t8KazU7EkkHGSLEpRbUsM6oZYbeJgWZuLGibahCNMPsOm1FegehvfribuSib9985RRbQ8c/640?wx_fmt=png&from=appmsg)

在管理员模式下运行程序后，成功地从VSS中恢复了原始文件的内容。

![image-20260502214610317](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3Rpuic5gOl2M5FiaFiaROTrqZMyISV4E4hSibxW04M0Z7phM29hBb4JwnicESAhzDaj3YoCBHwpg8f4ze8mAs8eImicibqI58nTSjr5unuia0/640?wx_fmt=png&from=appmsg)

## 云同步目录

> 从 Windows 10 版本 1709 开始，Windows 提供 *云文件 API*。 此 API 由多个本机 Win32 和 WinRT API 组成，这些 API 正式支持云同步引擎，并处理创建和管理占位符文件和目录等任务。 此 API 的用户通常是同步提供程序，在某种程度上是 Windows 应用程序。[4]

使用类似PoC中的代码创建云同步目录会发现由于占位符的存在，无法对其中的文件进行操作。

![image-20260503202047072](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuicKxbn7F012wVPiaHLhhlXgVukBDia5ymu3eMhnXfGyEGaPXwHickUfoicaDicyWGeR7CWTAJYEib3Xd42Q7gdYIiaLQiaEyc74VEcYNQM/640?wx_fmt=png&from=appmsg)

# PoC分析

来源：https://github.com/Nightmare-Eclipse/RedSun/

PoC主要替换掉了`TieringEngineService`这个服务，他是 Windows 里一个和**存储分层 / 数据分级（Storage Tiering）**相关的系统服务，名字直译就是“分层引擎服务”。

## API简介

* `WaitOnAddress`

  等待指定地址处的值更改。

  ```
  BOOL WaitOnAddress(
    [in]           volatile VOID* Address,
    [in]           PVOID          CompareAddress,
    [in]           SIZE_T         AddressSize,
    [in, optional] DWORD          dwMilliseconds
  );
  ```
* `GetOverlappedResult`

  检索指定文件、...