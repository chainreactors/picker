---
title: What's the deal with these router vulnerabilities&#x3f;, (Thu, Dec 1st)
url: https://isc.sans.edu/diary/rss/29288
source: SANS Internet Storm Center, InfoCON: green
date: 2022-12-02
fetch_date: 2025-10-04T00:19:36.392941
---

# What's the deal with these router vulnerabilities&#x3f;, (Thu, Dec 1st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29282)
* [next](/diary/29294)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

# [What's the deal with these router vulnerabilities?](/forums/diary/Whats%2Bthe%2Bdeal%2Bwith%2Bthese%2Brouter%2Bvulnerabilities/29288/)

**Published**: 2022-12-01. **Last Updated**: 2022-12-01 00:20:28 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Whats%2Bthe%2Bdeal%2Bwith%2Bthese%2Brouter%2Bvulnerabilities/29288/#comments)

Earlier today, I was browser recently made public vulnerabilities for tomorrow's version of our [@Risk newsletter](https://www.sans.org/newsletters/at-risk/). What stuck out was a set of about twenty vulnerabilities in Netgear and DLink routers:

[CVE-2022-44186](/vuln.html?cve=2022-44186) -  Netgear R7000P V1.3.1.64 is vulnerable to Buffer Overflow in /usr/sbin/httpd via parameter wan\_dns1\_pri.
[CVE-2022-44187](/vuln.html?cve=2022-44187) -  Netgear R7000P V1.3.0.8 is vulnerable to Buffer Overflow via wan\_dns1\_pri.
[CVE-2022-44188](/vuln.html?cve=2022-44188) -  Netgear R7000P V1.3.0.8 is vulnerable to Buffer Overflow in /usr/sbin/httpd via parameter enable\_band\_steering.
[CVE-2022-44190](/vuln.html?cve=2022-44190) -  Netgear R7000P V1.3.1.64 is vulnerable to Buffer Overflow via parameter enable\_band\_steering.
[CVE-2022-44191](/vuln.html?cve=2022-44191) -  Netgear R7000P V1.3.1.64 is vulnerable to Buffer Overflow via parameters KEY1 and KEY2.
[CVE-2022-44193](/vuln.html?cve=2022-44193) -  Netgear R7000P V1.3.1.64 is vulnerable to Buffer Overflow in /usr/sbin/httpd via parameters: starthour, startminute , endhour, and endminute.
[CVE-2022-44194](/vuln.html?cve=2022-44194) -  Netgear R7000P V1.3.0.8 is vulnerable to Buffer Overflow via parameters apmode\_dns1\_pri and apmode\_dns1\_sec.
[CVE-2022-44196](/vuln.html?cve=2022-44196) -  Netgear R7000P V1.3.0.8 is vulnerable to Buffer Overflow via parameter openvpn\_push1.
[CVE-2022-44197](/vuln.html?cve=2022-44197) -  Netgear R7000P V1.3.0.8 is vulnerable to Buffer Overflow via parameter openvpn\_server\_ip.
[CVE-2022-44198](/vuln.html?cve=2022-44198) -  Netgear R7000P V1.3.1.64 is vulnerable to Buffer Overflow via parameter openvpn\_push1.
[CVE-2022-44199](/vuln.html?cve=2022-44199) -  Netgear R7000P V1.3.1.64 is vulnerable to Buffer Overflow via parameter openvpn\_server\_ip.
[CVE-2022-44200](/vuln.html?cve=2022-44200) -  Netgear R7000P V1.3.0.8, V1.3.1.64 is vulnerable to Buffer Overflow via parameters: stamode\_dns1\_pri and stamode\_dns1\_sec.
[CVE-2022-44184](/vuln.html?cve=2022-44184) -  Netgear R7000P V1.3.0.8 is vulnerable to Buffer Overflow in /usr/sbin/httpd via parameter wan\_dns1\_sec.
[CVE-2022-44201](/vuln.html?cve=2022-44201) -  D-Link DIR823G 1.02B05 is vulnerable to Commad Injection.
[CVE-2022-44202](/vuln.html?cve=2022-44202) -  D-Link DIR878 1.02B04 and 1.02B05 are vulnerable to Buffer Overflow.
[CVE-2022-44801](/vuln.html?cve=2022-44801) -  D-Link DIR-878 1.02B05 is vulnerable to Incorrect Access Control.
[CVE-2022-44804](/vuln.html?cve=2022-44804) -  D-Link DIR-882 1.10B02 and1.20B06 is vulnerable to Buffer Overflow via the websRedirect function.
[CVE-2022-44806](/vuln.html?cve=2022-44806) -  D-Link DIR-882 1.10B02 and 1.20B06 is vulnerable to Buffer Overflow.
[CVE-2022-44807](/vuln.html?cve=2022-44807) -  D-Link DIR-882 1.10B02 and 1.20B06 is vulnerable to Buffer Overflow via webGetVarString.

Interestingly, both the [Netgear](https://www.netgear.com/about/security/) and the D-Link security pages are silent about it. The [D-Link](https://www.dlink.com/en/security-bulletin/).

The Netgear page lists another vulnerability for today. D-Link's page appears to have yet to be updated. The last D-Link vulnerability seems to have been patched about two years ago.

All vulnerability point to the same GitHub repo for exploit code, but the link in the NVD database isn't working. The repository, however, exists with various IoT vulnerabilities and exploits. It is hard to match up the vulnerabilities with specific exploits.

So what does this all mean:

1. Vendors aren't going to save you.
2. Your router is probably vulnerable.
3. If you still have the admin interface exposed (and that is what appears to be targeted here): Consider yourself lucky. Someone else will probably upgrade the router for you to prevent others from taking hold of it.
4. Use a non-default password and a non-default network address scheme internally to make attacks via the browser (SSRF, CSRF...) more difficult.
5. Use a "proper" open-source router. (OPNSense, PFSense...) . At least you will not have paid a vendor for software they stopped supporting during beta testing, and I find them MUCH easier to keep up to date.

Sorry for the rant.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[1 comment(s)](/diary/Whats%2Bthe%2Bdeal%2Bwith%2Bthese%2Brouter%2Bvulnerabilities/29288/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/cloudsecnext-summit-2025/course/application-security-securing-web-apps-api-microservices) | Denver | Oct 4th - Oct 9th 2025 |

* [previous](/diary/29282)
* [next](/diary/29294)

### Comments

Could it be that the navigation / listing you are following is not being maintained? I do find their lack of CVE references to be frustrating, they stopped some time in 2021?

I searched Support for the R7000P and found Firmware Version 1.3.3.154 (release notes https://kb.netgear.com/000065225/R7000P-Firmware-Version-1-3-3-154) publised 12-October-2022. I also found other, currently unmitigeted security bulletins, by searching for R7000P on https://www.netgear.com/about/security/.

Example: https://kb.netgear.com/000065243/Security-Advisory-for-Multiple-Vulnerabilities-on-the-R7000P-PSV-2022-0144-PSV-2022-0145.

#### dotBATman

#### Dec 1st 2022 2 years ago

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
* [Handlers](/handler_list.html)...