---
title: WordPress Backdoor Rebuilds Itself After Cleanup Using Files, Database, and Shared Memory
url: https://thehackernews.com/2026/10/wordpress-backdoor-rebuilds-itself.html
source: The Hacker News
date: 2026-10-01
fetch_date: 2026-10-02T07:49:37.789314
---

# WordPress Backdoor Rebuilds Itself After Cleanup Using Files, Database, and Shared Memory

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [WordPress Backdoor Rebuilds Itself After Cleanup Using Files, Database, and Shared Memory](https://thehackernews.com/2026/10/wordpress-backdoor-rebuilds-itself.html)

**Ravie Lakshmanan**Oct 01, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbdAzWwJ7WC6PL7vtBZDUWfVyYu9iIBlT3X5gZn-Yl9aRuZAEeW3RjEU81RQWsvH_7og6v7-somVgG-fR35drKy6bxLMcHdpJQAi6ydXw-m3oMxZ1hlDC7kr8Wsu0dOfRt6ZLEasAsYNGq-pzmQiBNWMbEBzqa9zYdAu16NtgIfDe3PpOvCVzGj6yFqmet/s1700-nu-rw-lo-l85-e365/wordpress-exploit.jpg)

Cybersecurity researchers have shed light on a WordPress compromise in which threat actors deployed multiple persistence mechanisms to ensure that the final payload kept returning without having to infect the site again.

The backdoor has been codenamed **SC** after the "SC\_" markers present in the injected content. Sucuri has described the malware as a "self-healing mesh" that's blockchain-controlled.

"The payload lives in at least eight places at once, spread across files, the database, and shared memory, and every one of those places can rebuild all the others," security researcher Gabriel Barbosa [said](https://blog.sucuri.net/2026/09/sc-wordpress-malware-a-self-healing-mesh-of-loaders-drop-ins-and-a-blockchain-controlled-backdoor.html).

"Delete the plugin and a drop-in rewrites it. Delete the drop-in and the theme rewrites it. Clean every file on disk, and the next page load restores the whole set from the database or from a shared-memory segment. The result is a circular system with no single point you can remove to stop it."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

According to Sucuri, the malware does not have any readable function names, instead employing a decoder to unscramble the code using a substitution cipher. A summary of the eight components is as follows -

* .user.ini, which sets "[auto\_prepend\_file](https://www.php.net/manual/en/ini.core.php#ini.auto-prepend-file)" to run a loader before every PHP request in that directory tree.
* wp-content/c1b12371.php, the loader that includes a hidden dot-prefixed file if it exists in the same location.
* wp-content/.c1b12371.php, the hidden dot-prefixed file which acts as the first-stage loader to locate a fake plugin and rebuilds it in mu-plugins from three sources: an existing copy in the plugins folder, an encoded stub in the cache directory, and a ZIP restore bundle with a random hex name.
* wp-content/db.php, which is loaded during bootstrap and carries the entire backdoor payload in compressed, Base64-encoded format. It decodes and re-deploys the plugin whenever it's missing or too small.
* wp-content/advanced-cache.php, which is loaded by WordPress before ordinary plugins when caching is enabled, and rebuilds the plugin from five independent sources: an existing mu-plugin, an existing plugin copy, a System V shared-memory segment holding PHP, a ZIP bundle, and the database. It then hooks plugins\_loaded and includes it.
* wp-content/themes/khorshidi/functions.php, a theme-resident twin of db.php that features the same backdoor and rewrites the plugin every time it is not present.
* wp-content/mu-plugins/hyper-engine-kit.php, the actual malware that's installed as both a must-use plugin and a normal plugin.
* wp-content/plugins/hyper-engine-kit/hyper-engine-kit.php, a duplicate of the same backdoor payload for redundancy.

Regardless of the method used to launch the backdoor, it carries out a number of actions, including hiding itself from the admin plugins screen or in update checks, communicating with a command-and-control (C2) server using the Ethereum blockchain, fingerprinting the infected site and retrieving additional payloads, creating a hidden administrator account, and running the reinfection loop.

The backdoor's capabilities allow the operator to take control of the WordPress site, fetch arbitrary JavaScript to inject and target site visitors with skimmers (or other malware), run PHP code, and deactivate or delete specific plugins.

"On servers that support System V shared memory, the payload is written into a segment identified by a fixed numeric key," Sucuri said. "That segment lives in RAM, so it survives file deletion and database cleanup alike, and on shared hosting it can even be owned by a different account."

"The infection registers cron hooks, including randomized names alongside a known fetch hook. System cron runs the WordPress cron file, not visitor traffic, then triggers redeployment on schedule."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

It's currently not known how the malware was delivered to the WordPress site. However, typical initial access vectors include known security flaws in WordPress, plugins, and themes; weak login credentials; software supply chain attacks targeting popular plugins; and the exploitation of insecure media or form upload features to push PHP web shells into server directories.

"SC is a reminder that a modern WordPress infection can be a system rather than a file," Sucuri said. "This toolkit spreads identical copies of one backdoor across drop-ins, the theme, a fake plugin in two locations, the database, and shared memory, hides its command channel inside legitimate blockchain infrastructure, and rewrites itself from any surviving copy on the very next request."

### wpForo Forum WordPress Plugin Flaw Exploited

The disclosure comes as a high-severity unauthenticated SQL injection flaw in the wpForo Forum WordPress plugin ([CVE-2026-1581](https://www.cve.org/CVERecord?id=CVE-2026-1581), CVSS score: 7.5) has come under active exploitation. The issue affects all versions of the plugin up to, and including, 2.4.14.

According to [telemetry data from Previdian](https://previdian.com/CVE-2026-1581), fewer than 20 exploitation attempts targeting the vulnerability have been observed since July 3...