---
title: Over 70 Malicious npm and VS Code Packages Found Stealing Data and Crypto
url: https://thehackernews.com/2025/05/over-70-malicious-npm-and-vs-code.html
source: The Hacker News
date: 2025-05-27
fetch_date: 2025-10-06T22:34:40.800005
---

# Over 70 Malicious npm and VS Code Packages Found Stealing Data and Crypto

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

# [Over 70 Malicious npm and VS Code Packages Found Stealing Data and Crypto](https://thehackernews.com/2025/05/over-70-malicious-npm-and-vs-code.html)

**May 26, 2025**Ravie LakshmananCybersecurity / Cryptocurrency

[![Malicious npm and VS Code Packages](data:image/png;base64... "Malicious npm and VS Code Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_KfU2a7iGQ4XFQ_4LvOsA7eYxbFf-AXsilkSYBnefv1_GP4-T9cd8XgIAEJrVUl6zDxmO306lnZsDhJijcj1EqugMFslFIGvBfBHuX_BtNZu2rPg-S6Yvdyw7Xj66_23eYeUgNdgsB36Ofc7dbiQwTsAwrMhp1P_WbDMtUOHe-f65ARh8L_qTz-bvLKSh/s790-rw-e365/vscode-npm.jpg)

As many as 60 malicious npm packages have been discovered in the package registry with malicious functionality to harvest hostnames, IP addresses, DNS servers, and user directories to a Discord-controlled endpoint.

The packages, published under three different accounts, come with an install‑time script that's triggered during npm install, Socket security researcher Kirill Boychenko said in a report published last week. The libraries have been collectively downloaded over 3,000 times.

"The script targets Windows, macOS, or Linux systems, and includes basic sandbox‑evasion checks, making every infected workstation or continuous‑integration node a potential source of valuable reconnaissance," the software supply chain security firm [said](https://socket.dev/blog/60-malicious-npm-packages-leak-network-and-host-data).

The names of the three accounts, each of which published 20 packages within an 11-day time period, are listed below. The accounts no longer exist on npm -

* bbbb335656
* cdsfdfafd1232436437, and
* sdsds656565

The malicious code, per Socket, is explicitly designed to fingerprint every machine that installs the package, while also aborting the execution if it detects that it's running in a virtualized environment associated with Amazon, Google, and others.

The harvested information, which includes host details, system DNS servers, network interface card (NIC) information, and internal and external IP addresses, is then transmitted to a Discord webhook.

"By harvesting internal and external IP addresses, DNS servers, usernames, and project paths, it enables a threat actor to chart the network and identify high‑value targets for future campaigns," Boychenko said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The disclosure follows another set of eight npm packages that masquerade as helper libraries for widely-used JavaScript frameworks including React, Vue.js, Vite, Node.js, and the open-source Quill Editor, but deploy destructive payloads once installed. They have been downloaded more than 6,200 times and are still available for download from the repository -

* vite-plugin-vue-extend
* quill-image-downloader
* js-hood
* js-bomb
* vue-plugin-bomb
* vite-plugin-bomb
* vite-plugin-bomb-extend, and
* vite-plugin-react-extend

"Masquerading as legitimate plugins and utilities while secretly containing destructive payloads designed to corrupt data, delete critical files, and crash systems, these packages remained undetected," Socket security researcher Kush Pandya [said](https://socket.dev/blog/malicious-npm-packages-target-react-vue-and-vite-ecosystems-with-destructive-payloads).

Some of the identified packages have been found to execute automatically once developers invoke them in their projects, enabling recursive deletion of files related to Vue.js, React, and Vite. Others are designed to either corrupt fundamental JavaScript methods or tamper with browser storage mechanisms like localStorage, sessionStorage, and cookies.

[![Malicious npm and VS Code Packages](data:image/png;base64... "Malicious npm and VS Code Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyFWKUo_jVBPdwxcsEKqqTZQ_CFCe2o7TTQrxl278Z-AhPZB8DwZqrs6qyENZ1jMhSd-WyV_G9S06H16NENmfjC7SE-h6UF_OuuhlP-Pkz76DJNQcYOt2DJ7ZntE6iLFI_zhBlq9laeXBvWcDVyrxIwyZNdmKVnneZpdhGyVJ50_FD0DPMmJDo5L3zdTVR/s790-rw-e365/npm-code.jpg)

Another package of note is js-bomb, which goes beyond deleting Vue.js framework files by also initiating a system shutdown based on the current time of the execution.

The activity has been traced to a threat actor named [xuxingfeng](https://www.npmjs.com/~xuxingfeng), who has also published five legitimate, non-malicious packages that work as intended. Some of the rogue packages were published in 2023. "This dual approach of releasing both harmful and helpful packages creates a facade of legitimacy that makes malicious packages more likely to be trusted and installed," Pandya said.

The findings also follow the discovery of a novel attack campaign that combines traditional email phishing with JavaScript code that's part of a malicious npm package disguised as a benign open-source library.

"Once communication was established, the package loaded and delivered a second-stage script that customized phishing links using the victim's email address, leading them to a fake Office 365 login page designed to steal their credentials," Fortra researcher Israel Cerda [said](https://www.fortra.com/blog/threat-analysis-malicious-npm-package-leveraged-o365-phishing-attack).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The starting point of the attack is a phishing email containing a malicious .HTM file, which includes encrypted JavaScript code hosted on [jsDelivr](https://thehackernews.com/2023/08/malicious-npm-packages-found.html) and associated with a now-removed npm package named [citiycar8](https://www.npmjs.com/package/citiycar8?activeTab=versions). Once installed, the JavaScript payload embedded within the package is used to initiate a URL redirection chain that eventually leads the user to a bogus landing page designed to capture their credentials.

"This phishing attack demonstrates a high level of sophistication, with threat actors linking technologies such as AES encryption, npm packages delivered through a CDN, and multiple redirections to...