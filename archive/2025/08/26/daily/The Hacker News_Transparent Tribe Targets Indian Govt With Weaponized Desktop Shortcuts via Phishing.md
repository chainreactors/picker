---
title: Transparent Tribe Targets Indian Govt With Weaponized Desktop Shortcuts via Phishing
url: https://thehackernews.com/2025/08/transparent-tribe-targets-indian-govt.html
source: The Hacker News
date: 2025-08-26
fetch_date: 2025-10-07T00:50:48.537597
---

# Transparent Tribe Targets Indian Govt With Weaponized Desktop Shortcuts via Phishing

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

# [Transparent Tribe Targets Indian Govt With Weaponized Desktop Shortcuts via Phishing](https://thehackernews.com/2025/08/transparent-tribe-targets-indian-govt.html)

**Aug 25, 2025**Ravie LakshmananMalware / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEid4XIqtUx4dvIytbJUeM5krSLJ26aFucK4uEgLFOnOEx08v0hbzkeZ2pQWeRq2upA7ndK78jnIV0Tmv_LpV7JLOJsR2FEl5W5y57mbfqrSn3bUgg-uk1SZtLven_5sstd7jitvS3MhYQroW-5SpPm7yLvGIDsafUW_g6eEXDjHs9ZA7vThyphenhyphen8nDdM6kmxc7/s790-rw-e365/icon.jpg)

The advanced persistent threat (APT) actor known as **Transparent Tribe** has been observed targeting both Windows and BOSS (Bharat Operating System Solutions) Linux systems with malicious Desktop shortcut files in attacks targeting Indian Government entities.

"Initial access is achieved through spear-phishing emails," CYFIRMA [said](https://www.cyfirma.com/research/apt36-targets-indian-boss-linux-systems-with-weaponized-autostart-files/). "Linux BOSS environments are targeted via weaponized .desktop shortcut files that, once opened, download and execute malicious payloads."

Transparent Tribe, also called APT36, is assessed to be of Pakistani origin, with the group – along with its sub-cluster SideCopy – having a [storied](https://thehackernews.com/2025/03/apt36-spoofs-india-post-website-to.html) [history](https://thehackernews.com/2025/04/pakistan-linked-hackers-expand-targets.html) of breaking into [Indian government institutions](https://thehackernews.com/2025/07/tag-140-deploys-drat-v2-rat-targeting.html) with a variety of remote access trojans (RATs).

The latest dual-platform demonstrates the adversarial collective's continued sophistication, allowing it to broaden its targeting footprint and ensure access to compromised environments.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack chains begin with phishing emails bearing supposed meeting notices, which, in reality, are nothing but booby-trapped Linux desktop shortcut files ("Meeting\_Ltr\_ID1543ops.pdf.desktop"). These files masquerade as PDF documents to trick recipients into opening them, leading to the execution of a shell script.

The shell script serves as a dropper to fetch a hex-encoded file from an attacker-controlled server ("securestore[.]cv") and save it to disk as an ELF binary, while simultaneously opening a decoy PDF hosted on Google Drive by launching Mozilla Firefox. The Go-based binary, for its part, establishes contact with a hard-coded command-and-control (C2) server, modgovindia[.]space:4000, to receive commands, fetch payloads, and exfiltrate data.

The malware also establishes persistence by means of a cron job that executes the main payload automatically after a system reboot or process termination.

Cybersecurity company CloudSEK, which also [independently reported](https://www.cloudsek.com/blog/investigation-report-apt36-malware-campaign-using-desktop-entry-files-and-google-drive-payload-delivery) the activity, said the malware performs system reconnaissance and is equipped to carry out a series of dummy anti-debugging and anti-sandbox checks in a bid to throw off emulators and static analyzers.

Furthermore, Hunt.io's [analysis](https://hunt.io/blog/apt36-india-infrastructure-attacks) of the campaign has revealed that the attacks are designed to deploy a known Transparent Tribe backdoor called [Poseidon](https://thehackernews.com/2023/04/pakistani-hackers-use-linux-malware.html) that enables data collection, long-term access, credential harvesting, and potentially lateral movement.

"APT36's capability to customize its delivery mechanisms according to the victim's operating environment thereby increases its chances of success while maintaining persistent access to critical government infrastructure and evading traditional security controls," CYFIRMA said.

The disclosure comes weeks after the Transparent Tribe actors were observed targeting Indian defense organizations and related government entities using spoofed domains with the ultimate goal of stealing credentials and two-factor authentication (2FA) codes. It's believed that users are redirected to these URLs through spear-phishing emails.

"Upon entering a valid email ID in the initial phishing page and clicking the 'Next' button, the victim is redirected to a second page that prompts the user to input their email account password and the Kavach authentication code," CYFIRMA [said](https://www.cyfirma.com/research/apt36-a-phishing-campaign-targeting-indian-government-entities/).

It's worth noting that the targeting of Kavach, a 2FA solution used by the Indian government agencies to improve account security, is a [tried-and-tested tactic](https://thehackernews.com/2022/03/new-hacking-campaign-by-transparent.html) adopted by [Transparent Tribe and SideCopy](https://thehackernews.com/2022/12/researchers-warn-of-kavach-2fa-phishing.html) since [early 2022](https://thehackernews.com/2023/04/pakistani-hackers-use-linux-malware.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The use of typo-squatted domains combined with infrastructure hosted on Pakistan-based servers is consistent with the group's established tactics, techniques, and procedures," the company said.

The findings also follow the discovery of a [separate campaign](https://strikeready.com/blog/apt-android-phishing-microsoft/) undertaken by a South Asian APT to strike Bangladesh, Nepal, Pakistan, Sri Lanka, and Turkey through spear-phishing emails that are engineered for credential theft using lookalike pages hosted on Netlify and Pages.dev.

"These campaigns mimic official communication to trick victims into entering credentials on fake login pages," Hunt.io [said](https://hunt.io/blog/apt-sidewinder-netlify-government-phishing) earlier this month, attributing it to a hacking group called [SideWinder](https://thehackernews.com/2025/05/south-asian-ministries-hit-by.html).

"Spoofed Zimbra ...