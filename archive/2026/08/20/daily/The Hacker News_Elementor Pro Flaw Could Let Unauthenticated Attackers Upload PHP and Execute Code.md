---
title: Elementor Pro Flaw Could Let Unauthenticated Attackers Upload PHP and Execute Code
url: https://thehackernews.com/2026/08/elementor-pro-flaw-could-let.html
source: The Hacker News
date: 2026-08-20
fetch_date: 2026-08-21T03:05:10.354646
---

# Elementor Pro Flaw Could Let Unauthenticated Attackers Upload PHP and Execute Code

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Elementor Pro Flaw Could Let Unauthenticated Attackers Upload PHP and Execute Code](https://thehackernews.com/2026/08/elementor-pro-flaw-could-let.html)

**Ravie Lakshmanan**Aug 20, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitKWjeNJOL_DEahUmMAYpH9qh94s2iFi8igtfSlAzOVWiUBU-EIM0MWMsFYPmA5NDL6Rs9E-w9vvCmw3Cc6Og0q-TDt87Q2hwYIePNAQ0xQ3OJYHzgCizDFm-YK9SxW4ncWnuVLaOzgb3SPO7Qpx17zHMaFzBQfYllgz5IP-p1jMALgWlasRkj1nV3Tq3G/s1700-e365/wordpress.jpg)

Cybersecurity researchers have disclosed details of a critical flaw in the Elementor Pro WordPress plugin that, if successfully exploited, could lead to remote code execution.

The vulnerability, tracked as **[CVE-2026-32475](https://www.cve.org/CVERecord?id=CVE-2026-32475)**, carries a CVSS score of 9.0 out of 10.0. It has been described as a case of unrestricted upload of a file with a dangerous type.

"The flaw lives in the Forms module's File Upload field, where the extension check and the file-move step run in two separate loops with different handling of empty file entries," Patchstack [said](https://patchstack.com/articles/critical-unauthenticated-file-upload-to-rce-in-elementor-pro-plugin/).

"By submitting two file parts for the same field, an unauthenticated attacker skips the extension blocklist entirely and writes a PHP file into a public directory."

This discrepancy in how it validates the file's extension and moves the uploaded file to a public directory when empty file entries are processed turns a restricted file-upload field into an unauthenticated remote code execution primitive.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Successful exploitation of the flaw could allow an attacker to upload arbitrary files, including PHP scripts, that could then be used to achieve remote code execution on affected systems. The security defect impacts all versions of the plugin prior to and including version 4.2.1.

The WordPress security company said the only precondition required to pull off an attack is that the target site has at least one published Elementor page containing a Form widget with a File Upload field. The uploaded file is written as "wp-content/uploads/elementor/forms/<uniqid>.php," where "<uniqid>" is the output of PHP's [uniqid() function](https://www.php.net/manual/en/function.uniqid.php).

"This is an extremely common, everyday configuration: job-application forms, 'attach a photo/ID/receipt' forms, and support-ticket attachments all use it," it noted. "The field's 'Required' toggle being off is its default state, so no hardened or unusual setting is needed."

Security researcher Tin Pham (aka TF1T) has been credited with discovering and reporting the flaw under the Patchstack Bug Bounty Program. After the issue was reported to Elementor Pro on July 16, 2026, a patch (version 4.2.2) was released on August 19.

The release comes a little over a week after WordPress [released 7.0.4](https://wordpress.org/news/2026/08/wordpress-7-0-4-release/) to address a high-severity security issue ([CVE-2026-65640](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-8vr3-7mxf-gx8w), CVSS score: 8.8) that enables remote code execution via malicious Postscript file upload by an Author-level user or higher. It affects WordPress core versions 4.7 all the way up to 7.0.

However, for the attack to be successful, two conditions have to be satisfied -

* Imagick and Ghostscript in use on the server, given the issue is in Ghostscript's handling of certain embedded files
* A malicious user with the upload\_files capability

The update "changes how WordPress hands your uploaded media to ImageMagick, and it closes a path that could let a logged-in author turn an ordinary-looking image upload into code execution on your server," Patchstack [said](https://patchstack.com/articles/when-a-png-isnt-a-png-wordpress-patches-an-author-level-imagick-rce/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"If you run a multi-author publication, a membership site, a client site with contributors, or anything with open or loosely managed registration, that bar is a lot lower than it sounds. On those sites, an Author uploading a booby-trapped 'image' is a genuinely realistic threat, not a theoretical one. If it's just you and a tightly held set of trusted editors, your exposure is smaller."

The findings also coincide with the discovery of a large-scale operation dubbed [StopAndProtect](https://thehackernews.com/2026/08/stopandprotect-uses-nearly-2000-hacked.html) that's turning thousands of compromised WordPress websites into a distributed infrastructure for malware delivery, command-and-control communications, and the storage of stolen data.

WordPress users are [advised](https://blog.sucuri.net/2024/09/how-do-website-owners-know-that-their-website-is-hacked.html) to keep their websites and plugins up-to-date, scan for unauthorized modifications that serve unexpected redirects or pop-ups, and audit them for unknown accounts and plugins.

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

[Application S...