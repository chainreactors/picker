---
title: 18 Malicious npm Packages Deliver Cross-Platform RAT to Alibaba Tool Users
url: https://thehackernews.com/2026/08/18-malicious-npm-packages-deliver-cross.html
source: The Hacker News
date: 2026-08-03
fetch_date: 2026-08-04T05:01:11.639545
---

# 18 Malicious npm Packages Deliver Cross-Platform RAT to Alibaba Tool Users

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

![cybersecurity](data:image/svg+xml;base64...)

# [18 Malicious npm Packages Deliver Cross-Platform RAT to Alibaba Tool Users](https://thehackernews.com/2026/08/18-malicious-npm-packages-deliver-cross.html)

**Ravie Lakshmanan**Aug 03, 2026Malware / Software Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhb0HLXOvc5Gir8E_IXoYIRMQG7CsNL7gJEkPytfRRQ67OWrIoyrGAX78K0Ca0VJ7hhpyru2Vck7ntHKLyBLhGezuyOD_znWoB88KhAdEWu8MyhVbiEia2GfbRVeDPhaCEAHfhY637LqeIyso03edEkOGL3p0c3O6_Nn7oJ6rNmyve-6_pqziBCokfiKoKI/s1700-e365/npm-git.jpg)

Cybersecurity researchers have discovered a new set of malicious npm packages that target users of Alibaba developer tools with a cross-platform remote access trojan (RAT) as part of a sophisticated, targeted software supply chain attack targeting Chinese-speaking environments.

One of the packages in question is "[lib-mtop](https://g.alicdn.com/x-bridge/mqn/book/api/api-mtop.html)," an unscoped package with the same name as a private Alibaba package under the "@ali" scope. Although the npm package was [first published](https://secure.software/npm/packages/lib-mtop/versions) sometime in November 2023 with no functionality, three new versions (v1.0.1, v1.0.2, and v1.0.3) were uploaded earlier this March and April.

It's currently not clear if this was the result of a maintainer account takeover or the project developer opting to go rogue. Regardless of how the malicious changes were pushed, the newly added changes feature a loader that's designed to fetch a remote JavaScript payload using curl and then execute it.

The same maintainer account "[ch4ce](https://www.npmjs.com/~ch4ce)," which currently redirects to a "not found" error on npmjs[.]com, has also published four other packages: aone-kit, aone-kit-cli, aone-sandbox, and local-config-parser.

"The first three are empty wrappers that have the same name as private, @ali-scoped packages which they declare as a dependency in the package.json file," Socket security researcher Karlo Zanki [said](https://socket.dev/blog/npm-rat-targets-alibaba) in an analysis.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The last package, local-config-parser, implements a legitimate JSON configuration file parser, but features dependencies that, on their own, are innocuous and are published from other npm user accounts. When combined together, they serve as a conduit for an advanced RAT targeting developers who are likely working in companies that are part of the Alibaba Group.

Specifically, the malicious loader functionality is split and embedded into several packages delivered to the targets as part of the same dependency tree. The top-layer packages, which impersonate private packages from the @ali scope, serve as decoys that activate the installation of the dependency tree.

"When such a package is installed in an environment that has access to impersonated, scoped private packages, the dependency resolution works as expected, with a little extra functionality delivered through additional dependencies that get installed," Socket explained.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgs6divl9iNhX21A3Ne6ImrIFLcW-DQycKbOx_eu3IKUyELTrwLfDw_bXYziLcRl00TDrMeboduRLWPZybX4NGudVwLeNaRkDVxw3PK2mVvlRojloMopCZBCSQRx5bUqH4f0zzzVnNH_K9paUKgOMYYSgF89ZzTws6-qDdr4xrusztpet8_fuQ5HPqkIPrC/s1700-e365/npm.png)

As many as 10 top-layer lure packages have been found to depend on "smart-config-manager," which functions akin to a middle-layer bridge that connects them to the malicious packages containing the loader logic. One of the low-layer packages proceeds to contact a GitHub repository to retrieve and store a rule engine configuration, and then it uses it to execute a malicious payload that then contacts a remote server to fetch secondary malware.

What's notable about the attack is that the rule engine makes use of the vm module to implement the final phase and perform the payload download depending on the victim's operating system. The payload is retrieved from a domain that masquerades as Alibaba ("aone-cli-next.oss-cn-beijing.aliyuncs[.]com") to blend in and sidestep detection.

This stage performs a number of actions -

* On Windows, it terminates the Alilang enterprise security, VPN, and office productivity app and replaces its core code with a trojanized version.
* On Linux, it downloads a binary payload to /tmp, runs it as a detached process, and deletes the file from disk after it's loaded into memory.
* On macOS, it inserts a malicious background script into ~/.zshrc and sets up a 10-minute Launch Agent.

The final payload is a complex backdoor equipped with comprehensive command execution, arbitrary file upload and download, host reconnaissance, payload staging, and lateral movement capabilities. It also has the capacity to persist by injecting malicious code into common enterprise collaboration applications like DingTalk, Wukong, and Qoder.

Exactly who is behind the campaign is unknown, but the presence of Chinese language comments in the source code, combined with the fact that GitHub commits are timestamped with the UTC+08:00 offset, indicates that it's possibly the work of a Chinese-speaking threat actor going after Chinese-speaking developers using tools belonging to Alibaba Group.

"The goal of the campaign seems to be industrial espionage," Zanki noted. "While the number of downloads for the malicious packages is not significant, the impact of the campaign is hard to evaluate, because of the targeted nature and lateral-spread capabilities of the final-stage payload."

The complete set of packages associated with the campaign is below -

* lib-mtop
* aone-kit
* aone-kit-cli
* aone-sandbox
* local-config-parser
* smart-config-manager
* cloud-config-fetcher
* fast-transform-pipeline
* aone-cloud-cli
* colder-cli
* def-open-client
* feedback-ai-sdk
* flight-compare-analyzer
* lwp-web-client
* lzd-unified-station-sdk
* open-worker-cli
* test-skill-zip
* uniapi-bridge

Users who have installed any of the above packages should assume compromise, rotate sensitive credentials from a clean machine, and audit developer systems for signs of suspicious activity.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The dis...