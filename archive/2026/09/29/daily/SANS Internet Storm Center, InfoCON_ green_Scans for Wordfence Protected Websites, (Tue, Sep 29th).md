---
title: Scans for Wordfence Protected Websites, (Tue, Sep 29th)
url: https://isc.sans.edu/diary/rss/33382
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-29
fetch_date: 2026-09-30T07:42:58.243392
---

# Scans for Wordfence Protected Websites, (Tue, Sep 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33376)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Scans for Wordfence Protected Websites](/forums/diary/Scans%2Bfor%2BWordfence%2BProtected%2BWebsites/33382/)

**Published**: 2026-09-29. **Last Updated**: 2026-09-29 13:29:33 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Scans%2Bfor%2BWordfence%2BProtected%2BWebsites/33382/#comments)

Starting yesterday, our sensors picked up a small number of scans for "wordfence-waf.php". This particular script is used by Wordfence, a solution to protect WordPress sites. During the Wordfence install, the wordpress-waf.php file will be created in the site's root directory [1].

The requests themselves are unremarkable, not including any headers like User-Agent. Just the bare minimum "Host" header, which is the IP address of the targeted site.

The file does not include any secrets or configuration parameters, but it includes other scripts intended to run before any WordPress code to assist with Wordfence's integration. My best guess is that attackers may attempt to enumerate Wordfence-protected sites to limit detection. Wordfence collects intelligence from the sites it protects and often publishes information about newly detected attacks. This, in turn, "burns" exploit techniques, as other sites will not be able to protect themselves as well.

Another possible option is that these scans attempt to bypass Wordfence. By using the IP address instead of the hostname, the attacker may attempt to identify Wordfence-protected sites that are directly reachable. This could be used to bypass Wordfence protection and expose sites that rely on it to delays in patching. Web application firewalls and "virtual patching" are only temporary fixes; please follow Wordfence's guidance on preventing the bypassing of its protection. But wordfence-waf.php is part of the "Extended Protection" feature, which is designed to help prevent this type of bypass.

[1] https://www.wordfence.com/help/firewall/optimizing-the-firewall/

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [wordfence](/tag.html?tag=wordfence) [wordpress](/tag.html?tag=wordpress) [waf](/tag.html?tag=waf)

[0 comment(s)](/diary/Scans%2Bfor%2BWordfence%2BProtected%2BWebsites/33382/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33376)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)