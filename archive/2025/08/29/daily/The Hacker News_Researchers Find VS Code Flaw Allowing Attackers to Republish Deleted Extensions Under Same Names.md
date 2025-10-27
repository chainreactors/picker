---
title: Researchers Find VS Code Flaw Allowing Attackers to Republish Deleted Extensions Under Same Names
url: https://thehackernews.com/2025/08/researchers-find-vs-code-flaw-allowing.html
source: The Hacker News
date: 2025-08-29
fetch_date: 2025-10-07T00:49:25.450955
---

# Researchers Find VS Code Flaw Allowing Attackers to Republish Deleted Extensions Under Same Names

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

# [Researchers Find VS Code Flaw Allowing Attackers to Republish Deleted Extensions Under Same Names](https://thehackernews.com/2025/08/researchers-find-vs-code-flaw-allowing.html)

**Aug 28, 2025**Ravie LakshmananMalware / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8Y9u9GKMsRB1GGJ2J6rfmmG3DVAbnxFf3wKnogYQtMl-S9FYeW0CxV7aFi_IZt_BxrghtuVoKnNG5i9JaOBtrb5TBnxQ6AnrMzoybR14km-s46-1L1YUPoSATfuUrEUAR3RFjI115Z5KM2JWc1SePkyzNwwrRz3-5eecK0FuK6SvzrMOS_lIGx_vWtHWF/s790-rw-e365/vscode.jpg)

Cybersecurity researchers have discovered a loophole in the Visual Studio Code Marketplace that allows threat actors to reuse names of previously removed extensions.

Software supply chain security outfit ReversingLabs [said](https://www.reversinglabs.com/blog/malware-vs-code-extension-names) it made the discovery after it identified a malicious extension named "ahbanC.shiba" that functioned similarly to two other extensions – ahban.shiba and ahban.cychelloworld – that were [flagged](https://thehackernews.com/2025/03/vscode-marketplace-removes-two.html) earlier this March.

All three libraries are designed to act as a downloader to retrieve a PowerShell payload from an external server that encrypts files in a folder called "testShiba" on the victim's Windows desktop and demands a Shiba Inu token by instructing the victim to deposit the assets to an unspecified wallet. These efforts suggest ongoing development attempts by the threat actor.

The company said it decided to dig deeper because of the fact that the name of the new extension ("ahbanC.shiba") was virtually the same as one of the two others previously identified ("ahban.shiba").

It's worth noting that each extension has to have a unique ID that's a combination of the publisher name and the name of the extension (i.e., <publisher>.<name>). In the case investigated by ReversingLabs, both extensions are differentiated only by the name of the publisher, while the actual name of the extension remains the same.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

However, [according](https://code.visualstudio.com/api/references/extension-manifest) to Visual Studio Code documentation, the <name> field specified in the extension manifest "should be all lowercase with no spaces" and "must be unique to the Marketplace."

"So how did extensions ahban.shiba and ahbanC.shiba end up having the same name despite the official documentation's publishing rules?," asked security researcher Lucija Valentić, who ultimately found that it is possible to do so once the extension is removed from the repository. But this behavior doesn't apply to scenarios where an author unpublishes an extension.

It's worth noting that the ability to reuse the name of deleted libraries also applies to the Python Package Index (PyPI) repository, as [demonstrated](https://www.reversinglabs.com/blog/package-names-repurposed-to-push-malware-on-pypi) by ReversingLabs in early 2023.

At the time, it was found that deleting a package would make its project name "available to any other PyPI user" as long as the distribution file names (a combination of the project name, version number, and distribution type) are different from those used in the now-removed distribution.

However, PyPI carves out an exception where PyPI package names can be made unavailable if they were first used by malicious packages. It appears that Visual Studio Code does not have a similar restriction to prevent the reuse of names of malicious extensions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjz7atyHngMW1qqb37zj5V8RxlwUTU9o7aFTu7zWSGzBDsE83R0Xx4wxciWyACsNSFDqH1DvKODc6fj-PBKp2jOS6mutiJlU7kgMiaBOLuevoXlLcOY1wPUY71rpiVu3YVw8j7hs5yeCATCEURJQ2Q4OK7xhRO1dwSNS0BDdEdb1EXaije4O44qFPSUH36G/s790-rw-e365/codede.jpg)

The development, as [observed](https://socket.dev/blog/black-basta-dependency-confusion-ambitions-and-ransomware-in-open-source-ecosystems) in [leaked Black Basta chat logs](https://thehackernews.com/2025/06/former-black-basta-members-use.html), shows how threat actors are looking at poisoning open-source registries with ransomware libraries that demand ransoms from unsuspecting victims who may install them. This makes it all the more crucial for organizations and developers to adopt secure development practices and proactively monitor these ecosystems for software supply chain threats.

"The discovery of this loophole exposes a new threat: that the name of any removed extension can be reused, and by anyone," Valentić said. "That means that if some legitimate and very popular extension is removed, its name is up for grabs."

The findings also follow the [identification](https://jfrog.com/blog/malicious-npm-packages-chrome-browser-information-stealer/) of eight malicious npm packages that have been found to deliver a Google Chrome browser information stealer targeting Windows systems that's capable of transmitting passwords, credit cards, cryptocurrency wallet data, and user cookies to a railway[.]app URL or a Discord webhook as a fallback mechanism.

The packages, published by users named ruer and npjun, are listed below -

* toolkdvv (versions 1.1.0, 1.0.0)
* react-sxt (version 2.4.1)
* react-typex (version 0.1.0)
* react-typexs (version 0.1.0)
* react-sdk-solana (version 2.4.1)
* react-native-control (version 2.4.1)
* revshare-sdk-api (version 2.4.1)
* revshare-sdk-apii (version 2.4.1)

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

What's notable about these packages is the use of 70 layers of obfuscated code to unpack a Python payload that's engineered to facilitate data theft and exfiltration.

"Open-source software repositories have become one of the main entry points for attackers as part of supply chain attacks, with growing waves using typosquatting and masquerading, pretending to be legitimate," JFrog security researcher Guy Korolevski said.

"The impact of sop...