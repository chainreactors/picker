---
title: A Survey of Bluetooth Vulnerabilities Trends (2023 Edition), (Tue, Feb 7th)
url: https://isc.sans.edu/diary/rss/29522
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-08
fetch_date: 2025-10-04T06:00:54.080946
---

# A Survey of Bluetooth Vulnerabilities Trends (2023 Edition), (Tue, Feb 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29518)
* [next](/diary/29528)

# [A Survey of Bluetooth Vulnerabilities Trends (2023 Edition)](/forums/diary/A%2BSurvey%2Bof%2BBluetooth%2BVulnerabilities%2BTrends%2B2023%2BEdition/29522/)

**Published**: 2023-02-07. **Last Updated**: 2023-02-07 14:09:45 UTC
**by** [Yee Ching Tok](https://poppopretn.com/aboutme/) (Version: 1)

[1 comment(s)](/diary/A%2BSurvey%2Bof%2BBluetooth%2BVulnerabilities%2BTrends%2B2023%2BEdition/29522/#comments)

The use of Bluetooth-enabled devices remains popular. New products (such as mobile phones, laptops and fitness trackers) still support this protocol and have even launched with more recent versions (e.g. Samsung S23 family of phones, iPhone 14 and 14 Pro, Apple Watch Series 8/SE/Ultra all shipped with Bluetooth 5.3). I had previously written about surveying the trend of Bluetooth vulnerabilities back in 2021 [1]. As roughly a year or so has passed, it was a timely moment to review how things may have evolved with respect to the vulnerabilities discovered. Compared to the previous diary, the current Bluetooth core specification has been bumped up to 5.3 (from 5.2 as compared to the previous diary) [2].

Firstly, to get an overview of the current situation, I turned to the CVE List hosted by MITRE and searched for Bluetooth-related vulnerabilities. At the point of writing, there was a total of 647 publicly listed vulnerabilities related to Bluetooth [3]. From the time since I last wrote the diary (May 2021), there was an increase of 202 publicly disclosed vulnerabilities. To further illustrate the trend, I updated the previously plotted graph (Figure 1 below). There were minor updates to the number of vulnerabilities disclosed (e.g. 2019 and 2020), probably due to the lifting of embargoed vulnerability listing as they have been patched (or perhaps not being fixed after a certain period of non-disclosure). We also do not distinguish between Bluetooth Classic and Bluetooth Low Energy (LE) in the graph.

![Bluetooth Vulnerabilities from the Year 2002 to 2022](https://isc.sans.edu/diaryimages/images/Feb_2023_1_1(1).png)

**Figure 1:** Bluetooth Vulnerabilities from the Year 2002 to 2022

We can see that the vulnerabilities disclosed in 2022 have increased to near 2019 levels (112 vs 113). This came as no surprise, as the year 2022 was an eventful year for Bluetooth vulnerabilities. Notable attacks such as Blacktooth [4], Bluetooth Address Tracking (BAT) [5] and Bluetooth Physical-Layer Relay Attacks [6] were disclosed. The impacts were significant – the vulnerabilities affected many products, such as Tesla cars, smart locks and mobile phones. It was heartening to see that the researchers also suggested ways to fix the discovered issues and worked with the Bluetooth SIG to resolve the vulnerabilities.

It would be interesting to see what 2023 would be like for Bluetooth – would there be more implementation or protocol design vulnerabilities reported to the Bluetooth SIG? Will there be closer collaboration between product vendors and System-on-Chip (SoC) vendors in rolling out security updates for the Bluetooth implementations in the affected devices? Although it appears that the number of Bluetooth vulnerabilities being discovered is rising again, we can take comfort that at least a vital protocol is being examined and improved upon.

**References:**

[1] https://isc.sans.edu/diary/27460

[2] https://www.bluetooth.com/wp-content/uploads/2021/01/Bluetooth\_5.3\_Feature\_Enhancements\_Update.pdf

[3] https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=bluetooth

[4] https://dl.acm.org/doi/abs/10.1145/3548606.3560668

[5] https://dl.acm.org/doi/10.1145/3548606.3559372

[6] https://dl.acm.org/doi/10.1145/3507657.3528536

-----------
Yee Ching Tok, ISC Handler
[Personal Site](https://poppopretn.com)
[Mastodon](https://infosec.exchange/%40poppopretn)
[Twitter](https://twitter.com/poppopretn)

Keywords: [Bluetooth](/tag.html?tag=Bluetooth)

[1 comment(s)](/diary/A%2BSurvey%2Bof%2BBluetooth%2BVulnerabilities%2BTrends%2B2023%2BEdition/29522/#comments)

* [previous](/diary/29518)
* [next](/diary/29528)

### Comments

It would be interesting to add data around devices, types of devices, numbers, etc... over the years, more and more bluetooth enabled devices were created and are being used.

#### 0x58

#### Feb 7th 2023 2 years ago

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