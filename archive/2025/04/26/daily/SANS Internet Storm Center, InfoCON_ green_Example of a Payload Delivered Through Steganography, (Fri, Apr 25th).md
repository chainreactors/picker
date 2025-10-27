---
title: Example of a Payload Delivered Through Steganography, (Fri, Apr 25th)
url: https://isc.sans.edu/diary/rss/31892
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-26
fetch_date: 2025-10-06T22:07:28.861780
---

# Example of a Payload Delivered Through Steganography, (Fri, Apr 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31888)
* [next](/diary/31894)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Example of a Payload Delivered Through Steganography](/forums/diary/Example%2Bof%2Ba%2BPayload%2BDelivered%2BThrough%2BSteganography/31892/)

**Published**: 2025-04-25. **Last Updated**: 2025-04-25 07:20:44 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Example%2Bof%2Ba%2BPayload%2BDelivered%2BThrough%2BSteganography/31892/#comments)

In this diary, I’ll show you a practical example of how steganography is used to hide payloads (or other suspicious data) from security tools and Security Analysts’ eyes. Steganography can be defined like this: It is the art and science of concealing a secret message, file, or image within an ordinary-looking carrier—such as a digital photograph, audio clip, or text—so that the very existence of the hidden data is undetectable to casual observers (read: security people). Many online implementations of basic steganography allow you to embed a message (a string) into a picture[[1](https://manytools.org/hacker-tools/steganography-encode-text-into-image/)].

Let’s have a look at the sample I found. Because it’s a .Net binary, it can be easily decompiled. But, because the source code is easily accessible, many malware are often obfuscated. A classic technique is to use UFT-16 in functions, classes, variable names, etc. In the following example, the registry key name is obfuscated:

![](https://isc.sans.edu/diaryimages/images/isc-20250425-1.png)

Another common behaviour of malware in .Net is to use reflective code loading techniques. Reflective code loading is the ability of a running program to inspect, load, and use code—classes, functions, libraries, even entire assemblies—that was not statically linked or explicitly referenced at compile time. Instead, the program decides at runtime what to bring into memory and how to invoke it. Therefore, when you reverse a .Net program, it’s a good idea to search for methods like .Load(), .LoadFrom() or .LoadFile(). This may indicate that more code will be loaded (passed as a parameter).

That’s what I found in this sample, but there were other interesting strings: “Bitmap”, “WebClient”, or “OpenRead”:

![](https://isc.sans.edu/diaryimages/images/isc-20250425-2.png)

A Bitmap payload (read: a picture) is downloaded from a URL. Once deobfuscated, we get:

```

hxxps://i[.]ibb[.]co/LgqktNn/freemaosnry[.]png
```

The deobfuscating function is here:

![](https://isc.sans.edu/diaryimages/images/isc-20250425-3.png)

Once the picture has been downloaded, a loop will process all the pixels from the top row and extract the “red” component value. All the values are added in a byte array to rebuild the next payload. We can reproduce this with a few lines of Python:

```

#!/usr/bin/env python3
import sys
from PIL import Image

def main():
    img = Image.open(“freemaosnry[.]png”).convert("RGBA")
    w, h = img.size
    pix = img.load()

    with open("payload.tmp", "wb") as f:
        for y in range(h):
            for x in range(w):
                r, g, b, a = pix[x, y]
                f.write(bytes([r]))

if __name__ == "__main__”:
    main()
```

Let’s have a look at the picture:

```

remnux@remnux:/MalwareZoo/20250418$ file freemaosnry.png
freemaosnry.png: PNG image data, 31744 x 1, 8-bit/color RGBA, non-interlaced
```

Based on the file details, we should get a payload of 31744 bytes:

```

remnux@remnux:/MalwareZoo/20250418$./decode_pic.py
remnux@remnux:/MalwareZoo/20250418$ ls -al payload.tmp
-rwx------ 1 501 dialout 31744 Apr 18 08:27 payload.tmp*
remnux@remnux:/MalwareZoo/20250418$ file payload.tmp
payload.tmp: PE32 executable (GUI) Intel 80386 Mono/.Net assembly, for MS Windows
```

Bingo! We have the next payload that, during execution, has been generated in memory. It is now ready to be invoked with:

```

AppDomain.CurrentDomain.Load(array).EntryPoint.Invoke(null, null);
```

What about this malware? The initial PE file was named “voice\_recording.bat” (SHA256:ce77b1bc3431139358e2a70fa5f731d1be127e77efe8b534df5ccde59083849d[[2](https://www.virustotal.com/gui/file/ce77b1bc3431139358e2a70fa5f731d1be127e77efe8b534df5ccde59083849d/detection)]). It belongs to the XWorm family and has the following config:

```

{
    “c2": [
        "cryptoghost[.]zapto[.]org"
    ],
    "family": "latentbot"
}
{
    "attr": {
        "install_file": "MasonUSB.exe"
    },
    "rule": "Xworm",
    "family": "xworm"
}
```

Happy hunting!

[1] <https://manytools.org/hacker-tools/steganography-encode-text-into-image/>
[2] <https://www.virustotal.com/gui/file/ce77b1bc3431139358e2a70fa5f731d1be127e77efe8b534df5ccde59083849d/detection>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Malware](/tag.html?tag=Malware) [Net](/tag.html?tag=Net) [Obfuscation](/tag.html?tag=Obfuscation) [Steganography](/tag.html?tag=Steganography)

[0 comment(s)](/diary/Example%2Bof%2Ba%2BPayload%2BDelivered%2BThrough%2BSteganography/31892/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31888)
* [next](/diary/31894)

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