---
title: ScreenConnect Client (Ab)used by Attackers, (Thu, Oct 1st)
url: https://isc.sans.edu/diary/rss/33388
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-01
fetch_date: 2026-10-02T07:49:34.599391
---

# ScreenConnect Client (Ab)used by Attackers, (Thu, Oct 1st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33382)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [ScreenConnect Client (Ab)used by Attackers](/forums/diary/ScreenConnect%2BClient%2BAbused%2Bby%2BAttackers/33388/)

**Published**: 2026-10-01. **Last Updated**: 2026-10-01 05:32:13 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/ScreenConnect%2BClient%2BAbused%2Bby%2BAttackers/33388/#comments)

Threat Actors do not always use top-notch techniques or very complex malware to perform their attacks. Sometimes, they just abuse of existing applications...

I received a very simple phishing email:

```

From: contact@mejuri[.]com
To: <redacted>
Subject: EFT Wire Transfer

Paid Invoice Receipt

Dear Customer,
Payment of $5745.65 was Received.
Please click here to view your Order Information in PDF
If this charge wasn't authorized by you, contact our customer service to cancel and
receive an immediate refund.

Digitally Yours,
Customer Support: +1(332)638474823
```

“Click here” is a link pointing to:

```

hxxps://thelittlecupandsaucer[.]com[.]au/ScreenConnect.ClientSetup.exe
```

This email passed all the basic security controls. The link points to a real PE file. Today this attack vector will be blocked by browsers because downloaded an executable is suspicious!

The PE file was unknown on VT so I did a quick analysis of it. It’s a legit application: a ScreenConnect[[1](https://www.screenconnect.com)] client preconfigured to call-back a test account operated by the Attacker. Here is the configuration extracted from the PE file:

![](https://isc.sans.edu/diaryimages/images/isc-20261001.png)

|  |  |
| --- | --- |
| **Parameter** | **Value** |
| Relay (h) | instance-v2e3e2-relay.screenconnect.com |
| Port (p) | 443 |
| Instance ID | v2e3e2 (ConnectWise-hosted cloud) |
| Instance key (k) | RSA-2048 public key, blob SHA256 16b1cec1…9b00ead7 |

The PE is signed by ConnectWise, LLC (DigiCert G4 Code Signing CA1). The Authenticode digest matches the signed digest exactly. There's no overlay and nothing appended to or injected into the certificate table, so the signed-but-tampered config trick isn't used here.

Such tools are a gold mine for attackers because they are easy to deploy and trusted by most used! The list of “RMM” (Remote Monitoring and Management) tools is huge. Here is a brief list of the well-known ones;

* ScreenConnect
* AnyDesk
* TeamViewer
* LogMeIn
* Bomgar (BeyondTrust Remote Support)
* Zoho Assist
* Remote utilities like rutserv.exe
* NetSupport Manager
* SimpleHelp

If you want a better overview, check LOLRMM project [[2](https://lolrmm.io)] that maintains a list similar to the LOLBAS project!

[1] [https://www.screenconnect.com](https://www.screenconnect.com/)
[2] [https://lolrmm.io](https://lolrmm.io/)

Xavier Mertens (@xme)
Senior ISC Handler | SANS Principal Instructor | Freelance Consultant
[Xameco](https://xameco.be) | [PGP Key](https://xameco.be/pgpkey.txt)

Keywords: [Phishing](/tag.html?tag=Phishing) [RAT](/tag.html?tag=RAT) [Remote](/tag.html?tag=Remote) [RMM](/tag.html?tag=RMM) [RMMLOL](/tag.html?tag=RMMLOL) [ScreenConnect](/tag.html?tag=ScreenConnect)

[1 comment(s)](/diary/ScreenConnect%2BClient%2BAbused%2Bby%2BAttackers/33388/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33382)

### Comments

I think I'm missing something - you say the .exe would be blocked by browsers but ... if they didn't this'd be a valid vector? So, we're safe as long as the browsers etc. block downloading .exe files?

#### afbach

#### Oct 1st 2026 13 hours ago

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)