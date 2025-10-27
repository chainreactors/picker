---
title: Python Obfuscation for Dummies, (Tue, Oct 18th)
url: https://isc.sans.edu/diary/rss/29160
source: SANS Internet Storm Center, InfoCON: green
date: 2022-10-19
fetch_date: 2025-10-03T20:19:20.850938
---

# Python Obfuscation for Dummies, (Tue, Oct 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29156)
* [next](/diary/29164)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Python Obfuscation for Dummies](/forums/diary/Python%2BObfuscation%2Bfor%2BDummies/29160/)

**Published**: 2022-10-18. **Last Updated**: 2022-10-18 05:11:17 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[2 comment(s)](/diary/Python%2BObfuscation%2Bfor%2BDummies/29160/#comments)

Recently, I found several malicious Python scripts that looked the same. They all contained the same strings at the end:

```

eval(compile(base64.b64decode(eval('<hex_encoded_string>')),'<string>','exec'))
```

Pretty nifty obfuscation technique because you cannot get any idea of the script's purpose without executing it in a sandbox or checking deeper. Obfuscation is a crucial element for attackers because they help to bypass classic security controls and they slow down the analysis process by Security Analysts. How does it work? Attackers write their code then they use tools to obfuscate the code. Of course, they are tools available in the underground, but there are also tools publicly available.

One of them is called development-tools.net[[1](https://development-tools.net/python-obfuscator/)], which provides a free online Python obfuscation tool:

![](https://isc.sans.edu/diaryimages/images/isc-20221018-1.png)

Here is a simple/fantastic script:

```

#!/usr/bin/python
print "Hello world!"
```

The obfuscated code is:

```

import base64, codecs
magic = 'IyEvdXNyL2Jpb'
love = 'v9jrKEbo24XpU'
god = 'JpbnQgIkhlbGx'
destiny = 'iVUqipzkxVFVX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + \
eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
```

But is the obfuscation efficient to make the Python script bypass some AV's? I selected a classic script (a password stealer). The script has a current score of 4/60 on VT (SHA256:5f9a62e6c09f085ffb60caefbe155e3ead38848d0f5201517ca0c3cccc09ce78)[[2](https://www.virustotal.com/gui/file/5f9a62e6c09f085ffb60caefbe155e3ead38848d0f5201517ca0c3cccc09ce78/detection)]. The obfuscated script received a score of 5/60.

Another one (a keylogger) with a score of 10/59 (SHA256:77d1cda4ab39e3e0f0a7af4c3d86a42721b9a0d62ccf2f3112988e518c296af5)[[3](https://www.virustotal.com/gui/file/77d1cda4ab39e3e0f0a7af4c3d86a42721b9a0d62ccf2f3112988e518c296af5/detection)]. The obfuscated version also received a score of 5/60.

As you can see, if the code is really difficult to understand out-of-the-box by an Analyst (goal completed) without proper tools. However, this obfuscation tool does not always improve the detection rate of antivirus tools.

[1] <https://development-tools.net/python-obfuscator/>
[2] <https://www.virustotal.com/gui/file/5f9a62e6c09f085ffb60caefbe155e3ead38848d0f5201517ca0c3cccc09ce78/detection>
[3] <https://www.virustotal.com/gui/file/77d1cda4ab39e3e0f0a7af4c3d86a42721b9a0d62ccf2f3112988e518c296af5/detection>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Malware](/tag.html?tag=Malware) [Obfuscation](/tag.html?tag=Obfuscation) [Python](/tag.html?tag=Python) [Tool](/tag.html?tag=Tool)

[2 comment(s)](/diary/Python%2BObfuscation%2Bfor%2BDummies/29160/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29156)
* [next](/diary/29164)

### Comments

Interestingly, knowing nothing of Python that did not take long to boil down to just needing to do a base64 decode
of the value IyEvdXNyL2Jpbi9weXRob24KcHJpbnQgIkhlbGxvIHdvcmxkISIK and no Python interpreter needed.

I am surprised it was not doing anything other than rot13 and base64, not even Unicode or EBCDIC.

#### Dingbat

#### Oct 18th 2022 2 years ago

I know a decent bit about Python, but I do agree with you and I made an account because this is the perfect opportunity to share a tool I use quite a bit. Keep in mind this is not specifically for you necessarily, but just anybody that comes across this post. If you use cyberchef.io and just copy-paste in each section of the obfuscated python code using the "magic" setting you can fully understand the obfuscated code without even understanding Python.

I am in no way affiliated with cyberchef I just think it's a great tool hope this helps some other people. Cheers.

https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false,'')

#### Dingbat

#### Oct 20th 2022 2 years ago

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