---
title: Fake BSOD Delivered by Malicious Python Script, (Fri, Feb 14th)
url: https://isc.sans.edu/diary/rss/31686
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-15
fetch_date: 2025-10-06T20:39:35.231094
---

# Fake BSOD Delivered by Malicious Python Script, (Fri, Feb 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31680)
* [next](/diary/31688)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Fake BSOD Delivered by Malicious Python Script](/forums/diary/Fake%2BBSOD%2BDelivered%2Bby%2BMalicious%2BPython%2BScript/31686/)

**Published**: 2025-02-14. **Last Updated**: 2025-02-14 12:18:05 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Fake%2BBSOD%2BDelivered%2Bby%2BMalicious%2BPython%2BScript/31686/#comments)

I found a Python script that implements a funny anti-analysis trick. The script has a low score on VT (4/59) (SHA256:d716c2edbcdb76c6a6d31b21f154fee7e0f8613617078b69da69c8f4867c9534)[[1](https://www.virustotal.com/gui/file/d716c2edbcdb76c6a6d31b21f154fee7e0f8613617078b69da69c8f4867c9534/detection)]. This sample attracted my attention because it uses the tkinter[[2](https://docs.python.org/3/library/tkinter.html)] library. This library is used to create graphical user interfaces (GUIs). It provides tools to create windows, dialogs, buttons, labels, text fields, and other interactive elements, allowing developers to build desktop applications with visual interfaces in Python. Most Python scripts are intended to be executed from a command line. That's why I consider this library as a good sign of suspicious behavior (It does not mean that all Python scripts using this library are malicious!)

While reviewing the script, a variable contains an interesting piece of text:

```

info = "\nA problem has been detected and windows has been shut down to prevent damage\nto your computer ... (removed) ..."
```

The interesting piece of code is here:

```

root = tk.Tk()
root.configure(background="dark blue")
ex = Example(root)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.wm_attributes("-topmost", 1)
root.mainloop()
```

The attribute "-topmost" set to "1" or "TRUE" will make the window remain open on top of all windows. The window will also be created to fill the screen without any control elements to close or resize it. When the script is executed, you will get this screen:

![](https://isc.sans.edu/diaryimages/images/isc-20250214-1.png)

To be honest, that's not the best BSOD ("Blue Screen of Death") that I saw... but it's a nice trick to annoy the victim or slow down (a bit) the analysis of the file.

[1] <https://www.virustotal.com/gui/file/d716c2edbcdb76c6a6d31b21f154fee7e0f8613617078b69da69c8f4867c9534/detection>
[2] <https://docs.python.org/3/library/tkinter.html>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Blue screen](/tag.html?tag=Blue screen) [BSOD](/tag.html?tag=BSOD) [GUI](/tag.html?tag=GUI) [TKInter](/tag.html?tag=TKInter) [TK](/tag.html?tag=TK) [Malware](/tag.html?tag=Malware) [Python](/tag.html?tag=Python)

[0 comment(s)](/diary/Fake%2BBSOD%2BDelivered%2Bby%2BMalicious%2BPython%2BScript/31686/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31680)
* [next](/diary/31688)

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