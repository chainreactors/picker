---
title: Hackers Backdoor Nextcloud Servers Through Critical Flaw in Collabora’s Built-in CODE App
url: https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html
source: The Hacker News
date: 2026-10-14
fetch_date: 2026-10-15T06:45:38.516015
---

# Hackers Backdoor Nextcloud Servers Through Critical Flaw in Collabora’s Built-in CODE App

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

# [Hackers Backdoor Nextcloud Servers Through Critical Flaw in Collabora’s Built-in CODE App](https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html)

**Swati Khandelwal**Oct 14, 2026Vulnerability / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkZLcjmZtzt6NpWa8x4Wz7EdcOQEW6xYv6DA_mBnwy1ctZZeRAyeSYLES-H_mkr1QOBv72WNuGKwKQ-NN179Rw8BRTcYO38sYwxcbDkg1ISW_qWrCRJ9JfUXh3102OmwrF0HQq6dbSc58VXACXoi_EoI8ysPuSlzB_nBcHuFl9r3QakOsGG9GUm6UVOU8/s1700-nu-rw-lo-l85-e365/nextcloud.jpg)

Attackers exploited a flaw in an optional Nextcloud app, [Collabora Online - Built-in CODE Server](https://apps.nextcloud.com/apps/richdocumentscode), to plant web shells on Nextcloud servers. Three administrators [reported the issue on GitHub](https://github.com/CollaboraOnline/richdocumentscode/issues/354), with the first logged attack on September 10.

A web shell is a small file that executes any command an attacker sends via a web request, with the rights of the web server account. The flaw allows an unauthenticated request to run a command on the server, but only when the app's local document server is not running, such as during a restart or upgrade, or after a crash.

Collabora fixed it in [version 26.4.303](https://github.com/CollaboraOnline/richdocumentscode/releases/tag/26.4.303) on September 11 and on October 14 published [an advisory](https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh) with the identifier [CVE-2026-110447](https://www.cve.org/CVERecord?id=CVE-2026-110447), warning that turning off the app does not help: it must be updated or removed.

### Who Is Affected

The app, published by Collabora under the package name richdocumentscode, downloads a copy of Collabora Online Development Edition (CODE) and runs it on the Nextcloud server itself.

That lets Nextcloud Office edit documents without a separate Collabora server. Its store listing says it is "for local testing and non-production use" and "for personal use or for small teams."

Collabora's advisory covers every version before 26.4.303 and says standalone Collabora Online servers are not affected. A [warning posted on the Nextcloud community forum](https://help.nextcloud.com/t/to-collabora-built-in-user-update-asap/250516) on October 3 stated that an installation is not affected if it uses only the Nextcloud Office app ( richdocuments) without the built-in app, whether its Collabora server runs in Docker, from a Linux package, or at a hosting provider.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The app's proxy.php script starts the local CODE server whenever a request arrives, and nothing is listening. In versions up to 26.4.302, the script placed text from the request, including its path, inside a double-quoted bash command, where the shell still runs anything written as $(...).

A request with a command hidden in its path ran that command as the web server user. Because the script only builds that command when it needs to start the server, the attack works only while the server is down, such as during a container restart, an upgrade, or a crash.

The script is a plain PHP file that the web server runs directly from the app's folder and loads none of Nextcloud's code.

"It is not sufficient to disable the app to avoid the problem; it must be upgraded to >= 26.4.303 or removed," Collabora said in the advisory.

The fixed versions [require Nextcloud 30 or later](https://apps.nextcloud.com/apps/richdocumentscode/releases?platform=26).

Nextcloud 29 and older are end of life, and the app store still serves them an affected version, so their users should upgrade Nextcloud or remove the app. Collabora's fix for a separate command-injection flaw in the same script, [CVE-2025-66208](https://github.com/CollaboraOnline/online/security/advisories/GHSA-j3q6-q5pc-v5wf), disclosed last December, does not prevent this one.

### What the Attackers Did

The first report came from an administrator who hosts several Nextcloud servers and wrote on GitHub that the servers had been hacked since the day before. Access logs from two of them show requests at 19:51 on September 10 and 09:56 on September 11 (UTC+2), both from one IP address and both aimed at proxy.php?status with a shell command hidden in the request path. All of the administrator's servers ran version 26.4.302.

The command decoded a one-line PHP web shell into the app's folder and tried to send the server's uname -a output to a webhook.site address. On one server, the attacker then used the shell to search for credential stores and cryptocurrency wallets, including \*.kdbx, wallet.dat and keystore.json files and names such as bitwarden, 1password, .bitcoin, .electrum, .monero and .ethereum.

The reviewed requests showed no commands that archived, uploaded, or copied out files, but anything the web server account can read must be treated as potentially exposed, the administrator wrote.

Two other administrators reported the same on their own instances. One found the shell when Nextcloud's integrity check flagged a new PHP file, and the other learned of the break-in from emails about failed sudo attempts on the server. None of the reports show the attacker gaining root access.

After updating to 26.4.303, one of them logged another attempt on September 14 from a second IP address with a payload of the same kind. The CODE server it started carried the attack text in its startup options, but no new shell file appeared. The output "looks scary but should be harmless," replied mmeeks, who answered for the project in the thread, telling users to update and to remove any leftover shx\*.php files.

The CVE record describes the flaw as "exploited in the wild in September and October 2026." How many servers were hit is not known. "This impacts only the Development Edition, and only in this (rather rarer) Built-in CODE Server deployment...