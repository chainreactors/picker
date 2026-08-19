---
title: 16 Typosquatted RubyGems Packages Steal Browser Credentials and Crypto Wallets
url: https://thehackernews.com/2026/08/16-typosquatted-rubygems-packages-steal.html
source: The Hacker News
date: 2026-08-18
fetch_date: 2026-08-19T03:00:29.381679
---

# 16 Typosquatted RubyGems Packages Steal Browser Credentials and Crypto Wallets

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [16 Typosquatted RubyGems Packages Steal Browser Credentials and Crypto Wallets](https://thehackernews.com/2026/08/16-typosquatted-rubygems-packages-steal.html)

**Ravie Lakshmanan**Aug 18, 2026Cryptocurrency / Open Source

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9BsXf9I7m4IoC0hb3fSwYiBJsaB1_vSj9kGhfi0HsWGeR0xVl_W1O_Z0bd6IxvQ-vUQP5FDsj5mpiwUjv72JG3vNdViDwAKDG1uswOPDfb84xN_n8AgafhIP2sCx8x1Jd4L0mptrXuzCCGze-safV0V13WiWsFbKrKYvIC6CPBncYuhwgaDafyqSJx9Kv/s1700-e365/ruby.jpg)

Cybersecurity researchers have flagged a new typosquatting campaign targeting RubyGems users with a Windows-based information stealer.

OpenSourceMalware, which [discovered](https://opensourcemalware.com/blog/stubmaker-rubygems-windows-infostealer) the activity on August 15, 2026, is tracking the threat under the moniker **StubMaker**. The [complete list of packages](https://opensourcemalware.com/?search=%23stubmaker) published as part of the campaign is below -

* ubnuler
* ubnlder
* ri18nr
* reaker
* rakier
* orakw
* joxn
* ise18n
* ioe18n
* ie18u
* iai8n
* i1l8n
* i18om
* activesupmport
* brumdler
* brundlef

"This new malware harvests browser credentials, cryptocurrency wallets, seed phrases, and Telegram data," security researcher Paul McCarty (aka 6mile) said. "All of the malicious RubyGems packages appear to be typosquats of popular Ruby dependencies, but rather than the clever SEO-fueled typosquats we've seen from other threat actors (e.g., events-channel imitating the popular Node.js events module), they're all clumsy typos."

The 16 gems have been published by users named "[mod8rz41mje](https://rubygems.org/profiles/mod8rz41mje)" (aka Riley Miller) and "[rbq95bwt6q](https://rubygems.org/profiles/rbq95bwt6q)" (aka Alex Davis). As of writing, the packages have been yanked from RubyGems.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

In at least two cases – brumdler and brundlef – the threat actor has been found to take advantage of a known RubyGems behavior that makes a namespace available for anyone to claim once all versions of a gem have been yanked. In both instances, the packages were originally published by "gemlewqqhu1" (aka Taylor Moore) before they were reclaimed by the aforementioned two accounts.

Jenn Gile, co-founder of OpenSourceMalware, told The Hacker News that although the campaign was disrupted fairly early, it became more effective because of Ruby's "poor design choices" via package name reuse and an unvalidated author field.

"When one of the malicious gems was yanked, the threat actor was able to spin up a new owner account and publish a new malicious version under the same package name," Gile said. "What should have been forever dead was revived to compromise more people."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgM4iiHHG2JIYuXsQ-KejNjlvLkAT5mfeZImAWK8CY642m5V3Yjsjq8tyPj3TmV2QydmKtbBYRC8-UDQeTNPiMwrz2SrBpooFAQS0D6gBdBeIp3A0nqNqlRoqQKEUAQ_Muc8QfpfQtVD44TfP-uPBiXf2OqZBCmPahA1Hg5XbyeMJ5qJ89ML-hPuMWGzZpG/s1700-e365/table.jpeg)

"The attacker assigned a different 'Author' name for each gem in an attempt to make them look unrelated, even though they all came from the same owner account. This is because the Author field is a totally unvalidated plaintext field. It doesn't have to match the Owner or anything else."

The attack chain, at a high level, makes use of an "extconf.rb" hook to trigger the execution hook. Similar to [npm's lifecycle hooks](https://docs.npmjs.com/cli/v8/using-npm/scripts), "extconf.rb" is [run automatically](https://guides.rubygems.org/gems-with-extensions/) when a user installs a gem. The file is typically used to configure native extensions written in C, C++, or Rust that are bundled inside a Ruby package within the "ext/" directory and compiled during installation of the gem.

In the case of StubMaker, the Ruby hook acts as a conduit to fetch a 22 MB Rust-based loader from a GitHub release, which, in turn, launches a Go-based stealer ("wincfg") payload embedded into it. The GitHub account ("github[.]com/bebraz1") is no longer accessible.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRw-VPAjgsGgx3eKz3zakFKegvv_CfSO4I_nxIFlpu7wYV3HTFQ94ZXl1HEdp2iaK9LcVB9VLwpnS1PiIVkZwp29U7Tuc7DQSnGyehvg_GBi_7lcTWuspvbU9aFU7v74eLDBiVoJRbrm5v-R1R5h4kiYGkdhiy3c7EfJQr6rDPTq7_-YJ8pOjKuHUt3PVs/s1700-e365/193.png)

The stealer, for its part, incorporates a DLL payload ("abe\_payload.dll") that's used to extract credentials from Chromium-based web browsers (i.e., Google Chrome, Microsoft Edge, Brave, Opera, Opera GX, Vivaldi, Yandex, Avast, AVG, and CCleaner Browser) by circumventing app-bound encryption ([ABE](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)) protections added by Google.

It also collects extension data, browsing history, and payment card numbers; searches for cryptocurrency wallets and seed phrases; extracts Telegram Desktop data; gathers system information; and makes an external request to "api.ipify[.]org" to obtain the victim's public IP address.

Once the relevant data is captured, it's uploaded to Gofile in the form of a password-protected ZIP archive and the resulting download link is sent to the threat actor ("dresslee.com") over an unencrypted HTTP channel.

"StubMaker doesn't build anything — it generates a Makefile with empty all, install, and clean targets, plus Unix and Windows stub scripts that do nothing but return success, so the extension phase reports a clean build while the real work (the platform beacon, the Windows loader fetch and execution) happens in the installer hook itself," McCarty explained.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"The name points at that specific move: manufacturing a fake build toolchain to make a malicious install look like a routine one, rather than just describing another ty...