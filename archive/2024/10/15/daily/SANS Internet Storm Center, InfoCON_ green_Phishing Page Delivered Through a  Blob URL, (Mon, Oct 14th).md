---
title: Phishing Page Delivered Through a  Blob URL, (Mon, Oct 14th)
url: https://isc.sans.edu/diary/rss/31350
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-15
fetch_date: 2025-10-06T18:54:46.356164
---

# Phishing Page Delivered Through a  Blob URL, (Mon, Oct 14th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31346)
* [next](/diary/31354)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Phishing Page Delivered Through a Blob URL](/forums/diary/Phishing%2BPage%2BDelivered%2BThrough%2Ba%2BBlob%2BURL/31350/)

**Published**: 2024-10-14. **Last Updated**: 2024-10-14 07:37:44 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Phishing%2BPage%2BDelivered%2BThrough%2Ba%2BBlob%2BURL/31350/#comments)

I receive a lot of spam in my catch-all mailboxes. If most of them are not interesting, some still attract my attention. Especially the one that I'll describe in this diary. The scenario is classic, an important document is pending delivery but... the victim needs to authenticate to get the precious! As you can see in the screenshot below, the phishing kit supports well-known service providers.

![](https://isc.sans.edu/diaryimages/images/isc-20241014-1.png)

But check carefully the URL: It starts with "blob:"! Usually, BLOBs are used to represent "Binary Large OBjects". In the context of a browser, an object URL[[1](https://en.wikipedia.org/wiki/Blob_URI_scheme)] is a pseudo protocol to allow blob and file objects to be used as URL sources for things like images, download links for binary data, and so forth. It's part of the URL specification for handling binary data that needs to be referenced or accessed as an actual file, even if it doesn't exist as a physical file on a server.

In the context of this phishing kit, the attacker generated the landing page in a blob to remain stealthy. Let's have a look at the code:

```

function saveFile(name, type, data) {
    if (data != null && navigator.msSaveBlob)
        return navigator.msSaveBlob(new Blob([data], { type: type }), name);
    var a = $("<a style='display: none;'/>");
    var encodedStringAtoB = " ... [Base64-encode-data] ... "
    var decodedStringAtoB = atob(encodedStringAtoB);
    const myBlob = new Blob([decodedStringAtoB], { type: 'text/html' });
    const url = window.URL.createObjectURL(myBlob);
    a.attr("href", url);
    $("body").append(a);
    a[0].click();
    window.URL.revokeObjectURL(url);
    a.remove();
}
```

In JavaScript, you create a Blob with window.URL.createObjectURL().

Note that if you provided "valid" credentials, the phishing kit will ask you for more personal details:

![](https://isc.sans.edu/diaryimages/images/isc-20241014-2.png)

Finally, the victim will get a fake document downloaded from hxxps://www[.]Mississauga[.]ca/wp-content/uploads/2021/01/14114418/EFT-Agreement-Form.pdf:

![](https://isc.sans.edu/diaryimages/images/isc-20241014-3.png)

[1] <https://en.wikipedia.org/wiki/Blob_URI_scheme>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [URI](/tag.html?tag=URI) [URL](/tag.html?tag=URL) [Blob](/tag.html?tag=Blob) [Phishing](/tag.html?tag=Phishing)

[0 comment(s)](/diary/Phishing%2BPage%2BDelivered%2BThrough%2Ba%2BBlob%2BURL/31350/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31346)
* [next](/diary/31354)

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