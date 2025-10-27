---
title: Mass Internet Scanning from ASN 43350 &#x5b;Guest Diary&#x5d;, (Thu, Aug 7th)
url: https://isc.sans.edu/diary/rss/32180
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-08
fetch_date: 2025-10-07T00:49:06.043669
---

# Mass Internet Scanning from ASN 43350 &#x5b;Guest Diary&#x5d;, (Thu, Aug 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32178)
* [next](/diary/32186)

# [Mass Internet Scanning from ASN 43350 [Guest Diary]](/forums/diary/Mass%2BInternet%2BScanning%2Bfrom%2BASN%2B43350%2BGuest%2BDiary/32180/)

**Published**: 2025-08-07. **Last Updated**: 2025-08-07 00:25:42 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[2 comment(s)](/diary/Mass%2BInternet%2BScanning%2Bfrom%2BASN%2B43350%2BGuest%2BDiary/32180/#comments)

[This is a Guest Diary by Duncan Woosley, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

During the last three months I've had a DShield sensor online and collecting data from a deployment in AWS. This week I did some statistical analysis of the last three months of data and found surprising result. Of all the locations that scanned and attacked the DShield sensor, one location was a clear winner in terms of volume of traffic, accounting for over 65% of the total traffic sent to the sensor. To my surprise, that location was Panama!

**Total DShield Sensor Traffic per Location**
![](https://isc.sans.edu/diaryimages/images/Duncan_Woosley_pic1.png)

The top 10 locations were close to inline with common expectations, however, the traffic from Panama was greater than the total traffic from all the remaining locations combined!

![](https://isc.sans.edu/diaryimages/images/Duncan_Woosley_pic2.png)

Digging into the source of this anomaly, I filtered for traffic by day and found that there were massive spikes on just a few days in the last three months that accounted for most of the DShield sensor's captured volume.

**Largest Single Days by volume from April 7th to July 7th**
![](https://isc.sans.edu/diaryimages/images/Duncan_Woosley_pic3.png)

Each spike was found to be caused by traffic from a single IP each day, but the IP responsible for each spike was different. However, six of the top ten most active IPs were all from a single /24 subnet! The subnet 141.98.80.0/24 was the cause of 59.4% of total logs collected by the sensor. Moreover, nine of the top 10 IPs were from the same internet service provider (ISP) named "NForce Entertainment B.V."

![](https://isc.sans.edu/diaryimages/images/Duncan_Woosley_pic4.png)

**Autonomous System Numbers ([ASN](https://www.arin.net/resources/guide/asn/)) 43350 accounted for 71.6% of the total sensor logs!** This ASN belonging to NForce Entertainment but NForce Entertainment appears to often lease out its IP space to other VPN and proxy providers like the Panama based Flyservers S.A. Flyservers is categorized as a "potentially very high fraud risk ISP" by [Scamalytics](https://scamalytics.com) and is likely the source of this activity.

**Top ASNs by Total Traffic**
![](https://isc.sans.edu/diaryimages/images/Duncan_Woosley_pic5.png)

![](https://isc.sans.edu/diaryimages/images/Duncan_Woosley_pic6.png)

Further research into this ISP found that the NForce Entertainment IP activity was often associated with phishing, malware, and scanning. As a Dutch ISP, they operate without strict regulatory oversight or pressure from their host nation to revoke threat actors’ use of their services.

**Recommendations**

Unfortunately, the solution for network defenders isn't as simple as blocking all traffic from NForce Entertainment. If your organization is in a position where no NForce Entertainment traffic is required for business, this may be an option, but the majority of organizations don’t allow sweeping IP blocking. Instead, I would recommend blocking only sensitive services and HTTP(S) endpoints that allow for logins. The following actions are recommended.

•    Flagging traffic from NForce Entertainment and particularly from ASN 43350.
•    Block access to Remote Desktop Protocol from the internet.
•    Monitor for SSH activity from ASN 43350 and configured SSH to use key based authentication.
•    Implement a Web Application Firewall ([WAF](https://owasp.org/www-community/Web_Application_Firewall)) for all web applications and monitor activity originating from any sources for suspicious queries.
•    Create a WAF alert threshold for high traffic originating from a single source.

[1] https://www.arin.net/resources/guide/asn/
[2] https://scamalytics.com
[3] https://owasp.org/www-community/Web\_Application\_Firewall
[4] https://www.sans.edu/cyber-security-programs/bachelors-degree/

NOTE: ChatGTP was used for Spelling and grammar checks only
-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [ASN43350](/tag.html?tag=ASN43350) [BACS](/tag.html?tag=BACS) [NForce Entertainment](/tag.html?tag=NForce Entertainment) [Scanning](/tag.html?tag=Scanning) [SecOps](/tag.html?tag=SecOps) [Threat Hunting](/tag.html?tag=Threat Hunting)

[2 comment(s)](/diary/Mass%2BInternet%2BScanning%2Bfrom%2BASN%2B43350%2BGuest%2BDiary/32180/#comments)

* [previous](/diary/32178)
* [next](/diary/32186)

### Comments

Thank you for posting this Guy! I had a great experience working as an intern at the Internet Storm Center.

#### Duncan Woosley

#### Aug 7th 2025 1 month ago

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