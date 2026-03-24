---
title: Setting Up a Tor Relay at National Taiwan Normal University: A Practical Experience of Communicating with the University and Leaving Open Possibilities
url: https://blog.torproject.org/setting-up-tor-university-relay-taiwan/
source: Tor Project blog
date: 2026-03-23
fetch_date: 2026-03-24T04:18:14.435085
---

# Setting Up a Tor Relay at National Taiwan Normal University: A Practical Experience of Communicating with the University and Leaving Open Possibilities

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Setting Up a Tor Relay at National Taiwan Normal University: A Practical Experience of Communicating with the University and Leaving Open Possibilities

by [toomore](/author/toomore)
| March 23, 2026

![](/setting-up-tor-university-relay-taiwan/lead.png)

*This is a guest post from our friends at [anoni.net](https://anoni.net/). This article was made possible with support from [Open Culture Foundation](https://ocf.tw/en/).*

## Preface: Why Talk About Anonymous Networks on Campus?

In many places, the internet is monitored closely and managed centrally. In that environment, anonymous communication is not just a technical choice. It supports safe exploration, research, and expression. In Taiwan, this matters because we sit in a sensitive part of East Asia. Internet freedom and communication resilience are practical skills for handling real pressure.

Universities and academic networks have historically been the earliest places where new technologies and public infrastructure are experimented with. The following interview documents how a computer science student at National Taiwan Normal University, also a member of the anonymous network community, stepped into institutional reality on campus, communicated with the university, and attempted to actually set up a Tor Relay.

Within the anonymous network community, people often talk about technology and ideals. The hard part is not the configuration itself. The question is whether the relay can survive in the real world.

This time, we interviewed a partner from the anonymous network community, NZ, who is currently studying in the Department of Computer Science at [National Taiwan Normal University](https://www.ntnu.edu.tw/). He set up a Tor Relay on campus by working openly with the university system and completing the full administrative process.

![NZ Su En-Li](/setting-up-tor-university-relay-taiwan/nz.jpg)

**èæ©ç« (Su En-Li, NZ)** is currently a third-year undergraduate student in the Department of Computer Science and Information Engineering at National Taiwan Normal University. With a strong interest in information security and network governance, he is currently responsible for operating and maintaining the [first Tor node on Taiwan Academic Network (TANet)](https://metrics.torproject.org/rs.html#search/as:AS1659). In addition to hands-on technical practice, he is also dedicated to knowledge sharing, serving as an anonymous network course instructor in the GDGoC NTNU student club. He has long been involved in Taiwan's open source and information security communities, and has volunteered multiple times at major technical conferences such as SITCON, HITCON, and COSCUP, demonstrating both community service experience and strong technical passion.

## Why Set Up a Tor Relay at a University?

His motivation was simple. If anonymous networks in Taiwan only show up in niche communities, overseas VPSs, or are treated as gray-area tools, they will not be taken seriously. Universitiesâespecially academic networks like TANetâare meant to support research, experimentation, and public interest. That is why this kind of foundational infrastructure can fit there.

He was also fully aware of the real-world constraints. Taiwan's academic network is highly centralized, with outbound connectivity controlled by the Ministry of Education. In practice, this setup limits what anonymous networks can do.

Because of those limits, he wanted to find out: **"Under such constraints, can it at least exist?"**

## How Did He Talk to the University? The Goal Was to Help Them Explain It Clearly

![Project Proposal Document](/setting-up-tor-university-relay-taiwan/nz-ntnu-4.png)

*Administrative Process Timeline*

When he moved from ideas to action, he did not frame Tor as something "cool" or radical. He explained it in terms the university could work with:

* This is a Tor **Relay**, not an Exit Node
* It does not directly provide content to external users
* It is an experiment in network infrastructure and anonymous communication

Process-wise, he exchanged emails with network administrators, professors, and the department chair. He made sure everyone who needed to sign offâor be "CC'd"âunderstood what this machine would do. The university's requirement was practical: if the Ministry of Education asked about it, they needed to be able to explain it. That became the entry point for communication.

## The Administrative Process Is a Hassle, but It Can Still Work

![Administrative Process](/setting-up-tor-university-relay-taiwan/nz-ntnu-3.png)

*Project Proposal Document*

At National Taiwan Normal University, all outbound connections are blocked by default. Any service requires applying for an exception, including specifying IP addresses, intended use, and supporting documentation, and ultimately ensuring it aligns with the university's reporting procedures to the Ministry of Education. He described this process as annoying and predictable.

As long as one is willing to write the paperwork and explain things clearly, this path does exist.

## Student Organizations and Outreach: Let Tor Mean More Than a Label

![Student Organizations and Outreach](/setting-up-tor-university-relay-taiwan/nz-ntnu-2.png)

*Student Organization Event: Anonymous Network Workshop*

Beyond the machine itself, he also organized anonymous networkârelated activities through student clubs on campus, introducing Tor, anonymous communication, and the design principles behind them. Even if attendance wasn't always high, it helped create a place where people could understand that **"anonymous networks â  criminal tools,"** without leaning on stereotypes.

These efforts may not be highly visible. They still matter.

## Practical Advice and Pitfalls for Others

The following points are distilled from this experience, intended as a reference for anyone who wants to promote or deploy a Tor Relay on a university campus in the future.

### Actionable Advice

* Take the public route from the start: don't wait until something goes wrong to explainâlet network administrators and supervising professors know what you are doing early on.
* Clearly distinguish between a Tor Relay and an Exit Node: this is almost always the deciding factor in whether communication succeeds, so be explicit about the difference in risk.
* Explain things in a way the university can "account for": you are not asking faculty to support anonymous networks ideologically. You are making sure they can answer questions when asked.
* Expect a lot of paperwork: IP addresses, outbound connectivity, and usage descriptions are all basic requirements.

### Common Pitfalls

* Assuming technical correctness is enough: within academic networks, institutional processes often determine success or failure before technology does.
* Underestimating the Ministry of Education's level of control: most universities block outbound connections by default, and any exceptions must align with formal reporting procedures.
* Failing to plan for maintenance and account ownership: account privileges after graduation directly affect whether long-term operation is possible.

## Conclusion

This attempt to deploy a Tor Relay at National Taiwan Normal University is not an endpoint, and it is not a definitive answer. Still, it proves one thing clearly:

* Within Taiwanese universities, as long as one is willing to communicate and explain,
* Anonymous networks are not entirely without a place.

If we hope to see Tor Relays on more campuses in the future, these "uncool but time-consuming" efforts may well be the most important foundation of all.

### Further Reflection: Why Are Attempts Like This Worth Preserving?

After reading this inter...