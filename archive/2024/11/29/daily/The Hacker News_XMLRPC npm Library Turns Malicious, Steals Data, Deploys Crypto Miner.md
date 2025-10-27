---
title: XMLRPC npm Library Turns Malicious, Steals Data, Deploys Crypto Miner
url: https://thehackernews.com/2024/11/xmlrpc-npm-library-turns-malicious.html
source: The Hacker News
date: 2024-11-29
fetch_date: 2025-10-06T19:19:58.254515
---

# XMLRPC npm Library Turns Malicious, Steals Data, Deploys Crypto Miner

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [XML-RPC npm Library Turns Malicious, Steals Data, Deploys Crypto Miner](https://thehackernews.com/2024/11/xmlrpc-npm-library-turns-malicious.html)

**Nov 28, 2024**Ravie LakshmananSoftware Security / Data Breach

[![npm Library](data:image/png;base64... "npm Library")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgazBLQRVDnI_M15Ojsym2zwzxW84l7OUzCX2Xxs1un10J_YMIq7ei7etcSZ9cyu9Mle78BUSf0k9bmTHZo6QOrEmZA9UOUeGvWHyvourzTZ-4c4wNxmesiszozQP5782Tcwl5SHRzwxtyZ5-zduSlUMzcBOiwe47sM8jHf7biLwUV9V8SIQUV_DCzv0_vs/s790-rw-e365/pipy.png)

Cybersecurity researchers have discovered a software supply chain attack that has remained active for over a year on the npm package registry by starting off as an innocuous library and later adding malicious code to steal sensitive data and mine cryptocurrency on infected systems.

The package, named [@0xengine/xmlrpc](https://www.npmjs.com/package/%400xengine/xmlrpc), was originally published on October 2, 2023 as a JavaScript-based XML-RPC server and client for Node.js. It has been downloaded 1,790 times to date and remains available for download from the repository.

**Checkmarx**, which discovered the package, said the malicious code was strategically introduced in version 1.3.4 a day later, harboring functionality to harvest valuable information such as SSH keys, bash history, system metadata, and environment variables every 12 hours, and exfiltrate it via services like Dropbox and file.io.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The attack achieved distribution through multiple vectors: direct npm installation and as a hidden dependency in a legitimate-looking repository," security researcher Yehuda Gelb [said](https://checkmarx.com/blog/dozens-of-machines-infected-year-long-npm-supply-chain-attack-combines-crypto-mining-and-data-theft/) in a technical report published this week.

The second approach involves a GitHub project repository named [yawpp](https://github.com/hpc20235/yawpp) (short for "Yet Another WordPress Poster") that purports to be a tool designed to programmatically create posts on the WordPress platform.

Its "package.json" file [lists](https://github.com/hpc20235/yawpp/blob/master/package.json) the latest version of @0xengine/xmlrpc as a dependency, thereby causing the malicious npm package to be automatically downloaded and installed when users attempt to set up the yawpp tool on their systems.

It's currently not clear if the developer of the tool deliberately added this package as a dependency. The repository has been forked once as of writing. Needless to say, this approach is another effective malware distribution method as it exploits the trust users place in package dependencies.

Once installed, the malware is designed to collect system information, establish persistence on the host through systemd, and deploy the XMRig cryptocurrency miner. As many as 68 compromised systems have been found to actively mine cryptocurrency through the attacker's Monero wallet.

Furthermore, it's equipped to constantly monitor the list of running processes to check for the presence of commands like top, iostat, sar, glances, dstat, nmon, vmstat, and ps, and terminate all mining-related processes if found. It's also capable of suspending mining operations if user activity is detected.

"This discovery serves as a stark reminder that a package's longevity and consistent maintenance history do not guarantee its safety," Gelb said. "Whether initially malicious packages or legitimate ones becoming compromised through updates, the software supply chain requires constant vigilance – both during initial vetting and throughout a package's lifecycle."

The disclosure comes as **Datadog Security Labs** uncovered an ongoing malicious campaign targeting Windows users that uses counterfeit packages uploaded to both npm and the Python Package Index (PyPI) repositories with the end goal of deploying open-source stealer malware known as Blank-Grabber and Skuld Stealer.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The company, which detected the supply chain attack last month, is tracking the threat cluster under the name MUT-8694 (where MUT stands for "mysterious unattributed threat"), stating it overlaps with a campaign that was [documented](https://thehackernews.com/2024/11/malicious-npm-packages-target-roblox.html) by Socket earlier this month as aiming to infect Roblox users with the same malware.

As many as 18 and 39 phony unique packages have been uploaded to npm and PyPI, with the libraries attempting to pass off as legitimate packages through the use of typosquatting techniques.

"The use of numerous packages and involvement of several malicious users suggests MUT-8694 is persistent in their attempts to compromise developers," Datadog researchers [said](https://securitylabs.datadoghq.com/articles/mut-8964-an-npm-and-pypi-malicious-campaign-targeting-windows-users/). "Contrary to the PyPI ecosystem, most of the npm packages had references to Roblox, an online game creation platform, suggesting that the threat actor is targeting Roblox developers in particular."

### Update

The GitHub repository for the yawpp tool and its associated account are no longer accessible.

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
[![Fac...