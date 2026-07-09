---
title: My Stack Simulator, (Wed, Jul 8th)
url: https://isc.sans.edu/diary/rss/33138
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-08
fetch_date: 2026-07-09T06:03:27.401661
---

# My Stack Simulator, (Wed, Jul 8th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33130)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [My Stack Simulator](/forums/diary/My%2BStack%2BSimulator/33138/)

**Published**: 2026-07-08. **Last Updated**: 2026-07-08 08:09:03 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/My%2BStack%2BSimulator/33138/#comments)

The stack is a memory region where a program stores temporary data - like local variables and return addresses. Think of the stack as a pile of plates in your kitchen: you can only add a new plate to the top, and you can only take one away from the top too. Programs use this same "last in, first out" principle to keep track of what they're doing. Every time a function is called, the program pushes a new plate onto the stack containing things like local variables and the address to return to once the function finishes. When the function is done, that plate is popped off the top, and execution resumes exactly where it left off. This simple mechanism is what allows programs to call functions within functions within functions, and always find their way back - but it's also precisely why a stack that grows too large, or gets overwritten with unexpected data, becomes a favorite target for attackers looking to hijack a program's execution flow.

In the SANS class FOR610[[1](https://www.sans.org/cyber-security-courses/reverse-engineering-malware-malware-analysis-tools-techniques)] (malware analysis), there is an introduction to assembly and, when students learn how functions work, they have to understand how the stack also works. If you’ve no prior experience, it could be a bit challenging. To help students to vizualise how the stack works, I created a “stack simulator” that allows to “see” what’s happening when code is executed.

![](https://isc.sans.edu/diaryimages/images/isc-20260708-1.png)

How does it work?

1. Select the architecture (32-64 bits) in the assembly editor
2. Select a predefined set of instructions (“lesson”, “call”, “prologue”, …).
3. Click on “Step” to you can see the impact on the stack and registers (like in a debugger).

Note that you can modify the predefined ASM code and add your own instructions.

The stack simulator is available on my website[[2](https://xameco.be/stack-simulator.html)].

If you’re interested in malware analysis, my next classes will be:

* SANS Tokyo Autumn 2026 [[3](https://www.sans.org/cyber-security-training-events/tokyo-autumn-2026)]
* SANS Paris November 2026 [[4](https://www.sans.org/cyber-security-training-events/paris-november-2026)]

[1] <https://www.sans.org/cyber-security-courses/reverse-engineering-malware-malware-analysis-tools-techniques>
[2] <https://xameco.be/stack-simulator.html>
[3] <https://www.sans.org/cyber-security-training-events/tokyo-autumn-2026>
[4] <https://www.sans.org/cyber-security-training-events/paris-november-2026>

**Xavier Mertens (@xme)**
[Xameco](https://xameco.be)
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://raw.githubusercontent.com/xme/pgp/refs/heads/main/public.key)

Keywords: [ASM](/tag.html?tag=ASM) [Assembly](/tag.html?tag=Assembly) [FOR610](/tag.html?tag=FOR610) [Registry](/tag.html?tag=Registry) [Simulator](/tag.html?tag=Simulator) [Stack](/tag.html?tag=Stack) [Tool](/tag.html?tag=Tool)

[0 comment(s)](/diary/My%2BStack%2BSimulator/33138/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33130)

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