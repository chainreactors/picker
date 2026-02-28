---
title: Fake Fedex Email Delivers Donuts&#x21;, (Fri, Feb 27th)
url: https://isc.sans.edu/diary/rss/32754
source: SANS Internet Storm Center, InfoCON: green
date: 2026-02-27
fetch_date: 2026-02-28T04:01:32.575524
---

# Fake Fedex Email Delivers Donuts&#x21;, (Fri, Feb 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32748)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

# [Fake Fedex Email Delivers Donuts!](/forums/diary/Fake%2BFedex%2BEmail%2BDelivers%2BDonuts/32754/)

**Published**: 2026-02-27. **Last Updated**: 2026-02-27 12:22:12 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Fake%2BFedex%2BEmail%2BDelivers%2BDonuts/32754/#comments)

It’s Friday, let’s have a look at another simple piece of malware to close a busy week! I received a Fedex notification about a delivery. Usually, such emails are simple phishing attacks that redirect you to a fake login page to collect your credentials. Here, it was a bit different:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-1.png)

Nothing really fancy but it is effective and uses interesting techniques. The attached archive called "fedex\_shipping\_document.7z" (SHA256: a02d54db4ecd6a02f886b522ee78221406aa9a50b92d30b06efb86b9a15781f5 ) contains a Windows script (.bat file) with the same filename. This script, not really obfuscated and easy to understand, receiveds a low VT score, only 12/61!

First, il will generate some environment variables and implement persistence through a Run key:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-2.png)

The variable name "!contract" contains the path of a script copy in %APPDATA%\Rail\EXPRESSIO.cmd. The threat actor does not use the classic environment variable format “%VAR%” but “!var!”. This is expanded at execution time, meaning it reflects the current value inside loops and blocks[[1](https://ss64.com/nt/delayedexpansion.html)]. It’s enabled via this command

```

setlocal enableDelayedExpansion
```

Simple but nice trick to defeat simple search of "%..%"!

Then a PowerShell one-liner is invoked. The Powershell payload is located in the script (at the end) and Bas64-encoded. A nice trick is that the very first characters of the Base64 payload makes it undetectable by tools like base64dump! PowerShell extracts it through a regular expression:

Once the payload decoded, it is piped to another PowerShell:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-3.png)

The PowerShell implements different behaviors. First, it will create a Mutex on the victim’s computer:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-4.png)

Strange, it seems that some anti-debugging and anti-sandoxing are not completely implemented. By example, the scripts gets the number of CPU cores (a classic) but it’s never tested!

The script waits for the presence of an « explorer » process (which means that a user is logged in) otherwise it exists:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-5.png)

There is a long Base64-encoded variable that contains a payload that has been AES encrypted. The IV and salt are extracted and the payload decrypted. No time to loose, run the script into the Powershell debugger and dump the decrypted data in a file:
![](https://isc.sans.edu/diaryimages/images/isc-20260227-6.png)
The decrypted data is the next stage: a shellcode. This one will be injected into the explorer process and a new thread started:

![](https://isc.sans.edu/diaryimages/images/isc-20260227-7.png)

This behavior is typical to DonutLoader[[2](https://medium.com/%40anyrun/donutloader-malware-overview-00d9e3d79a48)].

The shell code connects to the C2 server: 204[.]10[.]160[.]190:7003. It's a good old XWorm!

[1] <https://ss64.com/nt/delayedexpansion.html>
[2] [https://medium.com/@anyrun/donutloader-malware-overview-00d9e3d79a48](https://medium.com/%40anyrun/donutloader-malware-overview-00d9e3d79a48)

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Donutloader](/tag.html?tag=Donutloader) [Malware](/tag.html?tag=Malware) [Phishing](/tag.html?tag=Phishing) [PowerShell](/tag.html?tag=PowerShell) [Shellcode](/tag.html?tag=Shellcode) [XWorm](/tag.html?tag=XWorm)

[0 comment(s)](/diary/Fake%2BFedex%2BEmail%2BDelivers%2BDonuts/32754/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/amsterdam-march-2026/course/reverse-engineering-malware-advanced-code-analysis) | Amsterdam | Mar 16th - Mar 20th 2026 |

* [previous](/diary/32748)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)