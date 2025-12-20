---
title: DLLs &#x26; TLS Callbacks, (Fri, Dec 19th)
url: https://isc.sans.edu/diary/rss/32580
source: SANS Internet Storm Center, InfoCON: green
date: 2025-12-19
fetch_date: 2025-12-20T03:15:32.856867
---

# DLLs &#x26; TLS Callbacks, (Fri, Dec 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32578)
* [next](/diary/32584)

# [DLLs & TLS Callbacks](/forums/diary/DLLs%2BTLS%2BCallbacks/32580/)

**Published**: 2025-12-19. **Last Updated**: 2025-12-19 10:55:26 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/DLLs%2BTLS%2BCallbacks/32580/#comments)

Xavier's diary entry "[Abusing DLLs EntryPoint for the Fun](https://isc.sans.edu/diary/Abusing%2BDLLs%2BEntryPoint%2Bfor%2Bthe%2BFun/32562/)" inspired me to do some tests with TLS Callbacks and DLLs.

TLS stands for Thread Local Storage. TLS Callbacks are an execution mechanism in Windows PE files that lets code run automatically when a process or thread starts, before the program’s normal entry point is reached. I've done tests in the past with EXEs and TLS Callbacks, but never with DLLs.

In Windows, TLS is used to give each thread its own copy of certain variables. To support this, the PE format has a TLS directory (IMAGE\_TLS\_DIRECTORY) that describes:

* Where TLS data is stored
* How large it is
* A list of callback functions

My [pecheck.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pecheck.py) tool lists TLS callbacks:

![](https://isc.sans.edu/diaryimages/images/20251217-193116.png)

I used the following code for a DLL with a TLS callback:

```

#include <windows.h>

// Declare TLS callback section
#pragma section(".CRT$XLB", read)

// TLS callback function
void NTAPI MyTlsCallback(PVOID hModule, DWORD dwReason, PVOID pReserved)
{
    if (dwReason == DLL_PROCESS_ATTACH)
    {
        MessageBoxA(NULL, "TLS Callback fired", "TLS", MB_OK);
    }
}

// Force linker to include TLS directory symbol
#ifdef _WIN64
#pragma comment(linker, "/INCLUDE:_tls_used")
#pragma comment(linker, "/INCLUDE:tls_callback_func")
#else
#pragma comment(linker, "/INCLUDE:__tls_used")
#pragma comment(linker, "/INCLUDE:_tls_callback_func")
#endif

// Place pointer in TLS callback section (extern "C" prevents mangling)
extern "C" __declspec(allocate(".CRT$XLB"))
PIMAGE_TLS_CALLBACK tls_callback_func = MyTlsCallback;

// Standard DllMain
BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{
    if (ul_reason_for_call == DLL_PROCESS_ATTACH)
        MessageBoxA(NULL, "DllMain fired", "DllMain", MB_OK);
    return TRUE;
}
```

And compiled it with Visual Studio C++:

```

cl /nologo /EHsc /LD tls_dll.cpp user32.lib
```

I used rundll32 to load the DLL.

The callback function got executed:

![](https://isc.sans.edu/diaryimages/images/20251217-193545.png)

before the DllMain function:

![](https://isc.sans.edu/diaryimages/images/20251217-193611.png)

This is something to take into account when performing static analysis: next to looking at DllMain and exported functions, look also at TLS callbacks (if any).

And it's also important when performing dynamic analysis: when using a debugger, make sure to check how it is configured:

![](https://isc.sans.edu/diaryimages/images/20251217-194453.png)

This debugger is configured to break on TLS callbacks: thus these callbacks will not execute unbeknownst to you.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/DLLs%2BTLS%2BCallbacks/32580/#comments)

* [previous](/diary/32578)
* [next](/diary/32584)

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