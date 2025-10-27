---
title: VMP源码分析：反调试与绕过方法
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562488&idx=2&sn=fe5bd1498948137775db5f454bd5a6a2&chksm=b18d9f3286fa162491072b9cd141784c1a60b2b00fd8203f865c51ef753e3f45573a78810949&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-08
fetch_date: 2025-10-06T17:41:18.311399
---

# VMP源码分析：反调试与绕过方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMTDlr20LZvPXlZst96fExL0NlDLXZMojHsbwj3Wg1UiaSKO0J58udglg/0?wx_fmt=jpeg)

# VMP源码分析：反调试与绕过方法

JoJoRun

看雪学苑

```
一

vmp反调试相关源码部分
```

##

## 1.1 如何检索反调试源码

我们都知道，当vmp检测到被调试，会有如下弹框。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMeEpVicba7YnCicSjbzfBciarI5IMTVvDxiaLDqBmm1ParoK4DKM92OoKwg/640?wx_fmt=other&from=appmsg)

通过这条报错信息，不难在源码中找到：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMS9OQblLFfKv51zdS300H4QvDYaoZaAqHJdrlRuEEh2lg8SjBQhdiapg/640?wx_fmt=other&from=appmsg)

然后通过它的消息传递机制，不难找到：

```
void LoaderMessage(MessageType type, const void *param1 = NULL, const void *param2 = NULL)
{
    const VMP_CHAR *message;
    bool need_format = false;
    switch (type) {
    case mtDebuggerFound:
        message = reinterpret_cast<const VMP_CHAR *>(FACE_DEBUGGER_FOUND);
        break;
    case mtVirtualMachineFound:
        message = reinterpret_cast<const VMP_CHAR *>(FACE_VIRTUAL_MACHINE_FOUND);
        break;
    case mtFileCorrupted:
        message = reinterpret_cast<const VMP_CHAR *>(FACE_FILE_CORRUPTED);
        break;
    case mtUnregisteredVersion:
        message = reinterpret_cast<const VMP_CHAR *>(FACE_UNREGISTERED_VERSION);
        break;
    case mtInitializationError:
        message = reinterpret_cast<const VMP_CHAR *>(FACE_INITIALIZATION_ERROR);
        need_format = true;
        break;
    case mtProcNotFound:
        message = reinterpret_cast<const VMP_CHAR *>(FACE_PROC_NOT_FOUND);
        need_format = true;
        break;
    case mtOrdinalNotFound:
        message = reinterpret_cast<const VMP_CHAR *>(FACE_ORDINAL_NOT_FOUND);
        need_format = true;
        break;
    default:
        return;
    }
```

然后查找**mtDebuggerFound**的引用即可检索到各处反调试相关源码，也就是此文将要详细说的，至于其他部分的检测，感兴趣的童鞋可以自行研究。

## 1.2 源码阅读：反调试手段

### 1.2.1 系统版本号的判断

```
if (!os_build_number) {
    if (data.options() & LOADER_OPTION_CHECK_DEBUGGER) {
        LoaderMessage(mtDebuggerFound);
        return LOADER_ERROR;
    }
    tmp_loader_data->set_is_debugger_detected(true);
}
```

那么这个**os\_build\_number**怎么获取的呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMSKcUUglCJzKEN8Vuyn2iatvmpw1ibBhhWE8zMh44GZHzL0qZNGibnEPnQ/640?wx_fmt=other&from=appmsg)

简单说，一共两种获取方式，1. 从**peb**里直接去取得；2.从**ntdll.dll**的头部获取文件版本号从而确定系统版本。

可能有的童鞋会问了，系统版本号拿来判断反调试是不是有点什么大病，其实不是，私以为，这边判断系统版本号纯纯的只是为了方便取 syscall 所使用的系统调用号。

如下，**vmp**应该是把全量的发行版系统都是硬编码了：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBM0PY6bxYFCvr9eJr53p6KaZticKlHtESSamW01NjhELDAxDjUaepLqew/640?wx_fmt=other&from=appmsg)

当系统版本号不在 vmp 适配过的范围（比如测试版 windows），他则会去 map 一份新的 ntdll ，然后从中找他要的NT函数的系统调用号，至于系统调用号是什么，这里就不赘述了。

### 1.2.2 peb->BeingDebugged 标记

```
if (peb->BeingDebugged) {
    LoaderMessage(mtDebuggerFound);
    return LOADER_ERROR;
}
```

会心一笑，peb里的这个位就不用过多解释了。

### 1.2.3 ProcessDebugPort

```
if (NT_SUCCESS(reinterpret_cast<tNtQueryInformationProcess *>(syscall | sc_query_information_process)(process, ProcessDebugPort, &debug_object, sizeof(debug_object), NULL)) && debug_object != 0) {
    LoaderMessage(mtDebuggerFound);
    return LOADER_ERROR;
}
```

查询 ProcessDebugPort，如果查到了，自然是被调试了，也是很常见的反调。

### 1.2.4 ProcessDebugObjectHandle

```
if (NT_SUCCESS(reinterpret_cast<tNtQueryInformationProcess *>(syscall | sc_query_information_process)(process, ProcessDebugObjectHandle, &debug_object, sizeof(debug_object), reinterpret_cast<PULONG>(&debug_object)))
    || debug_object == 0) {
    LoaderMessage(mtDebuggerFound);
    return LOADER_ERROR;
}
```

