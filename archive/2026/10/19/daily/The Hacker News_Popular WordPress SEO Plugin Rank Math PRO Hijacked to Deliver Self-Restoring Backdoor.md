---
title: Popular WordPress SEO Plugin Rank Math PRO Hijacked to Deliver Self-Restoring Backdoor
url: https://thehackernews.com/2026/10/popular-wordpress-seo-plugin-rank-math.html
source: The Hacker News
date: 2026-10-19
fetch_date: 2026-10-20T06:53:58.179741
---

# Popular WordPress SEO Plugin Rank Math PRO Hijacked to Deliver Self-Restoring Backdoor

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

# [Popular WordPress SEO Plugin Rank Math PRO Hijacked to Deliver Self-Restoring Backdoor](https://thehackernews.com/2026/10/popular-wordpress-seo-plugin-rank-math.html)

**Swati Khandelwal**Oct 19, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEja-6AhEjL8YvRsoNjXIIDEnsVd8gMMW_cUqMvLNcRukJXjatSuo-phLfYxt2A76gSCk-uZFmo4EbJjQuMr8_k8Pxl2ho1TnUL_50Q_VknkR8JqnTiVOqZ48i5W6Mv6HB0cQfJoAjs8xHUu6urkucsPClURVP3aWM0aivfngCFZLykMYzJITwenYfSb9Sk/s1700-nu-rw-lo-l85-e365/wordpress-rank.jpg)

Copies of Rank Math PRO, the paid version of the Rank Math SEO plugin for WordPress, that were downloaded from rankmath.com or delivered as updates between 20:02 UTC on October 15 and 07:12 UTC on October 16 contained malware, Rank Math said in a [security notice](https://rankmath.com/kb/pro-3-0-123-security-incident/) published on October 16.

Any site that installed and activated one of those copies should be treated as compromised, and the malware can recreate its hidden backdoor whenever someone visits the site.

Rank Math has removed the affected files and released a clean version, 3.0.124. Installing it replaces the plugin but does not remove files, administrator accounts, or scheduled tasks the malware may already have placed elsewhere on the server, Wordfence said in an [advisory](https://www.wordfence.com/blog/2026/10/rank-math-seo-pro-3-0-123-malware/) on October 17.

### Who Is Affected

The version number does not show whether a copy is affected. Rank Math's [changelog](https://rankmath.com/changelog/pro/v3-0-123/) dates 3.0.123 to October 7, more than a week before the window opened, and the notice limits the incident to copies downloaded or installed through an update during the window.

A copy of 3.0.123 obtained before 20:02 UTC on October 15 is outside it.

The notice sorts sites into three cases:

* You installed and activated 3.0.123 during the window: treat the site as compromised, even if it has since been updated to 3.0.124, and follow the recovery steps below.
* You installed it but never activated it: delete the plugin files, install 3.0.124 from your Rank Math account, and run a security scan.
* You downloaded it but never installed or activated it: nothing in this incident alone indicates the site was compromised.

Rank Math has emailed some users about the incident and told anyone unsure whether the files were installed or activated to contact its support team.

The notice applies only to the PRO plugin, which customers download and update from rankmath.com rather than WordPress.org. The [free Rank Math SEO plugin](https://wordpress.org/plugins/seo-by-rank-math/) on WordPress.org, which lists more than 4 million active installations and was last updated on October 6, is not named in it.

### What the Malware Does

What is known about the malware comes from Rank Math's notice. Neither it nor Wordfence's advisory includes an analysis of the code, and neither names who is behind it.

Deleting suspicious files before stopping what recreates the backdoor may not resolve the problem, which is why the cleanup order below matters. The attacker may also have left PHP backdoor files in other plugins' folders, in theme folders, and in the must-use plugins directory, created administrator accounts, added a fake WordPress core file, changed .htaccess so that .cache files run as PHP, and added scheduled tasks and SSH keys.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Any password, database credential, API key, or other secret the site could reach may have been exposed, and owners should assume it was.

Wordfence assigned the incident CVE-2026-111862 and rates it 9.8 out of 10, with the researcher listed as unknown.

[Patchstack](https://patchstack.com/database/wordpress/plugin/seo-by-rank-math-pro/vulnerability/wordpress-rank-math-seo-pro-plugin-3-0-123-unauthenticated-embedded-malicious-code-vulnerability) classifies it as a backdoor and says that, because the attack was on Rank Math's own systems, "a rule is not possible for mitigation."

### How to Recover

Rank Math's preferred recovery is a restore. Where a backup of the site and its database from before 20:02 UTC on October 15 exists, restore it, run a security scan, change every password and credential, and only then install 3.0.124 from your Rank Math account.

Where no clean backup exists, the manual cleanup runs in a fixed order, and three actions come before anything else is touched:

1. Delete the entire rank-math-pro plugin folder using the hosting file manager or FTP. "Deactivating the plugin alone is not sufficient," the notice says.
2. In the wp\_options table, delete any entry whose option\_name is \_uf6qdn2hmm, t8krdk990phb or \_np5pvf754c.
3. Block outgoing connections to rank1cdn[.]com if the hosting provider or firewall allows it.

Only then does the search for other changes begin, in these places:

* **Files**: PHP files in wp-content/mu-plugins/, in other plugins' folders, in the inc/, includes/ and lib/ folders of non-default themes, in Rank Math's own includes/ folder, and in uploads/.
* **Code**: PHP that uses base64\_decode with XOR loops, the key xmmqhn, proc\_open, or PHP-FPM socket code.
* **File**: wp-includes/class-wp-cache-util.php, which is not a WordPress core file.
* **Accounts**: administrator usernames beginning wpsupport\_, or accounts with email addresses ending @wp-mail[.]net.
* **Server**: .htaccess rules that let .cache files run as PHP, .cache files containing PHP code, entries tagged #ms6v46 in the web server user's crontab, WordPress scheduled events, SSH authorized\_keys files, other users' crontabs, running processes, and any location outside the site where the web server can write.

Wordfence adds a caution: "Their absence does not, by itself, prove that a website is clean."

Credentials are changed in every case, even after a restore from backup. Th...