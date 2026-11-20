---
title: Everything Is a Web Application, Including Your Firewall
url: https://thehackernews.com/2026/11/everything-is-web-application-including.html
source: The Hacker News
date: 2026-11-19
fetch_date: 2026-11-20T09:23:13.328831
---

# Everything Is a Web Application, Including Your Firewall

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Everything Is a Web Application, Including Your Firewall](https://thehackernews.com/2026/11/everything-is-web-application-including.html)

**The Hacker News**Nov 19, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiC0roCfV92el2-gLSGwmumyjXgCjHookzwGjft2a6UWPZA1QvyrazDNLTvlZrF1F5iagg74JxnPEXbnK60OEeJuFNo2Fc2xcNSnJCeNw9BLu_y-lsRhrpO6s1End2gdDDlRU_r4wysTiiJS4ZKPDTmWK152psFdhxRizlSJZFCjnYr6nnamRsUciEJui4/s1700-nu-rw-lo-l85-e365/php-app.jpg)

One of the early targets of PHP2Shell exploitation was the firewall. On October 28, Palo Alto Networks [confirmed](https://thehackernews.com/2026/10/attackers-exploit-php2shell-flaws-in.html) that attackers were exploiting the two PHP vulnerabilities, CVE-2026-109618 and CVE-2026-109619, against PAN-OS management interfaces exposed to the internet. Both flaws let anyone execute code on the web server without authentication. The disclosure itself went a little wrong. Details leaked on October 20, ahead of the coordinated release, and the PHP project shipped an emergency patch the next day.

The vulnerabilities require no authentication, but they are not easy to exploit reliably. It takes skill and additional knowledge about the target system. Where it matters a lot is appliances, which run identical, often outdated software that an attacker can study in advance. That is the bigger picture. An awful lot of web applications control critical devices in your network. Almost anything is a web application to some extent. That often goes unrecognized, and as a result those applications aren't adequately protected.

Everything is a web application. That is the motto of the SANS course I teach, [SEC522: Application Security: Securing Web Applications, APIs, and Microservices](https://www.sans.org/cyber-security-courses/application-security-securing-web-apps-api-microservices?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_CDI26_Nov_OA_522_CP&utm_campaign=SANS_CDI_2026). Web application security has traditionally been treated as a developer issue, yet anyone protecting a network must understand how web applications work to properly defend them.

## **Why Appliances Are the Softer Target**

On ordinary web servers, address space layout randomization (ASLR) is one of the features that makes exploitation harder. It shuffles where code and data sit in memory, so an exploit can't rely on fixed addresses. VulnCheck's [early analysis](https://www.helpnetsecurity.com/2026/10/22/php2shell-vulnerability-fortinet-cisco-palo-alto-networks/) found the bugs exploitable on ARM64 systems and on x86 systems without ASLR. Few public exploits bypassed ASLR on x86-64, and the one VulnCheck confirmed worked only against a single PHP build. [VulnCheck's own exploit](https://www.vulncheck.com/blog/php2shell-vulnerabilities) chained a memory leak to get code execution with ASLR enabled.

Appliances change that math, not because the protections are missing, but because every device on a given software version runs the same binaries, so an attacker can work out memory offsets in advance. The PAN-OS exploit still had to defeat ASLR, leaking the libphp.so base address through the Set-Cookie header, and SELinux confined the resulting shell. PAN-OS also ships end-of-life PHP versions (8.0.30 and 7.4.33). Israeli security firm Dream, working with Palo Alto Networks on the investigation, [found](https://thehackernews.com/2026/10/attackers-exploit-php2shell-flaws-in.html) the attacker had obtained PAN-OS firmware, decrypted it, extracted the PHP libraries, and built precise memory profiles for nine software versions. The actor then chained PHP2Shell with a Linux kernel flaw ([Fragnesia, CVE-2026-46300](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)) to gain root on 25 systems (24 firewalls and one management server) in the U.S., Japan, Taiwan, and South Korea.

Web application security tends to focus on large, cloud-based applications. It's often the little things, the mosquitoes on the internet, that do you in. Appliances run predictable, often outdated software, and they are everywhere.

## **HTTP Is More Complex Than Your Defenses Assume**

HTTP is a very complex protocol with lots of options. To upload a file, a client doesn't have to send it in one piece. It can send the body in chunks without declaring its total length, and, if the server decompresses request bodies, compress it, which makes it difficult for a web server to calculate how much memory it needs to store it. Memory-safety bugs remain common as a result, in web applications and in the web servers running them. In PHP2Shell, a crafted multipart upload [pushes PHP past its memory limit](https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/) while it is still parsing the request, before any application code runs. The bugs are in what PHP leaves behind when it aborts the request: [uninitialized request memory (CVE-2026-109618) and a pointer to freed memory (CVE-2026-109619)](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/). The request doesn't need to be large, either. Deeply nested, empty file fields make PHP allocate far more memory than the body contains, so a request well under the default 8 MB post\_max\_size can still exhaust the default 128 MB memory limit.

Defenders must understand the protocol to know what these vulnerabilities look like, for example to write signatures that detect the exploits. The same complexity limits the middle boxes we rely on. They can even interfere in ways nobody planned. [Intruder found](https://www.intruder.io/research/how-exploitable-is-php2shell) that nginx in front of PAN-OS buffered chunked request bodies, which broke public exploit chains. Web application firewalls are often not adequate, and file uploads are key functionality for a lot of web applications, so blockin...