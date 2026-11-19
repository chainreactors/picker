---
title: Java4Shell, NGINX2Shell and more: Why we are not at "Yellow", (Wed, Nov 18th)
url: https://isc.sans.edu/diary/rss/33532
source: SANS Internet Storm Center, InfoCON: green
date: 2026-11-18
fetch_date: 2026-11-19T09:47:31.992792
---

# Java4Shell, NGINX2Shell and more: Why we are not at "Yellow", (Wed, Nov 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33526)
* [next](/diary/33534)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Java4Shell, NGINX2Shell and more: Why we are not at "Yellow"](/forums/diary/Java4Shell%2BNGINX2Shell%2Band%2Bmore%2BWhy%2Bwe%2Bare%2Bnot%2Bat%2BYellow/33532/)

**Published**: 2026-11-18. **Last Updated**: 2026-11-18 19:54:50 UTC
**by** [Johannes Ullrich](https://isc.sans.edu/handler_list.html#johannes-ullrich) (Version: 1)

[0 comment(s)](/diary/Java4Shell%2BNGINX2Shell%2Band%2Bmore%2BWhy%2Bwe%2Bare%2Bnot%2Bat%2BYellow/33532/#comments)

About a month ago, we went to Infocon Yellow for the first time in a few years. We decided to address the php2shell vulnerability and alert our readers to its significant impact. Following php2shell, we had a number of vulnerabilities and events that may also have scored high enough to trigger an Infocon "Yellow" [infocon]. In the last few days, we had a major Microsoft 365 outage, a critical vulnerability in Java, and a critical vulnerability in NGINX, which was disclosed today.

My plan today was to write a bit about attacks we are seeing against one of our Java-specific honeypots. But the results can be summarized in one sentence: We are seeing many attacks, but none that exploit Java4Shell (yet). Will it be an important issue? Probably. Should you patch? Sure. Will the world as we know it end? Maybe.

So why not go to "Yellow"? This is not a new question. Often people ask why we are on "Green" if they are seeing hundreds or thousands of attacks hitting their system each day. The Internet is a dangerous place. Shouldn't we be on "Yellow" (or "Orange") to reflect that danger? My answer has been: "Green" means the Internet is broken as usual. As long as the status is "Green", you should expect a normal "9-to-5" day. I have heard from organizations that have used our infocon to justify staffing and overtime, and I am well aware of the impact it may have.

The reason behind our conservative Infocon is that you can't be alert and "on guard" all the time. An alert status that is "high" all the time is meaningless and counterproductive. You must not treat these recent vulnerabilities as "emergencies". They are the "new normal". Treat them as such. You will not be able to patch nginx2shell across a large organization before the exploit is released. Instead of trying to do the impossible and fail, think beyond the vulnerability of the day. A new reality requires new procedures and techniques. Here are a few ideas:

* Automate patching as much as possible, in particular for less critical systems. Traditionally, automatic patching had two significant drawbacks. First, you may crash a system because of a failed patch. Secondly, the patch may not be applied correctly, and you treat a vulnerable system as "patched".
  Select less critical systems that would be at the end of your patch priority list. I'd rather take a system down myself than have ransomware do it for me. Having a system possibly patched is better than being sure the system isn't patched. And of course, there should be some testing, but that can wait a bit longer. This responds well to the faster development of exploits.
* Reduce your exposure. This should have been a priority years ago. But there are still too many systems connected to the internet that shouldn't be connected. Build a defensible architecture. The same is true for individual applications: reduce the "blast radius" by restricting which data and resources each application can access. And reduce your supply chain exposure. Do you get enough value from tools like Optimizely to justify the risk of them compromising your application?
* Avoid chasing squirrels. Do not change your plan and drop what you are doing just because the world is going to end. The world may end, in which case, patching one more system is probably not going to make a difference. Whether the world ends or not, at least you will be well-rested to deal with it.

During my classes, I am exposed to security professionals from a wide range of backgrounds, working in different industries and countries worldwide. The one thing they all have in common is that they do not have enough time, tools, and sometimes skills to do their job. Making the job you can't do right now any more urgent won't help. Work on tooling and resources, and develop a plan for applying best practices at a sustainable pace. Embrace AI tooling. It is immensely useful for automation. It is even more amazing at helping you get organized. Many partitioners are afraid that AI will do more harm than good, and they are not wrong. But use it where it helps you most. Are you great at writing little scripts but horrible at tracking and inventorying them? Give AI the job you suck at and develop a rapport with your tools. But embracing automation does include embracing AI tooling.

Finally, I got a lot of positive feedback on the final "conclusion" of yesterday's podcast, so I am going to link to it directly here:

[php2shell] https://isc.sans.edu/diary/33440
[infocon] https://isc.sans.edu/infocon.html

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-11-18%20at%202_47_04%E2%80%AFPM.png)

Keywords:

[0 comment(s)](/diary/Java4Shell%2BNGINX2Shell%2Band%2Bmore%2BWhy%2Bwe%2Bare%2Bnot%2Bat%2BYellow/33532/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33526)
* [next](/diary/33534)

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