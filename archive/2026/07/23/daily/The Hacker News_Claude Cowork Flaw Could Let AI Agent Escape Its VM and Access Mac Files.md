---
title: Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files
url: https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html
source: The Hacker News
date: 2026-07-23
fetch_date: 2026-07-24T05:05:41.396608
---

# Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Claude Cowork Flaw Could Let AI Agent Escape Its VM and Access Mac Files](https://thehackernews.com/2026/07/claude-cowork-flaw-could-let-ai-agent.html)

**Ravie Lakshmanan**Jul 23, 2026Vulnerability / Application Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj5Vr8pje9uM-Ce6rzE-_hhU3HvR2NkKtYfaSrIXz3m0BbrC1ZNC9p4GW4GRQaAvFKPjE5kopXmdmcKcMb7_1dbOWvMO6_oe87HCj4TUXV1dWK99cz_OBcNHd81Ziat93g4wJcBdc3K1vq0IkwFL9DO9GlSrf_KxGi2hpg7VVsU9iTt7B2XByXL7nil86i/s1700-e365/claude.gif)

Cybersecurity researchers have uncovered a sandbox escape vulnerability in Anthropic's [Claude Cowork](https://claude.com/product/cowork) that makes it possible to break out of the confines of a Linux virtual machine (VM) within which the agent runs to read or write files anywhere on the Mac.

Accomplish AI, which shared details of the vulnerability with The Hacker News ahead of publication, said about 500,000 macOS users running local Cowork sessions were affected prior to it being patched. It has been codenamed **SharedRoot**.

"We connected a folder to a fresh Claude Cowork session, sent one short message, and watched the agent escape the sandbox," Oren Yomtov, principal security researcher at Accomplish AI, [said](https://www.accomplish.ai/blog/sharedroot-escaping-claude-cowork-sandbox/). "From inside the VM, it reached the host Mac and read and wrote files all over it, far outside the folder we'd connected, with no permission prompt anywhere."

With this level of access, the agent can access any data stored on the Mac via the user's account, including SSH keys, cloud credentials, and other valuable information.

Following responsible disclosure, Anthropic closed the report as informative without issuing a fix. That said, the latest version of Cowork defaults to cloud execution, which addresses the issue. But users who opt to run the agent locally are still exposed to the problem.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Claude Cowork's macOS desktop app runs as the user who is logged into the system. The actual agent-related work, on the other hand, happens in a Linux VM created via Apple's [Virtualization framework](https://developer.apple.com/documentation/virtualization). Every session gets its own disposable unprivileged user, along with a Secure Computing Mode (seccomp) filter for application sandboxing. The folders connected by the user are shared into the VM by a root daemon called coworkd.

"One detail matters more than the rest: the host filesystem gets shared into that VM read-write," Yomtov explained. "The entire host '/,' mounted so that only guest-root inside the VM can see it, at /mnt/.virtiofs-root."

Because the entire host file system is mounted into the agent's VM with read-write privileges, any path to guest-root can grant the agent access to the underlying host, effectively escaping the sandbox.

This involves loading the Linux kernel's "act\_pedit" Traffic Control (tc) packet editing subsystem into an unprivileged user namespace and exploiting [CVE-2026-46331](https://thehackernews.com/2026/06/new-linux-pedit-cow-exploit-enables.html) in the guest kernel, a recently disclosed flaw called pedit COW, to obtain guest-root. From there, the agent can access the whole host ("/") with elevated privileges, allowing it to read or write files from and to the Mac's file system as the logged-in desktop user.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7w4UG99yP4m-ve8gVwEPvso3_thT0vixtu6gyIUo7k1hwNr3skO_YWt594i8U3fGdq0rwe3qpTpKSrbG6K82h6BqdIDjS1brw1cXUVSnHjbSTwdlC0ZrI6nxM21V4vYMaNGPCwH9fil6tRl3xtau35z3c8PkK5BhKel44kFPjUHS0CGlj5cBfmGEg01CI/s1700-e365/vm.jpg)

Or Hiltch, co-founder and CTO of Accomplish AI, told The Hacker News that creating user and network namespaces gives the session [CAP\_NET\_ADMIN](https://man7.org/linux/man-pages/man7/capabilities.7.html) within its private network namespace, allowing it to perform various network-related operations.

"That capability provides access to the vulnerable tc/act\_pedit kernel path used by pedit COW," Hiltch added. "The namespaces are not the exploit; they make its normally privileged prerequisite available to an ordinary user."

The development assumes significance in the face of [revelations](https://thehackernews.com/2026/07/openai-says-its-own-ai-models-escaped.html) that OpenAI's models managed to break out of its sandboxed environment during a security test that resulted in the breach of Hugging Face's production infrastructure in their quest to cheat the ExploitGym benchmark they were being graded on.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNPwzguLBCTkAnNkIEvSYaWamKLqYLrJPjnea1V_lz7UcfQkavBo2g3OEGoLyz7mD/s728-e100/sygnia-d-4.png)](https://thn.news/sygnia-webinar)

"act\_pedit is one bug in a category," Yomtov said. "The Linux net/sched subsystem throws off this exact shape of privilege escalation on a regular cadence: an autoloadable module, a config path an unprivileged user can reach, a memory bug at the end of it. Patch this one and you've fixed this one. The chain re-arms on the next one, with everything above the kernel untouched."

"And the next one is always coming. At any given moment there's likely a privilege-escalation bug it's still exposed to, sometimes fixed upstream but not yet in your image, sometimes not yet fixed anywhere, with a working exploit out within hours. This isn't a patch-faster problem. You're structurally one bug behind, all the time."

To mitigate the threat, it's essential to [disable unprivileged user namespaces](https://ubuntu.com/blog/ubuntu-23-10-restricted-unprivileged-user-namespaces), avoid making the seccomp filter overly permissive, stop autoloading of modules, and restrict sharing of the whole host into...