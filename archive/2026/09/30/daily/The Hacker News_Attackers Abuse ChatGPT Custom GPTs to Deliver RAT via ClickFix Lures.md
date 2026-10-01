---
title: Attackers Abuse ChatGPT Custom GPTs to Deliver RAT via ClickFix Lures
url: https://thehackernews.com/2026/09/attackers-abuse-chatgpt-custom-gpts-to.html
source: The Hacker News
date: 2026-09-30
fetch_date: 2026-10-01T07:59:25.434452
---

# Attackers Abuse ChatGPT Custom GPTs to Deliver RAT via ClickFix Lures

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

# [Attackers Abuse ChatGPT Custom GPTs to Deliver RAT via ClickFix Lures](https://thehackernews.com/2026/09/attackers-abuse-chatgpt-custom-gpts-to.html)

**Ravie Lakshmanan**Sep 30, 2026Malware / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-E2KBc2Kl1xfsJ_ayeCwrbYODEJELskOif8C_YQFyt7DoGklZczzFD3IetvE9mFBUeQN9SQWCE41WtJA-NkE6dya1xAOznACZzeRCMRhvfSQaGipfmD-z1F2rWFPFGLvYSJwrfKhUrbdzwMc_b4OkpTA8huBozpABL2OBcxCM1cod7Hvr0eH23GgE1sEo/s1700-nu-rw-lo-l85-e365/custom-gpt.jpg)

Threat actors are abusing ChatGPT Custom GPTs to disguise them as legitimate product offerings and direct unsuspecting victims to malicious sites that employ [ClickFix lures](https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html) to deliver malware.

Huntress, which [observed](https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat) the activity in late September 2026, said it marks the abuse of yet another feature in trusted artificial intelligence (AI) platforms. [Prior campaigns](https://thehackernews.com/2025/12/threatsday-bulletin-spyware-alerts.html#ai-chat-guides-spread-stealers) have weaponized [shared conversations](https://thehackernews.com/2026/07/threatsday-ai-powered-hacking-370.html#fake-claude-guide-spreads-malware) with AI chatbots and [malicious Claude Artifacts](https://thehackernews.com/2026/07/threatsday-android-spyware-plc-attacks.html#fake-claude-app-drops-rat) to distribute stealer malware and remote access trojans (RATs).

[Custom GPTs](https://openai.com/index/introducing-gpts/) refer to a personalized version of ChatGPT that, as the name implies, allows users to define custom instructions, upload reference files, and enable specific skills to handle unique tasks without any coding. They are hosted on the legitimate ChatGPT website with the Custom GPT name at the top.

"In the incidents we saw, victims interacted with an attacker-created Custom GPT, which was programmed to respond to their prompts with a message that included a Google Sites link," Huntress said. "This link then brought them to a ClickFix-style attack, which led to the download and execution of a malicious MSI installer."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The installer then initiates a DLL sideloading chain responsible for loading shellcode, which is used to launch a persistence script and a RAT payload. No less than 40 users have been infected as part of the campaign.

The starting point of the attack is a sponsored result for searches like "chatgpt" on Google. The two Custom GPT links are listed below -

* chatgpt[.]com/g/g-6ab595ad6554819181b686d4876efb80-plus-5-6
* chatgpt[.]com/g/g-6ab6ba039440819185ed491740b11cf8-plus-5-6

Users who end up interacting with the Custom GPT named "Plus 5.6" are served a "Service Availability Notice" that instructs them to either upgrade their subscription tier or navigate to a backup Google Sites domain due to "limited availability on the primary domain."

To nudge unsuspecting users into opting for the latter option, the notice also displays the message: "We recommend using the backup domain if you need immediate access."

Should the victim follow through, the Google Sites domain presents a fake Cloudflare CAPTCHA check that triggers a ClickFix attack, deceiving them into copying and executing a malicious PowerShell command. The PowerShell command is used to deploy an MSI installer ("ISOSimple.msi"), which abuses a legitimate Canon-signed binary ("COTFileReadApp.exe") to sideload a rogue DLL ("ceiinfolog.dll").

The DLL, per Huntress, is the real Canon DLL that's been altered to load a second, unsigned DLL ("rdCore.dll"), which subsequently extracts an encrypted loader from a .WAV audio file ("Common.Integrator.Preview.wav"). While this is not the first time threat actors have smuggled their payload within audio and video file formats, WAV-hidden payloads have been previously observed in connection with [Octowave Loader](https://malpedia.caad.fkie.fraunhofer.de/details/win.octowave) campaigns.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmcZQ3UP6tbwaQEnOkV_DfqrAU5pllAMGLdz1fxsj_r5JxqOAYq6mZTb2Icp12fg1QEzlEK-NNkx1w4-GrT33UUVA698ZPZ5jJQAEZJXSeqXG5NTd5CJPT5yJugnaId4-qXLe1ATB1W-FqJEMjC2GZk52ipJwzrTaHny5pn8UY_-56Ng33BZhh0Sd7bkho/s1700-nu-rw-lo-l85-e365/gpt-chain.jpg)

In the final stage, the loader shellcode proceeds to unpack the trojan and a persistence script from an encrypted file system ("monitor.raw"), but not before bypassing AMSI, [unhooking "ntdll.dll"](https://binarydefense.com/resources/blog/slivering-through-the-cracks) to sidestep user-mode monitoring by security programs, and running anti-virtual machine checks by checking CPU vendor strings against various VMware, VirtualBox, Hyper-V, QEMU, Xen, and Parallels drivers and services.

The trojan supports a wide range of features -

* Documents installed antivirus, Microsoft Defender status, and system profile
* Runs remote desktop sessions and screen "broadcasts."
* Captures the endpoint's camera input, the microphone, and system audio.
* Recognizes 17 web browsers and can launch the default one.
* Searches file contents across the system using a built-in file manager component.
* Drops and runs secondary payloads (i.e., .EXE, .DLL, and .MSI) and scripts (i.e., PowerShell, batch, VBScript, and JavaScript)

"To find its C2 server, which the strings call the 'Gate,' the RAT uses DNS-over-HTTPS through Cloudflare, Google, and Quad9 servers," Huntress said. "Its lookups travel inside ordinary HTTPS traffic to well-known resolvers, so they never appear in local DNS logs."

It's suspected the server details are hidden deep inside the code in an encrypted form or retrieved at runtime. The RAT malware has been consistently found to drop a legitimately signed binary ("GOMCam2024.exe") that launches Google Chrome with ...