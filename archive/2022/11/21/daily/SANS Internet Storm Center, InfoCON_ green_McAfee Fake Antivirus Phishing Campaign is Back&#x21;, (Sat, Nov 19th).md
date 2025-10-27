---
title: McAfee Fake Antivirus Phishing Campaign is Back&#x21;, (Sat, Nov 19th)
url: https://isc.sans.edu/diary/rss/29264
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-21
fetch_date: 2025-10-03T23:20:25.900707
---

# McAfee Fake Antivirus Phishing Campaign is Back&#x21;, (Sat, Nov 19th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29260)
* [next](/diary/29266)

# [McAfee Fake Antivirus Phishing Campaign is Back!](/forums/diary/McAfee%2BFake%2BAntivirus%2BPhishing%2BCampaign%2Bis%2BBack/29264/)

**Published**: 2022-11-19. **Last Updated**: 2022-11-20 00:02:43 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[1 comment(s)](/diary/McAfee%2BFake%2BAntivirus%2BPhishing%2BCampaign%2Bis%2BBack/29264/#comments)

Yesterday I received this email that my McAfee antivirus subscription is expired and that my computer is already infected with 5 viruses (how do they know?). The overall content of this email is simple and direct to the point and is similar to something Xavier posted earlier this year [[1](https://isc.sans.edu/diary/McAfee%2BPhishing%2BCampaign%2Bwith%2Ba%2BNice%2BFake%2BScan/28208)].

![](https://isc.sans.edu/diaryimages/images/Email_AV_Expired.PNG)

The email sound scary (infected with malware), however, a few clues from the email header, the sender is not McAfee, whatever they are asking me to do, indicate I'm the target of a phishing email and they likely want money.

![](https://isc.sans.edu/diaryimages/images/Email_AV_Expired_header.png)

The body of the email claims I'm already compromised and to resolve the issue is to first run a online scan against my host. I copied the hidden URL in **CONTINUE** and used wget to get a copy of the site. This is the step-by-step results:

![](https://isc.sans.edu/diaryimages/images/McAfee_results.PNG)

And it found 35 harmful viruses on my computer.

![](https://isc.sans.edu/diaryimages/images/McAfee_results_scan_now.PNG)

Last, the results of the scan and what malware was found on the PC. The initial email claimed the computer was infected with *5* viruses, then *35* and at last after the final scan, there is only *one*.

![](https://isc.sans.edu/diaryimages/images/McAfee_results_scanning_results.PNG)

What I found interesting, it didn't matter how many times I ran the scan, it always returned the same results (live scan and with the wget copy). Virustotal has very low detection and with 2 vendors identifying this as spam [[2](https://www.virustotal.com/gui/url-analysis/u-d83f4cf7d6320d92e653e825e582cfbfc207949bada3e3913128eb6b56377ad3-1668896404)]. I got curious and lookup Tapsnake and it turned out it " is a scareware scam involving coercion to buy protection from a non-existent computer virus that has been distributed in various ways." [[3](https://en.wikipedia.org/wiki/Tapsnake)] In the end, I never got a copy of McAfee antivirus.

One last thing, I checked the domain Whois information to see when this domain was registered or updated, this can often offer some clues if it is used for malicious purposes. Interesting enough, this domain was updated today. [[4](https://whois.domaintools.com/collectyoursordersnow.com)][[5](https://otx.alienvault.com/indicator/domain/collectyoursordersnow.com)] Here is summary of the current listing:

Domain Name: collectyoursordersnow.com
Registry Domain ID: 2699308613\_DOMAIN\_COM-VRSN
Registrar WHOIS Server: whois.namesilo.com
Registrar URL: https://www.namesilo.com/
Updated Date: 2022-11-19T07:00:00Z
Creation Date: 2022-05-26T07:00:00Z
Registrar Registration Expiration Date: 2023-05-26T07:00:00Z
Registrar: NameSilo, LLC

**Indicators**

https://tuk-vi.collectyoursordersnow[.]com/ga/click/2-76430879-6226-10575-20591-16810-fe164f969b-e290af9b7f

[1] https://isc.sans.edu/diary/McAfee+Phishing+Campaign+with+a+Nice+Fake+Scan/28208
[2] https://www.virustotal.com/gui/url-analysis/u-d83f4cf7d6320d92e653e825e582cfbfc207949bada3e3913128eb6b56377ad3-1668896404
[3] https://en.wikipedia.org/wiki/Tapsnake
[4] https://whois.domaintools.com/collectyoursordersnow.com
[5] https://otx.alienvault.com/indicator/domain/collectyoursordersnow.com

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Malware](/tag.html?tag=Malware) [McAfee](/tag.html?tag=McAfee) [Phishing](/tag.html?tag=Phishing) [Scam](/tag.html?tag=Scam) [Spam](/tag.html?tag=Spam)

[1 comment(s)](/diary/McAfee%2BFake%2BAntivirus%2BPhishing%2BCampaign%2Bis%2BBack/29264/#comments)

* [previous](/diary/29260)
* [next](/diary/29266)

### Comments

Problem with Mcafee is they don't do themselves any favours - they frequently have pop-ups unrelated to Security incidents - more to do with Sales or prompt for license renewal 2-3 months before expiry.. If they changed their behaviour it would make it harder to spoof their identity... Thank you for the excellent blogs btw

#### Han Solo

#### Nov 29th 2022 2 years ago

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