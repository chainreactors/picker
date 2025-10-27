---
title: Zero Trust and Entra ID Conditional Access, (Sun, Jan 19th)
url: https://isc.sans.edu/diary/rss/31602
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-20
fetch_date: 2025-10-06T20:10:17.484244
---

# Zero Trust and Entra ID Conditional Access, (Sun, Jan 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31600)
* [next](/diary/31608)

# [Zero Trust and Entra ID Conditional Access](/forums/diary/Zero%2BTrust%2Band%2BEntra%2BID%2BConditional%2BAccess/31602/)

**Published**: 2025-01-19. **Last Updated**: 2025-01-19 02:48:18 UTC
**by** [Tony Carothers](/handler_list.html#tony-carothers) (Version: 1)

[0 comment(s)](/diary/Zero%2BTrust%2Band%2BEntra%2BID%2BConditional%2BAccess/31602/#comments)

Microsoft Entra ID (Formerly Azure AD) Conditional Access (CA) policies are the key components to a Zero Trust strategy, as it provides the ability to function as the front door for users and devices. CA policies use attributes, or signals, of various components as variables to be used to enforce specific access controls. Attributes include user and device attributes, such as location and device risk. By defining and controlling the conditions in which access is granted, we can reduce risk and enhance security.

Conditional access is a cornerstone of a Zero Trust strategy. The ability to explicitly verify, evaluate context, and leveraging adaptive access on a continuous basis allows for granular access control and monitoring. Key benefits of using conditional access in a Zero Trust framework include a reduced attack surface and enhanced dynamic security. Organizations can enforce ‘trust but verify’ principles and ensure that only authorized users have access to assets and resources, on a dynamic basis.

A Conditional Access policy can be broken down into two components: conditions and controls.

Conditions define under which circumstances access is granted; they can also be used to explicitly deny. The conditions evaluated are primarily user, app, and device focused, such as user risk or device compliance. One example of a CA policy may state that a Windows 10 device must have current malware and signatures applied.

A control is a set of actions to be taken when conditions are met. By defining what actions occur when given a certain set of attributes exist, security automation and orchestration begins to take place. Access can be granted, blocked, or on hold until risk is remediated. To use the above antimalware example, a CA policy that requires a current AV signature to grant access would block an out-of-date signature, and then redirect the user to update the AV signature.

Entra ID CA is only one platform that has Security Orchestration capabilities, many security platforms in use today have added enhanced capabilities, and updated the user experience, to support Zero Trust.

For additional information, please visit the [Conditional Access overview](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) page, and note at the bottom how these functions contribute to Zero Trust.

tony d0t carothers --gmail

Keywords:

[0 comment(s)](/diary/Zero%2BTrust%2Band%2BEntra%2BID%2BConditional%2BAccess/31602/#comments)

* [previous](/diary/31600)
* [next](/diary/31608)

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