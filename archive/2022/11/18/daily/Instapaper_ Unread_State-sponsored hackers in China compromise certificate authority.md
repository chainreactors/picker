---
title: State-sponsored hackers in China compromise certificate authority
url: https://arstechnica.com/information-technology/2022/11/state-sponsored-hackers-in-china-compromise-certificate-authority/
source: Instapaper: Unread
date: 2022-11-18
fetch_date: 2025-10-03T23:10:39.171312
---

# State-sponsored hackers in China compromise certificate authority

[Skip to content](#main)
[Ars Technica home](https://arstechnica.com/)

Sections

[Forum](/civis/)[Subscribe](/subscribe/)[Search](/search/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

* [Feature](/features/)
* [Reviews](/reviews/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

[Forum](/civis/)[Subscribe](/subscribe/)

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Pin to story

Theme

* HyperLight
* Day & Night
* Dark
* System

Search dialog...

Sign In

Sign in dialog...

Sign in

BILLBUG

# State-sponsored hackers in China compromise certificate authority

Active in dozens of advanced hacks since 2009, Billbug is still going strong.

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
–

Nov 15, 2022 3:51 pm
| [28](https://arstechnica.com/information-technology/2022/11/state-sponsored-hackers-in-china-compromise-certificate-authority/#comments "28 comments")

[![](https://cdn.arstechnica.net/wp-content/uploads/2022/11/tls-concept.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2022/11/tls-concept.jpg)

Credit:
Getty Images

Credit:
Getty Images

Text
settings

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Minimize to nav

Nation-state hackers based in China recently infected a certificate authority and several government and defense agencies with a potent malware cocktail for burrowing inside a network and stealing sensitive information, researchers said on Tuesday.

The successful compromise of the unnamed certificate authority is potentially serious, because these entities are trusted by browsers and operating systems to certify the identities responsible for a particular server or app. In the event the hackers obtained control of the organization’s infrastructure, they could use it to digitally sign their malware to make it more easily slip past endpoint protections. They might also be able to cryptographically impersonate trusted websites or intercept encrypted data.

While the researchers who discovered the breach found no evidence the certificate infrastructure had been compromised, they said that this campaign was only the latest by a group they call Billbug, which has a documented history of noteworthy hacks dating back to at least 2009.

“The ability of this actor to compromise multiple victims at once indicates that this threat group remains a skilled and well-resourced operator that is capable of carrying out sustained and wide-ranging campaigns,” Symantec researchers [wrote](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/espionage-asia-governments-cert-authority). “Billbug also appears to be undeterred by the possibility of having this activity attributed to it, with it reusing tools that have been linked to the group in the past.”

Symantec [first documented](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets) Billbug in 2018, when company researchers tracked the group under the name Thrip. The group hacked multiple targets, including a satellite communications operator, a geospatial imaging and mapping company, three different telecom operators, and a defense contractor. Of particular concern was the hack on the satellite operator because the attackers “seemed to be particularly interested in the operational side of the company, looking for and infecting computers running software that monitors and controls satellites.” The researchers speculated that the hackers’ motivation may have gone beyond spying to also include disruption.

The researchers eventually traced the hacking activity to computers physically located in China. Besides Southeast Asia, targets were also located in the US.

A little more than a [year later](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/thrip-apt-south-east-asia), Symantec gathered new information that allowed researchers to determine that Thrip was effectively the same as a longer-existing group known as Billbug or Lotus Blossom. In the 15 months since the first write-up, Billbug had successfully hacked 12 organizations in Hong Kong, Macau, Indonesia, Malaysia, the Philippines, and Vietnam. The victims included military targets, maritime communications, and media and education sectors.

Billbug used a combination of legitimate software and custom malware to burrow into its victims’ networks. Using legitimate software such as PsExec, PowerShell, Mimikatz, WinSCP, and LogMeIn allowed the hacking activities to blend in with normal operations in the compromised environments. The hackers also used the custom-built Catchamas info stealer and backdoors dubbed Hannotog and Sagerunex.

In the more recent campaign targeting the certificate authority and the other organizations, Billbug was back with Hannotog and Sagerunex, but it also used a host of new, legitimate software, including AdFind, Winmail, WinRAR, Ping, Tracert, Route, NBTscan, Certutil, and Port Scanner.

Tuesday’s post includes a host of technical details people can use to determine if they’ve been targeted by Billbug. Symantec is the security arm of Broadcom Software.

Listing image:
Getty Images

[![Photo of Dan Goodin](https://cdn.arstechnica.net/wp-content/uploads/2018/10/Dang.jpg)](https://arstechnica.com/author/dan-goodin/)

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
Senior Security Editor

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
Senior Security Editor

Dan Goodin is Senior Security Editor at Ars Technica, where he oversees coverage of malware, computer espionage, botnets, hardware hacking, encryption, and passwords. In his spare time, he enjoys gardening, cooking, and following the independent music scene. Dan is based in San Francisco. Follow him at [here](https://infosec.exchange/%40dangoodin) on Mastodon and [here](https://bsky.app/profile/dangoodin.bsky.social) on Bluesky. Contact him on Signal at DanArs.82.

[28 Comments](https://arstechnica.com/information-technology/2022/11/state-sponsored-hackers-in-china-compromise-certificate-authority/#comments "28 comments")

Comments

[Forum view](https://arstechnica.com/civis/threads/state-sponsored-hackers-in-china-compromise-certificate-authority.1487901/)

![Loading](https://cdn.arstechnica.net/wp-content/themes/ars-v9/public/images/firework-loader.75ab30.gif)

[Prev story](https://arstechnica.com/science/2022/11/is-tonight-the-night-that-nasas-massive-sls-rocket-finally-takes-flight/ "Go to: Is tonight the night that NASA’s massive SLS rocket finally takes flight?")

[Next story](https://arstechnica.com/gadgets/2022/11/apples-satellite-emergency-service-launches-in-the-us-and-canada/ "Go to: Apple’s satellite emergency service launches in the US and Canada")

Most Read

1. [![Listing image for first story in Most Read: Meet the Arc spacecraft: It aims to deliver cargo anywhere in the world in an hour](https://cdn.arstechnica....