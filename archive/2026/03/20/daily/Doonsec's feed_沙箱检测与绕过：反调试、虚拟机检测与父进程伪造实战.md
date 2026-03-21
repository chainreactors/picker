---
title: 沙箱检测与绕过：反调试、虚拟机检测与父进程伪造实战
url: https://mp.weixin.qq.com/s/r59-kTkGajAIwUGkbAZ2ag
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T03:59:16.679206
---

# 沙箱检测与绕过：反调试、虚拟机检测与父进程伪造实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RDiaL6j1Wgd7Lpj12VicglxYGXFTn7baVjdPsd4tia1X5gQGU94fQzyKdb65VlPYaFAloPxwVBl94oqqgM3ibaIQpH10SmjPWUpDF5EJKHJSgUY/0?wx_fmt=jpeg)

# 沙箱检测与绕过：反调试、虚拟机检测与父进程伪造实战

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于尘宇安全
，作者尘佑不尘

![](http://wx.qlogo.cn/mmhead/jJSbu4Te5ib9vRpbZf349vmT81yp3BiadfvFbv3sOribMntBwWgQoB9IaehaCu2Ftt5CV8TxxjiboLY/0)

**尘宇安全**
.

分享挖洞技巧和实战，收集和开发各种渗透工具及其使用，泷羽Sec团队核心成员。 声明：在此公众号上学习的任何渗透技能和工具使用，切勿非法使用，一切后果自行承担

# 前言

现在绝大多数免杀思路为混淆shellcode，这个只要多套几层加密就可以绕过静态检测，难的是绕过动态检测，因为它会对你的行为进行分析，但是动态检测大多情况在沙箱或者虚拟机调试分析，那如果我们可以识别出这些运行环境，避免在这些沙箱上面运行，是不是就绕过了动态检测了呢？最后再执行shellcode，免杀不就完成了吗？

常见云沙箱：

* https://s.threatbook.com/ 微步沙箱
* https://www.virustotal.com/ VT
* https://any.run/ 可交互式的沙箱
* https://www.joesandbox.com/#windows joe沙箱
* https://www.hybrid-analysis.com/ hybrid分析系统
* https://sandbox.dbappsecurity.com.cn/ 安恒云沙箱
* https://sandbox.ti.qianxin.com/sandbox/page 奇安信沙箱
* https://sandbox.freebuf.com/ freebuf沙箱
* https://ata.360.net/ 360云沙箱
* https://habo.qq.com/ 哈勃沙箱

# 注册表检测

通过检查 Windows 注册表中特定路径下是否存在与虚拟化平台相关的字符串，来判断当前是否运行在虚拟机环境中

虚拟机注册表常见字段：

* "HKLM\HARDWARE\DEVICETREE\SYSTEM"
* "HKLM\HARDWARE\DESCRIPTION\System"
* "HKLM\SYSTEM\CurrentControlSet\Services\Disk\Enum"

实现代码：

```
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// 要检测的关键词（全部小写）
const char* keywords[] = {
    "vmware", "virtual", "vbox", "qemu", "xen"
};
const int KEYWORD_COUNT = sizeof(keywords) / sizeof(keywords[0]);

// 转小写
void to_lower_str(char* str) {
    for (size_t i = 0; str[i]; i++) {
        str[i] = (char)tolower((unsigned char)str[i]);
    }
}

// 检查字符串是否包含任一关键词
int contains_virt_keyword(const char* input) {
    if (!input) return 0;
    char* lower = _strdup(input);
    if (!lower) return 0;
    to_lower_str(lower);

    for (int i = 0; i < KEYWORD_COUNT; i++) {
        if (strstr(lower, keywords[i]) != NULL) {
            free(lower);
            return 1;
        }
    }
    free(lower);
    return 0;
}

// 将宽字符转为多字节字符串（UTF-8）
char* wchar_to_utf8(const wchar_t* wstr) {
    if (!wstr) return NULL;
    int len = WideCharToMultiByte(CP_UTF8, 0, wstr, -1, NULL, 0, NULL, NULL);
    if (len <= 0) return NULL;
    char* buf = (char*)malloc(len);
    if (!buf) return NULL;
    WideCharToMultiByte(CP_UTF8, 0, wstr, -1, buf, len, NULL, NULL);
    return buf;
}

// 递归检查注册表键及其子键和值
int check_registry_key(HKEY hRoot, const wchar_t* subKeyPath) {
    HKEY hKey;
    LONG ret = RegOpenKeyExW(hRoot, subKeyPath, 0, KEY_READ, &hKey);
    if (ret != ERROR_SUCCESS) {
        return 0;
    }

    // 枚举所有值（Values）
    DWORD maxValueNameLen = 0, maxValueDataLen = 0;
    RegQueryInfoKeyW(hKey, NULL, NULL, NULL, NULL, NULL, NULL,
                     NULL, &maxValueNameLen, &maxValueDataLen, NULL, NULL);

    DWORD maxNameSize = maxValueNameLen + 1;
    DWORD maxDataSize = maxValueDataLen;

    wchar_t* valueName = (wchar_t*)malloc(maxNameSize * sizeof(wchar_t));
    BYTE* valueData = (BYTE*)malloc(maxDataSize);

    if (valueName && valueData) {
        DWORD index = 0;
        while (1) {
            DWORD nameSize = maxNameSize;
            DWORD dataSize = maxDataSize;
            DWORD valueType = 0;

            ret = RegEnumValueW(hKey, index, valueName, &nameSize, NULL, &valueType, valueData, &dataSize);
            if (ret != ERROR_SUCCESS) break;

            // 只处理字符串类型（REG_SZ, REG_EXPAND_SZ）
            if (valueType == REG_SZ || valueType == REG_EXPAND_SZ) {
                char* dataStr = wchar_to_utf8((wchar_t*)valueData);
                if (dataStr) {
                    if (contains_virt_keyword(dataStr)) {
                        printf("[+] Found virtualization keyword in value data: %s\n", dataStr);
                        free(dataStr);
                        free(valueName);
                        free(valueData);
                        RegCloseKey(hKey);
                        return 1;
                    }
                    free(dataStr);
                }
            }

            // 检查值名称本身
            char* nameStr = wchar_to_utf8(valueName);
            if (nameStr) {
                if (contains_virt_keyword(nameStr)) {
                    printf("[+] Found virtualization keyword in value name: %s\n", nameStr);
                    free(nameStr);
                    free(valueName);
                    free(valueData);
                    RegCloseKey(hKey);
                    return 1;
                }
                free(nameStr);
            }

            index++;
        }
    }

    // 枚举子键（Subkeys）
    DWORD maxSubKeyLen = 0;
    RegQueryInfoKeyW(hKey, NULL, NULL, NULL, NULL, &maxSubKeyLen, NULL,
                     NULL, NULL, NULL, NULL, NULL);

    DWORD subKeySize = maxSubKeyLen + 1;
    wchar_t* subKeyName = (wchar_t*)malloc(subKeySize * sizeof(wchar_t));

    if (subKeyName) {
        DWORD index = 0;
        while (1) {
            DWORD size = subKeySize;
            ret = RegEnumKeyExW(hKey, index, subKeyName, &size, NULL, NULL, NULL, NULL);
            if (ret != ERROR_SUCCESS) break;

            // 检查子键名
            char* keyNameStr = wchar_to_utf8(subKeyName);
            if (keyNameStr) {
                if (contains_virt_keyword(keyNameStr)) {
                    printf("[+] Found virtualization keyword in subkey name: %s\n", keyNameStr);
                    free(keyNameStr);
                    free(subKeyName);
                    free(valueName);
                    free(valueData);
                    RegCloseKey(hKey);
                    return 1;
                }
                free(keyNameStr);
            }

            // 递归检查子键（可选，此处暂不递归以避免过深）
            // 若需递归，可拼接路径并调用 check_registry_key

            index++;
        }
        free(subKeyName);
    }

    free(valueName);
    free(valueData);
    RegCloseKey(hKey);
    return 0;
}

int main() {
    const wchar_t* paths[] = {
        L"HARDWARE\\DEVICETREE\\SYSTEM",
        L"HARDWARE\\DESCRIPTION\\System",
        L"SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum"
    };
    int pathCount = sizeof(paths) / sizeof(paths[0]);

    printf("[*] Checking registry for virtualization artifacts...\n");

    int detected = 0;
    for (int i = 0; i < pathCount; i++) {
        printf("[*] Checking: HKLM\\%ls\n", paths[i]);
        if (check_registry_key(HKEY_LOCAL_MACHINE, paths[i])) {
            detected = 1;
            break;
        }
    }

    if (detected) {
        printf("\n[!] Virtual machine detected via registry!\n");
    } else {
        printf("\n[*] No virtualization keywords found in registry.\n");
    }

    return 0;
}
```

虚拟机运行效果：

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd42rsiaXQeGWMLdmzG29c7DHm5a6ia9wnsQML1vcjagBukEqCib5iaDhfoBWJma50KqvLk9W4rZwKGB6ViaqzkQ7OqItonOawNiaHhUI/640?wx_fmt=png&from=appmsg)

