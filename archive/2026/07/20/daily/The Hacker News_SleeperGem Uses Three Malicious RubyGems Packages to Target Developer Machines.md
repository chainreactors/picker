---
title: SleeperGem Uses Three Malicious RubyGems Packages to Target Developer Machines
url: https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html
source: The Hacker News
date: 2026-07-20
fetch_date: 2026-07-21T05:03:17.794213
---

# SleeperGem Uses Three Malicious RubyGems Packages to Target Developer Machines

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [SleeperGem Uses Three Malicious RubyGems Packages to Target Developer Machines](https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html)

**Ravie Lakshmanan**Jul 20, 2026Malware / Application Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-5_crP04CVdna-erTGX9yykCNwqzeIcMALrWcRvgKWkfk7bntEBg50PBtoLvTeACMEHisZ-m1FLMEa2x9nbsRpVdAyeQyBkEmexn8p6W4r6JKA7dxDGJ6BXCqR6RYC3hyRSw7_1Wm1Elv-UFHRfttZQB0HX60SQRGXnJ-4VySo4gY-yfaDhT2FHKHTFj9/s1700-e365/ruby.jpg)

Cybersecurity researchers have flagged a new software supply chain attack codenamed SleeperGem targeting the Ruby ecosystem after three malicious gems were published to RubyGems with the end goal of serving additional payloads.

The rogue gems are listed below -

* [git\_credential\_manager](https://rubygems.org/gems/git_credential_manager) (versions 2.8.0, 2.8.1, 2.8.2, 2.8.3) - Published on July 18, 2026
* [Dendreo](https://rubygems.org/gems/Dendreo) (versions 1.1.3, 1.1.4) - Published on October 14, 2017
* [fastlane-plugin-run\_tests\_firebase\_testlab](https://rubygems.org/gems/fastlane-plugin-run_tests_firebase_testlab) (version 0.3.2) - Published on February 06, 2018

"Each malicious release is a loader," StepSecurity [said](https://www.stepsecurity.io/blog/sleepergem-compromised-rubygems-drop-persistent-backdoor) in an analysis. "It fetches a second stage from an attacker controlled Forgejo host, checks whether it is running in a build system and skips if it is, and on a developer machine it drops a native daemon and installs persistence."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

One aspect of the attack that immediately stands out is that "git\_credential\_manager" impersonates the official Microsoft Git Credential Manager, while the other two had been dormant for years before receiving the malicious updates. "Dendreo" was last updated on October 24, 2020, and "fastlane-plugin-run\_tests\_firebase\_testlab" stayed inactive since March 9, 2019, prior to the new versions.

Another defining trait of the activity is that the releases were published directly to the registry without any matching commit or tag in the source projects.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhaj8eoxZV_tZL3Ot7vqAo5oTmu3E5ujjNCWLlQCtU5-DX2ManqJSbtZHi3YBvJNi9Y7GTFxeq8IiQTK9BsbqOG6IZW_YQzMA4PGQbEoPkmOmJ2EbwzNinTSd3z7KU4uE2h9DB6mdB-IrvmBlGcnB3ZnefkcHvQmvkuYE2aNlxb0i-l2VMLjcuBdbMp5iE/s1700-e365/ruby-1.png)

Interestingly, "git\_credential\_manager" has been [added](https://rubygems.org/gems/git_credential_manager/reverse_dependencies) as a dependency to five packages, including "Dendreo" and "fastlane-plugin-run\_tests\_firebase\_testlab," effectively allowing the malicious payload to spread to existing users of the packages -

* Dendreo
* fastlane-plugin-run\_tests\_firebase\_testlab
* slackHtmlToMarkdown
* seo\_optimizer
* array\_fast\_methods

All the aforementioned packages, with the exception of "fastlane-plugin-run\_tests\_firebase\_testlab," are maintained by the same account ("[LR-DEV](https://rubygems.org/profiles/LR-DEV)"). The fact that the gem belongs to a different maintainer ("[pinkroom](https://rubygems.org/profiles/pinkroom)") indicates that more than one account was likely compromised to push the rogue versions to RubyGems.

Once installed, the malware embedded in these packages scans the infected system for about 30 environment variables, including those related to GitHub Actions, GitLab, CircleCI, Travis, Jenkins, and Vercel. If any of those are identified, it promptly exits. The check is assessed to be an intentional attempt to avoid running on ephemeral CI runners and ensure it's executed on a developer machine.

In the case of "git\_credential\_manager," the malicious code is fired when the library is required, causing it to download two payloads from a public Forgejo instance ("git.disroot[.]org/git-ecosystem"): a shell script ("deploy.sh") and a native binary that carries the same name as the tool the gem masquerades as. On Windows, the retrieved payload is executed via PowerShell.

While version 2.8.2 merely stages the payloads, version 2.8.3 of the gem moves to the next phase of the attack. This involves using the install script to launch the binary as a background daemon, after which it establishes persistence using a cron entry and as a systemd user service and queries the sudo and wheel groups.

"If the user can run sudo without a password, the script re-runs itself as root, and when it runs as root it plants a setuid root copy of the system shell at a path chosen to mimic a networking utility," StepSecurity said.

Users who have installed any of the aforementioned gems are advised to treat the machines and associated secrets as compromised. It's also recommended to remove the dropped daemon at "~/.local/share/gcm/," erase the persistence methods, check for a setuid shell at "/usr/local/sbin/ping6," and rotate all credentials.

"A RubyGems account that has gone quiet for six or seven years doesn't look risky to anyone," Aikido Security researcher Charlie Eriksen [said](https://www.aikido.dev/blog/sleepergem-rubygems-supply-chain-attack). "That's exactly the profile worth taking over. That's where the SleeperGem name comes from: not a planted, long-game attacker asset, but a real, ordinary account that had simply gone dormant, and looked harmless enough to hijack without anyone noticing."

### RubyGems as a Data Exfiltration Dead Drop

The disclosure comes more than two months after RubyGems [briefly paused](https://thehackernews.com/2026/05/rubygems-suspends-new-signups-after.html) account sign-ups after bad actors pushed dozens of malicious packages as part of a coordinated spam-publishing campaign. Around the same time, Socket researchers [flagged](https://thehackernews.com/2026/05/gemstuffer-abuses-150-rubygems-to.html) a parallel campaign that flooded the registry with ...