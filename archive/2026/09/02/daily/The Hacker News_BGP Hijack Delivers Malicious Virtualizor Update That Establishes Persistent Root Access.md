---
title: BGP Hijack Delivers Malicious Virtualizor Update That Establishes Persistent Root Access
url: https://thehackernews.com/2026/09/bgp-hijack-delivers-malicious.html
source: The Hacker News
date: 2026-09-02
fetch_date: 2026-09-03T07:02:42.083104
---

# BGP Hijack Delivers Malicious Virtualizor Update That Establishes Persistent Root Access

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

# [BGP Hijack Delivers Malicious Virtualizor Update That Establishes Persistent Root Access](https://thehackernews.com/2026/09/bgp-hijack-delivers-malicious.html)

**Swati Khandelwal**Sep 02, 2026Network Security / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjc5HwRa7RftYjoKUzpULa7DXn6tt4sZ7RrL1PNBN0Um5di5vxvgRQvmF3rF9-Xb7URM6YD9t-kEu0e3VBeERcdHio4Bz92EOYUwR2s3dosskPZbfztVyjAQ8p-h9PZ7ns3O8uOJ-DSxWPSIanM7l0lC2AZr71eXzWkSXTb_TjLmyBKvMR1KE97xp8PKJU/s1700-nu-rw-lo-l85-e365/virtualizer.jpg)

**Virtualizor** said hackers used a Border Gateway Protocol (BGP) hijack to divert **Softaculous** traffic. The hackers then used the diverted update traffic to deliver a malicious Virtualizor package to some installations. A hosting-provider account separately said 5 of its 34 checked Virtualizor hypervisors sustained root-level compromise.

The incident window ran from approximately August 28 at 20:57 Coordinated Universal Time (UTC) to August 30 at 06:10 UTC. Virtualizor said every operator should check its servers because the company has no affected-version range or definitive list of installations that received the package.

Virtualizor released Patch 9 with a Security Analyzer on September 1, but the vendor said cryptographic package signing remained future work. Operators should run the official scanner, rotate and restrict application programming interface (API) credentials, and audit each server for persistence and unauthorized access.

"This affected a handful of servers rather than the general Virtualizor user base," Virtualizor said in its [incident advisory](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/).

The first route announcement containing the vendor-identified path appeared at 20:57:30 UTC on August 28, The Hacker News confirmed using [RIPE Stat data](https://stat.ripe.net/data/bgp-updates/data.json?resource=162.55.80.0%2F24&starttime=2026-08-28T20%3A50%3A00&endtime=2026-08-30T10%3A00%3A00). Virtualizor said the route was unauthorized. Traffic for Softaculous services was diverted to an attacker-operated server.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The attacker obtained a valid Let's Encrypt certificate during the diversion window. Connections routed through the server therefore displayed no certificate warning. A Virtualizor installation that checked for updates during a diverted interval could receive the modified package. The update client lacked cryptographic package verification, so it did not reject the package on that basis.

The AlbaHost account, displayed as a Member and Patron Provider on LowEndTalk, said malicious commands had been inserted into three legitimate Virtualizor files. A root cron job later executed the modified code.

"We can confirm that 5 of our 34 Virtualizor hypervisor nodes contained the same malicious modifications described in this thread," the [AlbaHost account](https://lowendtalk.com/discussion/comment/4856297/) said.

The injected code added an attacker-controlled key to the root account. It installed Java 17 when the runtime was absent. It downloaded the Java payload. The payload was then executed as root.

The payload established persistence through a systemd service. It also created an unauthorized account named `proxyuser`. A successful password-based Secure Shell (SSH) login to that account from `193.32.127[.]248` appeared in the provider's logs.

In its examined environment, the AlbaHost account said it had no confirmed modification of customer virtual private servers and had not independently confirmed a database export.

Client-area sessions and payment-entry traffic during the diversion window may have reached the attacker-operated server, Virtualizor said. As of September 2, the vendor had not reported confirmed client-account or payment-data theft.

The vendor's guidance applies to the following groups -

* **Virtualizor operators** - Check every server because no affected-version range or definitive affected-server list is available.
* **Client-area users who logged in or entered payment details during the incident window** - Reset the client-area password, change it anywhere it was reused, review account activity, and review card statements if payment details were entered during the incident window. Client Center API users should regenerate their keys and update them on their servers.
* **Other Softaculous product operators** - Check Webuzo, Softaculous, Backuply, SitePad, and other product servers that performed an update check during the incident window. The vendor had not identified a malicious package for those products and said its investigation remained open.

### What Virtualizor Operators Should Do

Virtualizor advised operators to perform the following steps -

1. Check for `/etc/systemd/system/java-jre-update.service`. If present, preserve the evidence and contact Virtualizor support.
2. Rotate all Virtualizor API keys, restrict API access to trusted Internet Protocol (IP) addresses, and remove unrecognized keys.
3. Audit unknown SSH keys, new users, scheduled tasks or cron jobs, and unexpected outbound connections, and restrict SSH to trusted IP addresses.
4. Run the [official scanner](https://files.virtualizor.com/security/virtualizor_security_scan.sh), whose retrieved-script SHA-256 was `73e74402b3a61c7bab289fc11347bd54c7fcdc2fa2e410f4c3de9d6cd7377d48` when checked on September 2, 2026.
5. Contact support before remediating a positive host so evidence can be preserved. Treat scanner containment as containment of known indicators. Perform further remediation to restore host trust.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

The vendor's scanner checks the following indicators of compromise (IoCs) -

* **Systemd unit** - `/etc/systemd/system/java-jre-update.service`
* **Installed payload** - `/usr/lib/jvm/.cache/jre-runtime.dat`
...