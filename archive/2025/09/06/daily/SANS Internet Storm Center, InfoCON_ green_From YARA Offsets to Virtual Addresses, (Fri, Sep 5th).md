---
title: From YARA Offsets to Virtual Addresses, (Fri, Sep 5th)
url: https://isc.sans.edu/diary/rss/32262
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-06
fetch_date: 2025-10-02T19:46:02.856534
---

# From YARA Offsets to Virtual Addresses, (Fri, Sep 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32256)
* [next](/diary/32266)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [From YARA Offsets to Virtual Addresses](/forums/diary/From%2BYARA%2BOffsets%2Bto%2BVirtual%2BAddresses/32262/)

**Published**: 2025-09-05. **Last Updated**: 2025-09-05 06:18:43 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/From%2BYARA%2BOffsets%2Bto%2BVirtual%2BAddresses/32262/#comments)

YARA is an excellent tool that most of you probably already know and use daily. If you don't, search on isc.sans.edu, we have a bunch of diaries about it[[1](https://isc.sans.edu/search.html?q=yara&token=&Search=Search)]. YARA is very powerful because you can search for arrays of bytes that represent executable code. In this case, you provide the hexadecimal representation of the binary machine code.

Example:

```

$sequence_0 = { 42 895114 e8???????? 8901 833900 7407 8b01 }
    // n = 7, score = 100
    //   42                   | inc                 edx
    //   895114               | mov                 dword ptr [ecx + 0x14], edx
    //   e8????????           |
    //   8901                 | mov                 dword ptr [ecx], eax
    //   833900               | cmp                 dword ptr [ecx], 0
    //   7407                 | je                  9
    //   8b01                 | mov                 eax, dword ptr [ecx]
```

