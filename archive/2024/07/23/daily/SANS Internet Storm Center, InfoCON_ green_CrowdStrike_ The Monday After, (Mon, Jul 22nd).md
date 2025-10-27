---
title: CrowdStrike: The Monday After, (Mon, Jul 22nd)
url: https://isc.sans.edu/diary/rss/31098
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-23
fetch_date: 2025-10-06T17:46:03.553010
---

# CrowdStrike: The Monday After, (Mon, Jul 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31094)
* [next](/diary/31102)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [CrowdStrike: The Monday After](/forums/diary/CrowdStrike%2BThe%2BMonday%2BAfter/31098/)

**Published**: 2024-07-22. **Last Updated**: 2024-07-22 17:06:26 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/CrowdStrike%2BThe%2BMonday%2BAfter/31098/#comments)

Last Friday, after Crowdstrike released a bad sensor configuration update that caused widespread crashes of Windows systems. The most visible effects of these crashes appear to have been mitigated. I am sure many IT workers had to spend the weekend remediating the issue.

It is still early regarding the incident response part, but I would like to summarize some of the important facts we know and some lessons learned.

You are likely afected if the CrowdStrike sensor system retrieved updates between 0409 and 0527 UTC on Friday, July 19th. CrowdStrike allows users to configure a sensor update policy, which will delay the update of the sensor software. But the corrupt file was a configuration ("signature") update, not an update of the sensor itself. Configuration updates are always applied as soon as they are released. Customers do not have an option to delay these updates. Systems crashed because a kernel driver provided by CrowdStrike crashed as it read the malformed configuration file.

Since news of the incident broke, CrowdStrike has been updating and expanding its guidance. Your first stop should be Crowdstrikes "[Remediation and Guidance Hub](https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/)". It will link to all the resources CrowdStrike has to offer. Yesterday, CrowdStrike announced that they will soon offer a new, accelerated technique for recovery. As I write this, the new technique has not been published. CrowdStrike did provide a new dashboard to affected users to track systems affected by the update.

Microsoft developed a USB solution to simplify the process. To apply the update, systems must be booted from the USB key. However, Bitlocker-encrypted hosts may require a recovery key.

Bitlocker is the major hurdle to a speedy recovery for many affected organizations. [Ben Watsons posted on LinkedIn](https://www.linkedin.com/posts/ben-watson-792b092b_teamwork-crowdstrike-proud-ugcPost-7221053666449842177-QubD/) that his organization came up with a way to use a barcode scanner to simplify entering the recovery keys. I do not believe that the related code to create the barcodes is public.

It should be noted that there are some reports of scammers taking advantage of the incident. I reported on Friday about some phishing attempts and domains registered to take advantage of the incident. So far, we have not received a sample of a phishing e-mail, just reports that they had been seen. These phishing and malware emails may affect organizations not directly affected by the CrowdStrike problem. The extensive news coverage, often called a "Windows Problem", may prompt users into installing malicious files.

If you are affected: Only use tools provided by trustworthy sources. Refer to CrowdStrike's advice for guidance, and be careful with advice from others (including me :) ). Do not make far-reaching infrastructure changes before the incident is completely understood, and plan any changes carefully. This isn't the time to "rip out" CrowdStrike without first carefully evaluating alternatives. It may take a few weeks for CrowdStrike to completely understand what happened. Resiliency isn't just about avoiding outages. A big part is how to deal with outages that may happen. If you are not in the midst of recovering from CrowdStrike, Think about how you would deal with all your Windows Server (or Workstations) going down. How would you continue operations? Do you know where your Bitlocker recovery keys are?

If you are interested in recent domains registered to take advantage of the incident: Try our API. For example:

https://isc.sans.edu/api/recentdomains/today/crowdstrike?json

Instead of "crowdstrike," you may use other keywords or replace 'today' with a date in YYYY-MM-DD format. A suspect domain registered today: crowdstrike-fix.zip.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [crowdstrike](/tag.html?tag=crowdstrike)

[2 comment(s)](/diary/CrowdStrike%2BThe%2BMonday%2BAfter/31098/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31094)
* [next](/diary/31102)

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