---
title: Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed Bitcoin Wallets
url: https://thehackernews.com/2026/09/alby-hub-critical-flaw-could-let.html
source: The Hacker News
date: 2026-09-09
fetch_date: 2026-09-10T06:52:41.256052
---

# Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed Bitcoin Wallets

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

# [Alby Hub Critical Flaw Could Let Attackers Take Over Internet-Exposed Bitcoin Wallets](https://thehackernews.com/2026/09/alby-hub-critical-flaw-could-let.html)

**Swati Khandelwal**Sep 09, 2026Vulnerability / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfzwXsolZOaoU8mikO234FpoGAc_3wiI_OZ-Acpc-yPphzhUWmDh13CKiEG9xFbotf8RFEBh9jljS6pwUS4gryY-kk5UzPc7Mtb4Ds3mDpAhjyFoJibRDmnGXrLNt4VjGpTs1W5l6la2q4jO7D9hytPbAnLEFCHYVxxpcj7H-XNRDpGLfYSWAYqF7pl54/s1700-nu-rw-lo-l85-e365/alby-warning.jpg)

Bitcoin wallet company Alby has [warned of a critical flaw](https://x.com/getAlby/status/2097574956049498150) in Alby Hub that could have let an attacker take over a wallet and send its funds, but only where the owner had made the Hub reachable from the internet.

Alby Hub is a self-hosted Lightning wallet, meaning the owner runs it on their own computer or server, and it holds their bitcoin. The flaw affects versions v1.7.0 through v1.18.5, all released before August 2025, and Alby said one user has been affected so far.

Versions v1.19.0 and later do not have the flaw. The first release with that fix was published on August 29, 2025, so a Hub updated to any release published since then is not affected.

Alby is telling anyone still on an older build to stop outside access to the Hub's management interface first, which is the web page used to control the wallet. The next step is to update to [v1.24.0](https://github.com/getAlby/hub/releases), the current release.

The company has not said what the flaw is. It said it would publish full details later, in line with responsible disclosure practices, and thanked researchers who reported other issues that were fixed in the latest release.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Alby said that, to its knowledge, one user has been affected, and did not say whether that user lost money. It said the user reported the details to the company.

| Version | Status |
| --- | --- |
| `v1.7.0` to `v1.18.5` | Affected, where the Hub was reachable from the internet |
| `v1.19.0` and later | Not affected |
| `v1.24.0` | Current release. Alby recommends it even for people who are not affected |

### What to Do Now

1. Check the version your Hub is running.
2. If it is v1.18.5 or older, stop the Hub being reachable from outside your own network first. In a Docker setup, that means the port is published as 127.0.0.1:8080:8080 and not 8080:8080. On a cloud server, it means the firewall rule for port 8080 allows your own address rather than any address.
3. Update to v1.24.0.
4. If your Hub ran an affected version **and** was reachable from the internet, change your unlock password after the update and contact security@getalby.com.

Alby has not said whether updating alone ends any access an attacker already had to an exposed Hub. Its advice to change the unlock password applies to exactly that group, and no published source explains what the change is meant to undo.

### How a Hub Ends Up on the Internet

Alby Hub is built to sit on a private network. Its web interface requires a login, and [the project's own documentation](https://github.com/getalby/hub) now warns owners not to put it on the public internet because the server listens on every network connection the machine has, rather than only on the machine itself.

That warning is new. It arrived in a documentation [change merged on September 7](https://github.com/getAlby/hub/pull/2580), whose own description says several of the setup guides had described the server as "running on localhost when it actually listens on all network interfaces."

The same change switched the project's Docker file from publishing port 8080 to every address to publishing it only to the machine itself.

Before that, the guide for running Alby Hub on a Linux server said the Hub runs on localhost and recommended a reverse proxy for anyone who wanted to make it public. The README shipped with the oldest and the newest affected release did not carry that warning, and neither does the one in the current release.

As of September 9, the day of the warning, Alby's own guides for running a Hub on a cloud server still described a setup open to the internet.

Its [DigitalOcean guide](https://getalby.com/alby-hub/cloud/digitalocean) tells the reader to keep the server's public address switched on, because it is "needed so you can open Alby Hub in your browser," and then to open the Hub at that address.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

Its [Hetzner guide](https://getalby.com/alby-hub/cloud/hetzner) walks through creating a firewall rule for port 8080 with the source set to "Any IPv4 and Any IPv6, or your own IP address for better security," and its example Docker file publishes the port to every address.

### An Earlier Takeover on an Exposed Hub

This is not the first Alby Hub taken over after being left open. In November 2025, replying to a user whose Hub had been emptied, [Alby said](https://damus.io/nevent1qqsy66aynuese7y5f43aaqhvulz8g4297gl0v7tk7qcltfxjqtp22cgdwyee4) the machine was "reachable publicly on the clearnet, so it could be accessed from the outside."

By Alby's account, that was a different problem, not this flaw: the Hub's setup had never been finished, so no unlock password existed yet, and the attacker completed the setup themselves.

After that case, [a change to Umbrel's app](https://github.com/getumbrel/umbrel-apps/pull/4028) put Alby Hub behind Umbrel's own login, which had been switched off for it until then. Umbrel's app store now installs v1.24.0, and Alby's own Umbrel listing installs v1.21.4, both newer than the fixed version, though that describes what those stores install today rather than what any given Hub is running.

Two questions the warning leaves open matter to whole groups of users. It tells people to check the installed version, which does...