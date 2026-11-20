---
title: PHP Fixes 7 Critical Flaws, Including Bugs That Could Allow Remote Code Execution
url: https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html
source: The Hacker News
date: 2026-11-19
fetch_date: 2026-11-20T09:23:12.980560
---

# PHP Fixes 7 Critical Flaws, Including Bugs That Could Allow Remote Code Execution

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

# [PHP Fixes 7 Critical Flaws, Including Bugs That Could Allow Remote Code Execution](https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html)

**Swati Khandelwal**Nov 19, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjD2D26Hu7r43uUrdDxmsmmbBe2oMxd-L3_DIVLqAPyDrOnSmdvXfkIq1_lNmWqr49gbrIZ0NeTmA2OYgyWgdUjRf_RTRfflyXn3Vgujkb9tiByOPfej1OqEszpQf2FeozeSqmK5L7aSj28GLwzKmzehIp9zJyeJqgRvbVOW91_pVEMhs3KY9_oXjwf5BE/s1700-nu-rw-lo-l85-e365/php-flawss.jpg)

The PHP Foundation has [released](https://www.php.net/) security updates to address [multiple critical security flaws](https://thehackernews.com/2026/11/php-warns-of-critical-security-flaws.html) that could be exploited to achieve remote code execution on affected deployments, including CVE-2026-115560.

The release of the patch follows an advance notice in which the project maintainers alerted users to multiple critical vulnerabilities affecting all supported PHP versions under specific conditions, including non-default configuration or uncommon setups.

At a high level, successful exploitation of the defects could pave the way for remote code execution, session corruption, denial-of-service, memory corruption, or local privilege escalation.

The [list of vulnerabilities](https://github.com/php/php-src/security/advisories) is as follows -

* **[CVE-2026-115560](https://github.com/php/php-src/security/advisories/GHSA-658j-r8rw-q6mx)** (CVSS score: 9.2) - An improper input validation vulnerability that could result in remote code execution, file modification, session corruption, or denial-of-service. (Fixed in PHP 8.2.36, 8.3.37, 8.4.28, 8.5.13, 8.6.0)
* **[CVE-2026-129182](https://github.com/php/php-src/security/advisories/GHSA-2fjv-p558-g82m)** (CVSS score: 9.2) - A use-after-free vulnerability that could result in memory corruption and possible full remote code execution, as in the case of CVE-2026-109619. (Fixed in PHP 8.5.13, 8.6.0)
* **[CVE-2026-126714](https://github.com/php/php-src/security/advisories/GHSA-fm2m-fjf5-v3cp)** (CVSS score: 9.2) - A Time-of-check Time-of-use (TOCTOU) vulnerability that could result in the execution of arbitrary code with the privileges of the PHP worker. Successful exploitation requires an attacker's influence over the session data, an interruption at a useful point in the write, and an application with a suitable deserialization gadget chain. (Fixed in PHP 8.2.36, 8.3.37, 8.4.28, 8.5.13, 8.6.0)
* **[CVE-2026-129289](https://github.com/php/php-src/security/advisories/GHSA-qc49-hpvq-g2w6)** (CVSS score: 9.2) - An inconsistent interpretation of HTTP requests vulnerability that could result in execution of attacker-controlled PHP code as the worker without another user's interaction or a non-default PHP configuration. Successful exploitation requires a front end that enables persistent backend connections and an application path that opens "php://input" without reading it fully, such as nginx with fastcgi\_keep\_conn on, Apache mod\_proxy\_fcgi with enablereuse=on, HAProxy FastCGI applications that retain backend connections, and LSAPI. (Fixed in PHP 8.2.36, 8.3.37, 8.4.28, 8.5.13, 8.6.0)
* **[CVE-2026-129474](https://github.com/php/php-src/security/advisories/GHSA-8mjj-2r7p-4hg2)** (CVSS score: 9.2) - A use-after-free vulnerability that could result in remote code execution on PHP 8.5 and later. Successful exploitation depends on the application and requires control over enough request data to influence memory allocation, a reachable magic method call, and a fatal error at the relevant point. (Fixed in PHP 8.5.13, 8.6.0)
* **[CVE-2026-129481](https://github.com/php/php-src/security/advisories/GHSA-g3vh-838c-65v7)** (CVSS score: 9.2) - A use-after-free vulnerability that could cause an application's session cleanup to fail and potentially corrupt memory, crash a reused PHP worker, or potentially allow remote code execution. (Fixed in PHP 8.3.37, 8.4.28, 8.5.13, 8.6.0)
* **[CVE-2026-129496](https://github.com/php/php-src/security/advisories/GHSA-gr4f-wgx5-jpfv)** (CVSS score: 9.2) - A use-after-free vulnerability that could allow an unauthenticated remote attacker to crash PHP workers or execute arbitrary code with their privileges on an affected deployment. (Fixed in PHP 8.2.36, 8.3.37, 8.4.28, 8.5.13, 8.6.0)
* **[CVE-2026-129291](https://github.com/php/php-src/security/advisories/GHSA-jm4m-qfqx-967m)** (CVSS score: 8.8) - A use-after-free vulnerability that could result in local privilege escalation. Successful exploitation requires local code execution in an FPM worker, an affected pool with catch\_workers\_output enabled, the epoll event backend, and the ability to manipulate worker lifetimes and retain inherited pipe descriptors. (Fixed in PHP 8.2.36, 8.3.37, 8.4.28, 8.5.13, 8.6.0)

Depthfirst, which has [codenamed](https://depthfirst.com/research/phpaftershell) CVE-2026-126714 "[phpAfterShell](https://depthfirst.com/phpaftershell)," has described it as a critical flaw that can enable a remote attacker to run arbitrary code on affected servers.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyXpwvtMdoAn3EJg8tVRN8RDgLZ_BJNDuY7Mh7bLIS5_MBQN6DRFFl-paksq9OwsrkLN1YQALrOomSFUD4S6F11XG9vdH7AWU0YKq1yZmHSfhNuj0ZC9f6f2b2qDEIrfPWjsHca0g3YbPVPkp5qieU_QBA8bgJ3uViBawRPNDGgk5xutQ6ogSUm_3r_w0/s1700-nu-rw-lo-l85-e365/php-poc.gif)

"If a pwrite()/ftruncate() update is interrupted, PHP may leave behind a malformed session file that is later loaded by session\_start(), yielding an arbitrary deserialization primitive," Depthfirst said. "Chained with another of our PHP-native deserialization-to-RCE findings, this leads directly to remote code execution."

Put differently, the vulnerability turns an interrupted file write into a potential remote code execution primitive by manipulating how PHP writes session data to disk, causing it to interpret previously harmless data as executable object data.

It th...