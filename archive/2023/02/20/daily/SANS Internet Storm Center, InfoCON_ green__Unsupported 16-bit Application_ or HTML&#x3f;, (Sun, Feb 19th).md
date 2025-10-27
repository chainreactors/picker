---
title: "Unsupported 16-bit Application" or HTML&#x3f;, (Sun, Feb 19th)
url: https://isc.sans.edu/diary/rss/29562
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-20
fetch_date: 2025-10-04T07:33:58.452059
---

# "Unsupported 16-bit Application" or HTML&#x3f;, (Sun, Feb 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29560)
* [next](/diary/29564)

# ["Unsupported 16-bit Application" or HTML?](/forums/diary/Unsupported%2B16bit%2BApplication%2Bor%2BHTML/29562/)

**Published**: 2023-02-19. **Last Updated**: 2023-02-19 09:53:10 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[1 comment(s)](/diary/Unsupported%2B16bit%2BApplication%2Bor%2BHTML/29562/#comments)

Sometimes I download a Windows executable and when I run it, I get an error message "Unsupported 16-bit Application":

![](https://isc.sans.edu/diaryimages/images/20230219-104240.png)

This happens when I download a Windows executable via the command-line, and fail to pay attention to the URL.

Like this executable on GitHub:

![](https://isc.sans.edu/diaryimages/images/20230219-104100.png)

Downloading with curl from this URL:

![](https://isc.sans.edu/diaryimages/images/20230219-104216.png)

And when I run this, I get the Unsupported 16-bit Application" error. That's because I made a mistake, and downloaded the HTML page from GitHub in stead of the PE file:

![](https://isc.sans.edu/diaryimages/images/20230219-104300.png)

When you make this mistake, Windows will often show you that 16-bit error.

With this example from GitHub, I should have downloaded with the "raw" URL.

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [html](/tag.html?tag=html) [windows](/tag.html?tag=windows) [16bit](/tag.html?tag=16bit)

[1 comment(s)](/diary/Unsupported%2B16bit%2BApplication%2Bor%2BHTML/29562/#comments)

* [previous](/diary/29560)
* [next](/diary/29564)

### Comments

Remember .COM files from MS-DOS?
They were only 64KB big, didn't had a file header and weren't relocatable.

This strongly reminds me of them.

#### Tom

#### Feb 19th 2023 2 years ago

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