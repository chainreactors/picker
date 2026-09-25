---
title: Hacked Ukrainian Sites Serve Fake Cloudflare ClickFix Lures for Psychedelic Stealer
url: https://thehackernews.com/2026/09/hacked-ukrainian-sites-serve-fake.html
source: The Hacker News
date: 2026-09-24
fetch_date: 2026-09-25T06:53:33.900063
---

# Hacked Ukrainian Sites Serve Fake Cloudflare ClickFix Lures for Psychedelic Stealer

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

# [Hacked Ukrainian Sites Serve Fake Cloudflare ClickFix Lures for Psychedelic Stealer](https://thehackernews.com/2026/09/hacked-ukrainian-sites-serve-fake.html)

**Ravie Lakshmanan**Sep 24, 2026Malware / Social Engineering

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1xvw3iNKwWUngfdShXBAPKrbRDMZSCQ3_FdiHNKvwrLkip9fUiikko0FKN-cfgzBIgkLvKDR9xIlnfEZVQgHgOW2qTz8Pd4Ur0-DCYdUssgN_9vglgxRU6u5ZRK_FlQYmgV_sbv8pfA1YnSJcojUOhWC-7lkPbA07An_X-vNHmZ8xT2Okq9HiRfTBVt1h/s1700-nu-rw-lo-l85-e365/UK-CLICK.jpg)

An active [ClickFix campaign](https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html) has been observed compromising legitimate Ukrainian business websites to inject bogus Cloudflare verification pages and trick victims into downloading a previously undocumented information stealer called **Psychedelic**.

"When a visitor interacts with the page, the lure copies a Windows Installer command to the clipboard and instructs the visitor to paste it into the Windows Run dialog," Arctic Wolf Labs [said](https://arcticwolf.com/resources/blog/psychedelic-stealer-fake-clickfix-captcha-targets-ukraine/) in a technical report shared with The Hacker News.

The ClickFix chain uses an "msiexec.exe" command to fetch a Windows MSI installer that's used to deliver the stealer malware. The malicious tool is designed to harvest browser passwords, account tokens, and cryptocurrency-wallet data, set up scheduled-task persistence, and contact a command-and-control (C2) server for additional tasking.

Some of the compromised websites include a hair-treatment clinic, a scale-model manufacturer, a specialist bookseller and publisher, a psychological facility, a tool retailer, and an automotive retailer. These affected sites include an injected iframe element that's responsible for executing attacker-controlled JavaScript ("fsputnik[.]com/tds/tracker[.]js").

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The ClickFix command, for its part, retrieves an MSI installer ("elita.msi") hosted on "uasputnik[.]com," a domain that was registered on September 9, 2026. Other MSI payloads identified [include](https://github.com/rtkwlf/wolf-tools/tree/main/pack_alerts/202609-ukrainian-clickfix-psychedelic-stealer) "miks.msi," "astra.msi," "harbor.msi," "neon.msi," "sova.msi," and "vyse.msi."

"The attacker-controlled page imitates a Cloudflare verification screen and presents Ukrainian-language instructions," Arctic Wolf said. "The clipboard operation occurs before the lure displays its Windows Run instructions. After a three-second spinner, the page presents an instruction dialog and keeps the 'Done' button disabled for approximately 35 additional seconds."

"This delay controls progression through the lure interface; it does not verify that the visitor opened Windows Run, pasted the command, or installed the payload."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcHv34qj1pow6t4qs0Tbxg9t23waZK_EqQ2uVN8x06m9M-lGqPZHHGu79gvW1uGg4wBGKarAYFRrOYnI7fJrp3RInFFCL8JNtaLLbluD1pcLDYcPdgfVzEHpWz9bZ0jPJGGtukWPvVv38_TdAfXbWQFFpYUNV7WKJHyZb1AeEmoOGNC6KDwP0_oRYWq013/s1700-nu-rw-lo-l85-e365/stage-1.jpg)

The MSI installer, for its part, is responsible for retrieving the next-stage payload ("psychedeliclove.exe") from the URL "107.175.82[.]242:9000." The 64-bit Windows executable is Psychedelic Stealer, which performs the following functions -

* Collect credentials from Chromium-based browsers, including Google Chrome, Microsoft Edge, Brave, Opera, Opera GX, Vivaldi, and Yandex, and exfiltrate them through the "/api/v1/ext/passwords" endpoint
* Collect browser-associated account tokens and exfiltrate them through the "/api/v1/ext/tokens" endpoint
* Scan for known cryptocurrency wallet browser extensions (MetaMask, Trust Wallet, OKX Wallet, and SafePal) and desktop apps (Exodus, Atomic Wallet, Electrum, Bitcoin Core, and Litecoin Core) and exfiltrate data through the "/api/v1/ext/wallets" endpoint
* Capture extensive host information and exfiltrate it through the "/api/v1/checkin" endpoint
* Terminate selected browser processes, extract an embedded extension archive into web browser profiles, and set a [native-messaging bridge](https://thehackernews.com/2026/09/peep-turns-chrome-and-edge-into-post.html)

"These components extend the operation beyond one-time data collection," Arctic Wolf said. "Browser-profile modification and native messaging provide a mechanism for deployed browser content to communicate with a local host component."

"A recurring background routine revisits extension-related operations before polling the C2 server for tasks, indicating that browser-component handling is integrated into the implant's ongoing execution cycle rather than limited to initial installation."

Psychedelic Stealer also features the ability to retrieve further tasks using the "/api/v1/agent/tasks?hwid=%s" endpoint, where "hwid" refers to a unique victim identifier. It can allow the malware to run EXE, COM, BAT, CMD, MSI, and PowerShell payloads, offering the operator a way to introduce additional malware.

Arctic Wolf said it identified an exposed lure management panel linked to the campaign called РУБЛЁВКА TDS (Rublevka TDS) on the "uasputnik[.]com" domain. The panel, which is distinct from the implant's C2 ("193.178.159[.]128:8080"), is used to configure web-lure commands and records interactions.

"The dashboard polls visitor records every two seconds, providing near-real-time visibility into progression through the lure interface, not endpoint execution," it added.

At the time of analysis, the panel recorded 557 views, 426 clicks, and 79 complete events across 32 countries, with Ukraine accounting for 446 views, 351 clicks, and 71 complete events. Other targets include the U.S., Poland, Germany, Canada, and the Netherlands.

"Russian-language branding and implementation artifacts suggest lik...