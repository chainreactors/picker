---
title: More Brazil malspam pushing Astaroth (Guildma) in January 2023, (Thu, Jan 5th)
url: https://isc.sans.edu/diary/rss/29404
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-06
fetch_date: 2025-10-04T03:12:35.598188
---

# More Brazil malspam pushing Astaroth (Guildma) in January 2023, (Thu, Jan 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29400)
* [next](/diary/29408)

# [More Brazil malspam pushing Astaroth (Guildma) in January 2023](/forums/diary/More%2BBrazil%2Bmalspam%2Bpushing%2BAstaroth%2BGuildma%2Bin%2BJanuary%2B2023/29404/)

**Published**: 2023-01-05. **Last Updated**: 2023-01-05 20:24:45 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[0 comment(s)](/diary/More%2BBrazil%2Bmalspam%2Bpushing%2BAstaroth%2BGuildma%2Bin%2BJanuary%2B2023/29404/#comments)

***Introduction***

Tuesday 2023-01-03 and Wednesday 2023-01-04 revealed four Portuguese language emails targetging Brazil.  These messages are pushing the same type of **[Astaroth](https://malpedia.caad.fkie.fraunhofer.de/details/win.astaroth)** (Guildma) malware I've seen for the past several months.

*2023-01-05 update at 20:24 UTC: list of indicators, malware samples, and packet catpures (pcaps) from two infections related to this diary are now available **[here](https://www.malware-traffic-analysis.net/2023/01/04/index.html)**.*

On an infected Windows host, Astaroth malware is an **[AutoIt](https://www.autoitscript.com/wiki)** v3 script run by an AutoIt executable.  The executable is not inherently malicious on its own.  But AutoIt is so closely associated with malware that AutoIt's website has a wiki article noting legitimate AutoIt binaries are often detected as malicious by antivirus vendors (**[reference](https://www.secplicity.org/2021/06/29/autoit-malware-to-obfuscate-or-not-to-obfuscate/)**).

I've already posted ISC diaries about Astaroth malware in **[February 2022](https://isc.sans.edu/diary/Astaroth%2BGuildma%2Binfection/28346)** and **[August 2022](https://isc.sans.edu/diary/Brazil%2Bmalspam%2Bpushes%2BAstaroth%2BGuildma%2Bmalware/28962)**.  Today's diary presents two email templates from recent waves of malspam, and it briefly reviews artifacts from a persistent infection using AutoIt.

[![](https://isc.sans.edu/diaryimages/images/20232-01-05-ISC-diary-image-00.jpg)](https://isc.sans.edu/diaryimages/images/20232-01-05-ISC-diary-image-00.jpg)
*Shown above:  I should proabably say this is "so hot in Brazil right now."*

[![](https://isc.sans.edu/diaryimages/images/20232-01-05-ISC-diary-image-01a.jpg)](https://isc.sans.edu/diaryimages/images/20232-01-05-ISC-diary-image-01.jpg)
*Show above:  Flow chart for recent Astaroth (Guildma) infections.*

***Malspam Examples***

[![](https://isc.sans.edu/diaryimages/images/20232-01-05-ISC-diary-image-02a.jpg)](https://isc.sans.edu/diaryimages/images/20232-01-05-ISC-diary-image-02.jpg)
*Shown above:  Malspam from Tuesday 2023-01-03 pushing Astaroth malware.*

[![](https://isc.sans.edu/diaryimages/images/20232-01-05-ISC-diary-image-03a.jpg)](https://isc.sans.edu/diaryimages/images/20232-01-05-ISC-diary-image-03.jpg)
*Shown above:  Malspam from Wednesday 2023-01-04 pushing Astaroth malware.*

***Post-Infection Artifacts***

Astaroth malware infects a vulnerable Windows host through **[AutoIt](https://www.autoitscript.com/wiki)** script.  The malicious file is an AutoIt v3 compiled script made persistent through a Windows shortcut under the ***Startup Menu --> Programs --> Startup*** directory.  The malicious script is run by a legitimate AutoIt executable.

[![](https://isc.sans.edu/diaryimages/images/20232-01-05-ISC-diary-image-04a.jpg)](https://isc.sans.edu/diaryimages/images/20232-01-05-ISC-diary-image-04.jpg)
*Shown above:  Astaroth malware infection made persistent, early on Wendesday 2023-01-04.*

***Final Words***

The following are links from the four emails I've collected so far in 2023.

Links from first email on Tuesday 2023-01-03:

* hxxp://pka77.biagdum[.]review/X17pHJRhHlUB4/.qHANWxMqBxURxuh3O2/328883/CBM\_Ref0770590

Links from second email on Tuesday 2023-01-03:

* hxxp://i5ai2h.azuissu[.]directory/E07sWa0JVF3yJz3/ioJFa1sroWslVs3y7I1/357247/CBM\_Ref7732548

Links from first email on Wednesday 2023-01-04:

* hxxp://o6a3e.ulafeohash[.]world/Q13hCFaXNQ64X56/lzXQFOhWzChrNh642S5/93886/Imprimir\_DACTES
* hxxp://o6a3e.ulafeohash[.]world/Q13hCFaXNQ64X56/lzXQFOhWzChrNh642S5/8276833/4105\_CTe\_3360277200093886
* hxxp://o6a3e.ulafeohash[.]world/Q13hCFaXNQ64X56/lzXQFOhWzChrNh642S5/8276833/4105\_CTePDF\_3360277200093886

Links from second email on Wednesday 2023-01-04:

* hxxp://w1oieg.uripawuy[.]town/V19lKMAuK1WH6/r5KPQJkC5HkWAkxu9E1/22356/Imprimir\_DACTES
* hxxp://w1oieg.uripawuy[.]town/V19lKMAuK1WH6/r5KPQJkC5HkWAkxu9E1/5134464/4105\_CTe\_3360277200022356
* hxxp://w1oieg.uripawuy[.]town/V19lKMAuK1WH6/r5KPQJkC5HkWAkxu9E1/5134464/4105\_CTePDF\_3360277200022356

These URLs are geo-fenced, so they will not provide malware to an English language Windows host from an IP address based in the United States.

A zip archive containing the four emails is available **[here](https://github.com/brad-duncan/IOCs/blob/main/2023-01-03-and-01-04-Astaroth-Guildma-malspam-4-examples.zip)**.  Today's diary is a heads-up for this wave of Astaroth/Guildma activity.  I will soon post more technical details about the infection traffic on my blog at **[www.malware-traffic-analysis.net](https://www.malware-traffic-analysis.net/)**.

*2023-01-05 update at 20:24 UTC: list of indicators, malware samples, and packet catpures (pcaps) from two infections related to this diary are now available **[here](https://www.malware-traffic-analysis.net/2023/01/04/index.html)**.*

---
Brad Duncan
brad [at] malware-traffic-analysis.net

Keywords: [Astaroth](/tag.html?tag=Astaroth) [AutoIt](/tag.html?tag=AutoIt) [email](/tag.html?tag=email) [Guildma](/tag.html?tag=Guildma) [malspam](/tag.html?tag=malspam) [malware](/tag.html?tag=malware)

[0 comment(s)](/diary/More%2BBrazil%2Bmalspam%2Bpushing%2BAstaroth%2BGuildma%2Bin%2BJanuary%2B2023/29404/#comments)

* [previous](/diary/29400)
* [next](/diary/29408)

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