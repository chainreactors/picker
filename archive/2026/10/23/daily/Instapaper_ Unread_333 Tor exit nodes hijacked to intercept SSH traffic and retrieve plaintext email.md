---
title: 333 Tor exit nodes hijacked to intercept SSH traffic and retrieve plaintext email
url: https://arstechnica.com/information-technology/2026/10/300-tor-exit-nodes-hijacked-to-intercept-ssh-traffic-and-retrieve-plaintext-email/
source: Instapaper: Unread
date: 2026-10-23
fetch_date: 2026-10-24T06:48:20.992799
---

# 333 Tor exit nodes hijacked to intercept SSH traffic and retrieve plaintext email

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

[Search](/search/ "Search")

Sign In

Sign in dialog...

Sign in

POST-MORTEM

# 333 Tor exit nodes hijacked to intercept SSH traffic and retrieve plaintext email

For 3 days this month, 333 exit nodes were hacked in hopes of stealing sensitive data.

[Dan Goodin](https://arstechnica.com/author/dan-goodin/)
–

Oct 22, 2026 7:30 am
| [32](https://arstechnica.com/information-technology/2026/10/300-tor-exit-nodes-hijacked-to-intercept-ssh-traffic-and-retrieve-plaintext-email/#comments "32 comments")

[![In this photo illustration, the logo of Tor Browser (The Onion Router), an open source software is seen displayed on a smartphone.](https://cdn.arstechnica.net/wp-content/uploads/2026/10/GettyImages-1237260150-640x425.jpg)
![In this photo illustration, the logo of Tor Browser (The Onion Router), an open source software is seen displayed on a smartphone.](https://cdn.arstechnica.net/wp-content/uploads/2026/10/GettyImages-1237260150-1152x648.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2026/10/GettyImages-1237260150.jpg)

Credit:
[Photo Illustration by Pavlo Gonchar/SOPA Images/LightRocket via Getty Images](www.gettyimages.com/detail/news-photo/in-this-photo-illustration-the-logo-of-tor-browser-an-open-news-photo/1237260150)

Credit:
[Photo Illustration by Pavlo Gonchar/SOPA Images/LightRocket via Getty Images](www.gettyimages.com/detail/news-photo/in-this-photo-illustration-the-logo-of-tor-browser-an-open-news-photo/1237260150)

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

Unknown hackers hijacked more than 300 Tor exit nodes and reconfigured them to favor unencrypted email traffic and redirect SSH connections through servers they controlled, a researcher reported Tuesday.

The hijacking began in late August, when, [according to Tor volunteers](https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays%40lists.torproject.org/thread/QHRD6YOX6RZRDR7NCHNDO7GLCEA6VFM6/), the attacker used a valid password that had been reused to gain access to a Tor management server. The attacker then installed [Ebury](https://www.eset.com/us/about/newsroom/press-releases/eset-research-ebury-botnet-alive-growing/), a backdoor written for Linux that was discovered 12 years ago.

## Mysteries remain

Then the attacker connected from the management server to a second Tor server, called Switzerland2, through SSH, using an RSA key that, for unknown reasons, investigators couldn’t find among Switzerland2’s authorized keys. With administrative control of Switzerland2, the attackers installed Ebury there as well. Finally, the attacker reconfigured settings on two exit nodes that Switzerland2 hosted.

Ultimately, 333 exit relays were involved in the SSH and email interception campaign, although investigators haven’t established how the attackers gained control of all the underlying servers. The attackers then reconfigured the servers. One set of changes redirected SSH traffic traversing Tor to one of 12 attacker-controlled interceptor servers. Tor users who ignored warnings that the SSH host key had changed would then enter their SSH passwords.

A second set of changes caused the exit nodes to block ports 25, 465, 587, 993, and 995—used to accept various forms of encrypted email—while continuing to allow ports for receiving unencrypted email. If email services downgraded the connections, the attackers used their access to the exit nodes to obtain unencrypted messages. It’s unclear whether any such downgrade attempts succeeded. The hijacking occurred from October 2 to October 5.

Tor volunteers partially outlined the initial compromise of the management server and Switzerland2 and the attempt to intercept unencrypted email. [Tuesday’s report](https://kaba.cx/posts/20261020_Tor/) revealed many new details, including how many exit nodes were compromised and how the attackers used them to redirect SSH traffic.

“If you happen to get a circuit that exits over one of those 333 infected exit nodes, you won’t notice anything at first,” Kaba, the name of the Tor volunteer who authored the post, wrote. “Encrypted web traffic is forwarded as usual, but if you attempt an SSH connection over Port 22, you’re unknowingly redirected to one of 12 SSH interception servers. That’s exactly what happened to me on Friday morning.” Kaba then received the following warning:

> @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
> @ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @
> @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
> IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
> Someone could be eavesdropping on you right now (man-in-the-middle attack)!
> It is also possible that a host key has just been changed.
> The fingerprint for the ED25519 key sent by the remote host is
> SHA256:6baCZCPsl+AfQuujUS81fMEE/C7UeJ+AwjrImqmDB3E.
> Please contact your system administrator.

The volunteer investigated further and found that when people ignored the warning, the attacker (1) stole the SSH password, (2) opened a connection to the server and observed all typed commands, and (3) opened a second connection and infected the server with Ebury.

To investigate the campaign, Kaba created a script that polled all of Tor’s roughly 3,000 exit nodes to check whether they received a correct SSH fingerprint from a test server. The test server then checked whether the connection came from a pinned exit node or one of 12 SSH interception servers used by the attacker. The volunteer further set up a honeypot to observe the interception software attempting to log in and install Ebury.

Several mysteries remain. Tor volunteers still don’t know how the attackers accessed so many servers. One possibility is that a company hosting them was hacked, but the theory is inconclusive. Another open question is who is behind the attack. “The use of Ebury and the broad collection of unencrypted data point to a financially motivated crime group,” Kaba wrote. “Though this too is just speculation.”

A last perplexing finding: why did Switzerland2 accept an RSA key when there’s no evidence it was an authorized SSH certificate?

The takeaway from the event is the crucial role in-depth defense plays in preventing data theft in mass hacks like this one. Those measures include configuring email accounts to accept only encrypted traffic and reject unencrypted ports. Another is to disable password authentication in favor of SSH keys.

[![Photo ...