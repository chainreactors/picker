---
title: Malicious npm Package Poses as Twilio Bug-Bounty Probe, Can Exfiltrate Credentials
url: https://thehackernews.com/2026/09/malicious-npm-package-poses-as-twilio.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:52.604283
---

# Malicious npm Package Poses as Twilio Bug-Bounty Probe, Can Exfiltrate Credentials

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

# [Malicious npm Package Poses as Twilio Bug-Bounty Probe, Can Exfiltrate Credentials](https://thehackernews.com/2026/09/malicious-npm-package-poses-as-twilio.html)

**Ravie Lakshmanan**Sep 22, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikMlDL6W0FZvq8_gscr2M3UZIVnCYorB-Ip2G6To6-eZ04gFyOMsf-mvbqtMkYv484O3XnKhzySe0-UQjCOMm99fUhzrpkMD-QaZkn2UIUozJ5hLwrm7kXgLkODdkUUJk4GFXEkgrg7MlXKzcQ7kKtug2RmT80RROQfVRbQQm3HdeHBzAzhAjQ9bUf5eaT/s1700-nu-rw-lo-l85-e365/twilio.jpg)

Cybersecurity researchers have [disclosed](https://www.reversinglabs.com/blog/malicious-npm-campaign-twilio) details of a malicious npm package named "tw-pkgprobe-7731" that masquerades as a security tool targeting developers integrating Twilio into their applications, while stealthily attempting to harvest sensitive data.

The package, named "tw-pkgprobe-7731," was first uploaded to the npm registry in mid-August 2026 by an npm account named "twdepprobe7731." In total, [11 versions of the package](https://secure.software/npm/packages/tw-pkgprobe-7731/versions) were published in quick succession on the same day over an approximately 45-minute time period. The npm user account no longer exists as of writing.

"The first version of tw-pkgprobe-7731 posed as an authorized security research probe," ReversingLabs researcher Lucija Valentić said in a report published today.

"Comments inside the package describe it as an 'Authorized bug-bounty research probe (Twilio HackerOne program)' that 'runs only inside Twilio's serverless packager sandbox' and 'collects local process/host context and writes it next to itself; no destructive action.'"

Upon execution, the package first checks if the current environment is a Twilio developer environment. It immediately exits if that's not the case.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Should the check pass, the malware proceeds to extract environment variables along with system details like mounts, temporary folders, and various configurations. The gathered information is then exfiltrated via a webhook.

Subsequent versions of the npm package (viz., versions 1.0.1, 1.0.2, and 1.0.3) have been found to focus on developers using Twilio APIs, specifically searching for folders tied to specific Twilio account String Identifiers (SIDs). Most importantly, it avoids taking any action if there exists a folder with a specific SID name.

"Otherwise, if matching target folders were found, it scanned installed npm packages and node\_modules to inject a custom npm PoC package, creating package.json and index.js inside," ReversingLabs explained.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoV53Z4541pF-FWSJAV40cDp1G_pS8FGRsGMVKxiuFUG51UitUvSV8Jfr42BjQPHqwvNV_O77BRktlkLMs0zirkedG2sUYHyNVtrcXDKaZsMlljVlj_w5uX093zl5TS_l37aBhdNZpey6-joXupeLDh4KNxa-0ptiRGZ-SY0KKxiWR34A2d0fRaZN5_Ekq/s1700-nu-rw-lo-l85-e365/code-npm.jpg)

Version 1.0.4 is said to have introduced an added capability to exfiltrate [process.env.ACCOUNT\_SID and process.env.AUTH\_TOKEN](https://www.twilio.com/docs/usage/anti-fraud-developer-guide#account-level-protection), effectively compromising the victim's Twilio credentials and potentially allowing the threat actor to authorize billing and trigger communication.

However, the final three versions (i.e., 1.0.8, 1.1.0, and 1.1.1) "reverted to the basic probing profile of the package seen in version 1.0.0," dropping the malicious functionality incorporated in prior iterations.

In addition, the last two versions have been found to conduct OSINT gathering by probing various Twilio-related hosts, such as support-api.us1.twilio[.]com, kafka-ui.au1.twilio[.]com and litellm.ai-services.corp.twilio[.]com, even fetching AWS metadata located at "169.254.169[.]254/latest/meta-data/."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

Given these unusual course reversals, it's unclear what the end goals are and if it was published as part of a bug bounty program. However, ReversingLabs said the package versions did not follow [Twilio's bug hunting guidelines](https://hackerone.com/twilio?type=team) listed on HackerOne.

"In other words, these packages clearly violate the basic security research guidelines Twilio established, which suggests that the packages had malicious intent," Valentić said. "While the threat actor behind the campaign attempted to mask malicious features in certain releases by surrounding them with seemingly benign features and code, they made no real effort to obscure the malicious code or hide their activity.

"There is no obfuscation, typosquatting, or attempt to make the publishing npm account look legitimate – tactics we’ve routinely seen in previous campaigns. This suggests that a less sophisticated threat actor is responsible for the malicious campaign targeting Twilio developers."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Developer Security](https://thehackernews.com/search/label/D...