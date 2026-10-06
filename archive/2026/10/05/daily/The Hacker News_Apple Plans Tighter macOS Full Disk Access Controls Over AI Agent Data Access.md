---
title: Apple Plans Tighter macOS Full Disk Access Controls Over AI Agent Data Access
url: https://thehackernews.com/2026/10/apple-plans-tighter-macos-full-disk.html
source: The Hacker News
date: 2026-10-05
fetch_date: 2026-10-06T08:25:26.616865
---

# Apple Plans Tighter macOS Full Disk Access Controls Over AI Agent Data Access

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Apple Plans Tighter macOS Full Disk Access Controls Over AI Agent Data Access](https://thehackernews.com/2026/10/apple-plans-tighter-macos-full-disk.html)

**Ravie Lakshmanan**Oct 05, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDBg5lUcW7uXfKt2vo4Pq5MQUxOty2Xq3pApCIyhUAuSpTzu1jR_CGkNNS2UkAKxYvqk4KCyP1Ehr0PYcW6xVolcSuSdfRPx4rSDDnkuAKaCkgBii_l7kH-s9u7oEhyK2FpvAnaTRWDV48t9XBXEv-MpUIWhBaZYIBx3CFY_zSUXxdw-3C5rB_30Y0VEtf/s1700-nu-rw-lo-l85-e365/macos-ai.jpg)

Apple has announced that it's taking steps to tighten controls around a macOS setting called Full Disk Access (FDA) due to security risks posed by artificial intelligence (AI) agents.

"Some developers are using Full Disk Access in ways that could put users at risk, exposing everything on their systems—including files, mail, messages, and even browsing history – without users' full knowledge and understanding," Apple [said](https://developer.apple.com/news/?id=p6zjojqw) in a post. "For communication apps, this can also compromise the privacy of the people users are communicating with."

[Full Disk Access](https://support.apple.com/guide/mac-help/mchlccb25729/mac), accessed via Privacy & Security in the Settings app, was introduced by Apple in macOS Mojave (version 10.14), offers users greater control over which applications can access their entire system and data from apps like Mail, Messages, Safari, and Time Machine backups.

Once the setting is enabled for an application, it allows that program to bypass certain security restrictions and read and write to system files that apps are typically restricted from accessing or modifying. This option is essential for apps, such as security tools and backup software, that require deep system access to function properly.

Stating that Full Disk Access largely bypasses controls designed to safeguard users' private data, Apple said it plans to introduce updates to the setting to ensure that this sort of access is granted only with an explicit user action. It's currently not known when the new controls will be rolled out.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

"As AI agents become increasingly capable and autonomous, the risks associated with this level of access will grow substantially," Apple added. "We are committed to ensuring users clearly understand these risks before granting such access, so they can make informed decisions about their own data and privacy."

Although Apple did not take any specific name, the development appears to be a response to a recent report about how Meta's [Muse](https://ai.meta.com/muse/) agentic tool accessed a journalist's private iMessages after [they](https://www.inc.com/jason-aten/metas-new-muse-ai-agent-read-my-private-messages-i-never-asked-it-to/91408202) [granted](https://www.inc.com/jason-aten/meta-keeps-apologizing-for-muse-its-explanations-miss-the-point-entirely/91409363) it Full Disk Access. Muse is [advertised](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse) as a "personal AI agent" built along the lines of OpenClaw that runs on a dedicated Linux virtual machine on Meta's cloud.

Meta has since clarified that, for Muse to be able to access a user's private messages, it must have two permissions: have Full Disk Access and have a Messages connector setting in Muse enabled.

"The Messages integration in the Muse Mac app is opt in," Meta CTO David Singleton [said](https://www.threads.com/%40davidsingleton/post/DddI7WtG8ul). "Your Muse can only read Messages content if macOS system-level Full Disk Access is granted and the Messages connector is enabled."

Apple's announcement also comes weeks after security researcher Patrick Wardle [demonstrated](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html) a proof-of-concept (PoC) exploit for a zero-day in Muse's Mac app called not-a-mused that allows any app or terminal command to obtain access to the token that authenticates users to their Muse account.

The now-patched vulnerability "can let an unprivileged local process redirect Muse's dictation traffic and abuse the trust/access granted to the app," Wardle said. "The concern is that Muse may have significantly broader access than ordinary local malware, making it a particularly useful target for privilege/access amplification."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Specifically, a local attacker can exploit an undocumented setting named "endo\_voyager\_dictation\_endpoint" without requiring any special privileges, allowing them to capture dictated audio and prompts, inject malicious prompts, and abuse the access Muse has been granted for other malicious actions.

Wardle has also been [acknowledged](https://learn.chatgpt.com/docs/changelog#codex-2026-09-25-app) for reporting [another vulnerability](https://www.wired.com/story/a-flaw-in-chatgpts-mac-app-could-have-let-hackers-grab-sensitive-data/), tracked as [CVE-2026-100754](https://www.cve.org/CVERecord?id=CVE-2026-100754), impacting OpenAI's ChatGPT app for Mac that could have been abused to take over the AI assistant and grant an attacker unauthorized access to chat logs and other data stored by the app.

These findings demonstrate how the [privileged position](https://www.meta.com/en-gb/help/artificial-intelligence/1047255454427887/) enjoyed by agentic tools, [the extensive data they collect](https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/), and their ability to interact with various parts of the operating system, like writing files to disk, accessing the mic and camera, creating calendar events, sending emails, and monitoring location, can expand the attack surface and open the door for an adversary to abuse this access and steal sensitive data.

Found this article intere...