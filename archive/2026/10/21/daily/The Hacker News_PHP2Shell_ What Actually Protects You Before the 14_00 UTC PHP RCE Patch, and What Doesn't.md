---
title: PHP2Shell: What Actually Protects You Before the 14:00 UTC PHP RCE Patch, and What Doesn't
url: https://thehackernews.com/2026/10/php2shell-what-actually-protects-you.html
source: The Hacker News
date: 2026-10-21
fetch_date: 2026-10-22T06:46:43.652151
---

# PHP2Shell: What Actually Protects You Before the 14:00 UTC PHP RCE Patch, and What Doesn't

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

# [PHP2Shell: What Actually Protects You Before the 14:00 UTC PHP RCE Patch, and What Doesn't](https://thehackernews.com/2026/10/php2shell-what-actually-protects-you.html)

**Swati Khandelwal**Oct 21, 2026Vulnerability / Server Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipzsA5sBIvBsTGT1YIrSeK_4YH5ISqTd40ZG1tV8YN1VkjjZuiY6CfQojYR-TIoYKM0EgZM4fYrmdtD25XjeTtgBkTFCQGny4DLL0fTKT5SEFpOFBcxNjLgif_FrX-1d-IX9DE58tQX6ELzGk4cWNpUpU5Eaig8pqdLL2h6qqVCC95ZmHFN6m7tD6m7BY/s1700-nu-rw-lo-l85-e365/php-rce-patch.jpg)

You cannot fully block the [two critical PHP flaws called](https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html) **[PHP2Shell](https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html)** before today's fix, and the one setting being passed around as a workaround is not enough on its own, the security firm that suggested it now says.

PHP will release the fix at **14:00 UTC on October 21** for two flaws it rates 9.2 out of 10, and has given no workaround of its own. Until you can install it, what lowers your risk is taking exposed PHP off the internet or behind access controls, cutting what a compromised server can reach, and having the update ready to apply the moment it lands.

Cloudflare says it is seeing early attempts to exploit the flaws, and has pushed emergency rules for sites behind it that it calls a stopgap until you patch. No compromise has been confirmed, the public exploit code going around has not been shown to work, and neither flaw is in CISA's catalog of known exploited flaws.

PHP has not said which versions are affected, which part of PHP is involved, or whether any setting changes the risk; it says the full details and the fixed versions come with the release.

[⚡ UPDATE — PHP Issues Emergency Patches for Two Critical PHP2Shell RCE Flaws as Exploit Attempts Emerge](https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html)

At the time of writing, that release was not yet out. So nobody outside the group that found the flaws can test whether a given defense works, which is why the advice below is about lowering risk, not promising safety.

## The setting you were told to change is not protection

The workaround spreading on social media and security blogs is one line in a PHP configuration file: **session.upload\_progress.enabled=0**. It turns off Session Upload Progress, a PHP feature that's enabled by default, which records how far a file upload has progressed so another request can check on it.

GMO Flatt Security, a Tokyo security firm, suggested setting it early on October 21, saying it could not be sure the change fully addresses the flaws but thought it would help with some probability.

Later the same day, the firm walked that back. In an update timestamped 14:00 Japan time (05:00 UTC), it said the setting alone is not a complete fix and that attacks getting around it are expected. It told administrators to prepare their update, watch for attack traffic before the release, and apply the fix as soon as it is out.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

Two people from the PHP project said the same thing more bluntly. Replying to someone who suggested the upload-progress setting might patch the flaw, Gina Peter Banyard, a PHP core developer and documentation writer funded by the PHP Foundation, [wrote](https://phpc.social/%40Girgias/117476477429221001): "The only thing I can say is that the only mitigation is patching / upgrading PHP. I sadly know too much." Joe Ferguson, the release manager for the coming PHP 8.6, put it [shorter](https://phpc.social/%40joepferguson/117476265521630745): "ini settings won't save you."

The setting cannot be relied on for two reasons. GMO Flatt expects a way around it but has not said what that is. And the whole idea that the flaw lives in Session Upload Progress is a guess: PHP has not confirmed it, the firm itself said it holds only so far as its own research matches PHP2Shell, and an independent [code audit](https://github.com/xuehuolll/CVE-2026-109618-109619-audit) argues the specific bug others describe in that feature does not exist in released PHP. That audit is from an anonymous account and PHP's own code will settle it, but it is one more reason not to treat the setting as a shield.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7nJt-4vISmBAxZ_dIxc83uZPIJzTEaFOK2giCQ4C6rJtpSws1l_xmiyAtip0QN4ribofvRDLKdY4SWUiKdpKBk6CXAheeUoKpKbrJnYqH2WitMx7nf0V4Kxh8UcDrp7pJzbFPB4ZQqzpWdMsm7GUZmS8y0pS7v3oxupB0rlC-gF3fu4NbXwHqG_WofPA/s1700-nu-rw-lo-l85-e365/flaws.png)

Not everyone agrees. One vendor, Upwind, still lists the setting as an [immediate mitigation](https://www.upwind.io/feed/initial-assessment-php2shell-two-critical-unpatched-php-rces-cve-2026-109618-cve-2026-109619), passing along another researcher's analysis rather than its own tests. watchTowr, which reproduced one of the flaws, [says](https://watchtowr.com/intelligence/php-cve-2026-109618-faq/) there is "no confirmed patch or workaround at this time."

## If you already set it

No one is telling you to undo the change. The instruction is only not to count it as protection. PHP's own manual already advises turning the feature off where an application does not use upload progress bars, because the stored file names and field names "are not validated and may contain PHP code." If you turned it on by mistake somewhere that needs it, the only cost is that upload progress bars stop working.

Check that the change is actually in effect on the process that serves web traffic, not on the command line. The setting is INI\_PERDIR, so it can be set in php.ini, .htaccess, or .user.ini.

A [.user.ini file](https://www.php.net/manual/en/configuration.file.per-user.php) is read only by the CGI and FastCGI versions of PHP, not by the Apache module, and PHP re-reads it only every 300 sec...