---
title: Old Backdoor, New Obfuscation, (Sat, Mar 18th)
url: https://isc.sans.edu/diary/rss/29646
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-19
fetch_date: 2025-10-04T10:03:15.552560
---

# Old Backdoor, New Obfuscation, (Sat, Mar 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29642)
* [next](/diary/29650)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Old Backdoor, New Obfuscation](/forums/diary/Old%2BBackdoor%2BNew%2BObfuscation/29646/)

**Published**: 2023-03-18. **Last Updated**: 2023-03-18 08:33:15 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Old%2BBackdoor%2BNew%2BObfuscation/29646/#comments)

When you’re hunting, sometimes you feel lucky because you spotted something that looks brand new, but sometimes it’s not new or… the code has been changed to bypass existing detections. Here is a perfect example. A few months ago, Juniper discovered[[1](https://blogs.juniper.net/en-us/threat-research/a-custom-python-backdoor-for-vmware-esxi-servers)] a backdoor targeting VMWare ESXi servers, more precisely, the OpenSLP service ([CVE-2019-5544](/vuln.html?cve=2019-5544) and [CVE-2020-3992](/vuln.html?cve=2020-3992)).

If the backdoor isn’t new, I found new versions of it that implement more obfuscation techniques by reducing changes to be caught by antivirus tools and filters. The scripts, found on VT, have the following filename format: “esxi\_ransomware\_xxxxxxxx.py”. It seems that the attacker tested different obfuscation techniques. Sometimes, just having a look at the source code with a graphical overview is interesting:

![](https://isc.sans.edu/diaryimages/images/isc-20230318-1.png)

Many text editors propose this kind of view. In the picture above, you can see patterns with only interesting lines at the end.

The backdoor has been obfuscated with many functions that look complicated, but most of them do… nothing! Example:

```

self.send_response(200)
self.send_header('Content-type', 'text/html')
self.end_headers()
if opaque_fct_6_guXM09JTqW(1170448432, 34836967901, 30592200701, 23499594842, 7931033327):
    if opaque_fct_7_2givpU14Oj(12913767465, 29715926998, 28391806664, 34224856236, 27002350942, 38119355106, 17984667519, 33397958160, 34307567544, 3134198737, 6433478414, 1333569498, 30190306077, 31065906546):
        opaque_fct_3_HlBjJpTAMd(4559404501, 19631615206, 15232647523, 38155060881, 25231599065, 27560986774, 28564255047, 23742277226, 37444581463, 34726589553)
    elif opaque_fct_3_Jvb1H08Kzj(1744861910, 8785099158, 15933986777):opaque_fct_6_78lRkhN51d(13973672458, 29300903469, 6016412088, 32808894927, 2647492267, 10754001214, 28891585111, 32994113503, 19424804608)
    else:
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})
    else:
        opaque_fct_7_ueGht7ZaDw(34708030056, 3642393576, 19762095891, 22250089401, 11960747056)
```

The first if() condition will always be TRUE:

```

def opaque_fct_6_guXM09JTqW(opaque_fct_6_guXM09JTqW_0, opaque_fct_6_guXM09JTqW_1, opaque_fct_6_guXM09JTqW_2, opaque_fct_6_guXM09JTqW_3, opaque_fct_6_guXM09JTqW_4):
    if (opaque_fct_6_guXM09JTqW_1 > opaque_fct_6_guXM09JTqW_0):
        return True
    if (opaque_fct_6_guXM09JTqW_4 <= opaque_fct_6_guXM09JTqW_1):
        return True
    if (opaque_fct_6_guXM09JTqW_1 > opaque_fct_6_guXM09JTqW_0):
        return True
    if (opaque_fct_6_guXM09JTqW_1 < opaque_fct_6_guXM09JTqW_0):
        return False
    if (opaque_fct_6_guXM09JTqW_3 >= opaque_fct_6_guXM09JTqW_1):
        return False
    if (opaque_fct_6_guXM09JTqW_1 < opaque_fct_6_guXM09JTqW_4):
        return False
    if (opaque_fct_6_guXM09JTqW_0 >= opaque_fct_6_guXM09JTqW_1):
        return False
    if (opaque_fct_6_guXM09JTqW_1 < opaque_fct_6_guXM09JTqW_4):
        return False
    if (opaque_fct_6_guXM09JTqW_1 < opaque_fct_6_guXM09JTqW_0):
        return False
    if (opaque_fct_6_guXM09JTqW_1 > opaque_fct_6_guXM09JTqW_0):
        return True
    if (opaque_fct_6_guXM09JTqW_0 <= opaque_fct_6_guXM09JTqW_1):
        return True
    if (opaque_fct_6_guXM09JTqW_0 >= opaque_fct_6_guXM09JTqW_1):
        return False
```

Indeed, if you check the parameters, '34836967901' will always be bigger than '1170448432'. Other calls are useless (like the first call to opaque\_fct\_3\_HlBjJpTAMd()).

If you remove all the junk code, the backdoor has precisely the same behavior as the Juniper blog post explained.

[1] <https://blogs.juniper.net/en-us/threat-research/a-custom-python-backdoor-for-vmware-esxi-servers>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [VMware](/tag.html?tag=VMware) [Obfuscation](/tag.html?tag=Obfuscation) [Backdoor](/tag.html?tag=Backdoor) [Python](/tag.html?tag=Python)

[0 comment(s)](/diary/Old%2BBackdoor%2BNew%2BObfuscation/29646/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29642)
* [next](/diary/29650)

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