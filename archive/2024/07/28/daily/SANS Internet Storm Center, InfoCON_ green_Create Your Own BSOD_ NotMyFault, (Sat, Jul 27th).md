---
title: Create Your Own BSOD: NotMyFault, (Sat, Jul 27th)
url: https://isc.sans.edu/diary/rss/31120
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-28
fetch_date: 2025-10-06T17:42:03.006012
---

# Create Your Own BSOD: NotMyFault, (Sat, Jul 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31118)
* [next](/diary/31122)

# [Create Your Own BSOD: NotMyFault](/forums/diary/Create%2BYour%2BOwn%2BBSOD%2BNotMyFault/31120/)

**Published**: 2024-07-27. **Last Updated**: 2024-07-27 18:10:57 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Create%2BYour%2BOwn%2BBSOD%2BNotMyFault/31120/#comments)

With all the Blue Screen Of Death screenshots we saw lately, I got the idea to write about Sysinternals' tool [NotMyFault](https://learn.microsoft.com/en-us/sysinternals/downloads/notmyfault).

Say that you want to practice handling BSODs, or that you need to document and test a procedure to handle BSODs.

How do you cause a BSOD? One method to achieve this, is to use Sysinternals tool [NotMyFault](https://learn.microsoft.com/en-us/sysinternals/downloads/notmyfault) (don't do this on a production machine):

![](https://isc.sans.edu/diaryimages/images/20240727-190810.png)

Click button Crash to immediately crash the machine (you will lose all unsaved data):

![](https://isc.sans.edu/diaryimages/images/20240727-190853.png)

Once the machine is rebooted, you can use the windows debugger [WindDBG](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) or [BlueScreenView](https://www.nirsoft.net/utils/blue_screen_view.html#google_vignette) to analyze what caused the crash:

![](https://isc.sans.edu/diaryimages/images/20240727-191122.png)

Load the dump:

![](https://isc.sans.edu/diaryimages/images/20240727-191232.png)

Type command !analyze -v:

![](https://isc.sans.edu/diaryimages/images/20240727-191316.png)And it tells use that this crash was caused by driver myfault.sys.

If you don't want to install WinDBG, BlueScreenView works without installing:

![](https://isc.sans.edu/diaryimages/images/20240727-191458.png)

To perform the analysis on another machine, retrieve c:\windows\memory.dmp and/or c:\windows\minidump\\*.dmp files from the crashed machine, and load them in WindDBG or BlueScreenView on another machine.

Once you know what caused the crash, you can disable the driver and start looking for a fix.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Create%2BYour%2BOwn%2BBSOD%2BNotMyFault/31120/#comments)

* [previous](/diary/31118)
* [next](/diary/31122)

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