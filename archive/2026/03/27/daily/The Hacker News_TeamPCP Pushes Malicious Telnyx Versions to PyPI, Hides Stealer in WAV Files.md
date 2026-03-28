---
title: TeamPCP Pushes Malicious Telnyx Versions to PyPI, Hides Stealer in WAV Files
url: https://thehackernews.com/2026/03/teampcp-pushes-malicious-telnyx.html
source: The Hacker News
date: 2026-03-27
fetch_date: 2026-03-28T04:20:15.057724
---

# TeamPCP Pushes Malicious Telnyx Versions to PyPI, Hides Stealer in WAV Files

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [TeamPCP Pushes Malicious Telnyx Versions to PyPI, Hides Stealer in WAV Files](https://thehackernews.com/2026/03/teampcp-pushes-malicious-telnyx.html)

**Ravie Lakshmanan**Mar 27, 2026Cybersecurity / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1CMUCCEUOX5JczcW-qUC2Bw8_3GmKNoLItyUq-AeuCUvFrJJL0t6aW5EhyJzNT5OyQJulbqwy847fK_EEBieTmTHEKn33suBcHss0AflwRWkPdmqT7FUbX5Rahkwz09g0Fw2GDZr00dAqHeEouzWvFVKMLgNshyO2HQ6QcD5qtbNu59djr1cdm0iV_ksj/s1700-e365/wave.jpg)

TeamPCP, the threat actor behind the supply chain attack targeting [Trivy](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html), [KICS](https://thehackernews.com/2026/03/teampcp-hacks-checkmarx-github-actions.html), and [litellm](https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html), has now compromised the [telnyx](https://pypi.org/project/telnyx/) Python package by pushing two malicious versions to steal sensitive data.

The two versions, 4.87.1 and 4.87.2, published to the Python Package Index (PyPI) repository on March 27, 2026, concealed their credential harvesting capabilities within a .WAV file. Users are recommended to downgrade to version 4.87.0 immediately. The PyPI project is currently quarantined.

Various reports from [Aikido](https://www.aikido.dev/blog/telnyx-pypi-compromised-teampcp-canisterworm), [Endor Labs](https://www.endorlabs.com/learn/teampcp-strikes-again-telnyx-compromised-three-days-after-litellm), [Ossprey Security](https://ossprey.com/blog/telnyx-pypi-malware-wav/), [SafeDep](https://safedep.io/malicious-telnyx-pypi-compromise/), [Socket](https://socket.dev/blog/telnyx-python-sdk-compromised), and [StepSecurity](https://www.stepsecurity.io/blog/teampcp-plants-wav-steganography-credential-stealer-in-telnyx-pypi-package) indicate the malicious code is [injected](https://github.com/team-telnyx/telnyx-python/issues/235) into "telnyx/\_client.py," causing it to be invoked when the package is imported into a Python application. The malware is designed to target Windows, Linux, and macOS systems.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

"Our analysis reveals a three-stage runtime attack chain on Linux/macOS consisting of delivery via audio steganography, in-memory execution of a data harvester, and encrypted exfiltration," Socket said. "The entire chain is designed to operate within a self-destructing temporary directory and leave near-zero forensic artifacts on the host."

On Windows, the malware downloads a file named "hangup.wav" from a command-and-control (C2) server and extracts from the audio data an executable that's then dropped into the Startup folder as "msbuild.exe." This allows it to persist across system reboots and automatically run every time a user logs in to the system.

In case the compromised host runs on Linux or macOS, it fetches a different .WAV file ("ringtone.wav") from the same server to extract a third-stage collector script and run. The credential harvester is designed to capture a wide range of sensitive data and exfiltrate the data in the form of "tpcp.tar.gz" via an HTTP POST request to "83.142.209[.]203:8080."

"The standout technique in this sample - and the reason for the post title - is the use of audio steganography to deliver the final payload," Ossprey Security said. "Rather than hosting a raw executable or a base64 blob on the C2 (both of which are trivially flagged by network inspection and EDR), the attacker wraps the payload inside a .WAV file."

It's currently not known how the package's PYPI\_TOKEN was obtained by TeamPCP, but it's likely that it was through a prior credential harvesting operation.

"We believe the most likely vector is the litellm compromise itself," Endor Labs researchers Kiran Raj and Rachana Misal said. "TeamPCP's harvester swept environment variables, .env files, and shell histories from every system that imported litellm. If any developer or CI pipeline had both litellm installed and access to the telnyx PyPI token, that token was already in TeamPCP's hands."

What's notable about the attack is the absence of a persistence mechanism in Linux and macOS and the use of a temporary directory to conduct the malicious actions and recursively delete all its contents once everything is complete.

"The strategic split is clear. Windows gets persistence: a binary in the Startup folder that survives reboots, providing the threat actor with long-term, repeatable access," Socket explained. "Linux/macOS gets smash-and-grab: a single, high-speed data harvesting operation that collects everything of value and exfiltrates it immediately, then vanishes."

The development comes a few days after the threat actor [distributed](https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign) trojanized versions of the popular litellm Python package to exfiltrate cloud credentials, CI/CD secrets, and keys to a domain under its control.

The supply chain incident also reflects a new-found maturation, where the threat actor has consistently infected legitimate, trusted packages with massive user bases to distribute malware to downstream users and widen blast radius, rather than directly publishing malicious typosquats to open-source package repositories.

"The target selection across this campaign focuses on tools with elevated access to automated pipelines: a container scanner (Trivy), an infrastructure scanning tool (KICS), and an AI model routing library (litellm)," Snyk [said](https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/). "Each of these tools requires broad read access to the systems it operates on (credentials, configs, environment variables) by design."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ciso-risk-comm-cert-dr-d)

To mitigate the threat, developers are advised to perform the following actions -

* Audit Python environme...