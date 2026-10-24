---
title: PHP Warns of Another Unpatched RCE Risk Two Days After Emergency PHP2Shell Patches
url: https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html
source: The Hacker News
date: 2026-10-23
fetch_date: 2026-10-24T06:48:22.100053
---

# PHP Warns of Another Unpatched RCE Risk Two Days After Emergency PHP2Shell Patches

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [PHP Warns of Another Unpatched RCE Risk Two Days After Emergency PHP2Shell Patches](https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html)

**Swati Khandelwal**Oct 23, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSXE1XecomGt7TSLi_DCDVL8oQjsLEtppNNGjkuW1cbVl-cXZkMG-rqTr-oSVz_6XfoU8aoScw3rjGxsnTpV3JaV5eWfj431lg09Rnrrk1UjwNq1ZEofkwR4FaM2qatC_FD9ZNBZk-T9_9ddu8n-BtUkhwVgWzc2ZvaWAHP8eMxlLU19qxIjlXeHOJYHs/s1700-nu-rw-lo-l85-e365/php2.jpg)

PHP has warned of another way an attacker could run code on a web server, two days after it shipped emergency fixes for the critical PHP2Shell flaws.

The new issue, assigned **CVE-2026-115560**, affects only web applications configured in an unusual way, and PHP considers it an unlikely risk.

The project is not issuing an emergency fix for it. Instead, it recommends turning off a feature called **session upload progress** until a fix is available in the next routine release.

The warning came in a short [informational advisory](https://www.php.net/archive/2026.php#2026-10-23-1) published on October 23. It follows the October 21 [emergency release](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html) that fixed two critical PHP2Shell flaws, **CVE-2026-109618** and **CVE-2026-109619**, which let an attacker without an account run code on a server. Those were patched in PHP 8.5.12, 8.4.27, 8.3.36, and 8.2.35. The new issue is separate and is not fixed by those releases.

Only a narrow setup is at risk. PHP says the problem can occur when a web application does all of the following: sets the **session.serialize\_handler** option to php\_binary or php\_serialize in its configuration, then changes that option to php while running by calling ini\_set(), and makes that change before it calls session\_start().

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Session upload progress must also still be turned on. An application that never changes the serialize handler while running can leave the feature on and is not exposed through this path. PHP says this setup is unlikely in practice.

The action is one line. PHP recommends setting **session.upload\_progress.enabled=0** until the next routine bugfix release. This is the same setting it already listed as a mitigation in the October 21 [advisory](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp) for CVE-2026-109619.

Anyone who applied it then and left it in place needs to do nothing more for the new issue. Session upload progress is turned on by default and lets an application track the progress of a file upload.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLc5CkmqMPCNMKxkUjSlDL5IlCQeWS-_TIRXTt7oKMQRRpvUpoVLSIAcyQQgK8sBLs3cdO2aftMc2GUCAVnvhAtT6ekj58gJT80Ex5ol52Be9N10QpdyjzUGNPdcXDqc_hoPIFr-4GsUDNXUcwRiJf0dPlFLQsTfwqOlyym6eAJLMWFbk4VNBmgOxQQbc/s1700-nu-rw-lo-l85-e365/phpx.jpg)

Because the setup is uncommon, PHP is handling the fix as part of its regular release cycle rather than as an emergency, and it will publish a full advisory for CVE-2026-115560 with the next release.

PHP has not stated which versions are affected, which releases will contain the fix, or a severity score. It also has not said whether the new issue shares a root cause with CVE-2026-109619.

No exploitation of CVE-2026-115560 has been reported; the attacks reported since October 21 target the two earlier PHP2Shell flaws.

Separately, attempts to exploit the two earlier PHP2Shell flaws have surged. Amazon said its [honeypots logged an exploit attempt](https://thehackernews.com/2026/10/someone-tried-to-exploit-php2shell-4.html) against CVE-2026-109618 and CVE-2026-109619 on October 17, four days before the flaws were disclosed, and Cloudflare said attempts [rose from tens of thousands](https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html) within 45 minutes of the October 21 disclosure to millions by early October 22.

Attackers have tried to use the flaws to install a Mirai botnet variant, according to Sophos and Arctic Wolf. Those attempts have so far failed: Previdian, Wordfence and others report scanning and probing but no confirmed code execution, and researchers say a reliable exploit is proving harder to build than expected. That activity targets the two flaws patched on October 21, not CVE-2026-115560, which has not been reported under attack.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[PHP](https://thehackernews.com/search/label/PHP), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Researchers Demonstrate OpenBSD Root Exploit Chaining 37-Year-Old Shared-Memory Bug](https://thehackernews.com/2026/10/researchers-demonstrate-openbsd-root.html)

[![The Hacker News](data:image/svg+xml;base64...)

Critical PwnEscape Linux Kernel Vulnerability Lets Guest VMs Read Host Memory](https://thehackernews.com/2026/10/critical-...