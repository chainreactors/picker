---
title: Compiling Decompyle&#x2b;&#x2b; For Windows, (Wed, Dec 25th)
url: https://isc.sans.edu/diary/rss/31544
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-26
fetch_date: 2025-10-06T19:40:10.445042
---

# Compiling Decompyle&#x2b;&#x2b; For Windows, (Wed, Dec 25th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31542)
* [next](/diary/31546)

# [Compiling Decompyle++ For Windows](/forums/diary/Compiling%2BDecompyle%2BFor%2BWindows/31544/)

**Published**: 2024-12-25. **Last Updated**: 2024-12-25 07:58:25 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[1 comment(s)](/diary/Compiling%2BDecompyle%2BFor%2BWindows/31544/#comments)

Occasionaly I decompile Python code, with decompilers written in Python. Recently I discovered [Decompyle++](https://github.com/zrax/pycdc), a Python disassembler & decompiler written in C++.

It's very easy to compile for Linux, but a bit more difficult for Windows.

This is how I compiled Decompyle++ on Windows:

I used [Microsoft Visual Studio Community 2022](https://visualstudio.microsoft.com/vs/community/).

First I launch the Visual Studio 2022 Developer Command Prompt:

![](https://isc.sans.edu/diaryimages/images/20241222-110355.png)

![](https://isc.sans.edu/diaryimages/images/20241222-110421.png)

Then I download Decompyle++'s source code and navigate to the containing directory.

There I launch this command: cmake .

![](https://isc.sans.edu/diaryimages/images/20241222-111102.png)

And then I can start compilation (I'm compiling the Release configuration): msbuild pycdc.sln -t:Rebuild -p:Configuration=Release

![](https://isc.sans.edu/diaryimages/images/20241222-111225.png)

![](https://isc.sans.edu/diaryimages/images/20241222-111208.png)

And then I can find the disassembler (pycdas.exe) and decompiler (pycdc.exe) in the Release folder:

![](https://isc.sans.edu/diaryimages/images/20241222-111314.png)

Here I use pycdc.exe to decompile a .pyc file:

![](https://isc.sans.edu/diaryimages/images/20241224-150409.png)

In case you can't or don't want to  compile this yourself, I'm sharing the executables I compiled here.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[1 comment(s)](/diary/Compiling%2BDecompyle%2BFor%2BWindows/31544/#comments)

* [previous](/diary/31542)
* [next](/diary/31546)

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