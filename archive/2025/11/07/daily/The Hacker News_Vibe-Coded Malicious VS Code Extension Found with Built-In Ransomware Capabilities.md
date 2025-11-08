---
title: Vibe-Coded Malicious VS Code Extension Found with Built-In Ransomware Capabilities
url: https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html
source: The Hacker News
date: 2025-11-07
fetch_date: 2025-11-08T03:06:25.798946
---

# Vibe-Coded Malicious VS Code Extension Found with Built-In Ransomware Capabilities

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Vibe-Coded Malicious VS Code Extension Found with Built-In Ransomware Capabilities](https://thehackernews.com/2025/11/vibe-coded-malicious-vs-code-extension.html)

**Nov 07, 2025**Ravie LakshmananSupply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Dcu9T1Afix71Yt-8QCNjFUC__8eCH-PwqBYQbkqtmzclCd1DmtyV89McDlT1wJxv4qRnRmxQiEFsnpzw1a0k3EMPCBIpxwJysacU-wUGg6-tCUrTKFlPVtrR3Yw4qO5Yk_trwmpT5AMqUgSkFJMEvMYJL522Wjn4FOYfFAzFaZUvZ9ufXSV82U7lUFA3/s790-rw-e365/vide-code-ransomware.jpg)

Cybersecurity researchers have flagged a malicious Visual Studio Code (VS Code) extension with basic ransomware capabilities that appears to be created with the help of artificial intelligence – in other words, vibe-coded.

Secure Annex researcher John Tuckner, who [flagged](https://secureannex.com/blog/ransomvibe/) the extension "[susvsex](https://marketplace.visualstudio.com/items?itemName=suspublisher18.susvsex)," said it does not attempt to hide its malicious functionality. The extension was uploaded on November 5, 2025, by a user named "suspublisher18" along with the description "Just testing" and the email address "donotsupport@example[.]com."

"Automatically zips, uploads, and encrypts files from C:\Users\Public\testing (Windows) or /tmp/testing (macOS) on first launch," reads the description of the extension. As of November 6, Microsoft has stepped in to [remove](https://github.com/microsoft/vsmarketplace/blob/main/RemovedPackages.md) it from the official VS Code Extension Marketplace.

According to details shared by "suspublisher18," the extension is designed to automatically activate itself on any event, including installing or when launching VS Code, and invoke a function named "zipUploadAndEncrypt," which creates a ZIP archive of a target directory, exfiltrates it to a remote server, and replaces the files with their encrypted versions.

"Fortunately, the TARGET\_DIRECTORY is configured to be a test staging directory so it would have little impact right now, but is easily updated with an extension release or as a command sent through the C2 channel covered next," Tuckner said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Besides encryption, the malicious extension also uses GitHub as command-and-control (C2) by polling a private GitHub repository for any new commands to be executed by parsing the "index.html" file. The results of the command execution are written back to the same repository in the "requirements.txt" file using a GitHub access token embedded in the code.

The GitHub account associated with the [repository](https://github.com/aykhanmv/susvsex) – aykhanmv – continues to be active, with the developer claiming to be from the city of Baku, Azerbaijan.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHiY7gD7tf_etOKXW4CeXHEg2wzaQxLUBmffgXPFOvLarqr6yXTQTS8aWh-oBLFtlTjKq17VANjmQxIU8-I5-bJ4uno3mJRyBBty6ZTm4EaDJrHs1SSJ1b-iN45UvqabW-FRS2aBDR59gH4CGMhHtqdnrdQL74eX0ES_96Sb5sZ6E2vesuikG75jcZhkrv/s790-rw-e365/bot.png)

"Extraneous comments which detail functionality, README files with execution instructions, and placeholder variables are clear signs of 'vibe-coded' malware," Tuckner said. "The extension package accidentally included decryption tools, command and control server code, GitHub access keys to the C2 server, which other people could use to take over the C2."

### Trojanized npm Packages Drop Vidar Infostealer

The disclosure comes as Datadog Security Labs [unearthed](https://securitylabs.datadoghq.com/articles/mut-4831-trojanized-npm-packages-vidar/#initial-discovery) 17 npm packages that masquerade as benign software development kits (SDKs) and provide the advertised functionality, but are engineered to stealthily execute [Vidar Stealer](https://thehackernews.com/2025/05/hackers-use-tiktok-videos-to-distribute.html) on infected systems. The development marks the first time the information stealer has been distributed via the npm registry.

The cybersecurity company, which is tracking the cluster under the name MUT-4831, said some of the packages were first flagged on October 21, 2025, with subsequent uploads recorded the next day and on October 26. The names of the packages, published by accounts called "aartje" and "saliii229911," are below -

* abeya-tg-api
* bael-god-admin
* bael-god-api
* bael-god-thanks
* botty-fork-baby
* cursor-ai-fork
* cursor-app-fork
* custom-telegram-bot-api
* custom-tg-bot-plan
* icon-react-fork
* react-icon-pkg
* sabaoa-tg-api
* sabay-tg-api
* sai-tg-api
* salli-tg-api
* telegram-bot-start
* telegram-bot-starter

While the two accounts have since been banned, the libraries were downloaded at least 2,240 times prior to them being taken down. That said, Datadog noted that many of these downloads could likely have been the result of automated scrapers.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

The attack chain in itself is fairly straightforward, kicking in as part of a postinstall script specified in the "package.json" file that downloads a ZIP archive from an external server ("bullethost[.]cloud domain") and execute the Vidar executable contained within the ZIP file. The Vidar 2.0 samples have been found to use hard-coded Telegram and Steam accounts as dead drop resolvers to fetch the actual C2 server.

In some variants, a post-install PowerShell script, embedded directly in the package.json file, is used to download the ZIP archive, after which the execution control is passed to a JavaScript file to complete the rest of the steps in the attack.

'

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgz0o2KuIV7Nza_7d4Wy1mKQYjnEXqJfZ2x9sq9EcaRgUMSvqiqlMMBSPRdCfOcd2zVpCyUGowHaX2aiqN9CLVIXMT74QBoMiFCmskDOnEX0kVMfoFJ1LO2pXjgBiOio_S5PRvfE5_0NkWOg3kf2lU1SzLw786i0JVQBn5LW1OqQYdJ6UNBi2ohd_N1WRmr/s790-rw-e365/telegram.png)

"It is not clear why MUT-4831 chose to vary the post...