---
title: Open VSX Supply Chain Attack Used Compromised Dev Account to Spread GlassWorm
url: https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html
source: The Hacker News
date: 2026-02-02
fetch_date: 2026-02-03T04:11:07.529706
---

# Open VSX Supply Chain Attack Used Compromised Dev Account to Spread GlassWorm

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Open VSX Supply Chain Attack Used Compromised Dev Account to Spread GlassWorm](https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html)

**Ravie Lakshmanan**Feb 02, 2026Developer Tools / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPOwjTAXR_bWT_xYvDJKDsLnYrGiJXhQxeF4lVk_19Ovkom1S6fZsO3tDeSdpK2EZ8Q8ZJeDpWLtRhNHRisN-pwNwio6DDz24wH3nMyfzsT_ZpD2Mq08hKMJXWt_p8RxIK4DVpk70Ssm114e1BzrMJDDij0pYO1ZEOixGZtD0pB61mQWATJkAJP6gl_9BK/s1700-e365/open.jpg)

Cybersecurity researchers have disclosed details of a supply chain attack targeting the Open VSX Registry in which unidentified threat actors compromised a legitimate developer's resources to push malicious updates to downstream users.

"On January 30, 2026, four established Open VSX extensions published by the oorzc author had malicious versions published to Open VSX that embed the GlassWorm malware loader," Socket security researcher Kirill Boychenko [said](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise) in a Saturday report.

"These extensions had previously been presented as legitimate developer utilities (some first published more than two years ago) and collectively accumulated over 22,000 Open VSX downloads prior to the malicious releases."

The supply chain security company [said](https://github.com/oorzc/vscode_sync_tool/issues/25) that the supply chain attack involved the compromise of the developer's publishing credentials, with the Open VSX security team assessing the incident as involving the use of either a leaked token or other unauthorized access. The malicious versions have since been removed from the Open VSX.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The list of identified extensions is below -

* FTP/SFTP/SSH Sync Tool (oorzc.ssh-tools — version 0.5.1)
* I18n Tools (oorzc.i18n-tools-plus — version 1.6.8)
* vscode mindmap (oorzc.mind-map — version 1.0.61)
* scss to css (oorzc.scss-to-css-compile — version 1.3.4)

The poisoned versions, Socket noted, are designed to deliver a loader malware associated with a known campaign called [GlassWorm](https://thehackernews.com/2025/12/glassworm-returns-with-24-malicious.html). The loader is equipped to decrypt and run embedded at runtime, uses an increasingly weaponized technique called EtherHiding to fetch command-and-control (C2) endpoints, and ultimately run code designed to steal Apple macOS credentials and cryptocurrency wallet data.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0VcA6FnngFXhuJ5_Q2S-uhoa3JI6lYqYZnjsZF50SyBd-x0IM5Sj__qRadKnAWdqvIy6mGcRpA1LnO7ylmneqcgM4y5PWmIpGn_9yy0_vnEf4oTuyTRH9-L7FpzfSl8Ch5zJEumGKZltEw-QijGIh-s_LkLqb5JJ8HpZ4UAcB4sQ6Z567zsFKPAJOX2X-/s1700-e365/vscode.jpg)

At the same time, the malware is detonated only after the compromised machine has been profiled, and it has been determined that it does not correspond to a Russian locale, a pattern commonly observed in malicious programs originating from or affiliated with Russian-speaking threat actors to avoid domestic prosecution.

The kinds of information harvested by the malware include -

* Data from Mozilla Firefox and Chromium-based browsers (logins, cookies, internet history, and wallet extensions like MetaMask)
* Cryptocurrency wallet files (Electrum, Exodus, Atomic, Ledger Live, Trezor Suite, Binance, and TonKeeper)
* iCloud Keychain database
* Safari cookies
* Data from Apple Notes
* user documents from Desktop, Documents, and Downloads folders
* FortiClient VPN configuration files
* Developer credentials (e.g., ~/.aws and ~/.ssh)

The targeting of developer information poses severe risks as it exposes enterprise environments to potential cloud account compromise and lateral movement attacks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

"The payload includes routines to locate and extract authentication material used in common workflows, including inspecting npm configuration for \_authToken and referencing GitHub authentication artifacts, which can provide access to private repositories, CI secrets, and release automation," Boychenko said.

A significant aspect of the attack is that it diverges from previously observed GlassWorm indicators in that it makes use of a compromised account belonging to a legitimate developer to distribute the malware. In prior instances, the threat actors behind the campaign have leveraged typosquatting and brandjacking to upload fraudulent extensions for subsequent propagation.

"The threat actor blends into normal developer workflows, hides execution behind encrypted, runtime-decrypted loaders, and uses Solana memos as a dynamic dead drop to rotate staging infrastructure without republishing extensions," Socket said. "These design choices reduce the value of static indicators and shift defender advantage toward behavioral detection and rapid response."

### Update

Secure Annex researcher John Tuckner told The Hacker News that three of the aforementioned extensions were still available for download as of February 2, 2026, 6:30 a.m. UTC. They have since been removed from Open VSX as of writing -

* oorzc.mind-map@1.0.61
* oorzc.i18n-tools-plus@1.6.8
* oorzc.scss-to-css-compile@1.3.4

"This is also tricky because victims will have to wait until the real developer publishes a new higher version in order for an auto update to be triggered," Tuckner said. "Even if the extensions are removed from the marketplace, they won't uninstall from editors."

*(The story was updated after publication to include details of the extension status.)*

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[...