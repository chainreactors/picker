---
title: 10 npm Packages Caught Stealing Developer Credentials on Windows, macOS, and Linux
url: https://thehackernews.com/2025/10/10-npm-packages-caught-stealing.html
source: The Hacker News
date: 2025-10-29
fetch_date: 2025-10-30T03:12:55.492108
---

# 10 npm Packages Caught Stealing Developer Credentials on Windows, macOS, and Linux

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

# [10 npm Packages Caught Stealing Developer Credentials on Windows, macOS, and Linux](https://thehackernews.com/2025/10/10-npm-packages-caught-stealing.html)

**Oct 29, 2025**Ravie LakshmananMalware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUpZVfLPbWlZD8KMyaBn9nC53lUdBTLrXPQYMZoh4b9XiWsIyOlJYzRFzR4UTvcMBZFqSQE2H3f7GBoYIPiBxp2_jZgVYLyN11PnZ2pDY6l3DaNGeRV3mLW2oAglMTpCCgJlucrEGQVl1D9ZnrAuBDCimVIUqpdNu51wsyDaonpdBKJ4OW3VmwtCgJ3Psk/s790-rw-e365/npm-malware.jpg)

Cybersecurity researchers have discovered a set of 10 malicious npm packages that are designed to deliver an information stealer targeting Windows, Linux, and macOS systems.

"The malware uses four layers of obfuscation to hide its payload, displays a fake CAPTCHA to appear legitimate, fingerprints victims by IP address, and downloads a 24MB PyInstaller-packaged information stealer that harvests credentials from system keyrings, browsers, and authentication services across Windows, Linux, and macOS," Socket security researcher Kush Pandya [said](https://socket.dev/blog/10-npm-typosquatted-packages-deploy-credential-harvester).

The npm packages were uploaded to the registry on July 4, 2025, and accumulated over 9,900 downloads collectively -

* deezcord.js
* dezcord.js
* dizcordjs
* etherdjs
* ethesjs
* ethetsjs
* nodemonjs
* react-router-dom.js
* typescriptjs
* zustand.js

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The multi-stage credential theft operation manifested in the form of various typosquatted packages impersonating popular npm libraries such as TypeScript, discord.js, ethers.js, nodemon, react-router-dom, and zustand.

Once installed, the malware serves a fake CAPTCHA prompt and displays authentic-looking output that mimics legitimate package installations to give the impression that the setup process is proceeding along expected lines. However, in the background, the package captures the victim's IP address, sends it to an external server ("195.133.79[.]43"), and then proceeds to drop the main malware.

In each package, the malicious functionality is automatically triggered upon installation by means of a postinstall hook, launching a script named "install.js" that detects the victim's operating system and launches an obfuscated payload ("app.js") in a new Command Prompt (Windows), GNOME Terminal or x-terminal-emulator (Linux), or Terminal (macOS) window.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1ytY6oTBx0wybYGqzB2CXqrclYau6Ev4MoALtdt0_UvHNEuZrRQcYuPT9dg1-ebqGlmFZOpMFpQsEJjRjvQhQSoH8mVr9eWzT1W0aqd8ng_ZMyNFr379ODsuEYE_Iw93-039vnen3mrKbK4ut65-Ftmk_9WHi07BKScQ15DtDJL69QcReW95vm57kMfBD/s790-rw-e365/wire.jpg)

"By spawning a new terminal window, the malware runs independently of the npm install process," Pandya noted. "Developers who glance at their terminal during installation see a new window briefly appear, which the malware immediately clears to avoid suspicion."

The JavaScript contained within "app.js" is hidden through four layers of obfuscation -- such as XOR cipher with a dynamically generated key, URL-encoding of the payload string, and using hexadecimal and octal arithmetic to obscure program flow -- that are designed to resist analysis.

The end goal of the attack is to fetch and execute a comprehensive information stealer ("data\_extracter") from the same server that's equipped to thoroughly scan the developer's machine for secrets, authentication tokens, credentials, and session cookies from web browsers, configuration files, and SSH keys.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The stealer binary also incorporates platform-specific implementations to extract credentials from the system keyring using the [keyring npm library](https://www.npmjs.com/package/keyring). The harvested information is compressed into a ZIP archive and exfiltrated to the server.

"System keyrings store credentials for critical services including email clients (Outlook, Thunderbird), cloud storage sync tools (Dropbox, Google Drive, OneDrive), VPN connections (Cisco AnyConnect, OpenVPN), password managers, SSH passphrases, database connection strings, and other applications that integrate with the OS credential store," Socket said.

"By targeting the keyring directly, the malware bypasses application-level security and harvests stored credentials in their decrypted form. These credentials provide immediate access to corporate email, file storage, internal networks, and production databases."

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

[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Information Stealer](https://thehackernews.com/search/label/Information%20Stealer)[Malware](https://thehackernews.com/search/label/Malware)[NPM](https://thehackernews.com/search/label/NPM)[Obfuscation](https://thehackernews.com/search/label/Obfuscation)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[typosquatting](https://thehackernews.com/s...