查询 ProcessDebugObjectHandle, 如果 存在调试对象句柄，那也是被调试了，也属于常见反调。

### 1.2.5 SystemKernelDebuggerInformation

```
SYSTEM_KERNEL_DEBUGGER_INFORMATION info;
NTSTATUS status = nt_query_system_information(SystemKernelDebuggerInformation, &info, sizeof(info), NULL);
if (NT_SUCCESS(status) && info.DebuggerEnabled && !info.DebuggerNotPresent) {
    LoaderMessage(mtDebuggerFound);
    return LOADER_ERROR;
}
```

针对内核调试器的监测，也属常见。

### 1.2.6 针对驱动模块名的匹配

```
SYSTEM_MODULE_INFORMATION *buffer = NULL;
ULONG buffer_size = 0;
status = nt_query_system_information(SystemModuleInformation, &buffer, 0, &buffer_size);
if (buffer_size) {
    buffer = reinterpret_cast<SYSTEM_MODULE_INFORMATION *>(LoaderAlloc(buffer_size * 2));
    if (buffer) {
        status = nt_query_system_information(SystemModuleInformation, buffer, buffer_size * 2, NULL);
        if (NT_SUCCESS(status)) {
            for (size_t i = 0; i < buffer->Count && !is_found; i++) {
                SYSTEM_MODULE_ENTRY *module_entry = &buffer->Module[i];
                for (size_t j = 0; j < 5 ; j++) {
                    const char *module_name;
                    switch (j) {
                    case 0:
                        module_name = reinterpret_cast<const char *>(FACE_SICE_NAME);
                        break;
                    case 1:
                        module_name = reinterpret_cast<const char *>(FACE_SIWVID_NAME);
                        break;
                    case 2:
                        module_name = reinterpret_cast<const char *>(FACE_NTICE_NAME);
                        break;
                    case 3:
                        module_name = reinterpret_cast<const char *>(FACE_ICEEXT_NAME);
                        break;
                    case 4:
                        module_name = reinterpret_cast<const char *>(FACE_SYSER_NAME);
                        break;
                    }
                    if (Loader_stricmp(module_name, module_entry->Name + module_entry->PathLength, true) == 0) {
                        is_found = true;
                        break;
                    }
                }
            }
        }
        LoaderFree(buffer);
    }
}
```

这也是针对了一些常见的内核级调试器的检测，他们的驱动名。

### 1.2.7 线程隐藏

```
if (sc_set_information_thread)
    reinterpret_cast<tNtSetInformationThread *>(syscall | sc_set_information_thread)(thread, ThreadHideFromDebugger, NULL, 0);
```

对调试器隐藏了当前线程。

### 1.2.8 函数头 0xCC断点检测

```
tNtOpenFile *open_file = reinterpret_cast<tNtOpenFile *>(LoaderGetProcAddress(ntdll, reinterpret_cast<const char *>(FACE_NT_OPEN_FILE_NAME), true));
tNtCreateSection *create_section = reinterpret_cast<tNtCreateSection *>(LoaderGetProcAddress(ntdll, reinterpret_cast<const char *>(FACE_NT_CREATE_SECTION_NAME), true));
tNtMapViewOfSection *map_view_of_section = reinterpret_cast<tNtMapViewOfSection *>(LoaderGetProcAddress(ntdll, reinterpret_cast<const char *>(FACE_NT_MAP_VIEW_OF_SECTION), true));
tNtUnmapViewOfSection *unmap_view_of_section = reinterpret_cast<tNtUnmapViewOfSection *>(LoaderGetProcAddress(ntdll, reinterpret_cast<const char *>(FACE_NT_UNMAP_VIEW_OF_SECTION), true));
tNtClose *close = reinterpret_cast<tNtClose *>(LoaderGetProcAddress(ntdll, reinterpret_cast<const char *>(FACE_NT_CLOSE), true));

if (!create_section || !open_file || !map_view_of_section || !unmap_view_of_section || !close) {
    LoaderMessage(mtInitializationError, INTERNAL_GPA_ERROR);
    return LOADER_ERROR;
}

// check breakpoint
uint8_t *ckeck_list[] = { reinterpret_cast<uint8_t*>(create_section),
                                    reinterpret_cast<uint8_t*>(open_file),
                                    reinterpret_cast<uint8_t*>(map_view_of_section),
                                    reinterpret_cast<uint8_t*>(unmap_view_of_section),
                                    reinterpret_cast<uint8_t*>(close) };
for (i = 0; i < _countof(ckeck_list); i++) {
                if (*ckeck_list[i] == 0xcc) {
                    if (data.options() & LOADER_OPTION_CHECK_DEBUGGER) {
                        LoaderMessage(mtDebuggerFound);
                        return LOADER_ERROR;
                    }
                    tmp_loader_data->set_is_debugger_detected(true);
                }
}
```

```
if (*reinterpret_cast<uint8_t*>(virtual_protect) == 0xcc) {
    if (data.options() & LOADER_OPTION_CHECK_DEBUGGER) {
        LoaderMessage(mtDebuggerFound);
        return LOADER_ERROR...