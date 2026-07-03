---
title: FortiBleed Credential Theft Linked to INC and Lynx Ransomware Operations
url: https://thehackernews.com/2026/07/fortibleed-credential-theft-linked-to.html
source: The Hacker News
date: 2026-07-02
fetch_date: 2026-07-03T05:48:49.860215
---

# FortiBleed Credential Theft Linked to INC and Lynx Ransomware Operations

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

# [FortiBleed Credential Theft Linked to INC and Lynx Ransomware Operations](https://thehackernews.com/2026/07/fortibleed-credential-theft-linked-to.html)

**Ravie Lakshmanan**Jul 02, 2026Network Security / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcA80dQWiuszAlBgwcxzc3suImls2cKOwk_2nYMo7UY5MNSdlKNMgibekQNEhWRuxmX5s1JcLHCd_dsDZ3m9oy_FxN-livXwyMIqre86oK8WIOMKUSZwDBvoN7XQOaV63zVBAIKQCH77-RGxhyLNc0bnip4LoUd0P7HsWQx-bxBu8nHr7St5HKs6T1cS6Z/s1700-e365/bleed-ransomware.jpg)

The recently discovered financially-motivated **[FortiBleed](https://thehackernews.com/2026/06/fortibleed-targeted-fortigate-firewalls.html)** campaign has been attributed to INC and Lynx ransomware operations, indicating that the verified, stolen credentials were intended for follow-on intrusions.

"An operator tied to FortiBleed's infrastructure was found actively working negotiation panels for both groups, tying mass FortiGate credential theft directly to ransomware deployment for the first time," SOCRadar [said](https://socradar.io/blog/fortibleed-inc-lynx-ransomware-link/) in a new report published Wednesday.

The company said it tracked scanning activity against approximately 11,250 FortiGate portals in more than 150 countries, followed by confirmed admin-level access on 409 targets and successful completion of the full attack chain on 354 of them. In all, at least 12 ransomware deployments have resulted from this access, causing hundreds of endpoints to be encrypted across affected organizations.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The large-scale credential-harvesting operation, which came to light last month, involved the threat actors systematically scanning the internet for exposed Fortinet devices, attempting to break into them using known credential combinations, and then deploying custom packet sniffers to passively gather credentials and other authentication data from network traffic.

The campaign is assessed to have targeted 430,000 FortiGate firewalls globally, gathering over 110 million credentials in the process. The activity was exposed after an operational security error on the part of the attackers left a server containing credentials stolen from thousands of Fortinet appliances exposed on the internet.

The Golang sniffer is estimated to have been installed on about 12,000 Fortinet devices, making it a subset of the total number of networking gear targeted.

The latest findings from SOCRadar show that an operator with access to FortiBleed infrastructure was found logged in to both INC Ransom and Lynx negotiation panels, with victims listed by INC Ransom overlapping with data from the campaign. The links are based on one of the 200 newly discovered servers associated with the FortiBleed infrastructure that granted visibility into internal files, logs, and operational documentation.

Ensar Seker, chief information security officer at SOCRadar, told The Hacker News via email that the exposed server functioned as a staging staging and operational coordination server, and was not used for phishing or active credential collection.

"It contained target inventories, harvested data, automation scripts, configuration files, and operational artifacts that indicate it was used to coordinate large-scale credential harvesting against internet-facing network appliances," Seker said. "In other words, it served as part of the attackers’ backend infrastructure rather than the infrastructure victims directly interacted with."

Tooling, logs, and working hours indicate that the activity is the work of a Russian-speaking threat actor who likely operates as an initial access broker. Much of the targeting has singled out manufacturing, technology, and logistics sectors in Latin America and the Asia Pacific regions.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

SOCRadar also said it discovered an internal document that indicates it's an organized operation comprising about 20 people with a clear division of labor. "A small core of lead operators drives most high-impact intrusions, backed by specialists and support staff," it added.

In addition, the threat actors are believed to be in possession of at least one zero-day vulnerability in Nextcloud. The threat intelligence firm said it's actively coordinating with the affected vendor.

The Delaware-based company said it also identified Citrix-related artifacts that indicate the activity is likely targeting beyond Fortinet devices. The identified infrastructure included a dedicated target list containing about 29,000 IP addresses and 37 domains associated with Citrix environments. This suggests the automated workflow may be repurposed for other remote access technologies.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi88MjU6Aj4nzMXkyiyP2c4mhvEkI95sBe6pl8lp__xzT4Neks2lRg-u_DcLNtuICRpDz87NVGW9iB-XMGbSKEFfQ696RiypA3iNCu37-289VO2pf66xiOsGkAzibXuusod5alVv73-2M3i9LqU4t3TxvMdbdZtxjj1SZPgAbZjUeZVpXFznFT03MpSimqB/s1700-e365/fortinet.jpg)

"At this stage, the presence of these target lists does not conclusively prove that credential harvesting against Citrix devices has already occurred at scale," Seker explained. "Rather, it demonstrates clear reconnaissance and targeting preparations."

"However, given the sophistication of the infrastructure and the operators proven ability to automate credential collection against Fortinet devices, organizations using internet-facing Citrix infrastructure should treat this as an early warning and verify authentication logs, rotate exposed credentials where appropriate, enforce MFA, and monitor for...