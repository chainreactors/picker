---
title: Researchers Spot Modified Shai-Hulud Worm Testing Payload on npm Registry
url: https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html
source: The Hacker News
date: 2025-12-31
fetch_date: 2026-01-01T03:36:46.146089
---

# Researchers Spot Modified Shai-Hulud Worm Testing Payload on npm Registry

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Researchers Spot Modified Shai-Hulud Worm Testing Payload on npm Registry](https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html)

**Dec 31, 2026**Ravie LakshmananCybersecurity / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLzpeFOZHp8C7GZ0cMe57PMU10zY3RqrxkvwgczNMI5wgXFupY9-FWJ9YcOxsXyp8CS2DeqAPdzbyWgRIORNHw07bTMNOSidgkAI7CHrQ58iw8E027cxPGaxNmpQYEooO2OyRlWRe96ebuX1wSLsqOB7doUZaKELDsTn-vh3ht6Ti2RN1VTnTfsTtu13gA/s790-rw-e365/npm.jpg)

Cybersecurity researchers have disclosed details of what appears to be a new strain of Shai Hulud on the npm registry with slight modifications from the previous wave observed last month.

The npm package that embeds the novel Shai Hulud strain is "[@vietmoney/react-big-calendar](https://www.npmjs.com/package/%40vietmoney/react-big-calendar)," which was uploaded to npm back in March 2021 by a user named "hoquocdat." It was updated for the first time on December 28, 2025, to version 0.26.2. The package has been [downloaded 698 times](https://npm-stat.com/charts.html?package=%40vietmoney%2Freact-big-calendar) since its initial publication. The latest version has been downloaded 197 times.

Aikido, which spotted the package, said it has not spotted any major spread or infections following the release of the package.

"This suggests we may have caught the attackers testing their payload," security researcher Charlie Eriksen [said](https://www.aikido.dev/blog/shai-hulud-strikes-again---the-golden-path). "The differences in the code suggests that this was obfuscated again from the original source, not modified in place. This makes it highly unlikely to be a copy-cat, but was made by somebody who had access to the original source code for the worm."

The Shai-Hulud attack [first came to light](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html) in September 2025, when trojanized npm packages were found stealing sensitive data like API keys, cloud credentials, and npm and GitHub tokens, and exfiltrating them to GitHub repositories using the pilfered tokens. In the [second wave](https://thehackernews.com/2025/11/shai-hulud-v2-campaign-spreads-from-npm.html) spotted in November 2025, the repositories contained the description "Sha1-Hulud: The Second Coming."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ransomware_dragon_d)

But the most important aspect of the campaign is its ability to weaponize the npm tokens to fetch 100 other most-downloaded packages associated with the developer, introduce the same malicious changes, and push them to npm, thereby expanding the scale of the supply chain compromise in a worm-like manner.

The new strain comes with noticeable changes -

* The initial file is now called "bun\_installer.js" and the main payload is referred to as "environment\_source.js"
* The GitHub repositories to which the secrets are leaked feature the description "Goldox-T3chs: Only Happy Girl."
* The names of files that contain the secrets are: 3nvir0nm3nt.json, cl0vd.json, c9nt3nts.json, pigS3cr3ts.json, and actionsSecrets.json
* The removal of "dead man switch" that resulted in the execution of a wiper if no GitHub or npm tokens were found to abuse for data exfiltration and self-replication

Other important modifications include better error handling when TruffleHog's credential scanner times out, improved operating system-based package publishing, and tweaks to the order in which data is collected and saved.

### Fake Jackson JSON Maven Package Drops Cobalt Strike Beacon

The development comes as the supply chain security company said it identified a malicious package ("org.fasterxml.jackson.core/jackson-databind") on Maven Central that poses as a legitimate Jackson JSON library extension ("com.fasterxml.jackson.core"), but incorporates a multi-stage attack chain that delivers platform-specific executables. The package has since been taken down.

Present within the Java Archive (JAR) file is heavily obfuscated code that kicks into action once an unsuspecting developer adds the malicious dependency to their "pom.xml" file.

"When the Spring Boot application starts, Spring scans for @Configuration classes and finds JacksonSpringAutoConfiguration," Eriksen [said](https://www.aikido.dev/blog/maven-central-jackson-typosquatting-malware). "The @ConditionalOnClass({ApplicationRunner.class}) check passes (ApplicationRunner is always present in Spring Boot), so Spring registers the class as a bean. The malware's ApplicationRunner is invoked automatically after the application context loads. No explicit calls required."

The malware then looks for a file named ".idea.pid" in the working directory. The choice of the file name is intentional and is designed to blend in with IntelliJ IDEA project files. Should such a file exist, it's a signal to the malware that an instance of itself is already running, causing it to silently exit.

In the next step, the malware proceeds to check the operating system and contact an external server ("m.fasterxml[.]org:51211") to fetch an encrypted response containing URLs to a payload to be downloaded based on the operating system. The [payload](https://www.virustotal.com/gui/file/8bce95ebfb895537fec243e069d7193980361de9d916339906b11a14ffded94f/detection) is a [Cobalt Strike beacon](https://www.virustotal.com/gui/file/702161756dfd150ad3c214fbf97ce98fdc960ea7b3970b5300702ed8c953cafd/detection), a legitimate adversary simulation tool that can be abused for post-exploitation and command-and-control.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

On Windows, it's configured to download and execute a file called "svchosts.exe" from "103.127.243[.]82:8000," while a payload referred to as "update" is downloaded from the same server for Apple macOS systems.

Further analysis has revealed that the typosquatted domain fasterxml[.]org was registered via GoDaddy on December 17, 2025, merely a week before the malicious Maven package was det...