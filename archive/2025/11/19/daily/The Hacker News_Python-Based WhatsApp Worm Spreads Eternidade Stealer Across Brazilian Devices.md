---
title: Python-Based WhatsApp Worm Spreads Eternidade Stealer Across Brazilian Devices
url: https://thehackernews.com/2025/11/python-based-whatsapp-worm-spreads.html
source: The Hacker News
date: 2025-11-19
fetch_date: 2025-11-20T03:10:23.367885
---

# Python-Based WhatsApp Worm Spreads Eternidade Stealer Across Brazilian Devices

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Python-Based WhatsApp Worm Spreads Eternidade Stealer Across Brazilian Devices](https://thehackernews.com/2025/11/python-based-whatsapp-worm-spreads.html)

**Nov 19, 2025**Ravie LakshmananMalware / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_JS-2uc_a3c5S1eLk0Eo3HK8zCxsAijuKRwY0EFD5q19SEUDr1lwIICc_nphafxi12DafNvvqyGyGth6QWnBNKMZOSgy46Wrhpy-2KtVdj7CJbnlPcM-kHVQa6Y3zOBznsYMA2HWbel-KMoEeDyCzDvOSlQRk6ab056_7sL08HjgSCVMjRQojWCfoG6Ln/s2600/whatsapp-worm.jpg)

Cybersecurity researchers have disclosed details of a new campaign that leverages a combination of social engineering and WhatsApp hijacking to distribute a Delphi-based banking trojan named **Eternidade Stealer** as part of attacks targeting users in Brazil.

"It uses Internet Message Access Protocol (IMAP) to dynamically retrieve command-and-control (C2) addresses, allowing the threat actor to update its C2 server," Trustwave SpiderLabs researchers Nathaniel Morales, John Basmayor, and Nikita Kazymirskyi [said](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/spiderlabs-ids-new-banking-trojan-distributed-through-whatsapp/) in a technical breakdown of the campaign shared with The Hacker News.

"It is distributed through a WhatsApp worm campaign, with the actor now deploying a Python script, a shift from previous PowerShell-based scripts to hijack WhatsApp and spread malicious attachments.

The findings come close on the heels of another campaign dubbed [Water Saci](https://thehackernews.com/2025/11/whatsapp-malware-maverick-hijacks.html) that has targeted Brazilian users with a worm that propagates via WhatsApp Web known as SORVEPOTEL, which then acts as a conduit for [Maverick](https://www.bluevoyant.com/blog/advanced-banking-trojan-maverick-uses-whatsapp-to-prey-on-brazilian-users), a .NET banking trojan that's assessed to be an evolution of a .NET banking malware dubbed [Coyote](https://thehackernews.com/2025/07/new-coyote-malware-variant-exploits.html).

The Eternidade Stealer cluster is part of a broader activity that has abused the ubiquity of WhatsApp in the South American country to compromise target victim systems and use the messaging app as a propagation vector to launch large-scale attacks against Brazilian institutions.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Another notable trend is the [continued](https://thehackernews.com/2023/05/alert-brazilian-hackers-targeting-users.html) [preference](https://thehackernews.com/2024/03/new-banking-trojan-chavecloak-targets.html) for [Delphi-based malware](https://thehackernews.com/2024/07/experts-warn-of-mekotio-banking-trojan.html) for threat actors targeting Latin America, largely driven not only because of its technical efficiency but also by the fact that the programming language was taught and used in software development in the region.

The starting point of the attack is an obfuscated Visual Basic Script, which features comments written mainly in Portuguese. The script, once executed, drops a batch script that's responsible for delivering two payloads, effectively forking the infection chain into two -

* A Python script that triggers WhatsApp Web-based dissemination of the malware in a worm-like fashion
* An MSI installer that makes use of an AutoIt script to launch Eternidade Stealer

The Python script, similar to SORVEPOTEL, establishes communication with a remote server and leverages the open-source project [WPPConnect](https://github.com/wppconnect-team/wppconnect) to automate the sending of messages in hijacked accounts via WhatsApp. To do this, it harvests a victim's entire contact list, while filtering out groups, business contacts, and broadcast lists.

The malware then proceeds to capture, for each contact, their WhatsApp phone number, name, and information signaling whether they are a saved contact. This information is sent to the attacker-controlled server over an HTTP POST request. In the final stage, a malicious attachment is sent to all the contacts in the form of a malicious attachment by making use of a messaging template and populating certain fields with time-based greetings and contact names.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjEtfe_FVNkl7vhP57Y9L8EezwedF3CGV5HNFAlNn8p5iGMw_WlkN5Ob8b-twfvK_JPkWGJMKNLgvTlt2BvGsPqc7VGOf81_4fPBRClGB4HOdDmENHZvQ4Mu6n6KYFhiebBXW3Hn1MGA0yh0bB0SvzXR6UHQs5gst6iMk9fZsTxKcvZYWzkoZi010cad5J/s2600/code.png)

The second leg of the attack commences with the MSI installer dropping several payloads, including an AutoIt script that checks to see if the compromised system is based in Brazil by inspecting whether the operating system language is Brazilian Portuguese. If not, the malware self-terminates. This indicates a hyper-localized targeting effort on the part of the threat actors.

The script subsequently scans running processes and registry keys to ascertain the presence of installed security products. It also profiles the machine and sends the details to a command-and-control (C2) server. The attack culminates with the malware injecting the Eternidade Stealer payload into "svchost.exe" using process hollowing.

A Delphi-based credential stealer, Eternidade continuously scans active windows and running processes for strings related to banking portals, payment services, and cryptocurrency exchanges and wallets, such as Bradesco, BTG Pactual, MercadoPago, Stripe, Binance, Coinbase, MetaMask, and Trust Wallet, among others.

"Such a behavior reflects a classic banker or overlay-stealer tactic, where malicious components lie dormant until the victim opens a targeted banking or wallet application, ensuring the attack triggers only in relevant contexts and remains invisible to casual users or sandbox environments," the researchers said.

Once a match is found, it contacts a C2 server, details for which are fetched from an inbox linked to a terra.com[.]br email address, mirroring a tactic recently adopted by W...