(This example of coming from win.koadic\_auto.yar[[2](https://raw.githubusercontent.com/malpedia/signator-rules/main/rules/win.koadic_auto.yar)])

When you launch YARA rules against a file, the tool will notify you if there is a match (read: the array of bytes has been found). If you add the command line switch "-s", YARA will show you the file offset where it was detected:

```

remnux@remnux:/malwarezoo/20250905$ yara -s win.koadic_auto.yar sample.exe
win_koadic_auto sample.exe
0xc1b6:$sequence_0: 42 89 51 14 E8 A9 FF FF FF 89 01 83 39 00 74 07 8B 01
0xec0a:$sequence_2: 83 C2 01 89 55 F8 8B 45 08 0F B6 48 01 81 E1 C0 00 00 00 81 F9 80 00 00 00
0xec95:$sequence_2: 83 C2 01 89 55 F8 8B 45 08 0F B6 48 01 81 E1 C0 00 00 00 81 F9 80 00 00 00
0x5262:$sequence_3: 52 8B 14 01 52 FF 15 0C 3B 41 00 85 C0 0F 8E 08 01 00 00 8B 0F
0x4439:$sequence_4: 89 48 04 5B 83 C4 0C C3 0F 8E D6 00 00 00 8B C7 99
0x4579:$sequence_4: 89 48 04 5B 83 C4 0C C3 0F 8E D6 00 00 00 8B C7 99
0x46b9:$sequence_4: 89 48 04 5B 83 C4 0C C3 0F 8E D6 00 00 00 8B C7 99
0x47f9:$sequence_4: 89 48 04 5B 83 C4 0C C3 0F 8E D6 00 00 00 8B C7 99
0x53d9:$sequence_4: 89 48 04 5B 83 C4 0C C3 0F 8E D6 00 00 00 8B C7 99
0x5519:$sequence_4: 89 48 04 5B 83 C4 0C C3 0F 8E D6 00 00 00 8B C7 99
0xe8c6:$sequence_5: E8 95 04 00 00 8B 4C 24 10 5F C6 04 0E 00 5E 59
0x24a0:$sequence_7: 3B 44 24 04 7C 54 FF 74 24 04 8B 6C 24 20
0x76ba:$sequence_8: 57 8D 45 F8 50 56 53 FF 75 0C FF 15 CC 27 41 00
0x8cf6:$sequence_9: FF 15 58 28 41 00 8B F8 8D 5F 01 53 6A 00
```

Good news! We have a match. We can verify that the offset is related to the raw file. Let's take the example of $sequence0:

```

remnux@remnux:/malwarezoo/20250905$ cut-bytes.py -x 0xc1b6: sample.exe |head -5
42 89 51 14 E8 A9 FF FF FF 89 01 83 39 00 74 07
8B 01 83 C0 08 EB 02 33 C0 C2 04 00 55 8B EC 51
56 8B 75 08 33 C0 85 F6 74 69 39 45 0C 74 64 83
7D 10 00 8B 06 89 45 08 8B 46 14 89 45 FC 74 08
FF 75 0C E8 28 01 00 00 57 56 E8 E0 FE FF FF EB
```

What if we would like to find this piece of code in a debugger or a disassembler to continue our investigations? Is this piece of code relevant to our investigations?

First, let's take a few minutes to discuss the PE (Portable Executable) format. An executable contains sections (the well-known .text, .data, .rdata, ...) that contain the data used by the program. The more interesting one is usually .text that contains the executable code. In the PE headers, all sections are referenced by their offset and size:

```

remnux@remnux:/malwarezoo/20250905$ python3
Python 3.8.10 (default, Jun 22 2022, 20:18:18)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pefile
>>> pe = pefile.PE("sample.exe", fast_load=True)
>>> for s in pe.sections:
...     name = s.Name.rstrip(b"\x00").decode(errors="replace")
...     raw_off = s.PointerToRawData
...     raw_sz  = s.SizeOfRawData
...     va     = s.VirtualAddress
...     print(f"{name}\t{raw_off}\t{raw_sz}\t{va}")
...
.code    1024    13312    4096
.text    14336    47104    20480
.rdata    61440    2560    69632
.data    64000    5632    73728
.rsrc    69632    34816    81920
>>>
```

To map the YARA offset to the correct location in the program, we need to perform some actions:

1. Identify the correct section (that contains the array of bytes). For each section, test this:

```

section_raw_off <= yara_offset < section_raw_off + section_raw_sz
```

2. Convert the YARA offset to the RVA ("Relative Virtual Address"):

```

rva = (yara_offset - section_raw_off) + section_va
```

3. Convert the RVA to the VA based on the ImageBase found in the PE headers:

```

va = ImageBase + rva
```

Let's create a small script to perform these operations and parse the YARA output (disclaimer: some pieces of the code have been generated with ChatGPT):

```

remnux@remnux:/malwarezoo/20250905$ yara -s win.koadic_auto.yar sample.exe | ./map_va.py
File        Rule             String ID    File Offset  Section  RVA      VA        Note
----------  ---------------  -----------  -----------  -------  -------  --------  ----
sample.exe  win_koadic_auto  $sequence_0  0xC1B6       .text    0xD9B6   0x40D9B6
sample.exe  win_koadic_auto  $sequence_2  0xEC0A       .text    0x1040A  0x41040A
sample.exe  win_koadic_auto  $sequence_2  0xEC95       .text    0x10495  0x410495
sample.exe  win_koadic_auto  $sequence_3  0x5262       .text    0x6A62   0x406A62
sample.exe  win_koadic_auto  $sequence_4  0x4439       .text    0x5C39   0x405C39
sample.exe  win_koadic_auto  $sequence_4  0x4579       .text    0x5D79   0x405D79
sample.exe  win_koadic_auto  $sequence_4  0x46B9       .text    0x5EB9   0x405EB9
sample.exe  win_koadic_auto  $sequence_4  0x47F9       .text    0x5FF9   0x405FF9
sample.exe  win_koadic_auto  $sequence_4  0x53D9       .text    0x6BD9   0x406BD9
sample.exe  win_koadic_auto  $sequence_4  0x5519       .text    0x6D19   0x406D19
sample.exe  win_koadic_auto  $sequence_5  0xE8C6       .text    0x100C6  0x4100C6
sample.exe  win_koadic_auto  $sequence_7  0x24A0       .code    0x30A0   0x4030A0
sample.exe  win_koadic_auto  $sequence_8  0x76BA       .text    0x8EBA   0x408EBA
sample.exe  win_koadic_auto  $sequence_9  0x8CF6       .text    0xA4F6   0x40A4F6
```

Let's search for the $sequence0 in our disassembler:

![](https://isc.sans.edu/diaryimages/images/isc-20250905-1.png)

Now, you can debug the program around this piece of code and validate if it's really malicious or not!

The script is available on my GitHub repository[[3](https://github.com/xme/SANS-ISC/blob/master/map_va.py)].

[1] <https://isc.sans.edu/search.html?q=yara&token=&Search=Search>
[2] <https://raw.githubusercontent.com/malpedia/signator-rules/main/rules/win.koadic_auto.yar>
[3] <https://github.com/xme/SANS-ISC/blob/master/map_va.py>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Debugger](/tag.html?tag=Debugger) [Mapping](/tag.html?tag=Mapping) [Offset](/tag.html?tag=Offset) [RVA](/tag.html?tag=RVA) [VA](/tag.html?tag=VA) [YARA](/tag.html?tag=YARA)

[0 comment(s)](/diary/From%2BYARA%2BOff...