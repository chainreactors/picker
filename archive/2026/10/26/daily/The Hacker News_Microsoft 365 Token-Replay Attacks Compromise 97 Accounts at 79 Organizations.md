---
title: Microsoft 365 Token-Replay Attacks Compromise 97 Accounts at 79 Organizations
url: https://thehackernews.com/2026/10/microsoft-365-token-replay-attacks.html
source: The Hacker News
date: 2026-10-26
fetch_date: 2026-10-27T07:05:44.227297
---

# Microsoft 365 Token-Replay Attacks Compromise 97 Accounts at 79 Organizations

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Microsoft 365 Token-Replay Attacks Compromise 97 Accounts at 79 Organizations](https://thehackernews.com/2026/10/microsoft-365-token-replay-attacks.html)

**Ravie Lakshmanan**Oct 26, 2026Identity Security / Email Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKwJ8hpTcgaV_VMCyzQDPQQOPlZmmE3Fg-XAOrUfFazMKgVGEoT7OHQgWhyJLhCpHO6Hvp35u_YZGBfyGXAuJfpwP4BriicsNfvhPXjq4BzNyULVQPzNCWzmSIGnDLN7P2RNW2sfm15qZxLrVzpDg8FvOcGTZBhMsBFPH3IhiV1k3NdGAHFRC7kkKaOMMn/s1700-nu-rw-lo-l85-e365/contoso.jpg)

Cybersecurity researchers have disclosed a Microsoft 365 campaign that has been observed leveraging an adversary-in-the-middle ([AitM](https://thehackernews.com/2026/01/microsoft-flags-multi-stage-aitm.html)) relay to capture sign-in sessions and then replay the stolen tokens to break into email accounts at 79 organizations.

Huntress, which [observed](https://www.huntress.com/blog/token-replay-spray) the activity between July 14 and September 22, 2026, said it detected 497 successful Microsoft 365 sign-in events across the victim organizations from over 200,000 login attempts, with the attackers ultimately compromising 97 accounts and registering 48 rogue Entra devices.

"Rather than guessing passwords, the attacker replayed sign-in tokens stolen from victims, and we've traced more than 200,000 failed login attempts from the campaign window back to the 193.26.115[.]0/24 IP range," Huntress researchers Andrea Hatcher, Susannah Matt, Matt Poto, and Andrew Schwartz said.

The attack has been found to employ an AitM login page, which sits between the victims and legitimate Microsoft infrastructure to capture the entered credentials and MFA codes and relay the information to the real login page.

The end goal is to collect the access token issued by Microsoft following the sign-in process so that it doesn't have to bypass MFA a second time. The "proof of login" token is subsequently replayed by the attacker from their own devices within minutes to conduct automated sign-in attempts against Microsoft 365 services.

The approach has been codenamed token spraying, as it involves the attacker replaying many stolen tokens at scale across several organizations in a manner that's analogous to password spraying.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Upon gaining successful access, the attackers moved to add their own authenticator app as a form of persistence to complete MFA challenges for new sign-ins and overcome scenarios where the stolen session token expires or gets revoked by the victim.

In no less than 19 organizations, the victim's existing MFA methods were removed and a new method registered within three hours of the first sign-in. In one case observed on July 21, 2026, the threat actors activated a new authenticator app named "iPhone 13" less than 51 minutes after the session was hijacked.

"Rogue devices served the same purpose," the researchers said. "The threat actor registered at least 48 fake computers in victim organizations' Microsoft directories. A registered device can give the attacker a more durable way to request tokens than the stolen session alone, and it stays in the directory until someone deletes it."

Furthermore, the attackers have also been spotted setting up hidden email rules in victims' inboxes with names such as ".," "sss," "ss," "iT," ",.," "........," "s," and "d" to delete incoming mail with certain keywords referencing payroll, deposit, and bonus, or move them to obscure folders like RSS Feeds and Conversation History.

In one compromised mailbox, the email rule marked all incoming messages as read and deleted them. The mailbox was then used to send outbound spam to hundreds of external recipients before Microsoft Entra ID Protection rated the account high risk.

Huntress said the tokens originate from multiple sources, including AitM relays behind fake sign-in pages, [device-code phishing](https://thehackernews.com/2026/09/microsoft-takes-down-eviltokens-device.html), and social engineering during a legitimate login process.

The campaign was first observed from a Romanian IP address "[193.26.115[.]221](https://www.virustotal.com/gui/ip-address/193.26.115.221/detection)," which, according to VirusTotal, is used by a remote access trojan called AsyncRAT. The IP address is associated with a German hosting provider named 1337 Services GmbH.

Data from GreyNoise currently lists [29 IP addresses](https://viz.greynoise.io/ips?q=metadata.organization:%221337+Services+GmbH%22) matching the hosting provider, out of which [10 have been flagged](https://viz.greynoise.io/ips?q=metadata.organization:%221337+Services+GmbH%22+AND+classification:malicious) as malicious and five are marked suspicious. Notably, the entity is linked to [StarkRDP](https://web.archive.org/web/20210924052821/https%3A//starkrdp.io/imprint.php) and [rdp[.]sh](https://rdp.sh/privacy), which allows [paying customers](https://hackforums.net/showthread.php?tid=6292267) to rent virtual servers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The domains tied to both StarkRDP and rdp[.]sh were [taken down](https://thehackernews.com/2025/01/authorities-seize-domains-of-popular.html), alongside websites for Nulled, Cracked, and Sellix, as part of an [international law enforcement operation](https://lowendtalk.com/discussion/202302/fbi-seizes-starkrdp-and-possibly-rdp-sh) dubbed Talent in January 2025. As of writing, the two platforms are operational, with the former now rebranded as [exy[.]sh](https://exy.sh/).

"StarkRDP has always been operating by the law and is not involved in any of these alleged crimes, and the legal process will confirm this," the StarkRDP Telegram account said in a post dated January 30, [according](https://krebsonsecurity.com/2025/02/whos-behind-the-seized-forums-cracked-nulled/) to independent cybersecurity journalist Brian Krebs.

"The only things t...