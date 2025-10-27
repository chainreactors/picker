---
title: My Very Personal Guidance and Strategies to Protect Network Edge Devices, (Thu, Feb 6th)
url: https://isc.sans.edu/diary/rss/31660
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-18
fetch_date: 2025-10-06T20:49:02.765987
---

# My Very Personal Guidance and Strategies to Protect Network Edge Devices, (Thu, Feb 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31658)
* [next](/diary/31664)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [My Very Personal Guidance and Strategies to Protect Network Edge Devices](/forums/diary/My%2BVery%2BPersonal%2BGuidance%2Band%2BStrategies%2Bto%2BProtect%2BNetwork%2BEdge%2BDevices/31660/)

**Published**: 2025-02-06. **Last Updated**: 2025-02-17 12:51:04 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/My%2BVery%2BPersonal%2BGuidance%2Band%2BStrategies%2Bto%2BProtect%2BNetwork%2BEdge%2BDevices/31660/#comments)

Last week, CISA and other national cyber security organizations published an extensive document outlining "Guidance and Strategies to Protect Network Edge Devices." [1] The document is good but also very corporate and "bland." It summarizes good, well-intended advice that will help you secure edge devices. But reading it also made me think, "That's it?" Not that I expected earth-shattering advice eliminating vulnerabilities brought on by accumulating deceased worth of abandoned ware still peddled at often relatively high costs. But I don't know; maybe something more actionable would be helpful.

So here is my advice from the small network that is maintained, like so many, "on the side" and not by a team of dedicated edge device experts.

### 0 - Limit Access to Admin Functions

Before you do anything, limit access to admin interfaces, and do not forget access via SSH or APIs. At the bare minimum, access should only be available via the LAN interface. Carefully select any exposed services. SSH may be an option if you must have remote access or a VPN solution (many devices support Wireguard, OpenVPN, or other protocols). But the fewer options you enable, the better. Avoid exposing web-based APIs, admin interfaces, or SSL VPN gateways at all costs. HTTPs will not protect you in this case. The issue is numerous web application vulnerabilities that keep popping up in these devices. Move any exposed admin services (HTTPS or SSH) to non-default ports.

Removing internet access to admin features will eliminate the vast majority of threats. If you must expose a VPN or SSH, continue reading.

### 1 - Change Credentials and use MFA

Maybe this should be 0. Either way, Change your credentials. Your device doesn’t support MFA? Get a different one! Even open-source solutions usually support some kind of MFA these days. OPNSense makes it a bit painful, but it works. Maybe even use a different username instead of "admin" and disable "admin"/"root" if that is an option. It helps a bit. Harden protocols like SSH by using keys.

### 2 - Define a monthly "Router Update Day."

I don't care when. Third Thursday of the month, mornings, 10 am? Check if there is an update waiting; check the release notes. Is it important? Apply now. Can it wait? Apply later. Having redundant perimeter devices should be doable even for a smaller network. Add a monthly "perimeter update" reminder to your calendar. Some device manufacturers have mailing lists to notify you of updates or release updates on a specific schedule.

### 3 - Stay Open Source

Some may not agree with this advice. Commercial permitter security devices are often counterproductive. You can find well-respected, preconfigured, open-source perimeter security devices. For smaller networks, OpenWRT will work great. Use PFSense or OPNSense if you operate a more complex network or need additional features. Open-source packages provide much longer support timelines for existing hardware. Updates are usually painless, support is easy to come by, and, most importantly, You will have more insight into how the device works. Commercial systems make it sound like it is worth spending a lot of money to get less: A black box with a lot of magic packet dust. However, you will not be able to understand how the device works and how to debug it effectively. Some people say that you "pay with your time". The opposite is true in this case: Understanding and maintaining a closed-source solution for perimeter security devices is often more time-consuming or MUCH MORE expensive.

If it makes the boss happy, Buy a support contract. Multiple companies or developers behind the particular solution will offer commercial support contracts at competitive prices for all the open-source solutions mentioned above.

### 4 - Mark the Devices Expiration Date

Every device has an expiration date. As you purchase it, define how long the device will be in your network. Keep yourself honest. Apply a sticker to the device noting when and where it was purchased (nice for warranty, too) and when it is supposed to be replaced.

### 5 - Create Automated Configuration Backups

Once a day? The important part is to automate it. It will not happen unless you automate it. These configuration backups are essential for configuration downgrades to recover from a lousy upgrade quickly or if you need to replace a device. Sadly, this often requires a distinct process.

### 6 - Edge Devices are Endpoints too

So install endpoint protection software! OPNsense supports Wazuh (I think PFSense, too). Find out what works for your device. At the very least, monitor unapproved changes to the configuration backups. This may be an area where you want to spend some money on commercial software if needed and if it is applicable.

[1] https://www.cisa.gov/resources-tools/resources/guidance-and-strategies-protect-network-edge-devices

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [vpn](/tag.html?tag=vpn) [firewall](/tag.html?tag=firewall) [edge devices](/tag.html?tag=edge devices)

[0 comment(s)](/diary/My%2BVery%2BPersonal%2BGuidance%2Band%2BStrategies%2Bto%2BProtect%2BNetwork%2BEdge%2BDevices/31660/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31658)
* [next](/diary/31664)

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
Developers: We have an [API](/api/) for you!   [![Creative Commons License]...