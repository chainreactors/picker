---
title: PEEP Turns Chrome and Edge Into Post-Compromise Backdoors for Host Command Execution
url: https://thehackernews.com/2026/09/peep-turns-chrome-and-edge-into-post.html
source: The Hacker News
date: 2026-09-07
fetch_date: 2026-09-08T06:42:26.387062
---

# PEEP Turns Chrome and Edge Into Post-Compromise Backdoors for Host Command Execution

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [PEEP Turns Chrome and Edge Into Post-Compromise Backdoors for Host Command Execution](https://thehackernews.com/2026/09/peep-turns-chrome-and-edge-into-post.html)

**Ravie Lakshmanan**Sep 07, 2026Malware / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhA3-5bNylOMc_s8MAT2ibQnV33cnJXadwKPRXjYgAL0GcZWOXuwtM-s5HS4ryVu5ewnhfAqBtOiuSseLcUSyDIfxf5XKF6mAwrpyG-v3Y-siqjJY8I5zVEMXwfkKPwBNAqaO2sQFI-q2oA4MWiagZFUlknIPKADDfvOo8s2Ifsa_xBAojg1rD5ZGUErC85/s1700-nu-rw-lo-l85-e365/chrome-malware.jpg)

Cybersecurity researchers have disclosed details of a complex Chromium-based post-exploitation toolkit called **PEEP** that masquerades as a bookmarks extension for the web browser.

"Requiring prior administrative or code execution access, its installer injects the extension directly into Chrome/Edge profiles, bypassing Web Store checks and user prompts by forging Chromium's own Secure Preferences integrity values," SOCRadar [said](https://socradar.io/blog/peep-browser-rat-chrome-extension/). "A native-messaging tool then extends it beyond browser telemetry to host-level command execution and file management."

Once installed, the PEEP "extension" agent polls its command-and-control (C2) server ("206.237.30[.]232" or "[xfjcc[.]fun](https://www.virustotal.com/gui/domain/xfjcc.fun/details)") every 30 seconds over plaintext HTTP for new commands, while exfiltrating browsing history, active-tab metadata, and session cookies. It also functions as a remote access and browser monitoring toolkit that runs host commands, steals credentials, hijacks sessions, and alters web pages.

PEEP is built on the foundations of [RedExt](https://thehackernews.com/2025/11/glassworm-malware-discovered-in-three.html), an open-source, browser data analysis and red teaming framework that has also been put to use in prior GlassWorm attacks. However, it expands on the toolkit with dedicated installation routines, a native host bridge, heartbeat telemetry, an update channel, and a broader command set. This, in turn, makes PEEP a derivative of RedExt.

PEEP is described as a post-compromise framework as it lacks an initial access vector itself, meaning it requires the operator to breach a machine through some other means and deploy the malware. The activity remains unattributed, although the presence of Chinese-language artifacts in the source code points to a Chinese-speaking threat actor.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The extension masquerades as "Smart Bookmarks" (ID: ejkndncpkdcjcikfhiamcdehdoegilbj). It's the main agent responsible for executing the beacon loop by polling "/api/commands," harvesting browser data, receiving additional tasking, and sending the results back.

The browser add-on also invokes an auxiliary executable ("nm\_host.exe") when said task requires operating system access, while browser-based commands (e.g., screenshots, clipboard, or JavaScript injection) are run locally. The use of the [Native Messaging Host binary](https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging) transforms the malware from a basic credential stealer to a remote-access tool.

"Operating in the user context, the extension extracts browser artifacts and uses com.peep.lab/nm\_host.exe to run shell commands, manage files, and discover processes and services," SOCRadar said. "Bypassing Web Store checks, PEEP maintains persistence via sideloading, enterprise force-install policies, preference-integrity manipulation, and a ScriptCache fallback."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhc9nsOJtcS9-FkHAK8Q79dhjarvivTCOa4HDAtp_OnqP2QlFx0KZIHrYH4HW-p8JNwd6MzSHi6IXRKvGbqvSaxsW0RfQ4wA0KvS6mLuPnDpHbnpfOkHIYiFayUpp3lUNZcaauJmpkeecrfzm4qZG4wx_Gjj5hXuMD2mXKnR-CMDvHXcYpd01yO3i8_Shad/s1700-nu-rw-lo-l85-e365/soc.jpg)

Also used by the extension are several other endpoints -

* "/api/register" to register the infection
* "/api/agents/<id>/heartbeat" to send details about the browser's User-Agent string, operating system, and time zone
* "/api/extension\_update/" and "/api/extension\_crx/" to update the extension itself
* "/api/agents/<id>/task\_result" to post the results of the command execution
* "/api/exfil" to post auto-collected data, such as cookies, recent history, open tabs, active URL, public IP address, locale, and time zone
* "/health" to serve internal system status without requiring login credentials
* "/login" to serve a login interface for the C2 panel at port 5001

Another defining aspect of PEEP is its ability to modify the Secure Preferences file to ensure that the extension is auto-enabled upon launching the browser. Given that the extension is not available on the Chrome Web Store and other official extension marketplaces, it also leverages the ExtensionInstallForcelist or ExtensionSettings policies and sideloading tricks for delivery.

the malware makes use of two PowerShell scripts, while a third one acts as a re-registration helper for the extension without touching Secure Preferences -

* install\_silent.ps1, which enables Developer Mode to sideload arbitrary extensions
* patch\_secure\_prefs.ps1, which patches the Secure Preferences file
* force\_enable.ps1, which removes the extension from Preferences’s external\_uninstalls, places the CRX at %LOCALAPPDATA%PEEPcrx, re-registers via the HKCU Extensions key and an External Extensions JSON manifest, and restarts the browser

There also exists a Python script named "patch\_secure\_prefs\_linux.py" with the same function as its PowerShell counterpart, indicating that the threat actor behind the operation is replicating the behavior to also target Linux environments.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

Once initialized, the extension parses a configuration file to extract C2 information and activate automated data harvesting,...