本机运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd6hiaY5ichGxye7ibPQGmBNyKP5RhbVTbSOIy5JQ3d07KHKWQGARibJp5AWO2ib9r4o54EqtMwrNibYcDzEqNdx0cyN8oyGtanyUObHc/640?wx_fmt=png&from=appmsg)

可以发现虚拟机注册表被检测出来了，本机没有

# 检查虚拟机进程

通过枚举当前系统中运行的进程列表，检查是否存在与主流虚拟化平台相关的**特定进程名**，从而判断是否运行在虚拟机环境中

常见进程名：

* "vboxservice"
* "vboxtray"
* "vmwaretray"
* "vmwareuser"
* "vmacthlp"
* "vmsrvc"
* "vmusrvc"
* "prl\_cc"
* "prl\_tools"

实现代码：

```
#include <windows.h>
#include <tlhelp32.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

const char* vm_processes[] = {
    "vboxservice", "vboxtray", "vmwaretray", "vmwareuser",
    "vmacthlp", "vmsrvc", "vmusrvc", "prl_cc", "prl_tools"
};
const int VM_PROCESS_COUNT = sizeof(vm_processes) / sizeof(vm_processes[0]);

void to_lower_str(char* str) {
    for (size_t i = 0; str[i]; i++) {
        str[i] = (char)tolower((unsigned char)str[i]);
    }
}

int is_vm_process(const char* process_name) {
    if (!process_name) return 0;

    char lower_name[MAX_PATH];
    strncpy(lower_name, process_name, MAX_PATH - 1);
    lower_name[MAX_PATH - 1] = '\0';
    to_lower_str(lower_name);

    // 去掉 ".exe" 后缀
    size_t len...