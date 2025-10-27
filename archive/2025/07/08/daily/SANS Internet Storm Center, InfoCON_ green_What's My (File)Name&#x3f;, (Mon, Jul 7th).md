---
title: What's My (File)Name&#x3f;, (Mon, Jul 7th)
url: https://isc.sans.edu/diary/rss/32084
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-08
fetch_date: 2025-10-06T23:50:23.640150
---

# What's My (File)Name&#x3f;, (Mon, Jul 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32080)
* [next](/diary/32088)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [What's My (File)Name?](/forums/diary/Whats%2BMy%2BFileName/32084/)

**Published**: 2025-07-07. **Last Updated**: 2025-07-07 07:54:54 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Whats%2BMy%2BFileName/32084/#comments)

Modern malware implements a lot of anti-debugging and anti-analysis features. Today, when a malware is spread in the wild, there are chances that it will be automatically sent into a automatic analysis pipe, and a sandbox. To analyze a sample in a sandbox, it must be "copied" into the sandbox and executed. This can happen manually or automatically. When people start the analysis of a suspicious file, they usually call it "sample.exe", "malware.exe" or "suspicious.exe". It's not always a good idea because it's can be detected by the malware and make it aware that "I'm being analyzed".

From a malware point of view, it's easy to detect this situation. Microsoft offers to Developers thousands of API calls that can be used for "malicious purposes". Let's have a look at GetModuleFileName()[[1](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea)]. This API call retrieves the fully qualified path for the file that contains the specified module. The module must have been loaded by the current process. Normally, a "module" refers to a DLL but, in the Microsoft ecosystem, the main program is also a "module" (like a DLL is also a PE file but with exported functions)

If you read carefully the API description, it expects 3 parameters but the first name can be omitted (set to NULL):

"*If this parameter is NULL, GetModuleFileName retrieves the path of the executable file of the current process.*"

Let's write a small program:

```

using System;
using System.Runtime.InteropServices;

class Program
{
    // Invoke declaration for GetModuleFileName
    [DllImport("kernel32.dll", CharSet = CharSet.Auto)]
    static extern uint GetModuleFileName(IntPtr hModule, [Out] char[] lpFilename, uint nSize);

    static void Main(string[] args)
    {
        const int maxPath = 260;
        char[] buffer = new char[maxPath];
        uint length = GetModuleFileName(IntPtr.Zero, buffer, (uint)buffer.Length);

        // Get the exec basename
        string fullPath = new string(buffer, 0, (int)length);
        string exeName = System.IO.Path.GetFileName(fullPath);

        // List of potential sample names
        string[] allowedNames = {
            "sample.exe",
            "malware.exe",
            "malicious.exe",
            "suspicious.exe",
            "test.exe",
            "submitted_sample.exe",
            "file.bin",
            "file.exe",
            "virus.exe",
            "program.exe"
        };

        foreach (var name in allowedNames)
        {
            if (string.Equals(exeName, name, StringComparison.OrdinalIgnoreCase))
            {
                // Executable name matched, silenyly exit!
                return;
            }
        }

        Console.WriteLine($"I'm {exeName}, looks good! Let's infect this host! }}:->");
    }
}
```

Let's compile and execute this file named "ISC\_20250707.exe":

![](https://isc.sans.edu/diaryimages/images/isc-20250707-1.png)

Once renamed as "malware.exe", the program will just silently exit! Simple but effective!

Of course, this is a simple proof-of-concept. In a real malware, there will be more tests implemented (ex: ignore the case) and the list of potential suspicious filenames will be obfuscated (or a dynamic list will be loaded from a 3rd-party website).

[1] <https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Antianalysis](/tag.html?tag=Antianalysis) [API](/tag.html?tag=API) [Detection](/tag.html?tag=Detection) [Filename](/tag.html?tag=Filename) [Malware](/tag.html?tag=Malware)

[0 comment(s)](/diary/Whats%2BMy%2BFileName/32084/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/32080)
* [next](/diary/32088)

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