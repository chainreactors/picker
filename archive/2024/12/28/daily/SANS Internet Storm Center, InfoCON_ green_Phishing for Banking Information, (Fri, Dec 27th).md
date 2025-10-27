---
title: Phishing for Banking Information, (Fri, Dec 27th)
url: https://isc.sans.edu/diary/rss/31548
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-28
fetch_date: 2025-10-06T19:40:15.108467
---

# Phishing for Banking Information, (Fri, Dec 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31546)
* [next](/diary/31550)

# [Phishing for Banking Information](/forums/diary/Phishing%2Bfor%2BBanking%2BInformation/31548/)

**Published**: 2024-12-27. **Last Updated**: 2024-12-27 10:25:02 UTC
**by** [Phishing,Banking,Exploit](/handler_list.html#phishing,banking,exploit) (Version: 1)

[0 comment(s)](/diary/Phishing%2Bfor%2BBanking%2BInformation/31548/#comments)

It is again the time of the year when scammers are asking to verify banking information, whether it is credit cards, bank card, package shipping information, winning money, etc. Last night I received a text message to verify a credit card, it is case a Bank of Montreal (BMO) credit card.

From Bank of Montreal (BMO) website scam alerts, they uses a specific SMS number to send a text to their consumers: "The only BMO Alert you will receive on your mobile device via SMS regarding your accounts and credit cards will come from our 6-digit number “266898.” Our code never changes, so use this code to determine if it is BMO messaging you." [[1](https://www.bmo.com/en-ca/main/personal/security-centre/scam-alerts/)] It is important to know how a bank will contact your by SMS. This is a copy of the text I received.

![](https://isc.sans.edu/diaryimages/images/Phishing_BMO.png)

**Is it Phishing? Any Suspicious Clues that Stand Out?**

* The text I received was from a (438) area code and not from BMO, that is the first error.
* The second error is the card number "Starting in 5510 29\*\*" which normally is the last 4 digits of the card that appears on statements vs. the beginning.
* The last clue is the website that contains spelling errors: bmo-securltyverlfy1[.]com [[4](https://www.hybrid-analysis.com/sample/c76cbf6e22734f177e024e1fee02ed17a53413e0dfee02c6a6601be28280b167)] -> The website is spelled with the letter "l" vs the letter "i". This domain was registered on the 2024-12-11 [[5](https://www.scamadviser.com/check-website/bmo-securltyverlfy1.com?utm_source=hybridanalysis)] just in time for the holiday season.

**Reviewing Domain Information**

This domain resolves to IP 34.155.192.52 (ASN 396982). A review of VirusTotal relationship information from this domain shows as of this writing, 81 domains [[2](https://www.virustotal.com/gui/ip-address/34.155.192.52/relations)] have been created since the 23 Dec 2024 under this IP address targeting Canada Post, Scotiabank, rebate information, etransfer, Costco rewards, etc.

![](https://isc.sans.edu/diaryimages/images/Phishing_Scotiabank.png)

**Indicators**

34.155.192.52
bmo-securltyverlfy1[.]com

It is important to review carefully the data before entering any information. Stay safe.

[1] https://www.bmo.com/en-ca/main/personal/security-centre/scam-alerts/
[2] https://www.virustotal.com/gui/ip-address/34.155.192.52/relations
[3] https://www.virustotal.com/graph/34.155.192.52
[4] https://www.hybrid-analysis.com/sample/c76cbf6e22734f177e024e1fee02ed17a53413e0dfee02c6a6601be28280b167
[5] https://www.scamadviser.com/check-website/bmo-securltyverlfy1.com?utm\_source=hybridanalysis
[6] https://www.sans.org/security-awareness-training/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Secure the Human](/tag.html?tag=Secure the Human) [Phishing](/tag.html?tag=Phishing) [Exploit](/tag.html?tag=Exploit) [Credentials](/tag.html?tag=Credentials) [Banking](/tag.html?tag=Banking)

[0 comment(s)](/diary/Phishing%2Bfor%2BBanking%2BInformation/31548/#comments)

* [previous](/diary/31546)
* [next](/diary/31550)

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