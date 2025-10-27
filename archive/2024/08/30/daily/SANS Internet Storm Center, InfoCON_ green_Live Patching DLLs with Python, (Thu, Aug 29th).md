---
title: Live Patching DLLs with Python, (Thu, Aug 29th)
url: https://isc.sans.edu/diary/rss/31218
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-30
fetch_date: 2025-10-06T18:07:56.573954
---

# Live Patching DLLs with Python, (Thu, Aug 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31216)
* [next](/diary/31220)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Live Patching DLLs with Python](/forums/diary/Live%2BPatching%2BDLLs%2Bwith%2BPython/31218/)

**Published**: 2024-08-29. **Last Updated**: 2024-08-29 07:24:07 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Live%2BPatching%2BDLLs%2Bwith%2BPython/31218/#comments)

In my previous diary[[1](https://isc.sans.edu/diary/Why%2BIs%2BPython%2Bso%2BPopular%2Bto%2BInfect%2BWindows%2BHosts/31208)], I explained why Python became popular for attackers. One of the given reason was that, from Python scripts, it’s possible to call any Windows API and, therefore, perform low-level activities on the system. In another script, besides a classic code injection in a remote process, I found an implementation of another goold old technique: live patching of a DLL.

A typical usage of  live patching is the implementation of a hook on an API. They are many ways to hook an API but a common one is called inline API hooking or « trampoline » (because we « jump » from the original function to a malicious one). In a few words, how to implement this:  You modify the beginning of a function in memory so that when the function is called, it first jumps to your malicious code. After your code runs, it can pass control back to the original function, so the program behaves as if the function was called normally, but with your modifications applied. A good example of API hooking is to perform data exfiltration. Imagine that you hook the API WriteFile(), before writing the buffer to the file, the malicious function can search for sensitive data.

Another scenario where live patching is useful: to bypass certain security controls implemented by the API. That’s what the discovered Python script will implement. I found that it will patch two interesting API calls:

* EtwEventWrite()
* AmsiScanBuffer()

To help you to better understand and "see" how it works, I wrote a quick Python script with the same behaviour. Let's run it inside a debugger and inspect the memory.

Run the script:

```

C:\Users\REM\Desktop>python patch-demo.py
Attach a debugger to this process and press ENTER when ready
```

Now, launch your favourite debugger (I'm using x64dbg) and attach to the running python.exe process. Don't define any breakpoint, just allow the debugger to run the code. Go back to the command line and press enter.

```

AmsiScanBuffer() found at this address: 0x7ffbe9a523e0
In the debugger, jump to this address and check the code
Press ENTER to continue
```

The Python script found the API call that we will patch. In the debugger, jump to the discovered address (0x7ffbe9a523e0 in this case). You can see that we are at the very beginning of the AmsiScanBuffer() API call:

![](https://isc.sans.edu/diaryimages/images/isc-20240829-1.png)

Go back to the command line and press enter again. Now the Python script will patch!

```

AmsiScanBuffer() successfully patched
Go back to the previous addresses in the debugger and check the patched code!
Waiting to quit
```

In the debugger, jump again to the same address (0x7ffbe9a523e0) and you can see that the code changed!

![](https://isc.sans.edu/diaryimages/images/isc-20240829-2.png)

What happened? Microsoft API calls use EAX to store their return value. In this case the patch performs the following instructions:

* mov eax, 80070057 : We define the return value of AmsiScanBuffer to the value "INVALID ARG"
* ret : Terminate the function and go back to the caller.

Note that the patch has overwritten 6 bytes (0xB8, 0x57, 0x00, 0x07, 0x80, 0xC2, 0x18, 0x00) and made the code after the RET non-functional!

Practically, when AmsiScanBuffer() will be called, it will immediately return an error and never scan the passed buffer for malicious code!

This technique is, by default, not malicious. All API calls are supported by Microsoft. There is not "hacking" techniques. Because DDL’s are loaded in the process environment, the process has access to the memory.

Of course, DLL’s can prevent this technique using different methods:

* DLL can be signed using a trusted certificate. This ensures that any modification to the DLL can be detected because the signature will no longer be valid.
* Integrity checks can be implemented to verify that the code has not been tampered. This can involve checksums, hash functions, or cryptographic signatures.
* Actively monitor for known hooking techniques such as inline hooks
* Monitor the memory protection (changed from "RX" to "RWX")

The code[[2](https://pastebin.com/a8aAz9B6)] is in Python but you could use any language that can use Windows API calls.

[1] [https://isc.sans.edu/diary/Why+Is+Python+so+Popular+to+Infect+Windows+Hosts/31208](https://isc.sans.edu/diary/Why%2BIs%2BPython%2Bso%2BPopular%2Bto%2BInfect%2BWindows%2BHosts/31208)
[2] <https://pastebin.com/a8aAz9B6>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Python](/tag.html?tag=Python) [Patching](/tag.html?tag=Patching) [API](/tag.html?tag=API) [Live](/tag.html?tag=Live) [Patch](/tag.html?tag=Patch) [AmsiScanBuffer](/tag.html?tag=AmsiScanBuffer) [Memory](/tag.html?tag=Memory)

[0 comment(s)](/diary/Live%2BPatching%2BDLLs%2Bwith%2BPython/31218/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31216)
* [next](/diary/31220)

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