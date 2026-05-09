---
title: TCLBANKER Banking Trojan Targets Financial Platforms via WhatsApp and Outlook Worms
url: https://thehackernews.com/2026/05/tclbanker-banking-trojan-targets.html
source: The Hacker News
date: 2026-05-08
fetch_date: 2026-05-09T05:09:02.082328
---

# TCLBANKER Banking Trojan Targets Financial Platforms via WhatsApp and Outlook Worms

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [TCLBANKER Banking Trojan Targets Financial Platforms via WhatsApp and Outlook Worms](https://thehackernews.com/2026/05/tclbanker-banking-trojan-targets.html)

**Ravie Lakshmanan**May 08, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWchpptUYeW4vXSUXfGq-uMzB1mr_dzsvX8XIWssIKzaWa4_eYbaLwec5Zos3xCoD0s8-LDcGI7Vj8DjFq6RtUY68HP21YudHYdsFS2xdyzQE7OPyuTlqyO2X9uwlSCRuVl9tAUwq0mvGuXlYkxjdmC7ynyAcIDpbejkR45ucf_L3VCDupSZMteOby7BUp/s1700-e365/banking.jpg)

Threat hunters have flagged a previously undocumented Brazilian banking trojan dubbed **TCLBANKER** that's capable of targeting 59 banking, fintech, and cryptocurrency platforms.

The activity is being tracked by Elastic Security Labs under the moniker **REF3076**. The malware family is assessed to be a major update of the [Maverick](https://thehackernews.com/2025/12/brazil-hit-by-banking-trojan-spread-via.html), which is known to leverage a worm called SORVEPOTEL to spread via WhatsApp Web to a victim's contacts. The Maverick campaign is attributed to a threat cluster that Trend Micro calls Water Saci.

At the core of the attack chain is a loader with robust anti-analysis capabilities that deploys two embedded modules: a full-featured banking trojan and a worm component that uses WhatsApp and Microsoft Outlook for propagation.

"The observed infection chain bundles a malicious MSI installer inside a ZIP file," security researchers Jia Yu Chan, Daniel Stepanic, Seth Goodwin, and Terrance DeJesus [said](https://www.elastic.co/security-labs/tclbanker-brazilian-banking-trojan). "These MSI installer packages are abusing a signed Logitech program called Logi AI Prompt Builder."

The malware leverages DLL side-loading against the application to launch a malicious DLL ("screen\_retriever\_plugin.dll"), which functions as a loader with a "comprehensive watchdog subsystem" that continuously keeps an eye out for analysis tools, sandboxes, debuggers, disassemblers, instrumentation tools, and antivirus software to sidestep detection.

Specifically, the malicious DLL will only execute if it was loaded by either "logiaipromptbuilder.exe" (the Logitech program) or "tclloader.exe" (likely a reference to an executable used during testing). It also removes any usermode hooks placed by endpoint security software within "ntdll.dll" by replacing the library and disables Event Tracing for Windows (ETW) telemetry.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

What's more, the malware generates three fingerprints based on anti-debugging and anti-virtualization checks, system disk information checks, and language checks, using them to create an environment hash value that's used to decrypt the embedded payload. The system language check ensures that the user's default language is Brazilian Portuguese.

"For example, if a debugger is present, it will produce an incorrect hash, so when the malware attempts to derive the decryption keys from the hash, the payload will not decrypt correctly, and TCLBANKER will stop executing," Elastic explained.

The main component launched following these checks is the banking trojan that once again verifies if it's running on a Brazilian system, and then proceeds to establish persistence using a scheduled task.Subsequently, it beacons out to an external server with an HTTP POST request containing basic system information.

TCLBANKER also incorporates a self-update mechanism and a URL monitor that extracts the current URL from the foreground browser's address bar using [UI Automation](https://thehackernews.com/2025/07/new-coyote-malware-variant-exploits.html). This step targets popular browsers like Google Chrome, Mozilla Firefox, Microsoft Edge, Brave, Opera, and Vivaldi.

The extracted URL is matched against a hard-coded list of targeted financial institutions. If there is a match, it establishes a WebSocket connection to a remote server and enters into a command dispatch loop, enabling the operator to perform a broad range of tasks -

* Run shell commands
* Capture screenshots
* Start/stop screen streaming
* Manipulate clipboard
* Launch a keylogger
* Remotely control mouse/keyboard
* Manage files and processes
* Enumerate running processes
* List visible windows
* Serve fake credential-stealing overlays

To conduct data theft, TCLBANKER relies on a Windows Presentation Foundation (WPF)-based full-screen overlay framework to conduct social engineering using credential harvesting prompts, vishing wait screens, bogus progress bars, and fake Windows Updates, all while hiding overlays from screen capture tools.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

In tandem, the loader invokes the worming module to propagate the trojan via spam and phishing messages at scale. It employs a two-pronged approach that involves a WhatsApp Web worm that hijacks authenticated browser sessions and an Outlook email bot that abuses Microsoft Outlook to send fake emails to the victim's contacts.

Like in the case of [SORVEPOTEL](https://thehackernews.com/2025/11/python-based-whatsapp-worm-spreads.html), the WhatsApp worm retrieves a messaging template from the server and leverages the open-source project WPPConnect to automate the sending of messages to other users, while filtering out groups, broadcasts, and non-Brazilian numbers.

The Outlook agent, on the other hand, is an email spambot that abuses the victim's installed Microsoft Outlook application to send phishing emails from the victim's email address, thereby bypassing spam filters and giving the messages an illusion of trust.

"TCLBANKER reflects a broader maturation happening across the Brazilian banking trojan ecosystem," Elastic concluded. "Techniques that were once the hallmark of more sophisticated threat actors: environment-gated payload decryption, direct syscall generation, real-time social engineering orchestration over WebSocket, are now...