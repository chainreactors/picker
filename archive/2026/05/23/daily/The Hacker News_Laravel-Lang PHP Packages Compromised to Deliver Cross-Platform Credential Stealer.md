---
title: Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer
url: https://thehackernews.com/2026/05/laravel-lang-php-packages-compromised.html
source: The Hacker News
date: 2026-05-23
fetch_date: 2026-05-24T06:01:18.484716
---

# Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer](https://thehackernews.com/2026/05/laravel-lang-php-packages-compromised.html)

**Ravie Lakshmanan**May 23, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkqwlAgmL-HrE2pSx8xqfY4-AyYZ59wK4x5AWtnCXSHRoBO1wcYTpWw42Fe6VRoAT77e914MSqZW56fKX95IueHTCrk10XNn2Yxh7CU8iCdX5lzFowGeVkolW-4E3po81w9pFMsaLR_r85abtUv3bwvQMa6pP1BAiSj4DrmapTiYr1twfV61tvGdWJRgs8/s1700-e365/lang-hack.jpg)

Cybersecurity researchers have flagged a fresh software supply chain attack campaign that has targeted multiple PHP packages belonging to Laravel-Lang to deliver a comprehensive credential-stealing framework.

The affected packages include -

* laravel-lang/lang
* laravel-lang/http-statuses
* laravel-lang/attributes
* laravel-lang/actions

"The timing and pattern of the newly published tags point to a broader compromise of the Laravel Lang organization's release process, rather than a single malicious package version," Socket [said](https://socket.dev/blog/laravel-lang-compromise). "The tags were published in rapid succession on May 22 and May 23, 2026, with many versions appearing only seconds apart."

More than 700 versions associated with these packages have been identified, indicating automated mass tagging or republishing. It's suspected that the attacker may have managed to obtain access to organization-level credentials, repository automation, or release infrastructure.

The core malicious functionality is located in a file named "src/helpers.php" that's embedded into the version tags. It's mainly designed to fingerprint the infected host and contact an external server ("flipboxstudio[.]info") to retrieve a PHP-based cross-platform payload that runs on Windows, Linux, and macOS.

"The attacker added src/helpers.php to the autoload.files map in each compromised package," StepSecurity [said](https://www.stepsecurity.io/blog/laravel-lang-supply-chain-attack). "Because every Laravel application calls require \_\_DIR\_\_.'/vendor/autoload.php' on startup, and because Symfony, PHPUnit, and most other PHP frameworks do the same, the payload runs the moment any consumer of the package boots. No class instantiation, no method call, no special trigger is required."

According to Aikido Security, the dropper delivers a Visual Basic Script launcher on Windows and runs it via cscript. On Linux and macOS, it executes the stealer payload via exec().

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"Because this file ['src/helpers.php'] is registered in the composer.json under autoload.files, the backdoor is executed automatically on every PHP request handled by the compromised application," Socket explained.

"The script generates a unique per-host marker (an MD5 hash combining the directory path, system architecture, and inode) to ensure the payload only triggers once per machine. This prevents redundant executions and helps the malware remain undetected after the initial run."

The stealer is equipped to harvest a wide range of data from compromised systems and exfiltrate it to the same server. This includes -

* IAM roles and instance identity documents by querying cloud metadata endpoints
* Google Cloud application default credentials
* Microsoft Azure access tokens and service principal profiles
* Kubernetes Service Account tokens and Helm registry configurations
* Authentication tokens for DigitalOcean, Heroku, Vercel, Netlify, Railway and Fly.io
* HashiCorp Vault tokens
* Tokens and configurations from Jenkins, GitLab Runners, GitHub Actions, CircleCI, TravisCI, and ArgoCD
* Seed phrases and files associated with cryptocurrency wallets (Electrum, Exodus, Atomic, Ledger Live, Trezor, Wasabi, and Sparrow) and extensions (MetaMask, Phantom, Trust Wallet, Ronin, Keplr, Solflare, and Rabby)
* Browser history, cookies, and login data from Google Chrome, Microsoft Edge, Mozilla Firefox, Brave, and Opera by using a Base64-encoded embedded Windows executable that bypass Chromium's app-bound encryption ([ABE](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)) protections
* Local vaults and browser extension data for 1Password, Bitwarden, LastPass, KeePass, Dashlane, and NordPass
* PuTTY/WinSCP saved sessions
* Windows Credential Manager dumps
* WinSCP saved sessions
* RDP files
* Session tokens associated with applications like Discord, Slack, and Telegram
* Data from Microsoft Outlook, Thunderbird, and popular FTP clients (FileZilla, WinSCP, and CoreFTP)
* Configuration and credential files containing Docker auth tokens, SSH private keys, Git credentials, shell history files, database history files, Kubernetes cluster configurations, .env files, wp-config.php, and docker-compose.yml
* Environment variables loaded into the PHP process
* Source control credentials from global and local .gitconfig files, .git-credentials, and .netrc files
* VPN configuration and saved login files for OpenVPN, WireGuard, NetworkManager, and commercial VPNs such as NordVPN, ExpressVPN, CyberGhost, and Mullvad

"The fetched payload is a ~5,900 line PHP credential stealer, organised into fifteen specialist collector modules," Aikido researcher Ilyas Makari [said](https://www.aikido.dev/blog/supply-chain-attack-targets-laravel-lang-packages-with-credential-stealer). "After collecting everything it can find, it encrypts the results with AES-256 and sends them to flipboxstudio[.]info/exfil. It then deletes itself from the disk to limit forensic evidence."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link...