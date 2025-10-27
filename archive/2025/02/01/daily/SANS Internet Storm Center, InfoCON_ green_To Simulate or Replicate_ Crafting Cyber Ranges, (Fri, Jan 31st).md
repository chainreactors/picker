---
title: To Simulate or Replicate: Crafting Cyber Ranges, (Fri, Jan 31st)
url: https://isc.sans.edu/diary/rss/31642
source: SANS Internet Storm Center, InfoCON: green
date: 2025-02-01
fetch_date: 2025-10-06T20:38:16.556231
---

# To Simulate or Replicate: Crafting Cyber Ranges, (Fri, Jan 31st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31638)
* [next](/diary/31646)

# [To Simulate or Replicate: Crafting Cyber Ranges](/forums/diary/To%2BSimulate%2Bor%2BReplicate%2BCrafting%2BCyber%2BRanges/31642/)

**Published**: 2025-01-31. **Last Updated**: 2025-01-31 04:28:38 UTC
**by** [Richard Porter](/handler_list.html#richard-porter) (Version: 1)

[0 comment(s)](/diary/To%2BSimulate%2Bor%2BReplicate%2BCrafting%2BCyber%2BRanges/31642/#comments)

**The Good Stuff First**This tool is being shared (calling it a tool is generous) due to the number of times last year I had to create fake internet domains. It adds domains and zones to Windows DNS. This was to help with the many student cyber ranges that got ‘sploited [1] in the name of learning.

![](https://isc.sans.edu/diaryimages/images/fakenet_example.gif)

It is posted to GitHub. [4]

# **Introduction - To Simulate or Replicate**

In my experience with cybersecurity training, there's always this tug-of-war between using tools to simulate threats in a safe sandbox or going for the real deal by replicating actual attacks. To paraphrase; “To Simulate or not to Simulate, that is the question!” When we talk about simulation, I mean using tech like threat simulators where you can control everything down to the last byte. It's great for training because you can teach without the risk.

These tools do an amazing job and this is not a dig on any of them. Sometimes, you just have to take the type 2 approach [2].

When you replicate, you're building a digital mirror of real attacks. This is where you get the view into the "what if" moments. It is also where you can get your hands dirty with live behavior of malware and command and control. Sure, it's riskier, but the payoff in learning can be extremely useful. In my case, we settled on real ‘enough.’

## **The Problem**

Let's first acknowledge that no wheel was re-invented here. We went back to some basics. Routing, DNS and controlling what was executed and it worked [5].

* ***Safely** building an infrastructure so students and users could enjoy non-simulated attacks. Replicate -> Delete -> Repeat. We had to control routing, control leakage, control execution and make this safe at scale.*
* *Have the environment and logs look as **real** as possible [6].*
* *Use **known** use-cases from current documented APT reports [7].*

## The Solution

***First, Managed the Basics:*** Make sure you have 100% control over DNS, routing, and what was executed on the network. This provided the power to steer how the cyber range behaved, much like a conductor leading an orchestra. It started with hosts files, and evolved into controlling DNS servers, hence the above tool being shared.

***Next, Control the Environment:*** Pick out known bad IP addresses from the internet's underbelly, those associated with Indicators of Compromise (IOCs). By squatting on these IPs and locking down their routes with static entries and firewall rules at the network's edge, a controlled cyber-range is created. The example CSV in the applet used RFC 5737 and RFC 2606 for IP and domain examples. Make sure to adapt that, as example.test just does not look convincing in logs [8]. FYI, our very own DShield is a good place to start looking if you need a range to use: https://www.dshield.org/block.txt

***Then, Craft the Tools:*** I decided to build our attack tools from the bad guys lens and design our own game space. We tested many of the frameworks and went with Mythic and modeling APT28 and tweaking it to fit our unique setup. This way, we controlled exactly how the "bad guys" played [9]. We selected Mythic for many reasons, however do check out their Jupyter Notebooks!

**Building the Network:** We set up the network topology using tools like Ansible and Terraform for repeatability. Think of it as setting the stage - you could expect to see code for this in future diaries [10].

## Finally, Tested and Validated

I tested for route leakage. This is what prompted more than one layer of Firewalls. We had three firewalls in place, two in the primary gamespace with a final gatekeeper. There are dynamic lists that populate the border as a third layer of control importing our cyber-squating space. To summarize, control resultion, control routing, then filter at the border of the lab. [11]. Let me know if you want a deeper dive on this?

## Conclusion, Keep it Simple

Over the past year, I've been involved in constructing cyber ranges specifically for replication purposes. When you are asked to do this more than nTimes, where n = the number of times that cause you to lose it and code over the weekend, you automate. Sometimes old methods apply. If this is of interest to the community, let me know in the comments below and I will clean up and release more of the micro-tools assembled to make this all work?

Not a single AI was harmed in the creation of this diary!

**[@packetmonk](https://x.com/packetmonk) on X.**

**References:**

**[1] MITRE ATT&CK Framework - [MITRE ATT&CK](https://attack.mitre.org/)**

**[2] Honeynet Project - [Honeynet Project](https://www.honeynet.org/about/)**

**[3] Honey Pots - [Honey Pots and Honey Nets](https://www.sans.org/white-papers/41/)**

**[4] GitHub - Richard’s PowerShell Scripts (for the DNS configuration script mentioned) - [GitHub](https://github.com/packetalien)**

**[5] DNS is the new BGP - [APNIC](https://blog.apnic.net/2023/09/22/dns-is-the-new-bgp/)**

**[6] Generating Hyptoheses for Successful Threat Hunting - [SANS Whitepaper](https://www.sans.org/white-papers/37172/)**

**[7] MITRE APT List - [Attack Groups](https://attack.mitre.org/groups/)**

Richard Porter
--- ISC Handler on Duty

Keywords: [Cybersecurity](/tag.html?tag=Cybersecurity)

[0 comment(s)](/diary/To%2BSimulate%2Bor%2BReplicate%2BCrafting%2BCyber%2BRanges/31642/#comments)

* [previous](/diary/31638)
* [next](/diary/31646)

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