---
title: FortiBleed Targeted FortiGate Firewalls in 110 Million-Credential Harvesting Operation
url: https://thehackernews.com/2026/06/fortibleed-targeted-fortigate-firewalls.html
source: The Hacker News
date: 2026-06-23
fetch_date: 2026-06-24T06:06:30.738746
---

# FortiBleed Targeted FortiGate Firewalls in 110 Million-Credential Harvesting Operation

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [FortiBleed Targeted FortiGate Firewalls in 110 Million-Credential Harvesting Operation](https://thehackernews.com/2026/06/fortibleed-targeted-fortigate-firewalls.html)

**Ravie Lakshmanan**Jun 23, 2026Initial Access Broker / Firewall Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJkhDD5qINhfAhBFXG2C13raQF6T6zAOmnHlArhnLUP5z0ifBzpyq6M_4n11cgynQfZW0mxJWnYU-TDYSpKQHYFHvXsZHCB7uoMFg0w02yZILY-JLMm2-uqm-CA_wIqZHhzl25FfO_lMd7dYm6VfprDP83bz_SoB3MWLEc059E4YCa554bba-qWHW5udHv/s1700-e365/fortigate.jpg)

A Russian-speaking initial access broker (IAB) driven by financial gain is assessed to be behind a large-scale credential-harvesting operation known as **FortiBleed** that has targeted over 430,000 FortiGate firewalls globally.

The [campaign](https://thehackernews.com/2026/06/cisa-warns-fortinet-customers-as.html), active since February 2026, involves collecting credential lists, searching for exposed services, brute-forcing accessible systems, and deploying bespoke sniffers on compromised firewalls.

"Once deployed, these sniffers capture cleartext and hashed credentials from traffic passing through compromised devices," SOCRadar [said](https://socradar.io/wp-content/uploads/2026/06/Dismantling-FortiBleed.pdf) [PDF] in a fresh report. "The actors then crack, validate, and reuse the credentials against Active Directory domains and other exposed services."

Central to the operation is a Golang-based tool called **FortigateSniffer** that takes advantage of the FortiOS built-in diagnostic command -diagnose sniffer packet to passively capture authentication traffic from the infected appliances. The tool is designed to monitor traffic across 24 protocols, parse authentication data, and extract the credentials.

It's suspected that the threat actors may have sought the help of an open-source, AI-native offensive security platform dubbed [CyberStrike](https://github.com/CyberStrikeus/CyberStrike) to assist with some "parts of the workflow." Interestingly, another open-source framework called CyberStrikeAI was put to use in connection with [another automated mass scanning campaign](https://thehackernews.com/2026/03/open-source-cyberstrikeai-deployed-in.html) targeting FortiGate devices that Amazon Threat Intelligence [exposed](https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html) earlier this year.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"The campaign shows a heavy focus on Small and Medium Businesses (SMBs) with fewer than 200 employees," the SOCRadar explained. "The actor targets multiple sectors and regions, with notable emphasis on the United States and India. The IT services sector appears to be a key target. This targeting choice likely helps the actor maximize downstream access, as compromised service providers can create access paths into customer environments."

Perhaps the most interesting finding is that FortiBleed appears to be part of a broader, multi-vendor initial access operation that's orchestrated to not only target Fortinet devices, but also breach Synology NAS, Sophos firewalls, RDWeb portals, Citrix SSL-VPNs, and MS-SQL servers using automated brute-forcing since February 28, 2026.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZZyYbrLcpVz_CoSfqeQXURaddHErJYJte9jiJC2E9d_OThVClTl-Lu53FHSyEGDOTOSs6KLkcrHPXNwBPiU9Nn02KBNNvkcdm-N-sdP7i1TLqyb4iIak96JmKs4FY-PBLDquXpxCYc32TXpaet5qYdHuALHf0sPp6TtMmwLzKvkjPxZ7EDzoQnS5zQfZJ/s1700-e365/fort.jpg)

In all, the attackers are estimated to have launched no less than 659 credential-harvesting pipelines on May 31 and June 15, 2026, resulting in the identification of over 110 million credentials. This included -

* 14.8 million Remote Authentication Dial-In User Service (RADIUS) credentials
* 924,000 NTLM hashes
* 130,000 Kerberos hashes
* 89 million MySQL authentication tokens

The FortiBleed campaign takes place over five stages -

* Perform widespread reconnaissance using tools like Masscan and Shodan to identify vulnerable internet-facing FortiGate firewalls, followed by using a custom utility dubbed FortiProbe-fast and GeoSplit to filter FortiGate systems and group them by country, respectively.
* Compromise the devices with a credential checker named "forticheck" that specifically targets FortiGate's administrative panel and SSL-VPN portal, along with using tools to obtain administrative SSH access via credential stuffing and dictionary attacks.
* Upon establishing access via SSH, FortigateSniffer is deployed to passively intercept authentication traffic across 24 protocols (e.g., TACACS+, Kerberos, RPC, SMB, LDAP, SMTP, FTP, Telnet, RDP, WinRM, MS-SQL, MySQL, PostgreSQL, and RADIUS) using native FortiOS diagnostic commands, making it possible to harvest cleartext credentials and password hashes.
* The password hashes are cracked using Hashmat and Hashtopolis, and orchestrated by a Telegram bot named HASHBOT, after which they are used for lateral movement and Active Directory enumeration.
* Sensitive data from network shares is exfiltrated while stolen session cookies are used to maintain persistent, authenticated access.

"The group does not treat all targets equally," SOCRadar said. "Instead, targets are ranked according to economic value before exploitation resources are allocated."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

What's more, the sniffing mechanism includes a geofencing filter that restricts operations to specific IP ranges, not to mention limiting the activity to between 7 a.m. and 6 p.m. Moscow Time. According to data [captured](https://spycloud.com/blog/what-spycloud-found-inside-the-fortibleed-threat-actor-infrastructure/) by SpyCloud, the FortiGate-related capture cycle is said to have commenced on May 19, 2026, with the hash cracking infrastructure set up towards the end of the month.

"The operation runs in a pipeline of ...