---
title: Phobia
url: https://labs.yarix.com/2022/11/phobia/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-26
fetch_date: 2025-10-03T23:51:01.543688
---

# Phobia

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# Phobia

* [Home](https://labs.yarix.com "Go to Home Page")
* Phobia

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2022/11/Blog-1140x445.jpg)

25Nov25/11/2022

## Phobia

[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")2022-12-13T08:44:04+01:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")

Reading Time:   9 minutes

#

# **Ransomware Details**

Phobos ransomware, first discovered in December 2018, is another notorious cyber threat that targets businesses.

Phobos is popular among threat actors of various technical abilities because of its simple design. In addition, the Greek god Phobos was thought to be the incarnation of fear and panic; hence the name Phobos was likely inspired by him.

Phobos is a ransomware infection that spreads through hijacked Remote Desktop (RDP) connections. This isn’t surprising, given that hacked RDP servers are a cheap commodity on the underground market and can be an appealing and cost-effective distribution route for threat actors.

Additionally, Phobos is not packed or obfuscated, unlike the majority of malware that is secured by a crypter. Although the absence of packing is not frequent in the general population of malware, it is widespread among malware that is manually distributed by attackers.

**Observed Targets Industries**

Unlike other gangs that look for medium/enterprise targets, the Phobos team usually go after smaller firms that don’t have the financial wherewithal to pay massive ransoms. Phobos is standard ransomware that offers little in the way of innovation. This gang does not use the double extortion approach. There have been no reports of any underground leak sites linked to it revealing confidential information about its targets. This threat is most likely inserted to influence the victim, capitalizing on worries sparked by other high-profile ransomware attacks.

##

# INTRODUCTION

**Yarix Response Team first Engagement**

**Malware Analysis**

The analysis of the binary “ph\_decrypt.exe” obtained by YIR (Yarix Incident Response Team) will be divided into various sections distinguishing between static and dynamic.

## **Static Analysis – ph\_decrypt.exe**

### **PE Sections**

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x43.jpg)

Static Analysis – PE Sections

The binary has several sections such as “CODE”, “DATA”, “BSS”, “.idata”, “.tls”, “.rdata”, “.reloc” and “.rsrc”; in particular, it is noteworthy that inside “.rsrc” there are two particularly suspicious files given their Magic Signature which leads to an executable file and a Delphi Form.

Proceeding to a more in-depth analysis, it is noted that by exporting the binary resources, several secondary encrypted payloads emerge in addition to the two executables specified above

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x23.jpg)

Static Analysis – RCDATA

From the static analysis it is difficult to understand the true nature of textual resources such as “EX”, “KD”, “TK”, “VR” and “WO” as they appear to be strings encrypted by a matryoshka of different techniques that once decrypted lead to the evidence of payloads encoded with unknown methodologies.

The textual resources are then used by some internal routines for comparative checks during a strange file substitution routine analyzed in the dynamic analysis section.

As for the other resources, their use is as follows:

* CX Executable created by the malware during its execution and renamed to “.cache\_% FILENAME%”, in addition the binary is hidden and flagged as a system file
* TMAINFORM –> Form of the decryptor written in Delphi and used as a “GUI” for entering the “decrypt keys” provided by the Threat Actor and selecting the UNC paths containing the files to be decrypted

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x24.jpg)

Static Analysis – GUI

####

### **file-headers**

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x84.jpg)

Static Analysis – PE file-header

From the header file some useful information related to the nature of the file can be found, such as:

* Payload has been compiled for 32bit architectures
* The compiler date is pointing at 19th June 1992
* Symbols have been stripped from file

### **Import-table**

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x63.jpg)

Static Analysis – PE explicit imports

From the “Explicit Import Table” the following DLLs imported from the binary during the loading phase are detected: kernel32.dll, user32.dll, advapi32.dll, oleaut32.dll, version.dll, gdi32.dll, ole32.dll, comctl32.dll, shell32.dll, wininet.dll, wsock32.dll, netapi32.dll.

The type of imported DLLs suggests that the binary is not limited to the decryption of files as there are “wsock.dll” and “netapi.dll” for managing sockets, “shell32.dll” for sending commands via shells like “cmd.exe” and many other functions not normally present in ransomware decryptor software.

### **functions**

From the “Function Table” you can see the following functions coming from the DLLs shown in the “import-table” section of this report:

```
GetCurrentThreadId, SetCurrentDirectoryA, FindFirstFileA, WriteFile, RaiseException, GetKeyboardType, ShellExecuteExA, SHGetFileInfoA, SHFileOperationA, InternetGetConnectedState, WSACleanup, WSAStartup, WSAGetLastError, gethostbyname, socket, setsockopt, send, recv, ntohl, ioctlsocket, inet_addr, htons, htonl, connect, closesocket, Netbios, DeleteCriticalSection, LeaveCriticalSection, EnterCriticalSection, InitializeCriticalSection, VirtualFree, VirtualAlloc, LocalFree, LocalAlloc, GetTickCount, QueryPerformanceCounter, GetVersion, InterlockedDecrement, InterlockedIncrement, VirtualQuery, WideCharToMultiByte, MultiByteToWideChar, lstrlenA, lstrcpynA, LoadLibraryExA, GetThreadLocale, GetStartupInfoA, GetProcAddress, GetModuleHandleA, GetModuleFileNameA, GetLocaleInfoA, GetLastError, GetCurrentDirectoryA, GetCommandLineA, FreeLibrary, FindClose, ExitProcess, ExitThread, CreateThread, UnhandledExceptionFilter, SetFilePointer, SetEndOfFile, RtlUnwind, ReadFile, GetStdHandle, GetFileSize, GetFileType, CreateFileA, CloseHandle, LoadStringA, MessageBoxA, CharNextA, RegQueryValueExA, RegOpenKeyExA, RegCloseKey, SysFreeString, SysReAllocStringLen, SysAllocStringLen, VerQueryValueA, GetFileVersionInfoSizeA, GetFileVersionInfoA, UnrealizeObject, StretchBlt, SetWindowOrgEx, SetWinMetaFileBits, SetViewportOrgEx, SetTextColor, SetStretchBltMode, SetROP2, SetPixel, SetEnhMetaFileBits, SetDIBColorTable, SetBrushOrgEx, SetBkMode, SetBkColor, SelectPalette, SelectObject, SaveDC, RestoreDC, RectVisible, RealizePalette, PlayEnhMetaFile, PatBlt, MoveToEx, MaskBlt, LineTo, IntersectClipRect, GetWindowOrgEx, GetWinMetaFileBits, GetTextMetricsA, GetTextExtentPoint32A, GetSystemPaletteEntries, GetStockObject, GetPixel, GetPaletteEntries, GetObjectA, GetEnhMetaFilePaletteEntries, GetEnhMetaFileHeader, GetEnhMetaFileBits, GetDeviceCaps, GetDIBits, GetDIBColorTable, GetDCOrgEx, GetCurrentPositionEx, GetClipBox, GetBrushOrgEx, GetBitmapBits, GdiFlush, ExcludeClipRect, DeleteObject, DeleteEnhMetaFile, DeleteDC, CreateSolidBrush, CreatePenIndirect, CreatePalette, CreateHalftonePalette, CreateFontIndirectA, CreateDIBitmap, CreateDIBSection, CreateCompatibleDC, CreateCompatibleBitmap, CreateBrushIndirect, CreateBitmap, CopyEnhMetaFileA, BitBlt, CreateBindCtx, MkParseDisplayName, CLSIDFromProgID, CLSIDFromString, CoCreateInstance, CoUninitialize, CoInitializ...