---
title: Widespread Windows Crashes Due to Crowdstrike Updates, (Fri, Jul 19th)
url: https://isc.sans.edu/diary/rss/31094
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-20
fetch_date: 2025-10-06T17:44:27.945007
---

# Widespread Windows Crashes Due to Crowdstrike Updates, (Fri, Jul 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31086)
* [next](/diary/31098)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Widespread Windows Crashes Due to Crowdstrike Updates](/forums/diary/Widespread%2BWindows%2BCrashes%2BDue%2Bto%2BCrowdstrike%2BUpdates/31094/)

**Published**: 2024-07-19. **Last Updated**: 2024-07-19 16:59:59 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Widespread%2BWindows%2BCrashes%2BDue%2Bto%2BCrowdstrike%2BUpdates/31094/#comments)

Last night, endpoint security company Crowdstrike released an update that is causing widespread "blue screens of death" (BSOD) on Windows systems. Crowdstrike released an advisory, which is only available after logging into the Crowdstrike support platform. A brief public statement can be found [here](https://www.crowdstrike.com/blog/statement-on-windows-sensor-update/).

Crowdstrike now also published a detailed public document with tips to recover:

<https://www.crowdstrike.com/blog/statement-on-falcon-content-update-for-windows-hosts/>

---

**Update:** Some reports we have seen indicate that there may be phishing emails circulating claiming to come from "Crowdstrike Support" or "Crowdstrike Security". I do not have any samples at this point, but attackers are likely leveraging the heavy media attention. Please be careful with any "patches" that may be delivered this way.

One domain possibly associated with these phishing attacks is : crowdfalcon-immed-update [ .] com

---

Linux and MacOS systems are not affected by this issue.

The quickest fix appears to boot the system into "Windows Safemode with Network". This way, Crowdstrike will not start, but the current version may be downloaded and applied, which will fix the issue. This "quick version" of the fix is not part of Crowdstrike's recommendations but may be worth a try if you have many systems to apply the fix to or if you need to talk a non-computer-savvy person through the procedure. Some users have reported that this will succeed.

Casimir Pulaski (@cybermactex) mentioned on X that a simple reboot sometimes works if the latest update was downloaded before the system crashed.

The support portal statement offers the following steps to get affected systems back into business:

`CrowdStrike Engineering has identified a content deployment related to this issue and reverted those changes.`

`Workaround Steps:`

`1 - Boot Windows into Safe Mode or the Windows Recovery Environment`

`2 - Navigate to the C:\Windows\System32\drivers\CrowdStrike directory`

`3 - Locate the file matching “C-00000291*.sys”, and delete it.`

`4 - Boot the host normally.`

For a Bitlocker-protected system, you will have to provide the recovery key to delete the file.

Virtual systems are easier to fix as you should be able to just shut them down, mount the virtual disk to the host or a different virtual system (Linux? ;-) ), and remove the file.

Outages caused by this issue are far-reaching, with users on X reporting issues with Airports, 911 systems, banks, and media outlets. Please be patient with companies/workers affected by the issue.

This isn't the first time that security software has caused system crashes. Frequently, these issues are due to false positives marking system files as malicious.

Recently registered domains that may be related to Crowdstrike:

"crowdstrikeclaim.com"
"crowdstrikedown.site"
"crowdstrikeoutage.info"
"crowdstrikeupdate.com"
"crowdstrokeme.me"
"fix-crowdstrike-apocalypse.com"
"fix-crowdstrike-bsod.com"
"microsoftcrowdstrike.com"
"crowdfalcon-immed-update.com"

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [bsod](/tag.html?tag=bsod) [crowdstrike](/tag.html?tag=crowdstrike)

[0 comment(s)](/diary/Widespread%2BWindows%2BCrashes%2BDue%2Bto%2BCrowdstrike%2BUpdates/31094/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31086)
* [next](/diary/31098)

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