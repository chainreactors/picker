---
title: ConnectWise Quietly Patches Flaw That Helps Phishers
url: https://krebsonsecurity.com/2022/12/connectwise-quietly-patches-flaw-that-helps-phishers/
source: Krebs on Security
date: 2022-12-02
fetch_date: 2025-10-04T00:20:48.460269
---

# ConnectWise Quietly Patches Flaw That Helps Phishers

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# ConnectWise Quietly Patches Flaw That Helps Phishers

December 1, 2022

[14 Comments](https://krebsonsecurity.com/2022/12/connectwise-quietly-patches-flaw-that-helps-phishers/#comments)

**ConnectWise**, which offers a self-hosted, remote desktop software application that is widely used by Managed Service Providers (MSPs), is warning about an unusually sophisticated phishing attack that can let attackers take remote control over user systems when recipients click the included link. The warning comes just weeks after the company quietly patched a vulnerability that makes it easier for phishers to launch these attacks.

![](https://krebsonsecurity.com/wp-content/uploads/2022/12/connectwisephish.png)

**ConnectWise Control** is extremely popular among MSPs that manage, protect and service large numbers of computers remotely for client organizations. Their product provides a dynamic software client and hosted server that connects two or more computers together, and provides temporary or persistent remote access to those client systems.

When a support technician wants to use it to remotely administer a computer, the ConnectWise website generates an executable file that is digitally signed by ConnectWise and downloadable by the client via a hyperlink.

When the remote user in need of assistance clicks the link, their computer is then directly connected to the computer of the remote administrator, who can then control the client’s computer as if they were seated in front of it.

While modern Microsoft Windows operating systems by default will ask users whether they want to run a downloaded executable file, many systems set up for remote administration by MSPs disable that user account control feature for this particular application.

In October, security researcher **Ken Pyle** alerted ConnectWise that their client executable file *gets generated based on client-controlled parameters*. Meaning, an attacker could craft a ConnectWise Control client download link that would bounce or proxy the remote connection from the MSP’s servers to a server that the attacker controls.

This is dangerous because many organizations that rely on MSPs to manage their computers often set up their networks so that only remote assistance connections coming from their MSP’s networks are allowed.

Using a free ConnectWise trial account, Pyle showed the company how easy it was to create a client executable that is cryptographically signed by ConnectWise and can bypass those network restrictions by bouncing the connection through an attacker’s ConnectWise Control server.

“You as the attacker have full control over the link’s parameters, and that link gets injected into an executable file that is downloaded by the client through an unauthenticated Web interface,” said Pyle, a partner and exploit developer at the security firm [Cybir](http://cybir.com). “I can send this link to a victim, they will click this link, and their workstation will connect back to my instance via a link on your site.”

[![](https://krebsonsecurity.com/wp-content/uploads/2022/12/pyleofpain.png)](https://krebsonsecurity.com/wp-content/uploads/2022/12/pyleofpain.png)

A composite of screenshots researcher Ken Pyle put together to illustrate the ScreenConnect vulnerability.

On Nov. 29, roughly the same time Pyle [published a blog post about his findings](https://cybir.com/2022/cve/hijacking-connectwise-control-and-ddos/), ConnectWise issued [an advisory](https://www.connectwise.com/company/trust/advisories) warning users to be on guard against a new round email phishing attempts that mimic legitimate email alerts the company sends when it detects unusual activity on a customer account.

“We are aware of a phishing campaign that mimics ConnectWise Control New Login Alert emails and has the potential to lead to unauthorized access to legitimate Control instances,” the company said.

ConnectWise said it released software updates last month that included new protections against the misdirection vulnerability that Pyle reported.  But the company said there is no reason to believe the phishers they warned about are exploiting any of the issues reported by Pyle.

“Our team quickly triaged the report and determined the risk to partners to be minimal,” said **Patrick Beggs**, ConnectWise’s chief information security officer. “Nevertheless, the mitigation was simple and presented no risk to partner experience, so we put it into the then-stable *22.8 build* and the then-canary *22.9 build*, which were released as part of our normal release processes. Due to the low severity of the issue, we didn’t (and don’t plan to) issue a security advisory or alert, since we reserve those notifications for serious security issues.”

Beggs said the phishing attacks that sparked their advisory stemmed from an instance that was not hosted by ConnectWise.

“So we can confirm they are unrelated,” he said. “Unfortunately, phishing attacks happen far too regularly across a variety of industries and products. The timing of our advisory and Mr. Pyle’s blog were coincidental. That said, we’re all for raising more awareness of the seriousness of phishing attacks and the general importance of staying alert and aware of potentially dangerous content.”

The ConnectWise advisory warned users that before clicking any link that appears to come from their service, users should validate the content includes “domains owned by trusted sources,” and “links to go to places you recognize.”

But Pyle said this advice is not terribly useful for customers targeted in his attack scenario because the phishers can send emails directly from ConnectWise, and the short link that gets presented to the user is a wildcard domain that ends in ConnectWise Control’s own domain name — screenconnect.com. What’s more, examining the exceedingly long link generated by ConnectWise’s systems offers few insights to the average user.

“It’s signed by ConnectWise and comes from them, and if you sign up for a free trial instance, you can email people invites directly from them,” Pyle said.

ConnectWise’s warnings come amid breach reports from another major provider of remote support technologies: **GoTo** [disclosed](https://www.goto.com/blog/our-response-to-a-recent-security-incident) on Nov. 30 that it is investigating a security incident involving “unusual activity within our development environment and third-party cloud storage services. The third-party cloud storage service is currently shared by both GoTo and its affiliate, the password manager service **LastPass**.

In [its own advisory on the incident](https://blog.lastpass.com/2022/11/notice-of-recent-security-incident/), LastPass said they believe the intruders leveraged information stolen during a previous intrusion in August 2022 to gain access to “certain elements of our customers’ information.”  However, LastPass maintains that its “customer passwords remain safely encrypted due to LastPass’s Zero Knowledge architecture.”

In short, that architecture means if you lose or forget your all-important master LastPass password — the one needed to unlock access to all of your other passwords stored with them — LastPass can’t help you with that, ...